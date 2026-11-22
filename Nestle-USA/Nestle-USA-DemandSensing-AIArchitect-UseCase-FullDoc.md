# End-to-End Project Documentation — Agentic GLP-1 Demand Sensing & Scenario Copilot (Nestlé USA)

**Document type:** Master end-to-end project documentation (consolidates `documentation/` into one narrative)
**Project:** Target-state AI Solutions Architect platform for Nestlé USA GLP-1-aware demand sensing (Frozen & Coffee)
**Role framing:** AI Solutions Architect (late-2026 stack: MCP & A2A, AI gateways, permission-aware retrieval, enterprise governance)
**Status:** Draft / reference architecture (reconstruction — validate before external use)
**Owner:** AI Solutions Architect (Capgemini Engineering)
**Last updated:** 2026-11-22

---

## How to use this document

This is the **single entry point** for the project. It summarizes every area of the `documentation/` folder and links to the detailed files. Read it top-to-bottom for the full story, or jump to the area you need.

| Area | This doc § | Detailed source |
|---|---|---|
| Business & strategy | §3 | `documentation/01-business-and-strategy/` |
| Product & UX | §4 | `documentation/02-product-and-ux/` |
| System architecture | §5 | `documentation/03_system_and_architecture/` |
| Engineering & code | §6 | `documentation/04_engineering_and_code/` |
| Quality & verification | §7 | `documentation/05-quality-and-verification/` |
| Operations & infrastructure | §8 | `documentation/06-operations-and-infrastructure/` |
| Security & compliance | §9 | `documentation/07-security-compliance-and-users/` |
| Glossary | §12 | `documentation/00-glossary-and-terminology.md` |

**Source-of-truth hierarchy:** ADRs/decision-log → system design → scope/SLA → requirements → everything else. (See `documentation/README.md`.)

---

## 1. Document control

| Field | Value |
|---|---|
| Version | 1.0 |
| Date | 2026-11-22 |
| Author | AI Solutions Architect (Capgemini Engineering) |
| Reviewers | Nestlé USA Demand Planning; Enterprise Architecture; Security & Compliance |
| Classification | Internal — contains reconstructed project design |
| Related | `Nestle-USA-DemandSensing-AIArchitect-UseCase.md` (use case), `Nestle-USA-DemandSensing-ProjectDoc.md` (source spec), `Nestle-USA-Research.md` (company) |

---

## 2. Executive summary

### 2.1 The problem

Nestlé USA faces a **structural demand break**:

1. **Volumes are declining** — US food volume per person fell 0.6% in H1 2026.
2. **Frozen is the most exposed** — GLP-1 adoption is associated with a ~3-point drop in dollar spend in year one; frozen is where Nestlé is investing most.
3. **The old forecasting regime is dead** — models trained on 2015–2022 history encode a world without GLP-1, without private label at 23.8% of units, and without cocoa at ~$3,500/t. They produce confident, wrong numbers.

The gap is **predictive and causal**: not "what happened on the shelf" (descriptive, covered by digital-shelf monitoring) but **"what will happen 2–3 quarters ahead, and why."**

### 2.2 The solution

> An agentic, permission-aware decision-support platform that turns structured demand data and unstructured consumer signal into calibrated, causally-attributed, store-level forecasts — and lets a planner interrogate them conversationally.

**Core design decision: the LLM never forecasts.** It extracts structured signals and narrates grounded results; the constrained solver decides. The moat is **data + causal discipline + governance**, not the model.

### 2.3 The 6-layer architecture

