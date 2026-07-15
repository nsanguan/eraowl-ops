# Design Tokens Specification

> **Generated:** 2026-07-14 &nbsp;|&nbsp; **Version:** 1.0.0 &nbsp;|&nbsp; **Format:** CSS Custom Properties

---

## Overview

Design tokens are the atomic building blocks of the EODS design system. Every color, spacing value, typography setting, shadow, and animation is defined as a CSS custom property. Components NEVER use raw values — they always reference tokens.

The token hierarchy:
```
Tier 1: Primitive (e.g., #2563eb, 1rem)
Tier 2: Semantic (e.g., --color-primary-500, --font-size-base)
Tier 3: Component (e.g., --eods-btn-bg-primary, --eods-card-radius)
```

---

## Color System

### Primary — Blue (#2563EB base)

```
50: #eff6ff  ─── Lightest (backgrounds, hover states on dark)
100: #dbeafe  ─── Light (selected rows, info banners)
200: #bfdbfe  ─── Light-Medium (focus rings, active states)
300: #93c5fd  ─── Medium (disabled primary buttons)
400: #60a5fa  ─── Medium-Dark (hover states)
500: #2563eb  ─── Base (primary buttons, links, brand)
600: #1d4ed8  ─── Dark (pressed states, active)
700: #1e40af  ─── Darker (heading text on primary bg)
800: #1e3a8a  ─── Very Dark (large text on primary)
900: #172554  ─── Darkest (rare, very light text on primary)
```

### Neutral — Slate (#64748B base)

```
50: #f8fafc  ─── Page background, region surfaces
100: #f1f5f9  ─── Alt row colors, subtle borders
200: #e2e8f0  ─── Standard borders, dividers
300: #cbd5e1  ─── Disabled text, placeholder
400: #94a3b8  ─── Muted text, inactive icons
500: #64748b  ─── Body text, secondary text
600: #475569  ─── Strong secondary text
700: #334155  ─── Heading text, emphasized
800: #1e293b  ─── Primary heading text
900: #0f172a  ─── Strongest text (rare)
```

### Semantic Colors

#### Success — Emerald (#10B981 base)
```
50: #ecfdf5  100: #d1fae5  200: #a7f3d0  300: #6ee7b7
400: #34d399  500: #10b981  600: #059669  700: #047857
800: #065f46  900: #064e3b
```

#### Warning — Amber (#F59E0B base)
```
50: #fffbeb  100: #fef3c7  200: #fde68a  300: #fcd34d
400: #fbbf24  500: #f59e0b  600: #d97706  700: #b45309
800: #92400e  900: #78350f
```

#### Danger — Red (#EF4444 base)
```
50: #fef2f2  100: #fee2e2  200: #fecaca  300: #fca5a5
400: #f87171  500: #ef4444  600: #dc2626  700: #b91c1c
800: #991b1b  900: #7f1d1d
```

#### Info — Blue (#3B82F6 base)
```
50: #eff6ff  100: #dbeafe  200: #bfdbfe  300: #93c5fd
400: #60a5fa  500: #3b82f6  600: #2563eb  700: #1d4ed8
800: #1e40af  900: #1e3a8a
```

---

## Surface Colors

```css
--color-surface-page:       #ffffff;   /* Main page background */
--color-surface-region:     #f8fafc;   /* Region/container background */
--color-surface-card:       #ffffff;   /* Card component background */
--color-surface-overlay:    #ffffff;   /* Modal, popup, dropdown background */
--color-surface-selected:   #eff6ff;   /* Selected row/item background */
--color-surface-disabled:   #f1f5f9;   /* Disabled element background */
--color-surface-hover:      #f8fafc;   /* Hover state background */
```

---

## Typography

### Font Families
```css
--font-family-sans:   'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
--font-family-mono:   'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
--font-family-display: var(--font-family-sans);
```

### Font Sizes (1.25 Major Third Scale)
```css
--font-size-2xs:   0.625rem;   /* 10px — fine print, captions */
--font-size-xs:    0.75rem;    /* 12px — labels, hints, badges */
--font-size-sm:    0.875rem;   /* 14px — body text, inputs */
--font-size-base:  1rem;       /* 16px — default body */
--font-size-lg:    1.125rem;   /* 18px — lead text */
--font-size-xl:    1.25rem;    /* 20px — H4 */
--font-size-2xl:   1.5rem;     /* 24px — H3 */
--font-size-3xl:   1.875rem;   /* 30px — H2 */
--font-size-4xl:   2.25rem;    /* 36px — H1 */
--font-size-5xl:   3rem;       /* 48px — Hero/Display */
```

