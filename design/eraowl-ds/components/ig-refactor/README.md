# eops-ig — Enterprise Global Interactive Grid

Version 2.0 — Refactored from `interactive-grid._common.md` v1.0

## 5-Minute Quick Start

### 1. Add the component to your page

```apexlang
import "../components/ig-refactor/ig-refactored.apx"

region employees_grid (
  name: "Employees"
  type: interactiveGrid
  source {
    location: localDatabase
    type: sqlQuery
    sqlQuery:
      ```sql
      SELECT EMPLOYEE_ID, EMPLOYEE_NAME, DEPARTMENT, SALARY, HIRE_DATE
      FROM EMPLOYEES
      ORDER BY EMPLOYEE_NAME
      ```
    pageItemsToSubmit: "P1_DEPT_FILTER"
  }
  toolbar {
    profile: "full"
  }
  columns {
    EMPLOYEE_ID { type: number, heading: "ID", width: 80 }
    EMPLOYEE_NAME { type: text, heading: "Name" }
    DEPARTMENT { type: text, heading: "Department" }
    SALARY {
      type: currency
      heading: "Salary"
      formatMask: "FML999G999G999G999G990D00"
    }
    HIRE_DATE { type: date, heading: "Hire Date", formatMask: "DD-Mon-YYYY" }
  }
)
```

### 2. Include the stylesheet

```html
<link rel="stylesheet" href="components/ig-refactor/eops-ig.css">
```

### 3. Include the JavaScript

```html
<script type="module">
  import { IGController } from "./components/ig-refactor/eops-ig.js";
  window.empGrid = new IGController("employees_grid");
</script>
```

### 4. Wire up a master-detail

```javascript
import { IGMasterDetail } from "./components/ig-refactor/eops-ig.js";

IGMasterDetail.link("employees_grid", [
  {
    detailRegionId: "emp_detail",
    keys: [{ sourceColumn: "EMPLOYEE_ID", targetItem: "P1_EMP_ID" }]
  }
]);
```

### 5. Apply conditional highlighting

```javascript
import { IGRowHighlight } from "./components/ig-refactor/eops-ig.js";

IGRowHighlight.apply("employees_grid", [
  { column: "SALARY", operator: ">", value: 80000, className: "eops-ig--highlight-success" },
  { column: "SALARY", operator: "<", value: 50000, className: "eops-ig--highlight-danger" },
  { column: "DEPARTMENT", operator: "contains", value: "Engineering", rowLevel: true, className: "eops-ig--highlight-row-info" }
]);
```

---

## Migration Path: v1 → v2

### Step 1: Replace the template reference

**Before** (`interactive-grid._common.md`):
```
// Two separate templates selected by calling code
queryGrid(...) or tableGrid(...)
```

**After** (`ig-refactored.apx`):
```
// Single template. Set source.type to enable branching
source { type: "sqlQuery" | "tableName" ... }
```

### Step 2: Replace toolbar arrays with profiles

**Before** (in per-app config):
```javascript
controls: ["searchField", "actionsMenu", "saveReport", "resetReport", "download"]
```

**After** (in grid config):
```
toolbar {
  profile: "full"
}
```

### Step 3: Remove per-column filter operators

**Before**:
```
EMPLOYEE_NAME {
  type: text
  columnFilter {
    performanceImpactingOperators: ["contains", "startsWith", "caseInsensitive", "regexp"]
  }
}
```

**After**:
```
EMPLOYEE_NAME { type: text }
```

The global defaults in `IGColumnDefaults` apply automatically. Override per-column if needed:
```
SALARY {
  type: number
  columnFilter {
    defaultOperators: IGColumnDefaults.filterOperators("numeric")
  }
}
```

### Step 4: Replace inline JS with module import

**Before** (`initJavaScriptFunction` per grid):
```javascript
function(config) {
  var ig$ = apex.region("employees_grid").widget();
  ig$.interactiveGrid("getViews").grid.view$.grid("getSelectedRecords");
  // ... 10 more lines of boilerplate ...
}
```

**After** (one global import):
```javascript
import { IGController } from "./eops-ig.js";
const grid = new IGController("employees_grid");
grid.onRowSelect(row => apex.region("emp_detail").refresh());
```

### Step 5: Remove per-app IG CSS

**Before**: `app-ig-styles.css` (200+ lines of hardcoded IG overrides)