| Layer | Purpose | Key tech |
|---|---|---|
| **1. Cloud & managed AI** | Hybrid cloud, managed models, inference | Databricks, Snowflake Cortex, Fabric, Azure AI Foundry, Bedrock/Vertex, vLLM/NIM |
| **2. Model routing & gateway** | Cost control, no lock-in | Portkey/LiteLLM, semantic cache, chargeback |
| **3. Data & permission-aware RAG** | Governed data, grounding | Iceberg, dbt, Kafka, Feast, Azure AI Search, pgvector, Neo4j, Docling |
| **4. Agentic orchestration** | Integration, coordination | MCP, A2A, LangGraph, MS Agent Framework, Temporal, FastAPI, TypeScript |
| **5. Security & governance** | Identity, DLP, guardrails | Entra ID, Okta, OPA, NeMo Guardrails, Lakera, Purview, Vault |
| **6. FinOps & observability** | ROI, reliability | LangSmith, Arize, Braintrust, MLflow, OpenTelemetry, Datadog, Grafana |

### 2.4 Success criteria

- Out-of-regime WMAPE improves ≥15% relative vs. incumbent.
- Attribution sign-consistent across rolling windows.
- Intervals calibrated; no income-quintile bias.
- Planner adoption ≥ 80%.

---

## 3. Business & strategy

**Detailed source:** `documentation/01-business-and-strategy/`

### 3.1 Business case & ROI

The business case rests on three value drivers: avoided stockouts/overproduction (better store-level forecasts), trade-spend efficiency (causal attribution separates price/mix), and faster response to regime shifts (GLP-1 as a first-class driver). ROI is measured via a cost/ROI model with illustrative figures to be replaced with Nestlé USA actuals. See `business-case-and-roi.md` and `10_cost_roi_and_alternatives/`.

### 3.2 Scope & SLAs

**In scope:** demand sensing for Frozen and Coffee; GLP-1-aware forecasting with causal attribution; hierarchical forecasts (store → banner → DMA → national); conversational scenario copilot; permission-aware retrieval; continuous evaluation; audit trail.

**Out of scope:** price-setting, LLM-based forecasting, cross-retailer pooling without permission, household-level PII, descriptive shelf monitoring.

**SLAs:** copilot p95 ≤ 5s; scenario p95 ≤ 10s; nightly batch by 06:00; availability 99.9%; data freshness ≤ 24h. See `project-scope-and-sla.md` and `01_project_overview_and_context.md`.

### 3.3 Stakeholders & governance

Steering Committee (Sponsor + Product Owner + Architect) → Change Advisory Board → Delivery (Data Science, ML Eng, Platform, Security). RACI and decision rights in `02_stakeholders_and_governance.md`.

### 3.4 Goals & KPIs

Six goals (accuracy, causal explanation, trade-spend efficiency, productivity, governance, FinOps) with a KPI tree: weekly active planners (North Star), out-of-regime WMAPE, attribution sign consistency, adoption ≥ 80%, availability 99.9%, PII incidents 0. See `03_business_goals_and_kpis.md`.

### 3.5 Personas & scenarios

Four personas: Demand Planner (Priya), RGM Analyst (Arjun), Supply Planner (Meera), Data Steward (Vikram). Primary scenario: "GLP-1 +5pp in SE → DiGiorno by Q3?" See `07_personas_and_business_scenarios.md`.

### 3.6 Cost, ROI & alternatives

Hybrid build-vs-buy: buy managed infra (Databricks/Snowflake/Fabric/Azure/Bedrock), build the moat (causal attribution, permission-aware RAG, agentic orchestration, copilot). See `10_cost_roi_and_alternatives/` (build_vs_buy_options.md, cost_and_roi_summary.md, financial_model.xlsx).

### 3.7 Risks

14-item risk register: retailer data access, regime shift outpacing updates, adoption resistance, overclaiming accuracy, PII leakage, LLM hallucination, prompt injection, vendor lock-in, cost overrun, model drift, key-person dependency, integration complexity, panel licensing, scope creep. See `11_risk_analysis_and_mitigation.md`.

### 3.8 Tenets

1. LLM never forecasts. 2. Causal claims require causal evidence. 3. Point-in-time correctness is non-negotiable. 4. Governance is a feature. 5. Calibrated over confident. 6. Boring, auditable designs. 7. Period-accurate tooling. See `06_tenets_and_guiding_principles.md`.

---

## 4. Product & UX

**Detailed source:** `documentation/02-product-and-ux/`

