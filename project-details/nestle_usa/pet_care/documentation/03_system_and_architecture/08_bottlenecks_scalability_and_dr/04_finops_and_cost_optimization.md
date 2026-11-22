# FinOps and Cost Optimization

## 1. Cost drivers

| Driver | Notes |
|---|---|
| **Model inference** | Token spend (frontier + small) |
| **Vector search** | Embeddings + storage |
| **Data platform** | Snowflake/Databricks |
| **Observability** | LangSmith/Datadog |

## 2. Cost controls

| Control | Mechanism |
|---|---|
| **Semantic caching** | Cut repeated LLM calls |
| **Model routing** | Small for intake, frontier for coaching |
| **Autoscaling** | Scale to demand |
| **Chargeback** | Per business unit |

## 3. Chargeback

- Tag costs by business unit.
- Monthly chargeback reports.
- Budget alerts.

## 4. Optimization tactics

| Tactic | Impact |
|---|---|
| Cache hit rate ↑ | Token cost ↓ |
| Small-model routing | Token cost ↓ |
| Tiered storage | Storage ↓ |

## 5. Unit economics

| Metric | Target |
|---|---|
| **Cost per scenario** | Trend down |
| **Cost per coaching** | Trend down |
| **Cache hit rate** | ≥ 40% |

## 6. Monitoring

- Datadog/Grafana cost dashboards.
- Budget alerts.
- Anomaly detection.

## 7. Governance

- Monthly FinOps review.
- Quarterly optimization review.