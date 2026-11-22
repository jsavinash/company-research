# Performance and Load Reports

## 1. Performance targets (recap)

| Operation | Target |
|---|---|
| Copilot interactive response | p95 ≤ 5 s |
| Scenario what-if | p95 ≤ 10 s |
| Forecast batch (nightly) | Complete by 06:00 local |
| Forecast API throughput | Handle peak planner concurrency |

## 2. Load model

| Scenario | Concurrency | Notes |
|---|---|---|
| Normal planner load | ~100 concurrent | Interactive copilot + dashboards |
| Peak (planning cycle) | ~300 concurrent | Month-end / quarter-end |
| Batch | Nightly | Full hierarchy forecast |

## 3. Test results (template)

> Replace with actual measurements before release.

| Test | p50 | p95 | p99 | Error rate | Notes |
|---|---|---|---|---|---|
| Copilot interactive | — | — | — | — | |
| Scenario what-if | — | — | — | — | |
| Forecast API (single SKU) | — | — | — | — | |
| Forecast batch (full hierarchy) | — | — | — | — | |

## 4. Bottlenecks & mitigations

| Bottleneck | Mitigation |
|---|---|
| LLM latency (frontier model) | Semantic caching; stream tokens; route simple queries to small models |
| Snowflake query time | Result caching; clustering; pre-aggregation |
| Feature store reads | Online store (Feast); caching |
| Graph traversal (Neo4j) | Index + query limits |
| Policy checks (OPA) | Decision caching |

## 5. Scalability test plan

- **Horizontal:** add copilot replicas; verify linear scaling.
- **Data volume:** scale to full banner/DMA hierarchy; verify batch window.
- **Multi-category:** reuse across Frozen → Coffee → Baking; verify no degradation.

## 6. Reporting cadence

- Load test before each major release.
- Continuous latency/cost monitoring in Datadog/Grafana.
- Monthly FinOps review.