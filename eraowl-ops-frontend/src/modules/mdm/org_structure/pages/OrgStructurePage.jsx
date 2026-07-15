import { useState, useEffect, useCallback, useRef } from 'react'
import api from '../../../../api/client'
import { Plus } from 'lucide-react'
import { InteractiveGrid } from '../../../../shared-ui-kit/components/ui/InteractiveGrid'

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
    { key: 'zone', label: 'Zone' },
    { key: 'aisle', label: 'Aisle' },
    { key: 'rack', label: 'Rack' },
    { key: 'bin', label: 'Bin' },
  ],
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
    { key: 'locator_code', header: 'Code',     width: '140px' },
    { key: 'zone',         header: 'Zone',     width: '80px'  },
    { key: 'aisle',        header: 'Aisle',    width: '80px'  },
    { key: 'rack',         header: 'Rack',     width: '80px'  },
    { key: 'bin',          header: 'Bin',      width: '80px'  },
    { key: 'is_active',    header: 'Status',   width: '100px' },
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
          <h1 className="text-2xl font-bold text-on-surface">Org Structure</h1>
          <p className="text-sm text-outline mt-1">Manage corporates, companies, business units, sites, warehouses, and locators</p>
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

      {modalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm p-4">
          <div className="bg-surface-container rounded-2xl border border-outline-variant shadow-2xl w-full max-w-lg max-h-[90vh] overflow-y-auto custom-scrollbar">
            <div className="flex items-center justify-between p-5 border-b border-outline-variant">
              <h2 className="text-lg font-bold text-on-surface">{editingItem ? `Edit ${tab?.label}` : `Add ${tab?.label}`}</h2>
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
