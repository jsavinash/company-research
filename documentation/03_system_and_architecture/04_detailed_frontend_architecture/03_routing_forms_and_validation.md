# Routing, Forms, and Validation

## 1. Routing

| Route | Purpose | Guard |
|---|---|---|
| `/copilot` | Chat | Auth |
| `/dashboard` | Forecast review | Auth |
| `/attribution/:runId` | Driver breakdown | Auth + run access |
| `/runs/:runId` | Run detail / audit | Auth + run access |
| `/admin` | Roles, model registry | Admin |

- **Deep links:** every run has a shareable URL.
- **Route guards:** auth + permission (OPA).
- **404 / 403 pages:** clear messaging.

## 2. Guards

| Guard | Behavior |
|---|---|
| **Auth guard** | Redirect to Entra ID login |
| **Permission guard** | Show 403 + request access |
| **Feature flag guard** | Hide if flag off |

## 3. Forms

| Form | Fields | Validation |
|---|---|---|
| **Scenario** | Natural-language query | Non-empty, length |
| **Access request** | Banner/DMA + justification | Required fields |
| **Admin** | Role, scope | Schema |

- **React Hook Form** + **Zod** schema validation.
- **Inline errors.**
- **Optimistic UI** where safe.

## 4. Validation (Zod)

```ts
const scenarioSchema = z.object({
  query: z.string().min(5).max(500),
});
```

## 5. Deep linking

- `/runs/FR-2026-11-22-0142` → run detail.
- Shareable to Teams/email.
- Preserves context (banners/DMAs).

## 6. Error boundaries

- Route-level error boundaries.
- Fallback UI.

## 7. Accessibility

- Focus management on route change.
- Announce route changes to screen readers.

## 8. Related

- `01_component_hierarchy_and_design_system.md`
- `../07_api_and_network_communication/01_api_contracts_and_versioning.md`