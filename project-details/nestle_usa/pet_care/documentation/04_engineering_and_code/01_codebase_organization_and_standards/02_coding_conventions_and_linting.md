# Coding Conventions and Linting

## 1. Python

| Concern | Standard |
|---|---|
| **Formatter** | Black (line 100) |
| **Linter** | Ruff |
| **Type check** | mypy (strict) |
| **Naming** | snake_case / PascalCase |

## 2. TypeScript / React

| Concern | Standard |
|---|---|
| **Formatter** | Prettier |
| **Linter** | ESLint (airbnb + typescript) |
| **Types** | No `any`; explicit returns |

## 3. LLM-specific

- **Structured outputs** (JSON schema / function calling).
- **No free-text parsing** of LLM outputs.
- **Prompt versioning** in the registry.
- **Eval required** for prompt/model changes.

## 4. Static analysis

| Tool | Scope |
|---|---|
| Ruff | Python lint |
| mypy | Python types |
| ESLint | TS lint |
| Semgrep | Security |

## 5. Pre-commit hooks

- Formatting (Black, Prettier).
- Linting (Ruff, ESLint).
- Secret scanning (gitleaks).

## 6. Review checklist

- [ ] Tests / eval added
- [ ] No PII
- [ ] No secrets
- [ ] Docs updated
- [ ] Safety boundaries intact