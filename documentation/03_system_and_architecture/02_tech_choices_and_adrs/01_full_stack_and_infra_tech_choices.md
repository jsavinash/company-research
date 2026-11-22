# Full-Stack and Infra Tech Choices

## 1. Stack overview

| Layer | Choice | Rationale |
|---|---|---|
| **Front-end** | TypeScript + React | Copilot UI, type safety |
| **API** | FastAPI (Python) | ML ecosystem, async |
| **Agents** | LangGraph + MS Agent Framework + Semantic Kernel | Stateful orchestration |
| **Durable workflows** | Temporal | Long-running, fault-tolerant |
| **RAG** | LlamaIndex | Retrieval framework |
| **API gateway (AI)** | Portkey / LiteLLM (Kong/AxAPI alt) | Routing, cache, chargeback |
| **Data lakehouse** | Databricks (Unity Catalog) | Feature store, ABAC, lineage |
| **Warehouse** | Snowflake + Cortex | Retailer data, in-place AI |
| **Fabric** | Microsoft Fabric (OneLake) | Semi-structured feeds, Power BI |
| **Open table format** | Apache Iceberg | Portability |
| **Transforms** | dbt | Feature contracts |
| **Streaming** | Apache Kafka | Real-time ingestion |
| **Feature store** | Feast | Online/offline parity |
| **Vector search** | Azure AI Search, pgvector/Qdrant | Hybrid retrieval |
| **Graph** | Neo4j | GraphRAG |
| **Ingestion** | Docling / Unstructured / LlamaParse | Documents |
| **Forecast core** | LightGBM / Temporal Fusion Transformer | Regime-aware forecasting |
| **LLM serving** | vLLM + NVIDIA NIM / TensorRT | Extraction + narration |
| **Models** | Azure OpenAI / Bedrock / Vertex | Frontier + small |
| **Observability** | LangSmith, Arize, Langfuse, Braintrust, MLflow | Traces + evals |
| **Telemetry** | OpenTelemetry, Datadog, Grafana | Metrics + traces |
| **Secrets** | HashiCorp Vault | Secrets management |
| **CI/CD** | GitLab CI / Azure DevOps, Terraform, Argo CD | Delivery |

## 2. Infrastructure

| Concern | Choice |
|---|---|
| **Cloud** | Azure (primary), AWS (Bedrock/SageMaker), GCP (Vertex) |
| **Compute** | AKS (Kubernetes) |
| **Data** | Databricks, Snowflake, Iceberg on ADLS/S3 |
| **Networking** | Private endpoints, mTLS, VPC isolation |
| **IaC** | Terraform |
| **Secrets** | Vault + CSI driver |

## 3. Model choices

| Model | Tier | Use |
|---|---|---|
| Gemini Flash / Claude Haiku / Llama-3 / Qwen | Small/fast | Extraction, classification |
| OpenAI o-series / Claude / Gemini Pro | Frontier | Reasoning, narration |
| LightGBM / TFT | Forecast | Numeric forecasting |

## 4. Rationale

- **Buy the commodity, build the moat:** managed cloud/models/gateway; build causal + governance + copilot.
- **Open protocols:** MCP/A2A avoid brittle glue.
- **Iceberg:** avoids lock-in.
- **Microsoft-centric:** Entra ID, Fabric, Azure.

## 5. Related

- ADRs in `architecture_decision_records/`
- `Nestle-USA-DemandSensing-AIArchitect-UseCase/03-system-and-architecture/system-design-document.md`