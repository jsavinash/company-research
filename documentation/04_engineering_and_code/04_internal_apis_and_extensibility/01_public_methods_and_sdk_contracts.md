# Public Methods and SDK Contracts

## 1. Public interfaces

| Interface | Methods |
|---|---|
| **ForecastModel** | `predict(features) -> ForecastLine[]` |
| **AttributionStrategy** | `attribute(delta, drivers) -> DriverEffect[]` |
| **ModelRouter** | `route(task) -> ModelTier` |
| **Repository** | `get(id)`, `save(entity)`, `list(query)` |
| **CopilotService** | `ask(query, context) -> ScenarioResult` |

## 2. Method signatures

```python
class ForecastService:
    def run_forecast(
        self,
        sku_id: str,
        store_ids: list[str],
        horizon_weeks: int,
        shocks: dict[str, float] | None = None,
    ) -> ForecastResult: ...

class AttributionService:
    def attribute(
        self,
        delta: float,
        drivers: list[str],
    ) -> list[DriverEffect]: ...
```

## 3. Interface contracts

- **Input validation** at boundaries (Pydantic).
- **Explicit errors** (custom exception hierarchy).
- **Idempotent** methods where applicable.
- **Versioned** public APIs.

## 4. SDK contracts

- **OpenAPI** as source of truth for REST.
- **Generated clients** for TypeScript/Python.
- **SemVer** for SDK releases.

## 5. Versioning

| Layer | Strategy |
|---|---|
| **Public API** | URI versioning (`/v1`) |
| **Internal methods** | SemVer + deprecation |
| **SDK** | SemVer |

## 6. Backward compatibility

- **Additive** changes preferred.
- **Deprecation** with sunset headers.
- **N-2** support window.

## 7. Documentation

- Docstrings (Python), TSDoc (TS).
- Examples in OpenAPI.
- Changelog.

## 8. Related

- `02_extensibility_and_plugin_architecture.md`
- `../07_api_and_network_communication/01_api_contracts_and_versioning.md`