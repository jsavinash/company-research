# Accessibility and i18n / l10n

## 1. Accessibility (a11y)

| Requirement | Target |
|---|---|
| **WCAG** | 2.1 AA |
| **Keyboard** | Full navigation |
| **Screen reader** | ARIA labels, live regions |
| **Contrast** | ≥ 4.5:1 |
| **Streaming** | Announce new tokens politely |

## 2. A11y checklist

- [ ] Keyboard reachable
- [ ] Focus visible
- [ ] Form labels associated
- [ ] Errors announced
- [ ] Color not the only signal
- [ ] Reduced-motion support

## 3. Internationalization (i18n)

| Concern | Choice |
|---|---|
| **Framework** | i18next / react-i18next |
| **Locales** | en-US (initial); es-US (Hispanic market) |
| **Format** | ICU message format |
| **Dates/numbers** | Locale-aware |

## 4. Localization (l10n)

- Strings externalized.
- No hard-coded text.
- Pluralization handled.

## 5. Content guidelines

- Plain language.
- Consistent terminology (see glossary).

## 6. Testing

- Axe accessibility tests.
- Keyboard-only test pass.