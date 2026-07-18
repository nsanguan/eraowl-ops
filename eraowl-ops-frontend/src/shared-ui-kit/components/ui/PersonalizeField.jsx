import { createContext, useContext } from 'react'
import usePersonalizeStore from '../../../store/usePersonalizeStore'

/**
 * PersonalizeField
 *
 * APEX-style field-level personalization wrapper for form fields inside
 * detail/edit pages (modals, drawers). Wraps a labelled field and honors
 * component meta overrides persisted in the personalization tree:
 *   - meta.visible  : hide the whole field (false)
 *   - meta.label    : override the field label text
 *   - meta.required : force the field required (true) / optional (false)
 *
 * The resolved `label` and `required` are exposed via context so the inner
 * <input>/control can render the override without prop drilling.
 *
 * Props:
 *   componentId — unique id, e.g. 'field:user.username'
 *   label       — default label text
 *   required    — default required flag
 *   children    — (labelText, requiredOverride) => ReactNode  (render prop)
 *   className   — outer wrapper classes
 */

const FieldMetaContext = createContext({ label: null, required: null })

export function useFieldMeta() {
  return useContext(FieldMetaContext)
}

export default function PersonalizeField({
  componentId,
  label,
  required = false,
  children,
  className = '',
}) {
  const isDesignMode = usePersonalizeStore((s) => s.isDesignMode)
  const activeComponentId = usePersonalizeStore((s) => s.activeComponentId)
  const setActiveComponent = usePersonalizeStore((s) => s.setActiveComponent)

  const meta = usePersonalizeStore((s) => {
    const find = (node) => {
      if (!node || typeof node !== 'object') return null
      if (node.id === componentId) return node.meta || null
      if (node.children) {
        for (const c of node.children) {
          const f = find(c)
          if (f) return f
        }
      }
      return null
    }
    return find(s.pageSchema)
  }) || {}

  const visible = meta.visible !== false
  const resolvedLabel = meta.label || label
  const resolvedRequired = meta.required === undefined ? required : meta.required
  const isActive = activeComponentId === componentId

  if (!visible && !isDesignMode) return null

  const handleClick = (e) => {
    e.stopPropagation()
    setActiveComponent(componentId)
  }

  const wrapperStyle = isDesignMode
    ? {
        outline: isActive ? '2px dashed #3b82f6' : '1px dashed #94a3b8',
        outlineOffset: '2px',
        cursor: 'pointer',
        position: 'relative',
      }
    : undefined

  return (
    <div className={className} style={wrapperStyle} onClick={isDesignMode ? handleClick : undefined} data-personalize-id={isDesignMode ? componentId : undefined}>
      {isDesignMode && (
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
      )}
      <FieldMetaContext.Provider value={{ label: resolvedLabel, required: resolvedRequired }}>
        {typeof children === 'function' ? children(resolvedLabel, resolvedRequired) : children}
      </FieldMetaContext.Provider>
    </div>
  )
}
