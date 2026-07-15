# Duplicate Detection & Unification Report

> **Generated:** 2026-07-14 &nbsp;|&nbsp; **Version:** 1.0.0

---

## Executive Summary

In a typical enterprise Oracle APEX application, the most common root cause of maintenance burden is **component duplication**. Teams build "one more button style," "one more form layout," or "one more IG toolbar" when slight variations are needed — instead of parameterizing an existing global component.

This report identifies **12 major duplication patterns**, quantifies their impact, and proposes unified replacements using the EODS Global Component approach.

---

## Pattern 1: Button Styles (15 → 1)

### Current State
Enterprise apps typically accumulate button styles through copy-paste:
```
- btn-save (green, icon left)
- btn-cancel (gray, outline)
- btn-delete (red, icon left, with confirmation)
- btn-export (blue, icon right)
- btn-import (blue, icon right)
- btn-approve (green, large)
- btn-reject (red, large)
- btn-back (gray, ghost)
- btn-refresh (info, small, icon only)
- btn-add-row (success, small)
- btn-edit (primary, small, icon only)
- btn-download (primary, icon right)
- btn-upload (primary, icon right)
- btn-reset (warning, small)
- btn-print (neutral, icon right)
```

### Unification: Global Button

```html
<!-- One component, many configurations -->
<button class="eods-btn eods-btn--primary eods-btn--md eods-btn--icon-right">
  <span class="eods-btn__text">Save</span>
  <span class="eods-btn__icon fa fa-check"></span>
</button>

<button class="eods-btn eods-btn--danger eods-btn--md eods-btn--confirm">
  <span class="eods-btn__text">Delete</span>
</button>

<button class="eods-btn eods-btn--info eods-btn--sm eods-btn--icon-only">
  <span class="eods-btn__icon fa fa-sync"></span>
</button>
```

| Property | Values | Default |
|----------|--------|---------|
| `style` | primary, secondary, outline, ghost, link | primary |
| `size` | xs, sm, md, lg, xl | md |
| `color` | default, success, warning, danger, info | default |
| `icon` | none, left, right, icon-only | none |
| `state` | normal, loading, disabled | normal |
| `width` | auto, full | auto |

### Reduction
**15 styles → 1 component × 6 properties × 5 values × 4 icon positions = infinite combinations from one base**

---

## Pattern 2: Form Layouts (8 → 1)

### Current State
```
- form-2-col-fixed (static 2-column, 50/50)
- form-3-col-fixed (static 3-column, 33/33/33)
- form-2-col-left (70/30)
- form-2-col-right (30/70)
- form-stacked (1 column, full width)
- form-inline (side-by-side for search bars)
- form-compact (smaller labels, tighter spacing)
- form-wizard (multi-step with indicators)
```

### Unification: Global Form

```html
<form class="eods-form eods-form--responsive eods-form--cols-2 eods-form--label-top">
  <div class="eods-form__group">
    <label class="eods-form__label">Email</label>
    <input type="email" class="eods-form__control" />
    <span class="eods-form__hint">Enter your work email</span>
  </div>
</form>
```

| Property | Values | Default |
|----------|--------|---------|
| `layout` | 1-col, 2-col, 3-col, responsive, inline | responsive |
| `label-position` | top, left, floating | top |
| `size` | default, compact, large | default |
| `stretch` | none, all, individual | none |
| `validation` | inline, popup, both | inline |

### Reduction
**8 layouts → 1 component with 5 layout properties**

---

## Pattern 3: Modal / Dialog Patterns (5 → 1)

### Current State
```
- modal-confirm (confirmation dialog with Yes/No)
- modal-alert (simple OK dialog)
- modal-form (dialog with embedded form)
- modal-loading (spinner with message)
- modal-wizard (multi-step inside dialog)
```

### Unification: Global Dialog

