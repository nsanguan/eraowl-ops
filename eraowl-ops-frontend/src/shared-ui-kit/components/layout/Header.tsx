import { useState, useRef, useEffect, type FormEvent } from 'react';
import { getTheme, toggleTheme, type Theme } from '../../lib/theme';
import { PreferencesModal } from '../ui/PreferencesModal';
import { useAuthStore } from '../../stores/auth';
import type { Warehouse } from '../../stores/preferences';

export interface QuickSettingItem {
  label: string;
  description: string;
  path: string;
  icon: string;
}

interface HeaderProps {
  searchPlaceholder?: string;
  onSearch?: (query: string) => void;
  onNavigate?: (path: string) => void;
  quickSettings?: QuickSettingItem[];
  helpUrl?: string;
  homeUrl?: string;
  userLabel?: string;
  userInitials?: string;
  warehouses?: Warehouse[];
  moduleLabel?: string;
  moduleInitials?: string;
  /** Unread count for Chat (DM) badge */
  chatUnread?: number;
  /** Unread count for Discuss (channel) badge */
  discussUnread?: number;
  /** Unread count for Todo badge */
  collabTodoUnread?: number;
  /** Unread count for Activities badge */
  collabActivitiesUnread?: number;
}

export function Header({
  searchPlaceholder = 'Search records...',
  onSearch,
  onNavigate,
  helpUrl,
  homeUrl,
  userLabel = 'Admin User',
  userInitials = 'AU',
  warehouses = [],
  moduleLabel,
  moduleInitials,
  chatUnread = 0,
  discussUnread = 0,
  collabTodoUnread = 0,
  collabActivitiesUnread = 0,
}: HeaderProps) {
  const [helpOpen, setHelpOpen] = useState(false);
  const [searchVal, setSearchVal] = useState('');
  const [theme, setThemeState] = useState<Theme>('dark');
  const [prefsOpen, setPrefsOpen] = useState(false);
  const helpRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    setThemeState(getTheme());
  }, []);

  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (helpRef.current && !helpRef.current.contains(e.target as Node)) {
        setHelpOpen(false);
      }
    }
    if (helpOpen) {
      document.addEventListener('mousedown', handleClickOutside);
    }
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, [helpOpen]);

  const handleSearch = (e: FormEvent) => {
    e.preventDefault();
    if (searchVal.trim()) {
      onSearch?.(searchVal.trim());
    }
  };

  const handleToggleTheme = () => {
    const next = toggleTheme();
    setThemeState(next);
  };

  return (
    <>
      <header className="fixed top-0 right-0 left-64 h-16 bg-surface-container border-b border-outline-variant flex items-center justify-between px-6 z-40">
        <div className="flex items-center flex-1 max-w-xl">
          {moduleInitials && (
            <div className="flex items-center gap-2 mr-4 pr-4 border-r border-outline-variant">
              <div className="w-8 h-8 rounded-lg bg-primary/10 flex items-center justify-center text-primary font-bold text-xs">
                {moduleInitials}
              </div>
              {moduleLabel && <span className="text-[12px] font-semibold text-on-surface hidden sm:block">{moduleLabel}</span>}
            </div>
          )}

        </div>
        <div className="flex items-center gap-6">
          <div className="flex items-center gap-4 border-r border-outline-variant pr-6">
            <button className="text-on-surface-variant hover:text-primary transition-colors"
                    onClick={() => homeUrl ? (window.location.href = homeUrl) : onNavigate?.('/dashboard')}
                    title="Portal Home">
              <span className="material-symbols-outlined !text-[20px]">home</span>
            </button>
            <div className="relative">
              <button className="text-on-surface-variant hover:text-primary transition-colors" title="Notifications">
                <span className="material-symbols-outlined !text-[20px]">notifications</span>
              </button>
              <span className="absolute top-1 right-1 w-2 h-2 bg-error rounded-full border-2 border-surface-container"></span>
            </div>
            <a href={`http://${typeof window !== 'undefined' ? window.location.hostname : 'localhost'}:3000`}
               target="_blank" rel="noopener noreferrer"
               className="text-on-surface-variant hover:text-primary transition-colors" title="AI Chat (Open WebUI)">
              <span className="material-symbols-outlined !text-[20px]">auto_awesome</span>
            </a>
            {(() => {
              const base = `http://${typeof window !== 'undefined' ? window.location.hostname : 'localhost'}:3221/collaboration`;
              return (
                <>
                  <div className="relative">
                    <button className="text-on-surface-variant hover:text-primary transition-colors"
                            onClick={() => window.location.href = `${base}/discuss`} title="Discuss">
                      <span className="material-symbols-outlined !text-[20px]">forum</span>
                    </button>
                    {discussUnread > 0 && (
                      <span className="absolute -top-0.5 -right-0.5 flex h-4 min-w-[14px] items-center justify-center rounded-full bg-error px-1 text-[8px] font-bold text-white">
                        {discussUnread > 99 ? '99+' : discussUnread}
                      </span>
                    )}
                  </div>
                  <div className="relative">
                    <button className="text-on-surface-variant hover:text-primary transition-colors"
                            onClick={() => window.location.href = `${base}/chat`} title="Chat">
                      <span className="material-symbols-outlined !text-[20px]">chat</span>
                    </button>
                    {chatUnread > 0 && (
                      <span className="absolute -top-0.5 -right-0.5 flex h-4 min-w-[14px] items-center justify-center rounded-full bg-error px-1 text-[8px] font-bold text-white">
                        {chatUnread > 99 ? '99+' : chatUnread}
                      </span>
                    )}
                  </div>
                  <button className="text-on-surface-variant hover:text-primary transition-colors"
                          onClick={() => window.location.href = `${base}/calendar`} title="Calendar">
                    <span className="material-symbols-outlined !text-[20px]">calendar_month</span>
                  </button>
                  <div className="relative">
                    <button className="text-on-surface-variant hover:text-primary transition-colors"
                            onClick={() => window.location.href = `${base}/todo`} title="Todo">
                      <span className="material-symbols-outlined !text-[20px]">checklist</span>
                    </button>
                    {collabTodoUnread > 0 && (
                      <span className="absolute -top-0.5 -right-0.5 flex h-4 min-w-[14px] items-center justify-center rounded-full bg-error px-1 text-[8px] font-bold text-white">
                        {collabTodoUnread > 99 ? '99+' : collabTodoUnread}
                      </span>
                    )}
                  </div>
                  <div className="relative">
                    <button className="text-on-surface-variant hover:text-primary transition-colors"
                            onClick={() => window.location.href = `${base}/activities`} title="Activities">
                      <span className="material-symbols-outlined !text-[20px]">timeline</span>
                    </button>
                    {collabActivitiesUnread > 0 && (
                      <span className="absolute -top-0.5 -right-0.5 flex h-4 min-w-[14px] items-center justify-center rounded-full bg-error px-1 text-[8px] font-bold text-white">
                        {collabActivitiesUnread > 99 ? '99+' : collabActivitiesUnread}
                      </span>
                    )}
                  </div>
                </>
              );
            })()}
            <button className="text-on-surface-variant hover:text-primary transition-colors"
                    onClick={handleToggleTheme}
                    title={theme === 'dark' ? 'Switch to Light Mode' : 'Switch to Dark Mode'}>
              <span className="material-symbols-outlined !text-[20px]">{theme === 'dark' ? 'light_mode' : 'dark_mode'}</span>
            </button>
            <div className="relative" ref={helpRef}>
              <button className="text-on-surface-variant hover:text-primary transition-colors"
                      onClick={() => setHelpOpen((prev) => !prev)} title="Help">
                <span className="material-symbols-outlined !text-[20px]">help</span>
              </button>
              {helpOpen && (
                <div className="absolute right-0 top-full mt-2 w-64 rounded-xl overflow-hidden border border-outline-variant shadow-xl z-50 bg-surface-container">
                  <div className="px-4 py-2 border-b border-outline-variant/50">
                    <p className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">Help & Support</p>
                  </div>
                  <button onClick={() => { if (helpUrl) { window.location.href = helpUrl; setHelpOpen(false); } }}
                          className="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-high transition-colors text-left">
                    <span className="material-symbols-outlined text-outline !text-[18px]">menu_book</span>
                    <div>
                      <div className="font-semibold">Documentation</div>
                      <div className="text-[10px] text-outline">Read the user guide</div>
                    </div>
                  </button>
                  <button onClick={() => { setHelpOpen(false); onNavigate?.('/support'); }}
                          className="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-high transition-colors text-left border-t border-outline-variant/30">
                    <span className="material-symbols-outlined text-outline !text-[18px]">forum</span>
                    <div>
                      <div className="font-semibold">Contact Support</div>
                      <div className="text-[10px] text-outline">Get help from our team</div>
                    </div>
                  </button>
                  <button onClick={() => { setHelpOpen(false); onNavigate?.('/about'); }}
                          className="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-high transition-colors text-left border-t border-outline-variant/30">
                    <span className="material-symbols-outlined text-outline !text-[18px]">info</span>
                    <div>
                      <div className="font-semibold">About Axon OS</div>
                      <div className="text-[10px] text-outline">Version & system info</div>
                    </div>
                  </button>
                </div>
              )}
            </div>
            <button className="text-on-surface-variant hover:text-primary transition-colors"
                    onClick={() => setPrefsOpen(true)} title="Preferences Setup">
              <span className="material-symbols-outlined !text-[20px]">settings</span>
            </button>
          </div>
          <div className="flex items-center gap-3">
            <div className="text-right hidden sm:block">
              <p className="text-[11px] font-semibold text-on-surface">{userLabel}</p>
              <p className="text-[9px] text-outline text-right">AXON OS</p>
            </div>
            <div className="w-9 h-9 rounded-lg bg-surface-container-highest border border-outline-variant flex items-center justify-center text-primary font-bold text-xs">
              {userInitials}
            </div>
            <button className="material-symbols-outlined text-outline hover:text-error transition-colors ml-2 !text-[22px]"
                    title="Sign Out"
                    onClick={() => { useAuthStore.getState().clearAuth(); window.location.reload(); }}>logout</button>
          </div>
        </div>
      </header>
      <PreferencesModal open={prefsOpen} onClose={() => setPrefsOpen(false)} warehouses={warehouses} />
    </>
  );
}
