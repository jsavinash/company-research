# Component Hierarchy and Design System

## 1. Component hierarchy

```
AppShell
├── TopNav
├── Sidebar
├── CopilotPage
│   ├── ChatThread
│   │   ├── MessageBubble
│   │   ├── ScenarioCard
│   │   └── RunIdBadge
│   └── SuggestedPrompts
├── DashboardPage
│   ├── ForecastChart (P10/P50/P90)
│   ├── ExceptionTable
│   └── FreshnessBanner
├── AttributionPage
│   ├── DriverBreakdown
│   └── SignConsistencyBadge
├── RunDetailPage
│   ├── FeatureSnapshot
│   ├── ModelVersion
│   └── Citations
└── AdminPage
    ├── RoleTable
    └── ModelRegistry
```

## 2. Design system

| Token | Example |
|---|---|
| **Color** | Primary blue, warning amber, danger red, success green |
| **Typography** | Inter / system sans |
| **Spacing** | 4/8/12/16/24 |
| **Radius** | 8px |
| **Elevation** | Subtle shadows |

## 3. Component library

| Component | Purpose |
|---|---|
| `Button` | Primary/secondary/danger |
| `Card` | Content container |
| `Table` | Sortable, paginated |
| `Chart` | P10/P50/P90 forecast |
| `Badge` | Run ID, status, sign-consistency |
| `Banner` | Freshness / degraded warnings |
| `Drawer` | Run detail |
| `Modal` | Confirmations |

## 4. Accessibility

- All components keyboard-accessible.
- ARIA labels.
- Focus management.
- Color contrast (WCAG AA).

## 5. Storybook

- Every component has a story.
- Visual regression tests.
- Usage docs.

## 6. Theming

- Light/dark themes.
- Design tokens in CSS variables.

## 7. Related

- `../03_high_level_design_hld/02_ui_and_micro_frontend_topology.md`
- `05_accessibility_and_i18n_l10n.md`