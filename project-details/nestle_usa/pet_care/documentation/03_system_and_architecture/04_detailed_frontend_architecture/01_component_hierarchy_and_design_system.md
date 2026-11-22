# Component Hierarchy and Design System

## 1. Component hierarchy

```
AppShell
├── TopNav
├── CopilotPage
│   ├── ChatThread
│   │   ├── MessageBubble
│   │   ├── PlanCard
│   │   └── CitationBadge
│   └── SuggestedPrompts
├── ProfilePage
│   ├── PetProfileForm
│   └── CompletenessMeter
├── PlanPage
│   ├── FormulaCard
│   ├── PortionCard
│   └── AdequacyBadge
└── VetSummaryPage
    ├── SummaryView
    └── EndorseOverride
```

## 2. Design system

| Token | Example |
|---|---|
| **Color** | Primary, warning, danger, success |
| **Typography** | Inter / system sans |
| **Spacing** | 4/8/12/16/24 |
| **Radius** | 8px |

## 3. Component library

| Component | Purpose |
|---|---|
| `Button` | Primary/secondary |
| `Card` | Content container |
| `Chat` | Streaming messages |
| `Badge` | Adequacy, citation |
| `Meter` | Profile completeness |
| `Drawer` | Plan detail |

## 4. Accessibility

- Keyboard-accessible.
- ARIA labels.
- WCAG 2.1 AA.

## 5. Storybook

- Every component has a story.
- Visual regression tests.