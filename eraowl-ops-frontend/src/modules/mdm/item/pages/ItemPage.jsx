import { useState, useEffect, useCallback, useRef } from 'react'
import api from '../../../../api/client'
import { Plus } from 'lucide-react'
import { InteractiveGrid } from '../../../../shared-ui-kit/components/ui/InteractiveGrid'

const TABS = [
  { key: 'items',          label: 'Items',           endpoint: '/item/items',           idKey: 'item_id',            nameField: 'item_name'        },
  { key: 'itemCategories', label: 'Item Categories', endpoint: '/item/item-categories',  idKey: 'item_category_id',   nameField: 'category_name'    },
  { key: 'uoms',           label: 'UOMs',            endpoint: '/item/uoms',             idKey: 'uom_id',             nameField: 'uom_name'         },
]

const COLUMNS = {
  items: [
    { key: 'item_code', header: 'Code',    width: '140px' },
    { key: 'item_name', header: 'Name',    width: '220px' },
    { key: 'item_type', header: 'Type',    width: '130px' },
    { key: 'status',    header: 'Status',  width: '120px' },
    { key: 'is_active', header: 'Status',  width: '100px',
      render: (r) => r.is_active !== false
        ? <span className="text-success text-xs font-semibold">Active</span>
        : <span className="text-outline text-xs">Inactive</span>,
    },
  ],
  itemCategories: [
    { key: 'category_code', header: 'Code',   width: '140px' },
    { key: 'category_name', header: 'Name',   width: '220px' },
    { key: 'category_set',  header: 'Set',    width: '140px' },
    { key: 'is_active',     header: 'Status', width: '100px',
      render: (r) => r.is_active !== false
        ? <span className="text-success text-xs font-semibold">Active</span>
        : <span className="text-outline text-xs">Inactive</span>,
    },
  ],
  uoms: [
    { key: 'uom_code', header: 'Code',   width: '120px' },
    { key: 'uom_name', header: 'Name',   width: '200px' },
    { key: 'uom_type', header: 'Type',   width: '120px' },
    { key: 'is_active', header: 'Status', width: '100px',
      render: (r) => r.is_active !== false
        ? <span className="text-success text-xs font-semibold">Active</span>
        : <span className="text-outline text-xs">Inactive</span>,
    },
  ],
}

const FIELDS = {
  items: [
    { key: 'item_code',   label: 'Item Code',   required: true },
    { key: 'item_name',   label: 'Item Name',   required: true },
    { key: 'item_type',   label: 'Item Type',   required: true, type: 'select', options: ['RAW_MATERIAL', 'FINISHED_GOOD', 'WORK_IN_PROGRESS', 'SERVICE'] },
    { key: 'description', label: 'Description' },
  ],
  itemCategories: [
    { key: 'category_code', label: 'Category Code', required: true },
    { key: 'category_name', label: 'Category Name', required: true },
    { key: 'category_set',  label: 'Category Set',  required: true, type: 'select', options: ['COMMODITY', 'MERCHANDISE', 'PRODUCTION', 'PACKAGING', 'CONSUMABLE', 'MAINTENANCE'] },
  ],
  uoms: [
    { key: 'uom_code', label: 'UOM Code', required: true },
    { key: 'uom_name', label: 'UOM Name', required: true },
    { key: 'uom_type', label: 'UOM Type', required: true, type: 'select', options: ['QUANTITY', 'WEIGHT', 'VOLUME', 'LENGTH'] },
  ],
}

export default function ItemPage() {
  const [activeTab, setActiveTab] = useState('items')
  const [data, setData] = useState({})
  const [loading, setLoading] = useState({})
  const [search, setSearch] = useState({})
  const [modalOpen, setModalOpen] = useState(false)
  const [editingItem, setEditingItem] = useState(null)
  const [saving, setSaving] = useState(false)
  const [formError, setFormError] = useState(null)
  const [form, setForm] = useState({})
  const searchTimeout = useRef({})

  const tab = TABS.find((t) => t.key === activeTab)
  const fields = FIELDS[activeTab] || []

  const fetchData = useCallback(async (tabKey, searchTerm = '') => {
    const cfg = TABS.find((t) => t.key === tabKey)
    if (!cfg) return
    setLoading((prev) => ({ ...prev, [tabKey]: true }))
    try {
      const params = { page: 1, page_size: 100 }
      if (searchTerm) params.search = searchTerm
      const { data: res } = await api.get(cfg.endpoint, { params })
      setData((prev) => ({ ...prev, [tabKey]: res.items || res.data || [] }))
    } catch {
      setData((prev) => ({ ...prev, [tabKey]: [] }))
    } finally {
      setLoading((prev) => ({ ...prev, [tabKey]: false }))
    }
  }, [])

  useEffect(() => {
    if (!data[activeTab]) fetchData(activeTab, search[activeTab] || '')
  }, [activeTab, data, fetchData])

  const handleSearch = (query) => {
    const key = activeTab
    if (searchTimeout.current[key]) clearTimeout(searchTimeout.current[key])
    searchTimeout.current[key] = setTimeout(() => {
      setSearch((prev) => ({ ...prev, [key]: query }))
      fetchData(key, query)
    }, 300)
  }

  const rawData = data[activeTab] || []

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
      setFormError(err.response?.data?.detail?.message || 'Failed to save')
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
          <h1 className="text-2xl font-bold text-on-surface">Item Master</h1>
          <p className="text-sm text-outline mt-1">Manage items, categories, and units of measure</p>
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
              {t.key === 'items' ? 'inventory' :
               t.key === 'itemCategories' ? 'category' :
               'straighten'}
            </span>
            {t.label}
          </button>
        ))}
      </div>

      {tab && (
        <InteractiveGrid
          key={tab.key}
          columns={COLUMNS[tab.key]}
          data={rawData}
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
              {fields.map((f) => (
                <div key={f.key}>
                  <label className="block text-[11px] font-semibold uppercase tracking-wider text-outline mb-1.5">
                    {f.label} {f.required && '*'}
                  </label>
                  {f.type === 'select' ? (
                    <select value={form[f.key] || ''}
                      onChange={(e) => setForm({ ...form, [f.key]: e.target.value })}
                      className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition"
                      required={f.required}>
                      <option value="">Select {f.label}</option>
                      {f.options.map((opt) => (
                        <option key={opt} value={opt}>{opt}</option>
                      ))}
                    </select>
                  ) : (
                    <input type="text" value={form[f.key] || ''}
                      onChange={(e) => setForm({ ...form, [f.key]: e.target.value })}
                      className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition"
                      required={f.required} />
                  )}
                </div>
              ))}
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
