# Low-Level Design Specs

## 1. Scoring service

**Input:** account/cohort + as-of date.
**Output:** calibrated PD + survival time-to-event + reason codes + early-warning flag.

```
score(account, as_of) -> ScoreResult
  1. features = feature_store.get(account, as_of)   # point-in-time
  2. pd = pd_model.predict(features)                # XGBoost/LightGBM
  4. pd_cal = calibrate(pd)                          # Platt/isotonic
  5. tte = survival.predict(features)               # Cox PH / AFT
  6. reasons = shap.explain(features)               # reason codes
  7. flag = early_warning(pd_cal, tte)              # green/amber/red
  8. return ScoreResult
```

## 2. Feature layer

- **Financial:** payment history, DPD, credit-line utilization, firmographics.
- **Operational (moat):** utilization trend (30/60/90d), downtime, service-deferral, energy draw.
- **Macro/segment:** sector, region, indicators.
- **Point-in-time:** every feature as of prediction date.

## 3. PD model

- **XGBoost / LightGBM** with cost-sensitive loss.
- **Calibration:** Platt/isotonic, per cohort.
- **Metrics:** KS, PR-AUC, ECE.

## 4. Survival model

- **Cox PH / AFT** (lifelines) with censoring.
- **Output:** P10/P50/P90 months to delinquency.

## 5. Interpretability

- **SHAP** → reason codes in credit language.
- **WoE scorecard** as regulatory companion.

## 6. Early-warning

- **Green/amber/red** thresholds with horizon.
- **Ranked watchlist.**
- **Separated attribution:** operational vs. financial-only.

## 7. Error handling

| Error | Handling |
|---|---|
| Thin history | Reject inference; flag |
| Data-join error | Quarantine; audit |
| Calibration drift | Alert; recalibrate |
| Concept drift | PSI alert; retrain |

## 8. Observability

- MLflow registry + lineage.
- PSI/calibration dashboards (Prometheus/Grafana).
- Reason-code quality sampling.