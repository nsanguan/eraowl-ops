# EraOwl Design System (EODS)

> **Version:** 1.0.0 — **Target:** React 19 + FastAPI + Tailwind CSS 4

---

## Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                              PAGES                                    │
│   (Login, Dashboard, User/Role Management, Org Structure, Party,     │
│    Item Master, BOM Explorer, PO Management)                         │
├──────────────────────────────────────────────────────────────────────┤
│                            LAYOUT                                     │
│   (AppShell, Sidebar, Header, Breadcrumbs, ErrorBoundary,            │
│    TopStatusBar, ThemeProvider)                                       │
├──────────────────────────────────────────────────────────────────────┤
│                           COMPONENTS                                  │
│  ┌──────────┬───────────┬────────────┬──────────┬───────────┐       │
│  │ Buttons  │   Forms   │ Interactive│  Cards   │  Dialogs  │       │
│  │ (5 var.) │ (6 var.)  │    Grid    │ (4 var.) │ (3 var.)  │       │
│  ├──────────┼───────────┼────────────┼──────────┼───────────┤       │
│  │   Nav    │  Badges   │ Dashboards │  Wizard  │   Tree    │       │
│  │ (4 var.) │ (5 var.)  │  (6 var.)  │  (step)  │  (Grid)   │       │
│  ├──────────┼───────────┼────────────┼──────────┼───────────┤       │
│  │ Shuttle  │ Segmented │ Faceted    │   LOV    │ StatCard  │       │
│  │ Control  │  Control  │  Search    │  Modal   │           │       │
│  └──────────┴───────────┴────────────┴──────────┴───────────┘       │
├──────────────────────────────────────────────────────────────────────┤
│                     UTILITY CSS (eods-*)                              │
│   (Layout, Spacing, Typography, Display, Border, Shadow,             │
│    Animation, Print, Screen-Reader, Spinner)                         │
├──────────────────────────────────────────────────────────────────────┤
│                    DESIGN TOKENS  (CSS custom properties)             │
│  ┌─────────┬──────────┬───────────┬──────────┬─────────────┐        │
│  │ Colors  │   Type   │  Spacing  │ Shadows  │  Animation  │        │
│  │  (12×9) │  (scale) │  (scale)  │ (5 vars) │   (3 vars)  │        │
│  ├─────────┼──────────┼───────────┼──────────┼─────────────┤        │
│  │ Radius  │  Z-Index │ Breakpts  │ Surfaces │ Theme:Dark  │        │
│  │(7 vars) │ (8 vars) │  (3 vars) │ (4 vars) │  (override) │        │
│  └─────────┴──────────┴───────────┴──────────┴─────────────┘        │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Principles

| Principle | Description |
|-----------|-------------|
| **Tailwind-Compatible** | All CSS custom properties map to Tailwind's `@theme` directive. Use EODS tokens or Tailwind utility classes interchangeably. |
| **WCAG 2.1 AA Compliant** | Minimum contrast 4.5:1 (text), 3:1 (large text). Keyboard navigable. Screen-reader friendly. |
| **Responsive by Default** | Mobile-first breakpoints. Fluid typography. Adaptive sidebar layout (collapses on tablet). |
| **Dark Mode Ready** | CSS custom property approach — single source, dual themes. System preference + manual toggle via React ThemeProvider. |
| **React-First** | Components designed for React SPA patterns: Zustand state management, axios HTTP, react-router navigation. |
| **Declarative First** | Use Tailwind utility classes for layout/spacing, EODS component CSS for complex patterns (InteractiveGrid, Sidebar). |
| **Zero jQuery Dependency** | Vanilla JavaScript (ES2020+) with Promise-based async patterns. React handles DOM manipulation. |
| **Single Source of Truth** | Design tokens in `tokens.css` define everything. No magic numbers in component CSS. |

---

## Quick Start

The EraOwl Design System integrates with the existing Tailwind CSS v4 setup in `eraowl-ops-frontend/src/index.css`.

### 1. Import Design Tokens

Add to your `index.css`:

```css
@import "tailwindcss";

/* Design tokens — already mapped to Tailwind @theme below */
:root {
  /* Color tokens */
  --color-primary-50: #eff6ff;
  --color-primary-100: #dbeafe;
  /* ... see tokens.css for full list */
}

@theme inline {
  --color-primary: var(--color-primary-500);
  --color-primary-foreground: #ffffff;
  /* ... Tailwind-compatible mappings */
}
```

> **Note:** The project's `index.css` already maps all design tokens to Tailwind's `@theme inline` directive. See `css/tokens.css` for the full token reference.

### 2. Use Component CSS

