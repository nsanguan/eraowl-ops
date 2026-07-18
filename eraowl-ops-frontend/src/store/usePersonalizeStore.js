import { create } from 'zustand'
import api from '../api/client'

const usePersonalizeStore = create((set, get) => ({
  // ── State ──
  isDesignMode: false,
  activeComponentId: null,
  pageSchema: {},        // editable draft (template + unsaved changes)
  baseSchema: {},        // immutable base template, kept for delta calc

  // APEX-style Global Theme Roller tokens (applied as CSS variables on :root)
  themeTokens: null,     // { primary, surface, font, radius, spacing } or null = default
  themeSource: 'default',

  // ── Actions ──

  /** Toggle design mode on/off (clears selection when exiting) */
  toggleDesignMode: () =>
    set((s) => ({
      isDesignMode: !s.isDesignMode,
      activeComponentId: !s.isDesignMode ? s.activeComponentId : null,
    })),

  /** Set the currently inspected component */
  setActiveComponent: (id) => set({ activeComponentId: id }),

  /** APEX-style component metadata (beyond CSS styles): visibility, label,
   *  required flag, display order. Stored on node.meta and persisted in the
   *  same override tree alongside node.styles. */
  updateComponentMeta: (id, metaPatch) =>
    set((s) => {
      const pageSchema = { ...s.pageSchema }
      const walk = (node) => {
        if (!node || typeof node !== 'object') return
        if (node.id === id) {
          node.meta = { ...(node.meta || {}), ...metaPatch }
          return
        }
        if (node.children) node.children.forEach(walk)
      }
      walk(pageSchema)
      return { pageSchema }
    }),

  setComponentVisibility: (id, visible) => get().updateComponentMeta(id, { visible }),
  setComponentLabel: (id, label) => get().updateComponentMeta(id, { label }),
  setComponentRequired: (id, required) => get().updateComponentMeta(id, { required }),

  /** Apply global theme tokens (Theme Roller). Persisted separately. */
  applyThemeTokens: (tokens) => set({ themeTokens: tokens, themeSource: 'custom' }),
  resetThemeTokens: () => set({ themeTokens: null, themeSource: 'default' }),

  /** Update a component's style overrides (delta merge) */
  updateComponentStyles: (id, styleObject) =>
    set((s) => {
      const pageSchema = { ...s.pageSchema }
      const walk = (node) => {
        if (!node || typeof node !== 'object') return
        if (node.id === id) {
          node.styles = { ...(node.styles || {}), ...styleObject }
          return
        }
        if (node.children) {
          node.children.forEach(walk)
        }
      }
      walk(pageSchema)
      return { pageSchema }
    }),

  /** Reorder a component within its parent's children list.
   *  direction: -1 (move up / earlier) or +1 (move down / later).
   *  No-op at the boundaries.  Root-level components live in the top
   *  `children` array. */
  moveComponent: (id, direction) =>
    set((s) => {
      const pageSchema = { ...s.pageSchema }
      const swap = (siblings) => {
        const idx = siblings.findIndex((n) => n.id === id)
        if (idx === -1) return false
        const target = idx + direction
        if (target < 0 || target >= siblings.length) return true // found but bounded
        ;[siblings[idx], siblings[target]] = [siblings[target], siblings[idx]]
        return true
      }
      const walk = (node) => {
        if (!node || typeof node !== 'object') return false
        if (node.children && swap(node.children)) return true
        if (node.children) return node.children.some(walk)
        return false
      }
      // try top-level children first
      if (!pageSchema.children || !swap(pageSchema.children)) {
        walk(pageSchema)
      }
      return { pageSchema }
    }),

  /** Set explicit width/height (px or %) on a component. */
  setComponentSize: (id, { width, height } = {}) =>
    set((s) => {
      const patch = {}
      if (width != null) patch.width = width
      if (height != null) patch.height = height
      const pageSchema = { ...s.pageSchema }
      const walk = (node) => {
        if (!node || typeof node !== 'object') return
        if (node.id === id) {
          node.styles = { ...(node.styles || {}), ...patch }
          return
        }
        if (node.children) node.children.forEach(walk)
      }
      walk(pageSchema)
      return { pageSchema }
    }),

  /** Catalogue of all personalizable pages (standard templates). */
  listTemplates: async (search) => {
    try {
      const { data } = await api.get('/admin/ui-personalize/templates', {
        params: search ? { search } : {},
      })
      return data || []
    } catch (err) {
      console.error('Failed to list templates:', err)
      return []
    }
  },

  /** Apply a fixed set of styles to every component node on the page
   *  (skips the source node so its own values are the seed). */
  applyStylesToAll: (styles, sourceId = null) =>
    set((s) => {
      const pageSchema = { ...s.pageSchema }
      const apply = (node) => {
        if (!node || typeof node !== 'object') return
        if (!(sourceId && node.id === sourceId) && node.id != null) {
          node.styles = { ...(node.styles || {}), ...styles }
        }
        if (node.children) node.children.forEach(apply)
      }
      apply(pageSchema)
      return { pageSchema }
    }),

  /** "APPLY GLOBAL" — copy the active component's theme styles (color,
   *  fontFamily, fontSize, background, density) onto every component node in
   *  the current page layout. */
  applyGlobalTheme: (sourceId) =>
    set((s) => {
      const id = sourceId || s.activeComponentId
      if (!id) return {}
      const pageSchema = { ...s.pageSchema }
      let source = null
      const find = (node) => {
        if (!node || typeof node !== 'object') return
        if (node.id === id) { source = node.styles || {}; return }
        if (node.children) node.children.forEach(find)
      }
      find(pageSchema)
      if (!source) return {}
      const THEME_KEYS = [
        'color', 'fontColor', 'fontFamily', 'fontSize',
        'background', 'width', 'height', 'gap', 'padding', 'borderRadius',
      ]
      const theme = Object.fromEntries(
        Object.entries(source).filter(([k]) => THEME_KEYS.includes(k))
      )
      const apply = (node) => {
        if (!node || typeof node !== 'object') return
        if (node.id !== id && node.id != null) {
          node.styles = { ...(node.styles || {}), ...theme }
        }
        if (node.children) node.children.forEach(apply)
      }
      apply(pageSchema)
      return { pageSchema }
    }),

  /** Grid layout preset for a (container) component: stacked / columns / bento. */
  setGridLayout: (mode, targetId = null) => {
    const id = targetId || null
    const styles =
      mode === 'columns'
        ? { display: 'grid', gridTemplateColumns: 'repeat(2, minmax(0, 1fr))' }
        : mode === 'bento'
        ? { display: 'grid', gridTemplateColumns: 'repeat(12, minmax(0, 1fr))' }
        : { display: 'block' }
    if (id) {
      updateComponentStyles(id, styles)
      return
    }
    // no target → broadcast to all top-level containers
    get().applyStylesToAll(styles)
  },

  /** "GENERATE AI PRESET" — apply a polished, balanced preset across the page. */
  applyPreset: () =>
    set((s) => {
      const pageSchema = { ...s.pageSchema }
      const preset = {
        fontFamily: "'Inter', sans-serif",
        color: '#0d1c2e',
        borderRadius: '8px',
        gap: '16px',
      }
      const apply = (node) => {
        if (!node || typeof node !== 'object') return
        if (node.id != null) node.styles = { ...(node.styles || {}), ...preset }
        if (node.children) node.children.forEach(apply)
      }
      apply(pageSchema)
      return { pageSchema }
    }),


  /** Load a page's BASE template (read-only source) into the editable draft.
   *  Used by the admin Personalize Management page to edit a page's layout
   *  directly.  baseSchema is kept as the delta reference. */
  loadTemplate: async (pageKey) => {
    try {
      const { data } = await api.get(
        `/admin/ui-personalize/templates/${encodeURIComponent(pageKey)}`
      )
      const layout = data.base_layout_json || {}
      // Deep-clone the base reference: pageSchema is the editable draft and
      // baseSchema is the immutable delta baseline. A shallow copy would share
      // nested node objects, so mutating a node's meta/styles in the draft
      // would also mutate the baseline and the computed save delta would come
      // out empty.
      set({ pageSchema: structuredClone(layout), baseSchema: structuredClone(layout) })
      return data
    } catch (err) {
      console.error('Failed to load template:', err)
      return null
    }
  },

  /** Load a page's personalisation from the backend.
   *  The merged layout becomes the editable draft (pageSchema) AND the
   *  immutable reference (baseSchema) used to compute the save delta. */
  loadPersonalization: async (pageKey) => {
    try {
      const { data } = await api.get('/admin/ui-personalize/load', {
        params: { page_key: pageKey },
      })
      const layout = data.layout || {}
      set({ pageSchema: structuredClone(layout), baseSchema: structuredClone(layout) })
      return data
    } catch (err) {
      console.error('Failed to load personalization:', err)
      return null
    }
  },

  /** Compute the diff between a base layout and the current (edited) layout.
   *  Only nodes whose styles OR meta differ from base are kept — matches the
   *  backend delta model so stored overrides carry just the changes. */
  computeDelta: (base, current) => {
    if (!base || !current || !current.children) return current
    const baseById = {}
    const index = (node) => {
      if (!node || typeof node !== 'object') return
      if (node.id != null) baseById[node.id] = { styles: node.styles || {}, meta: node.meta || {} }
      ;(node.children || []).forEach(index)
    }
    index(base)
    const diff = (node) => {
      if (!node || typeof node !== 'object') return null
      const baseEntry = baseById[node.id] || { styles: {}, meta: {} }
      const curStyles = node.styles || {}
      const diffStyles = Object.fromEntries(
        Object.entries(curStyles).filter(([k, v]) => !_eq(baseEntry.styles[k], v))
      )
      const curMeta = node.meta || {}
      const diffMeta = Object.fromEntries(
        Object.entries(curMeta).filter(([k, v]) => !_eq(baseEntry.meta[k], v))
      )
      const keptChildren = (node.children || [])
        .map(diff)
        .filter((c) => c !== null)
      if (!Object.keys(diffStyles).length && !Object.keys(diffMeta).length && !keptChildren.length) return null
      const result = { id: node.id }
      if (Object.keys(diffStyles).length) result.styles = diffStyles
      if (Object.keys(diffMeta).length) result.meta = diffMeta
      if (keptChildren.length) result.children = keptChildren
      return result
    }
    return {
      children: (current.children || [])
        .map(diff)
        .filter((c) => c !== null),
    }
  },

  /** Save current overrides to the backend.
   *  When asDelta is true, only the diff vs. the base template is sent
   *  (In-Context Editor "Copy Template to Personalize" flow). */
  savePersonalization: async (pageKey, targetUserId, targetRoleId, opts = {}) => {
    const { pageSchema, baseSchema } = get()
    const asDelta = opts.asDelta !== false
    const payload = asDelta && baseSchema ? get().computeDelta(baseSchema, pageSchema) : pageSchema
    try {
      const { data } = await api.put('/admin/ui-personalize/save', {
        page_key: pageKey,
        target_user_id: targetUserId || null,
        target_role_id: targetRoleId || null,
        override_json: payload,
        as_delta: asDelta,
      })
      return data
    } catch (err) {
      console.error('Failed to save personalization:', err)
      return null
    }
  },

  /** Load the saved global theme tokens for the current user/role. */
  loadTheme: async () => {
    try {
      const { data } = await api.get('/admin/ui-personalize/theme')
      if (data && data.tokens) set({ themeTokens: data.tokens, themeSource: data.source || 'custom' })
      return data
    } catch (err) {
      console.error('Failed to load theme:', err)
      return null
    }
  },

  /** Persist global theme tokens (Theme Roller) for a target user/role. */
  saveTheme: async (targetUserId, targetRoleId) => {
    const { themeTokens } = get()
    try {
      const { data } = await api.put('/admin/ui-personalize/theme', {
        target_user_id: targetUserId || null,
        target_role_id: targetRoleId || null,
        tokens: themeTokens,
      })
      return data
    } catch (err) {
      console.error('Failed to save theme:', err)
      return null
    }
  },
}))

const _eq = (a, b) => JSON.stringify(a) === JSON.stringify(b)

export default usePersonalizeStore