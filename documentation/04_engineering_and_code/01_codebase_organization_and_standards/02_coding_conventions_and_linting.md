# Coding Conventions and Linting

## 1. General

- **Type hints** everywhere (Python), strict TS.
- **No comments unless necessary** — code should be self-documenting.
- **Small functions** (< 50 lines), single responsibility.
- **Explicit** over implicit.

## 2. Python

| Concern | Standard |
|---|---|
| **Formatter** | Black (line length 100) |
| **Linter** | Ruff |
| **Type check** | mypy (strict) |
| **Naming** | snake_case functions/vars; PascalCase classes |
| **Imports** | isort; absolute imports |

```python
def run_forecast(sku_id: str, store_ids: list[str], horizon_weeks: int) -> ForecastResult:
    ...
```

## 3. TypeScript / React

| Concern | Standard |
|---|---|
| **Formatter** | Prettier |
| **Linter** | ESLint (airbnb + typescript) |
| **Naming** | PascalCase components; camelCase functions/vars |
| **Types** | No `any`; explicit return types |
| **Hooks** | Follow rules-of-hooks |

```ts
export function ForecastChart({ run }: { run: ForecastRun }): JSX.Element { ... }
```

## 4. SQL / dbt

- snake_case columns.
- Explicit `SELECT` columns (no `SELECT *` in models).
- Every model has a `schema.yml` with tests.

## 5. IaC (Terraform)

- `tflint` + `terraform fmt`.
- Variables documented.
- No hard-coded secrets.

## 6. Static analysis

| Tool | Scope |
|---|---|
| Ruff | Python lint |
| mypy | Python types |
| ESLint | TS lint |
| Snyk / Dependabot | Dependencies |
| Semgrep | Security |

## 7. Pre-commit hooks

- Formatting (Black, Prettier).
- Linting (Ruff, ESLint).
- Type checks (mypy, tsc).
- Secret scanning (gitleaks).

## 8. Code review checklist

- [ ] Tests added/updated
- [ ] Types correct
- [ ] No secrets
- [ ] Docs updated
- [ ] No anachronisms / scope creep

## 9. Related

- `05_code_quality_and_developer_workflow/02_git_workflow_and_code_review_guide.md`