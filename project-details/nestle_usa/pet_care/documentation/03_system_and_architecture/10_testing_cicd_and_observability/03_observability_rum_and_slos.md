# Observability, RUM, and SLOs

## 1. Observability pillars

| Pillar | Tool |
|---|---|
| **Logs** | Datadog / Azure Monitor |
| **Metrics** | Datadog / Grafana / Prometheus |
| **Traces** | OpenTelemetry + LangSmith |
| **Evals** | LangSmith / Arize / Braintrust / MLflow |

## 2. Tracing

- **OpenTelemetry** end-to-end.
- **LangSmith** for agent/LLM runs (tools, models, tokens, latency).

## 3. Metrics

| Metric | Source |
|---|---|
| **Latency (p50/p95/p99)** | Datadog |
| **Error rate** | Datadog |
| **Token usage / cost** | Gateway |
| **Cache hit rate** | Gateway |
| **Slot accuracy** | MLflow |
| **Grounding faithfulness** | LangSmith |

## 4. RUM (Real User Monitoring)

- **Datadog RUM** for web vitals.
- Session replay (optional).
- Error tracking.

## 5. SLOs

| SLO | Target |
|---|---|
| **Availability** | 99.9% |
| **Copilot latency** | p95 ≤ 5 s |
| **Scenario latency** | p95 ≤ 10 s |
| **Error rate** | < 1% |

## 6. Error budgets

- **Budget** = allowed downtime for 99.9%.
- **Burn rate** alerts.
- **Freeze** releases if budget exhausted.

## 7. Alerting

| Alert | Threshold |
|---|---|
| Latency | p95 > target |
| Error rate | > 1% |
| Drift | Model/prompt drift |
| Hallucination | > 0 in eval |
| PII | Any DLP alert |

## 8. Dashboards

- Platform health.
- Quality / safety.
- FinOps.
- Adoption.