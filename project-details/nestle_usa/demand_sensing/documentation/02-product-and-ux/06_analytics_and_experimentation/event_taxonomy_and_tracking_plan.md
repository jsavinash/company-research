# Event Taxonomy and Tracking Plan

## 1. Event taxonomy

Events follow `object_action` naming, with common properties.

### Common properties

| Property | Type | Example |
|---|---|---|
| `user_id` | string | hashed |
| `role` | string | planner |
| `team` | string | frozen |
| `session_id` | string | |
| `timestamp` | ISO8601 | |
| `app_version` | string | |
| `env` | string | prod |

### 1.1 Onboarding

| Event | Properties |
|---|---|
| `signin` | method (entra) |
| `onboarding_started` | |
| `onboarding_completed` | |

### 1.2 Scenario / copilot

| Event | Properties |
|---|---|
| `scenario_submitted` | query_length, brands, dmas, horizon |
| `scenario_answered` | run_id, latency_ms, model |
| `scenario_attribution_viewed` | run_id, drivers |
| `scenario_shared` | run_id, channel |
| `scenario_failed` | reason |

### 1.3 Forecast / dashboard

| Event | Properties |
|---|---|
| `forecast_viewed` | run_id, scope |
| `forecast_exception_clicked` | sku, delta |
| `forecast_accepted` | run_id |
| `forecast_annotated` | run_id, note |
| `forecast_exported` | format |

### 1.4 Data quality / permissions

| Event | Properties |
|---|---|
| `data_quality_flag_viewed` | flag_type |
| `access_requested` | banner, dma |
| `access_denied` | reason (opa) |
| `access_granted` | banner |

### 1.5 Governance / audit

| Event | Properties |
|---|---|
| `run_audited` | run_id |
| `audit_exported` | range |

## 2. Tracking plan rules

- **One event per user action**, not per system event.
- **Immutable:** events are append-only.
- **PII-free:** no names, emails, or household data in events.
- **Versioned:** schema version in every event.
- **Governed:** reviewed by data steward.

## 3. Event → metric mapping

| Event | Metric |
|---|---|
| `scenario_submitted` | Scenario usage |
| `scenario_answered` | Time-to-answer |
| `forecast_accepted` | Acceptance rate |
| `signin` + `scenario_submitted` | Activation |

## 4. Instrumentation points

- Copilot front-end (TypeScript).
- Forecast API (FastAPI).
- AI gateway (token/latency).
- OPA (access decisions).
- MLflow / LangSmith (model runs).

## 5. Data pipeline

```
Events → Kafka → Snowflake → dbt → dashboards
```

## 6. Quality checks

- Event schema validation.
- Volume / null-rate monitoring.
- PII scan.

## 7. Privacy

- Hash user IDs.
- No household-level data.
- Retention per policy.