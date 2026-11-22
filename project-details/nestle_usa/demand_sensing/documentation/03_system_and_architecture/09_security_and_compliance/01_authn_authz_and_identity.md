# Authentication, Authorization, and Identity

## 1. Authentication

| Concern | Choice |
|---|---|
| **Enterprise SSO** | Microsoft Entra ID (OIDC) |
| **Partner access** | Okta |
| **Cloud IAM** | AWS IAM |
| **MFA** | Enforced (conditional access) |

## 2. Authorization (ABAC)

| Component | Choice |
|---|---|
| **Policy engine** | OPA (Open Policy Agent) |
| **Model** | Attribute-Based Access Control |
| **Attributes** | user role, team, assigned banners/DMAs; resource sensitivity; action |

Policy: `allow(user, resource, action)` iff attributes match.

## 3. Identity flow

```
User → Entra ID (OIDC) → token → Copilot BFF → OPA (policy) → resource
```

## 4. Roles

| Role | Scope |
|---|---|
| Viewer | Read-only |
| Planner | Own banners/DMAs |
| RGM Analyst | Own categories |
| Data Steward | All (governed) |
| Admin | All |

## 5. Token management

- **Access token** (short-lived).
- **Refresh token** (rotated).
- **Audience** scoping.

## 6. Session

- **HttpOnly, Secure, SameSite** cookies.
- **Idle timeout.**
- **Re-auth** for sensitive actions.

## 7. Service-to-service auth

- **mTLS** between services.
- **OAuth2 client credentials** for service accounts.

## 8. Auditing

- Every auth decision logged.
- Quarterly access reviews.

## 9. Related

- `02_appsec_and_data_protection.md`
- `03_data_privacy_and_governance.md`
- `Nestle-USA-DemandSensing-AIArchitect-UseCase/03-system-and-architecture/architecture-decision-records/002-authentication-strategy.md`