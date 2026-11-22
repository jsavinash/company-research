# Performance and Load Reports

## 1. Performance targets

| Operation | Target |
|---|---|
| Inference per study | p95 ≤ 3 s |
| Worklist triage | Near-real-time |
| Heatmap generation | p95 ≤ 1 s |
| Calibration | Per-site (offline fit) |

## 2. Load model

| Scenario | Concurrency | Notes |
|---|---|---|
| Normal | ~10 studies/min | Clinical reading |
| Screening camp | ~50 studies/min | High-burden TB screening |
| Batch backfill | Nightly | Re-analysis |

## 3. Results (template)

> Replace with actual measurements before release.

| Test | p50 | p95 | p99 | Error rate | Notes |
|---|---|---|---|---|---|
| Inference (single study) | — | — | — | — | |
| Heatmap | — | — | — | — | |
| Batch (screening) | — | — | — | — | |

## 4. Bottlenecks & mitigations

| Bottleneck | Mitigation |
|---|---|
| DICOM ingestion | Parallel; caching |
| GPU inference | Batch; horizontal workers |
| Grad-CAM | Compute on demand |
| Calibration | Offline fit; cached |

## 5. Scalability plan

- **Horizontal:** add inference workers.
- **GPU autoscaling.**
- **Partitioning** by site/date.

## 6. Reporting cadence

- Load test before each major release.
- Continuous latency/error monitoring.