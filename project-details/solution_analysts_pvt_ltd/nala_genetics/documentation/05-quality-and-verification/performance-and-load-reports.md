# Performance and Load Reports

## 1. Performance targets

| Operation | Target |
|---|---|
| Triage API (per batch) | p95 ≤ 3 s |
| Annotation (per variant) | p95 ≤ 50 ms |
| Feature assembly (per variant) | p95 ≤ 10 ms |
| Curator UI interaction | p95 ≤ 1 s |

## 2. Load model

| Scenario | Concurrency | Notes |
|---|---|---|
| Normal | ~10 concurrent | Research/clinical volume |
| Peak (national program) | ~50 concurrent | 10,000-genome batches |
| Batch backfill | Nightly | Re-triage |

## 3. Results (template)

> Replace with actual measurements before release.

| Test | p50 | p95 | p99 | Error rate | Notes |
|---|---|---|---|---|---|
| Triage (WES batch) | — | — | — | — | |
| Triage (WGS batch) | — | — | — | — | |
| Annotation | — | — | — | — | |
| Curator queue | — | — | — | — | |

## 4. Bottlenecks & mitigations

| Bottleneck | Mitigation |
|---|---|
| Annotation (VEP) latency | Cache; parallelize per variant |
| Model inference | Batch; Redis queue; horizontal workers |
| Literature triage | Two-stage (TF-IDF first, ULMFiT on shortlist) |
| Curator queue | Per-consequence thresholds to control load |

## 5. Scalability plan

- **Horizontal:** add triage workers.
- **Queue:** Redis with autoscaling.
- **Storage:** S3-compatible, partition by run.

## 6. Reporting cadence

- Load test before each major release.
- Continuous latency/error monitoring.
- Monthly FinOps review.