# End-to-End System Architecture

## 1. Overview

The platform is a 6-layer, agentic, permission-aware decision-support system. This document provides the end-to-end architecture; the visual companion is `01_end_to_end_system_architecture.png`.

## 2. Architecture diagram

```mermaid
flowchart LR
  subgraph Users[Users]
    P[Planners / RGM]
  end
  subgraph Frontend[Front-end]
    C[Copilot UI - React/TS]
    D[Dashboard - Fabric/PowerBI]
  end
  subgraph Gateway[AI Gateway]
    G[Portkey / LiteLLM]
  end
  subgraph Agents[Agentic Orchestration]
    AG[LangGraph + MS Agent Framework + Temporal]
    DA[Data Agent]
    FA[Forecast Agent]
    AA[Attribution Agent]
    SA[Scenario Agent]
    GA[Governance Agent]
  end
  subgraph Data[Data & AI Platform]
    DB[Databricks + Unity Catalog]
    SF[Snowflake + Cortex]
    FB[Fabric OneLake]
    IC[Iceberg]
    KB[Kafka]
    FS[Feast]
    VEC[Azure AI Search / pgvector / Qdrant]
    NG[Neo4j]
  end
  subgraph Models[Models]
    FM[LightGBM / TFT]
    LLM[vLLM / NIM + Azure OpenAI / Bedrock]
  end
  subgraph Sec[Security]
    ID[Entra ID / Okta / OPA]
    DG[NeMo / Lakera / Purview / Vault]
  end
  subgraph Ops[Observability]
    OB[LangSmith / Arize / MLflow]
    OT[OpenTelemetry / Datadog / Grafana]
  end
  P --> C --> G --> AG
  C --> D
  AG --> DA --> SF
  AG --> FA --> FS --> FM
  AG --> AA --> SF
  AG --> SA --> LLM
  AG --> GA --> ID
  G --> LLM
  VEC --> SA
  NG --> SA
  ID --> G
  DG --> G
  OB --> AG
  OT --> AG
```

## 3. Layer responsibilities

| Layer | Responsibility |
|---|---|
| **Users / Frontend** | Planner interaction (copilot, dashboard) |
| **AI Gateway** | Routing, semantic cache, rate limit, chargeback, fallback |
| **Agents** | Orchestrate data, forecast, attribution, scenario, governance |
| **Data & AI Platform** | Store, process, retrieve, ground |
| **Models** | Forecast (LightGBM/TFT) + LLM (extraction/narration) |
| **Security** | Identity, authorization, guardrails, DLP, secrets |
| **Observability** | Tracing, metrics, evals |

## 4. End-to-end flow (scenario)

1. Planner asks a scenario in the copilot.
2. Copilot → AI gateway (auth, route).
3. Gateway → Scenario Agent.
4. Scenario Agent → Attribution Agent (A2A) + Forecast Agent.
5. Data Agent (MCP) fetches data + quality flags.
6. Governance Agent checks policy (no price, cite run).
7. Copilot narrates grounded answer with run ID.
8. LangSmith logs trace; Datadog tracks latency; MLflow links model.

## 5. Key principles

- LLM never forecasts.
- Causal claims require causal evidence.
- Point-in-time correctness.
- Permission-aware retrieval.
- Audit every run.

## 6. Related

- `02_ui_and_micro_frontend_topology.md`
- `03_backend_and_bff_service_boundaries.md`
- `04_ai_and_ml_integration_pipeline.md`
- Platform doc set `Nestle-USA-DemandSensing-AIArchitect-UseCase/03-system-and-architecture/system-design-document.md`