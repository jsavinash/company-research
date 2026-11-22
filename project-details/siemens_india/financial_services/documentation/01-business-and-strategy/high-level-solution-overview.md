# High-Level Solution Overview

## 1. One-line description

> A credit-risk early-warning capability for B2B equipment finance: calibrated PD + survival time-to-delinquency, using operational machine telemetry as a leading signal beyond lagging financials — with a corporate risk-data and model-governance layer that makes it auditable.

## 2. Core design decision

**The operational signal is the moat, and it must be measured as a gate.** A model with high KS that shows no incremental value over a financial-only baseline has not earned the operational-data complexity. And **no autonomous credit decision** — the system scores, explains, flags; a credit officer decides.

## 3. Architecture at a glance

```
Source systems
  SFS credit book (contract, payment, DPD, firmographics)
  Siemens service/ops (telemetry, downtime, service-deferral, energy)  ← the moat
  Corporate finance (ledger, exposure, segment/macro)
   ▼
Risk-data platform (Corporate Units): Kafka → Spark → time-aware feature store
   ▼
Feature layer: financial + operational + macro → point-in-time features
   ├──▶ PD model (XGBoost/LightGBM + cost-sensitive) → PD
   └──▶ Survival model (Cox PH / AFT, censored) → P10/P50/P90 months to event
   ▼
Calibration + interpretability: Platt/isotonic → calibrated PD; WoE scorecard; SHAP → reason codes
   ▼
Early-warning: green/amber/red with horizon; watchlist; operational vs. financial attribution
   ▼
Credit officer review: accept / escalate / restructure → outcome labels → retrain (governed)
```

## 4. The stages

| Stage | Purpose | Key tech |
|---|---|---|
| **Risk-data platform** | Entity join + de-identification + lineage | Kafka, Spark, Airflow |
| **Feature layer** | Financial + operational + macro features | Time-aware feature store, InfluxDB |
| **PD model** | Probability of default | XGBoost / LightGBM |
| **Survival model** | Time-to-delinquency (censored) | lifelines (Cox PH, AFT) |
| **Calibration** | Reliable PD | Platt / isotonic |
| **Interpretability** | Reason codes + scorecard | SHAP, WoE |
| **Early-warning** | Green/amber/red + watchlist | Rule engine |
| **Governance** | Model risk, bias, drift | MLflow, PSI dashboards |

## 6. Why this was buildable in Aug 2019 – Mar 2022

| Capability | Availability | Use |
|---|---|---|
| Gradient boosting | XGBoost 0.90–1.2, LightGBM 2.x | PD model |
| Survival analysis | lifelines (Cox PH, AFT) | Time-to-delinquency |
| Class imbalance | Focal loss, SMOTE, cost-sensitive | Rare defaulters |
| Calibration | Platt, isotonic | Calibrated PD |
| Scorecards / WoE | Standard banking | Regulatory-friendly model |
| Explainability | **SHAP 0.35–0.40** | Reason codes |
| Experiment tracking | **MLflow 1.0 (Jun 2019)** | Registry, lineage |
| Orchestration | Airflow 1.10, **Kubeflow 1.0 (2020)** | Pipelines |
| Generative AI | **Not applicable** | **Excluded** |

**Excluded:** any LLM (no role in credit risk), any black-box model without reason codes, any autonomous approve/decline.

See `../03_system_and_architecture/system-design-document.md` for the detailed design.