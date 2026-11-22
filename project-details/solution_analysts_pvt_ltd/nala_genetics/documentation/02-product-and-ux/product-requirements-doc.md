# Product Requirements Document (PRD)

## 1. Summary

A confidence-scored variant triage layer for Nala CDS, scoped to the 2017–2018 toolchain. It ranks germline variants for curator review, attaches ACMG-aligned evidence codes and calibrated confidence, and routes uncertain cases to a human queue.

## 2. Goals

- Reduce VUS by ≥ 30% via triage + curator review.
- Make uncertainty explicit (calibrated confidence + abstention).
- Keep curator review fast (≤ 90 s/variant).
- Produce audit-grade outputs (provenance per code).
- Report the ancestry transfer gap as a headline metric.

## 3. Non-goals

- Variant calling from reads (DeepVariant/GATK).
- Somatic calling / tumour-only.
- PRS computation.
- Final clinical report generation / sign-out.
- PGx star-allele calling.

## 4. Personas

| Persona | Needs |
|---|---|
| **Curator** | Fast, explainable triage; review only uncertain variants |
| **Clinical lead** | Auditability, ISO 13485, no autonomous classification |
| **Bioinformatician** | Reproducible pipeline, feature store |
| **Data governance** | De-identified data, consent, no cross-border transfer |

## 5. Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | Ingest germline VCF (WES/WGS) + panel definition | Must |
| FR-2 | Annotate (VEP, dbNSFP, gnomAD/ExAC, ClinVar) | Must |
| FR-3 | Assemble ~40–60 interpretable features | Must |
| FR-4 | Supervised triage (XGBoost/GBM) | Must |
| FR-5 | Per-ancestry isotonic calibration | Must |
| FR-6 | Literature triage (TF-IDF/LSA → ULMFiT/ELMo) | Must |
| FR-7 | ACMG code mapping with provenance | Must |
| FR-8 | Routing: prioritize / queue / abstain | Must |
| FR-9 | Curator UI (evidence, codes, confidence, alternatives) | Must |
| FR-10 | Log every curator action as a training label | Must |
| FR-11 | Audit trail (code → evidence → provenance) | Must |
| FR-12 | Ancestry-disjoint + gene-disjoint evaluation | Must |

## 6. Non-functional requirements (summary)

- Triage p95 ≤ 3 s per variant batch.
- Top-20 recall ≥ 0.90; ECE ≤ 0.05.
- Curator ≤ 90 s/variant.
- ISO 13485 traceability; de-identified data.
- Availability 99.5%.

See `../03_system_and_architecture/non-functional-requirements.md`.

## 7. Success metrics

- VUS reduction ↓ 30% (primary).
- Precision@20 ≥ 0.70.
- Ancestry transfer gap quantified.

## 8. Open questions

- Exact ACMG code thresholds per consequence class.
- Cloud vs. local inference for ULMFiT/ELMo.
- Label-quality sensitivity (ClinVar review status).