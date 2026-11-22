# Design Patterns and Principles

## 1. Principles

| Principle | Application |
|---|---|
| **SOLID** | Single-responsibility services; interface-based DI |
| **DRY** | Shared schemas; shared design system |
| **KISS** | Boring, auditable designs |
| **YAGNI** | Build for current scope |

## 2. Patterns used

| Pattern | Where | Purpose |
|---|---|---|
| **Strategy** | `GroundingVerifier`, `Retriever` | Swap retrieval/verification |
| **Strategy** | `ModelRouter` (small/frontier) | Route by task |
| **Observer** | Eval event bus | Decouple notification |
| **Factory** | Model / agent construction | Centralized creation |
| **Repository** | Data access | Abstraction over stores |
| **Adapter** | LLM provider adapter | Uniform interface over Azure/Bedrock/Vertex |
| **Facade** | Copilot BFF | Simplify front-end calls |

## 3. Creational / Structural / Behavioral

| Category | Patterns |
|---|---|
| **Creational** | Factory, Builder (scenario params) |
| **Structural** | Adapter, Facade, Repository |
| **Behavioral** | Strategy, Observer, State |

## 4. Anti-patterns

- **God object** — split by domain.
- **Singleton abuse** — use DI.
- **LLM-as-decider** — forbidden.

## 5. Example — Strategy

```python
class GroundingVerifier(Protocol):
    def verify(self, claim: str, chunks: list[Chunk]) -> bool: ...

class NliVerifier(GroundingVerifier): ...
```

## 6. Related

- `02_class_interface_and_model_definitions.md`