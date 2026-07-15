# Dark Mode Implementation Strategy — EraOwl Design System

> **Version:** 1.0.0 &nbsp;|&nbsp; **Approach:** CSS Custom Properties + Single Source of Truth

---

## 1. Philosophy

The EODS dark mode strategy follows three core principles:

1. **No duplicate CSS.** The same CSS rules render both light and dark themes. Only CSS custom property values change.
2. **Respect user preference.** System preference (`prefers-color-scheme`) is the default. Users can override via explicit toggle.
3. **Persistence.** User's explicit theme choice is stored in `localStorage` and applied before paint to prevent flash.

---

## 2. Architecture

```
                    ┌──────────────────────┐
                    │   prefers-color-      │
                    │   scheme: dark/light  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  localStorage check  │
                    │  eods_theme = ?      │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                 ▼
       ┌──────────┐    ┌────────────┐    ┌────────────┐
       │  Light   │    │   Dark     │    │    Auto    │
       │ (forced) │    │  (forced)  │    │ (OS pref)  │
       └────┬─────┘    └─────┬──────┘    └──────┬─────┘
            │                │                   │
            └────────────────┼───────────────────┘
                             │
                             ▼
              ┌──────────────────────────┐
              │  <html data-theme="..."> │
              │  or no attribute (auto)  │
              └──────────┬───────────────┘
                         │
                         ▼
              ┌──────────────────────────┐
              │  CSS Custom Properties   │
              │  reassigned via :root or │
              │  [data-theme="dark"]     │
              └──────────┬───────────────┘
                         │
                         ▼
              ┌──────────────────────────┐
              │  ALL components render   │
              │  with current tokens     │
              │  No duplicate CSS rules  │
              └──────────────────────────┘
```

---

## 3. Implementation Details

### 3.1 Token-Based Theming

All EODS components use CSS custom properties for EVERY visual attribute:

```css
/* Component CSS — NEVER uses raw color values */
.eods-card {
  background-color: var(--eods-card-bg);
  box-shadow: var(--eods-card-shadow);
  border-radius: var(--eods-card-radius);
}
```

The theme files (`theme-light.css`, `theme-dark.css`) only reassign these variables:

```css
/* theme-light.css — Default values */
:root {
  --eods-card-bg: #ffffff;
  --eods-card-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

/* theme-dark.css — Override for dark mode */
[data-theme='dark'] {
  --eods-card-bg: #1e293b;
  --eods-card-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}
```

### 3.2 System Preference Detection

```css
/* theme-dark.css */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme='light']) {
    --color-surface-page: #0f172a;
    --color-neutral-50: #1e293b;
    /* ... all dark mode tokens ... */
  }
}
```

Key detail: `:root:not([data-theme='light'])` means system preference only applies when the user has NOT explicitly chosen light mode. This gives the user override control.

### 3.3 User Toggle

```javascript
// JavaScript API in apex-global.js
eods.theme.set('dark');   // Force dark mode
eods.theme.set('light');  // Force light mode
eods.theme.set('auto');   // Follow system preference
eods.theme.toggle();      // Toggle dark/light
eods.theme.get();         // Returns 'dark', 'light', or 'auto'
```

Toggle button HTML example:

```html
<button id="theme-toggle" class="eods-btn eods-btn--ghost eods-btn--sm eods-btn--icon-only"
        aria-label="Toggle dark mode" onclick="eods.theme.toggle()">
  <span class="eods-btn__icon fa fa-moon"></span>
</button>
```

### 3.4 Flash Prevention

To prevent a "flash of wrong theme" (light theme appears before dark mode JS runs), use an inline script in `<head>`:

```html
<script>
  (function() {
    var theme = localStorage.getItem('eods_theme');
    if (theme === 'dark' || theme === 'light') {
      document.documentElement.setAttribute('data-theme', theme);
    }
  })();
</script>
```

This runs synchronously before any CSS is applied and before `apex-global.js` loads.

### 3.5 Storage

| Storage Key | Value | Description |
|-------------|-------|-------------|
| `eods_theme` | `"dark"`, `"light"`, absent | User's explicit theme preference. Absent = auto (system). |

---

## 4. Color Token Mapping Strategy

### Neutral Palette Inversion

The neutral/slate palette is fully inverted for dark mode:

| Light Token | Light Value | Dark Token | Dark Value |
|-------------|------------|------------|------------|
| `--color-neutral-50` | `#f8fafc` (light) | `--color-neutral-50` | `#1e293b` (dark) |
| `--color-neutral-900` | `#0f172a` (dark) | `--color-neutral-900` | `#ffffff` (light) |

This means: a component using `background-color: var(--color-neutral-100)` automatically gets a dark background in dark mode without any additional CSS.

### Semantic Color Preservation

Success, warning, danger, and info colors do NOT invert — red means danger in both themes. However, the shades used shift to maintain contrast:

| Usage | Light Mode | Dark Mode | Reason |
|-------|-----------|-----------|--------|
| Danger bg (subtle) | `--color-danger-50` (#fef2f2) | `--color-danger-50` (#fef2f2 — same) | Light red still visible on dark bg |
| Danger text | `--color-danger-600` (#dc2626) | `--color-danger-400` (#f87171) | Lighter red needed for dark bg contrast |
| Success text | `--color-success-700` (#047857) | `--color-success-400` (#34d399) | Lighter green needed for dark bg contrast |

**Important:** The semantic-50 tokens (lightest) are preserved across modes because they work on both light and dark backgrounds as subtle indicators.

### Surface Color Shifting

| Surface | Light | Dark |
|---------|-------|------|
| Page background | `#ffffff` | `#0f172a` |
| Region/card background | `#f8fafc` | `#1e293b` |
| Overlay (modal, dropdown) | `#ffffff` | `#1e293b` |
| Selected state | `#eff6ff` | `#1e3a8a` |
| Disabled state | `#f1f5f9` | `#1e293b` |
| Hover state | `#f8fafc` | `#334155` |

### Shadow Strengthening

Shadows become more opaque in dark mode (shadows on dark backgrounds need higher opacity to be visible):

| Shadow | Light | Dark |
|--------|-------|------|
| `--shadow-sm` | 0 1px 3px rgba(0,0,0,0.06) | 0 1px 3px rgba(0,0,0,0.4) |
| `--shadow-lg` | 0 10px 15px rgba(0,0,0,0.1) | 0 10px 15px rgba(0,0,0,0.4) |

### Native Form Controls

```css
[data-theme='dark'] {
  color-scheme: dark;
}
```

The `color-scheme` property tells the browser to render native form controls (select, input, scrollbars) in their dark variant if available.

---

## 5. APEX Template Option Integration

For apps that want to leverage APEX's built-in template options for theme control:

**Option A: Per-user theme style**

Create two APEX Theme Styles: "EODS Light" and "EODS Dark". Users select their preference which is stored in their APEX user preferences.

**Option B: Page-level toggle**

Add a Dynamic Action to toggle `data-theme` on `<html>`:

```javascript
// Toggle dark mode DA
var current = document.documentElement.getAttribute('data-theme');
document.documentElement.setAttribute('data-theme', current === 'dark' ? 'light' : 'dark');
eods.storage.set('theme', current === 'dark' ? 'light' : 'dark');
```

**Option C: Application-level setting**

Store theme preference in an APEX Application Item (`AI_THEME_MODE`) and set `data-theme` in the page template's `<html>` tag.

---

## 6. Edge Cases & Problem Areas

### 6.1 Images and Logos

| Issue | Solution |
|-------|----------|
| White-background logos become invisible on dark bg | Provide dark-mode logo variant. Apply `filter: brightness(0.9)` as fallback. |
| Screenshots/charts with white backgrounds | Wrap in container with light background. Use `data-theme-reset` attribute to force light mode on specific elements. |
| Icons | Use SVG with `currentColor` or Font APEX icons that inherit color. |

```css
[data-theme='dark'] img[data-theme-adapt] {
  filter: brightness(0.9) contrast(1.1);
}
```

### 6.2 Third-Party Content

APEX plugins and embedded content (iframes) may not support dark mode. Solutions:
- Scope dark mode CSS with `:where()` to limit reach.
- Use `[data-theme-reset]` attribute to force light mode on plugin containers.
- Contact plugin authors for dark mode support.

### 6.3 Hardcoded Inline Styles

Legacy inline styles (`style="background: white"`) will not respond to theme changes. During migration (Phase 2), these must be replaced with token-based classes.

### 6.4 APEX Page Rendering

APEX may inject inline styles for regions. These can be overridden by:
- Using higher-specificity class selectors
- Using `!important` on utility classes (already done for `.eods-bg-*` utilities)
- Requesting APEX template option changes instead of inline overrides

### 6.5 Chart Libraries

Oracle JET charts have their own theming. Set the JET theme to match:
```javascript
// In page inline JS
require(['ojs/ojthemeutils'], function(ThemeUtils) {
  ThemeUtils.setTheme('dark');
});
```

---

## 7. Testing Methodology

### Automated Testing

| Tool | What it Tests |
|------|--------------|
| axe-core / Lighthouse | Color contrast in dark mode |
| Playwright screenshots | Visual regression: light vs. dark at all breakpoints |
| CSS Stats | Verify no duplicate CSS between themes |

### Manual Testing Checklist

1. Toggle theme: no flash of wrong theme.
2. Toggle theme: all text remains readable (no white-on-white or black-on-black).
3. Toggle theme: all form controls remain visible and usable.
4. Toggle theme: all focus indicators are visible.
5. Toggle theme: images are visible (or gracefully hidden/degraded).
6. System preference: Set OS to dark mode → page loads in dark mode.
7. System preference override: Set OS to dark mode → manually set light → page stays light.
8. Persistence: Toggle to dark → refresh page → stays dark.
9. Persistence: Set to auto → change OS preference → page follows.
10. Print: Print in dark mode → printed page is light (if desired).

### Contrast Regression Testing

Every time design tokens change, re-verify:
- Primary text on page background: ≥ 7:1 (AAA target)
- Secondary text on page background: ≥ 4.5:1 (AA minimum)
- Button text on button background: ≥ 4.5:1 (AA minimum) or ≥ 3:1 (large text AA)
- Focus indicators: ≥ 3:1 (AA minimum for non-text)
- Form borders: ≥ 3:1 (AA minimum for non-text)

---

## 8. Rollout Strategy

| Phase | Scope | Duration |
|-------|-------|----------|
| Phase 1 | Token system + auto-detection only | Week 1 |
| Phase 2 | Toggle button on all pages | Week 2 |
| Phase 3 | Per-component dark mode testing | Week 3 |
| Phase 4 | Edge case resolution (images, plugins, charts) | Week 4 |
| Phase 5 | User preference persistence + analytics | Week 5 |

---

## 9. Implementation Files

| File | Purpose |
|------|---------|
| `css/tokens.css` | All color, spacing, typography tokens (light defaults) |
| `css/theme-light.css` | Light mode explicit overrides + base element styles |
| `css/theme-dark.css` | Dark mode token reassignments + component contrast fixes |
| `js/apex-global.js` | `eods.theme` module: get, set, toggle, init |
