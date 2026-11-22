# Feature Prioritization Roadmap

## 1. Prioritization method

Features scored on **value** (provisioning reduction × adoption) vs. **effort** (data readiness + model complexity), with **risk** (model-risk audit, privacy) as a gate. Phased to the 2 yrs 8 mos window.

## 2. Roadmap

### Phase 0 — Months 1–2: Foundations
- Select pilot asset classes + two customer cohorts.
- Extract 24–36 months of contract, payment, operational records.
- Baseline: delinquency rate, provisioning accuracy, review cost.
- **Gate:** label definition + baseline signed off by credit-risk owner.

### Phase 1 — Months 3–7: Risk-data platform & features
- Entity join (credit + operational + finance) under governance; de-identification.
- Point-in-time feature store; operational-feature engineering.
- **Gate:** features reproducible; join accuracy audited.

### Phase 2 — Months 8–14: PD & survival models
- LightGBM/XGBoost PD (cost-sensitive); Cox PH / AFT survival.
- WoE scorecard companion; SHAP reason codes.
- **Gate:** out-of-time KS ≥ 0.30; ECE ≤ 0.05.

### Phase 3 — Months 15–22: Calibration & operational lift
- Platt/isotonic calibration; per-cohort calibration.
- **Operational-signal lift** vs. financial-only.
- **Gate:** calibrated KS ≥ 0.35; operational lift ≥ +0.03 KS.

### Phase 4 — Months 23–28: Early-warning & validation
- 3–6 month horizon; green/amber/red thresholds.
- Out-of-universe + per-cohort validation; reject inference; PSI baseline.
- **Gate:** lead time ≥ 3 months; recall ≥ 0.60.

### Phase 5 — Months 29–33: Governance & integration
- Model-risk governance pack; bias/fairness; versioned rollback.
- Credit-officer UI; watchlist integration.
- **Gate:** independent validation sign-off; reason codes officer-rated ≥ 0.70.

### Phase 6 — Months 34–38: Shadow deployment
- Silent run alongside existing process; monitor PSI/calibration.
- **Gate:** no calibration/stability regression over a full review cycle.

## 3. Deferred / out of scope

- Autonomous lending.
- IFRS 9 engine.
- Fraud / AML.
- Consumer credit.
- LLMs.