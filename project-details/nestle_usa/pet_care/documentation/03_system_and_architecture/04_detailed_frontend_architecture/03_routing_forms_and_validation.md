# Routing, Forms, and Validation

## 1. Routing

| Route | Purpose | Guard |
|---|---|---|
| `/copilot` | Chat | Auth |
| `/profile` | Pet profile | Auth |
| `/plan/:planId` | Plan detail | Auth + plan access |
| `/vet/:planId` | Vet summary | Vet role |
| `/admin` | Roles, model registry | Admin |

- **Deep links:** every plan has a shareable URL.
- **Route guards:** auth + permission (OPA).

## 2. Guards

| Guard | Behavior |
|---|---|
| **Auth guard** | Redirect to Entra ID |
| **Permission guard** | 403 + request access |
| **Feature flag guard** | Hide if flag off |

## 3. Forms

| Form | Fields | Validation |
|---|---|---|
| **Intake** | Free text | Non-empty |
| **Profile** | Species, breed, age, weight | Schema |
| **Vet endorsement** | Endorse/override + reason | Required |

- **React Hook Form** + **Zod** schema validation.
- **Inline errors.**

## 4. Validation (Zod)

```ts
const profileSchema = z.object({
  species: z.enum(["dog", "cat"]),
  breed: z.string(),
  age_years: z.number().min(0),
});
```

## 5. Deep linking

- `/plans/:planId` → plan detail.
- Shareable to Teams/email.

## 6. Error boundaries

- Route-level error boundaries.
- Fallback UI.