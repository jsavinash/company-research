# Design Patterns and Principles

OOP, SOLID, DRY, and the patterns used in the platform.

## 1. Principles

| Principle | Application |
|---|---|
| **SOLID** | Single-responsibility services; interface-based DI |
| **DRY** | Shared design system; shared feature contracts |
| **KISS** | Boring, auditable designs |
| **YAGNI** | Build for current scope; extend via strategies |

## 2. Patterns used

| Pattern | Where | Purpose |
|---|---|---|
| **Strategy** | `AttributionStrategy` (synthetic control / DiD) | Swap causal methods |
| **Strategy** | `ModelRouter` (small / frontier) | Route by task |
| **Observer** | Agent event bus; metrics | Decouple notification |
| **Factory** | Model / agent construction | Centralized creation |
| **Repository** | Data access | Abstraction over stores |
| **Adapter** | LLM provider adapter | Uniform interface over Azure/Bedrock/Vertex |
| **Facade** | Copilot BFF | Simplify front-end calls |
| **Saga** | Forecast publish / model promotion | Distributed transactions |
| **Circuit Breaker** | Downstream calls | Resilience |

## 3. Creational / Structural / Behavioral

| Category | Patterns |
|---|---|
| **Creational** | Factory, Builder (scenario params) |
| **Structural** | Adapter, Facade, Repository |
| **Behavioral** | Strategy, Observer, State, Saga |

## 4. Anti-patterns to avoid

- **God object** — split by domain.
- **Singleton abuse** — use DI.
- **Anemic domain** — keep behavior with data.
- **Distributed monolith** — clear boundaries.

## 5. Example — Strategy pattern

```python
class AttributionStrategy(Protocol):
    def attribute(self, delta: float, drivers: list[str]) -> list[DriverEffect]: ...

class SyntheticControl(AttributionStrategy): ...
class DiffInDiff(AttributionStrategy): ...

class AttributionService:
    def __init__(self, strategy: AttributionStrategy):
        self.strategy = strategy
```

## 6. Related

- `02_class_interface_and_model_definitions.md`
- `06_reference_implementation/src/strategies/`