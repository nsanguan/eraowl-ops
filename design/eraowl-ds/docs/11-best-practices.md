# EraOwl Design System — Best Practices

> **Version:** 1.0.0 &nbsp;|&nbsp; **Target:** Oracle APEX 24.x + EODS

---

## 1. Design & Architecture

### 1.1 Always Prefer Declarative Over Programmatic

| Do This | Not This |
|---------|----------|
| Use APEX template options to control component appearance | Write custom CSS overriding `.t-Button` |
| Use server-side conditions (`Type = SQL Expression`) for visibility | Write JavaScript to show/hide elements in Dynamic Actions |
| Use APEX validations for form field validation | Write custom JavaScript `if (value === '')` |
| Use APEX process types for data modifications | Write PL/SQL in Dynamic Actions for CRUD |

**Rationale:** Declarative features survive APEX upgrades. Custom code must be maintained and re-tested on every upgrade.

### 1.2 Use Template Options Before Custom CSS

Priority order for styling:
1. APEX Template Options (built-in)
2. EODS utility classes (`.eods-mt-4`, `.eods-text-center`)
3. EODS component classes (`.eods-btn--primary`, `.eods-card--elevated`)
4. Custom CSS (last resort, only if none of the above work)

### 1.3 Never Modify Oracle's CSS Directly

| Rule | Example |
|------|---------|
| Never edit `ut-core.css` or any Universal Theme file | Files get overwritten on APEX upgrade |
| Never use `.t-*` or `.a-*` selectors in custom CSS | Oracle may change these at any time |
| Never use `apex.` namespace for custom functions | Your function may collide with future APEX APIs |
| Always prefix custom CSS classes with `.eods-` | Clear ownership and zero collision risk |

### 1.4 One Page, One Purpose

A page should do one thing well:
- **Report page:** Query + display data. Add filters, but don't embed forms.
- **Form page:** Create or edit one record. Don't add reports on the same page.
- **Dashboard page:** Display KPIs, charts, cards. Actions navigate away.
- **Modal page:** Single interaction (confirm, quick edit, lookup).

**Exception:** Master-detail pages (master report + detail form) are acceptable and well-supported.

---

## 2. Performance

### 2.1 Minimize Page Items Per Page

| Threshold | Action |
|-----------|--------|
| <50 items | Acceptable, no action needed |
| 50-100 items | Review. Merge redundant items. Use computations instead of hidden items. |
| >100 items | Refactor. Page too complex. Split into multiple pages or use tabbed regions. |

**APEX limitation:** Every page item consumes server-side session state. 100+ items = measurable performance impact.

### 2.2 Use Dynamic Actions Sparingly

| DA Count | Concern |
|----------|---------|
| <10 per page | Normal |
| 10-20 per page | Review for redundancy |
| >20 per page | Refactor — too much client-side logic |

**Replace DAs with:**
- Server-side conditions (for visibility)
- Computations (for derived values)
- Page processes (for multi-step logic)
- PL/SQL callbacks (for complex data operations)

### 2.3 Use Lazy Loading for Regions

For pages with many regions, use APEX lazy loading:
- Set region `Lazy Loading` attribute to `Yes`
- Region content loads asynchronously after the page
- Especially important for dashboards with many chart regions

### 2.4 Optimize Interactive Reports and Grids

| Optimization | How |
|-------------|-----|
| Limit initial rows | Set `Maximum Rows Per Page` to 25 (default) or 50 |
| Use pagination | Never load entire dataset. Always paginate. |
| Index query columns | Every filtered, sorted, or searched column should have a database index |
| Avoid `SELECT *` | Only select columns needed for the report |
| Use `WHERE` clause for pre-filtering | Don't load 100K rows and filter client-side |
| Use Classic Report for simple lists | IR/IG adds overhead. For simple read-only lists, Classic Report is faster. |

### 2.5 Critical CSS Strategy

For above-fold content (dashboard, login page), inline critical CSS:

