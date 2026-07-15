# Global Component Specification

> **Generated:** 2026-07-14 &nbsp;|&nbsp; **Version:** 1.0.0

---

## Overview

Each Global Component is a normalized, parameterized, single-source-of-truth implementation that replaces multiple duplicate variants. Components follow BEM methodology (`block__element--modifier`) with the `.eods-` prefix.

All components:
- Use design tokens (never raw values)
- Support light and dark mode through CSS custom properties
- Meet WCAG 2.1 AA accessibility standards
- Are responsive by default
- Map to existing APEX Universal Theme template options where applicable
- Use vanilla JavaScript (no jQuery dependency)

---

## 1. Global Button

### Properties

| Property | Values | Default | Description |
|----------|--------|---------|-------------|
| `style` | `primary`, `secondary`, `outline`, `ghost`, `link` | `primary` | Visual style variant |
| `size` | `xs`, `sm`, `md`, `lg`, `xl` | `md` | Button dimensions |
| `color` | `default`, `success`, `warning`, `danger`, `info` | `default` | Semantic color (applies to primary/outline only) |
| `icon` | `none`, `left`, `right`, `icon-only` | `none` | Icon position |
| `width` | `auto`, `full` | `auto` | Width behavior |
| `disabled` | `true`, `false` | `false` | Disabled state |
| `loading` | `true`, `false` | `false` | Loading spinner state |
| `radius` | `none`, `sm`, `base`, `full` | `base` | Border radius override |

### HTML Template

```html
<!-- Primary, Medium, Default Color, Icon Left -->
<button type="button" class="eods-btn eods-btn--primary eods-btn--md eods-btn--icon-left"
        disabled aria-disabled="false">
  <span class="eods-btn__icon" aria-hidden="true">
    <span class="fa fa-check"></span>
  </span>
  <span class="eods-btn__text">Save Record</span>
</button>

<!-- Danger, Small, Icon Only, Loading -->
<button type="button" class="eods-btn eods-btn--danger eods-btn--sm eods-btn--icon-only eods-btn--loading"
        disabled aria-disabled="true" aria-label="Deleting...">
  <span class="eods-btn__spinner" aria-hidden="true"></span>
  <span class="eods-btn__icon" aria-hidden="true">
    <span class="fa fa-trash"></span>
  </span>
</button>

<!-- Outline, Large, Full Width -->
<button type="button" class="eods-btn eods-btn--outline eods-btn--lg eods-btn--full">
  <span class="eods-btn__text">Download Report</span>
  <span class="eods-btn__icon" aria-hidden="true">
    <span class="fa fa-download"></span>
  </span>
</button>

<!-- Ghost, Extra Small -->
<button type="button" class="eods-btn eods-btn--ghost eods-btn--xs">
  <span class="eods-btn__text">Cancel</span>
</button>

<!-- Link Style, Warning Color -->
<button type="button" class="eods-btn eods-btn--link eods-btn--warning">
  <span class="eods-btn__text">Skip this step</span>
</button>
```

### CSS Classes

```css
.eods-btn                          /* Base button */
.eods-btn--primary                 /* Filled, primary color */
.eods-btn--secondary               /* Filled, neutral color */
.eods-btn--outline                 /* Bordered, transparent bg */
.eods-btn--ghost                   /* No border, transparent bg, shows on hover */
.eods-btn--link                    /* Text-only, underline on hover */

.eods-btn--xs                      /* Height: 1.5rem, font: 0.625rem */
.eods-btn--sm                      /* Height: 2rem, font: 0.75rem */
.eods-btn--md                      /* Height: 2.5rem, font: 0.875rem */
.eods-btn--lg                      /* Height: 3rem, font: 1rem */
.eods-btn--xl                      /* Height: 3.5rem, font: 1.125rem */

.eods-btn--success                 /* Green color scheme */
.eods-btn--warning                 /* Amber color scheme */
.eods-btn--danger                  /* Red color scheme */
.eods-btn--info                    /* Blue color scheme (default) */

.eods-btn--icon-left               /* Icon before text */
.eods-btn--icon-right              /* Icon after text */
.eods-btn--icon-only              /* Icon only, no text (circle on xs/sm) */

.eods-btn--full                    /* width: 100% */
.eods-btn--loading                 /* Shows spinner, disables interaction */
.eods-btn--disabled                /* Grayed out, not-allowed cursor */
```

### JavaScript API

```javascript
eods.btn.setLoading(buttonElement, true);
eods.btn.setLoading(buttonElement, false);

eods.btn.disable(buttonElement);
eods.btn.enable(buttonElement);

eods.btn.confirm(buttonElement, {
  message: 'Are you sure you want to delete this record?',
  title: 'Confirm Delete',
  confirmText: 'Delete',
  cancelText: 'Cancel',
  type: 'danger'
}).then(confirmed => {
  if (confirmed) { /* proceed */ }
});
```

