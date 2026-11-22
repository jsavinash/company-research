# Network Resilience and Rate Limiting

## 1. Resilience patterns

| Pattern | Use |
|---|---|
| **Retries** | Transient failures |
| **Exponential backoff** | Rate limits / errors |
| **Jitter** | Avoid thundering herd |
| **Circuit breaker** | Downstream failures |
| **Timeouts** | Bounded latency |

## 2. Retry policy

```
max_retries = 3
base_delay = 200ms
backoff = exponential (2^n) + jitter
retry_on = 429, 500, 502, 503, 504
```

## 4. Circuit breaker

| State | Behavior |
|---|---|
| **Closed** | Normal |
| **Open** | Fail fast (after threshold) |
| **Half-open** | Probe recovery |

## 5. Rate limiting

| Scope | Limit |
|---|---|
| **Per user** | Per tier |
| **Per business unit** | Token budget |
| **Global** | Gateway policy |

- **Token bucket** algorithm.
- **429** with `Retry-After`.

## 6. Batching

- **Batch** forecast requests.
- **Debounce** rapid queries.

## 7. Idempotency

- `Idempotency-Key` header.
- Safe retries.

## 8. Timeouts

| Call | Timeout |
|---|---|
| Copilot | 60 s idle |
| Intake | 30 s |
| Data | 20 s |

## 9. Observability

- Track retry rates, circuit state, rate-limit hits.
- Alert on anomalies.