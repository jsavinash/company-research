# Error Handling and Resilience Code

## 1. Exception hierarchy

```
DomainError
├── ValidationError
├── PermissionDeniedError
├── IntakeError
│   └── SchemaValidationError
├── CoachingError
│   ├── RetrievalError
│   ├── GroundingError
│   └── RefusalError
├── MedicalScopeError
└── UpstreamError
    ├── LLMError
    └── RateLimitError
```

## 2. Result / Either types

- Prefer **exceptions** for exceptional paths.
- **Result** type for recoverable outcomes.

```python
@dataclass
class Result(Generic[T]):
    ok: bool
    value: T | None = None
    error: Exception | None = None
```

## 4. Validation

- **Pydantic** at boundaries.
- **Schema validation** for LLM outputs.
- **Fail fast** on invalid input.

## 5. Error mapping (HTTP)

| Exception | HTTP |
|---|---|
| ValidationError | 400 |
| PermissionDeniedError | 403 |
| RateLimitError | 429 |
| UpstreamError | 502/503 |
| DomainError | 500 |

## 6. Error responses (RFC 7807)

```json
{
  "type": "https://api/.../permission-denied",
  "title": "Permission denied",
  "status": 403,
  "detail": "No access to this pet profile"
}
```

## 7. Resilience patterns

| Pattern | Use |
|---|---|
| **Retry** | Transient errors |
| **Circuit breaker** | Downstream |
| **Fallback** | Cached / generic |
| **Timeout** | Bounded latency |

## 8. Logging

- No PII / secrets.
- Structured logs with session/run ID.