### APEX Template Option Mapping

| APEX Template Option | EODS Class |
|---------------------|-----------|
| Hot (Primary) | `.eods-btn--primary` |
| Warning | `.eods-btn--warning` |
| Danger | `.eods-btn--danger` |
| Success | `.eods-btn--success` |
| Large | `.eods-btn--lg` |
| Compact | `.eods-btn--sm` |
| Pill | `.eods-btn--radius-full` |
| Icon Only | `.eods-btn--icon-only` |
| Link Style | `.eods-btn--link` |

---

## 2. Global Form

### Properties

| Property | Values | Default | Description |
|----------|--------|---------|-------------|
| `layout` | `1-col`, `2-col`, `3-col`, `responsive`, `inline` | `responsive` | Column layout |
| `label-position` | `top`, `left`, `floating` | `top` | Label placement |
| `size` | `default`, `compact`, `large` | `default` | Field sizing |
| `stretch` | `none`, `all`, `individual` | `none` | Width behavior |
| `validation` | `inline`, `popup`, `both` | `inline` | Error display style |
| `label-width` | `auto`, `fixed-sm`, `fixed-md`, `fixed-lg` | `auto` | Fixed label width (left position only) |

### Supported Field Types

| Field Type | HTML Element | EODS Class | Notes |
|-----------|-------------|------------|-------|
| Text | `<input type="text">` | `.eods-form__control` | Single-line text |
| Textarea | `<textarea>` | `.eods-form__control .eods-form__textarea` | Multi-line, supports auto-resize |
| Select | `<select>` | `.eods-form__control .eods-form__select` | Dropdown |
| Date | `<input type="date">` | `.eods-form__control .eods-form__date` | Date picker |
| Number | `<input type="number">` | `.eods-form__control .eods-form__number` | Numeric input |
| Switch | `<input type="checkbox" role="switch">` | `.eods-form__switch` | Toggle switch |
| Checkbox | `<input type="checkbox">` | `.eods-form__checkbox` | Checkbox |
| Radio | `<input type="radio">` | `.eods-form__radio` | Radio button group |
| LOV / Popup LOV | `<input>` + popup trigger | `.eods-form__lov` | List of Values selector |
| Rich Text | `<div contenteditable>` | `.eods-form__richtext` | Rich text editor |
| File | `<input type="file">` | `.eods-form__file` | File upload |
| Display Only | `<span>` / `<div>` | `.eods-form__display` | Read-only display |
| Hidden | `<input type="hidden">` | N/A | Not rendered |

### HTML Template

```html
<form class="eods-form eods-form--responsive eods-form--cols-2 eods-form--label-top" novalidate>
  <!-- Standard text field -->
  <div class="eods-form__group">
    <label for="email" class="eods-form__label">
      Email Address
      <span class="eods-form__required" aria-hidden="true">*</span>
    </label>
    <input type="email" id="email" name="email"
           class="eods-form__control"
           placeholder="you@company.com"
           required
           aria-required="true"
           aria-describedby="email-hint email-error" />
    <span id="email-hint" class="eods-form__hint">Enter your work email address</span>
    <span id="email-error" class="eods-form__error" role="alert" hidden>Please enter a valid email</span>
  </div>

  <!-- Select field -->
  <div class="eods-form__group">
    <label for="department" class="eods-form__label">Department</label>
    <select id="department" name="department" class="eods-form__control eods-form__select">
      <option value="">— Select —</option>
      <option value="hr">Human Resources</option>
      <option value="it">Information Technology</option>
    </select>
  </div>

  <!-- Switch field -->
  <div class="eods-form__group eods-form__group--switch">
    <label class="eods-form__switch-label" for="active">
      <span class="eods-form__switch-track">
        <input type="checkbox" id="active" name="active"
               class="eods-form__switch-input" role="switch" checked />
        <span class="eods-form__switch-thumb"></span>
      </span>
      <span class="eods-form__switch-text">Active Employee</span>
    </label>
  </div>

  <!-- Textarea with character count -->
  <div class="eods-form__group eods-form__group--full">
    <label for="notes" class="eods-form__label">Notes</label>
    <textarea id="notes" name="notes"
              class="eods-form__control eods-form__textarea"
              rows="4" maxlength="500"
              aria-describedby="notes-count"></textarea>
    <span id="notes-count" class="eods-form__counter">0 / 500</span>
  </div>
</form>
```

### Validation States