```html
<style>
  /* Critical CSS: only styles needed for above-fold content */
  .eods-login { ... }
  .eods-dashboard__header { ... }
</style>
<link rel="preload" href="#WORKSPACE_FILES#eods/global.css" as="style" onload="this.rel='stylesheet'">
```

---

## 3. Security

### 3.1 Authorization at Component Level

| Level | Best Practice |
|-------|--------------|
| Page | Authorization scheme on page (coarse-grained) |
| Region | Authorization scheme on region (e.g., admin-only chart) |
| Button | Authorization scheme on button (e.g., delete button for managers only) |
| Column | Authorization on IG column (e.g., hide salary column for non-HR) |
| Process | Authorization on process (prevent direct URL access to sensitive operations) |

**Never rely on hidden UI elements as security.** Authorize at the server level.

### 3.2 Use APEX Session State Protection

Enable Session State Protection for all pages. This prevents:
- URL tampering (changing item values in the URL)
- CSRF attacks (cross-site request forgery)
- Direct page access bypassing authentication

### 3.3 Escape Output in Reports

When using HTML Expression in reports, always escape user-provided data:

```sql
-- WRONG — XSS vulnerability
SELECT '<a href="' || user_url || '">' || username || '</a>' AS link FROM users;

-- CORRECT — escaped
SELECT '<a href="' || apex_escape.html(user_url) || '">' || apex_escape.html(username) || '</a>' AS link FROM users;
```

### 3.4 Use Bind Variables (Always)

```sql
-- WRONG — SQL injection risk, no plan reuse
SELECT * FROM employees WHERE department_id = ' || :P1_DEPT_ID || ';

-- CORRECT — bind variable
SELECT * FROM employees WHERE department_id = :P1_DEPT_ID;
```

---

## 4. Shared Components

### 4.1 One LOV Per Business Entity

Create one List of Values for each business concept and reuse it everywhere:

| LOV Name | Where Used |
|----------|-----------|
| `LOV_DEPARTMENTS` | Employee form, Department report filter, Budget form |
| `LOV_STATUS_CODES` | Employee form, Project form, Task form |
| `LOV_COUNTRIES` | Address form, Supplier form, Customer form |

**Anti-pattern:** Creating `P1_DEPT_LOV`, `P2_DEPT_LOV`, `P12_DEPT_LOV` that all query the same table with slightly different SQL.

### 4.2 Use Authorization Schemes Centrally

| Scheme Name | Type | Logic |
|------------|------|-------|
| `AUTH_IS_ADMIN` | Exists SQL | `SELECT 1 FROM user_roles WHERE role = 'ADMIN'` |
| `AUTH_IS_MANAGER` | Exists SQL | `SELECT 1 FROM employees WHERE user_id = :APP_USER AND job_id = 'MANAGER'` |
| `AUTH_CAN_APPROVE` | PL/SQL Function | `RETURN approval_pkg.can_approve(:APP_USER);` |

**Reference these schemes everywhere** — page authorization, region authorization, button authorization, process authorization.

### 4.3 Use Lists for Navigation (Not Hardcoded Links)

All navigation menus should be Shared Components → Lists:
- APEX automatically highlights the active page
- Lists support authorization (auto-hide unauthorized menu items)
- Lists support build options
- Lists render correctly on mobile and desktop
- Lists can be dynamic (SQL-based) for role-aware menus

### 4.4 Use Build Options for Feature Toggles

Create build options for:
- Features under development (`BUILD_FEATURE_NEW_DASHBOARD`)
- Admin-only features (`BUILD_ADMIN_TOOLS`)
- Optional integrations (`BUILD_PAYROLL_INTEGRATION`)

Apply build options to regions, items, buttons, and list entries. This is APEX's native feature flag system.

### 4.5 Use Component Settings for Defaults

Shared Components → Component Settings let you set application-wide defaults:
- Default report pagination
- Default date format
- Default chart colors
- Default form template

Set these once. Don't configure per-component unless you need an override.

