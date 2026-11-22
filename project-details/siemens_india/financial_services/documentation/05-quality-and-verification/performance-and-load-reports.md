# Performance and Load Reports

## 1. Performance targets

| Operation | Target |
|---|---|
| Scoring API (on-demand) | p95 ≤ 5 s per account |
| Batch scoring | Nightly (full book) |
| Feature store reads | p95 ≤ 100 ms |
| Watchlist query | p95 ≤ 2 s |

## 2. Load model

| Scenario | Concurrency | Notes |
|---|---|---|
| Normal | ~20 concurrent | Credit officers |
| Month-end / review cycle | ~100 concurrent | Batch + on-demand |
| Full book batch | Nightly | Thousands of accounts |

## 3. Results (template)

> Replace with actual measurements before release.

| Test | p50 | p95 | p99 | Error rate | Notes |
|---|---|---|---|---|---|
| Scoring (single) | — | — | — | — | |
| Batch (full book) | — | — | — | — | |
| Watchlist | — | — | — | — | |

## 4. Bottlenecks & mitigations

| Bottleneck | Mitigation |
|---|---|
| Feature store reads | Online store; caching |
| Model inference | Batch; horizontal workers |
| Spark join | Partitioning; incremental |
| PSI computation | Scheduled; incremental |

## 5. Scalability plan

- **Horizontal:** add scoring workers.
- **Batch:** Spark autoscaling.
- **Storage:** partition by date.

## 5. Reporting cadence

- Load test before each major release.
- Continuous latency/error monitoring.