# Deployment and Environments

## 1. Deployment topology

- **Single new deployable** (extraction service) behind the existing MyTAXPrepOffice API gateway.
- **Components:** Flask + gunicorn API, Redis queue + workers, PostgreSQL, S3-compatible object storage.
- **Review UI:** server-rendered + small JS layer.

## 2. Environments

| Env | Purpose | Data |
|---|---|---|
| **dev** | Local development | Synthetic documents |
| **staging** | Pre-prod integration | Masked/sample documents |
| **prod** | Production | Real (governed) documents |

## 3. Configuration

- **Config as code:** per-env YAML.
- **Secrets:** environment variables / Vault (never in code).
- **Feature flags:** shadow mode, cloud-OCR fallback.

## 4. CI/CD

```
commit → build → test → eval → staging → approval → prod (shadow → canary)
```

- **CI:** unit + integration + eval.
- **CD:** manual approval for prod; canary rollout.
- **Rollback:** redeploy previous version.

## 5. Scaling

- **Workers:** Redis queue with autoscaling.
- **OCR:** local Tesseract (CPU); cloud fallback (rate-limited).
- **Storage:** S3-compatible, partition by date.

## 6. Monitoring

- **Logs:** structured, PII-redacted.
- **Metrics:** latency, error rate, queue depth, review time.
- **Alerts:** extraction failure, queue backlog, calibration drift.