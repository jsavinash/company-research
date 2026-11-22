# Full-Stack and Infra Tech Choices

## 1. Stack overview

| Layer | Choice | Rationale |
|---|---|---|
| **Front-end** | TypeScript + React | Copilot UI |
| **API** | FastAPI (Python) | ML ecosystem, async |
| **LLM serving** | vLLM + NVIDIA NIM / TensorRT | Extraction + coaching |
| **Models** | Azure OpenAI / Bedrock / Vertex | Frontier + small |
| **Vector store** | Azure AI Search / pgvector / Qdrant | RAG |
| **Graph** | Neo4j | GraphRAG (optional) |
| **Data** | Snowflake / Databricks / Fabric | Profiles, logs |
| **Gateway** | Portkey / LiteLLM | Routing, cache, chargeback |
| **Guardrails** | Lakera / NeMo Guardrails | Injection defense |
| **DLP** | Microsoft Purview | PII protection |
| **Observability** | LangSmith / Langfuse / Arize / Braintrust / MLflow | Traces + evals |
| **Telemetry** | OpenTelemetry / Datadog / Grafana | Metrics |

## 2. Model strategy

| Task | Tier | Models |
|---|---|
| Intake extraction | Small/fast | Gemini Flash, Claude Haiku, Llama-3, Qwen |
| Coaching narration | Frontier | GPT-4o, Claude, Gemini Pro |
| Grounding verifier | Small NLI | Entailment model |

## 3. Infrastructure

- **Cloud:** Azure (primary), AWS/GCP fallback.
- **Compute:** AKS (Kubernetes).
- **Data:** Snowflake/Databricks/Fabric + Iceberg.
- **Secrets:** Vault.

## 4. Rationale

- **Buy the commodity, build the moat:** managed models/vector store; build intake + grounding + eval.
- **Open protocols:** MCP/A2A avoid lock-in.
- **Microsoft-centric:** Entra ID, Fabric, Azure.

## 5. Related

- ADRs in `architecture_decision_records/`
- `../../Nestle-USA-PetCare-GenAI-LLM-UseCase.md`