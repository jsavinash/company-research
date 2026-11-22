# Database Schema and ERD

## 1. Core entities

```
Contract (contract_id PK, customer_id, asset_class, contract_type, start_date, exposure)
Customer (customer_id PK, firmographics, segment, region)
Payment (payment_id PK, contract_id FK, due_date, paid_date, dpd, amount)
Telemetry (telemetry_id PK, asset_id FK, date, utilization, downtime, service_deferral, energy)
Score (score_id PK, contract_id FK, as_of_date, pd, pd_calibrated, tte_p10, tte_p50, tte_p90, flag, model_version)
ReasonCode (score_id FK, feature, contribution, direction)
Model (model_id PK, version, type, metrics, created_at)
AuditEvent (event_id PK, score_id FK, action, user_id, timestamp)
```

## 2. ERD (text)

```
Customer ||--o{ Contract : has
Contract ||--o{ Payment : has
Contract ||--o{ Score : scored_by
Score ||--o{ ReasonCode : explains
Model ||--o{ Score : versions
```

## 3. Key design points

- **Point-in-time:** every score carries `as_of_date`.
- **Model version** on every score (audit).
- **Reason codes** stored with each score.
- **Telemetry** joined per contract under governance.

## 4. Example DDL (PostgreSQL)

```sql
CREATE TABLE contract (
  contract_id   UUID PRIMARY KEY,
  customer_id   UUID,
  asset_class   TEXT,
  contract_type TEXT,
  start_date    DATE,
  exposure      DOUBLE PRECISION
);

CREATE TABLE score (
  score_id       UUID PRIMARY KEY,
  contract_id    UUID REFERENCES contract(contract_id),
  as_of_date     DATE,
  pd             DOUBLE PRECISION,
  pd_calibrated  DOUBLE PRECISION,
  tte_p10        DOUBLE PRECISION,
  tte_p50        DOUBLE PRECISION,
  tte_p90        DOUBLE PRECISION,
  flag           TEXT,
  model_version  TEXT
);

CREATE TABLE reason_code (
  score_id     UUID REFERENCES score(score_id),
  feature      TEXT,
  contribution DOUBLE PRECISION,
  direction    TEXT
);
```

## 5. Indexing

| Table | Index |
|---|---|
| Score | (contract_id, as_of_date) |
| Payment | (contract_id, due_date) |
| Telemetry | (asset_id, date) |
| ReasonCode | (score_id) |

## 6. Governance

- Per-entity isolation; de-identification.
- Model risk (SR 11-7) versioning.
- Retention per policy.