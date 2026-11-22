# Project Documentation — Confidence-Scored Variant Triage for Nala CDS

**Working title:** `nala-variant-triage`
**Company context:** NalaGenetics Pte. Ltd. — Nala Clinical Decision Support (CDS) platform
**Author tenure:** May 2017 – Jul 2018 (1 yr 3 mos), AI Engineer — Variant Interpretation
**Documentation date:** 2026-11-21
**Status:** Retrospective project spec — reconstructs a buildable May 2017 – Jul 2018 system

---

## 1. Summary

This document specifies a **confidence-scored variant triage layer** for Nala CDS: a supervised system that ranks germline variants for clinical review, attaches ACMG-aligned evidence codes and calibrated confidence to each, and routes uncertain cases to a human curator queue.

**Thesis:** the company's own stated structural problem is not sequencing throughput but *interpretation underrepresentation*. Southeast Asia contributes a small fraction of global genomic reference data, which produces elevated variants of uncertain significance, poorly transferring polygenic scores, and miscalibrated screening (§7.2). A triage layer that prioritizes the right variants for expert review converts that bottleneck from a headcount problem into a ranking problem.

**Positioning against the period's headline technology:** DeepVariant (Google Brain, open-sourced Dec 2017) solved *variant calling* — turning reads into a VCF. It does not solve *variant interpretation*. This project targets the gap directly downstream of it.

---

## 2. Problem Statement

### 2.1 The business problem

NalaGenetics sells a platform, not just kits. §2.2 identifies Nala CDS as "the actual strategic asset": NGS analysis at scale, a PGx module covering 35 genes and 300+ gene–drug interactions, 10+ polygenic risk scores normalized on Asian datasets, and ACMG-aligned inherited disease and carrier screening. §6.3 credits the company with "AI/ML models and an Asian-enriched knowledge base."

The operational bottleneck is **variant review**. A clinical exome or genome produces tens of thousands of variants; ACMG/AMP classification (Richards et al., 2015) is a manual, expert-driven, multi-step process. For a company targeting 10,000-genome national programs (BGSi, §6.2) and 1,500-patient implementation studies (PRECISE-CIP), manual curation does not scale, and the VUS rate is the metric that determines both clinical utility and clinician trust.

### 2.2 Why this is the right intervention

§7.2 names the problem precisely: elevated variants of uncertain significance, polygenic scores that transfer poorly across ancestries, screening calibrated to non-representative populations. Each is an interpretation failure, not a wet-lab failure.

The research file also notes (§6.2) that the company's most credible reference case — the HLA-B*13:01 leprosy screening program — is fundamentally an **interpretation-to-action** success: identify a biomarker, classify it, act. That workflow is generalizable, and it is exactly where an ML triage layer adds value.

### 2.3 Why this was buildable in May 2017 – Jul 2018

| Capability | Availability in window | Use in this project |
|---|---|---|
| Variant effect annotation | Mature (Ensembl VEP, SnpEff, ANNOVAR) | Feature source |
| In-silico predictors | SIFT, PolyPhen-2, CADD, REVEL (2016) | Features |
| Population frequency | 1000 Genomes Phase 3 (2015), ExAC (2016) | Features |
| Gradient-boosted trees | XGBoost, LightGBM, scikit-learn | Primary classifier |
| Calibrated probabilities | Isotonic / Platt scaling | Confidence |
| Deep variant calling | DeepVariant (Dec 2017), Clairvoyante (May 2018) | Upstream dependency, not core |
| Text classification | CNN (Kim 2014), fastText (2016), **ULMFiT (Jan–May 2018)**, **ELMo (Feb 2018)** | Literature triage |
| Generative text | GPT-1 (Jun 2018) — research only | **Excluded** |

**Not available:** BERT (Oct 2018), which postdates the tenure by three months. The system is deliberately designed around ULMFiT/ELMo-era transfer learning, not BERT.

---

## 3. Scope

