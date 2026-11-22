# Use Case — Agentic GLP-1 Demand Sensing & Scenario Copilot (Nestlé USA)

**Prepared for:** AI Solutions Architect portfolio piece / enterprise reference architecture
**Role framing:** AI Solutions Architect (late-2026 stack: MCP & A2A, AI gateways, permission-aware retrieval, enterprise governance)
**Business context:** Nestlé USA — Frozen (DiGiorno, Stouffer's, Hot Pockets, Lean Pockets, Lean Cuisine, CPK, Tombstone, Jack's, Buitoni) and Coffee (Coffee mate, natural bliss, Nescafé, Starbucks at Home)
**Source docs:** `Nestle-USA-DemandSensing-ProjectDoc.md`, `Nestle-USA-Research.md`

---

## 1. The business problem (why this use case)

Three facts from the research define the problem:

1. **Volumes are structurally declining.** US food volume per person fell 0.6% in H1 2026. Nestlé USA cannot grow on category expansion — it must defend share and price/mix.
2. **Frozen is the most exposed category.** GLP-1 adoption is associated with a ~3-point drop in dollar spend in year one — the largest CPG category impact. Frozen is also where Nestlé is investing most.
3. **The old forecasting regime is dead.** Models trained on 2015–2022 history encode a world without meaningful GLP-1 penetration, without private label at 23.8% of units, and without cocoa at $3,500/t. Backtesting them on 2025–26 data produces confident, wrong numbers.

The gap is **predictive and causal**: not "what happened on the shelf" (descriptive, already covered by digital-shelf monitoring) but "what will happen two to three quarters ahead, and *why*", when the demand process itself has changed.

---

## 2. The use case in one line

> **An agentic, permission-aware decision-support platform that turns Nestlé USA's structured demand data and unstructured consumer signal into calibrated, causally-attributed, store-level forecasts — and lets a demand planner interrogate them conversationally ("if GLP-1 penetration rises 5pp in the Southeast, what happens to DiGiorno units by Q3, and which banners drive it?").**

The LLM **never** forecasts. It converts unstructured text into structured leading indicators, orchestrates the analytical agents, and explains results in the planner's language. The numbers come from a regime-aware forecasting core with a causal attribution layer.

This is deliberately an **AI Solutions Architect** use case, not a data-science project: the hard problems are integration (SAP/Salesforce/ServiceNow), governance (retailer-contract and household-panel restrictions), permission-aware retrieval, and proving ROI — not the gradient-boosted model.

---

## 3. Architecture at a glance

```
                    ┌──────────────────────────────────────────────────────────┐
   Planners / RGM ──▶│  Conversational Scenario Copilot (TypeScript + FastAPI)  │
   (Excel, Teams)    │  "GLP-1 +5pp in SE → DiGiorno units by Q3?"             │
                    └───────────────┬──────────────────────────────────────────┘
                                    │  (MCP tools + A2A)
                    ┌───────────────▼──────────────────────────────────────────┐
                    │  AI Gateway (Portkey / LiteLLM / Kong)                    │
                    │  routing · semantic cache · rate limit · chargeback      │
                    └───┬───────────────┬───────────────┬───────────────────────┘
        small/fast ─────┘               │               └───── frontier
        (Gemini Flash,                   │                      (o-series, Claude,
         Claude Haiku, Llama/Qwen)       │                       Gemini Pro)
                                          │
        ┌─────────────────────────────────▼─────────────────────────────────┐
        │  Agentic Orchestration (LangGraph + MS Agent Framework + Temporal) │
        │  ┌────────────┐ ┌──────────────┐ ┌────────────┐ ┌───────────────┐  │
        │  │ Data Agent │ │ Forecast     │ │ Attribution│ │ Scenario      │  │
        │  │ (MCP)      │ │ Agent        │ │ Agent      │ │ Agent (A2A)   │  │
        │  └─────┬──────┘ └──────┬───────┘ └─────┬──────┘ └──────┬────────┘  │
        └────────┼───────────────┼───────────────┼───────────────┼───────────┘
                 │               │               │               │
   ┌─────────────▼───────────────▼───────────────▼───────────────▼─────────────┐
   │  Data & AI Platform: Databricks (Unity Catalog) + Snowflake + Fabric       │
   │  Iceberg · dbt · Kafka · Feast feature store                               │
   │  Vector/graph: Azure AI Search · pgvector/Qdrant · Neo4j (GraphRAG)        │
   │  Models: LightGBM / TFT forecast core · vLLM/NIM for LLM extraction        │
   └───────────────────────────────────────────────────────────────────────────┘
                 │                                   │
   ┌─────────────▼──────────────┐      ┌─────────────▼───────────────────────┐
   │ Security & Governance      │      │ FinOps, Observability & Evals         │
   │ Entra ID · OPA · Purview   │      │ LangSmith/Arize/Langfuse · MLflow     │
   │ NeMo Guardrails · Lakera   │      │ OpenTelemetry · Datadog · Grafana     │
   │ Vault                      │      │                                       │
   └────────────────────────────┘      └───────────────────────────────────────┘
```

