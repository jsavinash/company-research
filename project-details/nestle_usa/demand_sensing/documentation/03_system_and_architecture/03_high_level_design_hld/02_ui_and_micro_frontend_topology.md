# UI and Micro-Frontend Topology

## 1. Front-end architecture

| Concern | Choice |
|---|---|
| **Framework** | React + TypeScript |
| **Build** | Vite / Webpack (module federation for micro-frontends) |
| **Routing** | React Router (deep links) |
| **State** | Redux Toolkit / Zustand + React Query (server state) |
| **Styling** | Tailwind / CSS Modules + design system |
| **Testing** | Jest + React Testing Library + Playwright (E2E) |

## 2. Micro-frontend topology

```
Shell (host)
├── Copilot MFE (chat, streaming)
├── Dashboard MFE (forecast review)
├── Attribution MFE (driver breakdown)
├── Run Detail MFE (audit)
└── Admin MFE (permissions, model registry)
```

- **Module Federation** for runtime composition.
- **Shared design system** package.
- **Independent deploy** per MFE.

## 3. Micro-frontend contracts

| Contract | Purpose |
|---|---|
| **Auth context** | Shared Entra ID token |
| **Navigation** | Deep-link routing |
| **Design tokens** | Consistent UI |
| **Event bus** | Cross-MFE communication |

## 4. State boundaries

| State | Location |
|---|---|
| **Server state** | React Query (cached) |
| **UI state** | Local / Zustand |
| **Auth** | Context + Entra ID |
| **Feature flags** | LaunchDarkly / custom |

## 5. Deployment

- Each MFE independently deployable.
- Shared shell versioned.
- Canary per MFE.

## 6. Performance

- Code splitting per MFE.
- Lazy load routes.
- Bundle budgets (see `04_detailed_frontend_architecture/06_performance_bundling_and_web_vitals.md`).

## 7. Accessibility

- Shared a11y primitives.
- WCAG 2.1 AA.

## 8. Related

- `04_detailed_frontend_architecture/`
- `02_rendering_and_delivery_strategy.md`