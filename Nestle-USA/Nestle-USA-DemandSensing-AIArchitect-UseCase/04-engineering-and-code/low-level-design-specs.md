# Low-Level Design Specs

## 1. Forecast Agent

**Input:** SKU × store × date, feature vector, forecast horizon, scenario shocks.
**Output:** P10/P50/P90 at store → banner → DMA → national, with run ID.

```
forecast(sku, store, horizon, shocks) -> ForecastResult
  1. fetch features (Feast, point-in-time)
  2. model.predict(...)  # LightGBM / TFT
  3. reconcile(minT)     # hierarchical consistency
  4. attach intervals + run metadata
  5. log to MLflow
```

**Error handling:** on model failure → fall back to last-good forecast; mark degraded.

## 2. Attribution Agent

**Input:** demand delta, candidate drivers (GLP-1, price, mix, distribution).
**Output:** per-driver effect + confidence.

```
attribute(delta, drivers) -> AttributionResult
  1. synthetic_control(dma, donor_pool) -> counterfactual
  2. did(glp1_adoption_ramp) -> effect
  3. placebo_tests()
  4. return effect + sign-consistency check
```

## 3. Scenario Agent

**Input:** natural-language query + policy context.
**Output:** structured scenario result + narrated summary.

```
scenario(query) -> ScenarioResult
  1. parse query -> structured params (LLM, schema-constrained)
  2. call Attribution + Forecast (A2A)
  3. assemble result
  4. narrate (frontier LLM, grounded in run data)
  5. guardrail check (no price advice, cite run ID)
```

## 4. Data Agent

**Input:** data request (banner, DMA, date range).
**Output:** data + quality flags.

```
fetch(request) -> DataResult
  1. check OPA policy (permitted?)
  2. query Snowflake / Iceberg
  3. attach quality flags (stockout censoring, freshness)
  4. return
```

## 5. Governance Agent

**Input:** outbound content + context.
**Output:** approved/redacted content.

```
guard(content) -> Content
  1. PII scan (Purview)
  2. policy check (no price advice, cite run)
  3. redact if needed
  4. return
```

## 6. Intake extraction (LLM)

**Input:** free text (reviews, notes, queries).
**Output:** structured JSON per schema.

```
extract(text, schema) -> JSON
  1. small/fast model with grammar-constrained decoding
  2. validate against schema
  3. slot confidence + missing slots
  4. route to follow-up or safe fallback
```

## 7. Non-functional notes

- All services idempotent.
- All LLM calls through the AI gateway (rate limit, cache, chargeback).
- All data access through OPA + Data Agent (no direct DB access from agents).