# Reference Implementation — Demand Sensing Core

Runnable LLD reference implementation demonstrating the domain model, state machine, strategy pattern, and per-key locking used by the Agentic GLP-1 Demand Sensing platform. Pure Python standard library — no external dependencies required to run the tests.

## Layout

```
06_reference_implementation/
├── src/
│   ├── models/         # Entities, value objects, enums
│   ├── services/       # Business logic + locking wrappers
│   ├── strategies/     # Pluggable interfaces (Strategy pattern)
│   └── exceptions/     # Domain exception hierarchy
└── tests/
    ├── unit/           # Isolated component & state transition tests
    └── concurrency/    # Race condition & thread-safety tests
```

## Key design points demonstrated

| Concept | Where |
|---|---|
| **State machine** (Queued → Running → Succeeded/Failed) | `src/models/entities.py` (`ForecastRun`) |
| **Value objects** with invariants | `src/models/value_objects.py` (`Interval`, `DriverEffect`) |
| **Strategy pattern** (swappable attribution) | `src/strategies/attribution_strategy.py` |
| **Model routing** (small vs frontier) | `src/strategies/model_router.py` |
| **Per-key locking** (no duplicate concurrent runs) | `src/services/forecast_service.py` (`_LockRegistry`) |
| **Exception hierarchy** | `src/exceptions/base.py` |

## Run the tests

```bash
cd 06_reference_implementation
python -m unittest discover -s tests -v
# or, with pytest installed:
pytest -q
```

## Notes

- This is a **reference/sample** implementation of the design, not production code.
- The forecast model is a deterministic stub; swap in LightGBM/TFT behind the same interface.
- The attribution strategies are stubs illustrating the Strategy pattern; replace with synthetic control / DiD.
- Concurrency tests use threads to demonstrate that per-(sku, store) locks serialize access.