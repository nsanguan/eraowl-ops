import { useState, useEffect, useCallback } from 'react'
import api from '../../../api/client'

const EVENT_COLORS = { meeting: 'oklch(0.55 0.14 290)', call: 'oklch(0.55 0.14 200)', email: 'oklch(0.55 0.14 260)', task: 'oklch(0.55 0.14 80)', reminder: 'oklch(0.55 0.14 150)' }

export default function CalendarPage() {
  const today = new Date()
  const [year, setYear] = useState(today.getFullYear())
  const [month, setMonth] = useState(today.getMonth())
  const [events, setEvents] = useState([])
  const [selectedDay, setSelectedDay] = useState(null)
  const [showForm, setShowForm] = useState(false)
  const [form, setForm] = useState({ title: '', event_type: 'meeting', event_date: '', all_day: false })

  const fetchEvents = useCallback(async () => {
    try { const { data } = await api.get('/collaboration/calendar-events', { params: { page: 1, page_size: 200 } }); setEvents(data?.items || []) } catch {}
  }, [])

  useEffect(() => { fetchEvents() }, [fetchEvents])

  const daysInMonth = new Date(year, month + 1, 0).getDate()
  const firstDay = new Date(year, month, 1).getDay()
  const monthEvents = events.filter((e) => { const d = new Date(e.event_date); return d.getFullYear() === year && d.getMonth() === month })
  const dayEvents = (day) => monthEvents.filter((e) => new Date(e.event_date).getDate() === day)

  const handlePrev = () => { if (month === 0) { setYear(y => y - 1); setMonth(11) } else setMonth(m => m - 1) }
  const handleNext = () => { if (month === 11) { setYear(y => y + 1); setMonth(0) } else setMonth(m => m + 1) }

  const handleSave = async () => {
    if (!form.title || !form.event_date) return
    try { await api.post('/collaboration/calendar-events', form); setShowForm(false); setForm({ title: '', event_type: 'meeting', event_date: '', all_day: false }); fetchEvents() } catch {}
  }

  const handleDelete = async (id) => {
    if (!confirm('Delete this event?')) return
    try { await api.delete(`/collaboration/calendar-events/${id}`); fetchEvents() } catch {}
  }

  const monthNames = ['January','February','March','April','May','June','July','August','September','October','November','December']
  const blanks = Array(firstDay).fill(null)
  const dayCells = Array.from({ length: daysInMonth }, (_, i) => i + 1)

  return (
    <div className="p-6 space-y-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-slate-900! dark:text-white!">Calendar</h1>
          <p className="text-sm text-slate-500! dark:text-slate-300! mt-1">{monthNames[month]} {year}</p>
        </div>
        <button onClick={() => setShowForm(true)} className="px-4 py-2 bg-primary text-primary-foreground rounded-xl text-sm font-semibold hover:opacity-90 flex items-center gap-2">
          <span className="material-symbols-outlined text-[18px]">add</span> Add Event
        </button>
      </div>

      <div className="flex items-center gap-2">
        <button onClick={handlePrev} className="px-3 py-1.5 bg-surface-container-lowest border border-outline-variant rounded-lg text-sm hover:bg-surface-container-low">&larr; Prev</button>
        <button onClick={() => { setYear(today.getFullYear()); setMonth(today.getMonth()) }} className="px-3 py-1.5 bg-surface-container-lowest border border-outline-variant rounded-lg text-sm hover:bg-surface-container-low">Today</button>
        <button onClick={handleNext} className="px-3 py-1.5 bg-surface-container-lowest border border-outline-variant rounded-lg text-sm hover:bg-surface-container-low">Next &rarr;</button>
      </div>

      <div className="border border-outline-variant rounded-xl overflow-hidden bg-surface-container-lowest">
        <div className="grid grid-cols-7 bg-surface-container-low border-b border-outline-variant">
          {['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].map((d) => <div key={d} className="px-2 py-2 text-[10px] font-semibold text-outline uppercase text-center">{d}</div>)}
        </div>
        <div className="grid grid-cols-7">
          {blanks.map((_, i) => <div key={`b-${i}`} className="min-h-[80px] border-b border-r border-outline-variant/30 bg-surface-container-low/20" />)}
          {dayCells.map((day) => {
            const de = dayEvents(day)
            const isToday = day === today.getDate() && month === today.getMonth() && year === today.getFullYear()
            return (
              <div key={day} onClick={() => setSelectedDay(selectedDay === day ? null : day)}
                className={`min-h-[80px] border-b border-r border-outline-variant/30 p-1 cursor-pointer transition-colors ${isToday ? 'bg-primary/5' : 'hover:bg-surface-container-low'} ${selectedDay === day ? 'ring-2 ring-inset ring-primary' : ''}`}>
                <div className={`text-[11px] font-semibold mb-1 ${isToday ? 'text-primary' : 'text-on-surface'}`}>{day}</div>
                <div className="space-y-0.5">
                  {de.slice(0, 3).map((e) => (
                    <div key={e.event_id} className="text-[9px] px-1 py-0.5 rounded truncate text-white font-medium" style={{ backgroundColor: EVENT_COLORS[e.event_type] || EVENT_COLORS.meeting }}>
                      {e.title}
                    </div>
                  ))}
                  {de.length > 3 && <div className="text-[9px] text-outline px-1">+{de.length - 3} more</div>}
                </div>
              </div>
            )
          })}
        </div>
      </div>

      {selectedDay && (
        <div className="border border-outline-variant rounded-xl bg-surface-container-lowest p-4">
          <h3 className="text-sm font-bold text-on-surface mb-3">{monthNames[month]} {selectedDay}, {year} — Events</h3>
          {dayEvents(selectedDay).length === 0 ? <p className="text-sm text-outline">No events for this day.</p> : (
            <div className="space-y-2">
              {dayEvents(selectedDay).map((e) => (
                <div key={e.event_id} className="flex items-center justify-between px-3 py-2 bg-surface-container-low rounded-lg">
                  <div className="flex items-center gap-3">
                    <span className="material-symbols-outlined text-[18px]" style={{ color: EVENT_COLORS[e.event_type] }}>
                      {e.event_type === 'meeting' ? 'groups' : e.event_type === 'call' ? 'call' : e.event_type === 'email' ? 'mail' : e.event_type === 'task' ? 'task' : 'notifications'}
                    </span>
                    <div>
                      <div className="text-sm font-medium text-on-surface">{e.title}</div>
                      <div className="text-[10px] text-outline capitalize">{e.event_type}{e.all_day ? ' · All day' : ''}</div>
                    </div>
                  </div>
                  <button onClick={() => handleDelete(e.event_id)} className="text-outline hover:text-error"><span className="material-symbols-outlined text-[16px]">delete</span></button>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {showForm && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40" onClick={() => setShowForm(false)}>
          <div className="bg-surface-container rounded-2xl border border-outline-variant shadow-2xl w-full max-w-md p-5" onClick={(e) => e.stopPropagation()}>
            <h2 className="text-lg font-bold text-slate-900! dark:text-white! mb-4">Add Event</h2>
            <div className="space-y-3">
              <input type="text" value={form.title} onChange={(e) => setForm({...form, title: e.target.value})} placeholder="Event title" className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none" />
              <select value={form.event_type} onChange={(e) => setForm({...form, event_type: e.target.value})} className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface outline-none">
                <option value="meeting">Meeting</option><option value="call">Call</option><option value="email">Email</option><option value="task">Task</option><option value="reminder">Reminder</option>
              </select>
              <input type="date" value={form.event_date} onChange={(e) => setForm({...form, event_date: e.target.value})} className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none" />
              <label className="flex items-center gap-2 text-sm text-on-surface"><input type="checkbox" checked={form.all_day} onChange={(e) => setForm({...form, all_day: e.target.checked})} className="accent-primary" /> All day</label>
            </div>
            <div className="flex justify-end gap-3 mt-5">
              <button onClick={() => setShowForm(false)} className="px-4 py-2 text-sm font-semibold text-on-surface-variant bg-surface-container-low border border-outline-variant rounded-xl">Cancel</button>
              <button onClick={handleSave} className="px-4 py-2 text-sm font-semibold text-white bg-primary rounded-xl hover:opacity-90">Save</button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
