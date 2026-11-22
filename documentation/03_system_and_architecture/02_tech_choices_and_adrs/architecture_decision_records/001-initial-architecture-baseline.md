# ADR 001: Initial Architecture Baseline

## Status

Accepted (2026-11-22)

## Context

We are building the Agentic GLP-1 Demand Sensing & Scenario Copilot for Nestlé USA. We need an initial architecture baseline that:
- Reuses existing investments (Snowflake, Microsoft stack).
- Supports agentic orchestration over open protocols (MCP/A2A).
- Enforces permission-aware retrieval and auditability.
- Avoids vendor lock-in.
- Is period-accurate (2026 stack).

## Decision

Adopt a **hybrid, 6-layer architecture**:

1. **Cloud & managed AI:** Azure primary, AWS/GCP fallback; Databricks + Snowflake + Fabric.
2. **AI gateway:** Portkey/LiteLLM with semantic caching, fallback, chargeback.
3. **Data + permission-aware RAG:** Iceberg, dbt, Kafka, Feast; Azure AI Search + pgvector/Qdrant + Neo4j; Docling/Unstructured.
4. **Agentic orchestration:** LangGraph + MS Agent Framework + Temporal over MCP/A2A; FastAPI + TypeScript.
5. **Security:** Entra ID, Okta, AWS IAM, OPA, NeMo Guardrails, Lakera, Purview, Vault.
6. **FinOps/observability:** LangSmith, Arize, Langfuse, Braintrust, MLflow; OpenTelemetry, Datadog, Grafana.

**Key rule:** the LLM never forecasts; it extracts and narrates. The constrained solver decides.

## Consequences

**Positive:**
- Reuses Snowflake/Microsoft investments.
- Open protocols avoid lock-in.
- Governance and auditability first-class.
- Period-accurate, production-ready stack.

**Negative:**
- Polyglot complexity (multi-cloud, multi-store).
- Requires skilled platform team.
- Integration effort (SAP/Salesforce/ServiceNow).

**Mitigations:**
- Iceberg as shared substrate.
- Phased delivery (Foundations → Intelligence → Copilot → Scale).
- Managed services for commodity layers.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| Single cloud (Azure only) | Simplicity | Lock-in; no Bedrock/Vertex fallback |
| Build everything custom | Control | Cost/time; reinventing gateway/RAG |
| Buy off-the-shelf suite | Speed | Weak causal; poor GLP-1 fit; lock-in |

## Compliance / Governance

- Retailer contracts: no pooling without permission.
- Panel privacy: aggregate only.
- Audit: every run logged.
- Microsoft-centric identity.

## References

- `Nestle-USA-DemandSensing-AIArchitect-UseCase/03-system-and-architecture/system-design-document.md`
- `Nestle-USA-DemandSensing-AIArchitect-UseCase/03-system-and-architecture/architecture-decision-records/001-database-selection.md`
- `.../002-authentication-strategy.md`
- `../01_full_stack_and_infra_tech_choices.md`