# Responsive Design Strategy — EraOwl Design System

> **Version:** 1.0.0 &nbsp;|&nbsp; **Approach:** Mobile-First, Fluid Layouts, Component-Level Breakpoints

---

## 1. Breakpoints

EODS uses three primary breakpoints, defined as design tokens:

```css
--breakpoint-sm: 640px;   /* Mobile landscape, small tablets */
--breakpoint-md: 1024px;  /* Tablets, small desktops */
--breakpoint-lg: 1280px;  /* Large desktops */
--breakpoint-xl: 1536px;  /* Extra large displays */
```

| Name | Min Width | Max Width | Primary Devices |
|------|-----------|-----------|----------------|
| `xs` (base) | 0px | 639px | Mobile phones (portrait) |
| `sm` | 640px | 1023px | Mobile phones (landscape), tablets (portrait) |
| `md` | 1024px | 1279px | Tablets (landscape), small laptops |
| `lg` | 1280px | 1535px | Desktop monitors |
| `xl` | 1536px | ∞ | Large desktop, 1440p+ |

**Approach:** Mobile-first CSS. Base styles target the smallest screens, and `min-width` media queries progressively enhance for larger screens. No `max-width` queries for layout (only for specific responsive overrides within components).

---

## 2. Grid System

### 12-Column CSS Grid

```css
.eods-container {
  width: 100%;
  max-width: var(--container-max-width); /* 1280px */
  margin: 0 auto;
  padding: 0 var(--space-4); /* 16px gutters on mobile */
}

@media (min-width: 640px) {
  .eods-container {
    padding: 0 var(--space-6); /* 24px gutters on tablet+ */
  }
}
```

### Responsive Card Grid

```css
/* Auto-fill: cards adapt automatically */
.eods-card-grid--responsive {
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
}
```

This single rule handles all breakpoints without media queries — cards flow from 1 column (mobile) to 2 (tablet) to 3-4 (desktop) automatically.

### Dashboard Grid

| Breakpoint | Behavior |
|------------|----------|
| <640px | 1 column, stacked |
| 640-1023px | 2 columns |
| 1024-1279px | 3 columns |
| 1280px+ | Configured column count (2-4) |

---

## 3. Component Responsive Behavior

### Forms

| Breakpoint | Behavior |
|------------|----------|
| <640px | 1 column, labels on top, full-width controls |
| 640px+ | `--cols-2` or `--cols-3` layout, labels on top (default) |
| 1024px+ | `--label-left` layout available, multi-column layouts |

```css
@media (max-width: 640px) {
  .eods-form--cols-2,
  .eods-form--cols-3,
  .eods-form--cols-4,
  .eods-form--responsive {
    grid-template-columns: 1fr;
  }

  .eods-form--label-left .eods-form__group {
    grid-template-columns: 1fr;
  }
}
```

### Interactive Grid / Tables

| Breakpoint | Behavior |
|------------|----------|
| <640px | Horizontal scroll on table. Compact pagination. Toolbar stacks vertically. |
| 640px+ | Full-width table. Standard pagination. Inline toolbar. |

```css
@media (max-width: 640px) {
  .eods-ig__toolbar {
    flex-direction: column;
    align-items: stretch;
  }

  .eods-ig__pagination {
    flex-direction: column;
    align-items: center;
  }
}
```

### Navigation

| Breakpoint | Behavior |
|------------|----------|
| <1024px | Side nav hidden. Hamburger menu visible. Drawer for nav. Bottom tab bar (optional). |
| 1024px+ | Side nav (default) or top nav visible. Hamburger hidden. |

```css
@media (max-width: 1024px) {
  .eods-nav--side {
    display: none;
  }

  .eods-nav__hamburger {
    display: flex;
  }
}
```

### Modal Dialogs

| Breakpoint | Behavior |
|------------|----------|
| <640px | Full-width, slides up from bottom (mobile sheet style). |
| 640px+ | Centered, fixed width (sm/md/lg/xl). |

```css
@media (max-width: 640px) {
  .eods-dialog {
    width: 100vw;
    max-width: 100vw;
    bottom: 0;
    top: auto;
    left: 0;
    transform: translateY(100%);
    border-radius: var(--eods-dialog-radius) var(--eods-dialog-radius) 0 0;
  }

  .eods-dialog--visible {
    transform: translateY(0);
  }
}
```

### Cards

| Breakpoint | Behavior |
|------------|----------|
| <640px | 1 column, stacked. Horizontal cards become vertical. |
| 640-1023px | 2 columns. |
| 1024px+ | 3-4 columns depending on container configuration. |

### Dashboard

| Breakpoint | Behavior |
|------------|----------|
| <640px | 1 column. KPI row becomes 1-2 columns. Quick actions 2 per row. |
| 640-1023px | 2 columns. KPI row 2 columns. |
| 1024-1279px | 3 columns. |
| 1280px+ | 4 columns or custom layout. |

---

## 4. Typography Scaling

