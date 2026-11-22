# Performance and Load Reports

## 1. Performance targets

| Operation | Target |
|---|---|
| Copilot interactive | p95 ≤ 5 s |
| Intake→plan | ≤ a few seconds |
| Coaching first token | ≤ 2 s |
| Coaching full | p95 ≤ 5 s |

## 2. Load model

| Scenario | Concurrency | Notes |
|---|---|---|
| Normal | ~100 concurrent | Owners |
| Peak | ~300 concurrent | Campaign |
| Batch eval | Nightly | Retraining |

## 4. Results (template)

> Replace with actual measurements before release.

| Test | p50 | p95 | p99 | Error rate | Notes |
|---|---|---|---|---|---|
| Intake | — | — | — | — | |
| Coaching | — | — | — | — | |
| Peak | — | — | — | — | |

## 5. Bottlenecks & mitigations

| Bottleneck | Mitigation |
|---|---|
| LLM latency | Semantic cache; small-model routing; streaming |
| Vector search | HNSW index; caching |
| Snowflake query | Clustering; result cache |
| OPA policy | Decision caching |

## 6. Scalability plan

- **Horizontal:** add workers.
- **Batch:** Spark autoscaling.

## 7. Reporting cadence

- Load test before each major release.
- Continuous latency/cost monitoring.