# Authentication, Authorization, and Identity

## 1. Authentication

| Concern | Choice |
|---|---|
| **Enterprise SSO** | Microsoft Entra ID (OIDC) |
| **Partner access** | Okta |
| **Cloud IAM** | AWS IAM |
| **MFA** | Enforced |

## 2. Authorization (ABAC)

| Component | Choice |
|---|---|
| **Policy engine** | OPA |
| **Model** | Attribute-Based Access Control |
| **Attributes** | user role, team; resource (pet, plan); action |

Policy: `allow(user, resource, action)` iff attributes match.

## 4. Identity flow

```
User → Entra ID (OIDC) → token → Copilot BFF → OPA (policy) → resource
```

## 5. Roles

| Role | Scope |
|---|---|
| Owner | Own pets |
| Vet | Referred pets |
| Admin | All |
| Auditor | Read-only |

## 6. Token management

- **Access token** (short-lived).
- **Refresh token** (rotated).
- **Audience** scoping.

## 7. Service-to-service auth

- **mTLS** between services.
- **OAuth2 client credentials** for service accounts.

## 8. Auditing

- Every auth decision logged.
- Quarterly access reviews.