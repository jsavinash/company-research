# Decision Log

Lightweight log of significant decisions. Complements the ADRs in `architecture-decision-records/`.

| ID | Date | Decision | Rationale | Status |
|---|---|---|---|---|
| D-001 | 2017-05 | No autonomous classification | Clinical safety + ISO 13485; curators decide | Accepted |
| D-002 | 2017-05 | Confidence-scored triage with explicit abstention | Directly addresses the VUS problem | Accepted |
| D-003 | 2017-06 | Gradient-boosted trees over deep learning | Tabular features; interpretability is a regulatory asset | Accepted |
| D-004 | 2017-06 | Per-ancestry calibration | European-calibrated models transfer poorly to Asian populations | Accepted |
| D-005 | 2017-07 | Gene-disjoint + temporal evaluation | Prevent gene memorization and future leakage | Accepted |
| D-006 | 2017-08 | ULMFiT / ELMo for literature triage | Period-correct transfer learning; BERT postdates tenure | Accepted |
| D-007 | 2017-09 | Deterministic ACMG code mapping with provenance | Never let the model assert a code without a reason | Accepted |
| D-008 | 2017-10 | Two-stage literature triage (TF-IDF/LSA → ULMFiT/ELMo) | Cheap retrieval + accurate relevance scoring | Accepted |
| D-009 | 2017-11 | ClinVar review-status filtering | Reduce label noise | Accepted |
| D-010 | 2018-01 | Curator efficiency gate (≤ 90 s/variant) | If review is slower than manual, the system failed | Accepted |
| D-011 | 2018-03 | Shadow deployment before prioritization | Prove VUS reduction without risking live classification | Accepted |
| D-012 | 2018-05 | Single deployable behind Nala CDS | Match a small team's operational appetite | Accepted |

## Change process

- New decisions appended with next ID.
- Status: Proposed → Accepted → Superseded.
- Architectural decisions get a full ADR in `architecture-decision-records/`.