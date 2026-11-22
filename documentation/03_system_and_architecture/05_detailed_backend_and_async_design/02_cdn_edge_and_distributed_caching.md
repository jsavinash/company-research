# CDN, Edge, and Distributed Caching

## 1. Caching layers

| Layer | Cache | TTL |
|---|---|---|
| **CDN / edge** | Static assets | Long (hashed) |
| **API gateway** | Semantic cache (LLM) | 5 min |
| **Application** | Query result cache | 5 min |
| **Data** | Materialized views | Nightly |
| **Client** | React Query / IndexedDB | 5 min / session |

## 2. CDN / edge

- **Azure Front Door / Cloudflare.**
- Static assets at edge.
- WAF + TLS.
- Compression (Brotli).

## 3. Distributed cache

| Store | Use |
|---|---|
| **Redis** | Session, rate limits, semantic cache |
| **Memcached** | Simple key-value (optional) |
| **In-memory** | Per-service LRU |

## 4. Semantic caching

- Cache LLM responses by semantic similarity.
- **Hit** on repeated retailer/category queries.
- **Invalidate** on model/prompt change.
- **Target:** 40% hit rate.

## 5. Invalidation strategies

| Strategy | Use |
|---|---|
| **TTL** | Time-based |
| **Write-through** | Updates |
| **Write-behind** | Async |
| **Event-based** | On data change |

## 6. Cache keys

- Include: query, banners, dmas, model version, permissions.
- Avoid PII in keys.

## 7. Stampede protection

- **Request coalescing.**
- **Early recompute** (probabilistic).
- **Lock** on miss.

## 8. Monitoring

- Hit rate, latency, memory.
- Alert on hit-rate drop.

## 9. Related

- `02_event_queues_and_background_jobs.md`
- `../04_detailed_frontend_architecture/02_state_management_and_client_cache.md`