### 4.1 Users & motivations

Personas + empathy maps; JTBD with triggers, alternatives, and desired progress. The value proposition: "For demand planners who can't trust history-based forecasts in a GLP-1 world, the Scenario Copilot delivers calibrated, causally-attributed forecasts — so you can answer 'what next, and why' in seconds, not days." See `01_users_and_motivations/`.

### 4.2 Core value & retention

The **magic moment**: a planner types a plain-English question and gets a defensible, explainable answer in seconds, with P10/P50/P90 numbers, a causal breakdown, and a run ID. Core loops: weekly planning loop, continuous feedback loop (accept/adjust/reject → labels), trust loop (out-of-regime eval → adoption). See `02_core_value_and_retention/`.

### 4.3 Experience & system mapping

Customer journey + service blueprint (frontstage: copilot/dashboard; backstage: gateway/agents/data; processes: Entra/OPA/Purview/MLflow/LangSmith/Datadog). Object model (ForecastRun, ForecastLine, Attribution, Scenario, Store/Banner/DMA, Product). UX-to-system-state mapping (loading/success/partial/permission-denied/error/stale). See `03_experience_and_system_mapping/`.

### 4.4 Permissions & plan tiers

Roles (Viewer, Planner, RGM Analyst, Data Steward, Admin, Auditor); ABAC attributes (role, team, assigned banners/DMAs); OPA policy; plan tiers with quotas (Standard/Power/Enterprise). See `04_permissions_and_plan_tiers.md`.

### 4.5 Edge cases & resilience

Empty/loading/error states; graceful degradation ladder (L0 full → L4 read-only); trust/safety/abuse vectors (prompt injection, jailbreak, data exfiltration, cost exhaustion, fraud, model poisoning, overclaiming) with mitigations. See `05_edge_cases_and_resilience/`.

### 4.6 Analytics & experimentation

Event taxonomy (`object_action` naming, common properties, event→metric mapping); North Star (weekly active planners with a trusted forecast) + funnel; A/B tests and cohort rollouts with feature flags. See `06_analytics_and_experimentation/`.

---

## 5. System architecture

**Detailed source:** `documentation/03_system_and_architecture/`

### 5.1 Requirements & capacity

Functional requirements (demand + supply + data); NFR matrix (performance, reliability, scalability, security, compliance, observability, usability, maintainability); back-of-envelope capacity estimates (QPS, bandwidth, storage, cache, compute, LLM token budget). See `01_requirements_and_capacity_estimation/`.

### 5.2 Tech choices & ADRs

Full-stack and infra tech choices; rendering/delivery strategy; ADRs:
- **ADR-001** Initial architecture baseline (hybrid 6-layer)
- **ADR-002** Database selection (polyglot persistence: Databricks + Snowflake + Iceberg + Feast + Azure AI Search/pgvector + Neo4j)
- **ADR-003** Authentication strategy (federated Entra ID + externalized OPA/ABAC)
- **Decision log** D-001..D-013

See `02_tech_choices_and_adrs/`.

### 5.3 High-level design

End-to-end system architecture (with PNG diagram); UI/micro-frontend topology (React MFE, module federation); backend/BFF service boundaries (modular monolith + microservices, DDD, BFF); AI/ML integration pipeline (LLM serving, RAG, embeddings, token limits); agent contracts (Agent | Tools (MCP) | Never). See `03_high_level_design_hld/`.

### 5.4 Frontend architecture

Component hierarchy + design system; state management + client cache (React Query, IndexedDB); routing/forms/validation (deep links, guards, Zod); browser runtime + web workers; accessibility + i18n/l10n; performance/bundling/web vitals (LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1). See `04_detailed_frontend_architecture/`.

### 5.5 Backend & async design

Core workflows + distributed algorithms (critical paths, sagas, locks, consensus, idempotency); CDN/edge/distributed caching (Redis, semantic cache, invalidation); event queues/background jobs (Kafka, DLQ, outbox, Temporal). See `05_detailed_backend_and_async_design/`.

