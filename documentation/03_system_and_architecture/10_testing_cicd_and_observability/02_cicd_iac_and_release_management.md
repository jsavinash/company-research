# CI/CD, IaC, and Release Management

## 1. Pipeline

```
commit → build → test → eval → staging → approval → prod (canary → full)
```

| Stage | Actions | Gate |
|---|---|---|
| **Build** | Compile, lint, unit | All pass |
| **Eval** | Out-of-regime eval, adversarial | No regression |
| **Staging** | Deploy, integration + e2e | All pass |
| **Approval** | CAB + on-call | Approved |
| **Prod** | Canary → full | Metrics healthy |

## 2. Tooling

| Concern | Tool |
|---|---|
| **CI** | GitLab CI / Azure DevOps |
| **IaC** | Terraform |
| **Packaging** | Docker, Helm |
| **CD** | Argo CD / Flux |
| **Artifacts** | Container registry + MLflow |
| **Secrets** | Vault |

## 3. Release strategy

- **Canary:** 5% → 25% → 50% → 100%.
- **Blue-green:** major versions.
- **Feature flags:** gradual rollout.
- **Rollback:** one-click; backward-compatible migrations.

## 4. IaC

- **Terraform** for cloud infra.
- **Helm** for Kubernetes.
- **Policy as code** (OPA conftest).
- **Drift detection.**

## 5. Versioning

- **SemVer** for services.
- **Git tags** for releases.
- **Model versions** in MLflow.

## 6. Quality gates

- Tests pass.
- Eval report attached.
- Adversarial suite green.
- Security scan clean.
- Change approval.

## 7. Emergency changes

- Hotfix path with expedited approval.
- Post-incident review.

## 8. Related

- `01_testing_strategy_and_ab_experiments.md`
- `Nestle-USA-DemandSensing-AIArchitect-UseCase/06-operations-and-infrastructure/cicd-and-release-process.md`