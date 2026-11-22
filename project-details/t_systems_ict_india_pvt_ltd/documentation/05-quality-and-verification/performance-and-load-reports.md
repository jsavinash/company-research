# Performance and Load Reports

## 1. Performance targets

| Operation | Target |
|---|---|
| Discovery API (search/reco) | p95 ≤ 35 ms (benchmark boundary defined) |
| p99 latency | Reported alongside p95 |
| Peak throughput | 2,500+ req/s (if evidenced) |

## 2. Load model

| Scenario | Concurrency | Notes |
|---|---|---|
| Steady state | ~500 req/s | Normal traffic |
| Peak (flash sale / Black Friday) | ~2,500+ req/s | Order-of-magnitude spike |
| Batch backfill | Nightly | Re-training |

## 3. Results (template)

> Replace with actual measurements before release.

| Test | p50 | p95 | p99 | Error rate | Notes |
|---|---|---|---|---|---|
| Search | — | — | — | — | |
| Recommendations | — | — | — | — | |
| Peak (2,500 rps) | — | — | — | — | |

## 4. Bottlenecks & mitigations

| Bottleneck | Mitigation |
|---|---|
| ANN retrieval | FAISS/Annoy tuning; product vector precompute |
| Model inference | TF Serving + HPA; warm capacity |
| Redis session reads | TTL + pipelining |
| Cold start | Content/popularity fallback |

## 5. Scalability plan

- **Horizontal:** HPA on CPU/concurrency.
- **Warm capacity** for peak.
- **Benchmark boundary:** define what's included in p95 (network, ranking, serialization).

## 6. Reporting cadence

- Load test before each major release.
- Continuous latency/error monitoring.
- Monthly FinOps review.