# Threat Model and Encryption

## 1. Scope

Threat model for the product-discovery platform, covering client data, event streams, models, and serving.

## 2. Assets

| Asset | Sensitivity |
|---|---|
| Client event stream (clicks, carts, orders) | Confidential (client-owned) |
| Catalog data | Confidential |
| User/session data | Restricted (PII-adjacent) |
| Model weights & configs | Client IP |

## 3. Trust boundaries

```
Client storefront → Event stream → Features → Retrieve → Rank → Serve
                         │            │          │         │
                    Kafka        Airflow      FAISS    TF Serving
```

## 4. Threats (STRIDE)

| Threat | Example | Mitigation |
|---|---|---|
| **Spoofing** | Stolen API key | API keys, mTLS, rotation |
| **Tampering** | Modified events | Schema validation, checksums |
| **Repudiation** | Deny an action | Immutable interaction log |
| **Information disclosure** | Cross-client data leak | Single-client isolation; RBAC |
| **Denial of service** | Request flood | Rate limits, HPA |
| **Elevation of privilege** | Access other clients' data | Tenant isolation |

## 5. AI-specific threats

| Threat | Mitigation |
|---|---|
| **Popularity/position bias** | Impression+position logging; bias controls |
| **Data leakage (cross-client)** | Single-client isolation; no cross-client training |
| **Model poisoning** | Signed datasets; lineage |
| **PII in logs** | Redaction; consent/retention |

## 6. Encryption

| Layer | In transit | At rest |
|---|---|---|
| Client ↔ API | TLS 1.2+ | — |
| Service ↔ data | TLS | AES-256 |
| Backups | TLS | AES-256 |

## 7. Key management

- Vault / K8s secrets; rotation policy.
- No secrets in code or logs.

## 8. Monitoring

- Access anomaly detection.
- DLP alerts.
- Audit log review.