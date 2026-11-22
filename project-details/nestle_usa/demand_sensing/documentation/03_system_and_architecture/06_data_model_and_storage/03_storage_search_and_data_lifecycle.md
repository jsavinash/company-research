# Storage, Search, and Data Lifecycle

## 1. Storage tiers

| Tier | Store | Use |
|---|---|---|
| **Hot** | Snowflake / Databricks | Recent, queryable data |
| **Warm** | Iceberg on ADLS/S3 | Full history |
| **Cold** | Archive ( Glacier ) | Compliance retention |
| **Vectors** | Azure AI Search / pgvector / Qdrant | Embeddings |
| **Graph** | Neo4j | Knowledge graph |
| **Object** | Blob / S3 | Documents, exports |

## 2. Search

| Concern | Choice |
|---|---|
| **Keyword** | Azure AI Search (BM25) |
| **Vector** | pgvector / Qdrant |
| **Hybrid** | Combined (keyword + dense) |
| **Rerank** | Cross-encoder |
| **Graph** | Neo4j (GraphRAG) |

## 3. Data lifecycle

| Stage | Retention | Action |
|---|---|---|
| **Raw** | 90 days | Drop / archive |
| **Curated** | 3 years | Archive |
| **Features** | 2 years | Recompute |
| **Forecasts** | 2 years | Archive |
| **Audit** | Per policy (7y) | Archive |

## 4. TTLs

| Data | TTL |
|---|---|
| Prompts / LLM logs | 90 days |
| Cache | 5 min (memory) / session (IndexedDB) |
| Temp tables | 7 days |

## 5. Archival & deletion

- **Archive** to cold storage.
- **Secure delete** on expiry.
- **Legal hold** overrides.

## 6. Data quality

- Completeness, freshness, uniqueness checks.
- Quarantine on failure.

## 7. Backup

| Data | Backup |
|---|---|
| Iceberg | Snapshot + manifest |
| Snowflake | Time Travel |
| Neo4j | Snapshot |
| Audit | Immutable store |

## 8. Related

- `01_client_normalized_and_offline_storage.md`
- `02_database_schemas_and_erd.md`
- `../09_security_and_compliance/03_data_privacy_and_governance.md`