# Feature Prioritization Roadmap

## 1. Prioritization method

Features scored on **value** (VUS reduction × curator time) vs. **effort** (data readiness + model complexity), with **risk** (QMS/privacy) as a gate. Phased to the 1 yr 3 mos window.

## 2. Roadmap

### Phase 0 — Weeks 1–4: Foundations
- Assemble ClinVar + internal labels; define variant feature schema.
- Build evaluation harness (gene-disjoint + temporal splits).
- **Gate:** baseline VUS rate + baseline curator review time measured.

### Phase 1 — Weeks 5–16: Annotation & feature pipeline
- VEP annotation, dbNSFP join, population frequency, constraint metrics.
- Feature store with versioning.
- **Gate:** 100% of panel variants annotated reproducibly.

### Phase 2 — Weeks 17–32: Supervised triage
- XGBoost classifier, per-ancestry calibration.
- Ancestry-stratified evaluation.
- **Gate:** ECE ≤ 0.05; top-20 recall ≥ 0.85; ancestry transfer gap quantified.

### Phase 3 — Weeks 33–46: Literature evidence triage
- TF-IDF/LSA retrieval over ClinVar + PubMed.
- ULMFiT / ELMo relevance classifier.
- **Gate:** ≥ 0.80 precision on top-5 retrieved abstracts.

### Phase 4 — Weeks 47–58: Evidence synthesis & routing
- ACMG code mapping with provenance.
- Threshold policy per consequence class.
- Abstention logic.
- **Gate:** every suggested code carries a human-readable justification.

### Phase 5 — Weeks 59–65: Shadow deployment
- Run in parallel with manual curation; no auto-classification.
- Compare triage ranking against curator priorities.
- **Gate:** VUS reduction ↓ 30% and curator time ≤ 90 s/variant.

## 3. Deferred / out of scope

- Variant calling (DeepVariant/GATK).
- PRS computation.
- PGx star-allele calling.
- BERT-era NLP (postdates tenure).