### Font Weights
```css
--font-weight-light:    300;
--font-weight-normal:   400;
--font-weight-medium:   500;
--font-weight-semibold: 600;
--font-weight-bold:     700;
--font-weight-extrabold: 800;
```

### Line Heights
```css
--line-height-none:    1;
--line-height-tight:   1.25;
--line-height-snug:    1.375;
--line-height-normal:  1.5;
--line-height-relaxed: 1.625;
--line-height-loose:   2;
```

### Letter Spacing
```css
--tracking-tighter: -0.05em;
--tracking-tight:   -0.025em;
--tracking-normal:  0;
--tracking-wide:    0.025em;
--tracking-wider:   0.05em;
--tracking-widest:  0.1em;
```

---

## Border Radius

```css
--radius-none:   0;
--radius-xs:     0.125rem;   /* 2px — subtle rounding */
--radius-sm:     0.25rem;    /* 4px — inputs, small elements */
--radius-base:   0.375rem;   /* 6px — buttons, form controls */
--radius-md:     0.5rem;     /* 8px — cards */
--radius-lg:     0.75rem;    /* 12px — modals, large cards */
--radius-xl:     1rem;       /* 16px — large containers */
--radius-2xl:    1.5rem;     /* 24px — panels */
--radius-full:   9999px;     /* Pill / fully rounded */
```

---

## Spacing Scale (4px base / 0.25rem increments)

```css
--space-0:   0;
--space-0\.5: 0.125rem;   /* 2px */
--space-1:   0.25rem;     /* 4px */
--space-1\.5: 0.375rem;   /* 6px */
--space-2:   0.5rem;      /* 8px */
--space-2\.5: 0.625rem;   /* 10px */
--space-3:   0.75rem;     /* 12px */
--space-3\.5: 0.875rem;   /* 14px */
--space-4:   1rem;        /* 16px */
--space-5:   1.25rem;     /* 20px */
--space-6:   1.5rem;      /* 24px */
--space-7:   1.75rem;     /* 28px */
--space-8:   2rem;        /* 32px */
--space-9:   2.25rem;     /* 36px */
--space-10:  2.5rem;      /* 40px */
--space-11:  2.75rem;     /* 44px */
--space-12:  3rem;        /* 48px */
--space-14:  3.5rem;      /* 56px */
--space-16:  4rem;        /* 64px */
--space-20:  5rem;        /* 80px */
--space-24:  6rem;        /* 96px */
--space-28:  7rem;        /* 112px */
--space-32:  8rem;        /* 128px */
--space-36:  9rem;        /* 144px */
--space-40:  10rem;       /* 160px */
--space-44:  11rem;       /* 176px */
--space-48:  12rem;       /* 192px */
--space-52:  13rem;       /* 208px */
--space-56:  14rem;       /* 224px */
--space-60:  15rem;       /* 240px */
--space-64:  16rem;       /* 256px */
--space-72:  18rem;       /* 288px */
--space-80:  20rem;       /* 320px */
--space-96:  24rem;       /* 384px */
```

---

## Shadows

```css
--shadow-none:    none;
--shadow-xs:      0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-sm:      0 1px 3px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
--shadow-base:    0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06);
--shadow-md:      0 4px 6px rgba(0, 0, 0, 0.07), 0 2px 4px rgba(0, 0, 0, 0.06);
--shadow-lg:      0 10px 15px rgba(0, 0, 0, 0.1), 0 4px 6px rgba(0, 0, 0, 0.05);
--shadow-xl:      0 20px 25px rgba(0, 0, 0, 0.1), 0 10px 10px rgba(0, 0, 0, 0.04);
--shadow-2xl:     0 25px 50px rgba(0, 0, 0, 0.25);
--shadow-inner:   inset 0 2px 4px 0 rgba(0, 0, 0, 0.06);
--shadow-focus:   0 0 0 3px rgba(37, 99, 235, 0.3);
--shadow-focus-danger: 0 0 0 3px rgba(239, 68, 68, 0.3);
```

---

## Animation & Transitions

