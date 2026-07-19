import { useState, useRef, useEffect } from 'react'
import useAuthStore from '../store/authStore'

export default function Header({
  onNavigate,
  helpUrl,
  userLabel = 'User',
  userInitials = 'U',
  onOpenCommandBar,
  isDesignMode = false,
  onToggleDesignMode,
  canPersonalize = false,
  onToggleSidebar,
  sidebarOpen = true,
  isMobile = false,
}) {
  const [helpOpen, setHelpOpen] = useState(false)
  const [theme, setTheme] = useState(() =>
    document.documentElement.classList.contains('dark') ? 'dark' : 'light'
  )
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
    <header className="fixed top-0 left-0 right-0 h-12 bg-surface-container border-b border-outline-variant flex items-center justify-between px-4 z-30">
      <div className="flex items-center gap-3 min-w-0">
        {/* Brand: circular logo + product name, far left of the top bar */}
        <button
          onClick={() => onNavigate?.('/')}
          className="flex items-center gap-2 shrink-0 hover:opacity-80 transition-opacity"
          title="EraOwl-OPS Home"
        >
          <span className="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-on-primary font-bold text-xs shadow-sm">EO</span>
          <span className="leading-tight hidden sm:block">
            <span className="block text-[13px] font-bold text-on-surface">EraOwl-OPS</span>
            <span className="block text-[9px] text-outline">AI ERP</span>
          </span>
        </button>

        <button
          onClick={onToggleSidebar}
          className="flex items-center justify-center w-8 h-8 rounded-lg text-on-surface-variant hover:text-primary hover:bg-surface-container-high transition-colors"
          title={sidebarOpen ? 'Collapse menu' : 'Open menu'}
          aria-label={sidebarOpen ? 'Collapse navigation menu' : 'Open navigation menu'}
        >
          <span className="material-symbols-outlined text-[20px]">
            {sidebarOpen ? 'menu_open' : 'menu'}
          </span>
        </button>
        <button
          onClick={onOpenCommandBar}
          className="flex items-center gap-2 px-3 py-1.5 rounded-xl border border-outline-variant bg-surface-container-low hover:bg-surface-container-high transition-colors text-left flex-1 min-w-0 max-w-md"
          title="Search (⌘K)"
        >
          <span className="material-symbols-outlined text-outline text-[18px]">
            search
          </span>
          <span className="text-xs text-outline flex-1">
            Search modules...
          </span>
          <kbd className="hidden sm:inline-flex items-center gap-0.5 px-1.5 py-0.5 text-[10px] font-mono font-medium text-outline bg-surface-container-high rounded border border-outline-variant">
            <span className="text-[11px]">⌘</span>K
          </kbd>
        </button>
      </div>

      <div className="flex items-center gap-4">
        <div className="flex items-center gap-3">
          <button
            className="text-on-surface-variant hover:text-primary transition-colors"
            onClick={() => onNavigate?.('/')}
            title="Home"
          >
            <span className="material-symbols-outlined text-[20px]">home</span>
          </button>

          <div className="w-px h-5 bg-outline-variant/50 mx-1" />

          <button className="text-on-surface-variant hover:text-primary transition-colors" onClick={() => onNavigate?.('/collaboration/discuss')} title="Discuss">
            <span className="material-symbols-outlined text-[20px]">forum</span>
          </button>
          <button className="text-on-surface-variant hover:text-primary transition-colors" onClick={() => onNavigate?.('/collaboration/chat')} title="Chat">
            <span className="material-symbols-outlined text-[20px]">chat</span>
          </button>
          <button className="text-on-surface-variant hover:text-primary transition-colors" onClick={() => onNavigate?.('/collaboration/calendar')} title="Calendar">
            <span className="material-symbols-outlined text-[20px]">calendar_month</span>
          </button>
          <button className="text-on-surface-variant hover:text-primary transition-colors" onClick={() => onNavigate?.('/collaboration/todo')} title="Tasks">
            <span className="material-symbols-outlined text-[20px]">checklist</span>
          </button>
          <button className="text-on-surface-variant hover:text-primary transition-colors" onClick={() => onNavigate?.('/collaboration/activities')} title="Activities">
            <span className="material-symbols-outlined text-[20px]">event_note</span>
          </button>

          <div className="w-px h-5 bg-outline-variant/50 mx-1" />

          <div className="relative">
            <button
              className="text-on-surface-variant hover:text-primary transition-colors"
              title="Notifications"
            >
              <span className="material-symbols-outlined text-[20px]">
                notifications
              </span>
            </button>
            <span className="absolute top-1 right-1 w-2 h-2 bg-error rounded-full border-2 border-surface-container" />
          </div>

          <button
            className="text-on-surface-variant hover:text-primary transition-colors"
            onClick={handleToggleTheme}
            title={
              theme === 'dark'
                ? 'Switch to Light Mode'
                : 'Switch to Dark Mode'
            }
          >
            <span className="material-symbols-outlined text-[20px]">
              {theme === 'dark' ? 'light_mode' : 'dark_mode'}
            </span>
          </button>

          {canPersonalize && (
            <button
              onClick={onToggleDesignMode}
              title={isDesignMode ? 'Exit Personalize Mode' : 'Enter Personalize Mode'}
              className={`flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg border text-[12px] font-semibold transition-colors ${
                isDesignMode
                  ? 'bg-primary text-on-primary border-primary'
                  : 'text-on-surface-variant border-outline-variant hover:text-primary hover:border-primary'
              }`}
            >
              <span className="material-symbols-outlined text-[18px]">
                {isDesignMode ? 'tune' : 'tune'}
              </span>
              <span className="hidden md:inline">
                {isDesignMode ? 'Exit Personalize' : 'Personalize'}
              </span>
              <span
                className={`w-2 h-2 rounded-full ml-0.5 ${
                  isDesignMode ? 'bg-on-primary' : 'bg-outline-variant'
                }`}
              />
            </button>
          )}

          <div className="relative" ref={helpRef}>
            <button
              className="text-on-surface-variant hover:text-primary transition-colors"
              onClick={() => setHelpOpen((prev) => !prev)}
              title="Help"
            >
              <span className="material-symbols-outlined text-[20px]">
                help
              </span>
            </button>
            {helpOpen && (
              <div className="absolute right-0 top-full mt-2 w-56 rounded-xl overflow-hidden border border-outline-variant shadow-xl z-50 bg-surface-container">
                <div className="px-4 py-2 border-b border-outline-variant/50">
                  <p className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">
                    Help & Support
                  </p>
                </div>
                <button
                  onClick={() => {
                    if (helpUrl) {
                      window.location.href = helpUrl
                      setHelpOpen(false)
                    }
                  }}
                  className="w-full flex items-center gap-3 px-4 py-2.5 text-sm text-on-surface hover:bg-surface-container-high transition-colors text-left"
                >
                  <span className="material-symbols-outlined text-outline text-[18px]">
                    menu_book
                  </span>
                  <div>
                    <div className="font-semibold text-xs">Documentation</div>
                    <div className="text-[10px] text-outline">
                      Read the user guide
                    </div>
                  </div>
                </button>
                <button
                  onClick={() => {
                    setHelpOpen(false)
                    onNavigate?.('/about')
                  }}
                  className="w-full flex items-center gap-3 px-4 py-2.5 text-sm text-on-surface hover:bg-surface-container-high transition-colors text-left border-t border-outline-variant/30"
                >
                  <span className="material-symbols-outlined text-outline text-[18px]">
                    info
                  </span>
                  <div>
                    <div className="font-semibold text-xs">About EraOwl-OPS</div>
                    <div className="text-[10px] text-outline">
                      Version & system info
                    </div>
                  </div>
                </button>
              </div>
            )}
          </div>
        </div>

        <div className="flex items-center gap-2.5 pl-4 border-l border-outline-variant">
          <div className="text-right hidden sm:block">
            <p className="text-[11px] font-semibold text-on-surface">
              {userLabel}
            </p>
            <p className="text-[9px] text-outline text-right">ERA OPS</p>
          </div>
          <div className="w-8 h-8 rounded-lg bg-primary/10 border border-primary/20 flex items-center justify-center text-primary font-bold text-xs">
            {userInitials}
          </div>
          <button
            className="material-symbols-outlined text-outline hover:text-error transition-colors text-[20px]"
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
