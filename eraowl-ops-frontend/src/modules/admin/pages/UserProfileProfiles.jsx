import { useState, useEffect, useCallback } from 'react'
import api from '../../../api/client'
import { Plus } from 'lucide-react'
import PersonalizeWrapper from '../../../shared-ui-kit/components/ui/PersonalizeWrapper'
import usePersonalizeStore from '../../../store/usePersonalizeStore'

const LEVELS = [
  { code: 'site', label: 'Site' },
  { code: 'application', label: 'Application' },
  { code: 'role', label: 'Role' },
  { code: 'user', label: 'User' },
]

const VALUE_TYPES = ['text', 'number', 'date', 'checkbox', 'url']

export default function UserProfileProfiles() {
  const [options, setOptions] = useState([])
  const [loading, setLoading] = useState(true)
  const [search, setSearch] = useState('')
  const [modalOpen, setModalOpen] = useState(false)
  const [editing, setEditing] = useState(null)
  const [formError, setFormError] = useState(null)
  const [saving, setSaving] = useState(false)

  const [selected, setSelected] = useState(null)
  const [values, setValues] = useState([])
  const [effective, setEffective] = useState(null)
  const [detailLoading, setDetailLoading] = useState(false)
  const [drafts, setDrafts] = useState({}) // level_code -> value string

  const loadPersonalization = usePersonalizeStore((s) => s.loadPersonalization)
  useEffect(() => { loadPersonalization('admin.user_profiles') }, [loadPersonalization])

  const fetchOptions = useCallback(async () => {
    setLoading(true)
    try {
      const { data } = await api.get('/admin/profile-options', {
        params: { page: 1, page_size: 200, search: search || undefined },
      })
      setOptions(data.items || [])
    } catch {
      setOptions([])
    } finally {
      setLoading(false)
    }
  }, [search])

  useEffect(() => { fetchOptions() }, [fetchOptions])

  const openCreate = () => {
    setEditing(null)
    setFormError(null)
    setModalOpen(true)
  }
  const openEdit = (opt) => {
    setEditing(opt)
    setFormError(null)
    setModalOpen(true)
  }
  const closeModal = () => setModalOpen(false)

  const handleSave = async (e) => {
    e.preventDefault()
    setSaving(true)
    setFormError(null)
    const payload = {
      profile_option_name: e.target.profile_option_name.value.trim(),
      user_profile_option_name: e.target.user_profile_option_name.value.trim(),
      description: e.target.description.value.trim() || null,
      value_type: e.target.value_type.value,
      site_enabled: e.target.site_enabled.checked,
      application_enabled: e.target.application_enabled.checked,
      role_enabled: e.target.role_enabled.checked,
      user_enabled: e.target.user_enabled.checked,
    }
    try {
      if (editing) {
        await api.put(`/admin/profile-options/${editing.profile_option_id}`, payload)
      } else {
        await api.post('/admin/profile-options', payload)
      }
      closeModal()
      fetchOptions()
    } catch (err) {
      setFormError(err.response?.data?.detail?.message || JSON.stringify(err.response?.data?.detail) || 'Save failed')
    } finally {
      setSaving(false)
    }
  }

  const handleDelete = async (opt) => {
    if (!window.confirm(`Delete profile option "${opt.profile_option_name}"?`)) return
    try {
      await api.delete(`/admin/profile-options/${opt.profile_option_id}`)
      fetchOptions()
      if (selected?.profile_option_id === opt.profile_option_id) setSelected(null)
    } catch {}
  }

  const selectOption = useCallback(async (opt) => {
    setSelected(opt)
    setDetailLoading(true)
    setDrafts({})
    try {
      const [vals, eff] = await Promise.all([
        api.get(`/admin/profile-options/${opt.profile_option_id}/values`),
        api.get('/admin/profile-values/effective', { params: { profile_option_name: opt.profile_option_name } }),
      ])
      const list = vals.data || []
      setValues(list)
      setEffective(eff.data)
      const d = {}
      list.forEach((v) => { d[v.level] = v.profile_option_value })
      setDrafts(d)
    } catch {
      setValues([])
      setEffective(null)
    } finally {
      setDetailLoading(false)
    }
  }, [])

  const saveLevel = async (level) => {
    if (!selected) return
    const value = drafts[level] ?? ''
    if (value === '') {
      // clear if present
      const existing = values.find((v) => v.level === level)
      if (existing) {
        await api.delete(`/admin/profile-options/${selected.profile_option_id}/values`, {
          params: { level, level_key: existing.level_key || undefined },
        })
      }
    } else {
      await api.put(`/admin/profile-options/${selected.profile_option_id}/values`, {
        level,
        level_key: level === 'site' ? null : draftKey(level),
        profile_option_value: value,
      })
    }
    selectOption(selected)
  }

  // level_key is required for application/role/user; for the demo UI we let the
  // admin type a key (module string / role_id / user_id).
  const [keyInputs, setKeyInputs] = useState({})
  const draftKey = (level) => keyInputs[level] || (values.find((v) => v.level === level)?.level_key ?? '')

  const columns = [
    { key: 'profile_option_name', header: 'Name', width: '240px', render: (r) => r.profile_option_name },
    {
      key: 'user_profile_option_name', header: 'Display Name', width: '240px',
      render: (r) => r.user_profile_option_name,
    },
    {
      key: 'value_type', header: 'Type', width: '100px',
      render: (r) => <span className="text-[10px] font-semibold uppercase tracking-wider text-outline">{r.value_type}</span>,
    },
    {
      key: 'levels', header: 'Enabled Levels', width: '220px',
      render: (r) => (
        <div className="flex flex-wrap gap-1">
          {r.site_enabled && <span className="px-1.5 py-0.5 bg-primary/10 text-primary rounded text-[10px]">Site</span>}
          {r.application_enabled && <span className="px-1.5 py-0.5 bg-primary/10 text-primary rounded text-[10px]">App</span>}
          {r.role_enabled && <span className="px-1.5 py-0.5 bg-primary/10 text-primary rounded text-[10px]">Role</span>}
          {r.user_enabled && <span className="px-1.5 py-0.5 bg-primary/10 text-primary rounded text-[10px]">User</span>}
        </div>
      ),
    },
    {
      key: 'is_system', header: 'System', width: '90px',
      render: (r) => r.is_system
        ? <span className="text-[10px] font-semibold text-warning">System</span>
        : <span className="text-[10px] text-outline">—</span>,
    },
  ]

  return (
    <div className="space-y-6">
      <PersonalizeWrapper componentId="header:user-profiles">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-slate-900! dark:text-white!">User Profiles</h1>
            <p className="text-sm text-slate-500! dark:text-slate-300! mt-1">
              EBS-style profile options — set values across Site, Application, Role and User levels (most specific wins)
            </p>
          </div>
          <button onClick={openCreate}
            className="flex items-center gap-1.5 px-4 py-2 bg-primary text-primary-foreground rounded-xl text-xs font-bold hover:opacity-90 transition-all shadow-lg shadow-primary/20">
            <Plus size={15} /> New Profile Option
          </button>
        </div>
      </PersonalizeWrapper>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Options list */}
        <PersonalizeWrapper componentId="grid:user-profiles">
          <div className="lg:col-span-2 border border-outline-variant rounded-xl overflow-hidden bg-surface-container-lowest">
            <div className="p-3 border-b border-outline-variant">
              <input
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                placeholder="Search profile options…"
                className="w-full px-3 py-2 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none"
              />
            </div>
            <div className="overflow-y-auto max-h-[60vh]">
              <table className="w-full text-sm">
                <thead className="bg-surface-container-low sticky top-0">
                  <tr className="text-left text-outline">
                    <th className="px-3 py-2 font-semibold">Name</th>
                    <th className="px-3 py-2 font-semibold">Type</th>
                    <th className="px-3 py-2 font-semibold">Levels</th>
                  </tr>
                </thead>
                <tbody>
                  {loading && (
                    <tr><td colSpan={3} className="px-3 py-6 text-center text-outline">Loading…</td></tr>
                  )}
                  {!loading && options.length === 0 && (
                    <tr><td colSpan={3} className="px-3 py-6 text-center text-outline">No profile options found</td></tr>
                  )}
                  {options.map((opt) => (
                    <tr
                      key={opt.profile_option_id}
                      onClick={() => selectOption(opt)}
                      className={`border-t border-outline-variant/40 cursor-pointer transition-colors ${
                        selected?.profile_option_id === opt.profile_option_id ? 'bg-primary/10' : 'hover:bg-surface-container-low'
                      }`}
                    >
                      <td className="px-3 py-2">
                        <div className="font-medium text-on-surface">{opt.profile_option_name}</div>
                        <div className="text-[11px] text-outline">{opt.user_profile_option_name}</div>
                      </td>
                      <td className="px-3 py-2"><span className="text-[10px] font-semibold uppercase text-outline">{opt.value_type}</span></td>
                      <td className="px-3 py-2">
                        <div className="flex flex-wrap gap-1">
                          {opt.site_enabled && <span className="px-1 py-0.5 bg-surface-container-highest rounded text-[9px]">Site</span>}
                          {opt.application_enabled && <span className="px-1 py-0.5 bg-surface-container-highest rounded text-[9px]">App</span>}
                          {opt.role_enabled && <span className="px-1 py-0.5 bg-surface-container-highest rounded text-[9px]">Role</span>}
                          {opt.user_enabled && <span className="px-1 py-0.5 bg-surface-container-highest rounded text-[9px]">User</span>}
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </PersonalizeWrapper>

        {/* Detail / values editor */}
        <PersonalizeWrapper componentId="panel:user-profiles-detail">
          <div className="border border-outline-variant rounded-xl overflow-hidden bg-surface-container-lowest">
            {!selected && (
              <div className="p-6 text-center text-outline text-sm">Select a profile option to view and edit its values.</div>
            )}
            {selected && (
              <div className="p-4 space-y-4">
                <div>
                  <div className="text-xs font-semibold uppercase tracking-wider text-outline">Profile Option</div>
                  <div className="text-sm font-bold text-on-surface">{selected.profile_option_name}</div>
                  {selected.description && (
                    <div className="text-[11px] text-outline mt-1">{selected.description}</div>
                  )}
                </div>

                {effective && (
                  <div className="p-3 rounded-lg bg-primary/10 border border-primary/20">
                    <div className="text-[10px] font-semibold uppercase tracking-wider text-primary">Effective Value</div>
                    <div className="text-sm font-bold text-on-surface mt-0.5">
                      {effective.effective_value ?? <span className="text-outline font-normal">— not set —</span>}
                    </div>
                    <div className="text-[10px] text-outline mt-0.5">
                      resolved at <span className="font-semibold">{effective.resolved_level || 'none'}</span>
                      {effective.level_key ? ` (${effective.level_key})` : ''}
                    </div>
                  </div>
                )}

                <div className="space-y-3">
                  {LEVELS.map((lvl) => {
                    const enabled = {
                      site: selected.site_enabled,
                      application: selected.application_enabled,
                      role: selected.role_enabled,
                      user: selected.user_enabled,
                    }[lvl.code]
                    if (!enabled) return null
                    const v = drafts[lvl.code] ?? ''
                    return (
                      <div key={lvl.code} className="border border-outline-variant rounded-lg p-2.5">
                        <div className="flex items-center justify-between mb-1.5">
                          <span className="text-[11px] font-bold uppercase tracking-wider text-on-surface-variant">{lvl.label}</span>
                          <button
                            onClick={() => saveLevel(lvl.code)}
                            className="text-[10px] px-2 py-1 bg-primary text-primary-foreground rounded-md font-semibold hover:opacity-90"
                          >
                            Save
                          </button>
                        </div>
                        {(lvl.code === 'application' || lvl.code === 'role' || lvl.code === 'user') && (
                          <input
                            value={keyInputs[lvl.code] ?? (values.find((x) => x.level === lvl.code)?.level_key ?? '')}
                            onChange={(e) => setKeyInputs((p) => ({ ...p, [lvl.code]: e.target.value }))}
                            placeholder={lvl.code === 'application' ? 'module (e.g. mdm)' : `${lvl.code}_id`}
                            className="w-full mb-1.5 px-2 py-1.5 text-xs bg-surface-bright border border-outline-variant rounded-lg text-on-surface outline-none focus:border-primary"
                          />
                        )}
                        {selected.value_type === 'checkbox' ? (
                          <select
                            value={v || 'N'}
                            onChange={(e) => { setDrafts((p) => ({ ...p, [lvl.code]: e.target.value })); saveLevel(lvl.code) }}
                            className="w-full px-2 py-1.5 text-xs bg-surface-bright border border-outline-variant rounded-lg text-on-surface outline-none focus:border-primary"
                          >
                            <option value="Y">Yes</option>
                            <option value="N">No</option>
                          </select>
                        ) : (
                          <input
                            value={v}
                            onChange={(e) => setDrafts((p) => ({ ...p, [lvl.code]: e.target.value }))}
                            type={selected.value_type === 'date' ? 'date' : selected.value_type === 'number' ? 'number' : 'text'}
                            placeholder={selected.value_type === 'url' ? 'https://…' : 'value'}
                            className="w-full px-2 py-1.5 text-xs bg-surface-bright border border-outline-variant rounded-lg text-on-surface outline-none focus:border-primary"
                          />
                        )}
                      </div>
                    )
                  })}
                </div>

                <div className="flex gap-2 pt-2 border-t border-outline-variant">
                  <button onClick={() => openEdit(selected)}
                    className="flex-1 px-3 py-1.5 text-xs font-semibold bg-surface-container-highest text-on-surface rounded-lg hover:bg-surface-variant">
                    Edit Option
                  </button>
                  {!selected.is_system && (
                    <button onClick={() => handleDelete(selected)}
                      className="px-3 py-1.5 text-xs font-semibold bg-error-container text-error rounded-lg hover:opacity-90">
                      Delete
                    </button>
                  )}
                </div>
              </div>
            )}
            {detailLoading && (
              <div className="p-6 text-center text-outline text-sm">Loading values…</div>
            )}
          </div>
        </PersonalizeWrapper>
      </div>

      {modalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm p-4">
          <div className="bg-surface-container rounded-2xl border border-outline-variant shadow-2xl w-full max-w-lg max-h-[90vh] overflow-hidden flex flex-col">
            <div className="flex items-center justify-between p-5 border-b border-outline-variant">
              <h2 className="text-lg font-bold text-slate-900! dark:text-white!">
                {editing ? 'Edit Profile Option' : 'New Profile Option'}
              </h2>
              <button onClick={closeModal} className="p-1.5 rounded-lg hover:bg-surface-container-high text-outline">
                <span className="material-symbols-outlined text-[18px]">close</span>
              </button>
            </div>
            <form onSubmit={handleSave} className="p-5 space-y-3 overflow-y-auto">
              {formError && <div className="bg-error-container text-error p-3 rounded-xl text-sm font-medium">{formError}</div>}
              <div>
                <label className="block text-[11px] font-semibold uppercase tracking-wider text-outline mb-1">Internal Name *</label>
                <input name="profile_option_name" defaultValue={editing?.profile_option_name || ''} required
                  className="w-full px-3 py-2 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface outline-none focus:border-primary" />
              </div>
              <div>
                <label className="block text-[11px] font-semibold uppercase tracking-wider text-outline mb-1">Display Name *</label>
                <input name="user_profile_option_name" defaultValue={editing?.user_profile_option_name || ''} required
                  className="w-full px-3 py-2 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface outline-none focus:border-primary" />
              </div>
              <div>
                <label className="block text-[11px] font-semibold uppercase tracking-wider text-outline mb-1">Description</label>
                <textarea name="description" defaultValue={editing?.description || ''} rows={2}
                  className="w-full px-3 py-2 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface outline-none focus:border-primary resize-none" />
              </div>
              <div>
                <label className="block text-[11px] font-semibold uppercase tracking-wider text-outline mb-1">Value Type</label>
                <select name="value_type" defaultValue={editing?.value_type || 'text'}
                  className="w-full px-3 py-2 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface outline-none focus:border-primary">
                  {VALUE_TYPES.map((t) => <option key={t} value={t}>{t}</option>)}
                </select>
              </div>
              <div className="grid grid-cols-2 gap-2 pt-1">
                {[
                  ['site_enabled', 'Site'],
                  ['application_enabled', 'Application'],
                  ['role_enabled', 'Role'],
                  ['user_enabled', 'User'],
                ].map(([name, label]) => (
                  <label key={name} className="flex items-center gap-2 text-sm text-on-surface">
                    <input type="checkbox" name={name} defaultChecked={editing?.[name] ?? (name === 'site_enabled')} className="accent-primary w-4 h-4" />
                    {label} level
                  </label>
                ))}
              </div>
              <div className="flex justify-end gap-3 pt-3">
                <button type="button" onClick={closeModal}
                  className="neo-button px-5 py-2.5 text-sm font-semibold text-on-surface-variant">Cancel</button>
                <button type="submit" disabled={saving}
                  className="flex items-center gap-2 px-5 py-2.5 bg-primary text-primary-foreground rounded-xl text-sm font-semibold hover:opacity-90 disabled:opacity-50">
                  {saving && <span className="animate-spin inline-block w-4 h-4 border-2 border-white/30 border-t-white rounded-full" />}
                  {editing ? 'Save Changes' : 'Create'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  )
}