### 5.6 Data model & storage

Client normalized/offline storage (IndexedDB, Service Workers, PWA sync); database schemas + ERD (Iceberg DDL, indexing, partitioning, PNG diagram); storage/search/data lifecycle (hot/warm/cold, Azure AI Search/pgvector/Neo4j, TTL, archival); integration & data strategy (12 data sources, SAP/Salesforce/ServiceNow via MCP). See `06_data_model_and_storage/`.

### 5.7 API & network

API contracts + versioning (REST/GraphQL/gRPC, pagination, idempotency); data exchange formats (JSON/YAML/CSV/Protobuf/Avro/Thrift); transfer & streaming protocols (HTTP/3, WS, SSE, SFTP); network resilience + rate limiting (retries, backoff, circuit breakers, batching). See `07_api_and_network_communication/`.

### 5.8 Bottlenecks, scalability & DR

Bottlenecks/SPOFs/hotspots (hot SKU/store, celebrity queries, shard rebalancing, backpressure); load balancing + auto-scaling (L4/L7, HPA/KEDA); HA/backups/DR (multi-region, RPO ≤ 24h, RTO ≤ 4h, chaos testing); FinOps/cost optimization (chargeback, tiered storage, spot). See `08_bottlenecks_scalability_and_dr/`.

---

## 6. Engineering & code

**Detailed source:** `documentation/04_engineering_and_code/`

### 6.1 Codebase organization

Monorepo layout (`apps/`, `ml/`, `infra/`, `policies/`, `shared/`); module boundaries; coding conventions (Black/Ruff/mypy for Python, Prettier/ESLint/tsc for TS); dependency management + DI (FastAPI `Depends`, constructor injection, IoC container). See `01_codebase_organization_and_standards/`.

### 6.2 Low-level design & patterns

UML modeling + use cases; class/interface/model definitions (entities, value objects, DTOs); design patterns (Strategy, Observer, Factory, Repository, Adapter, Facade, Saga, Circuit Breaker); state machines (forecast run lifecycle, scenario lifecycle, model promotion); PlantUML diagram sources (class, sequence, state). See `02_low_level_design_and_patterns/`.

### 6.3 Concurrency & runtime

Concurrency/threading/async model (asyncio, process pools, Temporal); memory management + resource pools (GC tuning, connection pools, leak prevention); synchronization + locking (mutexes, semaphores, distributed locks, deadlock avoidance). See `03_concurrency_and_runtime_execution/`.

### 6.4 Internal APIs & extensibility

Public methods + SDK contracts (ForecastModel, AttributionStrategy, ModelRouter, Repository); extensibility + plugin architecture (Strategy/Observer hooks, middleware, feature flags); error handling + resilience (exception hierarchy, Result/Either, RFC 7807). See `04_internal_apis_and_extensibility/`.

### 6.5 Quality & developer workflow

Unit/integration test patterns (mocking, fixtures, coverage targets); git workflow + code review (branching, conventional commits, PR templates). See `05_code_quality_and_developer_workflow/`.

### 6.6 Reference implementation

Runnable Python LLD code demonstrating the domain model, state machine, strategy pattern, and per-key locking. **9 tests pass** (`python -m unittest discover -s tests -v`). See `06_reference_implementation/`.

---

## 7. Quality & verification

**Detailed source:** `documentation/05-quality-and-verification/`

- **Master test strategy:** unit/integration/contract/eval/adversarial/E2E/visual/performance/accessibility; release gates (WMAPE degradation > 5% blocks, interval coverage, adversarial prompts, PII leaks).
- **Acceptance criteria & cases:** AC-1..AC-6 (forecast generation, permission-aware retrieval, scenario what-if, LLM never forecasts, audit trail, out-of-regime eval) + TC-01..TC-08 + NFR acceptance.
- **Performance & load reports:** targets, load model (100–300 concurrent), results template, bottlenecks & mitigations, scalability plan.

See `05-quality-and-verification/`.

---

## 8. Operations & infrastructure

