# Rendering and Delivery Strategy

## 1. Delivery model

| Aspect | Choice |
|---|---|
| **Front-end** | SPA (React) + SSR where needed |
| **API** | REST (FastAPI) + GraphQL for flexible queries |
| **Real-time** | SSE for streaming answers; WebSocket for live updates |
| **CDN** | Azure Front Door / Cloudflare |
| **Edge** | Static assets at edge; API at regional cluster |

## 2. Rendering strategy

| Content | Rendering |
|---|---|
| Copilot chat | Client-side streaming (SSE) |
| Dashboards | Client-side with server-side data |
| SEO/public pages | SSR (not applicable — internal) |
| Exports | Server-side generation (PDF/Excel) |

## 3. Delivery topology

```
User → Azure Front Door (CDN/WAF) → AKS (copilot BFF) → FastAPI → Agents → Data
```

## 4. Streaming

- **SSE** for token streaming from the copilot.
- **WebSocket** for live dashboard updates (optional).
- **Long-poll** fallback for restricted networks.

## 5. Caching at delivery layer

| Layer | Cache |
|---|---|
| CDN | Static assets |
| Gateway | Semantic cache for LLM calls |
| App | Query result cache |
| Data | Materialized views / pre-aggregation |

## 6. Progressive delivery

- **Canary** (5% → 25% → 50% → 100%).
- **Feature flags** for gradual rollout.
- **Blue-green** for major versions.

## 7. Performance budgets

| Metric | Budget |
|---|---|
| LCP | ≤ 2.5 s |
| INP | ≤ 200 ms |
| CLS | ≤ 0.1 |
| Copilot first token | ≤ 2 s |

## 8. Environments

See `06-operations-and-infrastructure/environments-and-secrets.md` in the platform doc set.