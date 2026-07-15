import { useState, useEffect, useCallback } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../../../api/client'
import { StatCard } from '../../../shared-ui-kit/components/ui/StatCard'

const QUICK_LINKS = [
  { path: '/collaboration/discuss',  label: 'Discuss',   icon: 'forum',        color: 'oklch(0.55 0.14 260)' },
  { path: '/collaboration/chat',     label: 'Chat',      icon: 'chat',         color: 'oklch(0.55 0.14 150)' },
  { path: '/collaboration/calendar', label: 'Calendar',  icon: 'calendar_month', color: 'oklch(0.55 0.14 80)' },
  { path: '/collaboration/todo',     label: 'Tasks',     icon: 'checklist',    color: 'oklch(0.55 0.14 290)' },
  { path: '/collaboration/activities', label: 'Activities', icon: 'event_note', color: 'oklch(0.55 0.14 30)' },
]

export default function CollaborationDashboard() {
  const navigate = useNavigate()
  const [counts, setCounts] = useState({ todos: 0, activities: 0, events: 0 })
  const [loading, setLoading] = useState(true)

  const fetchCounts = useCallback(async () => {
    setLoading(true)
    try {
      const [todos, activities, events] = await Promise.all([
        api.get('/collaboration/todos', { params: { page: 1, page_size: 1 } }),
        api.get('/collaboration/activities', { params: { page: 1, page_size: 1 } }),
        api.get('/collaboration/calendar-events', { params: { page: 1, page_size: 1 } }),
      ])
      setCounts({
        todos: todos.data?.total || 0,
        activities: activities.data?.total || 0,
        events: events.data?.total || 0,
      })
    } catch { } finally { setLoading(false) }
  }, [])

  useEffect(() => { fetchCounts() }, [fetchCounts])

  return (
    <div className="space-y-6 p-6">
      <div>
        <h1 className="text-2xl font-bold text-slate-900! dark:text-white!">Collaboration</h1>
        <p className="text-sm text-slate-500! dark:text-slate-300! mt-1">Team communication and productivity tools</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <StatCard title="To-Do Items" value={counts.todos} loading={loading} icon="checklist" color="oklch(0.55 0.14 260)" />
        <StatCard title="Activities" value={counts.activities} loading={loading} icon="event_note" color="oklch(0.55 0.14 150)" />
        <StatCard title="Calendar Events" value={counts.events} loading={loading} icon="calendar_month" color="oklch(0.55 0.14 80)" />
      </div>

      <div>
        <h2 className="text-sm font-bold text-slate-900! dark:text-white! mb-3">Quick Access</h2>
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3">
          {QUICK_LINKS.map((link) => (
            <button key={link.path} onClick={() => navigate(link.path)}
              className="flex flex-col items-center gap-2 p-4 bg-surface-container-lowest border border-outline-variant rounded-xl hover:bg-surface-container-low hover:border-primary/30 transition-all cursor-pointer">
              <span className="material-symbols-outlined text-[32px]" style={{ color: link.color }}>{link.icon}</span>
              <span className="text-xs font-semibold text-on-surface">{link.label}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  )
}
