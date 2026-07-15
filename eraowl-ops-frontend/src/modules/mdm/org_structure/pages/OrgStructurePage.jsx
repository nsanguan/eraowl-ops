import { useState, useEffect, useCallback, useRef, useMemo } from 'react'
import api from '../../../../api/client'
import { Plus } from 'lucide-react'
import { InteractiveGrid } from '../../../../shared-ui-kit/components/ui/InteractiveGrid'
import { TreeGrid } from '../../../../shared-ui-kit/components/ui/TreeGrid'

const TABS = [
  { key: 'corporates',    label: 'Corporates',    endpoint: '/org_structure/corporates',    idKey: 'corporate_id',      nameField: 'corp_name'  },
  { key: 'companies',     label: 'Companies',     endpoint: '/org_structure/companies',     idKey: 'company_id',        nameField: 'legal_name' },
  { key: 'businessUnits', label: 'Business Units', endpoint: '/org_structure/business-units', idKey: 'business_unit_id', nameField: 'bu_name'    },
  { key: 'sites',         label: 'Sites',          endpoint: '/org_structure/sites',         idKey: 'site_id',           nameField: 'site_name'  },
  { key: 'warehouses',    label: 'Warehouses',     endpoint: '/org_structure/warehouses',    idKey: 'warehouse_id',      nameField: 'warehouse_name' },
  { key: 'locators',      label: 'Locators',       endpoint: '/org_structure/locators',      idKey: 'locator_id',        nameField: 'locator_code' },
]

const LOOKUPS = {
  corporate_id:   { endpoint: '/org_structure/corporates',  valueKey: 'corporate_id',   labelKey: 'corp_code'  },
  company_id:     { endpoint: '/org_structure/companies',   valueKey: 'company_id',     labelKey: 'company_code'  },
  business_unit_id: { endpoint: '/org_structure/business-units', valueKey: 'business_unit_id', labelKey: 'bu_code' },
  site_id:        { endpoint: '/org_structure/sites',       valueKey: 'site_id',        labelKey: 'site_code'  },
  warehouse_id:   { endpoint: '/org_structure/warehouses',  valueKey: 'warehouse_id',   labelKey: 'warehouse_code' },
  address_id:     { endpoint: '/party/addresses',           valueKey: 'address_id',     labelKey: 'address_line1' },
}

const FIELDS = {
  corporates: [
    { key: 'corp_code', label: 'Code', required: true },
    { key: 'corp_name', label: 'Name', required: true },
  ],
  companies: [
    { key: 'company_code', label: 'Code', required: true },
    { key: 'legal_name',   label: 'Legal Name', required: true },
    { key: 'tax_id',       label: 'Tax ID' },
    { key: 'corporate_id', label: 'Corporate', lookup: 'corporate_id' },
  ],
  businessUnits: [
    { key: 'bu_code', label: 'Code', required: true },
    { key: 'bu_name', label: 'Name', required: true },
    { key: 'company_id', label: 'Company', lookup: 'company_id' },
  ],
  sites: [
    { key: 'site_code', label: 'Code', required: true },
    { key: 'site_name', label: 'Name', required: true },
    { key: 'business_unit_id', label: 'Business Unit', lookup: 'business_unit_id' },
    { key: 'address_id', label: 'Address', lookup: 'address_id' },
  ],
  warehouses: [
    { key: 'warehouse_code', label: 'Code', required: true },
    { key: 'warehouse_name', label: 'Name', required: true },
    { key: 'site_id', label: 'Site', lookup: 'site_id' },
  ],
  locators: [
    { key: 'locator_code', label: 'Code', required: true },
    { key: 'warehouse_id', label: 'Warehouse', lookup: 'warehouse_id' },
    { key: 'zone', label: 'Zone' },
    { key: 'aisle', label: 'Aisle' },
    { key: 'rack', label: 'Rack' },
    { key: 'bin', label: 'Bin' },
  ],
}

