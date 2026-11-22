# Permissions and Plan Tiers

## 1. Roles

| Role | Access | Scope |
|---|---|---|
| **Viewer** | Read-only dashboards | Assigned banners/DMAs |
| **Planner** | Copilot + dashboards + export | Owned banners/DMAs |
| **RGM Analyst** | Attribution + scenarios | Owned categories |
| **Data Steward** | Data quality + lineage + policy | All (governed) |
| **Admin** | User/role management, model registry | All |
| **Auditor** | Read-only audit log | All |

## 2. Permission model (ABAC)

Attributes:
- **User:** role, team, assigned banners/DMAs.
- **Resource:** banner, DMA, category, sensitivity.
- **Action:** read, query, export, admin.
- **Context:** purpose, time.

Policy (OPA): `allow(user, resource, action)` iff attributes match.

## 3. Entitlement logic

```
can_access(user, banner) =
  user.role in {Admin, Data Steward} OR
  banner in user.assigned_banners OR
  dma in user.assigned_dmas
```

- **Row-level:** planner sees only their banners.
- **Column-level:** sensitive columns (e.g., panel PII) masked/aggregated.

## 4. Plan tiers / quotas

| Tier | Quota | Features |
|---|---|---|
| **Standard (Planner)** | e.g., 100 scenarios/day | Copilot, dashboards, export |
| **Power (RGM/Analyst)** | e.g., 500 scenarios/day | + batch, attribution API |
| **Enterprise (Admin)** | Unlimited | + admin, audit export |

> **Note:** tiers are illustrative; align to Nestlé licensing.

## 5. Rate limits & quotas

| Scope | Limit |
|---|---|
| Scenarios per user | Per tier |
| API calls per minute | Per gateway policy |
| Token budget per business unit | Chargeback |

## 6. Access request flow

1. User requests access to a banner/DMA.
2. OPA workflow routes to data owner.
3. Approval → role/assignment updated.
4. Audit logged.

## 7. Auditing

- Every access decision logged (OPA).
- Every data access audited.
- Quarterly access reviews.

## 8. Segregation of duties

- **Requester** ≠ **Approver** for sensitive data.
- **Admin** actions logged and reviewed.