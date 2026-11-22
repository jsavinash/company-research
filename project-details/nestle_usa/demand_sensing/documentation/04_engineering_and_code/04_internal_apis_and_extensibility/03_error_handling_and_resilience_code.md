# Error Handling and Resilience Code

## 1. Exception hierarchy

```
DomainError
├── ValidationError
├── PermissionDeniedError
├── NotFoundError
├── ForecastError
│   ├── InsufficientDataError
│   └── ModelDegradedError
├── AttributionError
│   └── SignInconsistencyError
├── UpstreamError
│   ├── LLMError
   │   └── RateLimitError
│   └── DataPlatformError
└── PolicyViolationError
```

## 2. Result / Either types

- Prefer **exceptions** for exceptional paths.
- **Result** type for recoverable outcomes (e.g., `Result[ForecastResult, ForecastError]`).

```python
@dataclass
class Result(Generic[T]):
    ok: bool
    value: T | None = None
    error: Exception | None = None
```

## 3. Validation

- **Pydantic** at boundaries.
- **Explicit checks** for business rules.
- **Fail fast** on invalid input.

## 4. Error mapping (HTTP)

| Exception | HTTP |
|---|---|
| ValidationError | 400 |
| PermissionDeniedError | 403 |
| NotFoundError | 404 |
| RateLimitError | 429 |
| UpstreamError | 502/503 |
| DomainError | 500 |

## 5. Resilience patterns

| Pattern | Use |
|---|---|
| **Retry** | Transient errors |
| **Circuit breaker** | Downstream |
| **Fallback** | Last-good forecast |
| **Timeout** | Bounded latency |
| **Bulkhead** | Isolation |

## 6. Error responses (RFC 7807)

```json
{
  "type": "https://api/.../permission-denied",
  "title": "Permission denied",
  "status": 403,
  "detail": "No access to banner B-123"
}
```

## 7. Logging

- Structured logs with run ID.
- No PII / secrets.
- Error context (stack, inputs sanitized).

## 8. Testing

- Unit tests for each exception path.
- Chaos tests for resilience.

## 9. Related

- `06_reference_implementation/src/exceptions/`
- `../05_detailed_backend_and_async_design/`