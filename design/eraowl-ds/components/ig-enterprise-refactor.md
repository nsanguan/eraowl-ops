# Global Interactive Grid — Enterprise Refactoring

## Component: `eops-ig` (EraOwl-OPS Interactive Grid)

### Pre-Refactoring State (Oracle APEX `interactiveGrid`)

The current canonical APEXlang Interactive Grid contract (`interactive-grid._common.md`, v1.0) consists of **239 lines** defining two
nearly-identical output templates (query-backed: 137 lines, table-backed: 138 lines) with **80% structural duplication**.

### Enterprise Duplication Analysis

From the `02-duplicate-report.md` inventory of a typical 15-page ERP application:

| Pattern | Before | After | Reduction |
|---|---|---|---|
| Toolbar configurations | 12 IG variants | 1 config object | **92%** |
| `savedReport.displayColumn` lists | Per-grid × 12 | Generated from schema | **100%** |
| `columnFilter.performanceImpactingOperators` | 4 operators × N text cols | Single global default | **Per-column eliminated** |
| `componentAdvanced.initJavaScriptFunction` | Duplicated boilerplate | Shared JS module | **86%** |
| Source-mode branch (query vs table) | 2 full templates | 1 parameterized factory | **50%** |
