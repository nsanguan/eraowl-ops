# Migration Checklist — EraOwl Design System

> **Version:** 1.0.0 &nbsp;|&nbsp; **Target:** APEX 24.x Universal Theme

---

## Overview

This checklist provides a phased, repeatable process for migrating an existing Oracle APEX application to the EODS (Enterprise Oracle Design System). Each phase builds on the previous one and has clear entry/exit criteria.

---

## Phase 1: Inventory & Audit (Week 1)

| # | Task | Owner | Status | Notes |
|---|------|-------|--------|-------|
| 1.1 | Export component list from Shared Components | Architect | ☐ | List all LOVs, lists, auth schemes, authorization schemes |
| 1.2 | Audit all page templates in use | Architect | ☐ | Count pages per template type |
| 1.3 | Audit all region types across all pages | Developer | ☐ | interactive-report, form, IG, chart, etc. |
| 1.4 | Audit all page item types across all pages | Developer | ☐ | text-field, select-list, date-picker, etc. |
| 1.5 | Audit all button types and styles | Developer | ☐ | Hot, warning, danger, icon-only, etc. |
| 1.6 | Count dynamic actions per page | Developer | ☐ | Flag pages with >20 DAs for review |
| 1.7 | Catalog all custom CSS (inline, page-level, theme-level) | Developer | ☐ | Grep for `<style>`, style attributes, `.css` imports |
| 1.8 | Catalog all custom JavaScript (inline, page-level, theme-level) | Developer | ☐ | Grep for `<script>`, `.js` imports, `function` declarations |
| 1.9 | Check Universal Theme version and last upgrade date | Admin | ☐ | APEX → About Application |
| 1.10 | Check for deprecated APEX APIs in use | Architect | ☐ | `apex.util.showMessage`, old chart APIs, old IR APIs |
| 1.11 | Count total pages, regions, items | Architect | ☐ | Use APEX dictionary views |
| 1.12 | Run accessibility audit (Lighthouse / axe-core) | Developer | ☐ | Document baseline scores |
| 1.13 | Run performance audit (Lighthouse) | Developer | ☐ | Document baseline scores |
| 1.14 | Generate screenshot catalog of all pages | QA | ☐ | For visual regression baseline |

**Exit Criteria:** Complete inventory spreadsheet with all components cataloged.

---

## Phase 2: Duplicate Detection (Week 1-2)

| # | Task | Owner | Status | Notes |
|---|------|-------|--------|-------|
| 2.1 | Identify duplicate button styles | Architect | ☐ | List all unique button CSS classes, group by style |
| 2.2 | Identify duplicate form layouts | Architect | ☐ | Count unique form layouts used |
| 2.3 | Identify duplicate modal/dialog patterns | Architect | ☐ | Count unique modal implementations |
| 2.4 | Identify duplicate IG/IR toolbar configurations | Architect | ☐ | Count unique toolbar sets |
| 2.5 | Identify duplicate notification patterns | Architect | ☐ | List all toast/alert implementations |
| 2.6 | Identify duplicate JavaScript utility functions | Developer | ☐ | Grep for similar function patterns |
| 2.7 | Identify hardcoded color/typography/spacing values | Developer | ☐ | Grep for `color:`, `background:`, `font-size:`, `margin:`, `padding:` |
| 2.8 | Map duplicates to EODS Global Component | Architect | ☐ | Create mapping document |
| 2.9 | Score duplicates by: occurrence count × business impact | Architect | ☐ | Prioritize high-value merges |
| 2.10 | Present duplicate report to stakeholders | Architect | ☐ | Get sign-off on merge candidates |

**Exit Criteria:** Duplicate Report approved with merge priorities.

---

## Phase 3: Token Extraction (Week 2)

| # | Task | Owner | Status | Notes |
|---|------|-------|--------|-------|
| 3.1 | Extract all color values → design tokens | Developer | ☐ | Hex, RGB, HSL → mapped to `--color-*` tokens |
| 3.2 | Extract all font sizes → typography tokens | Developer | ☐ | Map to `--font-size-*` scale |
| 3.3 | Extract all spacing values → spacing tokens | Developer | ☐ | Map to `--space-*` scale |
| 3.4 | Extract all border-radii → radius tokens | Developer | ☐ | Map to `--radius-*` scale |
| 3.5 | Extract all shadow values → shadow tokens | Developer | ☐ | Map to `--shadow-*` scale |
| 3.6 | Extract all z-index values → z-index tokens | Developer | ☐ | Map to `--z-*` scale |
| 3.7 | Extract all breakpoint values → breakpoint tokens | Developer | ☐ | Consolidate to 3 breakpoints |
| 3.8 | Upload tokens.css to Shared Components → Static Files | Developer | ☐ | Under `css/eods/` folder |
| 3.9 | Verify tokens resolve correctly in browser dev tools | Developer | ☐ | Check computed styles panel |
| 3.10 | Create theme-dark.css with dark mode token overrides | Developer | ☐ | Verify contrast ratios in dark mode |

