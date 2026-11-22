# Project Scope and SLA

## 1. In scope

- **Input:** germline VCF (WES or WGS) + gene panel definition; optionally array calls for PGx loci
- **Variant scope:** rare coding variants (missense, nonsense, frameshift, canonical splice) in panel genes
- **Outputs per variant:**
  - Ranked triage score (0–1)
  - Calibrated confidence that the variant is P/LP
  - ACMG-aligned evidence code suggestions (PVS1, PS1–PS4, PM1–PM6, PP1–PP5, BA1, BS1–BS4)
  - Supporting evidence list (population frequency, in-silico, domain, clinical database hits)
  - Literature references with relevance scores
  - **Explicit abstention** where evidence is insufficient
- **Human interface:** curator review queue (accept/override/reject), all actions logged as labels

## 2. Out of scope

- Variant calling from reads (DeepVariant / GATK territory)
- Somatic variant calling / tumour-only workflows
- Polygenic risk score computation (separate module)
- Final clinical report generation and sign-out
- Pharmacogenomic star-allele calling

## 3. Explicit non-goals

- **No autonomous classification.** Every output is decision-support for a qualified curator (ISO 13485).
- **No claim of diagnostic accuracy.** The system ranks and explains; it does not diagnose.
- **No training on identifiable patient genomes without governance.** De-identified, consent-covered data only.

## 4. Stakeholders

| Stakeholder | Role |
|---|---|
| Curators | Primary users (review queue) |
| Clinical leadership | Accuracy, ISO 13485, sign-out |
| Bioinformatics | Pipeline + models |
| Data governance / privacy | UU PDP, PDPA compliance |
| Product (Nala CDS) | Platform direction |

## 5. SLAs

| Service | SLA | Measurement |
|---|---|---|
| Triage API response | p95 ≤ 3 s per variant batch | Service logs |
| Curator review time | Median ≤ 90 s/variant | Queue metrics |
| Top-20 recall | ≥ 0.90 | Eval harness |
| Calibration error (ECE) | ≤ 0.05 | Eval harness |
| VUS reduction | ↓ 30% vs. baseline | Shadow measurement |
| Availability | 99.5% | Uptime monitoring |

## 6. Constraints & dependencies

- **Period-accurate tooling (2017–2018):** no BERT (Oct 2018 postdates tenure), no LLMs.
- **Ancestry data:** per-superpopulation frequency features.
- **Governance:** de-identified data, consent, no cross-border transfer of identifiable genomes.
- **QMS:** ISO 13485 traceability, model versioning.
- **Cloud:** AWS ap-southeast-1 (matches existing deployment).

## 7. Change control

Scope changes require a decision-log entry and, if architectural, a new ADR. SLA changes require sign-off from clinical leadership.