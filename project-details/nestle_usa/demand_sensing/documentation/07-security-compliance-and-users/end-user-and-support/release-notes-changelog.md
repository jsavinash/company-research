# Release Notes and Changelog

All notable changes to the Agentic GLP-1 Demand Sensing & Scenario Copilot are documented here. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Planned
- Copilot v2 (streaming answers, richer what-ifs)
- Cross-category reuse (Coffee → Baking)
- FinOps chargeback dashboards

## [1.0.0] — 2026-11-22

### Added
- **Forecast core:** regime-aware LightGBM / Temporal Fusion Transformer with hierarchical reconciliation (MinT), P10/P50/P90 intervals.
- **GLP-1 driver:** first-class exogenous regressor with geographic/income heterogeneity.
- **Causal attribution:** synthetic control + DiD, sign-consistency checks, per-driver effects.
- **Scenario copilot:** conversational what-if ("GLP-1 +5pp in SE") with grounded, narrated answers and run IDs.
- **Agentic orchestration:** Data / Forecast / Attribution / Scenario / Governance agents on LangGraph + MS Agent Framework + Temporal, over MCP tools and A2A.
- **AI gateway:** Portkey/LiteLLM with semantic caching, fallback routing, rate limiting, chargeback.
- **Data platform:** Databricks (Unity Catalog) + Snowflake + Fabric; Iceberg, dbt, Kafka, Feast.
- **RAG:** Azure AI Search + pgvector/Qdrant + Neo4j GraphRAG; Docling/Unstructured/LlamaParse ingestion.
- **Governance:** Entra ID, Okta, AWS IAM, OPA/ABAC; NeMo Guardrails, Lakera, Purview, Vault.
- **Observability:** LangSmith, Arize, Langfuse, Braintrust, MLflow; OpenTelemetry, Datadog, Grafana.
- **Evaluation:** out-of-regime WMAPE (train ≤2022, test 2024–26), interval calibration, bias-by-income-quintile.
- **Documentation set:** this folder.

### Security
- Permission-aware retrieval (per banner/DMA) via OPA.
- No PII in prompts; DLP via Purview.
- Audit trail for every forecast/scenario.

### Notes
- This is a target-state reference architecture (reconstruction). Validate all figures before external use.

## Version history

| Version | Date | Notes |
|---|---|---|
| 1.0.0 | 2026-11-22 | Initial target-state architecture + documentation set |

## How to add entries

- Use `Added` / `Changed` / `Deprecated` / `Removed` / `Fixed` / `Security`.
- Reference the decision-log / ADR ID for architectural changes.
- Link to the PR / release.