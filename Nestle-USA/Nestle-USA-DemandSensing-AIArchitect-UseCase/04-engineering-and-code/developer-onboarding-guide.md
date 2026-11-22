# Developer Onboarding Guide

## 1. Prerequisites

- Access to: GitHub/GitLab, Databricks, Snowflake, Azure (Entra ID), AWS (Bedrock), Neo4j, Azure AI Search.
- Tools: Python 3.11, Node 20, Docker, `uv`/`pipenv`, `dbt`, Terraform/Az CLI.
- Policies: signed NDA, data-privacy training, security awareness.

## 2. Local setup

```bash
# clone
git clone <repo>
cd nestle-demand-sensing

# python env
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# env vars (from Vault — never commit)
export SNOWFLAKE_ACCOUNT=...
export DATABRICKS_HOST=...
export ENTRA_TENANT_ID=...
export OPA_URL=...

# run tests
pytest -q

# run the copilot locally
make dev-copilot
```

## 3. Repository layout

```
/apps
  /copilot          # TypeScript/React front-end
  /forecast-api     # FastAPI service
  /agents           # LangGraph agent definitions
  /gateway          # AI gateway config (Portkey/LiteLLM)
  /policies         # OPA/Rego policies
/ml
  /features         # dbt models + Feast definitions
  /models           # LightGBM/TFT training
  /evals            # out-of-regime evaluation harness
/infra
  /terraform        # cloud infra
  /k8s              # Kubernetes manifests
```

## 4. First-week plan

| Day | Activity |
|---|---|
| 1 | Access + local setup + run tests |
| 2 | Read `system-design-document.md` + `decision-log.md` |
| 3 | Walk through the data pipeline (Snowflake → dbt → Feast) |
| 4 | Run the evaluation harness; read an out-of-regime report |
| 5 | Ship a small PR (docs or a test) |

## 5. Key contacts

| Area | Contact |
|---|---|
| Data platform | Data platform team |
| ML models | Data science lead |
| Copilot / agents | ML engineering |
| Security / OPA | Security & compliance |
| FinOps | Platform + finance |

## 6. Useful commands

```bash
make test          # unit + integration
make eval          # out-of-regime evaluation
make lint          # ruff + eslint
make deploy-staging
```