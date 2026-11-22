# Performance and Load Reports

## 1. Performance targets

| Operation | Target |
|---|---|
| Extraction API (per document) | p95 ≤ 2 s |
| Reviewer UI interaction | p95 ≤ 1 s |
| OCR (per page) | p95 ≤ 1.5 s |
| Field extraction (per document) | p95 ≤ 0.5 s |

## 2. Load model

| Scenario | Concurrency | Notes |
|---|---|---|
| Normal (off-season) | ~10 concurrent | Dev/test volume |
| Filing-season peak (Jan–Apr) | ~100 concurrent | Peak upload + review |
| Batch backfill | Nightly | Re-extraction |

## 3. Results (template)

> Replace with actual measurements before release.

| Test | p50 | p95 | p99 | Error rate | Notes |
|---|---|---|---|---|---|
| Extraction (W-2) | — | — | — | — | |
| Extraction (K-1) | — | — | — | — | |
| OCR (degraded) | — | — | — | — | |
| Review queue | — | — | — | — | |

## 4. Bottlenecks & mitigations

| Bottleneck | Mitigation |
|---|---|
| OCR latency | Tesseract local; cloud fallback only on low confidence |
| Model inference | Batch; Redis queue; horizontal workers |
| Review queue | Per-field thresholds to keep load ≤ 0.20 |
| Cloud OCR cost | Route only degraded scans; cache |

## 5. Scalability plan

- **Horizontal:** add extraction workers.
- **Queue:** Redis with worker autoscaling.
- **Storage:** S3-compatible, partition by date.

## 6. Reporting cadence

- Load test before each major release.
- Continuous latency/error monitoring.
- Monthly FinOps review.