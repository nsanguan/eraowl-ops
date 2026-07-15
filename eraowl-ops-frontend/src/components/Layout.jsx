import { useState, useEffect, useMemo, useCallback } from 'react'
import { Outlet, useLocation, useNavigate } from 'react-router-dom'
import useAuthStore from '../store/authStore'
import Header from './Header'
import SidebarNav from './SidebarNav'
import CommandBar from './CommandBar'
import { getModulesByArea } from '../config/moduleRegistry'

export default function Layout() {
  const location = useLocation()
  const navigate = useNavigate()
  const { user, privileges } = useAuthStore()
  const userInitials = user?.username
    ? user.username.substring(0, 2).toUpperCase()
    : 'EU'

  const [activeArea, setActiveArea] = useState(null)
  const [commandBarOpen, setCommandBarOpen] = useState(false)

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
      />

      <div className="flex-1 flex flex-col ml-60">
        <Header
          onNavigate={handleNavigate}
          userLabel={user?.username ?? 'User'}
          userInitials={userInitials}
          onOpenCommandBar={() => setCommandBarOpen(true)}
        />

        <main className="mt-14 p-6 min-h-[calc(100vh-3.5rem)] overflow-y-auto bg-surface-container-lowest">
          <Outlet />
        </main>
      </div>

      <CommandBar
        open={commandBarOpen}
        onClose={() => setCommandBarOpen(false)}
      />
    </div>
  )
}