### 3.1 In scope

- **Input:** germline VCF (WES or WGS) plus a gene panel definition; optionally array calls for PGx loci
- **Variant scope:** rare coding variants (missense, nonsense, frameshift, canonical splice) in panel genes
- **Outputs per variant:**
  - Ranked triage score (0–1)
  - Calibrated confidence that the variant is pathogenic/likely pathogenic
  - ACMG-aligned evidence code suggestions (PVS1, PS1–PS4, PM1–PM6, PP1–PP5, BA1, BS1–BS4)
  - Supporting evidence list (population frequency, in-silico, domain, clinical database hits)
  - Literature references with relevance scores
  - **Explicit abstention** where evidence is insufficient
- **Human interface:** curator review queue with accept/override/reject, all actions logged as labels

### 3.2 Out of scope

- Variant calling from reads (DeepVariant / GATK territory)
- Somatic variant calling and tumour-only workflows
- Polygenic risk score computation (separate module; see §11)
- Final clinical report generation and sign-out
- Pharmacogenomic star-allele calling (see §11 runner-up)

### 3.3 Non-goals

- **No autonomous classification.** Every output is decision-support for a qualified curator. This is a hard requirement under ISO 13485 (§6.4) and the company's clinical positioning.
- **No claim of diagnostic accuracy.** The system ranks and explains; it does not diagnose.
- **No training on identifiable patient genomes without governance.** De-identified, consent-covered data only.

---

## 4. System Architecture (May 2017 – Jul 2018 buildable)

```
  VCF (WES/WGS)
        │
        ▼
  ┌─────────────────────────────────────────────────────┐
  │ 1. Annotation layer                                  │
  │    Ensembl VEP  →  consequence, protein change       │
  │    dbNSFP       →  SIFT, PolyPhen-2, CADD, REVEL     │
  │    gnomAD/ExAC  →  population allele frequencies     │
  │    gnomAD constraint (pLI, LOEUF)                    │
  │    ClinVar      →  existing classifications          │
  └───────────────────┬─────────────────────────────────┘
                      │
        ┌─────────────▼─────────────┐
        │ 2. Feature assembly       │
        │    ~40-60 interpretable   │
        │    features per variant   │
        └─────────────┬─────────────┘
                      │
     ┌────────────────┴────────────────┐
     ▼                                 ▼
┌──────────────────────┐   ┌──────────────────────────┐
│ 3. Supervised        │   │ 4. Literature evidence    │
│    classifier        │   │    retrieval + triage     │
│    XGBoost / GBM     │   │    ClinVar + PubMed       │
│    → raw score       │   │    TF-IDF + LSA baseline  │
│    → isotonic        │   │    → ULMFiT / ELMo text   │
│      calibration     │   │      relevance classifier │
└──────────┬───────────┘   └────────────┬─────────────┘
           │                            │
           └─────────────┬──────────────┘
                         ▼
        ┌────────────────────────────────────┐
        │ 5. Evidence synthesis              │
        │    map signals → ACMG codes        │
        │    compute calibrated P(pathogenic)│
        │    attach provenance for each code │
        └────────────────┬───────────────────┘
                         ▼
        ┌────────────────────────────────────┐
        │ 6. Triage + routing                │
        │    score ≥ τ_high → prioritize     │
        │    score ≤ τ_low  → deprioritize   │
        │    between        → curator queue  │
        │    insufficient   → explicit VUS   │
        └────────────────┬───────────────────┘
                         ▼
        ┌────────────────────────────────────┐
        │ 7. Curator review queue (UI)       │
        │    variant + evidence + code       │
        │    suggestions + confidence        │
        │    accept / override / reject      │
        │    → every action becomes a label  │
        └────────────────────────────────────┘
```

### 4.1 Component notes

**Annotation.** VEP is the backbone; it is deterministic, well-documented and fast. This is not where the ML lives, and pretending otherwise would be a mistake. The ML sits in stages 3–5.

