# EraOwl Design System Upgrade Strategy

> **Version:** 1.0.0 &nbsp;|&nbsp; **Current Target:** APEX 24.x &nbsp;|&nbsp; **Universal Theme:** Latest built-in

---

## 1. Guiding Principles

1. **APEX upgrades should not break EODS.** All custom CSS/JS is namespaced and isolated.
2. **Universal Theme updates are expected.** EODS extends — never replaces — Universal Theme.
3. **Test before you upgrade.** Every APEX version bump goes through the regression suite first.
4. **Rollback must be trivial.** Disabling EODS is a single line change (remove the `global.css` import).
5. **Stay current, but not bleeding-edge.** Target N-1 for production, N for development environments.

---

## 2. Universal Theme Version Tracking

| APEX Version | UT Version | EODS Compatible? | Notes |
|-------------|-----------|-----------------|-------|
| APEX 23.2 | UT 23.2 | Partial | Some template options may differ |
| APEX 24.1 | UT 24.1 | Yes | Baseline target |
| APEX 24.2 | UT 24.2 | Yes | Verified on release |
| APEX 25.x | UT 25.x | TBD | Test before upgrading |

### Version Detection

```javascript
// Detect APEX version at runtime
if (typeof apex !== 'undefined' && apex.version) {
  console.log('APEX Version:', apex.version);
}
```

```sql
-- Database-level APEX version check
SELECT VERSION_NO FROM APEX_RELEASE;
```

---

## 3. Deprecated Class & API Monitoring

### Oracle Resources to Monitor

