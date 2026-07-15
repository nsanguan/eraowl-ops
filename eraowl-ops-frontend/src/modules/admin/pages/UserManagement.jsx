import { useState, useEffect, useCallback, useRef } from 'react'
import api from '../../../api/client'
import { Plus, Download } from 'lucide-react'
import { InteractiveGrid } from '../../../shared-ui-kit/components/ui/InteractiveGrid'
import UserAssignmentModal from '../components/UserAssignmentModal'

export default function UserManagement() {
  const [users, setUsers] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [modalOpen, setModalOpen] = useState(false)
  const [editingUser, setEditingUser] = useState(null)
  const [saving, setSaving] = useState(false)
  const [formError, setFormError] = useState(null)
  const [selectedUserId, setSelectedUserId] = useState(null)
  const [assignModalUser, setAssignModalUser] = useState(null)
  const [search, setSearch] = useState('')
  const searchTimeout = useRef(null)

  const [form, setForm] = useState({ username: '', email: '', password: '', is_active: true, roles: [] })
  const [availableRoles, setAvailableRoles] = useState([])
  const [showPassword, setShowPassword] = useState(false)

  const fetchUsers = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const params = { page: 1, page_size: 100 }
      if (search) params.search = search
      const { data } = await api.get('/admin/users', { params })
      setUsers(data.items || data.data || [])
    } catch (err) {
      setError(err.response?.data?.detail?.message || 'Failed to load users')
    } finally { setLoading(false) }
  }, [search])

  const fetchRoles = useCallback(async () => {
    try {
      const { data } = await api.get('/admin/roles', { params: { page: 1, page_size: 100 } })
      setAvailableRoles(data.items || data.data || [])
    } catch {}
  }, [])

  useEffect(() => { fetchUsers(); fetchRoles() }, [fetchUsers, fetchRoles])

  const handleSearch = (query) => {
    if (searchTimeout.current) clearTimeout(searchTimeout.current)
    searchTimeout.current = setTimeout(() => setSearch(query), 300)
  }

  const userId = (u) => u.user_id || u.id

  const openCreateModal = () => {
    setEditingUser(null)
    setForm({ username: '', email: '', password: '', is_active: true, roles: [] })
    setFormError(null); setShowPassword(false); setModalOpen(true)
  }

  const openEditModal = (user) => {
    setEditingUser(user)
    setForm({
      username: user.username || '', email: user.email || '', password: '',
      is_active: user.is_active !== false,
      roles: (user.roles || []).map((r) => typeof r === 'object' ? (r.role_id || r.id) : r),
    })
    setFormError(null); setShowPassword(false); setModalOpen(true)
  }

  const closeModal = () => { setModalOpen(false); setEditingUser(null) }

  const handleRoleToggle = (roleId) => {
    setForm((prev) => ({
      ...prev,
      roles: prev.roles.includes(roleId) ? prev.roles.filter((id) => id !== roleId) : [...prev.roles, roleId],
    }))
  }

  const handleSave = async (e) => {
    e.preventDefault()
    setSaving(true); setFormError(null)
    try {
      const payload = { username: form.username, email: form.email, is_active: form.is_active }
      if (form.password) payload.password = form.password

      let uid = editingUser?.user_id || editingUser?.id

      if (editingUser) {
        await api.put(`/admin/users/${uid}`, payload)
      } else {
        const { data } = await api.post('/admin/users', payload)
        uid = data.user_id
      }

      // Save roles separately via dedicated endpoint
      if (form.roles.length > 0) {
        await api.put(`/admin/users/${uid}/roles`, { role_ids: form.roles })
      }

      closeModal(); fetchUsers()
    } catch (err) {
      setFormError(err.response?.data?.detail?.message || 'Failed to save user')
    } finally { setSaving(false) }
  }

  const handleDelete = async (user) => {
    const uid = userId(user)
    if (!window.confirm(`Delete user "${user.username}"? This will permanently remove the user.`)) return
    try {
      await api.delete(`/admin/users/${uid}`)
      fetchUsers()
      if (selectedUserId === uid) setSelectedUserId(null)
    } catch (err) {
      const msg = err.response?.data?.detail?.message || err.response?.data?.detail || ''
      if (msg.includes('deactivate')) {
        if (window.confirm(`Cannot delete "${user.username}" — they have related records.\n\nDeactivate this user instead (set to inactive)?`)) {
          try {
            await api.put(`/admin/users/${uid}/deactivate`)
            fetchUsers()
          } catch { setError('Failed to deactivate user') }
        }
      } else {
        setError(err.response?.data?.detail?.message || 'Failed to delete user')
      }
    }
  }

  const handleExportCSV = () => {
    const headers = ['Username', 'Email', 'Status', 'Roles', 'Last Login']
    const rows = users.map((u) => [
      u.username, u.email || '', u.is_active !== false ? 'Active' : 'Inactive',
      (u.roles || []).map((r) => (typeof r === 'object' ? (r.role_name || r.name) : r)).join('; '),
      u.last_login_at ? new Date(u.last_login_at).toISOString() : '',
    ])
    const csv = [headers, ...rows].map((r) => r.map((c) => `"${String(c).replace(/"/g, '""')}"`).join(',')).join('\n')
    const blob = new Blob(['\uFEFF' + csv], { type: 'text/csv;charset=utf-8' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a'); a.href = url; a.download = `users_${new Date().toISOString().slice(0, 10)}.csv`; a.click()
    URL.revokeObjectURL(url)
  }

  const columns = [
    { key: 'username', header: 'Username', width: '180px' },
    { key: 'email', header: 'Email', width: '220px', render: (row) => row.email || '—' },
    {
      key: 'is_active', header: 'Status', width: '100px',
      render: (row) => (
        <span className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wide ${
          row.is_active !== false ? 'bg-success/10 text-success' : 'bg-outline-variant/30 text-outline'
        }`}>
          <span className={`w-1.5 h-1.5 rounded-full ${row.is_active !== false ? 'bg-success' : 'bg-outline'}`} />
          {row.is_active !== false ? 'Active' : 'Inactive'}
        </span>
      ),
    },
    {
      key: 'roles', header: 'Roles', width: '200px',
      render: (row) => (
        <div className="flex flex-wrap gap-1">
          {(row.roles || []).length === 0 ? '—' : (row.roles || []).map((r) => (
            <span key={typeof r === 'object' ? (r.role_id || r.id) : r}
              className="px-2 py-0.5 bg-primary/10 text-primary rounded-md text-[10px] font-medium">
              {typeof r === 'object' ? (r.role_name || r.name) : r}
            </span>
          ))}
        </div>
      ),
    },
    {
      key: 'last_login_at', header: 'Last Login', width: '180px',
      render: (row) => row.last_login_at
        ? new Date(row.last_login_at).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' })
        : '—',
    },
  ]

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-on-surface">Users</h1>
          <p className="text-sm text-outline mt-1">Manage user accounts and role assignments</p>
        </div>
        <div className="flex items-center gap-2">
          <button onClick={handleExportCSV}
            className="neo-button flex items-center gap-1.5 px-3 py-2 text-on-surface-variant font-medium text-xs hover:text-primary">
            <Download size={14} /> Export
          </button>
          <button onClick={openCreateModal}
            className="flex items-center gap-1.5 px-4 py-2 bg-primary text-primary-foreground rounded-xl text-xs font-bold hover:opacity-90 transition-all shadow-lg shadow-primary/20">
            <Plus size={15} /> Create User
          </button>
        </div>
      </div>

      {error && (
        <div className="bg-error-container text-error p-4 rounded-xl text-sm font-medium border border-error/20">{error}</div>
      )}

      <InteractiveGrid
        columns={columns}
        data={users}
        loading={loading}
        idKey="user_id"
        searchable
        onSearch={handleSearch}
        onRowClick={(row) => setSelectedUserId(userId(row) === selectedUserId ? null : userId(row))}
        onEdit={(row) => openEditModal(row)}
        onDelete={(row) => handleDelete(row)}
        onAddRow={openCreateModal}
        addLabel="Add User"
        tableHeight="calc(100vh - 280px)"
      />

      {selectedUserId && (
        <div className="neo-card p-4 flex items-center justify-between">
          <p className="text-sm text-on-surface font-medium">
            Selected: {users.find((u) => userId(u) === selectedUserId)?.username || ''}
          </p>
          <div className="flex items-center gap-2">
            <button onClick={() => { const u = users.find((u) => userId(u) === selectedUserId); if (u) openEditModal(u) }}
              className="neo-button px-3 py-1.5 text-xs font-semibold text-primary">Edit</button>
            <button onClick={() => { const u = users.find((u) => userId(u) === selectedUserId); if (u) setAssignModalUser(u) }}
              className="neo-button px-3 py-1.5 text-xs font-semibold text-primary flex items-center gap-1">
              <span className="material-symbols-outlined text-[14px]">assignment_ind</span> Assign
            </button>
            <button onClick={() => { const u = users.find((u) => userId(u) === selectedUserId); if (u) handleDelete(u) }}
              className="neo-button px-3 py-1.5 text-xs font-semibold text-error">Delete</button>
          </div>
        </div>
      )}

      {assignModalUser && (
        <UserAssignmentModal
          user={assignModalUser}
          onClose={() => setAssignModalUser(null)}
          onSaved={fetchUsers}
        />
      )}

      {modalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm p-4">
          <div className="bg-surface-container rounded-2xl border border-outline-variant shadow-2xl w-full max-w-lg max-h-[90vh] overflow-y-auto custom-scrollbar">
            <div className="flex items-center justify-between p-5 border-b border-outline-variant">
              <h2 className="text-lg font-bold text-on-surface">{editingUser ? 'Edit User' : 'Create User'}</h2>
              <button onClick={closeModal} className="p-1.5 rounded-lg hover:bg-surface-container-high text-outline hover:text-on-surface transition-colors">
              <span className="material-symbols-outlined text-[18px]">close</span>
              </button>
            </div>
            <form onSubmit={handleSave} className="p-5 space-y-4">
              {formError && <div className="bg-error-container text-error p-3 rounded-xl text-sm font-medium">{formError}</div>}
              <div>
                <label className="block text-[11px] font-semibold uppercase tracking-wider text-outline mb-1.5">Username *</label>
                <input type="text" value={form.username} onChange={(e) => setForm({ ...form, username: e.target.value })}
                  className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition" required />
              </div>
              <div>
                <label className="block text-[11px] font-semibold uppercase tracking-wider text-outline mb-1.5">Email</label>
                <input type="email" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })}
                  className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition" />
              </div>
              <div>
                <label className="block text-[11px] font-semibold uppercase tracking-wider text-outline mb-1.5">
                  Password {editingUser ? '(leave blank to keep)' : '*'}
                </label>
                <div className="relative">
                  <input type={showPassword ? 'text' : 'password'} value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })}
                    className="w-full px-3 py-2.5 pr-10 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition" required={!editingUser} />
                  <button type="button" onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-2 top-1/2 -translate-y-1/2 p-1.5 text-outline hover:text-on-surface-variant transition-colors">
                    <span className="material-symbols-outlined text-[16px]">{showPassword ? 'visibility_off' : 'visibility'}</span>
                  </button>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <button type="button" role="switch" aria-checked={form.is_active}
                  onClick={() => setForm({ ...form, is_active: !form.is_active })}
                  className={`relative w-10 h-6 rounded-full transition-colors ${form.is_active ? 'bg-success' : 'bg-outline-variant'}`}>
                  <span className={`absolute top-1 w-4 h-4 rounded-full bg-white shadow transition-transform ${form.is_active ? 'left-5' : 'left-1'}`} />
                </button>
                <label className="text-sm font-medium text-on-surface cursor-pointer" onClick={() => setForm({ ...form, is_active: !form.is_active })}>Active</label>
              </div>
              <div>
                <label className="block text-[11px] font-semibold uppercase tracking-wider text-outline mb-2">Roles</label>
                <div className="space-y-1 max-h-48 overflow-y-auto custom-scrollbar border border-outline-variant rounded-xl p-2">
                  {availableRoles.map((role) => {
                    const rid = role.role_id || role.id
                    return (
                      <label key={rid} className="flex items-center gap-3 text-sm cursor-pointer py-1.5 px-2 rounded-lg hover:bg-surface-container-high transition-colors">
                        <input type="checkbox" checked={form.roles.includes(rid)} onChange={() => handleRoleToggle(rid)} className="rounded accent-primary w-4 h-4" />
                        <span className="text-on-surface">{role.role_name || role.name}</span>
                      </label>
                    )
                  })}
                </div>
              </div>
              <div className="flex justify-end gap-3 pt-2">
                <button type="button" onClick={closeModal}
                  className="neo-button px-5 py-2.5 text-sm font-semibold text-on-surface-variant">Cancel</button>
                <button type="submit" disabled={saving}
                  className="flex items-center gap-2 px-5 py-2.5 bg-primary text-primary-foreground rounded-xl text-sm font-semibold hover:opacity-90 disabled:opacity-50 transition-all shadow-lg shadow-primary/20">
                  {saving && <span className="animate-spin inline-block w-4 h-4 border-2 border-white/30 border-t-white rounded-full" />}
                  {editingUser ? 'Save Changes' : 'Create User'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  )
}