**Feature assembly.** Keep features interpretable — a clinical tool whose predictions cannot be explained will not be trusted by curators or regulators. Roughly 40–60 features: allele frequency (global and per-superpopulation), in-silico scores, conservation, gene constraint, domain membership (Pfam/InterPro), variant type, position relative to transcript, ClinVar assertion and review status.

**Classifier.** Gradient-boosted trees, not deep learning. Tabular variant features with moderate sample sizes are exactly the regime where GBM wins, and the interpretability is a regulatory asset. Deep learning would add cost and opacity without measurable gain at this scale.

**Calibration.** Raw scores are not probabilities. Isotonic regression on a held-out set, reported with expected calibration error. A confidently wrong variant is more dangerous than an abstained one.

**Literature triage.** Two-stage: cheap TF-IDF/LSA retrieval to shortlist candidate abstracts, then a ULMFiT or ELMo-based classifier to score relevance to the specific gene–variant–disease question. ULMFiT (Jan–May 2018) and ELMo (Feb 2018) are both inside the tenure window and are the correct period choice. BERT is not.

**Evidence synthesis.** Map signals to ACMG codes deterministically where the rules are explicit (BA1/BS1 from frequency thresholds, PVS1 from consequence class), and use model output only to *prioritize* where the rules are ambiguous. Never let the model assert a code without a human-visible reason.

**Abstention.** The system must be able to say "insufficient evidence." This is the single most important design property and maps directly to the VUS problem.

---

## 5. Data Strategy

### 5.1 Label sources

| Source | Label value | Notes |
|---|---|---|
| ClinVar (2017–2018 release) | P/LP vs B/LB assertions | Noisy; filter by review status (expert panel, multiple submitters) |
| Nala's own curated reports | Final classifications | Highest fidelity, smallest volume |
| Published cohort studies | Variant-level assertions in papers | Useful for under-represented genes |
| HGMD / OMIM | Disease-gene relationships | Feature, not label |
| gnomAD / ExAC | Population frequency | Feature |

### 5.2 The ancestry problem

This is the project's differentiator. Standard variant classifiers are trained and calibrated on European-ancestry data. Allele frequencies, LD structure, and the distribution of benign variation differ materially in South and Southeast Asian populations — the company's entire localization thesis (§7.2) rests on this.

Therefore:

1. **Per-ancestry frequency features**, not a single global AF.
2. **Ancestry-stratified calibration.** One isotonic calibrator per superpopulation, or a model with ancestry as an explicit feature.
3. **Evaluate transfer explicitly.** Measure how much a European-calibrated model degrades on East/South Asian variants. That number *is* the business case for the project.

### 5.3 Governance constraints

- De-identified data only; consent coverage verified before inclusion
- No cross-border transfer of identifiable genomes without the governance path in §7.4 of the research file (UU PDP, PDPA)
- Every training and evaluation run logged for ISO 13485 traceability
- Model versions and training data snapshots retained alongside reports they informed

---

## 6. Evaluation

### 6.1 Metrics

| Metric | Definition | Target |
|---|---|---|
| **VUS reduction** | Fraction of VUS reclassified after triage + curator review | **↓ 30% vs. baseline** |
| Top-20 recall | Of known P/LP variants, fraction ranked in top 20 | ≥ 0.90 |
| Precision@20 | Of top-20 ranked, fraction truly P/LP | ≥ 0.70 |
| Calibration error (ECE) | Expected calibration error | ≤ 0.05 |
| Abstention rate | Variants routed to explicit VUS | Report, do not minimize |
| Curator time per variant | Median review time | ≤ 90 s |
| Ancestry transfer gap | Performance delta, European vs. Asian calibrated | **Report as headline** |

**The headline metric is VUS reduction.** Ranking quality is a means. If curators cannot reclassify more variants in less time, the project has not paid for itself.

### 6.2 Evaluation protocol