**Exit Criteria:** All hardcoded values in codebase mapped to tokens. Token CSS files uploaded and resolving correctly.

---

## Phase 4: Component Refactor (Week 2-3)

| # | Task | Owner | Status | Notes |
|---|------|-------|--------|-------|
| 4.1 | Create Global Button component CSS | Developer | ☐ | `buttons.css` uploaded |
| 4.2 | Create Global Form component CSS | Developer | ☐ | `forms.css` uploaded |
| 4.3 | Create Global Dialog component CSS | Developer | ☐ | `dialog.css` uploaded |
| 4.4 | Create Global Card component CSS | Developer | ☐ | `cards.css` uploaded |
| 4.5 | Create Global IG Standard CSS | Developer | ☐ | `grid.css` uploaded |
| 4.6 | Create Global Navigation CSS | Developer | ☐ | `navigation.css` uploaded |
| 4.7 | Create Dashboard CSS | Developer | ☐ | `dashboard.css` uploaded |
| 4.8 | Create Badge CSS | Developer | ☐ | `badge.css` uploaded |
| 4.9 | Create Utility CSS | Developer | ☐ | `utility.css` uploaded |
| 4.10 | Build one "reference page" showing all components | Developer | ☐ | Internal reference only |
| 4.11 | Conduct component review with team | Architect | ☐ | Verify naming, token usage, documentation |
| 4.12 | Run accessibility audit on reference page | Developer | ☐ | Minimum WCAG 2.1 AA compliance |

**Exit Criteria:** All component CSS files created, uploaded, and reviewed. Reference page passes accessibility audit.

---

## Phase 5: Global CSS Application (Week 3-4)

| # | Task | Owner | Status | Notes |
|---|------|-------|--------|-------|
| 5.1 | Upload global.css to Shared Components | Developer | ☐ | |
| 5.2 | Add global.css reference to Desktop UI File URLs | Developer | ☐ | `#WORKSPACE_FILES#eods/global.css` |
| 5.3 | Add global.css reference to Theme Roller Custom CSS | Developer | ☐ | Via `@import url(...)` |
| 5.4 | Verify all tokens/styles load correctly on a test page | Developer | ☐ | |
| 5.5 | Add utility classes to existing pages (spacing, text, display) | Developer | ☐ | Non-breaking additions only |
| 5.6 | Run visual regression comparison (Phase 1 screenshots vs. current) | QA | ☐ | Flag any unintended visual changes |
| 5.7 | Fix any unexpected styling conflicts | Developer | ☐ | Check specificity, namespace collisions |
| 5.8 | Verify dark mode toggle works | Developer | ☐ | Test all 3 modes: light, dark, auto |

**Exit Criteria:** Global CSS applied and verified. Visual regression passes on non-migrated pages.

---

## Phase 6: Global JavaScript Standardization (Week 4)

| # | Task | Owner | Status | Notes |
|---|------|-------|--------|-------|
| 6.1 | Upload apex-global.js to Shared Components | Developer | ☐ | Under `js/eods/` folder |
| 6.2 | Add apex-global.js reference to Desktop JS File URLs | Developer | ☐ | `#WORKSPACE_FILES#eods/apex-global.js` |
| 6.3 | Audit existing inline JS for jQuery dependency removal | Developer | ☐ | Replace `$()` with `document.querySelector()` |
| 6.4 | Replace custom AJAX wrappers with `eods.ajax.*` | Developer | ☐ | Per-page migration |
| 6.5 | Replace custom notification code with `eods.notify.*` | Developer | ☐ | Per-page migration |
| 6.6 | Replace custom modal code with `eods.modal.*` | Developer | ☐ | Per-page migration |
| 6.7 | Replace custom loading indicators with `eods.loading.*` | Developer | ☐ | Per-page migration |
| 6.8 | Add global error handler to all pages | Developer | ☐ | `eods.error.init()` already runs automatically |
| 6.9 | Test all migrated JS on each page | QA | ☐ | Functional test of affected interactions |

**Exit Criteria:** `apex-global.js` loaded on all pages. Custom JS utilities fully replaced.

---

## Phase 7: Page-by-Page Migration (Week 4-8)

