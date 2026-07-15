import { useState, useEffect, useCallback } from 'react'
import api from '../../../api/client'

const TYPE_ICONS = { call: 'call', meeting: 'groups', email: 'mail', task: 'task', follow_up: 'redo' }

export default function ActivitiesPage() {
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(true)
  const [showForm, setShowForm] = useState(false)
  const [form, setForm] = useState({ activity_type: 'task', subject: '', description: '', due_date: '' })

  const fetchActivities = useCallback(async () => {
    setLoading(true)
    try { const { data } = await api.get('/collaboration/activities', { params: { page: 1, page_size: 100 } }); setItems(data?.items || []) } catch {} finally { setLoading(false) }
  }, [])

  useEffect(() => { fetchActivities() }, [fetchActivities])

  const handleCreate = async () => {
    if (!form.subject) return
    try { await api.post('/collaboration/activities', form); setShowForm(false); setForm({ activity_type: 'task', subject: '', description: '', due_date: '' }); fetchActivities() } catch {}
  }

  const handleMarkDone = async (id) => {
    try { await api.put(`/collaboration/activities/${id}`, { status: 'done' }); fetchActivities() } catch {}
  }

  const handleDelete = async (id) => {
    if (!confirm('Delete this activity?')) return
    try { await api.delete(`/collaboration/activities/${id}`); fetchActivities() } catch {}
  }

  const statusColor = (s) => s === 'open' ? 'bg-success/10 text-success' : s === 'overdue' ? 'bg-error/10 text-error' : 'bg-outline-variant/30 text-outline'

  return (
    <div className="p-6 space-y-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-on-surface">Activities</h1>
          <p className="text-sm text-outline mt-1">Track and manage activities across the system</p>
        </div>
        <button onClick={() => setShowForm(true)} className="px-4 py-2 bg-primary text-primary-foreground rounded-xl text-sm font-semibold hover:opacity-90 flex items-center gap-2">
          <span className="material-symbols-outlined text-[18px]">add</span> Schedule Activity
        </button>
      </div>

      <div className="space-y-2">
        {items.map((item) => (
          <div key={item.activity_id} className="flex items-center gap-4 px-4 py-3 bg-surface-container-lowest border border-outline-variant rounded-xl hover:bg-surface-container-low transition-colors group">
            <span className="material-symbols-outlined text-[20px] text-primary">{TYPE_ICONS[item.activity_type] || 'event_note'}</span>
            <div className="flex-1 min-w-0">
              <div className="text-sm font-medium text-on-surface truncate">{item.subject}</div>
              <div className="flex items-center gap-2 mt-0.5">
                <span className="text-[10px] text-outline capitalize">{item.activity_type}</span>
                {item.due_date && <span className="text-[10px] text-outline">· Due: {item.due_date}</span>}
              </div>
            </div>
            <span className={`px-2 py-0.5 text-[10px] font-semibold rounded-full ${statusColor(item.status)}`}>{item.status}</span>
            {item.status !== 'done' && (
              <button onClick={() => handleMarkDone(item.activity_id)} className="text-outline hover:text-success opacity-0 group-hover:opacity-100 transition-opacity" title="Mark done">
                <span className="material-symbols-outlined text-[18px]">check_circle</span>
              </button>
            )}
            <button onClick={() => handleDelete(item.activity_id)} className="text-outline hover:text-error opacity-0 group-hover:opacity-100 transition-opacity">
              <span className="material-symbols-outlined text-[18px]">delete</span>
            </button>
          </div>
        ))}
        {!loading && items.length === 0 && <p className="text-sm text-outline text-center py-8">No activities yet.</p>}
      </div>

      {showForm && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40" onClick={() => setShowForm(false)}>
          <div className="bg-surface-container rounded-2xl border border-outline-variant shadow-2xl w-full max-w-md p-5" onClick={(e) => e.stopPropagation()}>
            <h2 className="text-lg font-bold text-on-surface mb-4">Schedule Activity</h2>
            <div className="space-y-3">
              <select value={form.activity_type} onChange={(e) => setForm({...form, activity_type: e.target.value})} className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface outline-none">
                <option value="task">Task</option><option value="meeting">Meeting</option><option value="call">Call</option><option value="email">Email</option><option value="follow_up">Follow Up</option>
              </select>
              <input type="text" value={form.subject} onChange={(e) => setForm({...form, subject: e.target.value})} placeholder="Subject" className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none" />
              <textarea value={form.description} onChange={(e) => setForm({...form, description: e.target.value})} placeholder="Description (optional)" rows={3} className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none resize-none" />
              <input type="date" value={form.due_date} onChange={(e) => setForm({...form, due_date: e.target.value})} className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none" />
            </div>
            <div className="flex justify-end gap-3 mt-5">
              <button onClick={() => setShowForm(false)} className="px-4 py-2 text-sm font-semibold text-on-surface-variant bg-surface-container-low border border-outline-variant rounded-xl">Cancel</button>
              <button onClick={handleCreate} className="px-4 py-2 text-sm font-semibold text-white bg-primary rounded-xl hover:opacity-90">Schedule</button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
