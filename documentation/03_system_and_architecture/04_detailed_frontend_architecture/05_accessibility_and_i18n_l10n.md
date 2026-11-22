# Accessibility and i18n / l10n

## 1. Accessibility (a11y)

| Requirement | Target |
|---|---|
| **WCAG** | 2.1 AA |
| **Keyboard** | Full navigation |
| **Screen reader** | ARIA labels, live regions |
| **Contrast** | ≥ 4.5:1 |
| **Focus** | Visible, managed on route change |
| **Charts** | Text alternatives (P10/P50/P90) |

## 2. A11y checklist

- [ ] Every interactive element reachable by keyboard
- [ ] Focus visible
- [ ] Form labels associated
- [ ] Error messages announced
- [ ] Charts described in text
- [ ] Color not the only signal
- [ ] Reduced-motion support

## 3. Internationalization (i18n)

| Concern | Choice |
|---|---|
| **Framework** | i18next / react-i18next |
| **Locales** | en-US (initial); extensible |
| **Format** | ICU message format |
| **Dates/numbers** | Locale-aware |

## 4. Localization (l10n)

- **Strings** externalized to resource files.
- **No hard-coded text** in components.
- **Pluralization** handled.
- **RTL** support (future).

## 5. Content guidelines

- Plain language.
- Avoid idioms.
- Consistent terminology (see glossary).

## 6. Testing

- Axe accessibility tests.
- Keyboard-only test pass.
- Screen-reader spot checks.

## 7. Related

- `01_component_hierarchy_and_design_system.md`