---

## 4. Layer 1 — Enterprise Cloud & Managed AI Platforms

Nestlé is a Microsoft-centric enterprise, so the design is **hybrid, not self-hosted everything**:

| Concern | Choice | Why |
|---|---|---|
| Governed data + AI | **Databricks (Mosaic AI / Unity Catalog)** | Lakehouse for demand features; Unity Catalog for lineage + ABAC; Mosaic for model serving |
| Warehouse + Cortex | **Snowflake Cortex** | Snowflake already holds retailer sell-out/shipment data; Cortex keeps AI compute beside governed data |
| Fabric | **Microsoft Fabric** | OneLake for semi-structured retailer feeds; Power BI for planner-facing scenario output |
| Managed model APIs | **Azure AI Foundry / Azure OpenAI** | Primary frontier-model endpoint (enterprise compliance, VPC isolation, SLA) |
| Multi-cloud fallback | **AWS Bedrock & SageMaker**, **Vertex AI** | Fallback routing + training for TFT/temporal models; avoids single-vendor lock-in |
| High-throughput / low-latency inference | **vLLM + NVIDIA NIM / TensorRT**, burst to **Groq / CoreWeave** | Serves the LLM extraction layer and any real-time scoring; Groq for low-latency copilot turns |

**Architect's note:** the forecasting core (LightGBM / temporal-fusion) runs on Databricks/SageMaker; the *LLM extraction* layer is what needs vLLM/NIM. Keeping them separate is the design decision — the LLM is an unstructured-to-structured converter, not the forecaster.

---

## 5. Layer 2 — Model Routing & AI Gateways

A centralized gateway sits between internal apps and foundation models to control cost, avoid lock-in, and enforce policy.

| Concern | Choice | Application |
|---|---|---|
| Gateway | **Portkey** or **LiteLLM** (Kong AI Gateway / Azure API Management as enterprise alternatives) | Single control point for all LLM calls |
| Rate limiting / quota | Gateway policy | Per business unit (Frozen vs Coffee vs Baking) and per planner |
| Semantic caching | Gateway cache | Repeated retailer/category queries ("DiGiorno SE GLP-1") served from cache |
| Fallback routing | Gateway | Azure OpenAI primary → Bedrock/Vertex fallback on error or rate limit |
| Chargeback | Gateway + cost tags | Token spend attributed to Frozen / Coffee / Baking P&Ls |
| Model mix | Routing rules | Simple extraction (reviews → themes) → **Gemini Flash / Claude Haiku / Llama-3 / Qwen**; complex reasoning (scenario narrative, causal explanation) → **OpenAI o-series / Claude / Gemini Pro** |

**Why it matters here:** the extraction layer runs millions of short calls (reviews, search queries, call-centre notes). Routing those to small/fast models is the difference between a viable and an unaffordable system; only the planner-facing explanation and scenario reasoning need frontier models.

---

## 6. Layer 3 — Data Foundations & Permission-Aware Context (RAG)

An enterprise AI system fails if it leaks restricted retailer data or retrieves stale numbers.

**Data warehouses & streaming**
- **Snowflake** (retailer sell-out, shipments, pricing, distribution), **Databricks** (feature store, ML), **Microsoft Fabric OneLake** (semi-structured feeds)
- **Apache Iceberg** open table format so data is portable across Snowflake/Databricks/Fabric
- **dbt** for transformations and the feature contracts
- **Apache Kafka** for real-time retailer sell-out and GLP-1 prescription-prevalence streams

