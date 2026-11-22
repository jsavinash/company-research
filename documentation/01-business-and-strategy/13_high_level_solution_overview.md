# High-Level Solution Overview

Business-level overview of the Agentic GLP-1 Demand Sensing & Scenario Copilot. (Deep technical detail lives in `../03_system_and_architecture/`.)

## 1. One-line description

> An agentic, permission-aware decision-support platform that turns Nestlé USA's structured demand data and unstructured consumer signal into calibrated, causally-attributed, store-level forecasts — and lets a demand planner interrogate them conversationally.

## 2. The core design decision

**The LLM never forecasts.** It converts unstructured text into structured leading indicators, orchestrates the analytical agents, and explains results in the planner's language. The numbers come from a regime-aware forecasting core with a causal attribution layer. The moat is **data + causal discipline + governance**, not the model.

## 3. Value proposition

| Value driver | Mechanism | Beneficiary |
|---|---|---|
| **Avoided stockouts / overproduction** | Better store-level forecasts → right inventory in the right banner | Supply chain, retailers |
| **Trade-spend efficiency** | Causal attribution separates price/mix effects → less wasted promotion | Revenue growth management |
| **Faster response to regime shifts** | GLP-1 as a first-class driver → forecasts survive the break | Demand planning |
| **Audit-grade decisions** | Every number traceable to a forecast run + feature snapshot | Finance, compliance |
| **Reusable platform** | 6-layer architecture reused across Frozen, Coffee, Baking | Enterprise |

## 4. Architecture at a glance

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

## 5. The six layers

| Layer | Purpose | Key technologies |
|---|---|---|
| **1. Cloud & managed AI** | Hybrid cloud, managed models, inference | Databricks, Snowflake Cortex, Fabric, Azure AI Foundry, Bedrock/Vertex, vLLM/NIM, Groq/CoreWeave |
| **2. Model routing & gateway** | Cost control, no lock-in | Portkey/LiteLLM/Kong, semantic cache, chargeback, small/frontier model mix |
| **3. Data & permission-aware RAG** | Governed data, grounding | Iceberg, dbt, Kafka, Feast, Azure AI Search, pgvector/Qdrant, Neo4j, Docling/Unstructured |
| **4. Agentic orchestration** | Integration, coordination | MCP, A2A, LangGraph, MS Agent Framework, Temporal, FastAPI, TypeScript |
| **5. Security & governance** | Identity, DLP, guardrails | Entra ID, Okta, AWS IAM, OPA, NeMo Guardrails, Lakera, Purview, Vault |
| **6. FinOps & observability** | ROI, reliability | LangSmith, Arize, Langfuse, Braintrust, MLflow, OpenTelemetry, Datadog, Grafana |

## 6. Agent topology

| Agent | Responsibility | Model tier |
|---|---|---|
| **Data Agent** | Fetch/validate data, enforce permissions | Small/fast |
| **Forecast Agent** | Run regime-aware forecast + intervals | Deterministic (no LLM) |
| **Attribution Agent** | Synthetic control / DiD, decompose deltas | Frontier (reasoning) |
| **Scenario Agent** | Answer what-if, narrate results | Frontier |
| **Governance Agent** | PII redaction, policy checks, citations | Small/fast |

## 7. Why this is an AI Solutions Architect use case

| Data-science framing | Solutions-Architect framing |
|---|---|
| "Train a LightGBM forecaster" | "Design a governed, permission-aware, agentic platform across 6 layers" |
| Model accuracy is the goal | Integration, governance, and FinOps are the goal |
| One notebook | Hybrid cloud with fallback routing |
| LLM optional | LLM as structured-signal extractor + copilot, never the forecaster |
| Offline eval | Continuous eval + out-of-regime backtesting + chargeback |

See `../03_system_and_architecture/03_high_level_design_hld/01_end_to_end_system_architecture.md` for the detailed design.