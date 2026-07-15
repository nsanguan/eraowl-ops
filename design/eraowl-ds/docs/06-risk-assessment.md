# Risk Assessment — EraOwl Design System

> **Version:** 1.0.0 &nbsp;|&nbsp; **Date:** 2026-07-14

---

## Risk Matrix Legend

| Severity | Definition |
|----------|-----------|
| **Critical** | Application breaks. Users cannot perform core functions. |
| **High** | Major visual/functional regression. Requires immediate rollback. |
| **Medium** | Minor regression. Cosmetic issues. Can be fixed in next sprint. |
| **Low** | Edge cases only. Acceptable risk. |

| Likelihood | Definition |
|-----------|-----------|
| **Certain** | Will happen on every installation. |
| **Likely** | Will happen in most installations. |
| **Possible** | May happen under specific conditions. |
| **Unlikely** | Rare edge case, but theoretically possible. |
| **Rare** | Extremely unlikely, requires multiple conditions. |

---

## Risk 1: Universal Theme Upgrade Compatibility

| Attribute | Value |
|-----------|-------|
| **Severity** | Critical |
| **Likelihood** | Likely |
| **Description** | Oracle periodically updates Universal Theme CSS classes and template options. The EODS design system extends Universal Theme — if Oracle changes a class name, removes a template option, or alters the DOM structure that EODS targets, components may break. |
| **Affected Components** | All. Universal Theme is the foundation. |
| **Mitigation** | 1. EODS classes are prefixed with `.eods-` — no direct override of Oracle's `.a-*` classes. 2. Use design tokens (CSS custom properties) instead of overriding Universal Theme directly. 3. Test every APEX patch on dev before applying to prod. 4. Subscribe to Oracle APEX Known Issues and Release Notes. 5. Maintain a compatibility matrix of tested APEX versions. |
| **Detection** | Visual regression tests on APEX upgrade. |
| **Contingency** | If a Universal Theme change breaks EODS, temporarily disable the EODS global.css import until a fix is deployed. |

---

## Risk 2: Custom Template Option Conflicts

| Attribute | Value |
|-----------|-------|
| **Severity** | High |
| **Likelihood** | Possible |
| **Description** | Existing pages may have custom template options that conflict with EODS component defaults. For example, a region set to "Remove Body Padding" may not visually match the EODS card component that expects padding. |
| **Affected Components** | Cards, Forms, IG, Regions |
| **Mitigation** | 1. Audit all template options in Phase 1. 2. Document known conflicts and resolution paths. 3. Apply EODS classes only where template options allow. 4. Use `!important` sparingly and only for utility overrides. 5. Test each template option combination. |
| **Detection** | Visual inspection during migration. Automated screenshot comparison. |
| **Contingency** | Per-page exclusion of EODS styles using template option overrides. |

---

## Risk 3: JavaScript Namespace Collisions

| Attribute | Value |
|-----------|-------|
| **Severity** | High |
| **Likelihood** | Unlikely |
| **Description** | The global `eods` namespace may conflict with existing application JavaScript. This is unlikely given the unique prefix, but possible if the application also uses "eods" as a variable name. |
| **Affected Components** | All JS: modal, notify, ajax, ig, validation, theme |
| **Mitigation** | 1. The `eods` namespace is scoped within an IIFE. 2. Check for existing `eods` references in the codebase before deploying. 3. AMD support — the module doesn't pollute global scope in AMD environments. 4. Use `Object.freeze()` on the public API in production. |
| **Detection** | Grep codebase for `eods` before deployment. Browser console check. |
| **Contingency** | The namespace can be changed by updating the `EODS_NS` variable in the source. |

---

## Risk 4: CSS Specificity Wars

