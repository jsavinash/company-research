# Database Schema and ERD

## 1. Core entities

```
Variant (variant_id PK, gene, transcript, hgvs, consequence, rsid)
Annotation (variant_id FK, source, field, value, version)
Feature (variant_id FK, feature_name, value, source_version)
TriageRun (run_id PK, model_version, created_at, status)
TriageResult (run_id FK, variant_id FK, score, confidence, abstained)
EvidenceCode (result_id FK, code, provenance, source)
ReviewAction (action_id PK, result_id FK, curator_id, action, reason, timestamp)
AuditEvent (event_id PK, run_id FK, action, user_id, timestamp)
```

## 2. ERD (text)

```
Variant ||--o{ Annotation : has
Variant ||--o{ Feature : has
TriageRun ||--o{ TriageResult : produces
TriageResult ||--o{ EvidenceCode : suggests
TriageResult ||--o{ ReviewAction : reviewed_by
TriageRun ||--o{ AuditEvent : audited_by
```

## 3. Key design points

- **Per-field provenance** stored with every evidence code.
- **Review actions** are first-class records (training labels).
- **Audit events** append-only.
- **Feature versioning** (gnomAD, ClinVar releases) pinned.

## 4. Example DDL (PostgreSQL)

```sql
CREATE TABLE variant (
  variant_id   UUID PRIMARY KEY,
  gene         TEXT,
  transcript   TEXT,
  hgvs         TEXT,
  consequence  TEXT,
  rsid         TEXT
);

CREATE TABLE triage_result (
  result_id    UUID PRIMARY KEY,
  run_id       UUID,
  variant_id   UUID REFERENCES variant(variant_id),
  score        DOUBLE PRECISION,
  confidence   DOUBLE PRECISION,
  abstained    BOOLEAN
);

CREATE TABLE evidence_code (
  code_id      UUID PRIMARY KEY,
  result_id    UUID REFERENCES triage_result(result_id),
  code         TEXT,
  provenance   JSONB,
  source       TEXT
);

CREATE TABLE review_action (
  action_id    UUID PRIMARY KEY,
  result_id    UUID REFERENCES triage_result(result_id),
  curator_id   TEXT,
  action       TEXT,
  reason       TEXT,
  timestamp    TIMESTAMP
);
```

## 5. Indexing

| Table | Index |
|---|---|
| TriageResult | (run_id, variant_id) |
| EvidenceCode | (result_id) |
| ReviewAction | (result_id, timestamp) |
| AuditEvent | (run_id, timestamp) |

## 6. Governance

- De-identified data only.
- ISO 13485 traceability.
- Model + data versioning.