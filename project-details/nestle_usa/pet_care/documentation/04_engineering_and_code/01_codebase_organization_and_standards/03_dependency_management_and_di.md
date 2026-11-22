# Dependency Management and DI

## 1. Python

| Tool | Use |
|---|---|
| **uv / pipenv** | Virtual env + lockfile |
| **pyproject.toml** | Dependencies |
| **pip-tools** | Pinning |

## 2. TypeScript

| Tool | Use |
|---|---|
| **pnpm** | Package manager + workspace |
| **pnpm-lock.yaml** | Lockfile |

## 3. Dependency Injection

- **FastAPI:** `Depends()` for DI.
- **Constructor injection** for services.
- **No globals / singletons** for stateful deps.

```python
class CoachingService:
    def __init__(self, retriever: Retriever, generator: Generator):
        self.retriever = retriever
        self.generator = generator
```

## 4. Third-party package rules

- **Allowlist** of approved packages.
- **Security scan** (SCA).
- **Pin versions.**
- **License check.**

## 5. Version strategy

- **SemVer** for internal packages.
- **Lockfiles** committed.
- **Renovate** for updates.

## 6. Secrets & config

- Config via env vars / Vault.
- No secrets in code or manifests.