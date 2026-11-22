# Rendering and Delivery Strategy

## 1. Delivery model

| Aspect | Choice |
|---|---|
| **Front-end** | SPA (React) |
| **API** | REST (FastAPI) |
| **Real-time** | SSE for streaming coaching |
| **CDN** | Azure Front Door |
| **Edge** | Static assets at edge |

## 2. Rendering

| Content | Rendering |
|---|---|
| Copilot chat | Client-side streaming (SSE) |
| Plan | Client-side with server-side data |
| Vet summary | Client-side |

## 3. Streaming

- **SSE** for token streaming from coaching.
- **Fallback** to non-streaming if SSE unavailable.

## 4. Caching

| Layer | Cache |
|---|---|
| CDN | Static assets |
| Gateway | Semantic cache for LLM calls |
| App | Query result cache |

## 5. Progressive delivery

- **Canary** (5% → 25% → 50% → 100%).
- **Feature flags** for gradual rollout.

## 6. Performance budgets

| Metric | Budget |
|---|---|
| First token | ≤ 2 s |
| Full answer | ≤ 5 s |

## 7. Environments

- dev → staging → prod (see `../06-operations-and-infrastructure/`).