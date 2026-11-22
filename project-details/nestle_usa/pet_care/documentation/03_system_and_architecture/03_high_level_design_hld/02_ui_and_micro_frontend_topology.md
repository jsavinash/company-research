# UI and Micro-Frontend Topology

## 1. Front-end architecture

| Concern | Choice |
|---|---|
| **Framework** | React + TypeScript |
| **Build** | Vite / module federation |
| **Routing** | React Router (deep links) |
| **State** | Redux Toolkit / Zustand + React Query |
| **Styling** | Tailwind / CSS Modules |

## 2. Micro-frontend topology

```
Shell (host)
├── Copilot MFE (chat, streaming)
├── Profile MFE (pet profile)
├── Plan MFE (recommendation + rationale)
└── Vet Summary MFE (endorse/override)
```

## 3. Contracts

| Contract | Purpose |
|---|---|
| **Auth context** | Shared Entra ID token |
| **Navigation** | Deep-link routing |
| **Design tokens** | Consistent UI |
| **Event bus** | Cross-MFE communication |

## 4. State boundaries

| State | Location |
|---|---|
| **Server state** | React Query |
| **UI state** | Zustand |
| **Auth** | Context + Entra ID |
| **Feature flags** | LaunchDarkly / custom |

## 5. Deployment

- Each MFE independently deployable.
- Shared shell versioned.
- Canary per MFE.

## 6. Performance

- Code splitting per MFE.
- Lazy load routes.
- Bundle budgets (see `../04_detailed_frontend_architecture/06_performance_bundling_and_web_vitals.md`).