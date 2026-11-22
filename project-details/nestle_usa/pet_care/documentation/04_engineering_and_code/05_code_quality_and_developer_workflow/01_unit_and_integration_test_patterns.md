# Unit and Integration Test Patterns

## 1. Test levels

| Level | Scope | Tools |
|---|---|---|
| **Unit** | Extractors, verifiers, routing | pytest, Jest |
| **Integration** | Intake → plan → coaching | pytest, Testcontainers |
| **Contract** | API schemas, MCP | Schemathesis, Pact |
| **Evaluation (ML)** | Slot accuracy, grounding | MLflow, eval harness |
| **Adversarial** | Injection, thin profile | Braintrust, promptfoo |

## 2. Unit test patterns

- **Arrange-Act-Assert.**
- **One behavior per test.**
- **Deterministic** (no sleeps, no network).

```python
def test_extract_returns_slots():
    ex = IntakeExtractor(model=StubModel())
    profile = ex.extract("chunky 3-yr-old lab")
    assert profile.species == "dog"
    assert profile.completeness < 1.0
```

## 3. Mocking / test doubles

| Double | Use |
|---|---|
| **Stub** | Fixed LLM response |
| **Mock** | Verify calls |
| **Fake** | In-memory retriever |

## 4. Fixtures

- **pytest fixtures** for setup.
- **Factory functions** for profiles.
- **Golden files** for complex outputs.

## 5. Coverage targets

| Area | Target |
|---|---|
| **Domain services** | ≥ 90% |
| **API layer** | ≥ 80% |
| **Overall** | ≥ 80% |

## 6. Integration tests

- **Testcontainers** for Postgres/Redis.
- **Fake retriever** for RAG.
- **OPA** with test policies.

## 7. Test data

- Synthetic, PII-free.
- Adversarial prompts.

## 8. CI

- Run on every PR.
- Fail on regression.