| Resource | Frequency | Purpose |
|----------|-----------|---------|
| [APEX Release Notes](https://docs.oracle.com/en/database/oracle/apex/) | Per release | New features, breaking changes, deprecations |
| [APEX Known Issues](https://support.oracle.com/) | Monthly | Bug fixes, hot patches |
| Universal Theme CSS source | Per release | Class name changes, removed selectors |
| APEX JavaScript API Reference | Per release | Deprecated functions, new APIs |
| Oracle APEX Community (apex.world) | Weekly | Community-reported issues |

### Automated Deprecation Scanning

```javascript
// apex-global.js — optional deprecation warning module
(function() {
  var deprecated = {
    'apex.util.showMessage': 'Use eods.notify.show() instead',
    'apex.widget.report': 'Use eods.ig.* helpers instead',
  };

  // Override console.warn to catch APEX deprecation warnings
  var originalWarn = console.warn;
  console.warn = function(msg) {
    if (typeof msg === 'string' && msg.includes('deprecated')) {
      eods.error.handle(new Error('APEX deprecation: ' + msg), { source: 'apex' });
    }
    originalWarn.apply(console, arguments);
  };
})();
```

### Proactive CSS Monitoring

Run a comparison script after APEX upgrades:

```bash
# Compare UT CSS before and after upgrade
diff before-upgrade/ut-core.css after-upgrade/ut-core.css > ut-changes.diff

# Check for classes EODS targets
grep -n "\.a-IRR\b\|\.a-IG\b\|\.a-Button\b\|\.a-ModalDialog\b" ut-changes.diff
```

---

## 4. Custom Code Isolation Strategy

### CSS Isolation

All EODS CSS uses the `.eods-` prefix. No rule targets Oracle's `.a-*` or `.t-*` classes directly:

```css
/* CORRECT — own namespace */
.eods-btn--primary { background-color: var(--color-primary-500); }

/* WRONG — never do this */
.t-Button--hot { background-color: red; }  /* Overrides Universal Theme */
.a-IRR-reportTable { font-size: 12px; }    /* Breaks on UT update */
```

### JavaScript Isolation

```javascript
// CORRECT — own namespace
var eods = (function() { ... })();

// WRONG — never do this
apex.widget.report = function() { ... };  // Overrides APEX API
$.fn.extend({ ... });                     // Modifies jQuery prototype
```

### Custom APEX Template Option Isolation

When creating custom template options:
- Name them descriptively with a prefix: `EODS_CARD_ELEVATED`, `EODS_FORM_COMPACT`
- Reference them in component documentation
- Avoid naming collisions with future Oracle template options

---

## 5. Regression Test Suite

### Test Suite Components

| Layer | Tool | What it Tests |
|-------|------|--------------|
| Visual | Playwright + pixelmatch, or Percy, or Chromatic | Screenshot comparison before/after upgrade |
| Functional | Playwright / Cypress | Critical paths (login, CRUD, reports) |
| Accessibility | axe-core (automated), manual screen reader | WCAG 2.1 AA compliance |
| Performance | Lighthouse CI | TTI, FCP, LCP metrics |
| CSS | Custom script | Verify no direct `.a-*` or `.t-*` selectors in EODS CSS |
| Token | Custom script | Verify all tokens resolve to valid values |

### Minimum Test Cases

1. **Login page** — render, form validation, successful authentication
2. **Dashboard page** — all widgets render, metrics show data, charts load
3. **Interactive Report page** — filter, sort, paginate, export
4. **Interactive Grid page** — add row, edit cell, delete row, save
5. **Form page** — create record, validate, submit
6. **Form page** — edit record, change values, save
7. **Modal dialog** — open, submit, close, focus trap
8. **Navigation** — expand/collapse, mobile hamburger, breadcrumb
9. **Dark mode** — toggle, all components, forms, IG
10. **Print** — any report page printed output

### CI Pipeline

```yaml
# Example CI trigger
on:
  apex_upgrade:
    from_version: "24.1"
    to_version: "24.2"

steps:
  - name: Backup EODS
  - name: Apply APEX upgrade
  - name: Clear browser caches
  - name: Run visual regression suite
  - name: Run accessibility suite
  - name: Run performance suite
  - name: Report results
```

---

## 6. Staged Rollout Plan

### Environment Progression

```
Development (Week 1)
    → Feature/Component Testing
    → Dev team dogfooding
    → Automated test suite

Staging / UAT (Week 2)
    → Full application test suite
    → Business user acceptance testing
    → Performance benchmarking
    → Security review

Production (Week 3)
    → Blue/green deployment if available
    → Canary: 10% users → 50% → 100%
    → Monitor: errors, performance, user feedback
    → Rollback plan ready
```

### Feature Flags

For EODS migration (not APEX upgrades), use feature flags to control rollout:

```sql
-- APEX Application Item: AI_EODS_ENABLED
-- Value: Y (enabled) / N (disabled)
```

```html
<!-- Conditional CSS loading -->
{% if :AI_EODS_ENABLED = 'Y' %}
  <link rel="stylesheet" href="#WORKSPACE_FILES#eods/global.css">
{% endif %}
```

### Monitoring

| Metric | Tool | Threshold |
|--------|------|-----------|
| JavaScript errors | APEX debug, browser console | 0 new errors post-upgrade |
| Page load time | Lighthouse, APEX page timing | <5% degradation from baseline |
| 500 errors | APEX activity log, DB alert log | 0 increase |
| User-reported issues | Help desk tickets | <2 new issues in first week |

---

## 7. Rollback Procedures

### Quick Rollback (CSS only)

Remove the EODS CSS import from the application's Desktop User Interface → File URLs:

**Before:**
```
#WORKSPACE_FILES#eods/global.css
```

**After:**
```
(removed)
```

### Comprehensive Rollback (CSS + JS)

1. Remove `global.css` from File URLs.
2. Remove `apex-global.js` from File URLs.
3. Remove inline `<script>` for theme flash prevention from page template.
4. Clear application and browser cache.
5. Verify application renders correctly.

### Rollback Decision Matrix

| Condition | Action |
|-----------|--------|
| Visual regression on <5% of pages | Fix in next sprint, keep EODS |
| Visual regression on 5-20% of pages | Rollback EODS on affected pages only |
| Visual regression on >20% of pages | Full rollback |
| Functional breakage (any critical path) | Immediate full rollback |
| Performance degradation >10% | Investigate. If caused by bundle size, optimize. If structural, rollback. |
| Accessibility regression | Fix immediately or rollback |

---

## 8. APEX 24.x → Future Version Migration Path

### What Oracle Might Change

| Potential Change | EODS Impact | Mitigation |
|-----------------|-------------|-----------|
| New UT classes | None — EODS uses own classes | Verify no naming conflicts |
| Removed UT classes | None — EODS does not target `.a-*` | N/A |
| Changed template options | Components may need new mappings | Update 04-component-spec.md |
| New theme roller capabilities | May replace some EODS CSS | Evaluate and potentially deprecate redundant EODS rules |
| Deprecated JS APIs | `apex-global.js` may need updates | Abstract APEX API behind EODS facade |
| New region types (e.g., enhanced IG) | May need new EODS components | Extend, don't replace |
| Native dark mode in UT | May reduce need for EODS dark mode tokens | Migrate to native if complete; keep EODS if partial |
| CSS `@layer` support in UT | May affect specificity order | Adjust EODS layer ordering |

### Preparation Checklist for Next Major APEX Version

1. Review release notes for all changes.
2. Diff Universal Theme CSS for class name changes.
3. Test regression suite on new version.
4. Update EODS compatibility matrix.
5. Check for newly deprecated APIs.
6. Update EODS JavaScript if APEX APIs changed.
7. Verify dark mode tokens still apply correctly.
8. Test with new APEX templates and template options.
9. Update documentation (component spec, migration checklist).
10. Train developers on new APEX features that affect EODS.

---

## 9. Upgrade Governance

| Role | Responsibility |
|------|---------------|
| **Design System Architect** | Owns EODS codebase. Approves changes. Manages versioning. |
| **APEX Administrator** | Manages APEX environment upgrades. Coordinates with DBA. |
| **QA Lead** | Maintains regression test suite. Runs upgrade tests. Reports results. |
| **Lead Developer** | Reviews upgrade impact on custom code. Implements fixes. |

### Upgrade Decision Process

```
APEX New Version Available
    ↓
Review Release Notes (Architect)
    ↓
Evaluate Breaking Changes (Architect + Lead Dev)
    ↓
    ├── No breaking changes → Proceed to staging
    └── Breaking changes → Estimate fix effort
        ├── <1 week → Fix + proceed
        └── >1 week → Schedule for next sprint
    ↓
Deploy to staging → Run regression suite
    ↓
    ├── All tests pass → Deploy to production (staged)
    └── Tests fail → Fix → Re-test → Deploy
```