- **Temporal split.** Train on classifications available before date T; evaluate on those after. Never random-split, which leaks future knowledge.
- **Gene-disjoint split.** A classifier that memorizes gene identity is useless on a new panel. Hold out entire genes.
- **Ancestry-disjoint evaluation.** Report separately for each superpopulation.
- **Curator-in-the-loop ablation.** Measure VUS reduction with and without the triage layer to isolate its contribution.

### 6.3 Error analysis

Every failure attributed to one of:

1. Annotation error (bad VEP transcript or consequence)
2. Feature error (stale population frequency, wrong build)
3. Model error (classifier ranked a benign variant highly)
4. Calibration error (confidently wrong — most dangerous)
5. Evidence error (literature triage surfaced irrelevant papers)
6. Label error (ClinVar assertion was wrong)

Category 4 is tracked separately and reviewed at every model release.

---

## 7. Human-in-the-Loop Design

**Curator sees:**
- Variant in genomic and protein context (gene, transcript, HGVS, consequence)
- Ranked score + calibrated confidence
- The top contributing features, in plain language
- Suggested ACMG codes, each with its supporting evidence and provenance
- Literature excerpts with relevance scores
- Population frequencies by superpopulation
- A visible abstention reason where applicable

**Curator actions:** accept suggestion / override with reason / reject / mark insufficient evidence.

**Requirement:** every action is a training label with the curator's rationale. Median review ≤ 90 seconds. If review is slower than reading ClinVar manually, the system has failed regardless of its metrics.

---

## 8. Technology Stack (May 2017 – Jul 2018)

| Layer | Choice | Rationale |
|---|---|---|
| Language | Python 3.6 | Ecosystem standard |
| Workflow | Snakemake / Nextflow | Reproducible pipelines; both mature by 2017 |
| Annotation | Ensembl VEP, dbNSFP, SnpEff | Standard, deterministic |
| Variant I/O | pysam, cyvcf2, Biopython | Fast VCF handling |
| Classical ML | XGBoost 0.6–0.7, LightGBM, scikit-learn | Best tabular performance in period |
| Calibration | scikit-learn isotonic / Platt | Standard |
| NLP | ULMFiT (fastai, 2018), AllenNLP ELMo (2018), spaCy, Gensim | Period-correct transfer learning |
| Deep learning framework | TensorFlow 1.4–1.9 + Keras | Primary; PyTorch 0.3–0.4 acceptable |
| Serving | Flask + gunicorn, Redis | Simple, matches a small team |
| Storage | PostgreSQL (curator actions/audit), S3 (snapshots) | Conventional |
| Review UI | Server-rendered + small JS layer | No SPA framework needed |
| Cloud | AWS ap-southeast-1 | Matches existing deployment (§3.1) |

**Excluded deliberately:** BERT, any LLM, any generative text. BERT postdates the tenure; generative models do not belong in a clinical classification path.

---

## 9. Delivery Plan (phased to 1 yr 3 mos)

### Phase 0 — Weeks 1–4: Foundations
- Assemble ClinVar + internal labels; define the variant feature schema
- Build the evaluation harness with gene-disjoint and temporal splits
- **Gate:** baseline VUS rate and baseline curator review time measured

### Phase 1 — Weeks 5–16: Annotation and feature pipeline
- VEP annotation, dbNSFP join, population frequency join, constraint metrics
- Feature store with versioning
- **Gate:** 100% of panel variants annotated reproducibly; annotation reproducible from a tagged release

### Phase 2 — Weeks 17–32: Supervised triage
- XGBoost classifier, per-ancestry calibration
- Ancestry-stratified evaluation
- **Gate:** ECE ≤ 0.05; top-20 recall ≥ 0.85; ancestry transfer gap quantified

### Phase 3 — Weeks 33–46: Literature evidence triage
- TF-IDF/LSA retrieval baseline over ClinVar + PubMed
- ULMFiT / ELMo relevance classifier
- **Gate:** ≥ 0.80 precision on top-5 retrieved abstracts per variant