```html
<!-- Valid -->
<div class="eods-form__group eods-form__group--valid">
  ...
  <span class="eods-form__icon-valid" aria-hidden="true">✓</span>
</div>

<!-- Invalid / Error -->
<div class="eods-form__group eods-form__group--error">
  ...
  <span class="eods-form__error" role="alert">This field is required</span>
</div>

<!-- Warning -->
<div class="eods-form__group eods-form__group--warning">
  ...
  <span class="eods-form__warning" role="alert">Value is outside normal range</span>
</div>
```

### Accessibility Requirements

| Requirement | Implementation |
|-------------|---------------|
| Labels | Every control has `<label>` with matching `for`/`id` |
| Required fields | `required` attribute + `aria-required="true"` + visual asterisk |
| Error messages | `role="alert"` on error container, `aria-describedby` pointing to error ID |
| Hints | `aria-describedby` pointing to hint ID |
| Keyboard | All fields reachable via `Tab`, switches togglable via `Space` |
| Focus | Visible focus ring using `:focus-visible` with `--shadow-focus` |

### APEX Template Option Mapping

| APEX Template Option | EODS Class |
|---------------------|-----------|
| Stretch Form | `.eods-form--stretch` |
| Compact | `.eods-form--compact` |
| Large Labels | `.eods-form--large` |
| Floating Labels | `.eods-form--label-floating` |
| Field Labels Above | `.eods-form--label-top` |
| Field Labels Left | `.eods-form--label-left` |

---

## 3. Global Dialog (Modal)

### Properties

| Property | Values | Default | Description |
|----------|--------|---------|-------------|
| `size` | `sm`, `md`, `lg`, `xl`, `fullscreen` | `md` | Dialog width |
| `header` | `none`, `title`, `title-close` | `title-close` | Header content |
| `footer` | `none`, `buttons`, `custom` | `buttons` | Footer content |
| `close-action` | `none`, `backdrop`, `esc`, `both` | `both` | Dismiss triggers |
| `state` | `normal`, `loading`, `empty` | `normal` | Content state |
| `position` | `centered`, `top`, `right-drawer` | `centered` | Screen position |
| `animation` | `fade`, `slide-up`, `slide-right`, `none` | `fade` | Entry animation |

### HTML Template

```html
<div class="eods-dialog-backdrop" aria-hidden="true"></div>

<div class="eods-dialog eods-dialog--md eods-dialog--centered"
     role="dialog"
     aria-modal="true"
     aria-labelledby="dialog-title"
     aria-describedby="dialog-body">

  <div class="eods-dialog__header">
    <h2 id="dialog-title" class="eods-dialog__title">Confirm Delete</h2>
    <button type="button" class="eods-dialog__close"
            aria-label="Close dialog">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>

  <div id="dialog-body" class="eods-dialog__body">
    <p>Are you sure you want to delete record <strong>EMP-0042</strong>?</p>
    <p class="eods-text--muted">This action cannot be undone.</p>
  </div>

  <div class="eods-dialog__footer">
    <button type="button" class="eods-btn eods-btn--secondary eods-btn--md"
            data-eods-dialog-close>Cancel</button>
    <button type="button" class="eods-btn eods-btn--danger eods-btn--md"
            data-eods-dialog-confirm>Delete</button>
  </div>
</div>
```

### Loading State

```html
<div class="eods-dialog__body">
  <div class="eods-dialog__loading">
    <div class="eods-spinner eods-spinner--lg" role="status">
      <span class="eods-sr-only">Loading...</span>
    </div>
    <p>Processing your request...</p>
  </div>
</div>
```

### Empty State

```html
<div class="eods-dialog__body">
  <div class="eods-dialog__empty">
    <span class="eods-dialog__empty-icon fa fa-inbox"></span>
    <h3>No items found</h3>
    <p>There are no records matching your criteria.</p>
  </div>
</div>
```

### Accessibility Requirements

| Requirement | Implementation |
|-------------|---------------|
| Role | `role="dialog"` or `role="alertdialog"` (for confirmation) |
| Modal | `aria-modal="true"` |
| Label | `aria-labelledby` pointing to title ID |
| Description | `aria-describedby` pointing to body ID |
| Focus trap | Tab cycles within dialog, Shift+Tab reverses |
| Close | ESC key closes (when enabled), close button has `aria-label` |
| Return focus | Focus returns to triggering element on close |
| Screen reader | Live region announces dialog open |

### JavaScript API

```javascript
const dialog = eods.dialog.create({
  title: 'Confirm Action',
  body: '<p>Are you sure?</p>',
  size: 'sm',
  footer: [
    { text: 'Cancel', style: 'secondary', close: true },
    { text: 'Confirm', style: 'primary', action: 'confirm' }
  ]
});

dialog.open();
dialog.close();
dialog.setLoading(true);
dialog.setBody('<p>New content</p>');
dialog.onConfirm(() => { /* handle confirmation */ });
dialog.onClose(() => { /* handle close */ });

eods.dialog.alert({
  title: 'Success',
  message: 'Record saved successfully.',
  type: 'success'
});

eods.dialog.confirm({
  title: 'Delete Record',
  message: 'This action cannot be undone.',
  type: 'danger',
  confirmText: 'Delete'
}).then(result => {
  if (result) { /* user confirmed */ }
});
```

