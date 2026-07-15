import type { ReactNode } from 'react';
import { Sidebar, type NavSection } from './Sidebar';
import { Header, type QuickSettingItem } from './Header';
import { TopStatusBar } from './TopStatusBar';
import type { Warehouse } from '../../stores/preferences';

interface AppShellProps {
  children: ReactNode;
  currentPath?: string;
  onNavigate?: (path: string) => void;
  onSearch?: (query: string) => void;
  searchPlaceholder?: string;
  quickSettings?: QuickSettingItem[];
  helpUrl?: string;
  homeUrl?: string;
  homePath?: string;
  homeLabel?: string;
  moduleLabel?: string;
  moduleInitials?: string;
  userLabel?: string;
  userInitials?: string;
  warehouses?: Warehouse[];
  navSections?: NavSection[];
}

export function AppShell({
  children,
  currentPath = '/dashboard',
  onNavigate,
  onSearch,
  searchPlaceholder,
  helpUrl,
  homeUrl,
  homePath = '/dashboard',
  homeLabel = 'Home',
  moduleLabel,
  moduleInitials,
  userLabel,
  userInitials,
  warehouses = [],
  navSections,
}: AppShellProps) {
  return (
    <div className="min-h-screen bg-background text-on-surface" style={{ fontFamily: 'var(--font-sans, Inter, sans-serif)' }}>
      <Sidebar currentPath={currentPath} onNavigate={onNavigate ?? (() => {})} sections={navSections} moduleTitle={moduleLabel} moduleInitials={moduleInitials} />
      <Header
        onSearch={onSearch}
        onNavigate={onNavigate}
        searchPlaceholder={searchPlaceholder}
        helpUrl={helpUrl}
        homeUrl={homeUrl}
        userLabel={userLabel}
        userInitials={userInitials}
        warehouses={warehouses}
        moduleLabel={moduleLabel}
        moduleInitials={moduleInitials}
      />
      <main className="ml-64 mt-16 p-8 min-h-[calc(100vh-4rem)] overflow-y-auto custom-scrollbar">
        <TopStatusBar
          currentPath={currentPath}
          onNavigate={onNavigate}
          homePath={homePath}
          homeLabel={homeLabel}
          moduleLabel={moduleLabel}
        />
        <div className="space-y-6">
          {children}
        </div>
      </main>
      <div className="fixed top-0 right-0 -z-10 w-[500px] h-[500px] bg-primary/5 blur-[120px] rounded-full pointer-events-none"></div>
      <div className="fixed bottom-0 left-64 -z-10 w-[400px] h-[400px] bg-secondary/5 blur-[100px] rounded-full pointer-events-none"></div>
    </div>
  );
}
