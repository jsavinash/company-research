# Network Resilience and Rate Limiting

## 1. Resilience patterns

| Pattern | Use |
|---|---|
| **Retries** | Transient failures |
| **Exponential backoff** | Rate limits / errors |
| **Jitter** | Avoid thundering herd |
| **Circuit breaker** | Downstream failures |
| **Timeouts** | Bounded latency |
| **Bulkheads** | Isolation |

## 2. Retry policy

```
max_retries = 3
base_delay = 200ms
backoff = exponential (2^n) + jitter
retry_on = 429, 500, 502, 503, 504
```

## 3. Circuit breaker

| State | Behavior |
|---|---|
| **Closed** | Normal |
| **Open** | Fail fast (after threshold) |
| **Half-open** | Probe recovery |

## 4. Rate limiting

| Scope | Limit |
|---|---|
| **Per user** | Per tier (see permissions) |
| **Per business unit** | Token budget |
| **Global** | Gateway policy |

- **Token bucket** algorithm.
- **429** with `Retry-After`.

## 5. Batching

- **Batch** forecast requests.
- **Debounce** rapid queries.

## 6. Idempotency

- `Idempotency-Key` header.
- Safe retries.

## 7. Timeouts

| Call | Timeout |
|---|---|
| Copilot | 60 s idle |
| Forecast | 30 s |
| Data | 20 s |

## 8. Observability

- Track retry rates, circuit state, rate-limit hits.
- Alert on anomalies.

## 9. Related

- `01_api_contracts_and_versioning.md`
- `../05_detailed_backend_and_async_design/`