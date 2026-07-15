import { useMemo } from 'react'
import { useNavigate } from 'react-router-dom'
import useAuthStore from '../store/authStore'
import { FUNCTIONAL_AREAS, MODULE_REGISTRY } from '../config/moduleRegistry'

export default function DashboardHome() {
  const navigate = useNavigate()
  const privileges = useAuthStore((s) => s.privileges)

  const accessibleModules = useMemo(() => {
    if (!privileges || privileges.length === 0) return []
    return MODULE_REGISTRY.filter((mod) =>
      privileges.some((p) => p.module === mod.module && (p.action === mod.action || p.action === 'manage' || p.action === 'view'))
    )
  }, [privileges])

  const groupedAreas = useMemo(() => {
    const map = {}
    for (const area of FUNCTIONAL_AREAS) {
      const mods = accessibleModules.filter((m) => m.area === area.id)
      if (mods.length > 0) map[area.id] = { ...area, modules: mods }
    }
    return map
  }, [accessibleModules])

  return (
    <div className="p-6 space-y-8">
      <div>
        <h1 className="text-2xl font-bold text-on-surface">EraOwl-OPS</h1>
        <p className="text-sm text-outline mt-1">AI-powered ERP platform — select a module to get started</p>
      </div>

      {Object.keys(groupedAreas).length === 0 ? (
        <div className="flex flex-col items-center justify-center py-20 text-outline">
          <span className="material-symbols-outlined text-[64px] mb-4">dashboard_customize</span>
          <p className="text-lg font-semibold text-on-surface">Welcome to EraOwl-OPS</p>
          <p className="text-sm mt-1">Use the sidebar to navigate, or press <kbd className="px-1.5 py-0.5 text-xs font-mono bg-surface-container-high rounded border border-outline-variant">⌘K</kbd> for quick search.</p>
        </div>
      ) : (
        Object.entries(groupedAreas).map(([areaId, area]) => (
          <section key={areaId}>
            <div className="flex items-center gap-2 mb-3">
              <span className="material-symbols-outlined text-[20px]" style={{ color: area.color }}>{area.icon}</span>
              <h2 className="text-sm font-bold text-on-surface">{area.label}</h2>
              <span className="text-[10px] text-outline bg-surface-container-high px-1.5 py-0.5 rounded-full">{area.modules.length}</span>
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-3">
              {area.modules.map((mod) => (
                <button key={mod.id} onClick={() => navigate(mod.path)}
                  className="group flex flex-col items-center gap-2 p-4 bg-surface-container-lowest border border-outline-variant rounded-xl hover:border-primary/40 hover:bg-surface-container-low hover:shadow-sm transition-all cursor-pointer text-center">
                  <div className="w-10 h-10 rounded-xl flex items-center justify-center transition-colors" style={{ backgroundColor: `${area.color}15` }}>
                    <span className="material-symbols-outlined text-[22px]" style={{ color: area.color }}>{mod.icon}</span>
                  </div>
                  <span className="text-[11px] font-semibold text-on-surface leading-tight">{mod.label}</span>
                  <span className="text-[9px] text-outline leading-tight opacity-0 group-hover:opacity-100 transition-opacity">Open {mod.label}</span>
                </button>
              ))}
            </div>
          </section>
        ))
      )}

      <div className="border-t border-outline-variant/50 pt-6 pb-10">
        <p className="text-[10px] text-outline text-center">
          EraOwl-OPS v0.1.0 — {accessibleModules.length} modules available across {Object.keys(groupedAreas).length} functional areas
        </p>
      </div>
    </div>
  )
}
