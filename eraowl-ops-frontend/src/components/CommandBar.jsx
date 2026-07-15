import { useState, useEffect, useRef, useMemo } from 'react'
import { useNavigate } from 'react-router-dom'
import useAuthStore from '../store/authStore'
import { FUNCTIONAL_AREAS, getAccessibleModules } from '../config/moduleRegistry'

export default function CommandBar({ open, onClose }) {
  const [query, setQuery] = useState('')
  const [selectedIndex, setSelectedIndex] = useState(0)
  const inputRef = useRef(null)
  const resultsRef = useRef(null)
  const navigate = useNavigate()
  const privileges = useAuthStore((s) => s.privileges)

  const accessibleModules = useMemo(
    () => getAccessibleModules(privileges),
    [privileges]
  )

  const areaMap = useMemo(() => {
    const map = {}
    for (const area of FUNCTIONAL_AREAS) {
      map[area.id] = area
    }
    return map
  }, [])

  const results = useMemo(() => {
    if (!query.trim()) return accessibleModules

    const q = query.toLowerCase()
    return accessibleModules.filter((mod) => {
      if (mod.label.toLowerCase().includes(q)) return true
      if (mod.path.toLowerCase().includes(q)) return true
      if (mod.keywords.some((kw) => kw.includes(q))) return true
      const area = areaMap[mod.area]
      if (area && area.label.toLowerCase().includes(q)) return true
      return false
    })
  }, [query, accessibleModules, areaMap])

  useEffect(() => {
    setSelectedIndex(0)
  }, [query])

  useEffect(() => {
    if (open) {
      setQuery('')
      setSelectedIndex(0)
      setTimeout(() => inputRef.current?.focus(), 100)
    }
  }, [open])

  useEffect(() => {
    if (!open) return

    const handler = (e) => {
      if (e.key === 'Escape') {
        e.preventDefault()
        onClose()
      } else if (e.key === 'ArrowDown') {
        e.preventDefault()
        setSelectedIndex((prev) => Math.min(prev + 1, results.length - 1))
      } else if (e.key === 'ArrowUp') {
        e.preventDefault()
        setSelectedIndex((prev) => Math.max(prev - 1, 0))
      } else if (e.key === 'Enter' && results[selectedIndex]) {
        e.preventDefault()
        navigate(results[selectedIndex].path)
        onClose()
      }
    }

    window.addEventListener('keydown', handler)
    return () => window.removeEventListener('keydown', handler)
  }, [open, results, selectedIndex, navigate, onClose])

  useEffect(() => {
    if (!resultsRef.current) return
    const active = resultsRef.current.querySelector(
      `[data-index="${selectedIndex}"]`
    )
    if (active) {
      active.scrollIntoView({ block: 'nearest' })
    }
  }, [selectedIndex])

  if (!open) return null

  const groupedResults = results.reduce((acc, mod) => {
    const areaId = mod.area
    if (!acc[areaId]) acc[areaId] = []
    acc[areaId].push(mod)
    return acc
  }, {})

  const handleBackdropClick = () => {
    onClose()
  }

  const handleResultClick = (mod) => {
    navigate(mod.path)
    onClose()
  }

  return (
    <>
      <div
        className={`eods-cmdbar-backdrop ${open ? 'eods-cmdbar-backdrop--visible' : ''}`}
        onClick={handleBackdropClick}
      />

      <div
        className={`eods-cmdbar ${open ? 'eods-cmdbar--visible' : ''}`}
        role="dialog"
        aria-label="Command bar"
        aria-modal="true"
      >
        <div className="eods-cmdbar__input-area">
          <div className="eods-cmdbar__input-icon">
            <span className="material-symbols-outlined">search</span>
          </div>

          <input
            ref={inputRef}
            type="text"
            className="eods-cmdbar__input"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search modules, screens, actions..."
            aria-label="Search"
            autoComplete="off"
            spellCheck="false"
          />

          {query && (
            <button
              className="eods-cmdbar__clear"
              onClick={() => setQuery('')}
              aria-label="Clear search"
            >
              <span className="material-symbols-outlined">close</span>
            </button>
          )}

          <kbd className="eods-cmdbar__kbd">ESC</kbd>
        </div>

        <div className="eods-cmdbar__results" ref={resultsRef}>
          {results.length === 0 ? (
            <div className="eods-cmdbar__empty">
              <div className="eods-cmdbar__empty-icon">
                <span className="material-symbols-outlined">search_off</span>
              </div>
              <h3 className="eods-cmdbar__empty-title">No results found</h3>
              <p className="eods-cmdbar__empty-text">
                Try searching for &ldquo;{query}&rdquo; with different keywords
              </p>
            </div>
          ) : (
            Object.entries(groupedResults).map(([areaId, modules]) => {
              const area = areaMap[areaId]
              return (
                <div key={areaId} className="eods-cmdbar__group">
                  <div className="eods-cmdbar__group-header">
                    <div
                      className="eods-cmdbar__group-icon"
                      style={{ color: area?.color }}
                    >
                      <span className="material-symbols-outlined">
                        {area?.icon}
                      </span>
                    </div>
                    <span className="eods-cmdbar__group-title">
                      {area?.label}
                    </span>
                  </div>

                  {modules.map((mod) => {
                    const globalIndex = results.indexOf(mod)
                    const isSelected = globalIndex === selectedIndex

                    return (
                      <button
                        key={mod.id}
                        data-index={globalIndex}
                        className={`eods-cmdbar__item ${isSelected ? 'eods-cmdbar__item--selected' : ''}`}
                        onClick={() => handleResultClick(mod)}
                        onMouseEnter={() => setSelectedIndex(globalIndex)}
                        role="option"
                        aria-selected={isSelected}
                      >
                        <div className="eods-cmdbar__item-icon">
                          <span className="material-symbols-outlined">
                            {mod.icon}
                          </span>
                        </div>

                        <div className="eods-cmdbar__item-content">
                          <div className="eods-cmdbar__item-title">
                            {mod.label}
                          </div>
                          <div className="eods-cmdbar__item-subtitle">
                            {mod.path}
                          </div>
                        </div>

                        <div className="eods-cmdbar__item-action">
                          <kbd className="eods-cmdbar__kbd">↵</kbd>
                        </div>
                      </button>
                    )
                  })}
                </div>
              )
            })
          )}
        </div>

        <div className="eods-cmdbar__footer">
          <div className="eods-cmdbar__footer-hints">
            <span className="eods-cmdbar__hint">
              <kbd>↑</kbd>
              <kbd>↓</kbd>
              Navigate
            </span>
            <span className="eods-cmdbar__hint">
              <kbd>↵</kbd>
              Open
            </span>
            <span className="eods-cmdbar__hint">
              <kbd>esc</kbd>
              Close
            </span>
          </div>
          <span className="eods-cmdbar__footer-count">
            {results.length} result{results.length !== 1 ? 's' : ''}
          </span>
        </div>
      </div>
    </>
  )
}