**Detailed source:** `documentation/06-operations-and-infrastructure/`

- **Cloud infrastructure topology:** Azure primary, AWS/GCP fallback, Databricks/Snowflake/Fabric, AKS, private endpoints, US data residency.
- **Environments & secrets:** dev/ci/staging/prod matrix, promotion rules, Vault secrets, rotation, config-as-code.
- **CI/CD & release:** commit → build → test → eval → staging → approval → prod (canary → full); Terraform, Helm, Argo CD; SemVer; quality gates.
- **Disaster recovery:** RPO ≤ 24h, RTO ≤ 4h; backup/restore; chaos testing; quarterly DR drills.
- **Incident runbooks:** `db-failover-runbook.md`, `high-latency-troubleshooting.md`.

See `06-operations-and-infrastructure/`.

---

## 9. Security & compliance

**Detailed source:** `documentation/07-security-compliance-and-users/`

- **Threat model & encryption:** STRIDE threats, AI-specific threats (prompt injection, hallucination, data exfiltration, model poisoning), encryption (TLS 1.2+, AES-256), key management (Vault/Key Vault).
- **Data privacy & retention:** data classification, privacy principles, PII masking, retention (sell-out 3y, forecasts 2y, prompts 90d, audit 7y), compliance mapping, US data residency.
- **End-user & support:** help center guides, support escalation matrix (S1–S4, tiers T1–T5), release notes/changelog.

See `07-security-compliance-and-users/`.

---

## 10. The agent team (orchestration)

| Agent | Responsibility | Tools (MCP) | Never |
|---|---|---|---|
| **Data Agent** | Fetch/validate data, enforce permissions | `query_snowflake`, `get_glp1_penetration`, `get_attribution`, `fetch_retailer_contract_terms` | Leak restricted data |
| **Forecast Agent** | Run regime-aware forecast + intervals | `run_forecast`, `get_feature_store` | Use LLM to forecast |
| **Attribution Agent** | Synthetic control / DiD, decompose deltas | `synthetic_control`, `did` | Claim causality without validation |
| **Scenario Agent** | Answer what-if, narrate results | forecast + attribution + copilot | Set prices |
| **Governance Agent** | PII redaction, policy checks, citations | Purview, OPA, NeMo | Allow PII into prompts |

**Tool surface = permission boundary.** The Forecast Agent has no free-text generation tool; the Scenario Agent has no price-setting tool. This is how "LLM never forecasts / never sets prices" is enforced architecturally, not by prompt.

---

## 11. Worked example — a planner's Monday morning

> **Planner (Teams):** "GLP-1 keeps climbing in the Southeast. If it's up 5 points by Q3, what happens to DiGiorno and Hot Pockets, and which banners should I worry about?"

1. **Copilot** → **AI Gateway**: Entra ID auth, OPA policy check (Southeast + Frozen), route to **Frontier**.
3. **Scenario Agent** → **Attribution Agent** (A2A): synthetic control per DMA, DiD on the adoption ramp → GLP-1 effect separable from price/distribution.
4. **Forecast Agent**: regime-aware forecast with GLP-1 +5pp shock, MinT reconciliation, P10/P50/P90.
5. **Data Agent** (MCP): banner list, contract terms, data-quality flags.
6. **Governance Agent**: no price recommendation, cite run ID, redact PII.
7. **Copilot** narrates: *"By Q3, DiGiorno units −6.2% (P10 −8.1%, P90 −4.4%) vs. plan. Concentrated in 3 banners in 2 DMAs. GLP-1 −2.1pp, price −1.3pp, distribution −0.8pp, private label −0.5pp. Run ID FR-2026-11-22-0142."*
8. **Observability:** LangSmith logs the trace, Datadog tracks latency/cost, MLflow links the model.

Every number is a forecast; every "why" is a causal estimate; every sentence is LLM-narrated but **grounded** in a run the planner can audit.

---

## 12. Traceability matrix

