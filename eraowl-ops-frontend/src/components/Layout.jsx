import { Link, useLocation, Outlet, useNavigate } from 'react-router-dom'
import useAuthStore from '../store/authStore'
import Header from './Header'
import { Users, Shield, Package, Building2, Boxes, LayoutDashboard } from 'lucide-react'

const menuItems = [
  { path: '/',            label: 'Dashboard',       icon: LayoutDashboard, module: 'admin', action: 'view' },
  { path: '/admin/users', label: 'Users',            icon: Users,            module: 'admin', action: 'manage_users' },
  { path: '/admin/roles', label: 'Roles',            icon: Shield,           module: 'admin', action: 'manage_roles' },
  { path: '/org-structure', label: 'Org Structure',  icon: Building2,        module: 'org_structure', action: 'view' },
  { path: '/items',       label: 'Items',            icon: Package,          module: 'item', action: 'view' },
  { path: '/bom',         label: 'BOM',              icon: Boxes,            module: 'bom', action: 'view' },
]

export default function Layout() {
  const location = useLocation()
  const navigate = useNavigate()
  const { user } = useAuthStore()
  const userInitials = user?.username ? user.username.substring(0, 2).toUpperCase() : 'EU'

  return (
    <div className="flex h-screen">
      <aside className="fixed left-0 top-0 h-full w-64 border-r border-outline-variant bg-surface-dim flex flex-col z-50">
        <div className="p-6 flex items-center gap-3">
          <div className="w-10 h-10 bg-[#4a8eff] rounded flex items-center justify-center text-[#00285b] font-black text-sm leading-none">EO</div>
          <div>
            <h1 className="text-xl font-semibold text-primary leading-tight">EraOwl-OPS</h1>
            <p className="text-[10px] uppercase tracking-widest text-outline">AI ERP Platform</p>
          </div>
        </div>

        <nav className="flex-1 mt-1 overflow-y-auto custom-scrollbar px-2">
          {menuItems.map((item) => {
            const isActive = location.pathname === '/' ? location.pathname === item.path : location.pathname.startsWith(item.path) && item.path !== '/'
            return (
              <Link
                key={item.path}
                to={item.path}
                className={`flex items-center gap-3 px-3 py-2 rounded-lg text-sm mb-0.5 transition-colors ${
                  isActive
                    ? 'border-l-4 border-primary bg-surface-container-high text-primary font-semibold'
                    : 'text-on-surface-variant hover:bg-surface-container-low border-l-4 border-transparent'
                }`}
              >
                <item.icon size={18} />
                {item.label}
              </Link>
            )
          })}
        </nav>

        <div className="mt-auto p-4 border-t border-outline-variant bg-surface-container-low">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-full bg-[#00e3fd] text-[#00363d] flex items-center justify-center font-bold text-[10px]">
              {userInitials}
            </div>
            <div>
              <p className="text-[11px] font-semibold text-on-surface">{user?.username ?? 'User'}</p>
              <p className="text-[9px] text-outline">ERA OPS</p>
            </div>
          </div>
        </div>
      </aside>

      <div className="flex-1 flex flex-col ml-64">
        <Header
          onNavigate={(path) => navigate(path)}
          userLabel={user?.username ?? 'Admin User'}
          userInitials={userInitials}
          moduleLabel="Admin"
          moduleInitials="AD"
        />
        <main className="mt-16 p-8 min-h-[calc(100vh-4rem)] overflow-y-auto bg-surface-container-lowest">
          <nav className="flex items-center gap-2 mb-4 text-on-surface-variant text-[11px] font-semibold">
            <button onClick={() => navigate('/')} className="hover:text-primary transition-colors cursor-pointer">Home</button>
            <span className="material-symbols-outlined text-sm">chevron_right</span>
            <span className="text-primary font-bold">{location.pathname === '/' ? 'Dashboard' : location.pathname.split('/').pop()?.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase())}</span>
          </nav>
          <Outlet />
        </main>
      </div>
    </div>
  )
}