### APEX Template Option Mapping

| APEX Template Option | EODS Class |
|---------------------|-----------|
| Small | `.eods-dialog--sm` |
| Medium | `.eods-dialog--md` |
| Large | `.eods-dialog--lg` |
| Full Screen | `.eods-dialog--fullscreen` |
| Show Header | `.eods-dialog__header` present |
| Show Footer | `.eods-dialog__footer` present |
| Auto Height | Default behavior |
| Resizable | Not supported (fixed sizes preferred for consistency) |

---

## 4. Global Interactive Grid Standard

### Properties

| Property | Values | Default | Description |
|----------|--------|---------|-------------|
| `toolbar.actions` | Array: `['add','edit','delete','export','import','search','reset','save','refresh','subscribe','unsubscribe']` | Full set | Visible toolbar actions |
| `toolbar.search.mode` | `simple`, `advanced`, `none` | `simple` | Search bar type |
| `toolbar.position` | `top`, `bottom`, `both` | `top` | Toolbar location |
| `toolbar.bulkActions` | Array of action names | `[]` | Bulk action menu items |
| `toolbar.saveReport` | `true`, `false` | `true` | Allow saving report configs |
| `rows.actionsMenu` | `true`, `false` | `true` | Per-row actions menu |
| `rows.actions` | Array: `['edit','delete','duplicate','copy','history']` | `['edit','delete']` | Per-row actions |
| `rows.selection` | `none`, `single`, `multiple` | `multiple` | Row selection mode |
| `rows.highlight` | `none`, `single`, `conditional` | `conditional` | Row highlighting |
| `pagination.style` | `standard`, `compact`, `none` | `standard` | Pagination style |
| `pagination.rowsPerPage` | Number | `25` | Rows per page |
| `pagination.options` | Array of numbers | `[10,25,50,100,500]` | Per-page options |
| `columns.formatting` | Per-column object | Auto-detect | Column format overrides |
| `columns.reorder` | `true`, `false` | `true` | Allow column reordering |
| `columns.resize` | `true`, `false` | `true` | Allow column resizing |
| `mode` | `readonly`, `editable`, `mixed` | `readonly` | Grid edit mode |
| `edit.addRow` | `top`, `bottom`, `last-page` | `bottom` | New row position |
| `edit.confirmDelete` | `true`, `false` | `true` | Confirm before delete |
| `keyboard.shortcuts` | `true`, `false` | `true` | Enable keyboard shortcuts |
| `export.formats` | Array: `['csv','pdf','excel','html']` | `['csv','excel','pdf']` | Export format options |
| `masterDetail.linking` | `none`, `single`, `cascading` | `none` | Master-detail setup |

### Column Formatting Configuration

```javascript
columns: {
  formatting: {
    'SALARY': {
      align: 'right',
      format: 'currency',
      decimals: 2,
      currency: 'USD',
      prefix: '$'
    },
    'HIRE_DATE': {
      align: 'center',
      format: 'date',
      pattern: 'MM/DD/YYYY'
    },
    'STATUS': {
      align: 'center',
      highlight: {
        type: 'conditional',
        rules: [
          { value: 'Active', class: 'eods-ig-cell--success' },
          { value: 'Inactive', class: 'eods-ig-cell--danger' },
          { value: 'On Leave', class: 'eods-ig-cell--warning' }
        ]
      }
    },
    'PERFORMANCE': {
      align: 'center',
      highlight: {
        type: 'range',
        rules: [
          { min: 0, max: 2, class: 'eods-ig-cell--danger' },
          { min: 3, max: 3, class: 'eods-ig-cell--warning' },
          { min: 4, max: 5, class: 'eods-ig-cell--success' }
        ]
      }
    }
  }
}
```

### CSS Classes

