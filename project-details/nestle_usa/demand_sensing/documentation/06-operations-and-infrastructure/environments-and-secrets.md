# Environments and Secrets

## 1. Environment matrix

| Env | Purpose | Data | Access |
|---|---|---|---|
| **dev** | Local development | Synthetic / masked | Engineers |
| **ci** | Automated testing | Synthetic | CI service account |
| **staging** | Pre-prod integration | Masked / sample | QA + engineers |
| **prod** | Production | Real (governed) | SRE + on-call |

## 2. Promotion rules

```
dev → ci → staging → prod
```

- Promotion requires: tests green, eval report, approval.
- **Prod** changes require change-approval (CAB) + on-call sign-off.
- Hotfixes follow the same path but with expedited approval.

## 3. Secret management

| Secret type | Store | Rotation |
|---|---|---|
| DB credentials | HashiCorp Vault | 90 days |
| API keys (models) | Vault + gateway | 90 days |
| Entra ID client secrets | Vault / Key Vault | 90 days |
| TLS certs | Vault / cert-manager | Auto |
| Snowflake/Databricks tokens | Vault | 30 days |

**Rules:**
- No secrets in code, env files, or logs.
- Secrets injected at runtime via Vault agent / CSI driver.
- Access audited.

## 4. Configuration

- **Config as code:** per-env YAML/Helm values.
- **Feature flags:** for gradual rollout (e.g., copilot v2).
- **Model registry:** MLflow tracks model versions per env.

## 5. Access control

- **SSO:** Entra ID.
- **RBAC:** platform roles (viewer, engineer, SRE, admin).
- **Break-glass:** time-bound, audited emergency access.

## 6. Compliance

- Data residency: US regions.
- Audit logs retained per policy.
- Secrets never leave the vault boundary.