function OrgTreeView({ data }) {
  const corporates = data.corporates || []
  const companies = data.companies || []
  const businessUnits = data.businessUnits || []
  const sites = data.sites || []
  const warehouses = data.warehouses || []
  const locators = data.locators || []

  const treeNodes = useMemo(() => {
    return corporates.map((corp) => {
      const corpId = corp.corporate_id
      const corpCompanies = companies.filter((c) => String(c.corporate_id) === String(corpId))
      return {
        id: `corp-${corpId}`,
        data: { type: 'Corporate', name: corp.corp_name, code: corp.corp_code },
        children: corpCompanies.map((comp) => {
          const compId = comp.company_id
          const compBus = businessUnits.filter((b) => String(b.company_id) === String(compId))
          return {
            id: `comp-${compId}`,
            data: { type: 'Company', name: comp.legal_name, code: comp.company_code },
            children: compBus.map((bu) => {
              const buId = bu.business_unit_id
              const buSites = sites.filter((s) => String(s.business_unit_id) === String(buId))
              return {
                id: `bu-${buId}`,
                data: { type: 'Business Unit', name: bu.bu_name, code: bu.bu_code },
                children: buSites.map((site) => {
                  const siteId = site.site_id
                  const siteWarehouses = warehouses.filter((w) => String(w.site_id) === String(siteId))
                  return {
                    id: `site-${siteId}`,
                    data: { type: 'Site', name: site.site_name, code: site.site_code },
                    children: siteWarehouses.map((wh) => {
                      const whId = wh.warehouse_id
                      const whLocators = locators.filter((l) => String(l.warehouse_id) === String(whId))
                      return {
                        id: `wh-${whId}`,
                        data: { type: 'Warehouse', name: wh.warehouse_name, code: wh.warehouse_code },
                        children: whLocators.map((loc) => ({
                          id: `loc-${loc.warehouse_locator_id}`,
                          data: { type: 'Locator', name: loc.locator_code, code: loc.locator_code },
                        })),
                      }
                    }),
                  }
                }),
              }
            }),
          }
        }),
      }
    })
  }, [corporates, companies, businessUnits, sites, warehouses, locators])

  const treeColumns = [
    { id: 'type', header: 'Level', width: '130px', render: (r) => (
      <span className="text-[10px] font-semibold uppercase tracking-wider text-outline">{r.type}</span>
    )},
    { id: 'name', header: 'Name', width: '250px', render: (r) => (
      <span className="text-sm font-medium text-on-surface">{r.name}</span>
    )},
    { id: 'code', header: 'Code', width: '120px', render: (r) => (
      <span className="text-xs font-mono text-outline">{r.code}</span>
    )},
  ]

  if (treeNodes.length === 0) {
    return <p className="text-sm text-outline py-4 text-center">No organization data available.</p>
  }

  return (
    <TreeGrid
      data={treeNodes}
      columns={treeColumns}
      nodeLabelAccessor={(r) => `${r.type}: ${r.name}`}
      nodeIconAccessor={(r) =>
        r.type === 'Corporate' ? 'business' :
        r.type === 'Company' ? 'apartment' :
        r.type === 'Business Unit' ? 'layers' :
        r.type === 'Site' ? 'location_on' :
        r.type === 'Warehouse' ? 'warehouse' : 'inventory_2'
      }
      nodeDescriptionAccessor={(r) => r.code || r.name}
    />
  )
}