```css
.eods-ig                           /* Interactive Grid wrapper */
.eods-ig__toolbar                  /* Toolbar container */
.eods-ig__toolbar-actions          /* Action buttons group */
.eods-ig__toolbar-search           /* Search input group */
.eods-ig__table                    /* Table element */
.eods-ig__header-row              /* Header row */
.eods-ig__header-cell             /* Header cell */
.eods-ig__row                     /* Data row */
.eods-ig__row--selected           /* Selected row */
.eods-ig__row--hover              /* Hovered row */
.eods-ig__cell                    /* Data cell */
.eods-ig__cell--editable          /* Editable cell */
.eods-ig__cell--readonly          /* Read-only cell */
.eods-ig__cell--success           /* Green conditional highlight */
.eods-ig__cell--warning           /* Amber conditional highlight */
.eods-ig__cell--danger            /* Red conditional highlight */
.eods-ig__cell--info              /* Blue conditional highlight */
.eods-ig__pagination              /* Pagination container */
.eods-ig__row-actions             /* Per-row actions menu trigger */
.eods-ig__bulk-actions            /* Bulk actions dropdown */
.eods-ig__export-menu             /* Export format dropdown */

/* Modifiers */
.eods-ig--readonly                /* Read-only grid */
.eods-ig--editable                /* Editable grid */
.eods-ig--paginated               /* Pagination enabled */
.eods-ig--paginated-compact       /* Compact pagination */
.eods-ig--no-toolbar              /* Hidden toolbar */
.eods-ig--striped                 /* Alternating row colors */
.eods-ig--bordered                /* Cell borders */
.eods-ig--compact                 /* Reduced row height */
```

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| Tab | Next cell (or next focusable element) |
| Shift+Tab | Previous cell |
| Enter | Edit cell / confirm edit |
| Escape | Cancel edit / close popup |
| Arrow Keys | Navigate cells |
| Ctrl+Enter | Save all changes |
| Ctrl+A | Select all rows |
| Space | Toggle row selection |
| Delete | Delete selected row(s) |
| Ctrl+C | Copy cell content |
| Ctrl+F | Focus search field |
| Ctrl+Shift+F | Toggle advanced search |
| Page Down | Next page |
| Page Up | Previous page |
| Home | First row |
| End | Last row |

### APEX Template Option Mapping

| APEX Template Option | EODS Config |
|---------------------|-------------|
| Show Toolbar | `toolbar.actions` not empty |
| Show Search Bar | `toolbar.search.mode !== 'none'` |
| Show Actions Menu | `toolbar.actions` includes action names |
| Fixed Headers | CSS: `.eods-ig--fixed-header` |
| Stretch Report | CSS: `.eods-ig--stretch` |
| Row Selector | `rows.selection !== 'none'` |
| Alt Row Colors | CSS: `.eods-ig--striped` |
| Edit Mode — Row | `mode: 'editable'` |
| Edit Mode — Inline | `mode: 'editable'` + individual cell editing |
| Show Add Row | `toolbar.actions` includes `'add'` |

---

## 5. Global Card

### Properties

| Property | Values | Default | Description |
|----------|--------|---------|-------------|
| `variant` | `basic`, `elevated`, `outlined`, `interactive` | `basic` | Visual style |
| `layout` | `default`, `horizontal`, `metric`, `profile` | `default` | Content arrangement |
| `media` | `none`, `top`, `left`, `background` | `none` | Media/image placement |
| `size` | `sm`, `md`, `lg` | `md` | Card dimensions |
| `state` | `normal`, `hover`, `active`, `selected`, `loading` | `normal` | Interactive state |

### HTML Templates

```html
<!-- Default Card with Media Top -->
<div class="eods-card eods-card--elevated eods-card--md">
  <div class="eods-card__media">
    <img src="report-chart.png" alt="Sales Overview Chart" />
  </div>
  <div class="eods-card__body">
    <h3 class="eods-card__title">Quarterly Sales Report</h3>
    <p class="eods-card__text">Revenue up 24% compared to last quarter, driven by new product launches.</p>
  </div>
  <div class="eods-card__footer">
    <a href="#" class="eods-card__action">View Full Report &rarr;</a>
  </div>
</div>

<!-- Metric Card -->
<div class="eods-card eods-card--interactive eods-card--metric eods-card--sm">
  <div class="eods-card__body">
    <span class="eods-card__metric-label">Total Revenue</span>
    <span class="eods-card__metric-value">$2,847,293</span>
    <span class="eods-card__metric-trend eods-card__metric-trend--up">
      <span class="fa fa-arrow-up"></span> 12.5%
    </span>
  </div>
</div>

<!-- Profile Card -->
<div class="eods-card eods-card--outlined eods-card--profile eods-card--md">
  <div class="eods-card__avatar">
    <img src="avatar.jpg" alt="Jane Cooper" class="eods-card__avatar-img" />
  </div>
  <div class="eods-card__body">
    <h4 class="eods-card__title">Jane Cooper</h4>
    <p class="eods-card__subtitle">Senior Developer</p>
    <p class="eods-card__text">Engineering Department</p>
  </div>
  <div class="eods-card__footer">
    <span class="eods-badge eods-badge--success">Active</span>
  </div>
</div>

<!-- Horizontal Card (List Item) -->
<div class="eods-card eods-card--horizontal eods-card--sm eods-card--interactive">
  <div class="eods-card__icon">
    <span class="fa fa-file-pdf"></span>
  </div>
  <div class="eods-card__body">
    <h4 class="eods-card__title">Invoice-2024-0042.pdf</h4>
    <p class="eods-card__text">2.4 MB &bull; Uploaded 2 days ago</p>
  </div>
  <div class="eods-card__actions">
    <button class="eods-btn eods-btn--ghost eods-btn--sm eods-btn--icon-only">
      <span class="fa fa-download"></span>
    </button>
  </div>
</div>

<!-- Loading State -->
<div class="eods-card eods-card--loading">
  <div class="eods-card__skeleton eods-card__skeleton--title"></div>
  <div class="eods-card__skeleton eods-card__skeleton--text"></div>
  <div class="eods-card__skeleton eods-card__skeleton--text eods-card__skeleton--short"></div>
</div>
```

