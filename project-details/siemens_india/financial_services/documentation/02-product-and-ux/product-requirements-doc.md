# Product Requirements Document (PRD)

## 1. Summary

A credit-risk early-warning capability for SFS B2B equipment finance, scoped to the 2019–2022 toolchain. It predicts default/delinquency 3–6 months ahead using operational machine telemetry as a leading signal, with a corporate risk-data and model-governance layer.

## 2. Goals

- Predict default/delinquency 3–6 months ahead.
- Achieve calibrated KS ≥ 0.35 (out-of-time).
- Demonstrate operational-signal lift ≥ +0.03 KS vs. financial-only.
- Produce audit-grade reason codes + governance.
- Keep the credit officer in control (no autonomous decisions).

## 3. Non-goals

- Autonomous approve/decline.
- Loan pricing / capital allocation.
- Consumer credit.
- Fraud / AML.
- Full IFRS 9 ECL calculation.

## 4. Personas

| Persona | Needs |
|---|---|
| **Credit officer** | Actionable watchlist, reason codes, time-to-event |
| **Credit-risk owner** | Model approval, governance |
| **Model risk / compliance** | Validation, audit, bias checks |
| **Data governance / DPO** | Per-entity isolation, DPDP |

## 5. Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | Ingest credit book + operational telemetry + finance data | Must |
| FR-2 | Entity join under governance + de-identification | Must |
| FR-3 | Point-in-time feature store | Must |
| FR-4 | Operational features (utilization, downtime, service-deferral, energy) | Must |
| FR-5 | PD model (XGBoost/LightGBM, cost-sensitive) | Must |
| FR-6 | Survival model (Cox PH / AFT, censored) | Must |
| FR-7 | Calibration (Platt/isotonic) | Must |
| FR-6 | WoE scorecard companion | Should |
| FR-9 | SHAP reason codes | Must |
| FR-10 | Early-warning green/amber/red + horizon | Must |
| FR-11 | Ranked watchlist | Must |
| FR-12 | Model risk governance (versioning, validation, bias) | Must |
| FR-13 | Drift/calibration monitoring (PSI) | Must |

## 6. Non-functional requirements (summary)

- Scoring p95 ≤ 5 s per account.
- ECE ≤ 0.03.
- Availability 99.5%.
- Per-entity isolation; India DPDP.
- Model risk (SR 11-7-style) governance.

See `../03_system_and_architecture/non-functional-requirements.md`.

## 7. Success metrics

- Calibrated KS ≥ 0.35.
- Operational lift ≥ +0.03 KS.
- Lead time ≥ 3 months.
- Recall ≥ 0.60.

## 8. Open questions

- Achievable operational-data coverage (not every asset is connected).
- Per-entity data-sharing contracts.
- Choice of survival model (Cox PH vs. AFT) per cohort.