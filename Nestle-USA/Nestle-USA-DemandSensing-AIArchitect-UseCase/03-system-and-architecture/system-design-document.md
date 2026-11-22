# System Design Document

## 1. Context

This document specifies the as-built design of the Agentic GLP-1 Demand Sensing & Scenario Copilot. It complements `01-business-and-strategy/high-level-solution-overview.md` (business view) with the technical design.

## 2. Goals & non-goals

**Goals:** calibrated, causally-attributed, store-level forecasts; conversational scenario analysis; permission-aware retrieval; auditability; FinOps.

**Non-goals:** price-setting, LLM forecasting, cross-retailer pooling without permission.

## 3. Component design

### 3.1 Data & AI platform

| Component | Technology | Responsibility |
|---|---|---|
| Lakehouse | Databricks (Unity Catalog) | Feature store, ML, lineage, ABAC |
| Warehouse | Snowflake | Retailer sell-out/shipment data; Cortex in-place AI |
| Fabric | Microsoft Fabric (OneLake) | Semi-structured retailer feeds; Power BI |
| Open table format | Apache Iceberg | Portability across Snowflake/Databricks/Fabric |
| Transformations | dbt | Feature contracts |
| Streaming | Apache Kafka | Real-time sell-out, GLP-1 Rx |
| Feature store | Feast | Online/offline parity |
| Vector search | Azure AI Search, pgvector/Qdrant | Hybrid retrieval |
| Graph | Neo4j | GraphRAG (brand→category→DMA→banner) |
| Ingestion | Docling / Unstructured / LlamaParse | PDFs, ERP/CRM, contracts |
| Forecast core | LightGBM / Temporal Fusion Transformer | Regime-aware forecasting |
| LLM serving | vLLM + NVIDIA NIM / TensorRT | Extraction + narration |

### 3.2 AI gateway

- **Portkey / LiteLLM** (Kong / Azure API Management as enterprise alternatives).
- Responsibilities: routing, semantic caching, rate limiting, fallback, chargeback.
- **Model mix:** small/fast for extraction; frontier for reasoning.

### 3.3 Agentic orchestration

- **LangGraph** — stateful agent graph.
- **Microsoft Agent Framework / Semantic Kernel** — enterprise integration.
- **LlamaIndex** — RAG.
- **Temporal** — durable long-running workflows (nightly forecast, backtesting).
- **FastAPI** — API layer; **TypeScript/React** — copilot front-end.

**Agents:** Data, Forecast, Attribution, Scenario, Governance (see §5).

### 3.4 Security & governance

- **Entra ID / Okta / AWS IAM** — identity.
- **OPA** — ABAC policy decision point.
- **NeMo Guardrails / Lakera / Purview / Vault** — guardrails, injection defense, DLP, secrets.

### 3.5 FinOps & observability

- **LangSmith / Langfuse / Arize / Braintrust / MLflow** — tracing, evals, registry.
- **OpenTelemetry / Datadog / Grafana** — unified telemetry.

## 4. Data flow

1. **Ingest** — Kafka (real-time), batch (Snowflake/Iceberg), documents (Docling).
2. **Feature** — dbt transforms → Feast feature store; point-in-time correctness.
3. **Forecast** — Forecast Agent runs LightGBM/TFT; hierarchical reconciliation (MinT).
4. **Attribute** — Attribution Agent runs synthetic control / DiD.
5. **Orchestrate** — LangGraph graph; Temporal for durability.
6. **Serve** — Copilot (FastAPI + TypeScript) via AI Gateway.
7. **Govern** — OPA policy, NeMo Guardrails, Purview DLP.
8. **Observe** — LangSmith traces, Datadog metrics, MLflow model registry.

## 5. Agent contracts

| Agent | Tools (MCP) | Never |
|---|---|---|
| Data Agent | `query_snowflake`, `get_glp1_penetration`, `get_attribution`, `fetch_retailer_contract_terms` | Leak restricted data |
| Forecast Agent | `run_forecast`, `get_feature_store` | Use LLM to forecast |
| Attribution Agent | `synthetic_control`, `did` | Claim causality without validation |
| Scenario Agent | forecast + attribution + copilot | Set prices |
| Governance Agent | Purview, OPA, NeMo | Allow PII into prompts |

## 6. Deployment topology

- **Cloud:** Azure (primary), AWS (Bedrock/SageMaker fallback), GCP (Vertex).
- **Serving:** AKS / Databricks / Snowflake.
- **CI/CD:** GitLab CI / Azure DevOps.
- **Environments:** dev → staging → prod (see `06-operations-and-infrastructure/environments-and-secrets.md`).

## 7. Key design decisions

See `decision-log.md` and `architecture-decision-records/`.

## 8. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Retailer data access | Degrade to first-party + panel |
| Regime shift outpaces updates | Out-of-regime eval + scheduled re-estimation |
| LLM hallucination | LLM never forecasts; grounding verifier |
| Data leakage | ABAC + contract-term parsing + Purview |