| # | Task | Owner | Status | Notes |
|---|------|-------|--------|-------|
| 7.1 | Prioritize pages: High-traffic first, low-traffic last | Architect | ☐ | |
| 7.2 | Migrate Login Page → EODS styles | Developer | ☐ | |
| 7.3 | Migrate Dashboard Pages → `eods-dashboard` grid | Developer | ☐ | |
| 7.4 | Migrate Report Pages → `eods-ig` standard | Developer | ☐ | |
| 7.5 | Migrate Form Pages → `eods-form` standard | Developer | ☐ | |
| 7.6 | Migrate Button styles → `.eods-btn` classes | Developer | ☐ | Per page, replace old button CSS |
| 7.7 | Migrate Modal/Dialog pages → `eods-dialog` | Developer | ☐ | |
| 7.8 | Migrate Card regions → `eods-card` | Developer | ☐ | |
| 7.9 | Migrate Navigation → `eods-nav` | Developer | ☐ | |
| 7.10 | Migrate Wizard Pages | Developer | ☐ | |
| 7.11 | Migrate Breadcrumb regions | Developer | ☐ | |
| 7.12 | Full functional test of each migrated page | QA | ☐ | |
| 7.13 | Visual regression test of each migrated page | QA | ☐ | |
| 7.14 | Accessibility audit of each migrated page | QA | ☐ | |

**Exit Criteria:** All pages migrated. All tests passing.

---

## Phase 8: Testing (Week 8-9)

| # | Task | Owner | Status | Notes |
|---|------|-------|--------|-------|
| 8.1 | Cross-browser testing (Chrome, Firefox, Edge, Safari) | QA | ☐ | Latest 2 versions |
| 8.2 | Mobile responsive testing (<640px, 640-1024px) | QA | ☐ | Chrome DevTools device emulation |
| 8.3 | Tablet testing (iPad, Android tablet) | QA | ☐ | |
| 8.4 | Screen reader testing (NVDA/JAWS on Windows, VoiceOver on Mac) | QA | ☐ | |
| 8.5 | Keyboard-only navigation test | QA | ☐ | Tab through all interactive elements |
| 8.6 | WCAG 2.1 AA compliance scan | QA | ☐ | axe-core or Lighthouse |
| 8.7 | Color contrast verification (all token pairs) | QA | ☐ | Contrast ratio checker |
| 8.8 | Performance test (Lighthouse, PageSpeed) | QA | ☐ | Compare to Phase 1 baseline |
| 8.9 | Load test (if applicable — report pages, dashboards) | QA | ☐ | |
| 8.10 | Dark mode test (all pages, all components) | QA | ☐ | |
| 8.11 | Reduced motion test (`prefers-reduced-motion`) | QA | ☐ | |
| 8.12 | Print styles test (all report pages) | QA | ☐ | |

**Exit Criteria:** All test suites passing. No regressions from baseline.

---

## Phase 9: Performance (Week 9)

| # | Task | Owner | Status | Notes |
|---|------|-------|--------|-------|
| 9.1 | Audit CSS bundle size (`global.css` + all imports) | Developer | ☐ | Target <100KB minified |
| 9.2 | Audit JS bundle size (`apex-global.js`) | Developer | ☐ | Target <20KB minified |
| 9.3 | Minify CSS for production | Developer | ☐ | Use PostCSS or similar |
| 9.4 | Minify JS for production | Developer | ☐ | Use terser or similar |
| 9.5 | Implement critical CSS extraction (above-fold) | Developer | ☐ | |
| 9.6 | Defer non-critical CSS loading | Developer | ☐ | |
| 9.7 | Lazy load apex-global.js with `defer` attribute | Developer | ☐ | |
| 9.8 | Measure Time to Interactive (TTI) improvement | Developer | ☐ | Compare to Phase 1 baseline |
| 9.9 | Document performance results | Architect | ☐ | |
| 9.10 | Set up performance monitoring (if using APEX monitoring) | Admin | ☐ | |

**Exit Criteria:** Performance metrics equal to or better than Phase 1 baseline.

---

## Phase 10: Documentation & Handoff (Week 10)

| # | Task | Owner | Status | Notes |
|---|------|-------|--------|-------|
| 10.1 | Update team wiki with EODS documentation | Architect | ☐ | |
| 10.2 | Conduct developer training session (2 hours) | Architect | ☐ | |
| 10.3 | Create "Getting Started" guide for new developers | Architect | ☐ | |
| 10.4 | Create component usage examples (CodePen or similar) | Architect | ☐ | |
| 10.5 | Set up design token update process | Architect | ☐ | Who can change tokens, how, review process |
| 10.6 | Set up new component proposal process | Architect | ☐ | |
| 10.7 | Archive old CSS/JS files no longer referenced | Developer | ☐ | Remove from Shared Components |
| 10.8 | Update APEX build options to use EODS components | Developer | ☐ | |
| 10.9 | Announce rollout to stakeholders | Architect | ☐ | |

**Exit Criteria:** Team trained. Process documented. Old assets archived.

---

## Risk Mitigation During Migration

| Risk | Mitigation |
|------|-----------|
| Breaking existing pages | Apply global CSS non-destructively first. Migrate pages one at a time. |
| APEX upgrade during migration | Freeze APEX version during migration window. |
| Team unfamiliar with BEM/CSS variables | Conduct training before Phase 5. |
| Dark mode reveals accessibility issues | Test dark mode in Phase 3, not Phase 8. |
| Performance regression | Measure at every phase, not just at the end. |
