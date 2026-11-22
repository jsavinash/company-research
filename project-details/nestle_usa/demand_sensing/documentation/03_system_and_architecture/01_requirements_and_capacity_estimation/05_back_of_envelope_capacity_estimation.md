# Back-of-the-Envelope Capacity Estimates

> Order-of-magnitude estimates to size the platform. Replace with measured baselines before production sizing.

## 1. Traffic (QPS)

| Workload | Estimate | Basis |
|---|---|---|
| **Interactive copilot** | ~100 concurrent planners; ~5 queries/hr each | 8-hour day → ~70 queries/hr → ~0.02 QPS avg; peak ~5 QPS |
| **Dashboard reads** | ~300 concurrent; ~20 req/session | Peak ~20 QPS |
| **Forecast API** | Batch + on-demand | Peak ~10 QPS |
| **Nightly batch** | Full hierarchy | ~1 run/night; thousands of SKU×store forecasts |

**Peak aggregate:** ~50 QPS (interactive + API), with headroom for 3× spikes.

## 2. Bandwidth

| Flow | Estimate |
|---|---|
| **Copilot tokens** | ~2 KB/request × 5 QPS → ~10 KB/s |
| **Forecast payloads** | ~1 KB/forecast × 10 QPS → ~10 KB/s |
| **Static assets** | ~2 MB initial load × concurrent |
| **Data ingestion** | Kafka: ~MB/s (sell-out events) |

**Egress:** modest (internal); CDN handles static.

## 3. Storage

| Data | Volume (annual) | Notes |
|---|---|---|
| **Sell-out / shipment** | ~ billions of rows (SKU×store×week) | Partitioned Iceberg; compresses well |
| **Forecasts** | ~ millions of rows/yr | P10/P50/P90 per SKU×store×week |
| **Feature vectors** | ~ billions (entity×feature×date) | Columnar; compresses |
| **Vectors (embeddings)** | ~ millions of chunks | pgvector/Qdrant |
| **Graph (Neo4j)** | ~ millions of nodes/edges | Brand/category/DMA/banner |
| **Documents** | ~ TBs (contracts, PDFs) | Object storage |
| **Audit logs** | ~ GBs/yr | Immutable |

**Estimate:** low single-digit TB hot; tens of TB warm/cold with history.

## 4. Cache sizing

| Cache | Size | TTL |
|---|---|---|
| **Semantic cache (LLM)** | ~10 GB | 5 min |
| **Redis (sessions/rate limits)** | ~1–2 GB | Session |
| **Query result cache** | ~1 GB | 5 min |
| **CDN** | ~5 GB static | Long |

## 5. Compute (high-level)

| Service | Replicas (peak) | CPU/req |
|---|---|---|
| Copilot BFF | 5–10 | 0.5 vCPU |
| Forecast API | 5–10 | 1 vCPU |
| Agents | 5–10 | 0.5 vCPU |
| Gateway | 2–5 | 0.5 vCPU |
| Kafka | 3 brokers | — |
| Postgres/pgvector | 2 (HA) | — |
| Neo4j | 2 (HA) | — |

## 6. LLM token budget

| Use | Tokens/req | Volume |
|---|---|---|
| Extraction (small model) | ~500 in / 200 out | High (reviews, notes) |
| Narration (frontier) | ~2k in / 500 out | Per scenario |

**Monthly token estimate:** ~100M–500M tokens (illustrative); controlled by semantic cache + small-model routing.

## 7. High-level resource summary

| Resource | Estimate |
|---|---|
| **Compute** | ~50–100 vCPU steady; burst 3× |
| **Memory** | ~100–200 GB |
| **Hot storage** | ~5 TB |
| **Warm/cold** | ~50 TB |
| **Bandwidth** | ~100 Mbps peak (internal) |
| **LLM tokens** | ~100M–500M/month |

## 8. Assumptions & risks

- Planner concurrency ~100; 3× headroom.
- Data volume dominated by sell-out/feature rows.
- LLM cost is the main variable; cache + routing mitigate.
- Validate with load tests before prod sizing.

## 9. Related

- `01_business/10_cost_roi_and_alternatives/cost_and_roi_summary.md`
- `Nestle-USA-DemandSensing-AIArchitect-UseCase/05-quality-and-verification/performance-and-load-reports.md`