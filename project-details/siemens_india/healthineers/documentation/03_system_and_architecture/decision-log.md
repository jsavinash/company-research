# Decision Log

Lightweight log of significant decisions. Complements the ADRs in `architecture-decision-records/`.

| ID | Date | Decision | Rationale | Status |
|---|---|---|---|---|
| D-001 | 2019-08 | Per-site / per-prevalence calibration as the differentiator | Prevalence shift breaks global calibration | Accepted |
| D-002 | 2019-09 | nnU-Net + DenseNet (era-standard, not novel) | Novelty is calibration + workflow, not architecture | Accepted |
| D-003 | 2019-10 | Grad-CAM localization mandatory | Radiologists need localization; black box is a non-starter | Accepted |
| D-004 | 2019-11 | "Cannot assess" as an explicit output | Abstention over confident wrong | Accepted |
| D-005 | 2019-12 | Site-held-out validation | Measure domain shift directly | Accepted |
| D-006 | 2020-01 | Device class as a first-class feature | Domain shift across devices | Accepted |
| D-007 | 2020-03 | Microbiological linkage for TB subset | Gold-standard labels | Accepted |
| D-008 | 2020-06 | NLP over reports for labels | Weak labels are the reality | Accepted |
| D-009 | 2020-09 | MRMC reader study | Acceptance measured, not inferred | Accepted |
| D-010 | 2021-01 | Locked model versions + immutable audit | MDR/FDA/CDSCO compliance | Accepted |
| D-011 | 2021-05 | No autonomous diagnosis | Radiologist signs | Accepted |
| D-012 | 2021-09 | Per-site isolation + de-id | India DPDP; federation option | Accepted |

## Change process

- New decisions appended with next ID.
- Status: Proposed → Accepted → Superseded.
- Architectural decisions get a full ADR in `architecture-decision-records/`.