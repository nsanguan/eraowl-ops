import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { useEffect } from 'react'
import useAuthStore from './store/authStore'
import ProtectedRoute from './components/ProtectedRoute'
import Layout from './components/Layout'
import Login from './modules/admin/pages/Login'
import UserManagement from './modules/admin/pages/UserManagement'
import RoleManagement from './modules/admin/pages/RoleManagement'
import OrgStructurePage from './modules/mdm/org_structure/pages/OrgStructurePage'
import PartyPage from './modules/mdm/party/pages/PartyPage'
import ItemPage from './modules/mdm/item/pages/ItemPage'
import BomPage from './modules/bom/pages/BomPage'

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
          <Route path="/" element={<div className="p-4">Welcome to EraOwl-OPS</div>} />
          <Route path="/admin/users" element={<UserManagement />} />
          <Route path="/admin/roles" element={<RoleManagement />} />
          <Route path="/org-structure" element={<OrgStructurePage />} />
          <Route path="/party" element={<PartyPage />} />
          <Route path="/items" element={<ItemPage />} />
          <Route path="/bom" element={<BomPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
