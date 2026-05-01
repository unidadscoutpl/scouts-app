## 2026-05-01 - Missing ARIA labels on Icon-only Buttons
**Learning:** Found a recurring pattern where icon-only buttons (like `🔑` for settings or `✕` for delete actions) lacked `aria-label` attributes, relying sometimes only on a `title` attribute. This is an accessibility gap for screen readers which rely on explicit labels for context.
**Action:** Always verify that buttons containing only icons or emojis have explicit `aria-label`s to ensure robust screen reader support across all interactive components.
