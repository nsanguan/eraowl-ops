import { useCallback } from 'react'
import usePersonalizeStore from '../../../store/usePersonalizeStore'

/**
 * PersonalizeWrapper
 *
 * Wraps any child element.  When `isDesignMode` is active it renders a dashed
 * blue border and intercepts clicks to set the active component for the
 * PropertyInspector.
 *
 * Props:
 *   componentId  — unique identifier for this element (e.g. 'field:item_code')
 *   children     — React children
 *   className    — extra classes forwarded to the outer div
 *   style        — base style object (merged with design-mode overrides)
 */

export default function PersonalizeWrapper({
  componentId,
  children,
  className = '',
  style = {},
}) {
  const isDesignMode = usePersonalizeStore((s) => s.isDesignMode)
  const activeComponentId = usePersonalizeStore((s) => s.activeComponentId)
  const setActiveComponent = usePersonalizeStore((s) => s.setActiveComponent)
  const pageSchema = usePersonalizeStore((s) => s.pageSchema)

  // Read per-component overrides from the live schema (tree walk by id)
  const componentOverrides = useCallback(() => {
    const walk = (node) => {
      if (!node || typeof node !== 'object') return null
      if (node.id === componentId) return node.styles || {}
      if (node.children) {
        for (const child of node.children) {
          const found = walk(child)
          if (found) return found
        }
      }
      return null
    }
    return walk(pageSchema)
  }, [componentId, pageSchema])

  const rawOverrides = componentOverrides() || {}
  const isActive = activeComponentId === componentId

  // Translate high-level style keys into real CSS. `gridSpan` is converted to
  // a CSS grid column span; `fontColor` is normalized to `color`.
  const overrides = { ...rawOverrides }
  if (overrides.gridSpan) {
    overrides.gridColumn = `span ${parseInt(overrides.gridSpan, 10)} / span ${parseInt(overrides.gridSpan, 10)}`
    delete overrides.gridSpan
  }
  if (overrides.fontColor) {
    overrides.color = overrides.fontColor
    delete overrides.fontColor
  }

  if (!isDesignMode) {
    // Normal render — apply persisted overrides (fontSize/color/etc.) silently
    return (
      <div className={className} style={{ ...style, ...overrides }}>
        {children}
      </div>
    )
  }

  // Design mode — add border + click handler
  const mergedStyle = {
    ...style,
    ...overrides,
    outline: isActive ? '2px dashed #3b82f6' : '1px dashed #94a3b8',
    outlineOffset: '2px',
    cursor: 'pointer',
    position: 'relative',
    transition: 'outline 0.15s ease',
  }

  const handleClick = (e) => {
    e.stopPropagation()
    setActiveComponent(componentId)
  }

  return (
    <div
      className={className}
      style={mergedStyle}
      onClick={handleClick}
      data-personalize-id={componentId}
      title={`[Design] ${componentId} — click to edit`}
    >
      {/* Component label badge */}
      <span
        style={{
          position: 'absolute',
          top: '-10px',
          left: '4px',
          fontSize: '10px',
          lineHeight: '1',
          padding: '1px 6px',
          borderRadius: '4px',
          background: isActive ? '#3b82f6' : '#94a3b8',
          color: '#fff',
          zIndex: 50,
          pointerEvents: 'none',
        }}
      >
        {componentId}
      </span>
      {children}
    </div>
  )
}