# Threat Model and Encryption

## 1. Scope

Threat model for the Agentic GLP-1 Demand Sensing & Scenario Copilot, covering the AI gateway, agents, data layer, and copilot.

## 2. Assets

| Asset | Sensitivity |
|---|---|
| Retailer sell-out / shipment data | Confidential (contractual) |
| Household panel data | Restricted (privacy) |
| GLP-1 prescription prevalence | Confidential |
| Forecast / attribution outputs | Internal |
| Model weights & prompts | Internal IP |
| Credentials & secrets | Critical |

## 3. Trust boundaries

```
User → Copilot → AI Gateway → Agents → Data Layer
                │              │           │
              Entra ID        OPA        Vault
                │              │           │
             Purview         Audit      Secrets
```

## 4. Threats (STRIDE)

| Threat | Example | Mitigation |
|---|---|---|
| **Spoofing** | Stolen credentials | Entra ID MFA, conditional access |
| **Tampering** | Tampered prompts / data | Signed prompts, input validation, OPA |
| **Repudiation** | Deny an action | Immutable audit log |
| **Information disclosure** | Cross-retailer data leak | OPA/ABAC, Purview DLP, row-level security |
| **Denial of service** | Token flood / cost exhaustion | Rate limiting, quotas, semantic cache |
| **Elevation of privilege** | Access another banner's data | ABAC, least privilege, OPA policy |

## 5. AI-specific threats

| Threat | Mitigation |
|---|---|
| **Prompt injection** (owner/retailer text) | Treat external text as data; Lakera/NeMo input scanning; system prompt is sole instruction source |
| **Hallucination** | LLM never forecasts; grounding verifier; audit sample |
| **Data exfiltration via prompts** | Purview DLP; no PII in prompts; redaction |
| **Model poisoning** | Signed datasets; lineage; access control |
| **Overclaiming / scope creep** | NeMo Guardrails; "nutrition/price, not diagnosis" boundaries |

## 6. Encryption

| Layer | In transit | At rest |
|---|---|---|
| User ↔ Copilot | TLS 1.2+ | — |
| Copilot ↔ Gateway | mTLS | — |
| Gateway ↔ Model | TLS | — |
| Services ↔ Data | TLS + private endpoints | AES-256 (Snowflake/Databricks/Blob) |
| Secrets | — | Vault (encrypted) |
| Backups | TLS | AES-256 |

## 7. Key management

- HashiCorp Vault / Azure Key Vault.
- Rotation: 90 days (secrets), 30 days (tokens).
- HSM-backed for critical keys.

## 8. Monitoring

- Anomalous access patterns (Datadog + SIEM).
- Prompt-injection attempts (Lakera logs).
- DLP violations (Purview).
- Audit log review.