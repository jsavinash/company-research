# FinOps and Cost Optimization

## 1. Cost drivers

| Driver | Notes |
|---|---|
| **Cloud compute** | Databricks, Snowflake, AKS, Azure |
| **Model inference** | Token spend (frontier + small) |
| **Data** | Ingestion, storage, feature store |
| **Observability** | LangSmith, Datadog |
| **Licenses** | Panel, GLP-1 data, gateway |

## 2. Cost controls

| Control | Mechanism |
|---|---|
| **Semantic caching** | Cut repeated LLM calls |
| **Model routing** | Small/fast for extraction; frontier only for reasoning |
| **Autoscaling** | Scale to demand |
| **Tiered storage** | Hot/warm/cold |
| **Reserved capacity** | Databricks/Snowflake commitments |
| **Chargeback** | Per business unit |

## 3. Chargeback

- Tag costs by business unit (Frozen / Coffee / Baking).
- Monthly chargeback reports.
- Budget alerts.

## 4. Optimization tactics

| Tactic | Impact |
|---|---|
| Cache hit rate ↑ | Token cost ↓ |
| Small-model routing | Token cost ↓ |
| Batch forecast | Compute ↓ |
| Tiered storage | Storage ↓ |
| Spot instances (where safe) | Compute ↓ |

## 5. Unit economics

| Metric | Target |
|---|---|
| **Cost per scenario** | Trend down |
| **Cost per forecast run** | Trend down |
| **Cache hit rate** | ≥ 40% |
| **Token cost / business unit** | Within budget |

## 6. Monitoring

- Datadog / Grafana cost dashboards.
- Budget alerts.
- Anomaly detection.

## 7. Governance

- Monthly FinOps review.
- Quarterly optimization review.

## 8. Related

- `Nestle-USA-DemandSensing-AIArchitect-UseCase/01-business-and-strategy/business-case-and-roi.md`
- `01_business/10_cost_roi_and_alternatives/`