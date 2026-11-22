# Deployment and Environments

## 1. Deployment topology

- **Single new deployable** (triage service) behind the existing Nala CDS API.
- **Components:** Flask + gunicorn API, Redis queue + workers, PostgreSQL, S3-compatible object storage.
- **Review UI:** server-rendered + small JS layer.
- **Cloud:** AWS ap-southeast-1 (matches existing deployment).

## 2. Environments

| Env | Purpose | Data |
|---|---|---|
| **dev** | Local development | Synthetic / test VCFs |
| **staging** | Pre-prod integration | De-identified sample VCFs |
| **prod** | Production | De-identified (governed) VCFs |

## 3. Configuration

- **Config as code:** per-env YAML.
- **Secrets:** environment variables / Vault (never in code).
- **Feature flags:** shadow mode, model version pin.

## 4. CI/CD

```
commit → build → test → eval → staging → approval → prod (shadow → canary)
```

- **CI:** unit + integration + eval.
- **CD:** manual approval for prod; canary rollout.
- **Rollback:** redeploy previous version.

## 5. Scaling

- **Workers:** Redis queue with autoscaling.
- **Annotation:** parallel per variant.
- **Storage:** S3-compatible, partition by run.

## 6. Monitoring

- **Logs:** structured, de-identified.
- **Metrics:** latency, error rate, queue depth, curator time.
- **Alerts:** triage failure, queue backlog, calibration drift, ancestry gap regression.