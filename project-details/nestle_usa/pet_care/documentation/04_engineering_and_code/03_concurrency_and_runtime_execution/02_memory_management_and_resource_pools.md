# Memory Management and Resource Pools

## 1. Memory management

| Area | Strategy |
|---|---|
| **Python** | Reference counting + GC; avoid cycles |
| **Node/React** | Clean up subscriptions; release blobs |

## 2. GC tuning

- **Python:** `gc` thresholds.
- **Node:** `--max-old-space-size`.

## 3. Connection pools

| Resource | Pool | Size |
|---|---|---|
| **Postgres / pgvector** | SQLAlchemy pool | 5–20 |
| **Snowflake** | Connector pool | 5–10 |
| **Redis** | Client pool | 10–50 |
| **HTTP (LLM)** | httpx | 50–100 |

## 4. Memory leak prevention

- **No global caches** without TTL/bounds.
- **LRU** caches with maxsize.
- **Cleanup** on shutdown.

## 5. Resource limits

- **Kubernetes** requests/limits per pod.
- **OOM killer** avoidance.

## 6. Large object handling

- **Streaming** for large payloads.
- **Chunking** for documents.

## 7. Monitoring

- Memory metrics (Datadog).
- GC pause metrics.
- Pool saturation alerts.