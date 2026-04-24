## 2026-04-24 - Accessibility on Icon-Only Buttons
**Learning:** This single-file React app contained multiple icon-only `<button>` elements (e.g. `🔑`, `✕`) that lacked semantic accessible names for screen readers. This issue was replicated across duplicated code blocks inside the same `index.html` file.
**Action:** Always verify that buttons containing only text symbols/emojis or raw characters have an explicit `aria-label` describing their action, and ensure changes are synchronized if duplicate code blocks are present.
