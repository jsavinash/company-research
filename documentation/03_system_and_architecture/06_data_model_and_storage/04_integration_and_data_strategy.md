# Integration and Data Strategy

Data sources, ingestion patterns, quality, feature strategy, third-party integrations, and governance for the platform.

## 1. Data sources

| Source | Type | Freshness | Notes |
|---|---|---|---|
| Retailer sell-out | Structured | Daily | Contractually restricted; per-retailer governance |
| Shipments (sell-in) | Structured | Daily | From Snowflake |
| Pricing & promotion | Structured | Weekly | Price/mix effects |
| Distribution | Structured | Weekly | ACV / distribution points |
| GLP-1 prescription prevalence | Structured | Monthly | Exogenous driver; geographic + income heterogeneity |
| Household panel | Structured (aggregate) | Weekly | Privacy-sensitive; aggregate only |
| Product reviews | Unstructured | Daily | LLM extraction → themes |
| Search trends | Unstructured | Daily | Demand signal |
| Social listening | Unstructured | Daily | |
| Call-centre notes | Unstructured | Daily | LLM extraction |
| Retailer contracts | Documents | On change | Data-use terms; parsed by Docling |
| NPD calendars | Structured | On change | Analog forecasting |

## 2. Ingestion patterns

- **Batch:** Snowflake → dbt → Iceberg → Feast (nightly).
- **Streaming:** Kafka (sell-out, GLP-1 Rx) → stream processors → feature store.
- **Document:** Docling/Unstructured/LlamaParse → chunked → vector store + Azure AI Search.

## 3. Data quality

| Check | Method | Action |
|---|---|---|
| Completeness | Null-rate monitoring | Alert + degrade |
| Freshness | Lag monitoring | Alert; SLA tracking |
| Point-in-time correctness | Feature validation | Block training if leakage |
| Stockout censoring | Flag affected stores | Caveat on forecasts |
| Outliers | Statistical tests | Quarantine |

## 4. Feature strategy

- **Point-in-time correctness** is mandatory (no future leakage).
- **Feature contracts** versioned in dbt.
- **Online/offline parity** via Feast.
- **GLP-1 features:** penetration by DMA, income quintile, trend, acceleration.

## 5. Integration architecture

```
Sources → Kafka / Batch → Snowflake / Iceberg → dbt → Feast → Forecast/Attribution
Documents → Docling → Vector Store + Azure AI Search → RAG → Copilot
All → OPA (policy) → Purview (DLP) → Audit log
```

## 6. Third-party integrations

| System | Purpose | Protocol |
|---|---|---|
| SAP | ERP / production / procurement | REST / IDoc |
| Salesforce | Customer / retail relationships | REST |
| ServiceNow | Workflow / ticketing | REST |
| Retailer APIs | Sell-out / inventory | REST / SFTP |
| Panel providers | Household panel | Secure file transfer |

Integration with these uses **MCP tools** for agents (not custom glue), per the open-protocol design.

## 7. Data governance

- **Ownership:** Data stewards per domain.
- **Lineage:** Unity Catalog + OpenTelemetry.
- **Retention:** per policy (see `../09_security_and_compliance/03_data_privacy_and_governance.md`).
- **Access:** OPA/ABAC; least privilege.

## 8. Related

- `01_client_normalized_and_offline_storage.md`
- `02_database_schemas_and_erd.md`
- `03_storage_search_and_data_lifecycle.md`
- `../07_api_and_network_communication/01_api_contracts_and_versioning.md`