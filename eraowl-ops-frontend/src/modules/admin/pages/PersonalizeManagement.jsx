import { useState, useEffect, useCallback, useMemo } from 'react'
import api from '../../../api/client'
import usePersonalizeStore from '../../../store/usePersonalizeStore'
import useAuthStore from '../../../store/authStore'
import PersonalizeWrapper from '../../../shared-ui-kit/components/ui/PersonalizeWrapper'
import ThemeRoller from '../../../shared-ui-kit/components/ui/ThemeRoller'

import UserManagement from '../pages/UserManagement'
import RoleManagement from '../pages/RoleManagement'
import ObjectsPage from '../pages/ObjectsPage'
import OrgStructurePage from '../../mdm/org_structure/pages/OrgStructurePage'
import PartyPage from '../../mdm/party/pages/PartyPage'
import ItemPage from '../../mdm/item/pages/ItemPage'
import BomPage from '../../bom/pages/BomPage'
import DashboardHome from '../../../components/DashboardHome'
import CollaborationDashboard from '../../collaboration/pages/Dashboard'
import DiscussPage from '../../collaboration/pages/DiscussPage'
import ChatPage from '../../collaboration/pages/ChatPage'
import CalendarPage from '../../collaboration/pages/CalendarPage'
import TodoPage from '../../collaboration/pages/TodoPage'
import ActivitiesPage from '../../collaboration/pages/ActivitiesPage'

// APEX-style component inspector: edit visibility, label, required, order for
// the currently selected personalizable component.
// Stable empty-meta reference so the store selector never returns a fresh
// object (Zustand v5 + useSyncExternalStore throws "getSnapshot should be
// cached" / "Maximum update depth" when a selector returns a new object on
// every call — this was crashing the inspector with React error #185).
const EMPTY_META = {}

function ComponentInspector({ componentId }) {
  const meta = usePersonalizeStore((s) => {
    const find = (node) => {
      if (!node || typeof node !== 'object') return null
      if (node.id === componentId) return node.meta || EMPTY_META
      if (node.children) {
        for (const c of node.children) {
          const f = find(c)
          if (f) return f
        }
      }
      return null
    }
    return find(s.pageSchema) || EMPTY_META
  }) || EMPTY_META
  const setComponentVisibility = usePersonalizeStore((s) => s.setComponentVisibility)
  const setComponentLabel = usePersonalizeStore((s) => s.setComponentLabel)
  const setComponentRequired = usePersonalizeStore((s) => s.setComponentRequired)
  const moveComponent = usePersonalizeStore((s) => s.moveComponent)

  return (
    <div className="space-y-3 border-t border-outline-variant! pt-3">
      <div className="text-[10px] font-mono text-secondary! truncate">{componentId}</div>
      <label className="flex items-center justify-between text-xs text-on-surface!">
        <span>Visible</span>
        <input type="checkbox" checked={meta.visible !== false} onChange={(e) => setComponentVisibility(componentId, e.target.checked)} className="rounded accent-primary! w-4 h-4" />
      </label>
      <div>
        <label className="block text-[10px] font-semibold uppercase tracking-wider text-outline! mb-1">Label Override</label>
        <input
          value={meta.label || ''}
          placeholder="(default)"
          onChange={(e) => setComponentLabel(componentId, e.target.value || undefined)}
          className="w-full px-2 py-1.5 text-xs bg-surface-bright! border border-outline-variant! rounded-lg text-on-surface! outline-none focus:border-primary!" />
      </div>
      <label className="flex items-center justify-between text-xs text-on-surface!">
        <span>Required</span>
        <input type="checkbox" checked={!!meta.required} onChange={(e) => setComponentRequired(componentId, e.target.checked)} className="rounded accent-primary! w-4 h-4" />
      </label>
      <div className="flex gap-2">
        <button onClick={() => moveComponent(componentId, -1)} className="flex-1 px-2 py-1.5 text-[11px] font-semibold bg-surface-container-highest! text-on-surface! rounded-lg hover:bg-surface-variant!">Move Up</button>
        <button onClick={() => moveComponent(componentId, 1)} className="flex-1 px-2 py-1.5 text-[11px] font-semibold bg-surface-container-highest! text-on-surface! rounded-lg hover:bg-surface-variant!">Move Down</button>
      </div>
    </div>
  )
}