```html
<div class="eods-dialog" role="dialog" aria-modal="true">
  <div class="eods-dialog__header">
    <h2 class="eods-dialog__title">Confirm Delete</h2>
    <button class="eods-dialog__close">&times;</button>
  </div>
  <div class="eods-dialog__body">
    <!-- Any content: form, text, loading spinner, wizard -->
  </div>
  <div class="eods-dialog__footer">
    <button class="eods-btn eods-btn--secondary">Cancel</button>
    <button class="eods-btn eods-btn--danger">Delete</button>
  </div>
</div>
```

| Property | Values | Default |
|----------|--------|---------|
| `size` | sm, md, lg, xl, fullscreen | md |
| `header` | none, title, title+close | title+close |
| `footer` | none, buttons, custom | buttons |
| `state` | normal, loading, empty | normal |
| `close-action` | none, backdrop-click, ESC, both | both |
| `position` | centered, top, right-drawer | centered |

### Reduction
**5 modal patterns → 1 component × 4 regions × 3 states**

---

## Pattern 4: Interactive Grid Toolbar Configurations (12 → 1)

### Current State
```
- ig-toolbar-full (all actions visible)
- ig-toolbar-minimal (search only)
- ig-toolbar-edit (edit mode tools)
- ig-toolbar-readonly (no edit actions)
- ig-toolbar-admin (add, edit, delete, export)
- ig-toolbar-viewer (export, search, reset only)
- ig-toolbar-approval (approve, reject, comment)
- ig-toolbar-bulk (bulk actions dropdown)
- ig-toolbar-master (master-grid config)
- ig-toolbar-detail (detail-grid config)
- ig-toolbar-inline (edit actions inline per row)
- ig-toolbar-search (advanced search panel)
```

### Unification: Global IG Standard

```javascript
eods.ig.init('emp_grid', {
  toolbar: {
    actions: ['add', 'edit', 'delete', 'export', 'search', 'reset'],
    search: { mode: 'simple', advanced: false },
    bulkActions: ['approve', 'reject', 'export_checked'],
    position: 'top',
    saveReport: true
  },
  rows: {
    actions: ['edit', 'delete', 'duplicate'],
    selection: 'multiple',
    highlight: 'conditional'
  },
  columns: {
    defaults: { align: 'left', format: 'auto' },
    formatting: {
      SALARY: { format: 'currency', decimals: 2 },
      STATUS: { highlight: 'conditional', mapping: { 'Active': 'success', 'Inactive': 'danger' } }
    }
  },
  pagination: { style: 'standard', rowsPerPage: 25 },
  mode: 'editable',
  keyboardShortcuts: true
});
```

| Property | Values | Default |
|----------|--------|---------|
| `toolbar.actions` | Array of action names | Full set |
| `toolbar.search.mode` | simple, advanced, none | simple |
| `rows.selection` | none, single, multiple | multiple |
| `pagination.style` | standard, compact, none | standard |
| `mode` | readonly, editable, mixed | readonly |
| `columns.formatting` | Per-column object | Auto-detect |

### Reduction
**12 toolbar configs → 1 configuration object with nested properties**

---

## Pattern 5: Notification / Alert Display (7 → 1)

### Current State
```
- alert-page-top (full-width page alert)
- alert-inline (inline form validation summary)
- toast-bottom-right (Snackbar-style)
- toast-top-center (centered notification)
- notification-badge (red badge count indicator)
- in-field-error (error below form field)
- popup-confirm (browser-level confirm/alert)
```

### Unification: Global Notification

```javascript
eods.notify.show('Item saved successfully', 'success', {
  position: 'top-right',
  duration: 5000,
  dismissible: true,
  icon: true
});

eods.notify.inlineError('field_email', 'Please enter a valid email');

eods.notify.confirm('Are you sure?', {
  title: 'Confirm Delete',
  type: 'danger'
}).then(confirmed => {
  if (confirmed) eods.ajax.post('DELETE_ITEM', { id: 123 });
});
```

| Property | Values | Default |
|----------|--------|---------|
| `type` | success, warning, danger, info, loading | info |
| `position` | top-right, top-left, bottom-right, bottom-left, top-center, bottom-center | top-right |
| `duration` | ms or `false` (sticky) | 5000 |
| `dismissible` | true, false | true |
| `icon` | true, false | true |

