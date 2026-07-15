import { useState, useEffect, useCallback } from 'react'
import api from '../../../api/client'

export default function RolePrivilegeMatrix() {
  const [roles, setRoles] = useState([])
  const [privileges, setPrivileges] = useState([])
  const [rolePerms, setRolePerms] = useState({})
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [changed, setChanged] = useState(false)
  const [dirty, setDirty] = useState({})

  const fetchAll = useCallback(async () => {
    setLoading(true)
    try {
      const [rolesRes, privRes] = await Promise.all([
        api.get('/admin/roles', { params: { page: 1, page_size: 100 } }),
        api.get('/admin/privileges'),
      ])
      const roleList = rolesRes.data.items || rolesRes.data.data || rolesRes.data || []
      setRoles(roleList)

      const privList = privRes.data || []
      setPrivileges(privList)

      const initPerms = {}
      const initDirty = {}
      await Promise.all(roleList.map(async (role) => {
        const rid = role.role_id || role.id
        try {
          const { data } = await api.get(`/admin/roles/${rid}/permissions`)
          const ids = (data || []).map((p) => p.privilege_id || p.id)
          initPerms[rid] = new Set(ids)
        } catch {
          initPerms[rid] = new Set()
        }
        initDirty[rid] = new Set()
      }))
      setRolePerms(initPerms)
      setDirty(initDirty)
    } catch (err) {
      console.error('Failed to load matrix data:', err)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => { fetchAll() }, [fetchAll])

  const grouped = privileges.reduce((acc, p) => {
    const mod = p.module || 'unknown'
    if (!acc[mod]) acc[mod] = []
    acc[mod].push(p)
    return acc
  }, {})

  const moduleOrder = Object.keys(grouped).sort()
  const allActions = [...new Set(privileges.map((p) => p.action))]

  const isChecked = (roleId, privId) => {
    const base = rolePerms[roleId]
    const d = dirty[roleId]
    if (!base) return false
    if (d && d.has(privId)) return !base.has(privId)
    return base.has(privId)
  }

  const handleToggle = (roleId, privId) => {
    setDirty((prev) => {
      const next = { ...prev }
      const set = new Set(next[roleId] || [])
      if (set.has(privId)) set.delete(privId)
      else set.add(privId)
      next[roleId] = set
      return next
    })
    setChanged(true)
  }

  const handleToggleAllForRole = (roleId, privIds, checked) => {
    setDirty((prev) => {
      const next = { ...prev }
      const set = new Set(next[roleId] || [])
      privIds.forEach((pid) => {
        const base = rolePerms[roleId]
        const currentlyOn = base && base.has(pid)
        if (checked && !currentlyOn) set.add(pid)
        else if (!checked && currentlyOn) set.add(pid)
        else set.delete(pid)
      })
      next[roleId] = set
      return next
    })
    setChanged(true)
  }

  const handleToggleModuleForRole = (roleId, modPrivIds, checked) => {
    handleToggleAllForRole(roleId, modPrivIds, checked)
  }

  const handleSave = async () => {
    setSaving(true)
    try {
      const ops = []
      for (const roleId of Object.keys(dirty)) {
        if (dirty[roleId].size === 0) continue
        const base = rolePerms[roleId] || new Set()
        const finalIds = new Set(base)
        for (const privId of dirty[roleId]) {
          if (base.has(privId)) finalIds.delete(privId)
          else finalIds.add(privId)
        }
        ops.push(
          api.put(`/admin/roles/${roleId}/permissions`, {
            privilege_ids: [...finalIds],
          })
        )
      }
      await Promise.all(ops)
      await fetchAll()
      setChanged(false)
    } catch (err) {
      alert(err.response?.data?.detail?.message || 'Failed to save permissions')
    } finally {
      setSaving(false)
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center py-16 text-outline">
        <span className="material-symbols-outlined text-[24px] animate-spin mr-3">progress_activity</span>
        <span className="text-sm">Loading permission matrix...</span>
      </div>
    )
  }

  return (
    <div className="eods-matrix">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h2 className="text-lg font-bold text-on-surface">Permission Matrix</h2>
          <p className="text-sm text-outline mt-0.5">Manage permissions across all roles. Toggle switches to grant or revoke access.</p>
        </div>
        {changed && (
          <button onClick={handleSave} disabled={saving}
            className="flex items-center gap-2 px-5 py-2.5 bg-primary text-primary-foreground rounded-xl text-sm font-semibold hover:opacity-90 disabled:opacity-50 transition-all shadow-lg shadow-primary/20">
            {saving ? (
              <><span className="animate-spin inline-block w-4 h-4 border-2 border-white/30 border-t-white rounded-full" /> Saving...</>
            ) : (
              <><span className="material-symbols-outlined text-[18px]">save</span> Save Changes</>
            )}
          </button>
        )}
      </div>

      <div className="border border-outline-variant rounded-xl overflow-hidden bg-surface-container-lowest">
        <div className="overflow-auto custom-scrollbar" style={{ maxHeight: 'calc(100vh - 280px)' }}>
          <table className="eods-matrix__table w-full text-xs">
            <thead>
              <tr className="bg-surface-container-low border-b border-outline-variant sticky top-0 z-10">
                <th className="text-left px-3 py-3 font-semibold text-outline min-w-[180px]">Module / Action</th>
                {roles.map((role) => {
                  const rid = role.role_id || role.id
                  const allPrivIds = privileges.map((p) => p.privilege_id || p.id)
                  const baseSet = rolePerms[rid] || new Set()
                  const dirtySet = dirty[rid] || new Set()
                  let allOn = true
                  let anyOn = false
                  for (const pid of allPrivIds) {
                    const isOn = dirtySet.has(pid) ? !baseSet.has(pid) : baseSet.has(pid)
                    if (isOn) anyOn = true
                    else allOn = false
                  }
                  return (
                    <th key={rid} className="text-center px-2 py-3 font-semibold text-outline min-w-[120px]">
                      <div className="flex flex-col items-center gap-1">
                        <span className="text-[11px] leading-tight">{role.role_name || role.name}</span>
                        <button onClick={() => handleToggleAllForRole(rid, allPrivIds, !allOn)}
                          className="text-[10px] text-primary hover:text-primary/80 font-semibold transition-colors">
                          {allOn ? 'Deselect All' : 'Select All'}
                        </button>
                      </div>
                    </th>
                  )
                })}
              </tr>
            </thead>
            <tbody>
              {moduleOrder.length === 0 ? (
                <tr>
                  <td colSpan={roles.length + 1} className="text-center py-12 text-sm text-outline">
                    No privileges defined. Seed privileges first.
                  </td>
                </tr>
              ) : moduleOrder.map((mod) => {
                const modPrivs = grouped[mod]
                return (
                  <tr key={mod} className="bg-surface-container-low/50">
                    <td className="px-3 py-2 font-semibold text-on-surface-variant text-[11px] uppercase tracking-wider" colSpan={roles.length + 1}>
                      {mod}
                    </td>
                  </tr>
                )
              }).concat(
                moduleOrder.flatMap((mod) =>
                  grouped[mod].map((priv) => {
                    const pid = priv.privilege_id || priv.id
                    return (
                      <tr key={pid} className="border-b border-outline-variant/20 hover:bg-surface-container-low/30 transition-colors">
                        <td className="px-3 py-2 text-on-surface text-[12px] pl-6">
                          {priv.action}
                          {priv.description && (
                            <span className="ml-2 text-outline text-[10px]">({priv.description})</span>
                          )}
                        </td>
                        {roles.map((role) => {
                          const rid = role.role_id || role.id
                          const checked = isChecked(rid, pid)
                          return (
                            <td key={`${rid}-${pid}`} className="text-center px-2 py-2">
                              <label className="inline-flex items-center cursor-pointer">
                                <input type="checkbox" checked={checked}
                                  onChange={() => handleToggle(rid, pid)}
                                  className="sr-only peer" />
                                <div className={`
                                  relative w-9 h-5 rounded-full transition-colors peer-focus-visible:ring-2 peer-focus-visible:ring-primary/40
                                  ${checked ? 'bg-primary' : 'bg-outline-variant'}
                                  after:content-[''] after:absolute after:top-0.5 after:start-0.5 after:bg-white after:rounded-full after:h-4 after:w-4 after:transition-all
                                  ${checked ? 'after:translate-x-4' : ''}
                                `} />
                              </label>
                            </td>
                          )
                        })}
                      </tr>
                    )
                  })
                )
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}