| Business goal | Feature | Component | Test |
|---|---|---|---|
| G1 Accuracy under regime shift | Regime-aware forecasting (GLP-1) | Forecast Agent + LightGBM/TFT | Out-of-regime WMAPE eval |
| G2 Explain demand changes | Causal attribution | Attribution Agent (synthetic control/DiD) | Sign-consistency + placebo |
| G3 Trade-spend efficiency | Price/mix decomposition | Attribution + RGM copilot | Holdout experiment |
| G4 Planner productivity | Scenario copilot | Scenario Agent + FastAPI + React | E2E + adoption funnel |
| G5 Governance & audit | Permission-aware retrieval | OPA + Data Agent + audit log | AC-2, AC-5, TC-02 |
| G6 FinOps | Chargeback | AI Gateway + cost tags | FinOps review |
| Safety: LLM never forecasts | No diet/price generation | Forecast Agent tool surface | AC-4, TC-06 |
| Safety: no PII | Redaction + DLP | Purview + Governance Agent | NFR-SEC3, threat model |

---

## 13. Technology stack (consolidated)

| Layer | Primary | Alternatives |
|---|---|---|
| **Cloud/AI** | Azure (AI Foundry, Fabric, Entra, Purview), Databricks, Snowflake, AWS (Bedrock, SageMaker), GCP (Vertex) | — |
| **Gateway** | Portkey / LiteLLM (Kong, Azure API Management) | — |
| **Data** | Iceberg, dbt, Kafka, Feast, Snowflake, Databricks, Fabric | — |
| **RAG** | Azure AI Search, pgvector/Qdrant, Neo4j, Docling/Unstructured/LlamaParse | — |
| **Forecast** | LightGBM / Temporal Fusion Transformer | Prophet, statsmodels |
| **LLM** | Azure OpenAI, Bedrock, Vertex; small/fast (Gemini Flash, Claude Haiku, Llama-3, Qwen); frontier (o-series, Claude, Gemini Pro) | — |
| **Agents** | LangGraph + MS Agent Framework + Temporal; MCP + A2A; FastAPI + TypeScript | — |
| **Governance** | Entra ID, Okta, AWS IAM, OPA, NeMo Guardrails, Lakera, Purview, Vault | — |
| **Ops** | LangSmith, Arize, Langfuse, Braintrust, MLflow, OpenTelemetry, Datadog, Grafana | — |

Full tables with alternatives: `documentation/03_system_and_architecture/02_tech_choices_and_adrs/01_full_stack_and_infra_tech_choices.md`.

---

## 14. Claims discipline & caveats

- **All four business-unit projects are reconstructions** aligned with Nestlé USA's actual context, not verified internal case studies. Validate before external use.
- **The LLM never forecasts** — it extracts structured signals and narrates. This is the design's core defensibility.
- **Entity ambiguity:** the source docs attribute the work to Nestlé USA; confirm the legal employer.
- **2026 figures** (group revenue, headcount, private-label share, GLP-1 prevalence) are from `Nestle-USA-Research.md` and are company-reported or third-party estimates.
- **Period accuracy:** the late-2026 stack (MCP, A2A, Portkey/LiteLLM, vLLM/NIM, NeMo Guardrails, LangGraph, Temporal) is target-state; the tenure spans 2022–2026.
- **Financial and headcount figures are unaudited.**

---

## 15. Glossary (business-facing)

| Term | Definition |
|---|---|
| **GLP-1** | Glucagon-like peptide-1 receptor agonists — weight-loss/diabetes drugs associated with reduced food-basket spend. |
| **Regime shift** | A change in the demand process (GLP-1, private label, input costs) that invalidates history-based models. |
| **Banner / DMA** | Retail banner / Designated Market Area (Nielsen geography). |
| **Sell-in / Sell-out** | Nestlé shipments to retailer / retailer sales to consumers. |
| **Panel data** | Household-level purchase panel (Circana/Nielsen). |
| **WMAPE** | Weighted Mean Absolute Percentage Error — primary forecast accuracy metric. |
| **Out-of-regime** | Testing on data beyond the training regime (train ≤2022, test 2024–26). |
| **Causal attribution** | Decomposing a demand delta into drivers (GLP-1, price, mix, private label). |
| **Synthetic control / DiD** | Causal methods constructing a counterfactual / comparing exposed vs. control. |
| **MinT** | Minimum Trace reconciliation for hierarchical forecasts. |
| **MCP / A2A** | Model Context Protocol (tool/data access) / Agent-to-Agent (coordination). |
| **RAG / GraphRAG** | Retrieval-Augmented Generation / over a knowledge graph. |
| **ABAC / OPA** | Attribute-Based Access Control / Open Policy Agent. |
| **FinOps** | Financial operations for cloud/AI cost management. |

