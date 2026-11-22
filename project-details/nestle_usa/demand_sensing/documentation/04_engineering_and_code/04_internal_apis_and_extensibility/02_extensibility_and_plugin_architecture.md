# Extensibility and Plugin Architecture

## 1. Extension points

| Point | Mechanism |
|---|---|
| **Attribution methods** | Strategy interface (`AttributionStrategy`) |
| **Model providers** | Adapter interface (`LLMProvider`) |
| **Forecast models** | `ForecastModel` interface |
| **Data connectors** | Connector interface |
| **Agents** | Agent registration |
| **Tools (MCP)** | Tool registry |

## 2. Strategy / Observer hooks

- **Strategy:** swap causal methods (synthetic control / DiD) without changing callers.
- **Observer:** agents subscribe to events (run.completed, model.deployed).

```python
class AttributionService:
    def __init__(self, strategy: AttributionStrategy):
        self.strategy = strategy
```

## 3. Middleware

- **FastAPI middleware:** auth, rate limit, logging.
- **Gateway middleware:** routing, cache, chargeback.
- **Agent middleware:** guardrails, tracing.

## 4. Feature flags

- **LaunchDarkly / custom.**
- **Per-module flags** (e.g., `copilot_v2`, `small_model_routing`).
- **Gradual rollout.**

## 5. Plugin registration

```python
PLUGINS: dict[str, ForecastModel] = {}

def register(name: str, model: ForecastModel) -> None:
    PLUGINS[name] = model
```

## 6. Extension guidelines

- **Open/Closed:** open for extension, closed for modification.
- **Interface-first:** depend on abstractions.
- **No core changes** for new strategies/providers.

## 7. Versioning of extensions

- Extensions declare compatibility (`>=1.0,<2.0`).
- Registry validates at load.

## 8. Testing extensions

- Contract tests for interfaces.
- Plugin smoke tests.

## 9. Related

- `01_public_methods_and_sdk_contracts.md`
- `03_design_patterns_and_principles.md`