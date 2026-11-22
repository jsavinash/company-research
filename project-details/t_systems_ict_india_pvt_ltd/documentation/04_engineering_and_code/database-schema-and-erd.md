# Database Schema and ERD

## 1. Core entities

```
Product (sku_id PK, title, brand, category, price, attributes, updated_at)
User (user_id PK, anon_id, context)
Session (session_id PK, user_id FK, started_at, events)
Interaction (interaction_id PK, session_id FK, sku_id FK, position, event_type, model_version, timestamp)
Model (model_id PK, version, type, metrics, created_at)
FeatureSnapshot (snapshot_id PK, model_id FK, as_of_date, features)
```

## 2. ERD (text)

```
User ||--o{ Session : has
Session ||--o{ Interaction : records
Product ||--o{ Interaction : involved_in
Model ||--o{ FeatureSnapshot : versions
```

## 3. Key design points

- **Position + impression** stored with every interaction (position-bias control).
- **Model version** on every interaction (label provenance).
- **Time-ordered outcomes** (click → cart → order).
- **Feature snapshots** for point-in-time correctness.

## 4. Example DDL (PostgreSQL / data warehouse)

```sql
CREATE TABLE product (
  sku_id      TEXT PRIMARY KEY,
  title       TEXT,
  brand       TEXT,
  category    TEXT,
  price       DOUBLE PRECISION,
  attributes  JSONB,
  updated_at  TIMESTAMP
);

CREATE TABLE interaction (
  interaction_id  UUID PRIMARY KEY,
  session_id      UUID,
  sku_id          TEXT REFERENCES product(sku_id),
  position        INT,
  event_type      TEXT,
  model_version   TEXT,
  timestamp       TIMESTAMP
);

CREATE TABLE model (
  model_id    UUID PRIMARY KEY,
  version     TEXT,
  type        TEXT,
  metrics     JSONB,
  created_at  TIMESTAMP
);
```

## 5. Indexing

| Table | Index |
|---|---|
| Interaction | (session_id, timestamp), (sku_id, timestamp) |
| Product | (category, brand) |
| Model | (version) |

## 5. Governance

- Client data stays within the engagement.
- Consent/retention per client policy.
- Lineage via MLflow + feature store.