export default function OrgStructurePage() {
  const [activeTab, setActiveTab] = useState('corporates')
  const [data, setData] = useState({})
  const [loading, setLoading] = useState({})
  const [search, setSearch] = useState({})
  const [modalOpen, setModalOpen] = useState(false)
  const [editingItem, setEditingItem] = useState(null)
  const [saving, setSaving] = useState(false)
  const [formError, setFormError] = useState(null)
  const [form, setForm] = useState({})
  const [lookupData, setLookupData] = useState({})
  const [treeData, setTreeData] = useState({})
  const searchTimeout = useRef({})

  const resolveLabel = (lookupName, value) => {
    if (!value || !lookupName) return value
    const lk = LOOKUPS[lookupName]
    if (!lk) return value
    const list = lookupData[lk.endpoint] || []
    const match = list.find((item) => String(item[lk.valueKey]) === String(value))
    return match ? match[lk.labelKey] : value
  }

  const COLUMNS = {
  corporates: [
    { key: 'corp_code',  header: 'Code',   width: '140px' },
    { key: 'corp_name',  header: 'Name',   width: '220px' },
    { key: 'is_active',  header: 'Status', width: '100px',
      render: (r) => r.is_active !== false
        ? <span className="text-success text-xs font-semibold">Active</span>
        : <span className="text-outline text-xs">Inactive</span>,
    },
  ],
  companies: [
    { key: 'company_code', header: 'Code',     width: '140px' },
    { key: 'legal_name',   header: 'Name',     width: '220px' },
    { key: 'corporate_id', header: 'Corporate', width: '160px', render: (r) => resolveLabel('corporate_id', r.corporate_id) },
    { key: 'tax_id',       header: 'Tax ID',   width: '160px' },
    { key: 'is_active',    header: 'Status',   width: '100px' },
  ],
  businessUnits: [
    { key: 'bu_code',      header: 'Code',     width: '140px' },
    { key: 'bu_name',      header: 'Name',     width: '220px' },
    { key: 'company_id',   header: 'Company',  width: '140px', render: (r) => resolveLabel('company_id', r.company_id) },
    { key: 'is_active',    header: 'Status',   width: '100px' },
  ],
  sites: [
    { key: 'site_code',    header: 'Code',     width: '140px' },
    { key: 'site_name',    header: 'Name',     width: '220px' },
    { key: 'business_unit_id', header: 'BU',   width: '120px', render: (r) => resolveLabel('business_unit_id', r.business_unit_id) },
    { key: 'address_id',   header: 'Address',  width: '200px', render: (r) => resolveLabel('address_id', r.address_id) },
    { key: 'is_active',    header: 'Status',   width: '100px' },
  ],
  warehouses: [
    { key: 'warehouse_code', header: 'Code',   width: '140px' },
    { key: 'warehouse_name', header: 'Name',   width: '220px' },
    { key: 'site_id',        header: 'Site',   width: '120px', render: (r) => resolveLabel('site_id', r.site_id) },
    { key: 'is_active',      header: 'Status', width: '100px' },
  ],
  locators: [
    { key: 'locator_code', header: 'Code',        width: '140px' },
    { key: 'warehouse_id', header: 'Warehouse',   width: '140px', render: (r) => resolveLabel('warehouse_id', r.warehouse_id) },
    { key: 'zone',         header: 'Zone',        width: '80px'  },
    { key: 'aisle',        header: 'Aisle',       width: '80px'  },
    { key: 'rack',         header: 'Rack',        width: '80px'  },
    { key: 'bin',          header: 'Bin',         width: '80px'  },
    { key: 'is_active',    header: 'Status',      width: '100px' },
  ],
}

  const tab = TABS.find((t) => t.key === activeTab)
  const fields = FIELDS[activeTab] || []

  const fetchData = useCallback(async (tabKey) => {
    const cfg = TABS.find((t) => t.key === tabKey)
    if (!cfg) return
    setLoading((prev) => ({ ...prev, [tabKey]: true }))
    try {
      const { data: res } = await api.get(cfg.endpoint, { params: { page: 1, page_size: 100 } })
      setData((prev) => ({ ...prev, [tabKey]: res.items || res.data || [] }))
    } catch {
      setData((prev) => ({ ...prev, [tabKey]: [] }))
    } finally {
      setLoading((prev) => ({ ...prev, [tabKey]: false }))
    }
  }, [])

  const fetchAllTreeData = useCallback(async () => {
    try {
      const endpoints = [
        ['corporates', '/org_structure/corporates'],
        ['companies', '/org_structure/companies'],
        ['businessUnits', '/org_structure/business-units'],
        ['sites', '/org_structure/sites'],
        ['warehouses', '/org_structure/warehouses'],
        ['locators', '/org_structure/locators'],
      ]
      const results = {}
      for (const [key, ep] of endpoints) {
        try {
          const { data: res } = await api.get(ep, { params: { page: 1, page_size: 100 } })
          results[key] = res.items || res.data || []
        } catch { results[key] = [] }
      }
      setTreeData(results)
    } catch {}
  }, [])

  useEffect(() => {
    fetchAllTreeData()
  }, [fetchAllTreeData])

  useEffect(() => {
    const tabCfg = TABS.find((t) => t.key === activeTab)
    if (!tabCfg) return
    if (!data[activeTab]) fetchData(activeTab)
    const fkFields = (FIELDS[activeTab] || []).filter((f) => f.lookup)
    for (const f of fkFields) {
      const lk = LOOKUPS[f.lookup]
      if (!lk) continue
      ;(async () => {
        try {
          const { data: res } = await api.get(lk.endpoint, { params: { page: 1, page_size: 100 } })
          setLookupData((prev) => ({ ...prev, [lk.endpoint]: res.items || res.data || [] }))
        } catch {}
      })()
    }
  }, [activeTab])

  const handleSearch = (query) => {
    const key = activeTab
    if (searchTimeout.current[key]) clearTimeout(searchTimeout.current[key])
    searchTimeout.current[key] = setTimeout(() => {
      setSearch((prev) => ({ ...prev, [key]: query.toLowerCase() }))
    }, 300)
  }

  const rawData = data[activeTab] || []
  const searchTerm = search[activeTab] || ''
  const filteredData = searchTerm
    ? rawData.filter((row) => Object.values(row).some((v) => v != null && String(v).toLowerCase().includes(searchTerm)))
    : rawData

  const entityId = (row) => tab ? row[tab.idKey] : null

  const openCreate = () => {
    setEditingItem(null)
    const init = {}
    fields.forEach((f) => { init[f.key] = '' })
    setForm(init)
    setFormError(null)
    setModalOpen(true)
  }

  const openEdit = (row) => {
    setEditingItem(row)
    const init = {}
    fields.forEach((f) => { init[f.key] = row[f.key] != null ? String(row[f.key]) : '' })
    setForm(init)
    setFormError(null)
    setModalOpen(true)
  }

  const closeModal = () => { setModalOpen(false); setEditingItem(null) }

  const handleSave = async (e) => {
    e.preventDefault()
    setSaving(true)
    setFormError(null)
    try {
      const payload = {}
      fields.forEach((f) => {
        if (form[f.key] !== '') payload[f.key] = form[f.key]
      })
      if (editingItem) {
        await api.put(`${tab.endpoint}/${entityId(editingItem)}`, payload)
      } else {
        await api.post(tab.endpoint, payload)
      }
      closeModal()
      fetchData(activeTab)
    } catch (err) {
      const msg = err.response?.data?.detail?.message || err.response?.data?.detail?.[0]?.msg || err.response?.data || 'Failed to save'
      setFormError(typeof msg === 'string' ? msg : JSON.stringify(msg))
    } finally {
      setSaving(false)
    }
  }

  const handleDelete = async (row) => {
    const name = row[tab.nameField] || entityId(row)
    if (!window.confirm(`Delete "${name}"?`)) return
    try {
      await api.delete(`${tab.endpoint}/${entityId(row)}`)
      fetchData(activeTab)
    } catch (err) {
      setFormError(err.response?.data?.detail?.message || 'Failed to delete')
    }
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-slate-900! dark:text-white!">Org Structure</h1>
          <p className="text-sm text-slate-500! dark:text-slate-300! mt-1">Manage corporates, companies, business units, sites, warehouses, and locators</p>
        </div>
        <button onClick={openCreate}
          className="flex items-center gap-1.5 px-4 py-2 bg-primary text-primary-foreground rounded-xl text-xs font-bold hover:opacity-90 transition-all shadow-lg shadow-primary/20">
          <Plus size={15} /> Add {tab?.label}
        </button>
      </div>

      <div className="flex items-center gap-1 border-b border-outline-variant overflow-x-auto">
        {TABS.map((t) => (
          <button key={t.key} onClick={() => setActiveTab(t.key)}
            className={`flex items-center gap-2 px-4 py-3 text-xs font-semibold whitespace-nowrap border-b-2 transition-colors ${
              activeTab === t.key
                ? 'border-primary text-primary'
                : 'border-transparent text-on-surface-variant hover:text-on-surface hover:border-outline-variant'
            }`}>
            <span className="material-symbols-outlined text-[18px]">
              {t.key === 'corporates' ? 'business' : t.key === 'companies' ? 'apartment' : t.key === 'businessUnits' ? 'layers' : t.key === 'sites' ? 'location_on' : t.key === 'warehouses' ? 'warehouse' : 'inventory_2'}
            </span>
            {t.label}
          </button>
        ))}
      </div>

      {tab && (
        <InteractiveGrid
          key={tab.key}
          columns={COLUMNS[tab.key]}
          data={filteredData}
          loading={loading[activeTab]}
          idKey={tab.idKey}
          searchable
          onSearch={handleSearch}
          onAddRow={openCreate}
          onEdit={(row) => openEdit(row)}
          onDelete={(row) => handleDelete(row)}
          addLabel={`Add ${tab.label}`}
          tableHeight="calc(100vh - 320px)"
        />
      )}

      {/* ── ORG TREE VIEW ── */}
      <details className="border border-outline-variant rounded-xl overflow-hidden bg-surface-container-lowest group" open>
        <summary className="flex items-center justify-between px-5 py-3 cursor-pointer hover:bg-surface-container-low transition-colors text-sm font-semibold text-outline group-open:text-on-surface list-none">
          <span className="flex items-center gap-2">
            <span className="material-symbols-outlined text-[18px]">account_tree</span>
            Organization Hierarchy
          </span>
          <span className="material-symbols-outlined text-[18px] transition-transform group-open:rotate-180">expand_more</span>
        </summary>
        <div className="border-t border-outline-variant p-4">
          <OrgTreeView data={treeData} />
        </div>
      </details>

      {modalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm p-4">
          <div className="bg-surface-container rounded-2xl border border-outline-variant shadow-2xl w-full max-w-lg max-h-[90vh] overflow-y-auto custom-scrollbar">
            <div className="flex items-center justify-between p-5 border-b border-outline-variant">
              <h2 className="text-lg font-bold text-slate-900! dark:text-white!">{editingItem ? `Edit ${tab?.label}` : `Add ${tab?.label}`}</h2>
              <button onClick={closeModal} className="p-1.5 rounded-lg hover:bg-surface-container-high text-outline hover:text-on-surface transition-colors">
                <span className="material-symbols-outlined text-[18px]">close</span>
              </button>
            </div>
            <form onSubmit={handleSave} className="p-5 space-y-4">
              {formError && <div className="bg-error-container text-error p-3 rounded-xl text-sm font-medium">{formError}</div>}
              {fields.map((f) => {
                const isLookup = f.lookup && LOOKUPS[f.lookup]
                const lk = isLookup ? LOOKUPS[f.lookup] : null
                const options = lk ? (lookupData[lk.endpoint] || []) : []
                return (
                  <div key={f.key}>
                    <label className="block text-[11px] font-semibold uppercase tracking-wider text-outline mb-1.5">
                      {f.label} {f.required && '*'}
                    </label>
                    {isLookup ? (
                      <select value={form[f.key] || ''}
                        onChange={(e) => setForm({ ...form, [f.key]: e.target.value })}
                        className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition"
                        required={f.required}>
                        <option value="">-- Select {f.label} --</option>
                        {options.map((opt) => (
                          <option key={opt[lk.valueKey]} value={opt[lk.valueKey]}>
                            {opt[lk.labelKey]}
                          </option>
                        ))}
                      </select>
                    ) : (
                      <input type="text" value={form[f.key] || ''}
                        onChange={(e) => setForm({ ...form, [f.key]: e.target.value })}
                        className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition"
                        required={f.required} />
                    )}
                  </div>
                )
              })}
              <div className="flex justify-end gap-3 pt-2">
                <button type="button" onClick={closeModal}
                  className="neo-button px-5 py-2.5 text-sm font-semibold text-on-surface-variant">Cancel</button>
                <button type="submit" disabled={saving}
                  className="flex items-center gap-2 px-5 py-2.5 bg-primary text-primary-foreground rounded-xl text-sm font-semibold hover:opacity-90 disabled:opacity-50 transition-all shadow-lg shadow-primary/20">
                  {saving && <span className="animate-spin inline-block w-4 h-4 border-2 border-white/30 border-t-white rounded-full" />}
                  {editingItem ? 'Save Changes' : 'Create'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  )
}
