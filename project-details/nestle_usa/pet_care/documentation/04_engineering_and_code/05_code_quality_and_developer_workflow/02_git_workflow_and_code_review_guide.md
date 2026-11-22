# Git Workflow and Code Review Guide

## 1. Branching strategy

| Branch | Purpose |
|---|---|
| **main** | Production-ready |
| **develop** | Integration |
| **feature/** | Features |
| **fix/** | Bug fixes |
| **release/** | Release prep |

## 2. Commit conventions

```
<type>(<scope>): <subject>

<body>
```

| Type | Use |
|---|---|
| feat | New feature |
| fix | Bug fix |
| docs | Documentation |
| refactor | Refactor |
| test | Tests |

## 3. Pull requests

- **PR template:** summary, changes, tests, eval, checklist.
- **Small PRs** (< 400 lines).
- **Required reviewers:** 1 (2 for sensitive).
- **CI must pass.**

## 4. Code review checklist

- [ ] Tests / eval added
- [ ] Types correct
- [ ] No PII / secrets
- [ ] Docs updated
- [ ] Safety boundaries intact

## 5. Merge rules

- **Squash and merge** to main.
- **Delete branch** after merge.

## 6. Release

- **Tag** versions (SemVer).
- **Changelog** generated.

## 7. Protected branches

- **main:** require PR, status checks, review.
- **develop:** require PR, status checks.