# Decision Log

Lightweight log of significant decisions. Complements the ADRs in `architecture-decision-records/`.

| ID | Date | Decision | Rationale | Status |
|---|---|---|---|---|
| D-001 | 2019-08 | Operational telemetry as a first-class credit signal | The moat: SFS sees the machine, a bank does not | Accepted |
| D-002 | 2019-09 | PD + survival models (not a single classifier) | PD says how likely; survival says when (censoring) | Accepted |
| D-003 | 2019-10 | Gradient-boosted trees (XGBoost/LightGBM) | Best-in-class credit model in period | Accepted |
| D-004 | 2019-11 | Calibration (Platt/isotonic) + WoE scorecard | Every PD calibrated; regulatory-friendly companion | Accepted |
| D-005 | 2019-12 | SHAP reason codes | Regulatory requirement; no black box | Accepted |
| D-006 | 2020-01 | Cost-asymmetric thresholds | Missed default vs. false alarm asymmetry | Accepted |
| D-007 | 2020-02 | Out-of-time + out-of-universe validation | Judge on future books, not shuffled splits | Accepted |
| D-008 | 2020-03 | Operational-signal lift as a release gate | If no lift, the moat claim fails | Accepted |
| D-009 | 2020-05 | Per-entity data isolation + de-identification | India DPDP; cross-entity governance | Accepted |
| D-010 | 2020-09 | No autonomous credit decision | Regulated; credit officer decides | Accepted |
| D-011 | 2021-01 | MLflow registry + PSI monitoring | Registry, lineage, drift | Accepted |
| D-012 | 2021-06 | Shadow deployment before production | Prove no calibration/stability regression | Accepted |

## Change process

- New decisions appended with next ID.
- Status: Proposed → Accepted → Superseded.
- Architectural decisions get a full ADR in `architecture-decision-records/`.