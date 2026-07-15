import { useState, useRef, useEffect } from 'react'
import useAuthStore from '../store/authStore'

export default function Header({
  onNavigate,
  helpUrl,
  homeUrl,
  userLabel = 'Admin User',
  userInitials = 'AU',
  moduleLabel,
  moduleInitials,
}) {
  const [helpOpen, setHelpOpen] = useState(false)
  const [theme, setTheme] = useState(() => document.documentElement.classList.contains('dark') ? 'dark' : 'light')
  const helpRef = useRef(null)
  const { logout } = useAuthStore()

  useEffect(() => {
    function handleClickOutside(e) {
      if (helpRef.current && !helpRef.current.contains(e.target)) {
        setHelpOpen(false)
      }
    }
    if (helpOpen) document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [helpOpen])

  const handleToggleTheme = () => {
    const next = theme === 'dark' ? 'light' : 'dark'
    document.documentElement.classList.toggle('dark', next === 'dark')
    localStorage.setItem('theme', next)
    setTheme(next)
  }

  const handleLogout = async () => {
    await logout()
    window.location.reload()
  }

  return (
    <header className="fixed top-0 right-0 left-64 h-16 bg-surface-container border-b border-outline-variant flex items-center justify-between px-6 z-40">
      <div className="flex items-center flex-1 max-w-xl">
        {moduleInitials && (
          <div className="flex items-center gap-2 mr-4 pr-4 border-r border-outline-variant">
            <div className="w-8 h-8 rounded-lg bg-primary/10 flex items-center justify-center text-primary font-bold text-xs">
              {moduleInitials}
            </div>
            {moduleLabel && (
              <span className="text-[12px] font-semibold text-on-surface hidden sm:block">{moduleLabel}</span>
            )}
          </div>
        )}
      </div>

      <div className="flex items-center gap-6">
        <div className="flex items-center gap-4 border-r border-outline-variant pr-6">
          <button
            className="text-on-surface-variant hover:text-primary transition-colors"
            onClick={() => homeUrl ? (window.location.href = homeUrl) : onNavigate?.('/')}
            title="Home"
          >
            <span className="material-symbols-outlined text-[20px]">home</span>
          </button>
          <div className="relative">
            <button className="text-on-surface-variant hover:text-primary transition-colors" title="Notifications">
              <span className="material-symbols-outlined text-[20px]">notifications</span>
            </button>
            <span className="absolute top-1 right-1 w-2 h-2 bg-error rounded-full border-2 border-surface-container" />
          </div>
          <button
            className="text-on-surface-variant hover:text-primary transition-colors"
            onClick={handleToggleTheme}
            title={theme === 'dark' ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
          >
            <span className="material-symbols-outlined text-[20px]">{theme === 'dark' ? 'light_mode' : 'dark_mode'}</span>
          </button>
          <div className="relative" ref={helpRef}>
            <button
              className="text-on-surface-variant hover:text-primary transition-colors"
              onClick={() => setHelpOpen((prev) => !prev)}
              title="Help"
            >
              <span className="material-symbols-outlined text-[20px]">help</span>
            </button>
            {helpOpen && (
              <div className="absolute right-0 top-full mt-2 w-64 rounded-xl overflow-hidden border border-outline-variant shadow-xl z-50 bg-surface-container">
                <div className="px-4 py-2 border-b border-outline-variant/50">
                  <p className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">Help & Support</p>
                </div>
                <button
                  onClick={() => { if (helpUrl) { window.location.href = helpUrl; setHelpOpen(false) } }}
                  className="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-high transition-colors text-left"
                >
                  <span className="material-symbols-outlined text-outline text-[18px]">menu_book</span>
                  <div>
                    <div className="font-semibold">Documentation</div>
                    <div className="text-[10px] text-outline">Read the user guide</div>
                  </div>
                </button>
                <button
                  onClick={() => { setHelpOpen(false); onNavigate?.('/about') }}
                  className="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-high transition-colors text-left border-t border-outline-variant/30"
                >
                  <span className="material-symbols-outlined text-outline text-[18px]">info</span>
                  <div>
                    <div className="font-semibold">About EraOwl-OPS</div>
                    <div className="text-[10px] text-outline">Version & system info</div>
                  </div>
                </button>
              </div>
            )}
          </div>
        </div>

        <div className="flex items-center gap-3">
          <div className="text-right hidden sm:block">
            <p className="text-[11px] font-semibold text-on-surface">{userLabel}</p>
            <p className="text-[9px] text-outline text-right">ERA OPS</p>
          </div>
          <div className="w-9 h-9 rounded-lg bg-surface-container-highest border border-outline-variant flex items-center justify-center text-primary font-bold text-xs">
            {userInitials}
          </div>
          <button
            className="material-symbols-outlined text-outline hover:text-error transition-colors ml-2 text-[22px]"
            title="Sign Out"
            onClick={handleLogout}
          >
            logout
          </button>
        </div>
      </div>
    </header>
  )
}
