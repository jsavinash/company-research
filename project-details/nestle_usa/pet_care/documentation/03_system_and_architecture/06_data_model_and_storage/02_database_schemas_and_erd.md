# Database Schemas and ERD

## 1. Core entities

```
PetProfile (pet_id PK, owner_id, species, breed, age, condition, allergy, preference, completeness)
Plan (plan_id PK, pet_id FK, formula, portion, rationale, model_version)
CoachingSession (session_id PK, plan_id FK, query, response, citations, latency)
VetSummary (summary_id PK, plan_id FK, facts, prose, endorsement)
AuditEvent (event_id PK, session_id FK, action, user_id, timestamp)
```

## 2. ERD (text)

```
PetProfile ||--o{ Plan : has
Plan ||--o{ CoachingSession : has
Plan ||--o{ VetSummary : has
CoachingSession ||--o{ AuditEvent : audited_by
```

## 4. Example DDL (PostgreSQL)

```sql
CREATE TABLE pet_profile (
  pet_id       UUID PRIMARY KEY,
  owner_id     TEXT,
  species      TEXT,
  breed        TEXT,
  age_years    DOUBLE PRECISION,
  condition    JSONB,
  allergy      JSONB,
  preference   JSONB,
  completeness DOUBLE PRECISION
);

CREATE TABLE plan (
  plan_id       UUID PRIMARY KEY,
  pet_id        UUID REFERENCES pet_profile(pet_id),
  formula       TEXT,
  portion       TEXT,
  rationale     TEXT,
  model_version TEXT
);

CREATE TABLE coaching_session (
  session_id  UUID PRIMARY KEY,
  plan_id     UUID REFERENCES plan(plan_id),
  query       TEXT,
  response    TEXT,
  citations   JSONB,
  latency_ms  INT
);
```

## 5. Indexing

| Table | Index |
|---|---|
| Plan | (pet_id) |
| CoachingSession | (plan_id) |
| AuditEvent | (session_id, timestamp) |

## 6. Governance

- Per-owner isolation.
- PII redaction.
- Retention per policy.