### Phase 4 — Weeks 47–58: Evidence synthesis and routing
- ACMG code mapping with provenance
- Threshold policy per consequence class
- Abstention logic
- **Gate:** every suggested code carries a human-readable justification

### Phase 5 — Weeks 59–65: Shadow deployment
- Run in parallel with existing manual curation; no auto-classification
- Compare triage ranking against what curators actually prioritized
- **Gate:** VUS reduction ↓ 30% and curator time ≤ 90 s/variant in shadow measurement

---

## 10. Risks and Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| Confidently wrong classification | **Critical** | Calibration gate; mandatory abstention; category-4 error tracking; human sign-off |
| ClinVar label noise | High | Filter by review status; use internal curations as gold; report label-quality sensitivity |
| Ancestry bias / poor transfer | High | Per-ancestry calibration; ancestry-disjoint evaluation; report the gap as a headline metric |
| Gene memorization | High | Gene-disjoint splits; hold out entire genes during evaluation |
| Review queue becomes the bottleneck | High | ≤ 90 s/variant gate; per-consequence thresholds to control load |
| Regulatory / QMS exposure | High | ISO 13485 traceability; model versioning; no autonomous classification |
| Data governance (UU PDP, PDPA) | High | De-identified data; consent verification; no cross-border transfer of identifiable genomes |
| Feature staleness (gnomAD, ClinVar versions) | Medium | Versioned feature store; annotation reproducibility gate |
| Scope creep into PRS or PGx star-alleles | Medium | Hard architectural boundary — this service emits variant rankings only |

---

## 11. What This Deliberately Is Not

- **Not** a variant caller. DeepVariant (Dec 2017) and GATK already own that layer; this sits downstream.
- **Not** an autonomous classifier. Curators decide; the system prioritizes and explains.
- **Not** a polygenic risk score engine. PRS is a separate module with different statistics (see below).
- **Not** a BERT-era design. The tenure ends before BERT; the NLP layer is ULMFiT/ELMo-based by construction.

### Runner-up use cases (adjacent, same stack)

1. **PGx evidence curation for RxMax.** 35 genes and 300+ gene–drug interactions (§2.2) are maintained largely by hand. A ULMFiT-based literature triage layer over PubMed, classifying abstracts by gene–drug–phenotype relevance, directly reduces curation load. Same NLP stack, smaller scope, faster payback.
2. **PRS ancestry-transfer calibration.** 10+ polygenic scores normalized on Asian datasets (§2.2). A model that predicts score degradation when transferring across ancestries would quantify the localization moat. More research-flavoured, less immediately operational.
3. **CYP2D6 / CYP2D6-CNV calling.** The hardest PGx locus (pseudogene CYP2D7, structural variation, hybrid alleles). ML-assisted diplotype calling is high-value and period-feasible, but narrow enough to be a phase-2 extension.

---

## 12. Provenance and Honest Caveats

- Company facts are drawn from `NalaGenetics-Research.md` (research dated 2026-11-21) and describe the **2026** product. In May 2017 – Jul 2018 the company was pre-seed (seed closed Nov 2018, after the tenure), roughly a year old, and building the core of what became Nala CDS. The 2026 platform is substantially larger than anything that existed then.
- The author's tenure (May 2017 – Jul 2018) and function (bioinformatics / software) were supplied by the author, not independently verified.
- Technical claims about the window are period-accurate: DeepVariant open-sourced Dec 2017; Clairvoyante May 2018; ULMFiT Jan–May 2018; ELMo Feb 2018; GPT-1 Jun 2018. BERT (Oct 2018) postdates the tenure and is excluded by design.
- This is a reconstruction. It specifies a system that *could* have been built with the tools of the time and that aligns with the company's stated platform direction (Nala CDS, Asian-enriched knowledge base, AI/ML models). It is not a claim about what was actually built.
- Financial and headcount figures are third-party estimates and unverified.