### CSS Classes

```css
.eods-card                        /* Base card */
.eods-card--basic                 /* Flat, no shadow */
.eods-card--elevated              /* Box shadow */
.eods-card--outlined              /* Border only */
.eods-card--interactive           /* Hover lift effect + cursor pointer */

.eods-card--default               /* Vertical layout */
.eods-card--horizontal            /* Horizontal layout (icon + content) */
.eods-card--metric                /* Big number + label */
.eods-card--profile               /* Avatar + name + meta */

.eods-card--sm                    /* Small padding, small text */
.eods-card--md                    /* Default */
.eods-card--lg                    /* Large padding, large text */

.eods-card--hover                 /* Hover state (raised shadow) */
.eods-card--active                /* Active/pressed state */
.eods-card--selected              /* Selected state (primary border) */
.eods-card--loading               /* Loading skeleton state */

.eods-card__media                 /* Media container */
.eods-card__media--top            /* Media on top */
.eods-card__media--left           /* Media on left (horizontal layout) */
.eods-card__media--background     /* Media as background */

.eods-card__avatar                /* Avatar container (profile card) */
.eods-card__avatar-img            /* Avatar image */
.eods-card__icon                  /* Icon container (horizontal card) */

.eods-card__body                  /* Body container */
.eods-card__title                 /* Card title */
.eods-card__subtitle              /* Card subtitle */
.eods-card__text                  /* Card text */
.eods-card__metric-label          /* Metric label (small, muted) */
.eods-card__metric-value          /* Metric value (large, bold) */
.eods-card__metric-trend          /* Trend indicator */
.eods-card__metric-trend--up      /* Positive trend (green) */
.eods-card__metric-trend--down    /* Negative trend (red) */
.eods-card__metric-trend--flat    /* Flat trend (neutral) */

.eods-card__footer                /* Footer container */
.eods-card__action                /* Footer action link */

.eods-card__skeleton              /* Loading skeleton */
.eods-card__skeleton--title       /* Title-sized skeleton */
.eods-card__skeleton--text        /* Text-sized skeleton */
.eods-card__skeleton--short       /* 60% width skeleton */

/* Grid Layout for Cards Container */
.eods-card-grid                   /* CSS Grid container */
.eods-card-grid--cols-2           /* 2 columns */
.eods-card-grid--cols-3           /* 3 columns */
.eods-card-grid--cols-4           /* 4 columns */
.eods-card-grid--responsive       /* Auto-fill responsive grid */
```

---

## 6. Global Navigation

### Types

| Type | Description | Breakpoint |
|------|-------------|-----------|
| Side Menu | Vertical sidebar with icons + text | All |
| Side Collapsed | Icons only with flyout submenus | Desktop |
| Top Bar | Horizontal navigation bar | Desktop |
| Mega Menu | Top bar with multi-column dropdown | Desktop |
| Mobile Drawer | Slide-out hamburger menu | <1024px |
| Mobile Bottom Tab | Bottom tab bar | <640px |

### HTML Template (Side Menu)

