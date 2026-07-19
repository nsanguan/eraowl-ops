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

const MOBILE_BREAKPOINT = 768

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

  // Sidebar persistence: desktop collapse vs mobile drawer open state.
  const [desktopCollapsed, setDesktopCollapsed] = useState(() => {
    const saved = localStorage.getItem('sidebar.collapsed')
    return saved === null ? false : saved === 'true'
  })
  const [mobileOpen, setMobileOpen] = useState(false)
  const [isMobile, setIsMobile] = useState(
    () =>
      typeof window !== 'undefined' &&
      window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT - 1}px)`).matches
  )

  useEffect(() => {
    const mq = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT - 1}px)`)
    const onChange = (e) => {
      setIsMobile(e.matches)
      if (!e.matches) setMobileOpen(false)
    }
    mq.addEventListener('change', onChange)
    return () => mq.removeEventListener('change', onChange)
  }, [])

  const sidebarOpen = isMobile ? mobileOpen : !desktopCollapsed

  const toggleSidebar = useCallback(() => {
    if (isMobile) {
      setMobileOpen((v) => !v)
    } else {
      setDesktopCollapsed((v) => {
        const next = !v
        localStorage.setItem('sidebar.collapsed', String(next))
        return next
      })
    }
  }, [isMobile])

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
        isMobile={isMobile}
        mobileOpen={mobileOpen}
        onNavigate={() => isMobile && setMobileOpen(false)}
      />

      {/* Mobile drawer backdrop */}
      {isMobile && mobileOpen && (
        <div
          className="fixed inset-0 bg-black/40 z-[90]"
          onClick={() => setMobileOpen(false)}
          aria-hidden="true"
        />
      )}

      <div className={`flex-1 flex flex-col ${sidebarOpen ? 'md:ml-60' : 'md:ml-0'}`}>
        <Header
          onNavigate={handleNavigate}
          onToggleSidebar={toggleSidebar}
          sidebarOpen={sidebarOpen}
          isMobile={isMobile}
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
      </div>

      {/* The /admin/personalize page renders its own full editor panel
          (THEME / LAYOUT / COMPONENTS). The global inspector would
          overlay it (z-100, fixed right) and block all interaction, so
          suppress it there. */}
      {!location.pathname.startsWith('/admin/personalize') && <PropertyInspector />}

      <CommandBar
        open={commandBarOpen}
        onClose={() => setCommandBarOpen(false)}
      />
    </div>
  )
}
