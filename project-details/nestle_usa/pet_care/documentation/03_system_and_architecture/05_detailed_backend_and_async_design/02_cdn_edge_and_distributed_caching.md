# CDN, Edge, and Distributed Caching

## 1. Caching layers

| Layer | Cache | TTL |
|---|---|---|
| **CDN / edge** | Static assets | Long (hashed) |
| **API gateway** | Semantic cache (LLM) | 5 min |
| **Application** | Query result cache | 5 min |
| **Data** | Materialized views | Nightly |

## 2. CDN / edge

- **Azure Front Door / Cloudflare.**
- Static assets at edge.
- WAF + TLS.

## 3. Distributed cache

| Store | Use |
|---|---|
| **Redis** | Session, rate limits, semantic cache |
| **In-memory** | Per-service LRU |

## 4. Semantic caching

- Cache LLM responses by semantic similarity.
- **Hit** on repeated pet/profile queries.
- **Invalidate** on model/prompt change.
- **Target:** 40% hit rate.

## 5. Invalidation strategies

| Strategy | Use |
|---|---|
| **TTL** | Time-based |
| **Write-through** | Updates |
| **Event-based** | On data change |

## 6. Cache keys

- Include: query, profile, model version, permissions.
- Avoid PII in keys.

## 7. Stampede protection

- **Request coalescing.**
- **Early recompute.**
- **Lock** on miss.

## 8. Monitoring

- Hit rate, latency, memory.
- Alert on hit-rate drop.