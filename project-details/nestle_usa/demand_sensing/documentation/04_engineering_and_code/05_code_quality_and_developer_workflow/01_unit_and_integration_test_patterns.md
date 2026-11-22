# Unit and Integration Test Patterns

## 1. Test pyramid

| Level | Scope | Tools |
|---|---|---|
| **Unit** | Functions, services | pytest, Jest |
| **Integration** | DB, gateway, OPA | pytest, Testcontainers |
| **Contract** | API, MCP | Schemathesis, Pact |
| **E2E** | Copilot journey | Playwright |
| **Eval (ML)** | Forecast accuracy | MLflow, eval harness |

## 2. Unit test patterns

- **Arrange-Act-Assert.**
- **One behavior per test.**
- **Deterministic** (no sleeps, no network).
- **Fast** (< 100ms).

```python
def test_run_forecast_returns_intervals():
    svc = ForecastService(repo=FakeRepo(), model=StubModel())
    result = svc.run_forecast("SKU1", ["S1"], 12)
    assert result.forecasts[0].p10 < result.forecasts[0].p90
```

## 3. Mocking / test doubles

| Double | Use |
|---|---|
| **Stub** | Fixed return |
| **Mock** | Verify calls |
| **Fake** | In-memory implementation |
| **Spy** | Observe calls |

- Mock at **boundaries** (DB, LLM, HTTP), not internals.
- Prefer **fakes** over mocks for domain logic.

## 4. Fixtures

- **pytest fixtures** for setup.
- **Factory functions** for entities.
- **Golden files** for complex outputs.

## 5. Coverage targets

| Area | Target |
|---|---|
| **Domain services** | ≥ 90% |
| **API layer** | ≥ 80% |
| **Overall** | ≥ 80% |

## 6. Integration tests

- **Testcontainers** for Postgres/Redis/Kafka.
- **LocalStack** for S3.
- **OPA** with test policies.

## 7. Test data

- Synthetic, PII-free.
- Golden datasets.
- Edge cases (thin data, stockouts).

## 8. CI

- Run on every PR.
- Fail on regression.

## 9. Related

- `02_git_workflow_and_code_review_guide.md`
- `06_reference_implementation/tests/`