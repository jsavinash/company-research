# Deployment and Environments

## 1. Deployment topology

- **Kubernetes** (Docker) for scoring API + batch workers.
- **Airflow** for pipelines; **Kafka** for streaming; **Spark** for the join; **MLflow** for registry.
- **Prometheus/Grafana** for monitoring + PSI dashboards.

## 2. Environments

| Env | Purpose | Data |
|---|---|---|
| **dev** | Local development | Synthetic data |
| **staging** | Pre-prod integration | Masked data |
| **prod** | Production | Governed data (per-entity) |

## 3. Configuration

- **Config as code:** per-env YAML / Helm.
- **Secrets:** Vault (never in code).
- **Feature flags:** model version, shadow mode.

## 4. CI/CD

```
commit → build → test → eval → staging → shadow → approval → prod (canary)
```

- **CI:** unit + integration + eval.
- **CD:** manual approval; canary.
- **Rollback:** model-versioned.

## 5. Scaling

- **HPA** for scoring API.
- **Spark** autoscaling for batch.
- **Partitioning** by date.

## 6. Monitoring

- **Logs:** structured.
- **Metrics:** latency, error rate, PSI, calibration drift.
- **Alerts:** drift, calibration, data-join failure.