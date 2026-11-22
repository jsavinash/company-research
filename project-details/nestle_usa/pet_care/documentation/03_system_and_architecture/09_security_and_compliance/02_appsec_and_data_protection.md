# AppSec and Data Protection

## 1. Application security

| Concern | Control |
|---|---|
| **XSS** | Output encoding, CSP |
| **CSRF** | SameSite cookies, CSRF tokens |
| **CORS** | Strict allowlist |
| **Clickjacking** | X-Frame-Options / CSP frame-ancestors |
| **SQL injection** | Parameterized queries |

## 2. Content Security Policy (CSP)

```
default-src 'self';
script-src 'self';
style-src 'self' 'unsafe-inline';
img-src 'self' data:;
connect-src 'self' https://api.purina.internal;
```

## 4. Encryption

| Layer | In transit | At rest |
|---|---|---|
| Browser ↔ server | TLS 1.2+ | — |
| Service ↔ data | TLS | AES-256 |
| Backups | TLS | AES-256 |

## 5. Key management

- Vault / Key Vault.
- Rotation: 90 days.
- No secrets in code or logs.

## 6. Input validation

- Schema validation at boundaries.
- Output encoding.

## 7. Dependency security

- SCA scanning (SAST/DAST).
- Pin versions.
- Regular updates.

## 8. AI-specific protections

- **Prompt-injection defense:** Lakera/NeMo.
- **PII redaction:** Purview.
- **No PII in prompts/logs.**
- **Guardrails:** NeMo.

## 9. Monitoring

- Anomalous access patterns.
- DLP alerts.
- Audit log review.