```html
<nav class="eods-nav eods-nav--side" aria-label="Main navigation">
  <div class="eods-nav__header">
    <a href="/" class="eods-nav__logo">
      <img src="logo.svg" alt="Company Logo" />
      <span class="eods-nav__logo-text">ERP System</span>
    </a>
    <button class="eods-nav__collapse-btn" aria-label="Toggle navigation" aria-expanded="true">
      <span class="fa fa-bars"></span>
    </button>
  </div>

  <ul class="eods-nav__list" role="menubar">
    <li class="eods-nav__item" role="none">
      <a href="/dashboard" class="eods-nav__link eods-nav__link--active" role="menuitem" aria-current="page">
        <span class="eods-nav__icon fa fa-dashboard"></span>
        <span class="eods-nav__text">Dashboard</span>
      </a>
    </li>

    <li class="eods-nav__item eods-nav__item--has-children" role="none">
      <button class="eods-nav__link eods-nav__link--expandable"
              aria-expanded="false" aria-haspopup="true" role="menuitem">
        <span class="eods-nav__icon fa fa-users"></span>
        <span class="eods-nav__text">HR Management</span>
        <span class="eods-nav__chevron fa fa-chevron-down"></span>
      </button>
      <ul class="eods-nav__submenu" role="menu" aria-label="HR Management" hidden>
        <li class="eods-nav__subitem" role="none">
          <a href="/employees" class="eods-nav__sublink" role="menuitem">Employees</a>
        </li>
        <li class="eods-nav__subitem" role="none">
          <a href="/departments" class="eods-nav__sublink" role="menuitem">Departments</a>
        </li>
        <li class="eods-nav__subitem" role="none">
          <a href="/positions" class="eods-nav__sublink" role="menuitem">Positions</a>
        </li>
      </ul>
    </li>

    <li class="eods-nav__item eods-nav__item--divider" role="separator"></li>

    <li class="eods-nav__item" role="none">
      <a href="/reports" class="eods-nav__link" role="menuitem">
        <span class="eods-nav__icon fa fa-chart-bar"></span>
        <span class="eods-nav__text">Reports</span>
        <span class="eods-nav__badge eods-badge eods-badge--danger eods-badge--sm">3</span>
      </a>
    </li>
  </ul>

  <div class="eods-nav__footer">
    <a href="/settings" class="eods-nav__link" role="menuitem">
      <span class="eods-nav__icon fa fa-cog"></span>
      <span class="eods-nav__text">Settings</span>
    </a>
  </div>
</nav>
```

### HTML Template (Top Bar)

```html
<nav class="eods-nav eods-nav--top" aria-label="Main navigation">
  <div class="eods-nav__container">
    <a href="/" class="eods-nav__brand">ERP System</a>
    <ul class="eods-nav__list eods-nav__list--horizontal" role="menubar">
      <li class="eods-nav__item" role="none">
        <a href="/dashboard" class="eods-nav__link eods-nav__link--active" role="menuitem">Dashboard</a>
      </li>
      <li class="eods-nav__item eods-nav__item--has-mega" role="none">
        <button class="eods-nav__link eods-nav__link--expandable"
                aria-expanded="false" aria-haspopup="true" role="menuitem">HR</button>
        <div class="eods-nav__mega" hidden>
          <div class="eods-nav__mega-col">
            <h4 class="eods-nav__mega-title">Employee Management</h4>
            <a href="/employees" class="eods-nav__sublink">All Employees</a>
            <a href="/employees/new" class="eods-nav__sublink">New Hire</a>
            <a href="/org-chart" class="eods-nav__sublink">Org Chart</a>
          </div>
          <div class="eods-nav__mega-col">
            <h4 class="eods-nav__mega-title">Payroll</h4>
            <a href="/payroll" class="eods-nav__sublink">Payroll Runs</a>
            <a href="/payslips" class="eods-nav__sublink">Payslips</a>
          </div>
        </div>
      </li>
    </ul>
  </div>
</nav>
```

### HTML Template (Mobile)

```html
<button class="eods-nav__hamburger" aria-label="Open menu" aria-expanded="false"
        aria-controls="mobile-nav">
  <span class="eods-nav__hamburger-line"></span>
  <span class="eods-nav__hamburger-line"></span>
  <span class="eods-nav__hamburger-line"></span>
</button>

<div class="eods-nav__drawer" id="mobile-nav" hidden>
  <div class="eods-nav__drawer-backdrop" data-eods-nav-close></div>
  <nav class="eods-nav__drawer-content" aria-label="Mobile navigation">
    <!-- Same structure as side menu -->
  </nav>
</div>
```

### CSS Classes

