# Deployment and Environments

## 1. Deployment topology

- **Kubernetes** (Docker) for inference + training.
- **MONAI** for DICOM/transforms; **MLflow** registry; **Airflow/Kubeflow** pipelines.
- **syngo.via** integration at the reading surface.
- **Prometheus/Grafana** for site-level monitoring.

## 2. Environments

| Env | Purpose | Data |
|---|---|---|
| **dev** | Local development | Synthetic / test DICOM |
| **staging** | Pre-prod integration | De-identified sample DICOM |
| **prod** | Production | Governed DICOM (per-site) |

## 3. Configuration

- **Config as code:** per-env YAML / Helm.
- **Secrets:** Vault (never in code).
- **Feature flags:** model version, calibration set, shadow mode.

## 4. CI/CD

```
commit → build → test → eval → staging → shadow → approval → prod (canary)
```

- **CI:** unit + integration + eval.
- **CD:** manual approval; canary.
- **Rollback:** model-versioned.

## 5. Scaling

- **GPU autoscaling** for inference.
- **Partitioning** by site/date.
- **Batch** for backfill.

## 6. Monitoring

- **Logs:** structured, de-identified.
- **Metrics:** latency, error rate, drift, calibration.
- **Alerts:** drift, calibration, data-quality.