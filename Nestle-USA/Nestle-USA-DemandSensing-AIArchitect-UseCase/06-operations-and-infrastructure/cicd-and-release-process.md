# CI/CD and Release Process

## 1. Pipeline stages

```
commit → build → test → eval → staging → approval → prod (canary → full)
```

| Stage | Actions | Gate |
|---|---|---|
| **Build** | Compile, lint, unit tests | All pass |
| **Eval** | Out-of-regime eval, adversarial suite | No regression |
| **Staging** | Deploy, integration + e2e tests | All pass |
| **Approval** | CAB + on-call sign-off | Approved |
| **Prod** | Canary (5%) → full | Metrics healthy |

## 2. Tooling

| Concern | Tool |
|---|---|
| CI | GitLab CI / Azure DevOps |
| IaC | Terraform |
| Packaging | Docker, Helm |
| CD | Argo CD / Flux |
| Artifacts | Container registry + MLflow |
| Secrets | Vault (CSI driver) |

## 3. Release strategy

- **Canary:** 5% → 25% → 50% → 100%, with automated rollback on error-rate/latency breach.
- **Blue-green:** for major versions.
- **Feature flags:** for gradual feature rollout.
- **Rollback:** one-click to previous version; DB migrations backward-compatible.

## 4. Quality gates

- Unit + integration tests pass.
- Eval report attached (out-of-regime WMAPE, calibration, bias).
- Adversarial suite green.
- Security scan (SAST/DAST) clean.
- Change approval recorded.

## 5. Release notes

- Auto-generated from PR labels; curated highlights in `07-security-compliance-and-users/end-user-and-support/release-notes-changelog.md`.

## 6. Environments

See `environments-and-secrets.md`.

## 7. Emergency changes

- Hotfix path with expedited approval.
- Post-incident review required.