// Map a personalizable page_key to its REAL page component so the personalize
// preview renders exactly what the live page shows (full instrumentation).
const PAGE_PREVIEWS = {
  'admin.users': UserManagement,
  'admin.roles': RoleManagement,
  'admin.objects': ObjectsPage,
  'mdm.org_structure': OrgStructurePage,
  'mdm.party': PartyPage,
  'mdm.item': ItemPage,
  'bom.bom': BomPage,
  'dashboard.home': DashboardHome,
  'collaboration': CollaborationDashboard,
  'collaboration.discuss': DiscussPage,
  'collaboration.chat': ChatPage,
  'collaboration.calendar': CalendarPage,
  'collaboration.todo': TodoPage,
  'collaboration.activities': ActivitiesPage,
}

/**
 * User Personalize (Admin) — follows requirements/personalize-design-v2.html
 * (layered on the v1 functional base: page search, role-targeted delta save,
 * in-context edit chrome + upgraded Editor Tools panel).
 */

const ACCENT = '#6366F1'
const SWATCHES = ['#002045', '#1960a3', '#10b981', '#f59e0b', '#ef4444', ACCENT, '#06b6d4', '#ec4899']
const FONTS = [
  { id: 'Inter', label: 'Inter (Corporate)', stack: "'Inter', sans-serif" },
  { id: 'Roboto', label: 'Roboto (Standard)', stack: "'Roboto', sans-serif" },
  { id: 'JetBrains Mono', label: 'JetBrains Mono (Developer)', stack: "'JetBrains Mono', monospace" },
  { id: 'Outfit', label: 'Outfit (Modern)', stack: "'Outfit', sans-serif" },
]

const toCss = (styles = {}) => {
  const out = { ...styles }
  if (out.gridSpan) {
    out.gridColumn = `span ${parseInt(out.gridSpan, 10)} / span ${parseInt(out.gridSpan, 10)}`
    delete out.gridSpan
  }
  if (out.fontColor) { out.color = out.fontColor; delete out.fontColor }
  return out
}

// Resolve a stored style for the active component (helper for control defaults).
// NOTE: must select stable slices and derive with useMemo — Zustand v5's
// useSyncExternalStore throws ("getSnapshot should be cached") if a selector
// returns a fresh object on every call, which blanks the page.
function useActiveStyles() {
  const activeComponentId = usePersonalizeStore((s) => s.activeComponentId)
  const pageSchema = usePersonalizeStore((s) => s.pageSchema)
  return useMemo(() => {
    if (!activeComponentId) return {}
    const walk = (n) => {
      if (!n || typeof n !== 'object') return null
      if (n.id === activeComponentId) return n.styles || {}
      if (n.children) for (const c of n.children) { const f = walk(c); if (f) return f }
      return null
    }
    return walk(pageSchema) || {}
  }, [activeComponentId, pageSchema])
}