### Reduction
**7 alert patterns → 1 notification utility with 3 modes (toast, inline, confirm)**

---

## Pattern 6: Table / Report Styling (8 → 1)

### Current State
```
- table-striped (alternating row colors)
- table-bordered (borders on all cells)
- table-compact (reduced padding)
- table-hover (row highlight on hover)
- table-fixed (fixed header, scrollable body)
- table-responsive (horizontal scroll on mobile)
- table-selectable (click to select row)
- table-sortable (clickable column headers)
```

### Solution
APEX Interactive Report / Classic Report already handles most of these via **Template Options**. The EODS Global IG Standard extends this via CSS variables:

```css
.eods-ig {
  --eods-ig-row-stripe: var(--color-neutral-50);
  --eods-ig-row-hover: var(--color-primary-50);
  --eods-ig-row-selected: var(--color-primary-100);
  --eods-ig-cell-padding: var(--space-2) var(--space-3);
  --eods-ig-header-bg: var(--color-neutral-100);
  --eods-ig-border: 1px solid var(--color-neutral-200);
}
```

**Result:** 8 table style variations → 1 CSS class with customizable properties.

---

## Pattern 7: Card Layouts (9 → 1)

### Current State
```
- card-basic (simple box with padding, one of each)
- card-elevated (with box shadow)
- card-outlined (border only)
- card-interactive (hover effect, cursor pointer)
- card-metric (big number + label + trend indicator)
- card-profile (avatar + name + description)
- card-media (image top, text below)
- card-list-item (horizontal, icon left, text right)
- card-dashboard (compact, links to detail)
```

### Unification: Global Card

```html
<div class="eods-card eods-card--elevated eods-card--interactive">
  <div class="eods-card__media">
    <img src="chart.png" alt="Sales Chart" />
  </div>
  <div class="eods-card__body">
    <h3 class="eods-card__title">Quarterly Sales</h3>
    <p class="eods-card__text">Revenue increased by 24% this quarter.</p>
    <div class="eods-card__metric">
      <span class="eods-card__metric-value">$2.4M</span>
      <span class="eods-card__metric-trend eods-card__metric-trend--up">+24%</span>
    </div>
  </div>
  <div class="eods-card__footer">
    <a href="#" class="eods-btn eods-btn--ghost eods-btn--sm">View Details</a>
  </div>
</div>
```

| Property | Values | Default |
|----------|--------|---------|
| `variant` | basic, elevated, outlined, interactive | basic |
| `layout` | default, horizontal, metric, profile | default |
| `media` | none, top, left, background | top |
| `state` | normal, hover, active, selected, loading | normal |
| `size` | sm, md, lg | md |

### Reduction
**9 card layouts → 1 component × 4 variants × 4 layouts × 3 sizes**

---

## Pattern 8: Navigation Patterns (6 → 1)

### Current State
```
- nav-side-standard (icon + text, expandable)
- nav-side-collapsed (icons only, flyout menus)
- nav-top-bar (horizontal links across top)
- nav-top-mega (dropdown mega menu with columns)
- nav-mobile-bottom (bottom tab bar)
- nav-breadcrumb (hierarchical path trail)
```

### Unification: Global Navigation

| Type | Breakpoint | Description |
|------|-----------|-------------|
| `side` | All | Vertical sidebar with collapsible sections |
| `top` | Desktop | Horizontal top bar with dropdowns |
| `mega` | Desktop | Top bar with multi-column dropdowns |
| `mobile` | <1024px | Bottom tab bar or hamburger drawer |
| `breadcrumb` | All | Hierarchical path (separate component, but integrated) |

Breadcrumb is treated as a companion component since it serves a different UX purpose (location awareness vs. primary navigation).

### Reduction
**6 nav patterns → 2 components (Global Navigation + Breadcrumb)**

---

## Pattern 9: Color / Theming Abuse (N → 1 System)

