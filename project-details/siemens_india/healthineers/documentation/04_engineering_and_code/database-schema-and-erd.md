# Database Schema and ERD

## 1. Core entities

```
Study (study_id PK, site_id, device_class, acquisition_params, acquired_at)
Finding (finding_id PK, study_id FK, type, confidence, calibrated_confidence, heatmap_ref)
Calibration (site_id, model_version, slope, intercept, prevalence, updated_at)
Model (model_id PK, version, type, metrics, created_at)
ReviewAction (action_id PK, study_id FK, radiologist_id, action, reason, timestamp)
AuditEvent (event_id PK, study_id FK, action, user_id, timestamp)
```

## 2. ERD (text)

```
Study ||--o{ Finding : has
Study ||--o{ ReviewAction : reviewed_by
Model ||--o{ Calibration : versions
Study ||--o{ AuditEvent : audited_by
```

## 3. Key design points

- **Per-site calibration** stored with each model version.
- **Device class + acquisition params** captured as features.
- **Immutable prediction logs** (model version, device, calibration set) for audit.
- **Review actions** as labels.

## 4. Example DDL (PostgreSQL)

```sql
CREATE TABLE study (
  study_id      UUID PRIMARY KEY,
  site_id       TEXT,
  device_class  TEXT,
  acquisition   JSONB,
  acquired_at   TIMESTAMP
);

CREATE TABLE finding (
  finding_id            UUID PRIMARY KEY,
  study_id              UUID REFERENCES study(study_id),
  type                  TEXT,
  confidence            DOUBLE PRECISION,
  calibrated_confidence DOUBLE PRECISION,
  heatmap_ref           TEXT
);

CREATE TABLE calibration (
  site_id       TEXT,
  model_version TEXT,
  slope         DOUBLE PRECISION,
  intercept     DOUBLE PRECISION,
  prevalence    DOUBLE PRECISION,
  updated_at    TIMESTAMP
);
```

## 5. Indexing

| Table | Index |
|---|---|
| Finding | (study_id) |
| Calibration | (site_id, model_version) |
| ReviewAction | (study_id, timestamp) |
| AuditEvent | (study_id, timestamp) |

## 6. Governance

- Per-site isolation; de-identification.
- Regulatory-grade audit (MDR/FDA/CDSCO).
- Retention per policy.