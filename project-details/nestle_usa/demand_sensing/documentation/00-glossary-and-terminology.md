# 00 — Glossary and Terminology

Single source of truth for terms, acronyms, and definitions used across this documentation set.

## Business & domain

| Term | Definition |
|---|---|
| **GLP-1** | Glucagon-like peptide-1 receptor agonists (e.g., semaglutide, tirzepatide) — weight-loss/diabetes drugs associated with reduced food-basket spend. Treated here as a first-class exogenous demand driver. |
| **Regime shift / structural break** | A change in the demand process itself (e.g., GLP-1 penetration, private-label share, input-cost shocks) that invalidates models trained on prior history. |
| **Banner** | A retail banner (e.g., a specific grocery chain) within a retailer group. |
| **DMA** | Designated Market Area — a geographic market (Nielsen) used for store clustering. |
| **Sell-in** | Nestlé shipments to the retailer. |
| **Sell-out** | Retailer sales to consumers (scanner/loyalty). |
| **Panel data** | Household-level purchase panel (e.g., Circana/Nielsen). |
| **RIG** | Nestlé's "Refrigeration/Regeneration/Innovation" or, in this context, the group's Registered/Recognised Innovation Governance contribution metric — used here as the value-reporting mechanism to finance. |
| **MinT** | Minimum Trace reconciliation method for hierarchical forecast reconciliation. |
| **Analog forecasting** | Forecasting a reformulated/new product using a comparable historical product as a proxy. |

## Technical

| Term | Definition |
|---|---|
| **WMAPE** | Weighted Mean Absolute Percentage Error — the primary forecast accuracy metric. |
| **MAPE** | Mean Absolute Percentage Error (secondary). |
| **Bias** | Mean signed error (secondary). |
| **Interval calibration** | Whether P10/P50/P90 prediction intervals contain the truth at the stated rate. |
| **Synthetic control** | A causal method constructing a weighted "donor pool" counterfactual for an exposed unit. |
| **DiD** | Difference-in-differences — a causal design comparing exposed vs. control pre/post. |
| **Causal attribution** | Decomposing a demand delta into drivers (GLP-1, price, mix, distribution, private label). |
| **Point-in-time correctness** | Ensuring features use only data available at prediction time (no leakage). |
| **Out-of-regime evaluation** | Testing on data beyond the training regime (e.g., train ≤2022, test 2024–26). |
| **Hierarchical reconciliation** | Making store → banner → DMA → national forecasts consistent. |

## Platform & architecture

| Term | Definition |
|---|---|
| **MCP** | Model Context Protocol — open standard for LLM tool/data access. |
| **A2A** | Agent-to-Agent — open protocol for cross-agent coordination. |
| **AI Gateway** | Centralized control point between apps and foundation models (routing, caching, rate limit, chargeback). |
| **RAG** | Retrieval-Augmented Generation — grounding LLM output in retrieved context. |
| **GraphRAG** | RAG over a knowledge graph (Neo4j). |
| **ABAC** | Attribute-Based Access Control — permission decisions over attributes (banner, DMA, role). |
| **OPA** | Open Policy Agent — policy decision point for ABAC. |
| **Semantic caching** | Serving semantically-equivalent queries from cache. |
| **Chargeback** | Attributing token/compute spend to a business unit. |
| **FinOps** | Financial operations for cloud/AI cost management. |
| **DLP** | Data Loss Prevention. |
| **Out-of-regime WMAPE** | WMAPE measured on out-of-regime (post-break) data — the honest accuracy metric. |

## Abbreviations

| Abbreviation | Expansion |
|---|---|
| **GLP-1** | Glucagon-like peptide-1 |
| **DMA** | Designated Market Area |
| **RIG** | Registered/Recognised Innovation Governance (value reporting) |
| **MCP** | Model Context Protocol |
| **A2A** | Agent-to-Agent |
| **RAG** | Retrieval-Augmented Generation |
| **ABAC** | Attribute-Based Access Control |
| **OPA** | Open Policy Agent |
| **DLP** | Data Loss Prevention |
| **FinOps** | Financial Operations |
| **SLA** | Service Level Agreement |
| **NFR** | Non-Functional Requirement |
| **ADR** | Architecture Decision Record |
| **CI/CD** | Continuous Integration / Continuous Delivery |
| **DR** | Disaster Recovery |
| **p95** | 95th percentile latency |