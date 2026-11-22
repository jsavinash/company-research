# Event Taxonomy and Tracking Plan

## 1. Event taxonomy

Events follow `object_action` naming with common properties.

### Common properties

| Property | Type | Example |
|---|---|---|
| `user_id` | string | hashed |
| `session_id` | string | |
| `timestamp` | ISO8601 | |
| `app_version` | string | |
| `env` | string | prod |

### 1.1 Onboarding

| Event | Properties |
|---|---|
| `signin` | method |
| `intake_started` | |
| `intake_completed` | slots_filled, completeness |

### 1.2 Coaching

| Event | Properties |
|---|---|
| `coaching_requested` | plan_id, query |
| `coaching_answered` | run_id, latency_ms, model |
| `citation_viewed` | chunk_id |
| `coaching_refused` | reason |

### 1.3 Vet

| Event | Properties |
|---|---|
| `vet_summary_viewed` | plan_id |
| `vet_endorsed` | plan_id |
| `vet_overridden` | plan_id, reason |

### 1.4 Safety

| Event | Properties |
|---|---|
| `medical_question_routed` | |
| `injection_blocked` | |
| `pii_redacted` | |

## 2. Event → metric mapping

| Event | Metric |
|---|---|
| `intake_completed` | Activation |
| `coaching_answered` | Time-to-answer |
| `vet_endorsed` | Endorsement rate |
| `signin` + `intake_completed` | Funnel |

## 3. Instrumentation points

- Copilot front-end (TypeScript).
- Intake/coaching API (Python).
- AI gateway (token/latency).
- OPA (access decisions).
- LangSmith (agent traces).

## 4. Data pipeline

```
Events → Kafka → Snowflake → dbt → dashboards
```

## 5. Privacy

- Hash user IDs.
- No PII in events.
- Retention per policy.