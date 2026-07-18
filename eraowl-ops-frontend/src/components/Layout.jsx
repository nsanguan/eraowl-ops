import { useState, useEffect, useMemo, useCallback } from 'react'
import { Outlet, useLocation, useNavigate } from 'react-router-dom'
import useAuthStore from '../store/authStore'
import usePersonalizeStore from '../store/usePersonalizeStore'
import Header from './Header'
import SidebarNav from './SidebarNav'
import CommandBar from './CommandBar'
import PropertyInspector from '../shared-ui-kit/components/ui/PropertyInspector'
import { ErrorBoundary } from '../shared-ui-kit/components/layout/ErrorBoundary'
import { getModulesByArea } from '../config/moduleRegistry'

export default function Layout() {
  const location = useLocation()
  const navigate = useNavigate()
  const { user, privileges } = useAuthStore()
  const isDesignMode = usePersonalizeStore((s) => s.isDesignMode)
  const toggleDesignMode = usePersonalizeStore((s) => s.toggleDesignMode)
  const userInitials = user?.username
    ? user.username.substring(0, 2).toUpperCase()
    : 'EU'

  const [activeArea, setActiveArea] = useState(null)
  const [commandBarOpen, setCommandBarOpen] = useState(false)
  const [sidebarOpen, setSidebarOpen] = useState(true)

  // Whether the current user may use the in-context personalization editor
  const canPersonalize = useMemo(
    () =>
      (privileges || []).some(
        (p) =>
          p.module === 'admin' &&
          (p.action === 'personalize' || p.action === 'manage')
      ),
    [privileges]
  )

  const groupedModules = useMemo(
    () => getModulesByArea(privileges),
    [privileges]
  )
  const areaKeys = useMemo(() => Object.keys(groupedModules), [groupedModules])

  useEffect(() => {
    if (areaKeys.length === 0) return

    const currentModule = areaKeys.find((areaId) => {
      const mods = groupedModules[areaId].modules
      return mods.some(
        (m) =>
          location.pathname === m.path ||
          location.pathname.startsWith(m.path + '/')
      )
    })

    if (currentModule) {
      setActiveArea(currentModule)
    } else if (!activeArea || !groupedModules[activeArea]) {
      setActiveArea(areaKeys[0])
    }
  }, [location.pathname, areaKeys, groupedModules])

  useEffect(() => {
    const handler = (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault()
        setCommandBarOpen((prev) => !prev)
      }
      // Ctrl+Shift+P — toggle design mode
      if ((e.metaKey || e.ctrlKey) && e.shiftKey && (e.key === 'p' || e.key === 'P')) {
        e.preventDefault()
        toggleDesignMode()
      }
    }
    window.addEventListener('keydown', handler)
    return () => window.removeEventListener('keydown', handler)
  }, [])

  const handleAreaChange = useCallback(
    (areaId) => {
      setActiveArea(areaId)
      const mods = groupedModules[areaId]?.modules
      if (mods && mods.length > 0) {
        const matchingMod = mods.find(
          (m) =>
            location.pathname === m.path ||
            location.pathname.startsWith(m.path + '/')
        )
        if (!matchingMod) {
          navigate(mods[0].path)
        }
      }
    },
    [groupedModules, navigate, location.pathname]
  )

  const handleNavigate = useCallback(
    (path) => {
      navigate(path)
    },
    [navigate]
  )

  return (
    <div className="flex h-screen">
      <SidebarNav
        activeArea={activeArea}
        groupedModules={groupedModules}
        onAreaChange={handleAreaChange}
        user={user}
        userInitials={userInitials}
        collapsed={!sidebarOpen}
      />

      <div className={`flex-1 flex flex-col ${sidebarOpen ? 'ml-60' : 'ml-0'}`}>
        <Header
          onNavigate={handleNavigate}
          userLabel={user?.username ?? 'User'}
          userInitials={userInitials}
          onOpenCommandBar={() => setCommandBarOpen(true)}
          isDesignMode={isDesignMode}
          onToggleDesignMode={toggleDesignMode}
          canPersonalize={canPersonalize}
        />

        <main className="mt-14 p-6 h-[calc(100vh-3.5rem)] overflow-y-auto bg-surface-container-lowest">
          <ErrorBoundary>
            <Outlet />
          </ErrorBoundary>
        </main>

        {/* Design mode toggle button */}
        <button
          onClick={toggleDesignMode}
          title="Toggle Design Mode (Ctrl+Shift+P)"
          style={{
            position: 'fixed',
            bottom: 16,
            right: isDesignMode ? 316 : 16,
            zIndex: 200,
            width: 40,
            height: 40,
            borderRadius: '50%',
            border: 'none',
            background: isDesignMode ? '#3b82f6' : '#334155',
            color: '#fff',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: 18,
            boxShadow: '0 2px 8px rgba(0,0,0,0.3)',
            transition: 'right 0.2s ease',
          }}
        >
          {isDesignMode ? '✕' : '🎨'}
        </button>

        {/* Sidebar show/hide toggle switch */}
        <div
          className="nav-toggle-switch"
          data-on={sidebarOpen}
          onClick={() => setSidebarOpen((v) => !v)}
          title={sidebarOpen ? 'Hide navigation menu' : 'Show navigation menu'}
          style={{ left: sidebarOpen ? 16 : 16 }}
        >
          <span className="nav-toggle-switch__track">
            <span className="nav-toggle-switch__thumb" />
          </span>
          <span className="nav-toggle-switch__label">
            {sidebarOpen ? 'Menu' : 'Show Menu'}
          </span>
        </div>
      </div>

      <PropertyInspector />

      <CommandBar
        open={commandBarOpen}
        onClose={() => setCommandBarOpen(false)}
      />
    </div>
  )
}
