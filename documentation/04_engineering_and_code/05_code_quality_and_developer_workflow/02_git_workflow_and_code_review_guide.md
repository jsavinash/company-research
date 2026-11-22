# Git Workflow and Code Review Guide

## 1. Branching strategy

| Branch | Purpose |
|---|---|
| **main** | Production-ready |
| **develop** | Integration |
| **feature/*` | Features |
| **fix/*` | Bug fixes |
| **release/*` | Release prep |
| **hotfix/*` | Production fixes |

- **Short-lived** branches (< 3 days).
- **Rebase** on main before merge.
- **Squash** merge to main.

## 2. Commit conventions

Conventional Commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

| Type | Use |
|---|---|
| feat | New feature |
| fix | Bug fix |
| docs | Documentation |
| refactor | Refactor |
| test | Tests |
| chore | Maintenance |

## 3. Pull requests

- **PR template:** summary, changes, tests, screenshots, checklist.
- **Small PRs** (< 400 lines).
- **Required reviewers:** 1 (2 for sensitive).
- **CI must pass.**

## 4. Code review checklist

- [ ] Tests added/updated
- [ ] Types correct
- [ ] No secrets
- [ ] Docs updated
- [ ] No scope creep / anachronisms
- [ ] Security implications considered

## 5. Merge rules

- **Squash and merge** to main.
- **Delete branch** after merge.
- **Linear history** preferred.

## 6. Release

- **Tag** versions (SemVer).
- **Changelog** generated.
- **Release notes** curated.

## 7. Protected branches

- **main:** require PR, status checks, review.
- **develop:** require PR, status checks.

## 8. Related

- `01_unit_and_integration_test_patterns.md`
- `../01_codebase_organization_and_standards/02_coding_conventions_and_linting.md`