**Retrieval & knowledge engines**
- **Azure AI Search** — hybrid (vector + keyword) search over category docs, retailer contracts, prior planning memos
- **pgvector / Qdrant** — vector store for review/complaint/search-query embeddings
- **Neo4j (GraphRAG)** — a brand → category → DMA → banner → causal-driver graph, so the copilot can traverse "which banners in which DMAs are GLP-1-exposed"

**Document ingestion**
- **Docling / Unstructured / LlamaParse** — parse complex PDFs: retailer contracts (to enforce data-use terms), category reviews, ERP/CRM records, NPD calendars

**Permission-aware retrieval (the defining requirement)**
- Row/column-level security in Snowflake + Unity Catalog ABAC
- The copilot retrieves **only** the banners/DMA a planner is entitled to (enforced by OPA, see Layer 5)
- Every chunk carries provenance (source, date, contract restriction) so the answer can cite it

---

## 7. Layer 4 — Agentic Orchestration & Open Protocols

Integration with legacy systems (SAP, Salesforce, ServiceNow) is where most AI pilots die. The 2026 answer is **open protocols, not custom glue**.

**Connectivity protocols**
- **MCP (Model Context Protocol)** — vertical tool/data access: `query_snowflake`, `get_glp1_penetration`, `run_forecast`, `get_attribution`, `fetch_retailer_contract_terms`
- **A2A (Agent-to-Agent)** — cross-agent coordination: Forecast Agent ↔ Attribution Agent ↔ Scenario Agent, and escalation to a human planner agent

**Orchestration frameworks**
- **LangGraph** — the agent graph (stateful, branching, human-in-the-loop nodes)
- **Microsoft Agent Framework / Semantic Kernel** — since Nestlé is Microsoft-aligned; .NET/Python interop with existing enterprise services
- **LlamaIndex** — the RAG layer over Azure AI Search / pgvector / Neo4j
- **Temporal** — durable, fault-tolerant long-running workflows: nightly forecast refresh, weekly rolling-origin backtesting, month-end attribution review (these must survive failures and resume)

**Application & API layer**
- **Python (FastAPI)** — forecasting + attribution services
- **TypeScript** — the React copilot front-end (planner chat, scenario toggles, P10/P50/P90 bands)
- **GraphQL / REST** — the planner-facing API

**Agent topology**

| Agent | Responsibility | Tools (MCP) | Model tier |
|---|---|---|---|
| Data Agent | Fetch/validate data, enforce permissions | Snowflake, Kafka, contract terms | Small/fast |
| Forecast Agent | Run regime-aware forecast + intervals | Forecast service, feature store | (deterministic, no LLM) |
| Attribution Agent | Synthetic control / DiD, decompose deltas | Causal service | Frontier (reasoning) |
| Scenario Agent | Answer "what-if", narrate results | Forecast + attribution + copilot | Frontier |
| Governance Agent | PII redaction, policy checks, citations | Purview, OPA, NeMo | Small/fast |

---

## 8. Layer 5 — Security, Governance & Compliance

The defining layer for a Solutions Architect — and the reason this is an enterprise system, not a notebook.

**Identity & access control (RBAC/ABAC)**
- **Microsoft Entra ID** — enterprise SSO for planners
- **Okta** — partner/retailer collaboration access
- **AWS IAM** — for Bedrock/S3-resident assets
- **OPA (Open Policy Agent)** — the policy decision point: "this planner may retrieve only banner X, DMA Y, category Z"; enforced at the gateway and at the data layer

**AI guardrails & DLP**
- **NVIDIA NeMo Guardrails** — hard rails: the copilot may **not** set prices, may **not** fabricate a number, must cite a forecast run
- **Lakera Guard** — prompt-injection defense (retailer-supplied text, review content is untrusted input)
- **Microsoft Purview** — DLP over household-panel and retailer-confidential data; blocks PII from entering prompts
- **HashiCorp Vault** — secrets/keys for all model endpoints and data stores

**Governance controls specific to this use case**
- Retailer data is contractually restricted → no cross-retailer pooling without permission (enforced by ABAC + contract-term parsing)
- Household panel data is privacy-sensitive → aggregate only, minimum cell sizes enforced
- Every forecast version archived with its feature snapshot for auditability

---

## 9. Layer 6 — FinOps, Observability & Continuous Evaluation

Architects must prove ROI and hold reliability SLAs in production.

