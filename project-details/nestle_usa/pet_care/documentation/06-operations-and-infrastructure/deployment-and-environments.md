# Deployment and Environments

## 1. Deployment topology

- **Kubernetes** (Docker) for services.
- **AKS** (Azure Kubernetes Service).
- **vLLM / NIM** for LLM serving.
- **MLflow** registry; **LangSmith** for tracing.
- **Prometheus/Grafana** for monitoring.

## 2. Environments

| Env | Purpose | Data |
|---|---|---|
| **dev** | Local development | Synthetic |
| **staging** | Pre-prod integration | Masked |
| **prod** | Production | Governed |

## 3. Configuration

- **Config as code:** per-env YAML / Helm.
- **Secrets:** Vault (never in code).
- **Feature flags:** model version, shadow mode.

## 4. CI/CD

```
commit → build → test → eval → staging → approval → prod (canary → full)
```

- **CI:** unit + integration + eval.
- **CD:** manual approval; canary.
- **Rollback:** model/prompt-versioned.

## 5. Scaling

- **HPA** for APIs.
- **Queue** for coaching.
- **GPU** autoscaling for LLM serving.

## 6. Monitoring

- **Logs:** structured, PII-redacted.
- **Metrics:** latency, error rate, token cost, cache hit.
- **Alerts:** drift, hallucination, latency.