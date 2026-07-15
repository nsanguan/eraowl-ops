import { Link, useLocation, Outlet, useNavigate } from 'react-router-dom'
import useAuthStore from '../store/authStore'
import Header from './components/Header'

/**
 * Standard Page Layout
 * 
 * Use this as the top-level layout for any module page.
 * - Sidebar with nav links + brand
 * - Topbar with theme toggle, notifications, user menu
 * - Main content area with breadcrumbs
 * 
 * To create a new module page:
 * 1. Copy this component
 * 2. Update menuItems with your module's pages
 * 3. Update moduleLabel / moduleInitials
 * 4. Wrap your page content in <Outlet />
 */

export default function Layout() {
  const location = useLocation()
  const navigate = useNavigate()
  const { user } = useAuthStore()
  const userInitials = user?.username ? user.username.substring(0, 2).toUpperCase() : 'EU'

  return (
    <div className="flex h-screen">
      {/* Sidebar */}
      <aside className="fixed left-0 top-0 h-full w-64 border-r border-outline-variant bg-surface-dim flex flex-col z-50">
        <div className="p-6 flex items-center gap-3">
          <div className="w-10 h-10 bg-[#4a8eff] rounded flex items-center justify-center text-[#00285b] font-black text-sm leading-none">EO</div>
          <div>
            <h1 className="text-xl font-semibold text-primary leading-tight">EraOwl-OPS</h1>
            <p className="text-[10px] uppercase tracking-widest text-outline">AI ERP Platform</p>
          </div>
        </div>

        <nav className="flex-1 mt-1 overflow-y-auto custom-scrollbar px-2">
          {/* Replace with your module's menu items */}
          <p className="px-3 py-2 text-xs text-outline">Module placeholder</p>
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

      {/* Main area: Header + Content */}
      <div className="flex-1 flex flex-col ml-64">
        <Header
          onNavigate={(path) => navigate(path)}
          userLabel={user?.username ?? 'Admin User'}
          userInitials={userInitials}
          moduleLabel="Module"
          moduleInitials="MD"
        />
        <main className="mt-16 p-8 min-h-[calc(100vh-4rem)] overflow-y-auto bg-surface-container-lowest">
          {/* Breadcrumb — replace with your page breadcrumb */}
          <nav className="flex items-center gap-2 mb-4 text-on-surface-variant text-[11px] font-semibold">
            <button onClick={() => navigate('/')} className="hover:text-primary transition-colors cursor-pointer">Home</button>
            <span className="material-symbols-outlined text-sm">chevron_right</span>
            <span className="text-primary font-bold">Page Title</span>
          </nav>
          <Outlet />
        </main>
      </div>
    </div>
  )
}
