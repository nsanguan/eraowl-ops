import { useQuery } from '@tanstack/react-query';
import { MenuTree, type MenuTreeNode } from './MenuTree';
import { mcpCall } from '../../lib/gateway';
import { useAuthStore } from '../../stores/auth';

export interface NavItem {
  href: string;
  icon: string;
  label: string;
  permission?: string;
}

export interface NavSection {
  title: string;
  items: NavItem[];
}

interface SidebarProps {
  currentPath: string;
  onNavigate: (href: string) => void;
  sections?: NavSection[]; // Deprecated but kept for backward compatibility if needed
  moduleTitle?: string;
  moduleInitials?: string;
}

const iconMap: Record<string, string> = {
  'layout-dashboard': 'dashboard',
  'building-2': 'business',
  building: 'business',
  users: 'group',
  settings: 'settings',
  'package': 'inventory_2',
  truck: 'local_shipping',
  'clipboard-list': 'assignment',
  'bar-chart-3': 'bar_chart',
  'file-text': 'description',
  'shopping-cart': 'shopping_cart',
  'credit-card': 'credit_card',
  'database': 'database',
  'shield': 'shield',
  'user-check': 'person_check',
  'globe': 'language',
  'activity': 'trending_up',
  'alert-circle': 'error',
  'check-circle': 'check_circle',
  'circle-dollar-sign': 'attach_money',
  ruler: 'straighten',
  handshake: 'handshake',
  layers: 'layers',
  'folder-tree': 'account_tree',
  'package-plus': 'add_box',
  'file-stack': 'note_stack',
  puzzle: 'extension',
  warehouse: 'warehouse',
  'map-pin': 'location_on',
  map: 'map',
  'map-pinned': 'push_pin',
  history: 'history',
  'arrow-right-left': 'swap_horiz',
  'list-tree': 'account_tree',
  'dollar-sign': 'attach_money',
  'messages-square': 'forum',
  'message-circle': 'chat',
  'calendar': 'calendar_month',
  'check-square': 'check_box',
  landmark: 'account_balance',
  'book-open': 'book',
  'arrow-down': 'arrow_downward',
  'arrow-up': 'arrow_upward',
  user: 'person',
  route: 'alt_route',
  'trending-up': 'trending_up',
  'refresh-cw': 'refresh',
  'rotate-cw': 'rotate_right',
  'clipboard-check': 'task_alt',
  'file-search': 'find_in_page',
  receipt: 'receipt',
  percent: 'percent',
  factory: 'factory',
  folder: 'folder',
  list: 'list',
  tag: 'label',
  upload: 'file_upload',
  'git-branch': 'account_tree',
  'more-vertical': 'more_vert',
  'external-link': 'open_in_new',
  inventory: 'inventory_2',
  lock: 'lock',
  refresh: 'refresh',
  swap: 'swap_horiz',
  clock: 'schedule',
  inbox: 'inbox',
  search: 'search',
  edit: 'edit',
  'bar-chart': 'bar_chart',
  tool: 'handyman',
  'alert-triangle': 'warning',
  'arrow-right': 'arrow_forward',
  bell: 'notifications',
  book: 'book',
  bot: 'smart_toy',
  box: 'inventory_2',
  brain: 'psychology',
  'calendar-days': 'calendar_month',
  'chart-line': 'show_chart',
  circle: 'circle',
  cpu: 'memory',
  crosshair: 'gps_fixed',
  file: 'description',
  flask: 'science',
  gauge: 'speed',
  'git-compare': 'compare_arrows',
  'git-merge': 'merge',
  grid: 'grid_view',
  'heart-pulse': 'monitor_heart',
  leaf: 'eco',
  lightbulb: 'lightbulb',
  link: 'link',
  'message-square': 'chat',
  'pie-chart': 'pie_chart',
  'piggy-bank': 'savings',
  'play-circle': 'play_circle',
  rocket: 'rocket_launch',
  rows: 'table_rows',
  'shield-alert': 'shield',
  sliders: 'tune',
  square: 'square',
  table: 'table',
  tags: 'label',
  target: 'track_changes',
  'wave-sine': 'graphic_eq',
  waves: 'water',
  atom: 'science',
  bug: 'bug_report',
  'calendar-range': 'date_range',
  'file-bar-chart': 'bar_chart',
  'file-signature': 'edit_note',
  filter: 'filter_alt',
  'folder-code': 'code',
  'line-chart': 'show_chart',
  'list-checks': 'checklist',
  network: 'hub',
  paperclip: 'attachment',
  'pause-circle': 'pause_circle',
  'settings-2': 'settings',
  'shield-check': 'verified',
  sigma: 'functions',
  camera: 'camera',
  monitor: 'monitor',
  zap: 'bolt',
};

function mapIcon(icon: string): string {
  return iconMap[icon] ?? icon;
}

export function Sidebar({ currentPath, onNavigate, sections, moduleTitle, moduleInitials }: SidebarProps) {
  // Determine actual module initials from title if not passed
  const derivedModuleInitials = moduleInitials ?? (moduleTitle ? moduleTitle.substring(0, 2).toUpperCase() : 'MD');
  
  const token = useAuthStore((state) => state.token);

  const { data: menuTree, isLoading, error } = useQuery<MenuTreeNode[]>({
    queryKey: ['menuTree', moduleTitle],
    queryFn: async () => {
      const decoded = token ? JSON.parse(atob(token.split('.')[1].replace(/-/g, '+').replace(/_/g, '/'))) : null;
      const userId = decoded?.sub ?? '';
      return mcpCall<MenuTreeNode[]>('menus.tree', { user_id: userId, module: moduleTitle });
    },
    enabled: !!token,
  });

  return (
    <aside className="fixed left-0 top-0 h-full w-64 border-r border-outline-variant bg-surface-dim flex flex-col z-50" style={{ fontFamily: 'var(--font-sans, Inter, sans-serif)' }}>
      <div className="p-6 flex items-center gap-3">
        <div className="w-10 h-10 bg-[#4a8eff] rounded flex items-center justify-center text-[#00285b] font-black text-sm leading-none">AX</div>
        <div>
          <h1 className="text-xl font-semibold text-primary leading-tight">Axon OS</h1>
          <p className="text-[10px] uppercase tracking-widest text-outline">Enterprise Control</p>
        </div>
      </div>
      <nav className="flex-1 mt-1 overflow-y-auto custom-scrollbar px-2">
        {isLoading ? (
          <div className="p-4 text-sm text-outline animate-pulse flex flex-col gap-3">
             <div className="h-4 bg-outline-variant rounded w-3/4"></div>
             <div className="h-4 bg-outline-variant rounded w-1/2"></div>
             <div className="h-4 bg-outline-variant rounded w-5/6"></div>
          </div>
        ) : error ? (
          <div className="p-4 text-xs text-error">Failed to load navigation</div>
        ) : menuTree && menuTree.length > 0 ? (
          <MenuTree nodes={menuTree} currentPath={currentPath} onNavigate={onNavigate} mapIcon={mapIcon} />
        ) : (
          <div className="p-4 text-xs text-outline">No menus available</div>
        )}
      </nav>
      <div className="mt-auto p-4 border-t border-outline-variant bg-surface-container-low">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-full bg-[#00e3fd] text-[#00363d] flex items-center justify-center font-bold text-[10px]">
            {derivedModuleInitials}
          </div>
          <div>
            <p className="text-[11px] font-semibold text-on-surface">{moduleTitle ?? 'Module'} User</p>
            <p className="text-[9px] text-outline">AXON OS</p>
          </div>
        </div>
      </div>
    </aside>
  );
}