**After**: `<link rel="stylesheet" href="eops-ig.css">` (cached globally, design-token-driven)

### Step 6: Add APEXgen loader support

Add to your APEXgen pipeline config so that `{{IGToolbar.resolve(...)}}` resolves:
```json
{
  "loaders": {
    "IGToolbar": "./components/ig-refactor/ig-toolbar.js",
    "IGColumnDefaults": "./components/ig-refactor/ig-column-defaults.js"
  }
}
```

---

## Toolbar Profile Selection Guide

Choose the profile that matches the grid's interaction mode:

| Profile | Controls Included | Use When |
|---------|-------------------|----------|
| `full` | search, actions, save, reset, downloads | Default choice. Editable grids with all features |
| `minimal` | search only | Display-only grids with large datasets. Users only need to search |
| `readonly` | search, actions, downloads | Read-only grids where users may still need row actions and export |
| `admin` | search, actions, save, reset, downloads, subscriptions | Admin panels where users subscribe to report changes |
| `approval` | search, actions | Approval queues. Row actions (approve/reject) but no editing in-grid |
| `bulk` | search, actions, save, reset | Bulk-edit scenarios where checkboxes drive multi-row operations |
| `inline` | search, actions, save, reset | Inline editing mode (single-row-at-a-time edit) |
| `detail` | search, actions | Detail drill-down grids (row click opens detail panel) |
| `master` | search, actions, downloads | Master grids in master-detail layouts, with download capability |
| `viewer` | search, downloads | Public-facing or embedded read-only grids, download only |

---

## Column Formatter Usage

```javascript
import { IGColumnFormatter } from "./eops-ig.js";

// Currency formatting
IGColumnFormatter.currency(12500.5, { currency: "EUR", locale: "de-DE" });
// → "12.500,50 €"

// Date formatting
IGColumnFormatter.date("2025-03-15", { format: "longDate" });
// → "March 15, 2025"

// Percentage formatting
IGColumnFormatter.percentage(0.23, 1);
// → "23.0%"

// Status badge (returns HTML)
IGColumnFormatter.statusBadge("approved");
// → '<span class="eops-ig--highlight-success">approved</span>'
```

Use in an APEX column's HTML expression:
```
#HTML_EXPRESSION# = eods.ig2.IGColumnFormatter.statusBadge(#STATUS#);
```

---

## Highlight Rule Syntax

Rules are arrays of objects. Each rule has:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `column` | string | Yes | Column name to evaluate against |
| `operator` | string | No (default `"="`) | `"="`, `"!="`, `">"`, `"<"`, `">="`, `"<="`, `"contains"`, `"startsWith"`, `"isNull"`, `"isNotNull"` |
| `value` | * | No | Comparison value. Not used for `isNull`/`isNotNull` |
| `className` | string | Yes | CSS class to apply (prefix with `eops-ig--highlight-*`) |
| `rowLevel` | boolean | No (default `false`) | If `true`, applies class to the whole row instead of the cell |

**Available highlight classes:**

| Class | Effect |
|-------|--------|
| `eops-ig--highlight-success` | Green text (cell-level) |
| `eops-ig--highlight-warning` | Amber text (cell-level) |
| `eops-ig--highlight-danger` | Red text (cell-level) |
| `eops-ig--highlight-info` | Blue text (cell-level) |
| `eops-ig--highlight-row-success` | Green background (row-level) |
| `eops-ig--highlight-row-warning` | Amber background (row-level) |
| `eops-ig--highlight-row-danger` | Red background (row-level) |
| `eops-ig--highlight-row-info` | Blue background (row-level) |

---

## Master-Detail Wiring

```javascript
import { IGMasterDetail } from "./eops-ig.js";

// Wire up: clicking a row in "orders_grid" sets page items and refreshes detail regions
IGMasterDetail.link("orders_grid", [
  {
    detailRegionId: "order_items",
    keys: [{ sourceColumn: "ORDER_ID", targetItem: "P1_ORDER_ID" }]
  },
  {
    detailRegionId: "order_notes",
    keys: [{ sourceColumn: "ORDER_ID", targetItem: "P1_ORDER_ID" }]
  }
]);

// Clean up (e.g., in a dynamic action "Before Page Submit")
var detailLink = IGMasterDetail.link("orders_grid", [...]); // capture return
detailLink.dispose();
```

---

## Keyboard Navigation

