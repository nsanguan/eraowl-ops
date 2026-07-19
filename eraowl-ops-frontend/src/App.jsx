import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { useEffect } from 'react'
import useAuthStore from './store/authStore'
import usePersonalizeStore from './store/usePersonalizeStore'
import { applyThemeToRoot } from './shared-ui-kit/components/ui/ThemeRoller'
import ProtectedRoute from './components/ProtectedRoute'
import Layout from './components/Layout'
import Login from './modules/admin/pages/Login'
import UserManagement from './modules/admin/pages/UserManagement'
import RoleManagement from './modules/admin/pages/RoleManagement'
import ObjectsPage from './modules/admin/pages/ObjectsPage'
import PersonalizeManagement from './modules/admin/pages/PersonalizeManagement'
import UserProfileProfiles from './modules/admin/pages/UserProfileProfiles'
import AdminHome from './modules/admin/pages/AdminHome'
import OrgStructurePage from './modules/mdm/org_structure/pages/OrgStructurePage'
import PartyPage from './modules/mdm/party/pages/PartyPage'
import PartyTcaManager from './modules/mdm/party/pages/PartyTcaManager'
import SupplierPage from './modules/mdm/party/pages/SupplierPage'
import CustomerPage from './modules/mdm/party/pages/CustomerPage'
import ItemPage from './modules/mdm/item/pages/ItemPage'
import BomPage from './modules/bom/pages/BomPage'
import DashboardHome from './components/DashboardHome'
import CollaborationDashboard from './modules/collaboration/pages/Dashboard'
import DiscussPage from './modules/collaboration/pages/DiscussPage'
import ChatPage from './modules/collaboration/pages/ChatPage'
import CalendarPage from './modules/collaboration/pages/CalendarPage'
import TodoPage from './modules/collaboration/pages/TodoPage'
import ActivitiesPage from './modules/collaboration/pages/ActivitiesPage'

function ThemeBridge() {
  const themeTokens = usePersonalizeStore((s) => s.themeTokens)
  const loadTheme = usePersonalizeStore((s) => s.loadTheme)
  const isDesignMode = usePersonalizeStore((s) => s.isDesignMode)
  const authed = useAuthStore((s) => s.user)
  useEffect(() => {
    if (authed) loadTheme()
  }, [authed, loadTheme])
  useEffect(() => {
    applyThemeToRoot(themeTokens)
  }, [themeTokens, isDesignMode])
  return null
}

export default function App() {
  const checkAuth = useAuthStore((s) => s.checkAuth)

  useEffect(() => {
    checkAuth()
  }, [checkAuth])

  return (
    <BrowserRouter>
      <ThemeBridge />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          element={
            <ProtectedRoute>
              <Layout />
            </ProtectedRoute>
          }
        >
          <Route path="/" element={<DashboardHome />} />
          <Route path="/admin" element={<AdminHome />} />
          <Route path="/admin/users" element={<UserManagement />} />
          <Route path="/admin/roles" element={<RoleManagement />} />
          <Route path="/admin/objects" element={<ObjectsPage />} />
          <Route path="/admin/personalize" element={<PersonalizeManagement />} />
          <Route path="/admin/user-profiles" element={<UserProfileProfiles />} />
          <Route path="/org-structure" element={<OrgStructurePage />} />
          <Route path="/party" element={<PartyPage />} />
          <Route path="/party/tca" element={<PartyTcaManager />} />
          <Route path="/party/suppliers" element={<SupplierPage />} />
          <Route path="/party/suppliers/:supplierId" element={<SupplierPage />} />
          <Route path="/party/customers" element={<CustomerPage />} />
          <Route path="/party/customers/:customerId" element={<CustomerPage />} />
          <Route path="/items" element={<ItemPage />} />
          <Route path="/bom" element={<BomPage />} />
          <Route path="/collaboration" element={<CollaborationDashboard />} />
          <Route path="/collaboration/discuss" element={<DiscussPage />} />
          <Route path="/collaboration/chat" element={<ChatPage />} />
          <Route path="/collaboration/calendar" element={<CalendarPage />} />
          <Route path="/collaboration/todo" element={<TodoPage />} />
          <Route path="/collaboration/activities" element={<ActivitiesPage />} />
          <Route path="/po" element={<div className="p-4"><h1 className="text-2xl! font-bold text-slate-900! dark:text-white!">Purchase Orders</h1><p className="text-sm text-slate-500! dark:text-slate-300! mt-2">Purchase order management coming soon.</p></div>} />
          <Route path="/gl" element={<div className="p-4"><h1 className="text-2xl! font-bold text-slate-900! dark:text-white!">General Ledger</h1><p className="text-sm text-slate-500! dark:text-slate-300! mt-2">General ledger module coming soon.</p></div>} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
