interface TopStatusBarProps {
  currentPath?: string;
  onNavigate?: (path: string) => void;
  homePath?: string;
  homeLabel?: string;
  moduleLabel?: string;
}

const ROUTE_LABELS: Record<string, string> = {
  '/dashboard': 'Dashboard',
  '/corporates': 'Corporates',
  '/companies': 'Companies',
  '/users': 'Users',
  '/settings/config': 'Configuration',
  '/inventory': 'Stock View',
  '/exceptions': 'Exceptions',
  '/activity': 'Activity',
  '/reports': 'Reports',
  '/config': 'Configuration',
  '/items': 'Item Master',
  '/bom': 'BOM Manager',
  '/categories': 'Categories',
  '/suppliers': 'Suppliers',
  '/uom': 'UOM',
  '/pricing': 'Pricing',
  '/validation': 'Data Validation',
  '/settings': 'Settings',
  // Collaboration & Productivity
  '/discuss': 'Discuss',
  '/chat': 'Chat',
  '/calendar': 'Calendar',
  '/todo': 'Todo',
  '/activities': 'Activities',
};

export function TopStatusBar({
  currentPath = '/dashboard',
  onNavigate,
  homePath = '/dashboard',
  homeLabel = 'Home',
  moduleLabel,
}: TopStatusBarProps) {
  const routeKey = currentPath.replace(/^\/[^/]+/, '');
  const currentLabel = ROUTE_LABELS[currentPath] || ROUTE_LABELS[routeKey] || moduleLabel || 'Dashboard';

  return (
    <nav className="flex items-center gap-2 mb-4 text-on-surface-variant text-[11px] font-semibold">
      <button onClick={() => onNavigate?.(homePath)}
              className="hover:text-primary transition-colors cursor-pointer">{homeLabel}</button>
      <span className="material-symbols-outlined text-sm">chevron_right</span>
      {moduleLabel && (
        <>
          <span className="text-primary font-bold">{moduleLabel}</span>
          <span className="material-symbols-outlined text-sm">chevron_right</span>
        </>
      )}
      <span className="text-primary font-bold">{currentLabel}</span>
    </nav>
  );
}
