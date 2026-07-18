import { useEffect } from 'react'
import usePersonalizeStore from '../../../store/usePersonalizeStore'

/**
 * Apply APEX-style Theme Roller tokens to the document root as CSS variables.
 * Call once at app root (see App.jsx). Respects tokens from the store.
 */
export function applyThemeToRoot(tokens) {
  if (!tokens || typeof document === 'undefined') return
  const root = document.documentElement
  if (tokens.primary) root.style.setProperty('--primary', tokens.primary)
  if (tokens.primaryContainer) root.style.setProperty('--primary-container', tokens.primaryContainer)
  if (tokens.surface) root.style.setProperty('--surface', tokens.surface)
  if (tokens.background) root.style.setProperty('--background', tokens.background)
  if (tokens.font) root.style.setProperty('--font-sans', tokens.font)
  if (tokens.radius) root.style.setProperty('--radius', `${tokens.radius}px`)
  if (tokens.spacing) root.style.setProperty('--spacing', `${tokens.spacing}px`)
}

export const THEME_PRESETS = [
  { id: 'blue', label: 'Oracle Blue', tokens: { primary: '#0059bb', primaryContainer: '#0070ea', surface: '#f8f9fa', background: '#f8f9fa', font: "'Inter', sans-serif", radius: 12, spacing: 16 } },
  { id: 'violet', label: 'Violet', tokens: { primary: '#6d28d9', primaryContainer: '#7c3aed', surface: '#faf5ff', background: '#faf5ff', font: "'Inter', sans-serif", radius: 14, spacing: 18 } },
  { id: 'emerald', label: 'Emerald', tokens: { primary: '#047857', primaryContainer: '#059669', surface: '#f0fdf4', background: '#f0fdf4', font: "'Inter', sans-serif", radius: 10, spacing: 14 } },
  { id: 'slate', label: 'Slate Dark', tokens: { primary: '#38bdf8', primaryContainer: '#0ea5e9', surface: '#0f172a', background: '#0f172a', font: "'Inter', sans-serif", radius: 10, spacing: 16 } },
  { id: 'rose', label: 'Rose', tokens: { primary: '#be123c', primaryContainer: '#e11d48', surface: '#fff1f2', background: '#fff1f2', font: "'Inter', sans-serif", radius: 16, spacing: 18 } },
]

export default function ThemeRoller({ targetRoleId, targetUserId }) {
  const themeTokens = usePersonalizeStore((s) => s.themeTokens)
  const applyThemeTokens = usePersonalizeStore((s) => s.applyThemeTokens)
  const resetThemeTokens = usePersonalizeStore((s) => s.resetThemeTokens)
  const saveTheme = usePersonalizeStore((s) => s.saveTheme)

  // Preview live as tokens change
  useEffect(() => {
    applyThemeToRoot(themeTokens)
  }, [themeTokens])

  const current = themeTokens || {}

  const update = (key, value) => applyThemeTokens({ ...current, [key]: value })

  return (
    <div className="space-y-4">
      <p className="text-[11px] text-outline leading-relaxed">
        APEX-style Theme Roller — customize global colors, typography and shape. Changes apply live and can be saved per role or user.
      </p>

      <div>
        <div className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1.5">Presets</div>
        <div className="grid grid-cols-2 gap-2">
          {THEME_PRESETS.map((p) => (
            <button key={p.id} onClick={() => applyThemeTokens(p.tokens)}
              className="flex items-center gap-2 px-2 py-1.5 rounded-lg border border-outline-variant hover:bg-surface-container-low text-[11px] font-medium text-on-surface">
              <span className="w-4 h-4 rounded-full" style={{ background: p.tokens.primary }} />
              {p.label}
            </button>
          ))}
        </div>
      </div>

      <div className="space-y-3">
        <div>
          <label className="block text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">Primary Color</label>
          <input type="color" value={current.primary || '#0059bb'} onChange={(e) => update('primary', e.target.value)} className="w-full h-9 rounded-lg border border-outline-variant bg-transparent" />
        </div>
        <div>
          <label className="block text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">Surface / Background</label>
          <input type="color" value={current.surface || '#f8f9fa'} onChange={(e) => { update('surface', e.target.value); update('background', e.target.value) }} className="w-full h-9 rounded-lg border border-outline-variant bg-transparent" />
        </div>
        <div>
          <label className="block text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">Font Family</label>
          <select value={current.font || "'Inter', sans-serif"} onChange={(e) => update('font', e.target.value)}
            className="w-full px-2 py-1.5 text-xs bg-surface-bright border border-outline-variant rounded-lg text-on-surface outline-none focus:border-primary">
            <option value="'Inter', sans-serif">Inter</option>
            <option value="'JetBrains Mono', monospace">JetBrains Mono</option>
            <option value="'Roboto', sans-serif">Roboto</option>
            <option value="'Georgia', serif">Georgia</option>
          </select>
        </div>
        <div>
          <label className="block text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">Corner Radius ({current.radius ?? 12}px)</label>
          <input type="range" min={0} max={24} value={current.radius ?? 12} onChange={(e) => update('radius', Number(e.target.value))} className="w-full accent-primary" />
        </div>
        <div>
          <label className="block text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">Spacing ({current.spacing ?? 16}px)</label>
          <input type="range" min={8} max={28} value={current.spacing ?? 16} onChange={(e) => update('spacing', Number(e.target.value))} className="w-full accent-primary" />
        </div>
      </div>

      <div className="flex gap-2 pt-1">
        <button onClick={() => resetThemeTokens()} className="flex-1 px-3 py-2 text-xs font-semibold bg-surface-container-highest text-on-surface rounded-lg hover:bg-surface-variant">
          Reset
        </button>
        <button onClick={() => saveTheme(targetUserId, targetRoleId)} className="flex-1 px-3 py-2 text-xs font-semibold bg-primary text-primary-foreground rounded-lg hover:opacity-90">
          Save Theme
        </button>
      </div>
    </div>
  )
}
