# Tailwind CSS v4 Integration Guide

The EraOwl Design System tokens are designed to work seamlessly with Tailwind CSS v4 via the `@theme inline` directive.

## Current Mapping (in `eraowl-ops-frontend/src/index.css`)

```css
@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-muted: var(--muted);
  --color-accent: var(--accent);
  --color-destructive: var(--destructive);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --color-success: var(--success);
  --color-warning: var(--warning);
  --color-surface-dim: var(--surface-dim);
  --color-surface-container: var(--surface-container);
  --color-on-surface: var(--on-surface);
  --color-outline: var(--outline);
  --color-error: var(--error);
  --radius-sm: calc(var(--radius) - 0.375rem);
  --radius-md: calc(var(--radius) - 0.25rem);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 0.25rem);
  --font-sans: Inter, ui-sans-serif, system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

## Using Tokens from EODS

### Option 1: Via Tailwind Utility Classes

```jsx
<button className="bg-primary text-primary-foreground rounded-lg px-4 py-2">
  Save
</button>
```

### Option 2: Via CSS Custom Properties

```css
.my-component {
  background-color: var(--color-surface-container);
  border: 1px solid var(--color-outline-variant);
  border-radius: var(--radius-lg);
}
```

### Option 3: Via EODS CSS Classes

```jsx
<button className="eods-btn eods-btn--primary eods-btn--lg">
  Save
</button>
```

## How Tokens Flow

```
tokens.css              index.css                  Component CSS
───color-primary-500 →  @theme { --color-primary } → bg-primary
───color-primary-500 →  --eods-btn-primary-bg     → .eods-btn--primary { background: var(--color-primary-500) }
```

All three approaches reference the same underlying CSS custom properties — they are interchangeable.

## Adding New Tokens

1. Add the value in `css/tokens.css`
2. Add the light/dark override in `css/theme-light.css` and `css/theme-dark.css` if needed
3. Add the Tailwind mapping in `src/index.css` `@theme inline` block