Typography uses `rem` units for all sizes, enabling consistent browser zoom behavior (WCAG 1.4.4 compliance).

```css
/* Base: 16px = 1rem */
html { font-size: 16px; }

/* All font sizes in rem */
--font-size-xs: 0.75rem;    /* 12px */
--font-size-sm: 0.875rem;   /* 14px */
--font-size-base: 1rem;     /* 16px */
```

No viewport-unit (`vw`) font sizes used, to preserve user zoom control. Headings use absolute `rem` sizes, not fluid scaling, for predictability.

---

## 5. Touch vs. Mouse Interaction

| Concern | Implementation |
|---------|---------------|
| Touch targets | Primary interactive elements ≥44×44px (md buttons: 40×40px, lg: 48×48px). Switch track: 44×24px. |
| Hover states | Wrapped in `@media (hover: hover)` to avoid sticky hover on touch devices. |
| Tap highlight | `-webkit-tap-highlight-color: transparent` for custom-styled elements (optional). |
| Touch scrolling | `-webkit-overflow-scrolling: touch` for iOS smooth scroll on overflow containers. |
| Gesture ambiguity | No complex gesture requirements. All actions available via single tap or keyboard. |

```css
@media (hover: hover) {
  .eods-card--interactive:hover {
    box-shadow: var(--eods-card-shadow-hover);
    transform: translateY(-2px);
  }
}
```

---

## 6. Image Handling

| Concern | Implementation |
|---------|---------------|
| Responsive images | `<img>` uses `max-width: 100%; height: auto;` by default. |
| Art direction | Card media uses `object-fit: cover` to maintain aspect ratio without distortion. |
| Resolution switching | Not enforced at design system level — developers should use `srcset` and `sizes` attributes where needed. |
| Background images | Card background media uses `background-size: cover; background-position: center`. |
| Dark mode images | Option to apply `filter: brightness(0.9)` in dark mode. Prefer SVG icons that inherit `currentColor`. |

---

## 7. Print Styles

Print styles are defined in `theme-light.css` and can be extended:

```css
@media print {
  /* Hide navigation, modals, toasts, buttons */
  .eods-nav, .eods-dialog, .eods-toast-container, .eods-btn { display: none !important; }

  /* Show content at full width */
  .eods-container { max-width: 100%; padding: 0; }

  /* Show report tables without scroll */
  .eods-ig__table-container { overflow: visible; }

  /* Show URLs after links */
  a[href]::after { content: ' (' attr(href) ')'; }

  /* Page breaks */
  .eods-page-break { page-break-before: always; }
  .eods-avoid-break { page-break-inside: avoid; }
}
```

Utility classes:
- `.eods-no-print` — hide element when printing
- `.eods-print-only` — show element only when printing

---

## 8. Responsive Utilities

```css
/* Hide on mobile */
@media (max-width: 640px) {
  .eods-sm-hidden { display: none !important; }
}

/* Hide on tablet and below */
@media (max-width: 1024px) {
  .eods-md-hidden { display: none !important; }
}

/* Full-width on mobile */
@media (max-width: 640px) {
  .eods-sm-w-full { width: 100% !important; }
}
```

---

## 9. Testing Protocol

| Device/Viewport | Width | Test Method |
|-----------------|-------|------------|
| iPhone SE | 375px | Chrome DevTools emulation |
| iPhone 14 | 390px | Chrome DevTools emulation |
| iPhone 14 Pro Max | 430px | Chrome DevTools emulation |
| Galaxy S22 | 360px | Chrome DevTools emulation |
| iPad (portrait) | 768px | Chrome DevTools emulation |
| iPad (landscape) | 1024px | Chrome DevTools emulation |
| iPad Pro | 1024px | Chrome DevTools emulation |
| Laptop (1366x768) | 1366px | Standard desktop |
| Desktop (1920x1080) | 1920px | Standard desktop |
| Large Desktop (2560x1440) | 2560px | Test on real hardware |

### Test Criteria Per Breakpoint

1. No horizontal scroll at any breakpoint (except for wide data tables within IG).
2. All interactive elements are visible and tappable (≥44px touch targets for primary actions).
3. Navigation is usable (hamburger menu works on mobile, side nav on desktop).
4. Forms are readable and usable (labels remain visible, controls are appropriately sized).
5. Modal dialogs do not overflow viewport height.
6. Text is readable without zooming (minimum 14px for body text).
7. All content is accessible at 200% zoom (WCAG 1.4.4).
8. Dark mode renders correctly at all breakpoints.

---

## 10. Future Considerations

- **Container queries:** When browser support reaches 95%+, migrate breakpoint logic from `@media` to `@container` for truly component-level responsiveness. Currently, Safari 16+ supports container queries (93%+ global coverage as of 2025).
- **Fluid typography:** Consider `clamp()` for headline sizes if design requirements demand fluid scaling.
- **Viewport segments:** For foldable devices, test dual-screen scenarios when market share increases.
- **CSS Layers:** Use `@layer` for explicit cascade control when browser support is universal.