Full glossary: `documentation/00-glossary-and-terminology.md`.

---

## 16. Document index (detailed files)

### 01-business-and-strategy/
- `00_executive_summary_and_signoffs/executive_summary.md`, `approval_and_change_log.md`
- `01_project_overview_and_context.md`, `02_stakeholders_and_governance.md`, `03_business_goals_and_kpis.md`
- `04_current_vs_future_state/as_is_workflow_and_pain_points.md`, `to_be_target_capabilities.md`
- `05_scope_and_boundaries/in_scope_and_out_of_scope.md`, `assumptions_and_dependencies.md`
- `06_tenets_and_guiding_principles.md`, `07_personas_and_business_scenarios.md`
- `08_high_level_functional_requirements.md`, `09_non_functional_business_constraints.md`
- `10_cost_roi_and_alternatives/build_vs_buy_options.md`, `cost_and_roi_summary.md`, `financial_model.xlsx`
- `11_risk_analysis_and_mitigation.md`, `12_domain_glossary.md`, `13_high_level_solution_overview.md`

### 02-product-and-ux/
- `01_users_and_motivations/`, `02_core_value_and_retention/`, `03_experience_and_system_mapping/`
- `04_permissions_and_plan_tiers.md`, `05_edge_cases_and_resilience/`, `06_analytics_and_experimentation/`

### 03_system_and_architecture/
- `01_requirements_and_capacity_estimation/`, `02_tech_choices_and_adrs/` (+ ADRs), `03_high_level_design_hld/`
- `04_detailed_frontend_architecture/`, `05_detailed_backend_and_async_design/`, `06_data_model_and_storage/`
- `07_api_and_network_communication/`, `08_bottlenecks_scalability_and_dr/`, `09_security_and_compliance/`, `10_testing_cicd_and_observability/`

### 04_engineering_and_code/
- `01_codebase_organization_and_standards/`, `02_low_level_design_and_patterns/` (+ diagrams), `03_concurrency_and_runtime_execution/`
- `04_internal_apis_and_extensibility/`, `05_code_quality_and_developer_workflow/`, `06_reference_implementation/`

### 05-quality-and-verification/
- `master-test-strategy.md`, `acceptance-criteria-and-cases.md`, `performance-and-load-reports.md`

### 06-operations-and-infrastructure/
- `cloud-infrastructure-topology.md`, `environments-and-secrets.md`, `cicd-and-release-process.md`, `disaster-recovery-plan.md`, `incident-runbooks/`

### 07-security-compliance-and-users/
- `security-and-compliance/threat-model-and-encryption.md`, `data-privacy-and-retention.md`
- `end-user-and-support/user-help-center-guides.md`, `support-escalation-matrix.md`, `release-notes-changelog.md`

---

## 17. Provenance

- Company facts: `Nestle-USA-Research.md` (2026-11-21), reflecting the 2026 Nestlé USA context.
- Project design: `Nestle-USA-DemandSensing-ProjectDoc.md` (retrospective spec) and `Nestle-USA-DemandSensing-AIArchitect-UseCase.md` (use case).
- Documentation set: `documentation/` (7 folders, ~135 files).
- This document is a consolidation; where it conflicts with the detailed files, the **source-of-truth hierarchy** (§How to use this document) applies.
- All projects are reconstructions to be validated against the author's actual record before publication.