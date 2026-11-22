# Extensibility and Plugin Architecture

## 1. Extension points

| Point | Mechanism |
|---|---|
| **Retrievers** | `Retriever` interface |
| **Generators** | `Generator` interface |
| **Verifiers** | `GroundingVerifier` interface |
| **Models** | Model registry |
| **Tools (MCP)** | Tool registry |

## 2. Strategy / Observer hooks

- **Strategy:** swap retrievers/verifiers without changing callers.
- **Observer:** eval event bus.

```python
class CoachingService:
    def __init__(self, retriever: Retriever, verifier: GroundingVerifier):
        self.retriever = retriever
        self.verifier = verifier
```

## 4. Middleware

- **Gateway middleware:** routing, cache, chargeback.
- **Agent middleware:** guardrails, tracing.

## 5. Feature flags

| Flag | Purpose |
|---|---|
| `copilot_v2` | New copilot UX |
| `small_model_intake` | Cost optimization |
| `grounding_verifier` | Safety check |

## 6. Plugin registration

```python
RETRIEVERS: dict[str, Retriever] = {}

def register(name: str, r: Retriever) -> None:
    RETRIEVERS[name] = r
```

## 7. Extension guidelines

- **Open/Closed:** open for extension, closed for modification.
- **Interface-first:** depend on abstractions.
- **No core changes** for new strategies.

## 8. Testing extensions

- Contract tests for interfaces.
- Plugin smoke tests.