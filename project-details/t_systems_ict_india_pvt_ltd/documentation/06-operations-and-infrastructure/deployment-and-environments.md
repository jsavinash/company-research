# Deployment and Environments

## 1. Deployment topology

- **Kubernetes** cluster (client's or T-Systems India delivery).
- **Components:** TF Serving (model serving), Airflow (batch), Redis (session), MLflow (registry), Prometheus/Grafana (monitoring).
- **CI:** GitLab CI (shadow validation).
- **Cloud:** client's cloud / T-Systems India delivery.

## 2. Environments

| Env | Purpose | Data |
|---|---|---|
| **dev** | Local development | Synthetic data |
| **staging** | Pre-prod integration | Masked/sample data |
| **prod** | Production | Client data (governed) |

## 3. Configuration

- **Config as code:** per-env YAML / Helm values.
- **Secrets:** Vault / K8s secrets (never in code).
- **Feature flags:** model version, ANN config, shadow mode.

## 4. CI/CD

```
commit → build → test → eval → staging → shadow → approval → prod (canary)
```

- **CI:** unit + integration + eval.
- **CD:** manual approval; canary rollout.
- **Rollback:** model-versioned rollback.

## 5. Scaling

- **HPA** on CPU/concurrency.
- **Warm capacity** for peak.
- **Redis** for session signals.

## 5. Monitoring

- **Logs:** structured.
- **Metrics:** latency, error rate, throughput, fallback rate.
- **Alerts:** latency, error rate, no-results, model drift.