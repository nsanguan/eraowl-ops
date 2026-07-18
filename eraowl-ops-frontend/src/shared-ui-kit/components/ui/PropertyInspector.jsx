import { useCallback, useMemo } from 'react'
import usePersonalizeStore from '../../../store/usePersonalizeStore'
import { ColorPicker } from './ColorPicker'

/**
 * PropertyInspector
 *
 * A side drawer that appears when the user is in design mode and has
 * selected a component.  Provides controls for:
 *   - Font size (px spinner)
 *   - Font colour (native colour picker)
 *   - Grid column span (1–12)
 *   - Background colour
 *   - Padding
 *
 * Props:
 *   pageKey       — current page key (for save)
 *   targetUserId   — optional user UUID to save personalisation against
 *   targetRoleId   — optional role UUID to save personalisation against
 */

const SPAN_OPTIONS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

export default function PropertyInspector({
  pageKey,
  targetUserId = null,
  targetRoleId = null,
}) {
  const isDesignMode = usePersonalizeStore((s) => s.isDesignMode)
  const activeComponentId = usePersonalizeStore((s) => s.activeComponentId)
  const updateComponentStyles = usePersonalizeStore(
    (s) => s.updateComponentStyles
  )
  const moveComponent = usePersonalizeStore((s) => s.moveComponent)
  const setComponentSize = usePersonalizeStore((s) => s.setComponentSize)
  const savePersonalization = usePersonalizeStore(
    (s) => s.savePersonalization
  )
  const pageSchema = usePersonalizeStore((s) => s.pageSchema)

  // Derive current overrides for the active component
  const currentOverrides = useMemo(() => {
    if (!activeComponentId) return {}
    const walk = (node) => {
      if (!node || typeof node !== 'object') return null
      if (node.id === activeComponentId) return node.styles || {}
      if (node.children) {
        for (const child of node.children) {
          const found = walk(child)
          if (found) return found
        }
      }
      return null
    }
    return walk(pageSchema) || {}
  }, [activeComponentId, pageSchema])

  const handleChange = useCallback(
    (key, value) => {
      if (!activeComponentId) return
      updateComponentStyles(activeComponentId, { [key]: value })
    },
    [activeComponentId, updateComponentStyles]
  )

  const handleMove = useCallback(
    (direction) => {
      if (!activeComponentId) return
      moveComponent(activeComponentId, direction)
    },
    [activeComponentId, moveComponent]
  )

  const handleSize = useCallback(
    (dim, value) => {
      if (!activeComponentId) return
      const parsed = value === '' ? null : value
      setComponentSize(activeComponentId, { [dim]: parsed })
    },
    [activeComponentId, setComponentSize]
  )

  // Normalize the stored color key: inspector edits `fontColor`, wrapper
  // translates it to `color`. Read from either to stay in sync.
  const fontColor = currentOverrides.fontColor || currentOverrides.color || '#0f172a'

  const handleSave = useCallback(async () => {
    if (!pageKey) return
    const result = await savePersonalization(pageKey, targetUserId, targetRoleId)
    if (result) {
      // Flash a brief success indicator
      const btn = document.getElementById('pi-save-btn')
      if (btn) {
        btn.textContent = '✓ Saved'
        btn.style.background = '#16a34a'
        setTimeout(() => {
          btn.textContent = 'Save'
          btn.style.background = ''
        }, 1500)
      }
    }
  }, [pageKey, targetUserId, targetRoleId, savePersonalization])

  if (!isDesignMode) return null

  return (
    <div
      style={{
        position: 'fixed',
        right: 0,
        top: '3.5rem',
        width: '300px',
        height: 'calc(100vh - 3.5rem)',
        background: '#1e293b',
        borderLeft: '1px solid #334155',
        color: '#e2e8f0',
        zIndex: 100,
        display: 'flex',
        flexDirection: 'column',
        overflowY: 'auto',
        fontFamily: 'Inter, sans-serif',
        fontSize: '13px',
      }}
    >
      {/* Header */}
      <div
        style={{
          padding: '12px 16px',
          borderBottom: '1px solid #334155',
          fontWeight: 600,
          fontSize: '14px',
        }}
      >
        🎨 Property Inspector
      </div>

      {!activeComponentId ? (
        <div style={{ padding: '16px', color: '#94a3b8', fontStyle: 'italic' }}>
          Click a component in the page to inspect its properties.
        </div>
      ) : (
        <>
          {/* Active component info */}
          <div
            style={{
              padding: '10px 16px',
              background: '#0f172a',
              fontSize: '12px',
              fontFamily: 'JetBrains Mono, monospace',
              wordBreak: 'break-all',
            }}
          >
            {activeComponentId}
          </div>

          {/* Controls */}
          <div style={{ padding: '16px', display: 'flex', flexDirection: 'column', gap: '14px' }}>
            {/* Font Size */}
            <ControlRow label="Font Size">
              <input
                type="number"
                min={8}
                max={72}
                value={parseInt(currentOverrides.fontSize, 10) || 14}
                onChange={(e) => handleChange('fontSize', `${e.target.value}px`)}
                style={inputStyle}
              />
              <span style={{ color: '#94a3b8', marginLeft: 4 }}>px</span>
            </ControlRow>

            {/* Font Colour */}
            <ControlRow label="Font Colour">
              <div style={{ width: 160 }}>
                <ColorPicker
                  value={fontColor}
                  onChange={(c) => handleChange('fontColor', c)}
                />
              </div>
            </ControlRow>

            {/* Background Colour */}
            <ControlRow label="Background">
              <div style={{ width: 160 }}>
                <ColorPicker
                  value={currentOverrides.background || '#ffffff'}
                  onChange={(c) => handleChange('background', c)}
                />
              </div>
            </ControlRow>

            {/* Grid Column Span */}
            <ControlRow label="Grid Span">
              <select
                value={currentOverrides.gridSpan || ''}
                onChange={(e) => handleChange('gridSpan', e.target.value)}
                style={selectStyle}
              >
                <option value="">Auto</option>
                {SPAN_OPTIONS.map((n) => (
                  <option key={n} value={n}>
                    {n} / 12
                  </option>
                ))}
              </select>
            </ControlRow>

            {/* Padding */}
            <ControlRow label="Padding">
              <input
                type="number"
                min={0}
                max={48}
                value={parseInt(currentOverrides.padding, 10) || 0}
                onChange={(e) => handleChange('padding', `${e.target.value}px`)}
                style={inputStyle}
              />
              <span style={{ color: '#94a3b8', marginLeft: 4 }}>px</span>
            </ControlRow>

            {/* Position — move field up / down within its group */}
            <ControlRow label="Position">
              <div style={{ display: 'flex', gap: 6 }}>
                <button onClick={() => handleMove(-1)} style={miniBtn} title="Move up">
                  ↑ Up
                </button>
                <button onClick={() => handleMove(1)} style={miniBtn} title="Move down">
                  ↓ Down
                </button>
              </div>
            </ControlRow>

            {/* Size — width / height */}
            <ControlRow label="Width">
              <input
                type="text"
                placeholder="auto"
                value={currentOverrides.width || ''}
                onChange={(e) => handleSize('width', e.target.value)}
                style={{ ...inputStyle, width: 80 }}
              />
            </ControlRow>
            <ControlRow label="Height">
              <input
                type="text"
                placeholder="auto"
                value={currentOverrides.height || ''}
                onChange={(e) => handleSize('height', e.target.value)}
                style={{ ...inputStyle, width: 80 }}
              />
            </ControlRow>
          </div>

          {/* Save button */}
          <div style={{ padding: '12px 16px', borderTop: '1px solid #334155', marginTop: 'auto' }}>
            <button
              id="pi-save-btn"
              onClick={handleSave}
              style={{
                width: '100%',
                padding: '8px 16px',
                background: '#3b82f6',
                color: '#fff',
                border: 'none',
                borderRadius: 6,
                fontWeight: 600,
                cursor: 'pointer',
                fontSize: 13,
              }}
            >
              Save
            </button>
          </div>
        </>
      )}
    </div>
  )
}

// ── Small helpers ──

function ControlRow({ label, children }) {
  return (
    <div
      style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
      }}
    >
      <span style={{ color: '#94a3b8', fontSize: 12, minWidth: 80 }}>
        {label}
      </span>
      <div style={{ display: 'flex', alignItems: 'center' }}>{children}</div>
    </div>
  )
}

const inputStyle = {
  width: 56,
  padding: '4px 6px',
  background: '#0f172a',
  color: '#e2e8f0',
  border: '1px solid #334155',
  borderRadius: 4,
  fontSize: 12,
  outline: 'none',
}

const selectStyle = {
  ...inputStyle,
  width: 80,
}

const miniBtn = {
  padding: '4px 10px',
  background: '#334155',
  color: '#e2e8f0',
  border: '1px solid #475569',
  borderRadius: 4,
  fontSize: 12,
  cursor: 'pointer',
}