---

## 5. Development Workflow

### 5.1 Use APEX_DEBUG for Logging

```plsql
-- In processes and validations
apex_debug.info('Processing employee ID: %s', :P1_EMP_ID);
apex_debug.error('Failed to validate: %s', SQLERRM);
```

**Never use `DBMS_OUTPUT`** — it's not captured in APEX runtime. **Never use `console.log`** in production JavaScript — use `eods.error.handle()` which integrates with APEX debug.

### 5.2 Use Page Zero for Global Components

Page Zero (page 0) renders on every page. Use it for:
- Global notification region
- Global loading indicator
- Session timeout warning
- Global error display
- Global footer/help link

### 5.3 Version Control for APEX Applications

Export your application regularly and store in Git:

```bash
# Export application to split files (one per page)
sqlcl /nolog <<EOF
  connect myuser/mypass@mydb
  apex export -applicationid 100 -split
EOF

# Commit to Git
git add f100/
git commit -m "APEX app 100: Added employee dashboard"
```

### 5.4 Use Application Aliases

Never hardcode application IDs in code:

```plsql
-- WRONG
apex_page.get_url(p_page => 10, p_app => 100);

-- CORRECT
apex_page.get_url(p_page => 'employees', p_app => 'HR_APP');
```

Set Application Alias in Shared Components → Application Definition.

---

## 6. CSS & JavaScript

### 6.1 Use EODS Classes, Not Inline Styles

```html
<!-- WRONG -->
<div style="margin-top: 16px; color: red; font-size: 14px;">

<!-- CORRECT -->
<div class="eods-mt-4 eods-text-danger eods-text-sm">
```

### 6.2 Use EODS JavaScript API

```javascript
// WRONG — jQuery dependency, fragile
$('#myModal').modal('show');
$.ajax({ url: '...', success: function() { alert('Done'); } });

// CORRECT — vanilla JS, EODS namespace
eods.modal.open('myModal');
eods.ajax.post('MY_CALLBACK', { p_id: 123 })
  .then(() => eods.notify.success('Done'));
```

### 6.3 Scope JavaScript to Page or Region

```javascript
// Use APEX namespacing to avoid global scope pollution
// Page-level JS
var apex_page_10 = {
  init: function() { ... },
  refreshReport: function() { ... }
};

// OR use EODS event system
document.addEventListener('eods:page:ready', function(e) {
  if (e.detail.pageId === '10') {
    eods.notify.info('Employee list loaded');
  }
});
```

### 6.4 File Organization

```
Shared Components / Static Workspace Files
├── css/
│   └── eods/          ← EODS design system CSS files
├── js/
│   └── eods/          ← EODS JavaScript
└── app/
    ├── css/           ← Application-specific CSS (rare)
    └── js/            ← Page-specific JavaScript
```

---

## 7. Forms & Validation

### 7.1 Server-Side Validation Always

Client-side validation (`eods.validation.*`) is for UX convenience only. Always pair it with server-side APEX validations.

```plsql
-- APEX Validation: P1_EMAIL must be valid
IF NOT REGEXP_LIKE(:P1_EMAIL, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$') THEN
  RETURN 'Please enter a valid email address.';
END IF;
```

### 7.2 Use Page Processes (Not Dynamic Actions) for DML

```plsql
-- WRONG — Dynamic Action executes PL/SQL
BEGIN
  INSERT INTO employees (...) VALUES (...);
END;

-- CORRECT — Page Process (Automated Row Processing or custom PL/SQL)
-- Defined in Processing → Processes
BEGIN
  INSERT INTO employees (...) VALUES (:P1_NAME, :P1_EMAIL, ...);
END;
```

### 7.3 Use Fetch Process for AJAX

For AJAX callbacks, use `apex_session.create_session` on the server side:

