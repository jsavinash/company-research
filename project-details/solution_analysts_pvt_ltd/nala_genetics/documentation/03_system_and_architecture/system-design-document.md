# System Design Document

## 1. Context

This document specifies the as-built design of the confidence-scored variant triage layer for Nala CDS, scoped to the 2017–2018 toolchain. It complements `../01-business-and-strategy/high-level-solution-overview.md` (business view).

## 2. Goals & non-goals

**Goals:** calibrated, auditable variant triage; human review of uncertain cases; low curator time; integration with Nala CDS.

**Non-goals:** variant calling, somatic calling, PRS, final report sign-out, PGx star-alleles.

## 3. Component design

| Stage | Component | Technology | Responsibility |
|---|---|---|---|
| 1 | Annotation | Ensembl VEP, dbNSFP, SnpEff | Consequence, in-silico, frequency, constraint, ClinVar |
| 2 | Feature assembly | Python + pandas | ~40–60 interpretable features |
| 3 | Supervised classifier | XGBoost / LightGBM / scikit-learn | Rank variants |
| 4 | Literature triage | TF-IDF/LSA → ULMFiT / ELMo | Relevance scoring over ClinVar + PubMed |
| 5 | Evidence synthesis | Deterministic rules + model | ACMG code mapping + provenance |
| 6 | Triage + routing | Rule engine | Prioritize / queue / abstain |
| 7 | Serving | Flask + gunicorn, Redis | API + async |
| 8 | Review UI | Server-rendered + JS | Curator queue |

## 4. Data flow

1. **Ingest** — VCF + panel.
2. **Annotate** — VEP + dbNSFP + gnomAD/ExAC + ClinVar.
3. **Features** — interpretable feature vector.
4. **Classify** — XGBoost/GBM → raw score.
5. **Calibrate** — per-ancestry isotonic → P(pathogenic).
6. **Literature triage** — TF-IDF/LSA → ULMFiT/ELMo.
7. **Synthesize** — ACMG codes with provenance.
8. **Route** — per-consequence thresholds; abstain where insufficient.
9. **Curator review** — accept/override/reject → label.

## 5. Component notes

- **Annotation:** VEP is the backbone; deterministic, documented, fast. ML sits in stages 3–5, not here.
- **Feature assembly:** keep features interpretable (a clinical tool that can't be explained won't be trusted). ~40–60 features: allele frequency (global + per-superpopulation), in-silico scores, conservation, gene constraint, domain membership, variant type, position, ClinVar assertion + review status.
- **Classifier:** gradient-boosted trees, not deep learning. Tabular variant features with moderate sample sizes are exactly where GBM wins; interpretability is a regulatory asset.
- **Calibration:** raw scores are not probabilities; isotonic regression on a held-out set; report ECE. A confidently wrong variant is more dangerous than an abstained one.
- **Literature triage:** two-stage — cheap TF-IDF/LSA retrieval to shortlist abstracts, then a ULMFiT or ELMo-based classifier to score relevance to the specific gene–variant–disease question. ULMFiT (Jan–May 2018) and ELMo (Feb 2018) are inside the window; BERT is not.
- **Evidence synthesis:** map signals to ACMG codes deterministically where rules are explicit (BA1/BS1 from frequency, PVS1 from consequence); use model output only to *prioritize* where rules are ambiguous. Never let the model assert a code without a human-visible reason.
- **Abstention:** the system must be able to say "insufficient evidence." The single most important design property.

## 6. Deployment topology

- **Single new deployable** (triage service) behind the existing Nala CDS API.
- **Components:** Flask + gunicorn API, Redis queue, PostgreSQL (curator actions/audit), S3 (snapshots).
- **Review UI:** server-rendered + small JS.
- **Cloud:** AWS ap-southeast-1.

## 7. Key design decisions

See `decision-log.md` and `architecture-decision-records/`.

## 8. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Confidently wrong classification | Calibration + mandatory abstention; category-4 tracking |
| ClinVar label noise | Filter by review status; internal curations as gold |
| Ancestry bias | Per-ancestry calibration; ancestry-disjoint evaluation |
| Gene memorization | Gene-disjoint splits |
| Review queue bottleneck | ≤ 90 s/variant; per-consequence thresholds |
| QMS exposure | ISO 13485 traceability; no autonomous classification |

## 9. Related

- `../02-product-and-ux/product-requirements-doc.md`
- `non-functional-requirements.md`
- `integration-and-data-strategy.md`