For complex UI patterns (InteractiveGrid, Sidebar, Dialog), import the EODS component CSS:

```jsx
// In your React component
import '../../design/eraowl-ds/css/grid.css'
import '../../design/eraowl-ds/css/buttons.css'
```

Or in your main entry:

```jsx
// main.jsx — import all design system styles
import '../design/eraowl-ds/css/global.css'
```

### 3. Use Tailwind for Layout

```jsx
// Standard page layout
<div className="flex h-screen">
  <Sidebar /> {/* Uses eods-nav--side classes */}
  <main className="flex-1 overflow-y-auto p-6">
    <PageHeader title="User Management" />
    <InteractiveGrid columns={columns} data={data} />
  </main>
</div>
```

### 4. Use Zustand for Theme State

```jsx
import { useThemeStore } from './stores/preferences'

function ThemeToggle() {
  const { theme, toggleTheme } = useThemeStore()
  return <button onClick={toggleTheme}>Toggle {theme}</button>
}
```

---

## File Structure

```
design/eraowl-ds/
├── README.md                          # This file
├── TAILWIND_INTEGRATION.md            # Tailwind CSS v4 mapping guide
├── docs/
│   ├── 01-tokens-reference.md         # Complete design token specification
│   ├── 02-components-overview.md      # Component library overview
│   ├── 03-accessibility.md            # WCAG 2.1 AA compliance
│   ├── 04-responsive.md               # Responsive design strategy
│   ├── 05-dark-mode.md                # Dark mode implementation
│   └── 06-best-practices.md           # React + EraOwl best practices
├── css/
│   ├── global.css                     # Master import file
│   ├── tokens.css                     # CSS custom properties (design tokens)
│   ├── theme-light.css                # Light mode (default)
│   ├── theme-dark.css                 # Dark mode overrides
│   ├── buttons.css                    # Button component (5 variants)
│   ├── forms.css                      # Form component (6 layouts)
│   ├── grid.css                       # Interactive Grid component
│   ├── dialog.css                     # Modal Dialog component
│   ├── cards.css                      # Card component (4 variants)
│   ├── navigation.css                 # Sidebar + Top navigation
│   ├── dashboard.css                  # Dashboard grid layouts
│   ├── badge.css                      # Badges & status indicators
│   └── utility.css                    # Utility classes + spinner
└── js/
    └── eraowl-global.js               # EODS JavaScript utilities
```

---

## Design Tokens

All tokens are defined as CSS custom properties in `css/tokens.css`. Key categories:

