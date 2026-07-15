import { useState, useEffect, useCallback } from 'react'
import api from '../../../api/client'

export default function TodoPage() {
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(true)
  const [title, setTitle] = useState('')
  const [priority, setPriority] = useState('medium')
  const [editingId, setEditingId] = useState(null)
  const [editTitle, setEditTitle] = useState('')

  const fetchTodos = useCallback(async () => {
    setLoading(true)
    try { const { data } = await api.get('/collaboration/todos', { params: { page: 1, page_size: 100 } }); setItems(data?.items || [])
    } catch {} finally { setLoading(false) }
  }, [])

  useEffect(() => { fetchTodos() }, [fetchTodos])

  const handleAdd = async () => {
    if (!title.trim()) return
    await api.post('/collaboration/todos', { title, priority })
    setTitle(''); setPriority('medium'); fetchTodos()
  }

  const handleToggle = async (item) => {
    await api.put(`/collaboration/todos/${item.todo_id}`, { is_complete: !item.is_complete })
    fetchTodos()
  }

  const handleDelete = async (id) => {
    if (!confirm('Delete this task?')) return
    await api.delete(`/collaboration/todos/${id}`)
    fetchTodos()
  }

  const handleEditSave = async (id) => {
    if (!editTitle.trim()) return
    await api.put(`/collaboration/todos/${id}`, { title: editTitle })
    setEditingId(null); fetchTodos()
  }

  const priorityColor = (p) => p === 'high' ? 'oklch(0.6 0.22 30)' : p === 'medium' ? 'oklch(0.7 0.16 80)' : 'oklch(0.55 0.14 260)'

  return (
    <div className="p-6 max-w-2xl space-y-4">
      <div>
        <h1 className="text-2xl font-bold text-on-surface">To-Do</h1>
        <p className="text-sm text-outline mt-1">Personal task management</p>
      </div>

      <div className="flex gap-2">
        <input type="text" value={title} onChange={(e) => setTitle(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleAdd()}
          placeholder="Add a new task..." className="flex-1 px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none" />
        <select value={priority} onChange={(e) => setPriority(e.target.value)}
          className="px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface outline-none">
          <option value="high">High</option><option value="medium">Medium</option><option value="low">Low</option>
        </select>
        <button onClick={handleAdd} className="px-4 py-2.5 bg-primary text-primary-foreground rounded-xl text-sm font-semibold hover:opacity-90">Add</button>
      </div>

      <div className="space-y-1">
        {items.map((item) => (
          <div key={item.todo_id}
            className="flex items-center gap-3 px-4 py-3 bg-surface-container-lowest border border-outline-variant rounded-xl hover:bg-surface-container-low transition-colors group"
            style={{ borderLeft: `3px solid ${priorityColor(item.priority)}` }}>
            <input type="checkbox" checked={item.is_complete} onChange={() => handleToggle(item)}
              className="accent-primary w-4 h-4 cursor-pointer shrink-0" />
            {editingId === item.todo_id ? (
              <div className="flex-1 flex gap-2">
                <input type="text" value={editTitle} onChange={(e) => setEditTitle(e.target.value)}
                  className="flex-1 px-2 py-1 bg-surface-bright border border-outline-variant rounded text-sm outline-none" autoFocus />
                <button onClick={() => handleEditSave(item.todo_id)} className="text-xs text-primary font-semibold">Save</button>
                <button onClick={() => setEditingId(null)} className="text-xs text-outline">Cancel</button>
              </div>
            ) : (
              <span className={`flex-1 text-sm ${item.is_complete ? 'line-through text-outline' : 'text-on-surface'}`}
                onDoubleClick={() => { setEditingId(item.todo_id); setEditTitle(item.title) }}>
                {item.title}
              </span>
            )}
            <span className="text-[10px] font-semibold uppercase px-1.5 py-0.5 rounded" style={{ color: priorityColor(item.priority), background: `${priorityColor(item.priority)}15` }}>{item.priority}</span>
            {item.due_date && <span className="text-[10px] text-outline">{item.due_date}</span>}
            <button onClick={() => handleDelete(item.todo_id)} className="text-outline hover:text-error opacity-0 group-hover:opacity-100 transition-opacity">
              <span className="material-symbols-outlined text-[16px]">delete</span>
            </button>
          </div>
        ))}
        {!loading && items.length === 0 && <p className="text-sm text-outline text-center py-8">No tasks yet. Add one above!</p>}
      </div>
    </div>
  )
}