```javascript
import { IGKeyboardNav } from "./eops-ig.js";

// Initialize on a grid. Returns a disposable object.
var nav = IGKeyboardNav.init("employees_grid");

// Keys:
//   Arrow keys  — move between cells
//   Enter       — edit focused cell (if editable)
//   Escape      — cancel edit, return focus to grid
//   Tab         — native browser tab order

// Clean up:
nav.dispose();
```

---

## Export API

```javascript
import { IGController, IGExportHelper } from "./eops-ig.js";

var grid = new IGController("employees_grid");

// Programmatic export
grid.exportData("excel");   // triggers APEX download action

// CSV with custom filename
grid.exportCSV({ filename: IGExportHelper.generateFilename("Employees", "csv") });

// Static shortcut (no controller needed)
IGExportHelper.triggerDownload("employees_grid", "pdf");
```

---

## IGController Full API Reference

```javascript
var ig = new IGController("employees_grid");

// Read
ig.getAllRows();                // → Array of all row objects
ig.getSelectedRows();           // → Array of selected row objects
ig.getCellValue("recordId", "COLUMN_NAME"); // → single cell value

// Write
ig.addRow({ NAME: "New", DEPT: "IT" });    // Add row with defaults
ig.setCellValue("recordId", "SALARY", 75000);
ig.deleteSelectedRows();        // Delete selected (requires edit enabled)
ig.saveAll();                   // Persist all changes

// Filter
ig.setFilter("DEPARTMENT", "Engineering", "EQ");
ig.clearFilters();

// Highlight
ig.applyHighlight([
  { column: "SALARY", operator: ">", value: 100000, className: "eops-ig--highlight-success" }
]);

// Events
ig.onRowSelect(function(row, allSelected) {
  console.log("Selected:", row.EMPLOYEE_NAME);
});

// Export
ig.exportData("csv");
ig.exportCSV({ filename: "export.csv" });
```

---

## Testing Checklist

Before deploying a grid with eops-ig, verify:

- [ ] **Template generation**: `ig-refactored.apx` produces valid APEXlang output for both `sqlQuery` and `tableName` source modes
- [ ] **Toolbar**: Correct controls appear for the selected profile (verify each of the 10 profiles renders correctly)
- [ ] **Responsive**: Resize viewport to 320px, 768px, 1200px. Toolbar wraps, cells remain readable, touch targets ≥ 44px
- [ ] **Dark mode**: Set `data-theme="dark"` on `<html>`. All rows, headers, inputs, dropdowns render with correct contrast
- [ ] **Keyboard nav**: Tab into grid. Arrow keys move between cells. Enter begins edit. Escape cancels.
- [ ] **Focus ring**: Navigate by keyboard. Every cell shows a visible 2px blue outline on focus.
- [ ] **Sort indicator**: Click a column header. `aria-sort` updates. Visual sort arrow appears.
- [ ] **Zebra striping**: Every even row shows the token stripe color. Selected row overrides stripe.
- [ ] **Editable cells**: Click cell → border turns blue. Enter value → no visual glitch. Error state → red border.
- [ ] **Pagination**: Click page numbers. Current page highlighted. Previous/Next work. `[disabled]` on first/last page.
- [ ] **Empty state**: Grid with zero rows shows centered "No data found." message.
- [ ] **Skeleton loading**: Grid shows shimmer animation during initial data fetch.
- [ ] **Action menu**: Click row action button. Dropdown opens with items. Click outside → closes.
- [ ] **Download menu**: Click download button. CSV/Excel/PDF options appear. Selecting one triggers download.
- [ ] **Single row view**: Click "View Details" action. Modal opens with field labels and values. Close button works.
- [ ] **Master-detail**: Select a row in master grid. Detail region refreshes with related data.
- [ ] **Highlight rules**: Apply rules to grid. Cells/rows with matching values receive correct classes.
- [ ] **Column formatters**: Currency shows symbol, date shows locale format, percentage shows `%`, status shows colored badge.
- [ ] **Export filename**: Exported file uses format `{gridname}_{YYYYMMDD_HHmmss}.{ext}`.
- [ ] **No jQuery dependency**: Verify no `$` or `jQuery` references in production code path.
- [ ] **CSP compatibility**: No `eval()`, no inline `onclick=""`, no `javascript:` URIs in generated code.
- [ ] **Cross-browser**: Tested on latest Chrome, Firefox, Safari, Edge.