| Attribute | Value |
|-----------|-------|
| **Severity** | Medium |
| **Likelihood** | Likely |
| **Description** | Universal Theme uses high-specificity selectors (nested `.t-*` and `.a-*` classes). If EODS classes have lower specificity, they won't override Universal Theme. If they have higher specificity, they may be difficult to override later. |
| **Affected Components** | All CSS components |
| **Mitigation** | 1. EODS uses BEM methodology with flat specificity (0,1,0 for single class). 2. Use `:where()` pseudo-class for zero-specificity variants where appropriate. 3. Never use ID selectors. 4. Limit nesting depth to 2 levels. 5. Use CSS layers (`@layer eods`) for explicit priority control in browsers that support it. 6. Utility classes include `!important` intentionally. 7. Component modifiers use single-class selectors. |
| **Detection** | CSS specificity analyzer tool. Browser DevTools "Styles" tab inspection. |
| **Contingency** | Targeted specificity adjustments per component using `@layer` or scoping. |

---

## Risk 5: Browser Compatibility

| Attribute | Value |
|-----------|-------|
| **Severity** | Medium |
| **Likelihood** | Possible |
| **Description** | CSS custom properties (`var()`) are not supported in Internet Explorer 11 or very old browsers. The EODS design system requires modern browser features. |
| **Affected Components** | All CSS and JS |
| **Mitigation** | 1. Document minimum browser requirements clearly. 2. Oracle APEX 24.x itself requires modern browsers, so this is aligned. 3. Provide a fallback stylesheet for critical paths (login page) using PostCSS processing. 4. Use `@supports` queries for progressive enhancement. |

### Browser Compatibility Matrix

| Browser | Min Version | CSS Custom Properties | Grid | Flexbox | ES2020 |
|---------|------------|----------------------|------|---------|--------|
| Chrome | 90+ | ✓ | ✓ | ✓ | ✓ |
| Firefox | 90+ | ✓ | ✓ | ✓ | ✓ |
| Edge | 90+ | ✓ | ✓ | ✓ | ✓ |
| Safari | 14+ | ✓ | ✓ | ✓ | Partial |
| Safari iOS | 14+ | ✓ | ✓ | ✓ | Partial |
| Chrome Android | 90+ | ✓ | ✓ | ✓ | ✓ |
| Samsung Internet | 14+ | ✓ | ✓ | ✓ | ✓ |
| IE 11 | N/A | ✗ | ✗ (partial) | ✓ | ✗ |

| **Detection** | Cross-browser testing suite (BrowserStack, LambdaTest, or Playwright). |
| **Contingency** | If IE11 support is required, use a PostCSS plugin to compile custom properties to static values. This adds build complexity. |

---

## Risk 6: Dark Mode Edge Cases

| Attribute | Value |
|-----------|-------|
| **Severity** | Medium |
| **Likelihood** | Possible |
| **Description** | Dark mode may reveal hardcoded colors in legacy APEX components that were invisible in light mode. Third-party plugins may not respect dark mode. Images and logos may not have dark mode variants. |
| **Affected Components** | All visual components, Plugins, Custom regions |
| **Mitigation** | 1. Audit all plugins and third-party components in dark mode. 2. Use `color-scheme: dark` on `html` for native form control styling. 3. Provide CSS filters for images: `img { filter: brightness(0.9); }` in dark mode. 4. Allow per-user opt-out via the theme toggle. 5. Test all Oracle JET charts in dark mode (Oracle JET supports themes). |
| **Detection** | Manual dark mode testing on every page. Automated visual regression in dark mode. |
| **Contingency** | Per-component dark mode exclusions using `:not([data-theme='dark'])` selectors for problematic components. |

---

## Risk 7: Performance Regression

| Attribute | Value |
|-----------|-------|
| **Severity** | Medium |
| **Likelihood** | Possible |
| **Description** | Adding 11+ CSS files and a JS utility library increases the total bytes delivered to the client. If not optimized, this could increase page load time and degrade user experience. |
| **Affected Components** | All (global impact) |
| **Mitigation** | 1. Use `@import` only in development; bundle all CSS into a single minified file for production. 2. Use critical CSS extraction for above-fold content. 3. Defer non-critical CSS and JS. 4. Use `link rel="preload"` for fonts. 5. Lazy-load `apex-global.js` with `defer` attribute. 6. Measure TTI, FCP, LCP before and after. Target <5% regression. 7. Use HTTP/2 server push or HTTP/3 for parallel resource loading. |
| **Detection** | Lighthouse CI in deployment pipeline. RUM (Real User Monitoring) via APEX instrumentation. |
| **Contingency** | Remove non-essential CSS modules if performance degrades beyond threshold. |

