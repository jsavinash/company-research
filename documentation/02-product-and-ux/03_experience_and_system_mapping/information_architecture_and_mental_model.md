# Information Architecture and Mental Model

## 1. Object model

| Object | Attributes | Relationships |
|---|---|---|
| **Forecast run** | run_id, model_version, created_at, status | has many ForecastLine, Attribution |
| **Forecast line** | sku, store, week, p10/p50/p90 | belongs to run |
| **Attribution** | driver, effect, confidence | belongs to run |
| **Scenario** | query, params, result | produces a run |
| **Banner / DMA / Store** | hierarchy | contains stores |
| **Product** | sku, brand, category | sold at stores |
| **Audit event** | user, action, entity, run_id | references run |

## 2. Navigation / IA

```
Home
├── Copilot (ask a scenario)
├── Dashboard (forecast review)
├── Attribution (why)
├── Data quality (caveats)
├── Run history / audit
└── Admin (permissions, model registry)
```

## 3. Mental model

Planners think in terms of:
- **Category → Brand → SKU**
- **Geography → DMA → Banner → Store**
- **Time → Week → Quarter → Horizon**

The IA should mirror this hierarchy so navigation matches the planner's mental model.

## 4. Key screens

| Screen | Purpose | Key elements |
|---|---|---|
| **Copilot** | Ask what-if | Chat, templates, run ID |
| **Dashboard** | Review forecasts | P10/P50/P90, exceptions, freshness |
| **Attribution** | Understand why | Driver breakdown, sign consistency |
| **Run detail** | Audit | Feature snapshot, model version, citations |

## 5. Navigation principles

- **Hierarchy-first:** category → brand → geography → time.
- **Progressive disclosure:** summary → drill-down → run detail.
- **Consistent run IDs:** every answer links to an auditable run.

## 6. Object relationships

```
ForecastRun 1──* ForecastLine
ForecastRun 1──* Attribution
Scenario 1──1 ForecastRun
Banner 1──* Store 1──* ForecastLine
Store 1──* Price / Distribution / Sellout
```

## 7. Mental model validation

- Test with planners: can they find "DiGiorno, Southeast, Q3" in < 3 clicks?
- Can they trace a number to a run ID?
- Do they understand P10/P50/P90?