import { useMemo, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import useAuthStore from '../../../store/authStore'
import { FUNCTIONAL_AREAS, MODULE_REGISTRY } from '../../../config/moduleRegistry'
import PersonalizeWrapper from '../../../shared-ui-kit/components/ui/PersonalizeWrapper'
import usePersonalizeStore from '../../../store/usePersonalizeStore'

export default function AdminHome() {
  const navigate = useNavigate()
  const privileges = useAuthStore((s) => s.privileges)
  const user = useAuthStore((s) => s.user)
  const loadPersonalization = usePersonalizeStore((s) => s.loadPersonalization)
  useEffect(() => { loadPersonalization('admin.home') }, [loadPersonalization])

  const area = FUNCTIONAL_AREAS.find((a) => a.id === 'admin')

  const modules = useMemo(() => {
    const all = MODULE_REGISTRY.filter((m) => m.area === 'admin')
    if (!privileges || privileges.length === 0) return all
    return all.filter((m) =>
      privileges.some((p) => p.module === m.module && (p.action === m.action || p.action === 'manage' || p.action === 'view'))
    )
  }, [privileges])

  return (
    <div className="p-6 space-y-8">
      <PersonalizeWrapper componentId="header:admin-home">
        <div className="flex items-center gap-3">
          <div className="w-11 h-11 rounded-2xl flex items-center justify-center" style={{ backgroundColor: `${area?.color}15` }}>
            <span className="material-symbols-outlined text-[26px]" style={{ color: area?.color }}>{area?.icon}</span>
          </div>
          <div>
            <h1 className="text-2xl font-bold text-slate-950 dark:text-slate-50">Administration</h1>
            <p className="text-sm text-slate-600 dark:text-slate-300 mt-1">
              {area?.description} — manage users, roles, profile options & system configuration
            </p>
          </div>
        </div>
        {user && (
          <p className="text-[11px] text-slate-600 dark:text-slate-300 mt-3">
            Signed in as <span className="font-semibold text-slate-950 dark:text-slate-50">{user.username}</span>
            {user.email ? ` (${user.email})` : ''}
          </p>
        )}
      </PersonalizeWrapper>

      <section>
        <div className="flex items-center gap-2 mb-3">
          <span className="material-symbols-outlined text-[20px]" style={{ color: area?.color }}>apps</span>
          <h2 className="text-sm font-bold text-slate-950 dark:text-slate-50">Admin Modules</h2>
          <span className="text-[10px] text-slate-600 dark:text-slate-300 bg-surface-container-high px-1.5 py-0.5 rounded-full">{modules.length}</span>
        </div>

        {modules.length === 0 ? (
          <div className="flex flex-col items-center justify-center py-16 border border-outline-variant rounded-2xl bg-surface-container-lowest">
            <span className="material-symbols-outlined text-[48px] mb-3 text-slate-400 dark:text-slate-500">lock</span>
            <p className="text-sm font-semibold text-slate-950 dark:text-slate-50">No admin modules available</p>
            <p className="text-[11px] mt-1 text-slate-600 dark:text-slate-300">You don't have permission to access any administration features.</p>
          </div>
        ) : (
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-3">
            {modules.map((mod) => (
              <button key={mod.id} onClick={() => navigate(mod.path)}
                className="group flex flex-col items-center gap-2 p-4 bg-surface-container-lowest border border-outline-variant rounded-xl hover:border-primary/40 hover:bg-surface-container-low hover:shadow-sm transition-all cursor-pointer text-center">
                <div className="w-10 h-10 rounded-xl flex items-center justify-center transition-colors" style={{ backgroundColor: `${area?.color}15` }}>
                  <span className="material-symbols-outlined text-[22px]" style={{ color: area?.color }}>{mod.icon}</span>
                </div>
                <span className="text-[11px] font-semibold text-slate-950 dark:text-slate-50 leading-tight">{mod.label}</span>
                <span className="text-[9px] text-slate-600 dark:text-slate-300 leading-tight opacity-0 group-hover:opacity-100 transition-opacity">Open {mod.label}</span>
              </button>
            ))}
          </div>
        )}
      </section>

      <div className="border-t border-outline-variant/50 pt-6 pb-10">
        <p className="text-[10px] text-slate-600 dark:text-slate-300 text-center">
          Administration · {modules.length} module{modules.length === 1 ? '' : 's'} available
        </p>
      </div>
    </div>
  )
}
