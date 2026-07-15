import { useState, useRef, useEffect } from 'react'
import { FUNCTIONAL_AREAS } from '../config/moduleRegistry'

export default function ModuleSwitcher({
  activeArea,
  groupedModules,
  onAreaChange,
}) {
  const [isOpen, setIsOpen] = useState(false)
  const containerRef = useRef(null)

  const areaKeys = Object.keys(groupedModules)
  const currentArea = groupedModules[activeArea]
  const currentMeta = FUNCTIONAL_AREAS.find((a) => a.id === activeArea)

  useEffect(() => {
    if (!isOpen) return

    const handleClickOutside = (e) => {
      if (containerRef.current && !containerRef.current.contains(e.target)) {
        setIsOpen(false)
      }
    }

    const handleEscape = (e) => {
      if (e.key === 'Escape') {
        setIsOpen(false)
      }
    }

    document.addEventListener('mousedown', handleClickOutside)
    document.addEventListener('keydown', handleEscape)

    return () => {
      document.removeEventListener('mousedown', handleClickOutside)
      document.removeEventListener('keydown', handleEscape)
    }
  }, [isOpen])

  const handleSelect = (areaId) => {
    onAreaChange(areaId)
    setIsOpen(false)
  }

  if (!currentMeta || areaKeys.length === 0) {
    return null
  }

  return (
    <div className="eods-modsw" ref={containerRef}>
      <button
        className="eods-modsw__trigger"
        onClick={() => setIsOpen(!isOpen)}
        aria-expanded={isOpen}
        aria-haspopup="listbox"
      >
        <div
          className="eods-modsw__trigger-icon"
          style={{ backgroundColor: `${currentMeta.color}20` }}
        >
          <span
            className="material-symbols-outlined"
            style={{ color: currentMeta.color }}
          >
            {currentMeta.icon}
          </span>
        </div>

        <div className="eods-modsw__trigger-content">
          <div className="eods-modsw__trigger-title">{currentMeta.label}</div>
          <div className="eods-modsw__trigger-subtitle">
            {currentArea?.modules?.length || 0} module
            {(currentArea?.modules?.length || 0) !== 1 ? 's' : ''}
          </div>
        </div>

        <div className="eods-modsw__trigger-chevron">
          <span className="material-symbols-outlined">expand_more</span>
        </div>
      </button>

      <div
        className={`eods-modsw__menu ${isOpen ? 'eods-modsw__menu--open' : ''}`}
        role="listbox"
        aria-label="Select functional area"
      >
        {areaKeys.map((areaId) => {
          const area = groupedModules[areaId]
          const meta = FUNCTIONAL_AREAS.find((a) => a.id === areaId)
          const isActive = areaId === activeArea

          return (
            <button
              key={areaId}
              className={`eods-modsw__item ${isActive ? 'eods-modsw__item--active' : ''}`}
              onClick={() => handleSelect(areaId)}
              role="option"
              aria-selected={isActive}
            >
              <div
                className="eods-modsw__item-icon"
                style={{ backgroundColor: `${meta.color}20` }}
              >
                <span
                  className="material-symbols-outlined"
                  style={{ color: meta.color }}
                >
                  {meta.icon}
                </span>
              </div>

              <div className="eods-modsw__item-content">
                <div className="eods-modsw__item-title">{meta.label}</div>
                <div className="eods-modsw__item-subtitle">
                  {area.modules.length} module{area.modules.length !== 1 ? 's' : ''}
                </div>
              </div>

              {isActive && (
                <div className="eods-modsw__item-check">
                  <span className="material-symbols-outlined">check_circle</span>
                </div>
              )}
            </button>
          )
        })}
      </div>
    </div>
  )
}
