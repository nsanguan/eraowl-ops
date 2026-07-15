import { useState, useEffect, useCallback } from 'react'
import api from '../../../api/client'
import { ShuttleControl } from '../../../shared-ui-kit/components/ui/ShuttleControl'

const TAB_ROLES = 'roles'
const TAB_BUS = 'bus'

export default function UserAssignmentModal({ user, onClose, onSaved }) {
  const [tab, setTab] = useState(TAB_ROLES)
  const [allRoles, setAllRoles] = useState([])
  const [allBus, setAllBus] = useState([])
  const [userRoleIds, setUserRoleIds] = useState([])
  const [userBuIds, setUserBuIds] = useState([])
  const [saving, setSaving] = useState(false)
  const [loading, setLoading] = useState(true)

  const uid = user?.user_id || user?.id

  const fetchAll = useCallback(async () => {
    setLoading(true)
    try {
      const [rolesRes, busRes, userRolesRes, userBusRes] = await Promise.all([
        api.get('/admin/roles', { params: { page: 1, page_size: 100 } }),
        api.get('/org_structure/business-units', { params: { page: 1, page_size: 500 } }),
        api.get(`/admin/users/${uid}/roles`),
        api.get(`/admin/users/${uid}/business-units`),
      ])

      const roles = rolesRes.data.items || rolesRes.data.data || rolesRes.data || []
      const bus = busRes.data.items || busRes.data.data || busRes.data || []

      setAllRoles(Array.isArray(roles) ? roles : [])
      setAllBus(Array.isArray(bus) ? bus : [])

      const roleIds = (userRolesRes.data || []).map((r) => r.role_id || r.id)
      setUserRoleIds(roleIds)

      const buIds = (userBusRes.data || []).map((id) => typeof id === 'string' ? id : id.business_unit_id || id.id)
      setUserBuIds(buIds)
    } catch (err) {
      console.error('Failed to load assignment data:', err)
    } finally {
      setLoading(false)
    }
  }, [uid])

  useEffect(() => { fetchAll() }, [fetchAll])

  const allRoleItems = allRoles.map((r) => ({
    id: r.role_id || r.id,
    label: r.role_name || r.name,
    description: r.description || '',
  }))

  const selectedRoleItems = allRoleItems.filter((r) => userRoleIds.includes(r.id))

  const allBuItems = allBus.map((b) => ({
    id: b.business_unit_id || b.id,
    label: b.bu_name || b.name,
    description: b.bu_code || '',
  }))

  const selectedBuItems = allBuItems.filter((b) => userBuIds.includes(b.id))

  const handleSave = async () => {
    setSaving(true)
    try {
      await Promise.all([
        api.put(`/admin/users/${uid}/roles`, { role_ids: userRoleIds }),
        api.put(`/admin/users/${uid}/business-units`, { bu_ids: userBuIds }),
      ])
      onSaved?.()
      onClose()
    } catch (err) {
      alert(err.response?.data?.detail?.message || 'Failed to save assignments')
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40" onClick={onClose}>
      <div className="bg-surface-container rounded-2xl border border-outline-variant shadow-2xl w-full max-w-3xl max-h-[90vh] overflow-hidden flex flex-col" onClick={e => e.stopPropagation()}>
        <div className="flex items-center justify-between p-5 border-b border-outline-variant shrink-0">
          <div>
            <h2 className="text-lg font-bold text-on-surface">User Assignments</h2>
            <p className="text-sm text-outline mt-0.5">{user?.username || user?.email}</p>
          </div>
          <button onClick={onClose} className="p-1.5 rounded-lg hover:bg-surface-container-high text-outline hover:text-on-surface transition-colors">
            <span className="material-symbols-outlined text-[18px]">close</span>
          </button>
        </div>

        <div className="flex border-b border-outline-variant shrink-0">
          <button onClick={() => setTab(TAB_ROLES)}
            className={`flex-1 py-3 text-sm font-semibold transition-colors relative ${
              tab === TAB_ROLES ? 'text-primary' : 'text-outline hover:text-on-surface'
            }`}>
            Assigned Roles
            {tab === TAB_ROLES && <div className="absolute bottom-0 left-4 right-4 h-0.5 bg-primary rounded-full" />}
          </button>
          <button onClick={() => setTab(TAB_BUS)}
            className={`flex-1 py-3 text-sm font-semibold transition-colors relative ${
              tab === TAB_BUS ? 'text-primary' : 'text-outline hover:text-on-surface'
            }`}>
            Authorized Business Units
            {tab === TAB_BUS && <div className="absolute bottom-0 left-4 right-4 h-0.5 bg-primary rounded-full" />}
          </button>
        </div>

        <div className="p-5 flex-1 overflow-y-auto custom-scrollbar min-h-[400px]">
          {loading ? (
            <div className="flex items-center justify-center py-16 text-outline">
              <span className="material-symbols-outlined text-[24px] animate-spin mr-3">progress_activity</span>
              <span className="text-sm">Loading...</span>
            </div>
          ) : tab === TAB_ROLES ? (
            <ShuttleControl
              availableItems={allRoleItems}
              selectedItems={selectedRoleItems}
              onChange={(ids) => setUserRoleIds(ids)}
              availableLabel="Available Roles"
              selectedLabel="Assigned Roles"
              height="320px"
            />
          ) : (
            <ShuttleControl
              availableItems={allBuItems}
              selectedItems={selectedBuItems}
              onChange={(ids) => setUserBuIds(ids)}
              availableLabel="Available Business Units"
              selectedLabel="Authorized BUs"
              height="320px"
            />
          )}
        </div>

        <div className="flex justify-end gap-3 p-5 border-t border-outline-variant shrink-0">
          <button onClick={onClose}
            className="px-5 py-2.5 text-sm font-semibold text-on-surface-variant bg-surface-container-low border border-outline-variant rounded-xl hover:bg-surface-container-high transition-colors">
            Cancel
          </button>
          <button onClick={handleSave} disabled={saving || loading}
            className="flex items-center gap-2 px-5 py-2.5 bg-primary text-primary-foreground rounded-xl text-sm font-semibold hover:opacity-90 disabled:opacity-50 transition-all shadow-lg shadow-primary/20">
            {saving ? (
              <><span className="animate-spin inline-block w-4 h-4 border-2 border-white/30 border-t-white rounded-full" /> Saving...</>
            ) : (
              <><span className="material-symbols-outlined text-[18px]">save</span> Save Changes</>
            )}
          </button>
        </div>
      </div>
    </div>
  )
}