```css
.eods-nav                            /* Base nav container */
.eods-nav--side                      /* Vertical sidebar */
.eods-nav--side-collapsed            /* Collapsed sidebar (icons only) */
.eods-nav--top                       /* Horizontal top bar */
.eods-nav--fixed                     /* Fixed position */
.eods-nav--sticky                    /* Sticky position */

.eods-nav__container                 /* Inner container (top nav) */
.eods-nav__header                    /* Top section of side nav (logo area) */
.eods-nav__footer                    /* Bottom section of side nav */
.eods-nav__brand                     /* Brand/logo link (top nav) */
.eods-nav__logo                      /* Logo image wrapper */
.eods-nav__logo-text                 /* Logo text */
.eods-nav__collapse-btn              /* Collapse/expand toggle */

.eods-nav__list                      /* Top-level menu list */
.eods-nav__list--horizontal          /* Horizontal list (top nav) */
.eods-nav__item                      /* Menu item */
.eods-nav__item--has-children        /* Item with submenu */
.eods-nav__item--has-mega            /* Item with mega menu */
.eods-nav__item--divider             /* Menu divider */
.eods-nav__item--active              /* Active item (parent of active child) */

.eods-nav__link                      /* Menu link */
.eods-nav__link--active              /* Active link (aria-current="page") */
.eods-nav__link--expandable          /* Expandable link (button element) */
.eods-nav__icon                      /* Menu icon */
.eods-nav__text                      /* Menu text */
.eods-nav__chevron                   /* Expand/collapse chevron */
.eods-nav__badge                     /* Badge on menu item */

.eods-nav__submenu                   /* Nested submenu */
.eods-nav__subitem                   /* Submenu item */
.eods-nav__sublink                   /* Submenu link */

.eods-nav__mega                      /* Mega menu container */
.eods-nav__mega-col                  /* Mega menu column */
.eods-nav__mega-title                /* Mega menu column title */

.eods-nav__hamburger                 /* Hamburger toggle button */
.eods-nav__hamburger-line            /* Hamburger line */
.eods-nav__drawer                    /* Mobile drawer wrapper */
.eods-nav__drawer-backdrop           /* Drawer backdrop */
.eods-nav__drawer-content            /* Drawer content */

.eods-nav--dark                      /* Dark theme nav (default) */
.eods-nav--light                     /* Light theme nav */
```

### Accessibility Requirements

| Requirement | Implementation |
|-------------|---------------|
| Landmark | `<nav aria-label="Main navigation">` |
| Menubar | `role="menubar"` on `<ul>`, `role="none"` on `<li>`, `role="menuitem"` on links |
| Current page | `aria-current="page"` on active link |
| Expandable | `aria-expanded` and `aria-haspopup="true"` on expandable menus |
| Keyboard | Arrow keys navigate menu items, Enter/Space activate, Escape closes submenu |
| Mobile | `aria-expanded` on hamburger, `aria-controls` linking to drawer |
| Skip link | `.eods-skip-link` as first focusable element |

---

## 7. Global Badge

### HTML Template

```html
<span class="eods-badge eods-badge--success eods-badge--md">Active</span>
<span class="eods-badge eods-badge--danger eods-badge--sm eods-badge--pill">3</span>
<span class="eods-badge eods-badge--warning eods-badge--lg">
  <span class="eods-badge__icon fa fa-clock"></span>
  Pending
</span>
```

### Properties

| Property | Values | Default |
|----------|--------|---------|
| `color` | default, success, warning, danger, info, neutral | default |
| `size` | sm, md, lg | md |
| `shape` | default, pill | default |
| `variant` | solid, outline, subtle | solid |
| `has-icon` | true, false | false |
| `dismissible` | true, false | false |

---

## 8. Breadcrumb

### HTML Template

```html
<nav class="eods-breadcrumb" aria-label="Breadcrumb">
  <ol class="eods-breadcrumb__list">
    <li class="eods-breadcrumb__item">
      <a href="/" class="eods-breadcrumb__link">
        <span class="fa fa-home" aria-hidden="true"></span>
        Home
      </a>
    </li>
    <li class="eods-breadcrumb__separator" aria-hidden="true">/</li>
    <li class="eods-breadcrumb__item">
      <a href="/hr" class="eods-breadcrumb__link">HR Management</a>
    </li>
    <li class="eods-breadcrumb__separator" aria-hidden="true">/</li>
    <li class="eods-breadcrumb__item">
      <span class="eods-breadcrumb__current" aria-current="page">Employee #0042</span>
    </li>
  </ol>
</nav>
```

---

## Summary: Component Class Map

| Component | Base Class | Modifier Examples |
|-----------|-----------|------------------|
| Button | `.eods-btn` | `--primary`, `--sm`, `--danger`, `--loading`, `--full` |
| Form | `.eods-form` | `--cols-2`, `--compact`, `--label-floating` |
| Dialog | `.eods-dialog` | `--sm`, `--fullscreen`, `--right-drawer` |
| Interactive Grid | `.eods-ig` | `--striped`, `--compact`, `--editable` |
| Card | `.eods-card` | `--elevated`, `--metric`, `--horizontal`, `--loading` |
| Navigation | `.eods-nav` | `--side`, `--top`, `--collapsed` |
| Badge | `.eods-badge` | `--success`, `--pill`, `--lg` |
| Breadcrumb | `.eods-breadcrumb` | (minimal modifiers) |
| Spinner | `.eods-spinner` | `--sm`, `--primary`, `--overlay` |
| Toast / Notification | `.eods-toast` | `--success`, `--top-right` |
| Skip Link | `.eods-skip-link` | (single variant) |
| Screen Reader Only | `.eods-sr-only` | (utility) |
