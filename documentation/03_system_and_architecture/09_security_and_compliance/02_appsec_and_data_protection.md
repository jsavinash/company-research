# AppSec and Data Protection

## 1. Application security

| Concern | Control |
|---|---|
| **XSS** | Output encoding, CSP |
| **CSRF** | SameSite cookies, CSRF tokens |
| **CORS** | Strict allowlist |
| **Clickjacking** | X-Frame-Options / CSP frame-ancestors |
| **SQL injection** | Parameterized queries |
| **SSRF** | Egress filtering |

## 2. Content Security Policy (CSP)

```
default-src 'self';
script-src 'self';
style-src 'self' 'unsafe-inline';
img-src 'self' data:;
connect-src 'self' https://api.nestle-demand-sensing.internal;
```

## 3. Encryption

| Layer | In transit | At rest |
|---|---|---|
| **Browser ↔ server** | TLS 1.2+ | — |
| **Service ↔ service** | mTLS | — |
| **Data** | TLS | AES-256 |
| **Backups** | TLS | AES-256 |

## 4. Key management

- **HashiCorp Vault / Azure Key Vault.**
- **Rotation:** 90 days (secrets), 30 days (tokens).
- **HSM-backed** for critical keys.

## 5. Secrets

- No secrets in code.
- Injected via Vault CSI driver.
- Audited.

## 6. Input validation

- Schema validation at boundaries.
- Output encoding.

## 7. Dependency security

- SCA scanning (SAST/DAST).
- Pin versions.
- Regular updates.

## 8. Logging

- No PII / secrets in logs.
- Structured logs.
- Centralized (Datadog).

## 9. Related

- `01_authn_authz_and_identity.md`
- `03_data_privacy_and_governance.md`
- `Nestle-USA-DemandSensing-AIArchitect-UseCase/07-security-compliance-and-users/security-and-compliance/threat-model-and-encryption.md`