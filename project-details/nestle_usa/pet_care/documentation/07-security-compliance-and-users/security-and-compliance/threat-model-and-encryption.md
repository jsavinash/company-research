# Threat Model and Encryption

## 1. Scope

Threat model for the GenAI layer: intake, RAG, coaching, vet summary.

## 2. Assets

| Asset | Sensitivity |
|---|---|
| Pet profiles + owner PII | Restricted |
| Plans + coaching | Confidential |
| Model weights & prompts | Internal IP |
| Audit logs | Confidential |

## 3. Trust boundaries

```
Owner → Copilot → Gateway → Agents → Data
                     │          │
                 Entra ID    OPA
                     │          │
                 Purview     Vault
```

## 4. Threats (STRIDE)

| Threat | Example | Mitigation |
|---|---|---|
| **Spoofing** | Stolen credentials | Entra ID MFA |
| **Tampering** | Modified prompts | Signed prompts; validation |
| **Repudiation** | Deny an action | Immutable audit |
| **Information disclosure** | Cross-owner data leak | ABAC; per-owner isolation |
| **Denial of service** | Token flood | Rate limits; quotas |
| **Elevation of privilege** | Access other owners' pets | ABAC |

## 5. AI-specific threats

| Threat | Mitigation |
|---|---|
| **Prompt injection** | Owner text as data; Lakera/NeMo |
| **Hallucination** | Grounding verifier; no LLM diet |
| **Data exfiltration** | Purview DLP; no PII in prompts |
| **Model poisoning** | Signed datasets; lineage |
| **Overclaiming** | NeMo Guardrails; medical routing |

## 6. Encryption

| Layer | In transit | At rest |
|---|---|---|
| Client ↔ server | TLS 1.2+ | — |
| Service ↔ data | TLS | AES-256 |
| Backups | TLS | AES-256 |

## 7. Key management

- Vault / Key Vault.
- Rotation: 90 days.

## 8. Monitoring

- Injection attempts (Lakera).
- DLP alerts (Purview).
- Access anomalies.