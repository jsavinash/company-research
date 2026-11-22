# Project Scope and SLA

## 1. In scope

**Portfolio**
- B2B equipment finance and leasing book (SFS).
- Cohorts by asset class (drives, switchgear, imaging, rail, factory automation) and contract type (lease / loan).

**Signals**
- Financial/transaction: payment history, DPD, credit-line utilization, firmographics.
- **Operational (the differentiator):** equipment utilization trend, downtime, service-deferral, energy draw, contract/lease events — joined from Siemens service and operations systems.
- Macro/segment context: sector, region, economic indicators (features, not forecasts).

**Outputs**
- Calibrated PD and probability of delinquency, with **survival / time-to-event** view (P10/P50/P90 months to event).
- Early-warning flags (green/amber/red) with horizon stated.
- **Reason codes** in credit language (SHAP translated).
- Ranked watchlist for credit review.

**Platform (Corporate Units)**
- Risk-data platform joining credit + telemetry + finance, with de-identification and per-entity isolation.
- Model risk governance: versioned, validated, audited; bias/fairness checks.
- Monitoring: population stability, calibration drift, concept drift.

## 2. Out of scope

- Autonomous approve/decline decisions (credit officer decides).
- Loan pricing and capital-allocation optimisation.
- Consumer / retail banking credit.
- Fraud detection and AML transaction monitoring.
- Market risk / trading.
- Full IFRS 9 ECL calculation (accounting owns it; this feeds it).

## 3. Explicit non-goals

- **No autonomous credit decision.** The system scores, explains, flags; a credit officer decides.
- **No uncalibrated PD.** Every PD is calibrated with a confidence statement.
- **No black-box output.** Reason codes are a regulatory requirement.
- **No cross-entity raw-data pooling without governance.**

## 4. Stakeholders

| Stakeholder | Role |
|---|---|
| Credit officers | Primary users (watchlist) |
| Credit-risk owner | Model approval, sign-off |
| Model risk / compliance | Independent validation, audit |
| Corporate Units (Finance/Risk/IT) | Risk-data platform |
| Data governance / DPO | India DPDP, de-identification |

## 5. SLAs

| Service | SLA | Measurement |
|---|---|---|
| Scoring API (batch) | Complete nightly | Airflow logs |
| Scoring API (on-demand) | p95 ≤ 5 s per account | Service logs |
| Early-warning lead time | ≥ 3 months | Backtest |
| Calibration (ECE) | ≤ 0.03 | Eval harness |
| Model governance | Independent validation sign-off | Model-risk pack |
| Availability | 99.5% | Monitoring |

## 6. Constraints & dependencies

- **Period-accurate tooling (2019–2022):** XGBoost/LightGBM, lifelines, SHAP, MLflow 1.0, Airflow 1.10, Kubeflow 1.0. No LLMs.
- **Data access:** credit book (SFS), telemetry (service/ops), finance (Corporate) — joined under contracts.
- **Governance:** per-entity isolation, India DPDP, IFRS 9 backdrop.
- **Model risk:** SR 11-7-style discipline.

## 7. Change control

Scope changes require a decision-log entry and, if architectural, a new ADR. SLA changes require sign-off from the credit-risk owner.