**Tracing & evals**
- **LangSmith / Langfuse** — trace every agent run (which tools, which models, token cost, latency)
- **Arize Phoenix** — LLM extraction quality: is the review→theme extraction accurate? drift over time?
- **Braintrust** — regression testing of the copilot's answers (does a prompt/model change degrade scenario answers?)
- **MLflow** — forecast model registry, experiment tracking, the out-of-regime evaluation (train ≤2022, test 2024–26)

**System telemetry**
- **OpenTelemetry** — unified traces across FastAPI, agents, gateway, data services
- **Datadog / Grafana** — AI metrics (token spend, cache hit rate, fallback rate) alongside traditional infra monitoring

**The eval that matters (from the ProjectDoc)**
- Out-of-regime WMAPE vs. incumbent (≥15% relative improvement)
- GLP-1 effect stability (sign-consistent across rolling windows)
- Interval calibration (P50/P90 coverage)
- No systematic bias by DMA income quintile
- Decision adoption ≥ 80%

---

## 10. Worked example — a planner's Monday morning

> **Planner (Teams):** "GLP-1 keeps climbing in the Southeast. If it's up 5 points by Q3, what happens to DiGiorno and Hot Pockets, and which banners should I worry about?"

1. **Copilot** (TypeScript front-end) → **AI Gateway** (Portkey): authenticates via Entra ID, checks OPA policy (planner owns Southeast + Frozen), routes to **Frontier** (this is complex reasoning).
2. **Scenario Agent** calls **Attribution Agent** (A2A) → causal service runs synthetic control per DMA, DiD on the adoption ramp → estimated GLP-1 effect, separable from price/distribution.
3. **Forecast Agent** runs the regime-aware forecast with GLP-1 +5pp shock, hierarchical reconciliation (MinT), returns P10/P50/P90 at store → banner → DMA.
4. **Data Agent** (MCP) pulls the banner list, contract terms, and data-quality flags (stockout censoring).
5. **Governance Agent** (NeMo Guardrails) enforces: no price recommendation, cite the forecast run ID, redact any household PII.
6. **Copilot** narrates: *"By Q3, DiGiorno units −6.2% (P10 −8.1%, P90 −4.4%) vs. plan. Concentrated in [3 banners] in [DMAs]. GLP-1 accounts for −2.1pp, price −1.3pp, distribution −0.8pp, private label −0.5pp. Run ID FR-2026-11-22-0142."*
7. **Observability:** LangSmith logs the trace, Datadog tracks latency/cost, MLflow links to the model version.

Every number is a forecast; every "why" is a causal estimate; every sentence is LLM-narrated but **grounded** in a run the planner can audit.

---

## 11. Why this is an AI Solutions Architect deliverable (not a data-science project)

| Data-science framing | Solutions-Architect framing (this doc) |
|---|---|
| "Train a LightGBM forecaster" | "Design a governed, permission-aware, agentic platform across 6 layers" |
| Model accuracy is the goal | Integration (SAP/Salesforce/ServiceNow via MCP), governance (retailer contracts, panel privacy), and FinOps are the goal |
| One notebook | Hybrid cloud (Databricks/Snowflake/Fabric/Azure/Bedrock) with fallback routing |
| LLM optional | LLM as structured-signal extractor + copilot, never the forecaster |
| Offline eval | Continuous eval (LangSmith/Arize/Braintrust) + out-of-regime backtesting + chargeback |

The moat is not the model — it is the **data (retailer + GLP-1 + digital shelf), the causal discipline, and the governance** that makes the number trustworthy enough to change a production decision.

---

## 12. Caveats / period accuracy

- The 2026 stack (MCP, A2A, Portkey/LiteLLM, vLLM/NIM, NeMo Guardrails, LangGraph, Temporal) is late-2026; the Nestlé demand-sensing tenure spans 2022–2026, so this is the **target-state** architecture, not what existed in 2022.
- The LLM never forecasts — it extracts structured signals and narrates. This boundary is the design's core defensibility.
- Specific vendor choices (Portkey vs LiteLLM, Azure vs Bedrock) are illustrative; the architecture holds regardless of which concrete gateway/cloud is chosen.
- All Nestlé figures are from `Nestle-USA-Research.md` (2026-11-21) and are company-reported or third-party estimates.

---

## 13. Technology Stack (consolidated)

The full stack, grouped by the six architecture layers. "Primary" = the concrete choice this design assumes; "Alternatives" = interchangeable options that preserve the architecture.

### 13.1 Enterprise Cloud & Managed AI Platforms

