# Memory Management and Resource Pools

## 1. Memory management

| Area | Strategy |
|---|---|
| **Python** | Reference counting + GC; avoid cycles; `weakref` where needed |
| **Node/React** | Avoid leaks: clean up subscriptions/observers; release blobs |
| **JVM (if any)** | Heap sizing; GC tuning |

## 2. Garbage collection tuning

- **Python:** `gc` thresholds; disable GC in short-lived workers where safe.
- **Node:** `--max-old-space-size`; monitor heap.

## 3. Connection pools

| Resource | Pool | Size |
|---|---|---|
| **Postgres / pgvector** | SQLAlchemy pool | 5–20 |
| **Snowflake** | Connector pool | 5–10 |
| **Redis** | Client pool | 10–50 |
| **HTTP (LLM)** | httpx / gateway | 50–100 |

## 4. Memory leak prevention

- **No global caches** without TTL/bounds.
- **LRU** caches (e.g., `functools.lru_cache` with maxsize).
- **Cleanup** on shutdown (lifespan events).
- **Monitoring:** RSS, heap, pool usage.

## 5. Resource limits

- **Kubernetes** requests/limits per pod.
- **OOM killer** avoidance: set memory limits + monitoring.

## 6. Large object handling

- **Streaming** for large payloads (not loading fully).
- **Chunking** for documents.
- **Lazy loading** in front-end.

## 7. Observability

- Memory metrics (Datadog).
- GC pause metrics.
- Pool saturation alerts.

## 8. Related

- `01_concurrency_threading_and_async_model.md`
- `03_synchronization_and_locking.md`