# System Design Document

## 1. Context

This document specifies the as-built design of the credit-risk early-warning capability for SFS B2B equipment finance, scoped to the 2019–2022 toolchain. It complements `../01-business-and-strategy/high-level-solution-overview.md` (business view).

## 2. Goals & non-goals

**Goals:** calibrated PD + survival early warning; operational-signal lift; audit-grade reason codes; model-risk governance.

**Non-goals:** autonomous lending, IFRS 9 engine, fraud/AML, consumer credit, LLMs.

## 3. Component design

| Stage | Component | Technology | Responsibility |
|---|---|---|---|
| 1 | Risk-data platform | Kafka, Spark 3.0, Airflow 1.10 | Entity join, de-identification, lineage |
| 2 | Feature store | Time-aware store + InfluxDB | Point-in-time features |
| 3 | PD model | XGBoost / LightGBM | Probability of default |
| 4 | Survival model | lifelines (Cox PH, AFT) | Time-to-delinquency (censored) |
| 5 | Calibration | Platt / isotonic | Calibrated PD |
| 6 | Interpretability | SHAP + WoE scorecard | Reason codes + regulatory companion |
| 7 | Early-warning | Rule engine | Green/amber/red + watchlist |
| 8 | Serving | Docker, Kubernetes | Batch + on-demand scoring |
| 9 | Monitoring | Prometheus/Grafana + PSI | Drift & stability |

## 4. Data flow

1. **Ingest** — credit book (SFS), telemetry (service/ops), finance (Corporate).
2. **Join** — entity join under governance; de-identification.
3. **Features** — point-in-time; operational features windowed/lagged.
4. **PD** — XGBoost/LightGBM + cost-sensitive loss.
5. **Survival** — Cox PH / AFT with censoring.
6. **Calibrate** — Platt/isotonic; per-cohort.
7. **Explain** — SHAP reason codes; WoE scorecard.
8. **Warn** — green/amber/red + horizon; watchlist.
9. **Review** — credit officer → labels → governed retrain.

## 5. Component notes

- **The entity join is the project.** Credit + telemetry + finance live in different systems with different keys. Joining time-correctly under per-entity governance is the hard engineering — and the whole differentiator.
- **Operational features are the moat.** Utilization trend, downtime, service-deferral, energy — computed as windowed features and **attributed separately** from financial signals. The system must say "this deterioration is operational, not (only) financial."
- **Two models, one decision.** PD says *how likely*; survival says *when*. WoE scorecard is the regulatory-friendly companion.
- **Calibration and reason codes are the product.** A calibrated PD with business-language reason codes is what a credit officer can act on and an auditor can defend.

## 6. Deployment topology

- **Kubernetes** (Docker) for serving + batch scoring.
- **Airflow** for pipelines; **Kafka** for streaming; **Spark** for the join; **MLflow** for registry.
- **Prometheus/Grafana** for monitoring + PSI dashboards.

## 7. Key design decisions

See `decision-log.md` and `architecture-decision-records/`.

## 8. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Operational signal doesn't beat financial-only | Measure lift as a gate |
| Class imbalance | Survival framing; cost-asymmetric thresholds; PR-AUC/KS |
| Right-censoring bias | Survival models with censoring |
| Data-join error | Audited join accuracy; per-contract keys |
| Concept drift | PSI + calibration monitoring |
| Regulatory audit failure | Governed versioning, validation, reason codes |

## 9. Related

- `../02-product-and-ux/product-requirements-doc.md`
- `non-functional-requirements.md`
- `integration-and-data-strategy.md`