---

## Risk 8: Developer Adoption Barriers

| Attribute | Value |
|-----------|-------|
| **Severity** | Medium |
| **Likelihood** | Likely |
| **Description** | Developers accustomed to inline styles, arbitrary class names, and copy-paste component patterns may resist adopting the design system. Learning BEM methodology, design tokens, and the EODS JavaScript API takes time. |
| **Affected Components** | Process/People (not technical) |
| **Mitigation** | 1. Provide training sessions before rollout. 2. Create cheat sheets and quick-reference documentation. 3. Set up linting rules that flag direct Universal Theme class overrides. 4. Add design token autocomplete to IDE via CSS variable definitions. 5. Start with non-breaking changes (utility classes, design tokens). 6. Appoint a design system champion on each development team. 7. Use code review to enforce EODS adoption. |
| **Detection** | Code review metrics. CSS class audit reports. |
| **Contingency** | Phased rollout — allow legacy patterns during transition period. |

---

## Risk 9: Testing Coverage Gaps

| Attribute | Value |
|-----------|-------|
| **Severity** | Medium |
| **Likelihood** | Likely |
| **Description** | APEX applications are notoriously difficult to automate-test. The combination of dynamic DOM generation, PL/SQL server-side logic, and session state management means that CSS/JS changes may break functionality in ways that are hard to detect without manual testing. |
| **Affected Components** | All |
| **Mitigation** | 1. Maintain a visual regression baseline with screenshot comparisons. 2. Use Playwright or Cypress for critical path automation (login, form submission, report generation). 3. Implement APEX automation testing with tools like APEX Nitro or utPLSQL. 4. Test on real mobile devices, not just emulators. 5. Include keyboard-navigation and screen-reader tests in CI. 6. Create a test checklist per page type (form, report, dashboard, modal). |
| **Detection** | Automated test suite failures. Manual QA findings. |
| **Contingency** | Per-page rollback capability. Feature flags to enable/disable EODS on specific pages. |

---

## Risk 10: APEX Plugin Incompatibility

| Attribute | Value |
|-----------|-------|
| **Severity** | Medium |
| **Likelihood** | Possible |
| **Description** | Third-party APEX plugins (regions, items, dynamic actions) may have their own CSS/JS that conflicts with EODS styling. Plugin authors may use fixed CSS values or target specific Universal Theme selectors that EODS overrides. |
| **Affected Components** | Plug-ins |
| **Mitigation** | 1. Inventory all plugins in use during Phase 1. 2. Test each plugin with EODS enabled. 3. Contact plugin authors about EODS compatibility. 4. Scope EODS styles to non-plugin regions using `:not()` or scoping. 5. Consider replacing problematic plugins with native APEX components. |
| **Detection** | Plugin-by-plugin manual testing. |
| **Contingency** | Plugin-scoped CSS resets to isolate plugin styling from EODS. |

---

## Summary

| Risk # | Risk Name | Severity | Likelihood | Overall |
|--------|-----------|----------|-----------|---------|
| 1 | UT Upgrade Compatibility | Critical | Likely | **Critical** |
| 2 | Template Option Conflicts | High | Possible | **High** |
| 3 | JS Namespace Collisions | High | Unlikely | Medium |
| 4 | CSS Specificity Wars | Medium | Likely | Medium |
| 5 | Browser Compatibility | Medium | Possible | Medium |
| 6 | Dark Mode Edge Cases | Medium | Possible | Medium |
| 7 | Performance Regression | Medium | Possible | Medium |
| 8 | Developer Adoption | Medium | Likely | Medium |
| 9 | Testing Coverage Gaps | Medium | Likely | Medium |
| 10 | Plugin Incompatibility | Medium | Possible | Low-Medium |

**Overall Risk Level:** Medium. The design system is built with isolation as a core principle (prefixed classes, BEM naming, no jQuery dependency, no direct Universal Theme overrides). The primary risk is Universal Theme changes from Oracle, mitigated by isolation and testing discipline.