export default function PersonalizeManagement() {
  const isDesignMode = usePersonalizeStore((s) => s.isDesignMode)
  const toggleDesignMode = usePersonalizeStore((s) => s.toggleDesignMode)
  const listTemplates = usePersonalizeStore((s) => s.listTemplates)
  const loadTemplate = usePersonalizeStore((s) => s.loadTemplate)
  const loadTheme = usePersonalizeStore((s) => s.loadTheme)
  const savePersonalization = usePersonalizeStore((s) => s.savePersonalization)
  const updateComponentStyles = usePersonalizeStore((s) => s.updateComponentStyles)
  const applyGlobalTheme = usePersonalizeStore((s) => s.applyGlobalTheme)
  const applyStylesToAll = usePersonalizeStore((s) => s.applyStylesToAll)
  const setGridLayout = usePersonalizeStore((s) => s.setGridLayout)
  const applyPreset = usePersonalizeStore((s) => s.applyPreset)
  const pageSchema = usePersonalizeStore((s) => s.pageSchema)
  const activeComponentId = usePersonalizeStore((s) => s.activeComponentId)
  const activeStyles = useActiveStyles()

  const [pages, setPages] = useState([])
  const [search, setSearch] = useState('')
  const [selected, setSelected] = useState(null)
  const [roles, setRoles] = useState([])
  const [targetRoleId, setTargetRoleId] = useState('')
  const [status, setStatus] = useState(null)
  const [tab, setTab] = useState('layout')
  const [gutter, setGutter] = useState(16)
  const [radius, setRadius] = useState(8)
  const [hex, setHex] = useState('#002045')

  const refreshPages = useCallback(async (q) => setPages(await listTemplates(q || undefined)), [listTemplates])
  useEffect(() => { refreshPages('') }, [refreshPages])
  useEffect(() => {
    api.get('/admin/roles', { params: { page: 1, page_size: 200 } })
      .then((r) => setRoles(r.data.items || [])).catch(() => setRoles([]))
  }, [])
  useEffect(() => { loadTheme() }, [loadTheme])

  const selectPage = useCallback(async (pageKey) => {
    setSelected(pageKey); setStatus(null); await loadTemplate(pageKey)
  }, [loadTemplate])

  const handleSearch = (e) => { const q = e.target.value; setSearch(q); refreshPages(q) }

  const handleSave = async () => {
    if (!selected) return
    setStatus(null)
    // A personalisation must target a role OR a user. When no role is picked
    // (the "No role (user draft)" option) we save against the current user so
    // the backend's "at least one target" rule is satisfied.
    const currentUserId = useAuthStore.getState().user?.user_id || null
    const targetUserId = targetRoleId ? null : currentUserId
    const res = await savePersonalization(selected, targetUserId, targetRoleId || null, { asDelta: true })
    setStatus(res ? { ok: true, msg: 'Saved personalization.' } : { ok: false, msg: 'Save failed.' })
  }
  const handleReset = async () => {
    if (!selected) return
    await loadTemplate(selected)
    setStatus({ ok: true, msg: 'Reverted to base template.' })
  }

  // ── Editor Tools handlers ──
  const setColor = (c) => { setHex(c); if (activeComponentId) updateComponentStyles(activeComponentId, { fontColor: c }) }
  const setFont = (stack) => activeComponentId && updateComponentStyles(activeComponentId, { fontFamily: stack })
  const applyGutter = (px) => { setGutter(px); if (activeComponentId) updateComponentStyles(activeComponentId, { gap: `${px}px` }) }
  const setRadiusVal = (px) => { setRadius(px); if (activeComponentId) updateComponentStyles(activeComponentId, { borderRadius: `${px}px` }) }

  const children = pageSchema?.children || []

  return (
    <div className="flex flex-col h-full gap-4">
      {/* ── Top: branding + Personalizable Pages search ── */}
      <div className="flex items-center justify-between gap-4 rounded-xl border border-outline-variant! bg-primary! px-4 py-3">
        <div>
          <h1 className="font-bold text-lg text-on-primary! leading-tight">CoreAdmin</h1>
          <p className="text-xs text-on-primary! opacity-70">Enterprise Resource Planning</p>
        </div>
        <div className="flex items-center gap-2 flex-1 max-w-md ml-auto">
          <span className="text-sm font-semibold text-on-primary! whitespace-nowrap">Personalizable Pages</span>
          <input
            value={search}
            onChange={handleSearch}
            placeholder="Search pages…"
            className="w-full px-3 py-1.5 text-sm rounded-lg bg-primary-container! text-on-primary! border border-outline-variant! placeholder:text-on-primary!/50"
          />
        </div>
      </div>

      {/* ── Body row: page list | editor | panel ── */}
      <div className="flex flex-1 min-h-0 gap-4">
      {/* ── Left: page list (functional) ── */}
      <aside className="w-80 shrink-0 rounded-xl border border-outline-variant! bg-surface-container-lowest! p-3 flex flex-col">
        <div className="flex-1 overflow-y-auto space-y-1 pz-thin-scroll">
          {pages.map((p) => (
            <button
              key={p.page_key}
              onClick={() => selectPage(p.page_key)}
              className={`w-full text-left px-2 py-1.5 rounded-lg text-sm flex items-center justify-between ${
                selected === p.page_key ? 'bg-accent-personalization! text-white! font-semibold'
                  : 'text-on-surface-variant! opacity-80 hover:bg-surface-container-high!'
              }`}
            >
              <span className="font-mono text-xs truncate">{p.page_key}</span>
              <span className="text-[10px] opacity-70">{p.component_count}</span>
            </button>
          ))}
          {pages.length === 0 && <p className="text-xs text-on-surface-variant!/60 italic px-1">No pages found.</p>}
        </div>
      </aside>

      {/* ── Center: WYSIWYG editor ── */}
      {/* When the right Personalization Panel is open (design mode + a page
          selected) it is position:fixed and overlaps the section's right edge,
          which would hide the SAVE CHANGES button. Reserve that width so the
          canvas (and its Save button) stay clear of the panel. */}
      <section className={`flex-1 min-w-0 flex flex-col ${isDesignMode && selected ? 'xl:pr-80' : ''}`}>
        {/* Top app bar (v2) */}
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2">
            <span className="material-symbols-outlined text-primary!">settings_applications</span>
            <h1 className="text-2xl font-bold text-primary!">ERP Personalize</h1>
          </div>
          {isDesignMode && selected && (
            <div className="flex items-center gap-2">
              <select
                value={targetRoleId}
                onChange={(e) => setTargetRoleId(e.target.value)}
                className="px-2 py-1 text-sm rounded-lg border border-outline-variant! bg-surface-container-low! text-on-surface!"
                title="Save personalization for this role"
              >
                <option value="">No role (user draft)</option>
                {roles.map((r) => (<option key={r.role_id} value={r.role_id}>{r.role_name}</option>))}
              </select>
              <button onClick={handleReset}
                className="px-3 py-1.5 rounded-lg text-sm font-bold bg-surface-container-highest! text-on-surface-variant! hover:bg-surface-variant!">
                Discard Changes
              </button>
            </div>
          )}
        </div>

        {/* Edit canvas */}
        <div className={`flex-1 overflow-y-auto rounded-xl border border-outline-variant! bg-surface-container-low! p-6 pz-thin-scroll ${
          isDesignMode ? 'pz-edit-grid' : ''
        }`}>
          {!selected ? (
            <div className="h-full flex items-center justify-center text-slate-400! dark:text-slate-500! text-sm">
              Choose a page to begin editing its layout.
            </div>
          ) : (
            <div className="max-w-2xl mx-auto space-y-4">
              {/* Status badge + Save */}
              <div className="flex justify-between items-center">
                {isDesignMode ? (
                  <span className="bg-accent-personalization! text-white! px-3 py-1 rounded-full font-mono text-xs flex items-center gap-1">
                    <span className="material-symbols-outlined text-[14px]" style={{ fontVariationSettings: "'FILL' 1" }}>edit</span>
                    LAYOUT EDIT MODE
                  </span>
                ) : <span />}
                <button onClick={toggleDesignMode}
                  className="bg-primary! text-white! text-sm font-semibold px-4 py-2 rounded-lg shadow-sm active:scale-95">
                  {isDesignMode ? 'Exit Edit' : 'Edit Layout'}
                </button>
              </div>

              {status && (
                <div className={`px-3 py-1.5 rounded-lg text-sm ${
                  status.ok ? 'bg-green-100! text-green-800! dark:bg-green-900! dark:text-green-100!'
                            : 'bg-red-100! text-red-800! dark:bg-red-900! dark:text-red-100!'
                }`}>{status.msg}</div>
              )}

              {/* Save Changes (v2 canvas button, visible in edit mode) */}
              {isDesignMode && (
                <div className="flex justify-end">
                  <button onClick={handleSave}
                    className="bg-primary! text-white! font-semibold text-sm px-4 py-2 rounded-lg shadow-sm active:scale-95">
                    SAVE CHANGES
                  </button>
                </div>
              )}

              {/* Live preview = the REAL page component (full instrumentation) */}
              {(() => {
                const Preview = PAGE_PREVIEWS[selected]
                if (Preview) return <Preview />
                // Fallback: render the base layout skeleton
                if (children.length === 0) {
                  return <p className="text-slate-400! text-sm italic">This template has no components yet.</p>
                }
                return children.map((node) => (
                  <EditCard key={node.id} node={node} activeId={activeComponentId} />
                ))
              })()}

              <p className="text-center font-mono text-on-surface-variant! mt-6 uppercase tracking-widest text-xs">
                Drag elements via handles to reorder layout
              </p>
            </div>
          )}
        </div>

        {/* Drag hint */}
        {isDesignMode && selected && (
          <div className="fixed bottom-6 left-[360px] bg-primary! text-on-primary! px-4 py-2 rounded-full shadow-2xl flex items-center gap-2 z-40 border border-secondary! pointer-events-none">
            <span className="material-symbols-outlined">drag_indicator</span>
            <span className="text-sm font-bold">Drag components to rearrange your workspace</span>
          </div>
        )}
      </section>

      {/* ── Right: Editor Tools drawer (v2) ── */}
      {isDesignMode && selected && (
        <aside className="fixed right-0 top-14 h-[calc(100vh-3.5rem)] w-80 bg-surface-container-lowest! border-l-4 border-secondary! shadow-lg z-50 flex flex-col p-4 overflow-y-auto pz-thin-scroll">
          <div className="flex items-center justify-between mb-3">
            <h3 className="text-base font-bold text-secondary!">Personalization Panel</h3>
          </div>

          {/* Tabs */}
          <nav className="flex border-b border-outline-variant! mb-4">
            {[['theme', 'THEME'], ['layout', 'LAYOUT'], ['components', 'COMPONENTS']].map(([k, label]) => (
              <button key={k} onClick={() => setTab(k)}
                className={`flex-1 pb-2 text-[11px] font-bold uppercase ${
                  tab === k ? 'text-primary! border-b-2 border-primary!' : 'text-on-surface-variant!'
                }`}>
                {label}
              </button>
            ))}
          </nav>

          {tab === 'theme' && (
            <ThemeRoller targetRoleId={targetRoleId || null} targetUserId={null} />
          )}

          {tab === 'layout' && (
            <div className="space-y-5">
              {/* Spacing & Density (gutter + radius) */}
              <section className="space-y-3">
                <div className="flex items-center gap-1 text-primary!">
                  <span className="material-symbols-outlined text-sm">space_bar</span>
                  <h4 className="text-sm font-semibold">Spacing &amp; Density</h4>
                </div>
                <div className="space-y-1">
                  <div className="flex justify-between text-[11px] font-bold uppercase text-on-surface-variant!">
                    <span>Gutter Width</span><span className="text-secondary!">{gutter}px</span>
                  </div>
                  <input type="range" min={4} max={40} value={gutter}
                    onChange={(e) => applyGutter(parseInt(e.target.value, 10))}
                    className="w-full accent-secondary! cursor-pointer" />
                </div>
                <div className="space-y-1">
                  <div className="flex justify-between text-[11px] font-bold uppercase text-on-surface-variant!">
                    <span>Corner Radius</span><span className="text-secondary!">{radius}px</span>
                  </div>
                  <input type="range" min={0} max={24} value={radius}
                    onChange={(e) => setRadiusVal(parseInt(e.target.value, 10))}
                    className="w-full accent-secondary! cursor-pointer" />
                </div>
              </section>

              {/* Grid Layout */}
              <section className="space-y-2">
                <div className="flex items-center gap-1 text-primary!">
                  <span className="material-symbols-outlined text-sm">grid_view</span>
                  <h4 className="text-sm font-semibold">Grid Layout</h4>
                </div>
                <div className="flex gap-2">
                  {[['stacked', 'view_stream', 'STACKED'], ['columns', 'view_week', 'COLUMNS'], ['bento', 'view_quilt', 'BENTO']].map(([mode, icon, label]) => (
                    <button key={mode} onClick={() => setGridLayout(mode, activeComponentId)}
                      className="flex-1 py-2 rounded-lg flex flex-col items-center gap-1 text-[10px] font-bold border border-outline-variant! bg-surface-container-low! text-on-surface-variant! hover:bg-surface-container-high!">
                      <span className="material-symbols-outlined text-sm">{icon}</span>
                      {label}
                    </button>
                  ))}
                </div>
              </section>

              {/* Reset */}
              <section>
                <div className="flex items-center justify-between p-2 bg-surface-container! rounded-lg border border-outline-variant!">
                  <div className="flex items-center gap-1 text-primary!">
                    <span className="material-symbols-outlined text-sm">restart_alt</span>
                    <span className="text-[11px] font-bold uppercase">Reset Layout</span>
                  </div>
                  <button onClick={handleReset} className="text-error! text-[11px] font-bold uppercase">Execute</button>
                </div>
              </section>

              {/* APPLY GLOBAL */}
              <section>
                <button onClick={() => applyGlobalTheme(activeComponentId)}
                  disabled={!activeComponentId}
                  className="w-full bg-accent-personalization! text-white! py-2 rounded-lg font-bold shadow-lg flex items-center justify-center gap-1 hover:scale-105 active:scale-95 transition-all disabled:opacity-40">
                  <span className="material-symbols-outlined text-sm">published_with_changes</span>
                  Apply Global
                </button>
              </section>
            </div>
          )}

          {tab === 'components' && (
            <div className="space-y-3">
              <h4 className="text-sm font-semibold text-primary!">Components</h4>
              {children.map((node) => (
                <button key={node.id} onClick={() => usePersonalizeStore.getState().setActiveComponent(node.id)}
                  className={`w-full text-left px-2 py-1.5 rounded text-xs font-mono truncate ${
                    activeComponentId === node.id ? 'bg-accent-personalization! text-white!' : 'text-on-surface-variant! hover:bg-surface-container-high!'
                  }`}>
                  {node.id}
                </button>
              ))}

              {activeComponentId && (
                <ComponentInspector key={activeComponentId} componentId={activeComponentId} />
              )}
            </div>
          )}

          {/* Footer: GENERATE AI PRESET */}
          <div className="mt-auto pt-3 border-t border-outline-variant!">
            <button onClick={applyPreset}
              className="w-full bg-accent-personalization! text-white! py-3 rounded-lg font-semibold flex items-center justify-center gap-1 shadow-md hover:brightness-110 transition-all">
              <span className="material-symbols-outlined text-sm">auto_fix_high</span>
              Generate AI Preset
            </button>
          </div>
        </aside>
      )}

      {/* Mobile bottom nav (v2) */}
      </div>

      <nav className="md:hidden fixed bottom-0 w-full z-50 bg-surface-container! h-16 px-4 border-t border-outline-variant! flex justify-around items-center shadow-sm">
        {[['admin_panel_settings', 'Admin'], ['group', 'Users'], ['home', 'Home'], ['corporate_fare', 'Org'], ['more_horiz', 'More']].map(([icon, label], i) => (
          <button key={label} className={`flex flex-col items-center justify-center ${i === 1 ? 'text-primary!' : 'text-on-surface-variant!'}`}>
            <span className="material-symbols-outlined text-sm">{icon}</span>
            <span className="text-[10px] font-bold uppercase">{label}</span>
          </button>
        ))}
      </nav>
    </div>
  )
}

/** Component card with v2 chrome: dashed border + hover-reveal drag handle. */
function EditCard({ node, activeId }) {
  if (!node || typeof node !== 'object') return null
  const style = toCss(node.styles || {})
  const kids = node.children || []
  const isActive = activeId === node.id

  return (
    <PersonalizeWrapper componentId={node.id}>
      <div
        className={`bg-surface-container-lowest! p-4 rounded-lg border border-outline-variant! shadow-sm pz-group ${
          isActive ? 'personalization-active pz-edit-indicator' : 'personalization-active'
        }`}
        style={style}
      >
        <div className="pz-drag-handle-hover">
          <span className="material-symbols-outlined text-[14px]">drag_indicator</span>
        </div>
        <div className="text-[10px] uppercase tracking-wide text-slate-400! dark:text-slate-500! mb-1 font-mono">{node.id}</div>
        {kids.length > 0 ? (
          <div className="space-y-2 pl-2 border-l-2 border-outline-variant!">
            {kids.map((child) => (<EditCard key={child.id} node={child} activeId={activeId} />))}
          </div>
        ) : (
          <div className="h-10 rounded-lg bg-surface-container! border border-dashed border-outline-variant!" />
        )}
      </div>
    </PersonalizeWrapper>
  )
}
