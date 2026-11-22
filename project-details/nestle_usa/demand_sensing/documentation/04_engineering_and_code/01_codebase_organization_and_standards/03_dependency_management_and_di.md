# Dependency Management and Dependency Injection

## 1. Dependency management

### Python

| Tool | Use |
|---|---|
| **uv / pipenv** | Virtual env + lockfile |
| **pyproject.toml** | Dependencies + metadata |
| **pip-tools** | Pinning (if not using uv) |

- Pin exact versions in lockfile.
- Separate dev/prod dependencies.
- Renovate/Dependabot for updates.

### TypeScript

| Tool | Use |
|---|---|
| **pnpm** | Package manager + workspace |
| **pnpm-lock.yaml** | Lockfile |
| **npm audit** | Vulnerability scan |

### Infrastructure

- Terraform providers pinned.
- Helm charts versioned.

## 2. Dependency Injection (DI) / IoC

- **FastAPI:** `Depends()` for DI.
- **Python:** constructor injection; avoid globals.
- **TypeScript:** React Context + hooks; avoid singletons.

```python
class ForecastService:
    def __init__(self, repo: ForecastRepository, model: ForecastModel):
        self.repo = repo
        self.model = model
```

## 3. IoC container

- **FastAPI:** built-in DI container.
- **Service registration:** central `core/container.py`.
- **Lifespan:** resources managed via lifespan events.

## 4. Third-party package rules

- **Allowlist** of approved packages.
- **Security scan** (SAST/SCA).
- **Pin versions.**
- **Avoid heavy dependencies** where stdlib suffices.
- **License check.**

## 5. Version strategy

- **SemVer** for internal packages.
- **Lockfiles** committed.
- **Renovate** PRs for updates (auto-merge patch).

## 6. Dependency boundaries

- **apps** → shared, ml.
- **ml** → features, data.
- **No** app-to-app imports.
- **No** circular dependencies.

## 7. Secrets & config

- Config via env vars / Vault.
- No secrets in code or dependency manifests.

## 8. Related

- `01_repository_and_folder_structure.md`
- `../05_code_quality_and_developer_workflow/02_git_workflow_and_code_review_guide.md`