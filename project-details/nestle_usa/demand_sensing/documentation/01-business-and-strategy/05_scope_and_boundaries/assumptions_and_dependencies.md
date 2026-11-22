# Assumptions and Dependencies

## 1. Assumptions

| ID | Assumption | Impact if false |
|---|---|---|
| A1 | Retailer sell-out data is accessible (per contract) | Degrade to first-party + panel |
| A2 | GLP-1 prescription prevalence data is available at DMA/income granularity | Coarser driver; weaker attribution |
| A3 | Household panel data can be licensed (aggregate) | Reduced signal |
| A4 | Nestlé is Microsoft-centric (Entra ID, Fabric, Azure) | Adjust cloud mix |
| A5 | Existing Snowflake holds retailer data | Extra ingestion cost |
| A6 | Planners will adopt a copilot workflow | Adoption risk; training needed |
| A7 | Out-of-regime evaluation is accepted as the accuracy metric | Disputed metric; credibility risk |

## 2. Dependencies

### 2.1 Cross-team

| Dependency | Owner | Needed for |
|---|---|---|
| Retailer data contracts | Legal + Sales | Data ingestion |
| Panel data license | Procurement + DS | GLP-1/panel features |
| Entra ID / SSO | IT Security | Authentication |
| OPA policy framework | Security | Permission-aware retrieval |
| Snowflake/Databricks platform | Data Platform | Storage/compute |
| SAP/Salesforce/ServiceNow APIs | Enterprise Integration | MCP tools |

### 2.2 Vendor / external

| Dependency | Vendor | Needed for |
|---|---|---|
| Frontier model APIs | Azure OpenAI / Bedrock / Vertex | Copilot reasoning |
| AI gateway | Portkey / LiteLLM | Routing, caching, chargeback |
| Panel data | Circana / Nielsen | Household panel |
| GLP-1 data | IQVIA / claims | Prescription prevalence |

### 2.3 Technology

| Dependency | Technology | Needed for |
|---|---|---|
| Lakehouse | Databricks + Snowflake + Iceberg | Data platform |
| Streaming | Kafka | Real-time ingestion |
| Feature store | Feast | Features |
| Vector/graph | Azure AI Search, pgvector/Qdrant, Neo4j | RAG |
| Orchestration | LangGraph, Temporal, MS Agent Framework | Agents |
| Observability | LangSmith, Datadog, OpenTelemetry | Ops |

## 3. Constraints

- **Contractual:** no cross-retailer pooling without permission.
- **Privacy:** aggregate panel only; minimum cell sizes.
- **Enterprise:** Microsoft-centric identity and data platform.
- **Regulatory:** audit-grade lineage and retention.

## 4. Risk of unmet dependencies

See `../11_risk_analysis_and_mitigation.md`.