| Capability | Primary | Alternatives |
|---|---|---|
| Lakehouse + governance | **Databricks (Mosaic AI / Unity Catalog)** | — |
| Warehouse + in-place AI | **Snowflake Cortex** | BigQuery |
| Unified data/AI fabric | **Microsoft Fabric (OneLake)** | — |
| Managed frontier models | **Azure AI Foundry / Azure OpenAI** | AWS Bedrock, Google Vertex AI |
| Model training platform | **AWS SageMaker** | Databricks Mosaic AI |
| LLM inference serving | **vLLM + NVIDIA NIM / TensorRT** | — |
| Low-latency burst inference | **Groq / CoreWeave** | — |
| Forecasting core | **LightGBM / Temporal Fusion Transformer** | Prophet, statsmodels |

### 13.2 Model Routing & AI Gateways

| Capability | Primary | Alternatives |
|---|---|---|
| AI gateway | **Portkey** | LiteLLM, Kong AI Gateway, Azure API Management |
| Semantic caching / rate limit / chargeback | Gateway-native | — |
| Small/fast models (extraction) | **Gemini Flash, Claude Haiku, Llama-3, Qwen** | — |
| Frontier models (reasoning) | **OpenAI o-series, Claude, Gemini Pro** | — |

### 13.3 Data Foundations & Permission-Aware Context (RAG)

| Capability | Primary | Alternatives |
|---|---|---|
| Data warehouse | **Snowflake** | Databricks, BigQuery |
| Lakehouse | **Databricks** | — |
| Open table format | **Apache Iceberg** | Delta Lake, Hudi |
| Transformations | **dbt** | — |
| Real-time streaming | **Apache Kafka** | Kinesis, Pub/Sub |
| Feature store | **Feast** (or Databricks Feature Store) | — |
| Vector search | **Azure AI Search** | Elasticsearch, Qdrant, Pinecone, pgvector |
| Graph / GraphRAG | **Neo4j** | — |
| Document ingestion | **Docling / Unstructured / LlamaParse** | — |

### 13.4 Agentic Orchestration & Open Protocols

| Capability | Primary | Alternatives |
|---|---|---|
| Tool/data connectivity | **MCP (Model Context Protocol)** | — |
| Cross-agent coordination | **A2A (Agent-to-Agent)** | — |
| Agent graph orchestration | **LangGraph** | Microsoft Agent Framework / Semantic Kernel, LlamaIndex |
| Durable long-running workflows | **Temporal** | — |
| RAG framework | **LlamaIndex** | — |
| API layer | **Python (FastAPI)** | — |
| Front-end | **TypeScript (React)** | — |
| API contracts | **GraphQL / REST** | — |

### 13.5 Security, Governance & Compliance

| Capability | Primary | Alternatives |
|---|---|---|
| Enterprise SSO | **Microsoft Entra ID** | Okta |
| Partner access | **Okta** | — |
| Cloud IAM | **AWS IAM** | — |
| Policy engine (ABAC) | **OPA (Open Policy Agent)** | — |
| AI guardrails | **NVIDIA NeMo Guardrails** | — |
| Prompt-injection defense | **Lakera Guard** | — |
| DLP | **Microsoft Purview** | — |
| Secrets management | **HashiCorp Vault** | — |

### 13.6 FinOps, Observability & Continuous Evaluation

| Capability | Primary | Alternatives |
|---|---|---|
| LLM tracing | **LangSmith** | Langfuse |
| LLM quality / drift | **Arize Phoenix** | — |
| Regression testing | **Braintrust** | — |
| Model registry / experiment tracking | **MLflow** | — |
| Unified traces | **OpenTelemetry** | — |
| Infrastructure monitoring | **Datadog / Grafana** | — |

### 13.7 One-line stack summary

> **Cloud:** Azure (AI Foundry, Fabric, Entra, Purview) + Databricks + Snowflake + AWS (Bedrock, SageMaker) · **Gateway:** Portkey/LiteLLM · **Data:** Iceberg, dbt, Kafka, Feast · **RAG:** Azure AI Search, pgvector/Qdrant, Neo4j · **Agents:** MCP + A2A on LangGraph + Temporal, FastAPI + TypeScript · **Governance:** Entra ID, OPA, NeMo Guardrails, Lakera, Purview, Vault · **Ops:** LangSmith, Arize, Braintrust, MLflow, OpenTelemetry, Datadog, Grafana.