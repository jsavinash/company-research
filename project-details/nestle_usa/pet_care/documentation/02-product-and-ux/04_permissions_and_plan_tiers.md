# Permissions and Plan Tiers

## 1. Roles

| Role | Access | Scope |
|---|---|---|
| **Owner** | Copilot + profile | Own pets |
| **Vet** | Vet summary + endorse/override | Referred pets |
| **Nutrition scientist** | KB + eval | All (governed) |
| **Admin** | User/role management | All |
| **Auditor** | Read-only audit | All |

## 2. Permission model (ABAC)

Attributes:
- **User:** role, team.
- **Resource:** pet profile, plan, vet summary.
- **Action:** read, query, endorse.
- **Context:** purpose.

## 3. Entitlement logic

```
can_access(user, pet) =
  user.role in {Admin, Nutrition scientist} OR
  pet.owner_id == user.id OR
  vet referral exists
```

## 4. Plan tiers / quotas

| Tier | Quota | Features |
|---|---|---|
| **Standard (Owner)** | e.g., 50 chats/day | Copilot, coaching |
| **Vet** | e.g., 200 summaries/day | Vet summary, endorse |
| **Enterprise** | Unlimited | Admin, audit |

## 5. Rate limits & quotas

| Scope | Limit |
|---|---|
| Chats per user | Per tier |
| API calls per minute | Gateway policy |
| Token budget per business unit | Chargeback |

## 6. Auditing

- Every access decision logged (OPA).
- Every coaching session logged.
- Quarterly access reviews.