```plsql
-- Application Process: MY_LOOKUP
DECLARE
  l_result CLOB;
BEGIN
  -- Server-side validation and authorization here
  SELECT JSON_ARRAYAGG(JSON_OBJECT(...)) INTO l_result FROM ...
  WHERE department_id = :p_dept_id;

  apex_json.open_object;
  apex_json.write('data', l_result);
  apex_json.close_object;
END;
```

```javascript
// Client-side
eods.ajax.post('MY_LOOKUP', { p_dept_id: 42 })
  .then(function(result) {
    console.log(result.data);
  });
```

---

## 8. Testing

### 8.1 Test Every Template Option Combination

For each component, test at minimum:
- Light mode + dark mode
- Mobile + desktop breakpoints
- Default state + loading state + error state + empty state
- Keyboard navigation only
- Screen reader

### 8.2 Visual Regression for Every APEX Upgrade

Run screenshot comparison between:
- Current production (previous APEX version)
- New staging (upgraded APEX version, same application)

Flag any difference >1% pixel change.

### 8.3 Performance Budget

| Metric | Budget |
|--------|--------|
| Total CSS (all imports, gzipped) | <50KB |
| Total JS (all imports, gzipped) | <20KB |
| First Contentful Paint | <1.5s |
| Largest Contentful Paint | <2.5s |
| Time to Interactive | <3.5s |
| Cumulative Layout Shift | <0.1 |

---

## 9. Documentation

### 9.1 Document Template Options Per Component

For every page, document in page comments:
- Which template options are used on each region
- Why a particular template option was chosen
- Which EODS classes supplement the template options

### 9.2 Document DA Dependencies

Dynamic Actions create invisible dependencies. Document:
- Which DA triggers which elements
- What server-side callbacks are invoked
- Any chained DAs (DA that triggers another DA)

---

## 10. Governance

### 10.1 Review Checklist for New Pages

Before deploying a new page, verify:
- [ ] Uses Shared Component LOVs (no one-off LOVs)
- [ ] Uses EODS CSS classes (no inline styles)
- [ ] Uses EODS JavaScript API (no raw jQuery/vanilla JS for notifications, modals, AJAX)
- [ ] Authorization on every region and process
- [ ] Session state protection enabled
- [ ] Bind variables used in all SQL
- [ ] HTML expressions escaped (`apex_escape.html()`)
- [ ] Page items <50 (justify if >50)
- [ ] Dynamic actions <10 (justify if >10)
- [ ] Accessible: labels on all inputs, alt text on images, ARIA on custom widgets
- [ ] Dark mode: tested with `data-theme="dark"`
- [ ] Responsive: tested at 375px and 1920px
- [ ] Print: tested print output for report pages

### 10.2 EODS Design Token Change Process

1. Propose change in the design system repository with rationale.
2. Review contrast ratios for both light and dark mode.
3. Check all components that use the token for regressions.
4. Update `docs/03-design-tokens.md` documentation.
5. Deploy tokens.css to all environments.
6. Run visual regression suite.
7. Announce change to development team.

### 10.3 New Component Proposal Process

1. Developer identifies a pattern used on 3+ pages that doesn't have a global component.
2. Propose component spec (properties, variants, template).
3. Design System Architect reviews against existing components for overlap.
4. Create component CSS + documentation.
5. Add to `01-inventory.md` and `04-component-spec.md`.
6. Create reference example page.
7. Announce to team.
8. Migrate existing instances to use new component.

---

## Summary: The Golden Rules

1. **Declarative first.** Template options, conditions, LOVs before custom code.
2. **Shared Components for reusability.** LOVs, lists, auth schemes, build options.
3. **EODS for styling.** Never inline styles. Never modify Universal Theme.
4. **Server-side validation always.** Client-side JS validation is UX only.
5. **Bind variables always.** Never concatenate values into SQL.
6. **Authorization everywhere.** Page, region, button, process, column.
7. **One LOV per entity.** Reuse across the entire application.
8. **Page Zero for global components.** Notifications, loading, footers.
9. **Test in dark mode.** Every page, every component, every time.
10. **Document as you build.** Template options, DA chains, component choices.
