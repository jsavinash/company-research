# Cost and ROI Summary

## 1. Cost model (illustrative)

| Category | Driver | Notes |
|---|---|---|
| **Cloud infrastructure** | Compute, storage, networking | Databricks + Snowflake + Azure + AWS |
| **Model inference** | Token spend (frontier + small) | Controlled by gateway + cache |
| **Data platform** | Ingestion, storage, feature store | Kafka, Iceberg, Feast |
| **Personnel** | Data science, ML eng, platform, security | Build + run |
| **Licenses** | Panel data, GLP-1 data, gateway | Recurring |
| **Observability** | LangSmith, Datadog | Per-seat / usage |

## 2. ROI model (illustrative)

| Value driver | Assumption | Annual value (illustrative) |
|---|---|---|
| Forecast accuracy improvement | ≥15% relative WMAPE reduction | Reduced safety stock + fewer lost sales |
| Trade-spend efficiency | Attribution-driven reallocation | Margin uplift |
| Analyst time saved | Copilot handles scenario analysis | Productivity |
| Avoided write-offs | Better shelf-life / promotion planning | Waste reduction |
| Reuse across categories | Frozen → Coffee → Baking | Amortized platform cost |

> **Note:** all figures are illustrative and must be replaced with Nestlé USA's actual baseline before any business-case submission. The source ProjectDoc deliberately avoids unverified numbers.

## 3. Cost-benefit summary

| Metric | Value |
|---|---|
| Estimated annual run cost | (to be filled with actuals) |
| Estimated annual benefit | (to be filled with actuals) |
| Net benefit | (to be filled) |
| Payback period | (to be filled) |
| ROI | (to be filled) |

## 4. FinOps controls

- **Chargeback** per business unit (Frozen / Coffee / Baking).
- **Semantic caching** to cut token spend.
- **Model routing** (small/fast for extraction; frontier only for reasoning).
- **Budget alerts** and anomaly detection.

## 5. Sensitivity

| Variable | Low | High |
|---|---|---|
| WMAPE improvement | 10% | 20% |
| Adoption | 50% | 90% |
| Token cost | +50% | -30% |

## 6. Financial model

See `financial_model.xlsx` (or `financial_model.csv` as a companion) for the working model.

## 7. Governance

- Monthly FinOps review.
- Quarterly business review with Steering Committee.
- ROI tracked against baseline in `../03_business_goals_and_kpis.md`.