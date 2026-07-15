import { useState, useEffect, useCallback } from 'react'
import api from '../../../api/client'
import { Plus } from 'lucide-react'
import { InteractiveGrid } from '../../../shared-ui-kit/components/ui/InteractiveGrid'
import RolePrivilegeMatrix from '../components/RolePrivilegeMatrix'

export default function RoleManagement() {
  const [roles, setRoles] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [modalOpen, setModalOpen] = useState(false)
  const [editingRole, setEditingRole] = useState(null)
  const [saving, setSaving] = useState(false)
  const [formError, setFormError] = useState(null)
  const [selectedRoleId, setSelectedRoleId] = useState(null)
  const [permissionsOpen, setPermissionsOpen] = useState(false)

  const [form, setForm] = useState({ name: '', description: '', permissions: {} })
  const [privileges, setPrivileges] = useState([])

  const roleId = (r) => r.role_id || r.id

  const fetchRoles = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.get('/admin/roles', { params: { page: 1, page_size: 100 } })
      setRoles(data.items || data.data || [])
    } catch (err) {
      setError(err.response?.data?.detail?.message || 'Failed to load roles')
    } finally { setLoading(false) }
  }, [])

  const fetchPrivileges = useCallback(async () => {
    try {
      const { data } = await api.get('/admin/privileges')
      setPrivileges(data.privileges || data.groups || data.modules || data || [])
    } catch {}
  }, [])

  useEffect(() => { fetchRoles(); fetchPrivileges() }, [fetchRoles, fetchPrivileges])

  const openCreateModal = () => {
    setEditingRole(null)
    setForm({ name: '', description: '', permissions: {} })
    setFormError(null); setPermissionsOpen(false); setModalOpen(true)
  }

  const openEditModal = (role) => {
    setEditingRole(role)
    const perms = {}
    if (role.permissions) {
      if (Array.isArray(role.permissions)) {
        role.permissions.forEach((p) => {
          const key = typeof p === 'string' ? p : `${p.module}:${p.action}`
          perms[key] = true
        })
      } else if (typeof role.permissions === 'object') {
        Object.assign(perms, role.permissions)
      }
    }
    setForm({ name: role.role_name || role.name || '', description: role.description || '', permissions: perms })
    setFormError(null); setPermissionsOpen(false); setModalOpen(true)
  }

  const closeModal = () => { setModalOpen(false); setEditingRole(null); setPermissionsOpen(false) }

  const normalizePrivileges = () => {
    if (!privileges || privileges.length === 0) return []
    const first = privileges[0]
    if (first && first.module && first.module_name) {
      return privileges.map((p) => ({
        module: p.module || p.module_name,
        label: p.label || p.module_name || p.module,
        actions: p.actions || p.permissions?.map((x) => x.action || x) || ['view', 'create', 'edit', 'delete'],
      }))
    }
    if (first && first.module && first.action) {
      const groups = {}
      privileges.forEach((p) => {
        if (!groups[p.module]) groups[p.module] = new Set()
        groups[p.module].add(p.action)
      })
      return Object.entries(groups).map(([m, a]) => ({ module: m, label: m, actions: [...a] }))
    }
    return []
  }

  const moduleList = normalizePrivileges()

  const allActions = moduleList.reduce((acc, m) => {
    m.actions.forEach((a) => { if (!acc.includes(a)) acc.push(a) })
    return acc
  }, [])

  const handlePermissionToggle = (module, action) => {
    const key = `${module}:${action}`
    setForm((prev) => {
      const next = { ...prev.permissions }
      if (next[key]) delete next[key]
      else next[key] = true
      return { ...prev, permissions: next }
    })
  }

  const handleToggleAll = (module, actions) => {
    setForm((prev) => {
      const next = { ...prev.permissions }
      const allOn = actions.every((a) => next[`${module}:${a}`])
      actions.forEach((a) => {
        if (allOn) delete next[`${module}:${a}`]
        else next[`${module}:${a}`] = true
      })
      return { ...prev, permissions: next }
    })
  }

  const handleToggleAllModules = (action) => {
    setForm((prev) => {
      const next = { ...prev.permissions }
      const allOn = moduleList.every((m) => next[`${m.module}:${action}`])
      moduleList.forEach((m) => {
        if (allOn) delete next[`${m.module}:${action}`]
        else next[`${m.module}:${action}`] = true
      })
      return { ...prev, permissions: next }
    })
  }

  const permissionsToArray = () =>
    Object.entries(form.permissions)
      .filter(([, v]) => v)
      .map(([key]) => {
        const [module, ...rest] = key.split(':')
        return { module, action: rest.join(':') }
      })

  const handleSave = async (e) => {
    e.preventDefault()
    setSaving(true); setFormError(null)
    try {
      const payload = {
        role_name: form.name,
        name: form.name,
        description: form.description,
        permissions: permissionsToArray(),
      }
      const rid = editingRole?.role_id || editingRole?.id
      if (editingRole) {
        await api.put(`/admin/roles/${rid}`, payload)
      } else {
        await api.post('/admin/roles', payload)
      }
      closeModal(); fetchRoles()
    } catch (err) {
      setFormError(err.response?.data?.detail?.message || 'Failed to save role')
    } finally { setSaving(false) }
  }

  const handleDelete = async (role) => {
    const rid = roleId(role)
    if (!window.confirm(`Delete role "${role.role_name || role.name}"?`)) return
    try {
      await api.delete(`/admin/roles/${rid}`)
      fetchRoles(); if (selectedRoleId === rid) setSelectedRoleId(null)
    } catch (err) {
      setError(err.response?.data?.detail?.message || 'Failed to delete role')
    }
  }

  const columns = [
    {
      key: 'role_name', header: 'Name', width: '180px',
      render: (row) => row.role_name || row.name,
    },
    {
      key: 'description', header: 'Description', width: '300px',
      render: (row) => row.description || '\u2014',
    },
    {
      key: 'permissions', header: 'Permissions', width: '200px',
      render: (row) => {
        if (!row.permissions) return '\u2014'
        const count = Array.isArray(row.permissions) ? row.permissions.length
          : typeof row.permissions === 'object' ? Object.keys(row.permissions).length : 0
        return (
          <span className="px-2 py-0.5 bg-primary/10 text-primary rounded-md text-[10px] font-medium">
            {count} permission{count !== 1 ? 's' : ''}
          </span>
        )
      },
    },
  ]

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-on-surface">Roles</h1>
          <p className="text-sm text-outline mt-1">Define user roles with granular permissions</p>
        </div>
        <div className="flex items-center gap-2">
          <button onClick={openCreateModal}
            className="flex items-center gap-1.5 px-4 py-2 bg-primary text-primary-foreground rounded-xl text-xs font-bold hover:opacity-90 transition-all shadow-lg shadow-primary/20">
            <Plus size={15} /> Create Role
          </button>
        </div>
      </div>

      {error && (
        <div className="bg-error-container text-error p-4 rounded-xl text-sm font-medium border border-error/20">{error}</div>
      )}

      <InteractiveGrid
        columns={columns}
        data={roles}
        loading={loading}
        idKey="role_id"
        searchable
        onRowClick={(row) => setSelectedRoleId(roleId(row) === selectedRoleId ? null : roleId(row))}
        onEdit={(row) => openEditModal(row)}
        onDelete={(row) => handleDelete(row)}
        onAddRow={openCreateModal}
        addLabel="Add Role"
        tableHeight="calc(100vh - 280px)"
      />

      {selectedRoleId && (
        <div className="neo-card p-4 flex items-center justify-between">
          <p className="text-sm text-on-surface font-medium">
            Selected: {roles.find((r) => roleId(r) === selectedRoleId)?.role_name || roles.find((r) => roleId(r) === selectedRoleId)?.name || ''}
          </p>
          <div className="flex items-center gap-2">
            <button onClick={() => { const r = roles.find((r) => roleId(r) === selectedRoleId); if (r) openEditModal(r) }}
              className="neo-button px-3 py-1.5 text-xs font-semibold text-primary">Edit</button>
            <button onClick={() => { const r = roles.find((r) => roleId(r) === selectedRoleId); if (r) handleDelete(r) }}
              className="neo-button px-3 py-1.5 text-xs font-semibold text-error">Delete</button>
          </div>
        </div>
      )}

      <RolePrivilegeMatrix />

      {modalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm p-4">
          <div className="bg-surface-container rounded-2xl border border-outline-variant shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-hidden flex flex-col">
            <div className="flex items-center justify-between p-5 border-b border-outline-variant shrink-0">
              <h2 className="text-lg font-bold text-on-surface">{editingRole ? 'Edit Role' : 'Create Role'}</h2>
              <button onClick={closeModal} className="p-1.5 rounded-lg hover:bg-surface-container-high text-outline hover:text-on-surface transition-colors">
                <span className="material-symbols-outlined text-[18px]">close</span>
              </button>
            </div>
            <form onSubmit={handleSave} className="flex flex-col flex-1 overflow-hidden">
              <div className="p-5 space-y-4 overflow-y-auto flex-1 custom-scrollbar">
                {formError && (
                  <div className="bg-error-container text-error p-3 rounded-xl text-sm font-medium">{formError}</div>
                )}
                <div>
                  <label className="block text-[11px] font-semibold uppercase tracking-wider text-outline mb-1.5">Name *</label>
                  <input type="text" value={form.name}
                    onChange={(e) => setForm({ ...form, name: e.target.value })}
                    className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition" required />
                </div>
                <div>
                  <label className="block text-[11px] font-semibold uppercase tracking-wider text-outline mb-1.5">Description</label>
                  <textarea value={form.description}
                    onChange={(e) => setForm({ ...form, description: e.target.value })}
                    rows={2}
                    className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition resize-none" />
                </div>
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <label className="text-[11px] font-semibold uppercase tracking-wider text-outline">Permissions</label>
                    <button type="button" onClick={() => setPermissionsOpen(!permissionsOpen)}
                      className="text-xs text-primary hover:text-primary/80 font-semibold transition-colors">
                      {permissionsOpen ? 'Collapse' : 'Expand'}
                    </button>
                  </div>
                  {permissionsOpen ? (
                    <div className="border border-outline-variant rounded-xl overflow-hidden">
                      <div className="overflow-x-auto custom-scrollbar">
                        <table className="w-full text-xs">
                          <thead>
                            <tr className="bg-surface-container-low border-b border-outline-variant">
                              <th className="text-left px-3 py-2.5 font-semibold text-outline w-40">Module</th>
                              {allActions.map((action) => (
                                <th key={action} className="text-center px-2 py-2.5 font-semibold text-outline">
                                  <button type="button" onClick={() => handleToggleAllModules(action)}
                                    className="hover:text-primary capitalize transition-colors">
                                    {action}
                                  </button>
                                </th>
                              ))}
                            </tr>
                          </thead>
                          <tbody>
                            {moduleList.length === 0 ? (
                              <tr>
                                <td colSpan={allActions.length + 1} className="text-center py-6 text-sm text-outline">No modules available. Seed privileges first.</td>
                              </tr>
                            ) : (
                              moduleList.map((mod) => {
                                const allOn = mod.actions.every((a) => form.permissions[`${mod.module}:${a}`])
                                return (
                                  <tr key={mod.module} className="border-b border-outline-variant/30 hover:bg-surface-container-low transition-colors">
                                    <td className="px-3 py-2">
                                      <button type="button" onClick={() => handleToggleAll(mod.module, mod.actions)}
                                        className={`font-semibold text-left transition-colors ${allOn ? 'text-primary' : 'text-on-surface-variant hover:text-primary'}`}>
                                        {mod.label || mod.module}
                                      </button>
                                    </td>
                                    {allActions.map((action) => {
                                      const key = `${mod.module}:${action}`
                                      const enabled = mod.actions.includes(action)
                                      const checked = !!form.permissions[key]
                                      return (
                                        <td key={action} className="text-center px-2 py-2">
                                          {enabled ? (
                                            <input type="checkbox" checked={checked}
                                              onChange={() => handlePermissionToggle(mod.module, action)}
                                              className="rounded accent-primary w-4 h-4 cursor-pointer" />
                                          ) : (
                                            <span className="text-outline-variant">\u2014</span>
                                          )}
                                        </td>
                                      )
                                    })}
                                  </tr>
                                )
                              })
                            )}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  ) : moduleList.length > 0 ? (
                    <div className="flex flex-wrap gap-1">
                      {Object.keys(form.permissions).length === 0 ? (
                        <span className="text-sm text-outline">No permissions granted</span>
                      ) : (
                        Object.keys(form.permissions).filter((k) => form.permissions[k]).map((key) => (
                          <span key={key} className="px-2 py-0.5 bg-primary/10 text-primary rounded-md text-[10px] font-medium">
                            {key}
                          </span>
                        ))
                      )}
                    </div>
                  ) : (
                    <p className="text-sm text-outline">No modules available</p>
                  )}
                </div>
              </div>
              <div className="flex justify-end gap-3 p-5 border-t border-outline-variant shrink-0">
                <button type="button" onClick={closeModal}
                  className="neo-button px-5 py-2.5 text-sm font-semibold text-on-surface-variant">Cancel</button>
                <button type="submit" disabled={saving}
                  className="flex items-center gap-2 px-5 py-2.5 bg-primary text-primary-foreground rounded-xl text-sm font-semibold hover:opacity-90 disabled:opacity-50 transition-all shadow-lg shadow-primary/20">
                  {saving && <span className="animate-spin inline-block w-4 h-4 border-2 border-white/30 border-t-white rounded-full" />}
                  {editingRole ? 'Save Changes' : 'Create Role'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  )
}