### Current State
Enterprise apps commonly have:
- Inline `style="color: #ff0000"` on 200+ elements
- Multiple competing color palettes across pages
- Different "blue" for different developers
- Hardcoded dark-mode overrides
- Shadow values inconsistent across pages

### Solution: Design Token System

All colors, spacing, typography, shadows, and radii are defined **exactly once** in `tokens.css`. Components reference tokens, not raw values.

```css
/* BEFORE: Hardcoded */
color: #2563eb;
background: #f8fafc;

/* AFTER: Token-based */
color: var(--color-primary-500);
background: var(--color-surface-region);
```

**Result:** Infinite color variations → 1 design token system (108+ tokens covering all needs)

---

## Pattern 10: JavaScript Utilities (15+ → 1)

### Current State
Multiple copies of:
- AJAX wrapper functions (3+ variants)
- Modal open/close utilities (4+ variants)
- Notification functions (2+ variants)
- Form validation helpers (3+ variants)
- Date formatting functions (2+ variants)
- Storage wrappers (2+ variants)
- Error handlers (4+ variants)

### Solution: `apex-global.js` — Single namespace, all utilities

### Reduction
**15+ utility copies → 1 JavaScript file with 8 modules**

---

## Pattern 11: Responsive / Mobile Adapters (5 → 1)

### Current State
- Per-page `@media` queries (inconsistent breakpoints)
- Duplicate CSS for mobile form layouts
- Inconsistent hamburger menu triggers
- Different mobile table handling per report
- Per-component scroll-container wrappers

### Solution: Responsive Design System

Defined once in the token system:
```css
--breakpoint-sm: 640px;
--breakpoint-md: 1024px;
```

All components use these breakpoints. Responsive behavior is built into each Global Component.

### Reduction
**5 scattered approaches → 1 breakpoint system + built-in responsive components**

---

## Pattern 12: Page Templates / Layouts (10+ → 3)

### Current State
Enterprise apps accumulate page templates:
```
- standard-page (left nav + content)
- no-nav-page (full width, no sidebar)
- login-page (centered card)
- wizard-page (multi-step with progress)
- report-page (IG full-width + filters)
- dashboard-page (grid of cards/charts)
- modal-page (just for modals)
- blank-page (no header/footer)
- print-page (optimized for printing)
- error-page (404/500 styled pages)
```

### Solution: One `Standard Page` template with template options

Universal Theme's Standard Page template handles nearly all of this via template options. The EODS adds dashboard and wizard templates as documented configurations:

| Page Type | Template Option Config |
|-----------|----------------------|
| Standard | Nav: Left, Content: Full |
| Full Width | Nav: Hidden, Content: Full |
| Dashboard | Nav: Left/Collapsed, Content: Full (Dashboard region) |
| Wizard | Nav: Hidden, Region: Wizard Container |
| Login | Login Page Template (built-in) |
| Modal | Modal Page Template (built-in) |
| Print | Standard Page + Print CSS |

### Reduction
**10+ page templates → 2 templates + template options**

---

## Impact Summary

| Pattern | Before | After | Reduction |
|---------|--------|-------|-----------|
| Button Styles | 15 | 1 component | 93% |
| Form Layouts | 8 | 1 component | 87.5% |
| Modal Patterns | 5 | 1 component | 80% |
| IG Toolbar Configs | 12 | 1 config object | 92% |
| Notification Patterns | 7 | 1 utility | 86% |
| Table Styles | 8 | 1 CSS class | 87.5% |
| Card Layouts | 9 | 1 component | 89% |
| Navigation Patterns | 6 | 2 components | 67% |
| Color/Theming | Infinite | 1 token system | ~100% |
| JS Utilities | 15+ copies | 1 file | ~93% |
| Responsive Adapters | 5 approaches | 1 system | 80% |
| Page Templates | 10+ | 2 + options | ~80% |

**Total estimated reduction in unique component variants: ~85%**

**Estimated maintenance effort reduction: ~70%**

**Estimated onboarding time reduction (new developers): ~60%**