| Category | Example Tokens | Count |
|----------|---------------|-------|
| **Primary Color** | `--color-primary-500` (#2563EB) | 10 shades |
| **Neutral** | `--color-neutral-500` (#64748B) | 10 shades |
| **Semantic** | success, warning, danger, info | 10 shades each |
| **Surface** | page, region, card, overlay, selected | 7 tokens |
| **Typography** | font families, sizes (10), weights (6), line heights (6) | 28 tokens |
| **Spacing** | 4px base scale (0 → 24rem) | 33 values |
| **Shadows** | xs → 2xl + inner + focus | 11 tokens |
| **Border Radius** | none → full/pill | 9 values |
| **Z-Index** | base → debug | 10 values |
| **Animation** | transitions (4), easing (3) | 7 tokens |

---

## Component CSS Classes

All custom CSS classes use the `.eods-` prefix to avoid collisions with Tailwind utilities.

### Buttons (css/buttons.css)
`.eods-btn` base + style modifiers: `--primary`, `--secondary`, `--outline`, `--ghost`, `--link`
Size: `--xs`, `--sm`, `--md`, `--lg`, `--xl`
Color: `--success`, `--warning`, `--danger`, `--info`
States: `:disabled`, `.eods-btn--loading` (with spinner animation)
Group: `.eods-btn-group`

### Interactive Grid (css/grid.css)
`.eods-ig` — Full-featured data table with toolbar, header sorting, pagination, row actions, bulk selection, export menu, loading/empty states
Modifiers: `--striped`, `--bordered`, `--compact`, `--no-toolbar`, `--fixed-header`

### Forms (css/forms.css)
`.eods-form` — Layouts: `--cols-2/3/4`, `--responsive`, `--inline`, `--compact`, `--large`, `--label-left`, `--label-floating`
`.eods-form__group`, `__label`, `__control`, `__hint`, `__error`, `__select`, `__textarea`
Validation: `--error`, `--warning`, `--valid` states
Components: Switch toggle, Checkbox, Radio, Fieldset

### Dialog/Modal (css/dialog.css)
`.eods-dialog` + `.eods-dialog-backdrop` — Sizes: `--sm/md/lg/xl/fullscreen`
Positions: `--right-drawer`, `--top`
Types: `--alert`, `--confirm`, `--form`
Elements: `__header`, `__body`, `__footer`, `__close`, `__title`

### Cards (css/cards.css)
`.eods-card` — Variants: `--basic`, `--elevated`, `--outlined`, `--interactive`
Layouts: `--horizontal`, `--metric`, `--profile`
Elements: `__media`, `__body`, `__title`, `__subtitle`, `__text`, `__footer`, `__skeleton`
Grid: `.eods-card-grid` with `--cols-1/2/3/4`, `--responsive`

### Navigation / Sidebar (css/navigation.css)
`.eods-nav--side` — Collapsible sidebar with logo, links, submenus, footer
`.eods-nav--top` — Horizontal top navigation bar
`.eods-nav--light` — Light sidebar variant
`.eods-breadcrumb` — Breadcrumb navigation

### Dashboard (css/dashboard.css)
`.eods-dashboard` — Grid layouts: `--cols-2/3/4`, `--cols-2-1`, `--cols-1-2`
Widget variants: `--metrics`, `--table`, `--chart`, `--list`

### Badge (css/badge.css)
`.eods-badge` — Colors: `--primary`, `--success`, `--warning`, `--danger`, `--info`, `--neutral`
Sizes: `--sm`, `--md`, `--lg`
Variants: `--dot` (online indicator), `--pill` (rounded), `--outline`, `--ghost`
Position: `--top-right` (overlapping)

### Utilities (css/utility.css)
Layout: `.eods-container`, `.eods-flex-*`, `.eods-grid-cols-*`
Spacing: `.eods-m-*`, `.eods-p-*`, `.eods-gap-*`
Text: `.eods-text-*`, `.eods-truncate`, `.eods-text-bold`
Visibility: `.eods-sr-only`, `.eods-hidden`, `.eods-visible`
Shadow: `.eods-shadow-*`
Spinner: `.eods-spinner` (sizes: `--sm`, `--lg`, `--xl`; colors: `--success`, `--warning`, `--danger`, `--light`)
Responsive: `.eods-sm-hidden`, `.eods-md-hidden`, `.eods-sm-w-full`

---

## Integration with React Shared UI Kit

The design system CSS powers the React components in `eraowl-ops-frontend/src/shared-ui-kit/`:

| React Component | EODS CSS | File |
|----------------|----------|------|
| `InteractiveGrid` | `grid.css` | `shared-ui-kit/components/ui/InteractiveGrid.tsx` |
| `StatCard` | `cards.css` | `shared-ui-kit/components/ui/StatCard.tsx` |
| `StatusChip` | `badge.css` | `shared-ui-kit/components/ui/StatusChip.tsx` |
| `PageHeader` | (Tailwind) | `shared-ui-kit/components/ui/PageHeader.tsx` |
| `Sidebar` | `navigation.css` | `shared-ui-kit/components/layout/Sidebar.tsx` |
| `AppShell` | `navigation.css` | `shared-ui-kit/components/layout/AppShell.tsx` |
| `Wizard` | `dialog.css` | `shared-ui-kit/components/ui/Wizard.tsx` |
| `SegmentedControl` | `forms.css` | `shared-ui-kit/components/ui/SegmentedControl.tsx` |
| `TreeGrid` | `grid.css` | `shared-ui-kit/components/ui/TreeGrid.tsx` |

---

## Naming Conventions

| Prefix | Purpose | Example |
|--------|---------|---------|
| `.eods-` | All custom CSS classes | `.eods-btn--primary` |
| `eods.` | JavaScript namespace | `eods.modal.open()` |
| `--eods-` | CSS custom properties (internal) | `--eods-btn-radius` |
| `--color-` | Shared design tokens | `--color-primary-500` |

---

## Browser Support

- Modern browsers (Chrome 90+, Firefox 90+, Safari 15+, Edge 90+)
- CSS Custom Properties (Level 1+)
- CSS Grid (Level 1+)
- ES2020+ JavaScript
- `prefers-color-scheme` for dark mode detection
- `prefers-reduced-motion` for accessibility

---

## How to Contribute

1. Never modify the frontend's `index.css` directly — update tokens in `css/tokens.css` instead.
2. Add custom styles in component CSS files under `css/`.
3. Prefix all classes with `.eods-`.
4. Use design tokens — never hardcode colors, spacing, or typography values.
5. Test in light and dark mode before committing.
6. Run Lighthouse accessibility checks.
7. Update the component reference in this README if adding new CSS.
8. Keep Tailwind `@theme` mapping in sync with token changes.