```css
--transition-fast:     150ms cubic-bezier(0.4, 0, 0.2, 1);
--transition-base:     250ms cubic-bezier(0.4, 0, 0.2, 1);
--transition-slow:     350ms cubic-bezier(0.4, 0, 0.2, 1);
--transition-very-slow: 500ms cubic-bezier(0.4, 0, 0.2, 1);

--easing-in:     cubic-bezier(0.4, 0, 1, 1);
--easing-out:    cubic-bezier(0, 0, 0.2, 1);
--easing-in-out: cubic-bezier(0.4, 0, 0.2, 1);
```

---

## Z-Index Scale

```css
--z-base:        0;
--z-dropdown:    1000;
--z-sticky:      1020;
--z-fixed:       1030;
--z-modal-backdrop: 1040;
--z-modal:       1050;
--z-popover:     1060;
--z-tooltip:     1070;
--z-toast:       1080;
--z-debug:       9999;
```

---

## Layout

```css
--container-max-width:    1280px;
--container-narrow-width:  768px;
--container-wide-width:   1600px;

--breakpoint-sm:  640px;
--breakpoint-md:  1024px;
--breakpoint-lg:  1280px;
--breakpoint-xl:  1536px;

--grid-columns: 12;
--grid-gutter:  var(--space-4);
```

---

## Borders

```css
--border-width-thin:  1px;
--border-width-base:  1px;
--border-width-thick: 2px;

--border-style: solid;

--border-color-default: var(--color-neutral-200);
--border-color-strong:  var(--color-neutral-300);
--border-color-focus:   var(--color-primary-400);
--border-color-error:   var(--color-danger-400);
```

---

## Component-Specific Tokens (Tier 3)

```css
/* Button */
--eods-btn-height-sm:    2rem;
--eods-btn-height-md:    2.5rem;
--eods-btn-height-lg:    3rem;
--eods-btn-padding-x-sm: var(--space-3);
--eods-btn-padding-x-md: var(--space-4);
--eods-btn-padding-x-lg: var(--space-6);
--eods-btn-font-size-sm: var(--font-size-xs);
--eods-btn-font-size-md: var(--font-size-sm);
--eods-btn-font-size-lg: var(--font-size-base);
--eods-btn-radius:       var(--radius-base);

/* Form */
--eods-form-label-size:     var(--font-size-sm);
--eods-form-label-weight:   var(--font-weight-medium);
--eods-form-control-height: 2.5rem;
--eods-form-control-padding: var(--space-2) var(--space-3);
--eods-form-control-radius:  var(--radius-sm);
--eods-form-hint-size:       var(--font-size-xs);
--eods-form-error-size:      var(--font-size-xs);

/* Card */
--eods-card-padding:    var(--space-6);
--eods-card-radius:     var(--radius-md);
--eods-card-shadow:     var(--shadow-base);
--eods-card-shadow-hover: var(--shadow-md);
--eods-card-gap:        var(--space-4);

/* Dialog */
--eods-dialog-radius:   var(--radius-lg);
--eods-dialog-shadow:   var(--shadow-xl);
--eods-dialog-padding:  var(--space-6);
--eods-dialog-max-width-sm: 400px;
--eods-dialog-max-width-md: 560px;
--eods-dialog-max-width-lg: 720px;
--eods-dialog-max-width-xl: 960px;

/* Navigation */
--eods-nav-width:           240px;
--eods-nav-collapsed-width: 64px;
--eods-nav-bg:              var(--color-neutral-800);
--eods-nav-text:            var(--color-neutral-100);
--eods-nav-active-bg:       var(--color-primary-600);
--eods-nav-hover-bg:        var(--color-neutral-700);
```

---

## Dark Mode Token Mapping

| Light Token | Dark Token Value |
|-------------|-----------------|
| `--color-surface-page` | `#0f172a` |
| `--color-surface-region` | `#1e293b` |
| `--color-surface-card` | `#1e293b` |
| `--color-surface-overlay` | `#1e293b` |
| `--color-surface-selected` | `#1e3a8a` |
| `--color-surface-hover` | `#334155` |
| `--color-neutral-50` | `#1e293b` |
| `--color-neutral-100` | `#334155` |
| `--color-neutral-200` | `#475569` |
| `--color-neutral-300` | `#64748b` |
| `--color-neutral-400` | `#94a3b8` |
| `--color-neutral-500` | `#cbd5e1` |
| `--color-neutral-600` | `#e2e8f0` |
| `--color-neutral-700` | `#f1f5f9` |
| `--color-neutral-800` | `#f8fafc` |
| `--color-neutral-900` | `#ffffff` |
| `--border-color-default` | `var(--color-neutral-700)` |
| `--border-color-strong` | `var(--color-neutral-600)` |
