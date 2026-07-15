import { useState, useEffect, useCallback, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../../../../api/client'
import { Plus } from 'lucide-react'
import { InteractiveGrid } from '../../../../shared-ui-kit/components/ui/InteractiveGrid'

const TABS = [
  { key: 'addresses', label: 'Addresses',  endpoint: '/party/addresses',  idKey: 'address_id',   nameField: 'city'           },
  { key: 'parties',   label: 'Parties',    endpoint: '/party/parties',    idKey: 'party_id',     nameField: 'party_name'     },
  { key: 'customers', label: 'Customers',  endpoint: '/party/customers',  idKey: 'customer_id',   nameField: 'customer_code'  },
]

const COLUMNS = {
  addresses: [
    { key: 'address_line1', header: 'Address',     width: '240px' },
    { key: 'city',          header: 'City',        width: '150px' },
    { key: 'country_code',  header: 'Country',     width: '130px' },
    { key: 'is_active',     header: 'Status',      width: '100px',
      render: (r) => r.is_active !== false
        ? <span className="text-success text-xs font-semibold">Active</span>
        : <span className="text-outline text-xs">Inactive</span>,
    },
  ],
  parties: [
    { key: 'party_code',  header: 'Code',   width: '120px' },
    { key: 'party_name',  header: 'Name',   width: '220px' },
    { key: 'party_type',  header: 'Type',   width: '130px' },
    { key: 'is_active',   header: 'Status', width: '100px',
      render: (r) => r.is_active !== false
        ? <span className="text-success text-xs font-semibold">Active</span>
        : <span className="text-outline text-xs">Inactive</span>,
    },
  ],
  customers: [
    { key: 'customer_code',    header: 'Code',        width: '140px' },
    { key: 'credit_limit',     header: 'Credit Limit', width: '130px' },
    { key: 'payment_term_days', header: 'Payment Terms', width: '140px' },
    { key: 'is_active',        header: 'Status',      width: '100px',
      render: (r) => r.is_active !== false
        ? <span className="text-success text-xs font-semibold">Active</span>
        : <span className="text-outline text-xs">Inactive</span>,
    },
  ],
}

const FIELDS = {
  addresses: [
    { key: 'address_line1',  label: 'Address Line 1', required: true },
    { key: 'address_line2',  label: 'Address Line 2' },
    { key: 'city',           label: 'City',           required: true },
    { key: 'state_province', label: 'State/Province' },
    { key: 'postal_code',    label: 'Postal Code' },
    { key: 'country_code',   label: 'Country Code' },
  ],
  parties: [
    { key: 'party_code', label: 'Party Code' },
    { key: 'party_name', label: 'Party Name', required: true },
    { key: 'party_type', label: 'Party Type', required: true },
    { key: 'tax_id',     label: 'Tax ID' },
  ],
  customers: [
    { key: 'customer_code',    label: 'Customer Code',    required: true },
    { key: 'credit_limit',     label: 'Credit Limit' },
    { key: 'payment_term_days', label: 'Payment Term Days' },
  ],
}

export default function PartyPage() {
  const navigate = useNavigate()
  const [activeTab, setActiveTab] = useState('addresses')
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
    if (!data[activeTab]) fetchData(activeTab)
  }, [activeTab, data, fetchData])

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
          <h1 className="text-2xl font-bold text-on-surface">Party Management</h1>
          <p className="text-sm text-outline mt-1">Manage addresses, parties, suppliers, and customers</p>
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
              {t.key === 'addresses' ? 'map' :
               t.key === 'parties' ? 'groups' :
               'group'}
            </span>
            {t.label}
          </button>
        ))}
        <button onClick={() => navigate('/party/suppliers')}
          className="flex items-center gap-2 px-4 py-3 text-xs font-semibold whitespace-nowrap border-b-2 border-transparent text-on-surface-variant hover:text-on-surface hover:border-outline-variant transition-colors">
          <span className="material-symbols-outlined text-[18px]">local_shipping</span>
          Suppliers
        </button>
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
              {fields.map((f) => (
                <div key={f.key}>
                  <label className="block text-[11px] font-semibold uppercase tracking-wider text-outline mb-1.5">
                    {f.label} {f.required && '*'}
                  </label>
                  <input type="text" value={form[f.key] || ''}
                    onChange={(e) => setForm({ ...form, [f.key]: e.target.value })}
                    className="w-full px-3 py-2.5 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition"
                    required={f.required} />
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
