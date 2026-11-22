# Database Schema and ERD

## 1. Core entities

```
Document (document_id PK, doc_type, uploaded_at, status)
Field (field_id PK, document_id FK, field_name, value, confidence, ocr_token_confidence, provenance, status)
ReviewAction (action_id PK, field_id FK, reviewer_id, action, corrected_value, timestamp)
AuditEvent (event_id PK, document_id FK, action, user_id, timestamp)
FieldSchema (schema_id PK, doc_type, field_name, data_type, required)
ThresholdConfig (doc_type, field_name, tau, updated_at)
```

## 2. ERD (text)

```
Document ||--o{ Field : contains
Field ||--o{ ReviewAction : reviewed_by
Document ||--o{ AuditEvent : audited_by
FieldSchema }o--|| Document : defines
ThresholdConfig }o--|| FieldSchema : configures
```

## 3. Key design points

- **Per-field confidence + provenance** stored with every field.
- **Review actions** are first-class records (training labels).
- **Audit events** are append-only.
- **Field schema** drives validation and the review UI.

## 4. Example DDL (PostgreSQL)

```sql
CREATE TABLE document (
  document_id   UUID PRIMARY KEY,
  doc_type      TEXT,
  uploaded_at   TIMESTAMP,
  status        TEXT
);

CREATE TABLE field (
  field_id       UUID PRIMARY KEY,
  document_id    UUID REFERENCES document(document_id),
  field_name     TEXT,
  value          TEXT,
  confidence     DOUBLE PRECISION,
  ocr_token_confidence DOUBLE PRECISION,
  provenance     JSONB,
  status         TEXT
);

CREATE TABLE review_action (
  action_id      UUID PRIMARY KEY,
  field_id       UUID REFERENCES field(field_id),
  reviewer_id    TEXT,
  action         TEXT,
  corrected_value TEXT,
  timestamp      TIMESTAMP
);
```

## 5. Indexing

| Table | Index |
|---|---|
| Field | (document_id, field_name) |
| ReviewAction | (field_id, timestamp) |
| AuditEvent | (document_id, timestamp) |

## 6. Governance

- PII/TIN: encryption, access logging, retention per WISP.
- Audit log append-only.
- Field schema versioned.