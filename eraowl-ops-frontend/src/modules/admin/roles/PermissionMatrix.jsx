import { useState, useEffect, useCallback } from 'react'
import api from '../../../api/client'
import { SwitchToggle } from '../../../shared-ui-kit/components/ui/SwitchToggle'

export default function PermissionMatrix() {
  const [roles, setRoles] = useState([])
  const [privileges, setPrivileges] = useState([])
  const [matrix, setMatrix] = useState({})
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [changed, setChanged] = useState(false)

  const fetchMatrix = useCallback(async () => {
    setLoading(true)
    try {
      const { data } = await api.get('/admin/roles/permission-matrix')
      setRoles(data.roles || [])
      setPrivileges(data.privileges || [])
      const init = {}
      for (const r of data.roles || []) {
        const rid = r.role_id || r.id
        init[rid] = new Set((data.matrix || {})[rid] || [])
      }
      setMatrix(init)
    } catch (err) {
      console.error('Failed to load permission matrix:', err)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => { fetchMatrix() }, [fetchMatrix])

  const grouped = privileges.reduce((acc, p) => {
    const mod = (p.module || 'unknown').toLowerCase()
    if (!acc[mod]) acc[mod] = []
    acc[mod].push(p)
    return acc
  }, {})

  const moduleOrder = Object.keys(grouped).sort()

  const handleToggle = (roleId, privId) => {
    setMatrix(prev => {
      const next = { ...prev }
      const s = new Set(next[roleId] || [])
      if (s.has(privId)) s.delete(privId)
      else s.add(privId)
      next[roleId] = s
      return next
    })
    setChanged(true)
  }

  const handleSelectAll = (roleId, privIds, checked) => {
    setMatrix(prev => {
      const next = { ...prev }
      next[roleId] = new Set(checked ? privIds : [])
      return next
    })
    setChanged(true)
  }

  const handleModuleToggle = (roleId, modPrivIds, checked) => {
    setMatrix(prev => {
      const next = { ...prev }
      const s = new Set(next[roleId] || [])
      for (const pid of modPrivIds) {
        if (checked) s.add(pid)
        else s.delete(pid)
      }
      next[roleId] = s
      return next
    })
    setChanged(true)
  }

  const handleSave = async () => {
    setSaving(true)
    try {
      const payload = {}
      for (const rid of Object.keys(matrix)) {
        payload[rid] = [...matrix[rid]]
      }
      await api.put('/admin/roles/permission-matrix/sync', { matrix: payload })
      await fetchMatrix()
      setChanged(false)
    } catch (err) {
      alert(err.response?.data?.detail?.message || 'Failed to save permission matrix')
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
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-lg font-bold text-slate-900! dark:text-white!">Permission Matrix</h2>
          <p className="text-sm text-slate-500! dark:text-slate-300! mt-0.5">
            Manage permissions across all roles. Toggle switches to grant or revoke access.
          </p>
        </div>
        <button onClick={handleSave} disabled={saving || !changed}
          className="flex items-center gap-2 px-5 py-2.5 bg-primary text-primary-foreground rounded-xl text-sm font-semibold hover:opacity-90 disabled:opacity-50 transition-all shadow-lg shadow-primary/20">
          {saving ? (
            <><span className="animate-spin inline-block w-4 h-4 border-2 border-white/30 border-t-white rounded-full" /> Saving...</>
          ) : (
            <><span className="material-symbols-outlined text-[18px]">save</span> Save Configuration</>
          )}
        </button>
      </div>

      <div className="border border-outline-variant rounded-xl overflow-hidden bg-surface-container-lowest">
        <div className="overflow-auto custom-scrollbar" style={{ maxHeight: 'calc(100vh - 280px)' }}>
          <table className="w-full text-xs">
            <thead>
              <tr className="bg-surface-container-low border-b border-outline-variant sticky top-0 z-10">
                <th className="text-left px-3 py-3 font-semibold text-outline min-w-[180px]">Module / Action</th>
                {roles.map((role) => {
                  const rid = role.role_id || role.id
                  const allPrivIds = privileges.map((p) => p.privilege_id || p.id)
                  const currentSet = matrix[rid] || new Set()
                  const allOn = allPrivIds.length > 0 && allPrivIds.every((pid) => currentSet.has(pid))
                  return (
                    <th key={rid} className="text-center px-2 py-3 font-semibold text-outline min-w-[120px] max-w-[140px]">
                      <div className="flex flex-col items-center gap-1">
                        <span className="text-[11px] leading-tight break-words">{role.role_name}</span>
                        <button onClick={() => handleSelectAll(rid, allPrivIds, !allOn)}
                          className="text-[10px] text-primary hover:text-primary/80 font-semibold transition-colors whitespace-nowrap">
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
              ) : moduleOrder.map((mod) => [
                <tr key={`h-${mod}`} className="bg-surface-container-low/50">
                  <td className="px-3 py-2 font-semibold text-on-surface-variant text-[11px] uppercase tracking-wider" colSpan={roles.length + 1}>
                    <div className="flex items-center gap-2">
                      <span>{mod}</span>
                      {roles.map((role) => {
                        const rid = role.role_id || role.id
                        const modPrivIds = grouped[mod].map((p) => p.privilege_id || p.id)
                        const currentSet = matrix[rid] || new Set()
                        const allOn = modPrivIds.every((pid) => currentSet.has(pid))
                        return (
                          <button key={rid} onClick={() => handleModuleToggle(rid, modPrivIds, !allOn)}
                            className="text-[10px] text-primary/60 hover:text-primary font-semibold transition-colors">
                            {allOn ? '×' : '○'}
                          </button>
                        )
                      })}
                    </div>
                  </td>
                </tr>,
                ...grouped[mod].map((priv) => {
                  const pid = priv.privilege_id || priv.id
                  return (
                    <tr key={pid} className="border-b border-outline-variant/20 hover:bg-surface-container-low/30 transition-colors">
                      <td className="px-3 py-2 text-on-surface text-[12px] pl-6">
                        <span className="font-medium">{priv.action}</span>
                        {priv.description && (
                          <span className="ml-2 text-outline text-[10px]">({priv.description})</span>
                        )}
                      </td>
                      {roles.map((role) => {
                        const rid = role.role_id || role.id
                        const checked = matrix[rid] ? matrix[rid].has(pid) : false
                        return (
                          <td key={`${rid}-${pid}`} className="text-center px-2 py-2">
                            <SwitchToggle
                              checked={checked}
                              onChange={() => handleToggle(rid, pid)}
                              size="sm"
                            />
                          </td>
                        )
                      })}
                    </tr>
                  )
                }),
              ])}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}
