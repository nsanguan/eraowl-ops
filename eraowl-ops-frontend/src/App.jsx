import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { useEffect } from 'react'
import useAuthStore from './store/authStore'
import ProtectedRoute from './components/ProtectedRoute'
import Layout from './components/Layout'
import Login from './modules/admin/pages/Login'
import UserManagement from './modules/admin/pages/UserManagement'
import RoleManagement from './modules/admin/pages/RoleManagement'
import ObjectsPage from './modules/admin/pages/ObjectsPage'
import OrgStructurePage from './modules/mdm/org_structure/pages/OrgStructurePage'
import PartyPage from './modules/mdm/party/pages/PartyPage'
import ItemPage from './modules/mdm/item/pages/ItemPage'
import BomPage from './modules/bom/pages/BomPage'
import CollaborationDashboard from './modules/collaboration/pages/Dashboard'
import DiscussPage from './modules/collaboration/pages/DiscussPage'
import TodoPage from './modules/collaboration/pages/TodoPage'

export default function App() {
  const checkAuth = useAuthStore((s) => s.checkAuth)

  useEffect(() => {
    checkAuth()
  }, [checkAuth])

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          element={
            <ProtectedRoute>
              <Layout />
            </ProtectedRoute>
          }
        >
          <Route path="/" element={<div className="p-4"><h1 className="text-2xl font-bold text-on-surface">Welcome to EraOwl-OPS</h1><p className="text-sm text-outline mt-2">Use the sidebar to navigate between modules, or press <kbd className="px-1.5 py-0.5 text-xs font-mono bg-surface-container-high rounded border border-outline-variant">⌘K</kbd> for quick search.</p></div>} />
          <Route path="/admin/users" element={<UserManagement />} />
          <Route path="/admin/roles" element={<RoleManagement />} />
          <Route path="/admin/objects" element={<ObjectsPage />} />
          <Route path="/org-structure" element={<OrgStructurePage />} />
          <Route path="/party" element={<PartyPage />} />
          <Route path="/items" element={<ItemPage />} />
          <Route path="/bom" element={<BomPage />} />
          <Route path="/collaboration" element={<CollaborationDashboard />} />
          <Route path="/collaboration/discuss" element={<DiscussPage />} />
          <Route path="/collaboration/todo" element={<TodoPage />} />
          <Route path="/po" element={<div className="p-4"><h1 className="text-2xl font-bold text-on-surface">Purchase Orders</h1><p className="text-sm text-outline mt-2">Purchase order management coming soon.</p></div>} />
          <Route path="/gl" element={<div className="p-4"><h1 className="text-2xl font-bold text-on-surface">General Ledger</h1><p className="text-sm text-outline mt-2">General ledger module coming soon.</p></div>} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
