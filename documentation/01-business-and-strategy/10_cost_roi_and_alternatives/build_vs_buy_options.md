# Build vs. Buy Options

## 1. Options considered

| Option | Description | Pros | Cons |
|---|---|---|---|
| **A. Build (custom platform)** | Full custom 6-layer build | Full control; moat (causal + governance) | High cost; long timeline; talent |
| **B. Buy (managed suite)** | Buy an off-the-shelf demand-sensing / AIOps suite | Fast; vendor-supported | Lock-in; weak causal; poor fit for GLP-1 |
| **C. Hybrid (recommended)** | Buy managed infra (cloud, gateway, data), build the moat (causal + governance + copilot) | Best of both; avoids lock-in; reuses Snowflake | Requires integration discipline |

## 2. Recommendation

**Hybrid (Option C):**
- **Buy:** Databricks, Snowflake, Azure AI Foundry/Bedrock, AI gateway (Portkey/LiteLLM), observability.
- **Build:** causal attribution layer, permission-aware retrieval (OPA policies), agentic orchestration, copilot UX, out-of-regime evaluation.
- **Reuse:** existing Snowflake retailer data; Entra ID; Fabric.

## 3. Build vs. buy by component

| Component | Build/Buy | Rationale |
|---|---|---|
| Lakehouse / warehouse | Buy (Databricks, Snowflake) | Managed, compliant, exists |
| AI gateway | Buy (Portkey/LiteLLM) | Avoid reinventing routing/caching |
| Frontier models | Buy (Azure OpenAI/Bedrock/Vertex) | Commodity |
| Forecast core | Build (LightGBM/TFT) | Domain-specific, causal |
| Causal attribution | Build | Moat; not off-the-shelf |
| Permission-aware RAG | Build (OPA + retrieval) | Governance-critical |
| Agentic orchestration | Build (LangGraph + Temporal) | Workflow-specific |
| Copilot UX | Build | User-specific |
| Observability | Buy (LangSmith/Datadog) | Managed |
| Evaluation | Build (out-of-regime harness) | Honest accuracy |

## 4. Vendor trade-offs

| Vendor | Strength | Risk | Mitigation |
|---|---|---|---|
| Azure (AI Foundry/OpenAI) | Enterprise compliance, Entra | Cost | Gateway + caching |
| AWS Bedrock | Model variety | Multi-cloud complexity | Fallback routing |
| Databricks | Lakehouse + ML | Cost | Reserved capacity |
| Snowflake | Warehouse + Cortex | Cost | Reuse existing |
| Portkey/LiteLLM | Gateway | Maturity | Fallback to Kong/AxAPI |

## 5. Commercial considerations

- **Lock-in:** mitigated by Iceberg + open protocols (MCP/A2A) + gateway abstraction.
- **Cost:** managed services + chargeback; avoid over-provisioning.
- **Exit:** data in Iceberg is portable; models in MLflow; policies as code.

## 6. Decision

Hybrid. See ADRs for database and auth decisions in `../../Nestle-USA-DemandSensing-AIArchitect-UseCase/03-system-and-architecture/architecture-decision-records/`.