import { Link, useLocation } from 'react-router-dom'
import { FUNCTIONAL_AREAS } from '../config/moduleRegistry'

export default function SidebarNav({
  activeArea,
  groupedModules,
  onAreaChange,
  user,
  userInitials,
}) {
  const location = useLocation()
  const areaKeys = Object.keys(groupedModules)
  const currentArea = groupedModules[activeArea]
  const currentMeta = FUNCTIONAL_AREAS.find((a) => a.id === activeArea)
  const otherAreas = areaKeys.filter((id) => id !== activeArea)

  const userRoles = user?.roles?.map((r) => r.role_name).join(', ') || 'User'

  return (
    <aside className="eods-snav">
      <div className="eods-snav__header">
        <div className="eods-snav__brand">
          <div className="eods-snav__logo">EO</div>
          <div className="eods-snav__brand-text">
            <div className="eods-snav__brand-title">EraOwl-OPS</div>
            <div className="eods-snav__brand-subtitle">AI ERP</div>
          </div>
        </div>
      </div>

      <div className="eods-snav__switcher">
        <div className="eods-modsw">
          <button
            className="eods-modsw__trigger"
            onClick={() => {
              const nextIndex =
                (areaKeys.indexOf(activeArea) + 1) % areaKeys.length
              onAreaChange(areaKeys[nextIndex])
            }}
            title={`Current: ${currentMeta?.label}. Click to switch.`}
          >
            <div
              className="eods-modsw__trigger-icon"
              style={{ backgroundColor: `${currentMeta?.color}20` }}
            >
              <span
                className="material-symbols-outlined"
                style={{ color: currentMeta?.color }}
              >
                {currentMeta?.icon}
              </span>
            </div>
            <div className="eods-modsw__trigger-content">
              <div className="eods-modsw__trigger-title">
                {currentMeta?.label}
              </div>
              <div className="eods-modsw__trigger-subtitle">
                {currentArea?.modules?.length || 0} module
                {(currentArea?.modules?.length || 0) !== 1 ? 's' : ''}
              </div>
            </div>
            <div className="eods-modsw__trigger-chevron">
              <span className="material-symbols-outlined">swap_horiz</span>
            </div>
          </button>
        </div>
      </div>

      <nav className="eods-snav__body">
        {currentArea && currentMeta && (
          <div className="eods-snav__section">
            <div className="eods-snav__section-header">
              <div
                className="eods-snav__section-icon"
                style={{ color: currentMeta.color }}
              >
                <span className="material-symbols-outlined">
                  {currentMeta.icon}
                </span>
              </div>
              <span className="eods-snav__section-title">
                {currentMeta.label}
              </span>
            </div>

            {currentArea.modules.map((mod) => {
              const isActive =
                location.pathname === mod.path ||
                location.pathname.startsWith(mod.path + '/')

              return (
                <Link
                  key={mod.id}
                  to={mod.path}
                  className={`eods-snav__link ${isActive ? 'eods-snav__link--active' : ''}`}
                >
                  <span className="eods-snav__link-icon">
                    <span className="material-symbols-outlined">{mod.icon}</span>
                  </span>
                  <span className="eods-snav__link-text">{mod.label}</span>
                </Link>
              )
            })}
          </div>
        )}

        {otherAreas.length > 0 && (
          <div className="eods-snav__quick-areas">
            <div className="eods-snav__quick-title">Other Areas</div>
            {otherAreas.map((areaId) => {
              const area = groupedModules[areaId]
              const meta = FUNCTIONAL_AREAS.find((a) => a.id === areaId)

              return (
                <button
                  key={areaId}
                  className="eods-snav__quick-item"
                  onClick={() => onAreaChange(areaId)}
                >
                  <span
                    className="eods-snav__quick-item-icon"
                    style={{ color: meta?.color }}
                  >
                    <span className="material-symbols-outlined">
                      {meta?.icon}
                    </span>
                  </span>
                  <span className="eods-snav__quick-item-text">
                    {meta?.label}
                  </span>
                  <span className="eods-snav__quick-item-count">
                    {area.modules.length}
                  </span>
                </button>
              )
            })}
          </div>
        )}

        {areaKeys.length === 0 && (
          <div className="eods-snav__empty">
            <div className="eods-snav__empty-icon">
              <span className="material-symbols-outlined">lock</span>
            </div>
            <p className="eods-snav__empty-text">
              No modules available for your role.
            </p>
          </div>
        )}
      </nav>

      <div className="eods-snav__footer">
        <div className="eods-snav__avatar">{userInitials}</div>
        <div className="eods-snav__user-info">
          <div className="eods-snav__user-name">{user?.username || 'User'}</div>
          <div className="eods-snav__user-role">{userRoles}</div>
        </div>
      </div>
    </aside>
  )
}
