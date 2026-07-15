import { useState, useEffect, useCallback, useMemo } from 'react'
import { useNavigate, useParams, useLocation } from 'react-router-dom'
import api from '../../../../api/client'
import { InteractiveGrid } from '../../../../shared-ui-kit/components/ui/InteractiveGrid'

const CURRENCIES = ['THB', 'USD', 'EUR', 'JPY', 'GBP', 'SGD', 'MYR', 'IDR', 'VND', 'CNY']
const PAYMENT_METHODS = ['CHECK', 'EFT', 'WIRE_TRANSFER', 'CASH', 'DIRECT_DEBIT']
const VENDOR_TYPES = ['STANDARD', 'GOVERNMENT', 'EMPLOYEE', 'ONE_TIME', 'INTERNAL', 'FOREIGN']
const STATUS_OPTIONS = ['ACTIVE', 'ON_HOLD', 'INACTIVE']

function Inp({ value, onChange, placeholder, className, type = 'text' }) {
  return <input type={type} value={value ?? ''} onChange={e => onChange(type === 'number' ? (e.target.value ? Number(e.target.value) : null) : e.target.value)} placeholder={placeholder}
    className={`w-full bg-surface-container-lowest border border-outline-variant rounded-lg px-3 py-2.5 text-sm text-on-surface font-semibold focus:ring-2 focus:ring-primary outline-none transition-all placeholder:text-outline/40 ${className ?? ''}`} />
}

function Sel({ value, onChange, options, label }) {
  return (
    <select value={value} onChange={e => onChange(e.target.value)}
      className="w-full bg-surface-container-lowest border border-outline-variant rounded-lg px-3 py-2.5 text-sm text-on-surface font-semibold focus:ring-2 focus:ring-primary outline-none transition-all">
      {label && <option value="">{label}</option>}
      {options.map(o => <option key={o} value={o}>{o.replace(/_/g, ' ')}</option>)}
    </select>
  )
}

function Toggle({ value, onChange }) {
  return (
    <button type="button" onClick={() => onChange(!value)}
      className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors duration-200 flex-shrink-0 ${value ? 'bg-green-500' : 'bg-outline-variant'}`}>
      <span className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform duration-200 shadow-sm ${value ? 'translate-x-6' : 'translate-x-1'}`} />
    </button>
  )
}

function Badge({ active, labelTrue, labelFalse }) {
  return <span className={`inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wide ${active ? 'bg-green-500/10 text-green-400' : 'bg-outline-variant/30 text-outline'}`}>
    <span className={`w-1.5 h-1.5 rounded-full ${active ? 'bg-green-500' : 'bg-outline'}`} />{active ? (labelTrue ?? 'Yes') : (labelFalse ?? 'No')}
  </span>
}

function Fld({ label, required, children }) {
  return <div><label className="block text-[10px] text-on-surface-variant font-semibold mb-2 tracking-wider uppercase">{label}{required && <span className="text-error"> *</span>}</label>{children}</div>
}

function Tabs({ tabs, activeTab, onTabChange }) {
  return (
    <div className="border-b border-outline-variant/50">
      <div className="flex items-center gap-1 px-2 pt-2 overflow-x-auto">
        {tabs.map(tab => (
          <button key={tab.key} type="button" onClick={() => onTabChange(tab.key)}
            className={`px-4 py-2.5 text-[10px] font-bold uppercase tracking-wider rounded-t-lg transition-all flex items-center gap-1.5 whitespace-nowrap ${activeTab === tab.key ? 'bg-surface-container-high text-primary shadow-sm' : 'text-outline hover:text-on-surface hover:bg-surface-container-low'}`}>
            <span className="material-symbols-outlined !text-[14px]">{tab.icon}</span>{tab.label}</button>
        ))}
      </div>
    </div>
  )
}

function parseRows(data) {
  if (Array.isArray(data)) return data
  if (data && typeof data === 'object' && 'items' in data && Array.isArray(data.items)) return data.items
  return []
}

export default function SupplierPage() {
  const { supplierId } = useParams()
  const location = useLocation()
  const navigate = useNavigate()
  const isFormOpen = Boolean(supplierId) || location.state?.creating === true
  const isEdit = Boolean(supplierId)

  const [headerTab, setHeaderTab] = useState('basic')
  const [saving, setSaving] = useState(false)
  const [suppliers, setSuppliers] = useState([])
  const [suppliersLoading, setSuppliersLoading] = useState(true)
  const [form, setForm] = useState({
    supplier_code: '', currency_code: 'THB', payment_term_days: '',
    vendor_type_lookup_code: 'STANDARD', payment_method_code: 'EFT',
    is_active: true,
  })
  const [existingSupplier, setExistingSupplier] = useState(null)

  const [sites, setSites] = useState([])
  const [sitesLoading, setSitesLoading] = useState(false)
  const [addresses, setAddresses] = useState([])
  const [newSite, setNewSite] = useState(null)
  const [selectedSiteIds, setSelectedSiteIds] = useState(new Set())
  const [editingSiteIds, setEditingSiteIds] = useState(new Set())

  const fetchSuppliers = useCallback(async () => {
    setSuppliersLoading(true)
    try {
      const { data } = await api.get('/party/suppliers', { params: { page: 1, page_size: 100 } })
      setSuppliers(parseRows(data))
    } catch { setSuppliers([]) } finally { setSuppliersLoading(false) }
  }, [])

  const fetchExisting = useCallback(async () => {
    if (!supplierId) return
    try {
      const { data } = await api.get(`/party/suppliers/${supplierId}`)
      setExistingSupplier(data)
      setForm({
        supplier_code: data.supplier_code || '',
        currency_code: data.currency_code || 'THB',
        payment_term_days: data.payment_term_days != null ? String(data.payment_term_days) : '',
        vendor_type_lookup_code: data.vendor_type_lookup_code || 'STANDARD',
        payment_method_code: data.payment_method_code || 'EFT',
        is_active: data.is_active !== false,
      })
    } catch { setExistingSupplier(null) }
  }, [supplierId])

  const fetchSites = useCallback(async () => {
    if (!supplierId) { setSites([]); return }
    setSitesLoading(true)
    try {
      const { data } = await api.get('/party/supplier-sites', { params: { supplier_id: supplierId, page: 1, page_size: 100 } })
      setSites(parseRows(data))
    } catch { setSites([]) } finally { setSitesLoading(false) }
  }, [supplierId])

  const fetchAddresses = useCallback(async () => {
    try {
      const { data } = await api.get('/party/addresses', { params: { page: 1, page_size: 100 } })
      setAddresses(parseRows(data))
    } catch { setAddresses([]) }
  }, [])

  useEffect(() => { if (!isFormOpen) fetchSuppliers() }, [isFormOpen, fetchSuppliers])
  useEffect(() => { if (isFormOpen) { fetchExisting(); fetchSites(); fetchAddresses() } }, [isFormOpen, fetchExisting, fetchSites, fetchAddresses])

  const updateForm = useCallback((patch) => { setForm(prev => ({ ...prev, ...patch })) }, [])

  const handleSave = useCallback(async () => {
    if (!form.supplier_code.trim()) { alert('Supplier code is required.'); return }
    setSaving(true)
    try {
      const payload = {}
      for (const k of Object.keys(form)) {
        if (k === 'payment_term_days') payload[k] = form[k] ? parseInt(form[k]) : undefined
        else if (k === 'is_active') payload[k] = form[k]
        else payload[k] = form[k] || undefined
      }
      if (isEdit && supplierId) {
        await api.put(`/party/suppliers/${supplierId}`, payload)
      } else {
        await api.post('/party/suppliers', payload)
      }
      navigate('/party/suppliers', { replace: true })
    } catch (err) {
      alert(err.response?.data?.detail?.message || 'Failed to save')
    } finally { setSaving(false) }
  }, [form, isEdit, supplierId, navigate])

  const handleDelete = useCallback(async (id) => {
    if (!confirm('Delete this supplier?')) return
    try {
      await api.delete(`/party/suppliers/${id}`)
      fetchSuppliers()
    } catch (err) { alert(err.response?.data?.detail?.message || 'Failed to delete') }
  }, [fetchSuppliers])

  const siteUpdate = useCallback(async (id, payload) => {
    try { await api.put(`/party/supplier-sites/${id}`, payload); fetchSites() } catch (err) { alert(err.response?.data?.detail?.message || 'Failed') }
  }, [fetchSites])

  const siteCreate = useCallback(async (payload) => {
    try { await api.post('/party/supplier-sites', { ...payload, supplier_id: supplierId }); setNewSite(null); fetchSites() } catch (err) { alert(err.response?.data?.detail?.message || 'Failed') }
  }, [supplierId, fetchSites])

  const siteDelete = useCallback(async (id) => {
    try { await api.delete(`/party/supplier-sites/${id}`); fetchSites() } catch (err) { alert(err.response?.data?.detail?.message || 'Failed') }
  }, [fetchSites])

  // ===== LIST VIEW =====
  if (!isFormOpen) {
    const listColumns = [
      {
        key: 'supplier_code', header: 'Supplier Code', width: '160px',
        render: (row) => (
          <button onClick={() => navigate(`/party/suppliers/${row.supplier_id}`)}
            className="text-sm font-semibold text-primary hover:underline text-left">{row.supplier_code}</button>
        )
      },
      { key: 'currency_code', header: 'Currency', width: '100px',
        render: (row) => <span className="text-sm font-mono text-on-surface">{row.currency_code || '\u2014'}</span>
      },
      { key: 'payment_term_days', header: 'Terms', width: '90px',
        render: (row) => <span className="text-sm font-mono text-on-surface">{row.payment_term_days ? `${row.payment_term_days}d` : '\u2014'}</span>
      },
      { key: 'vendor_type_lookup_code', header: 'Type', width: '120px',
        render: (row) => <span className="text-[11px] font-semibold px-2 py-1 rounded-md bg-primary/10 text-primary">{(row.vendor_type_lookup_code || 'STANDARD').replace(/_/g, ' ')}</span>
      },
      { key: 'payment_method_code', header: 'Method', width: '120px',
        render: (row) => <span className="text-sm text-on-surface">{(row.payment_method_code || '\u2014').replace(/_/g, ' ')}</span>
      },
      { key: 'is_active', header: 'Status', width: '90px',
        render: (row) => <Badge active={row.is_active !== false} labelTrue="Active" labelFalse="Inactive" />
      },
    ]

    return (
      <div className="h-[calc(100vh-6.5rem)] flex flex-col">
        <div className="flex items-center justify-between px-4 py-3 border-b border-outline-variant">
          <div>
            <h1 className="text-[32px] font-semibold leading-10 tracking-tight text-on-surface">Suppliers</h1>
            <p className="text-sm text-outline mt-1">{suppliersLoading ? 'Loading...' : `${suppliers.length} supplier${suppliers.length !== 1 ? 's' : ''}`}</p>
          </div>
          <button onClick={() => navigate('/party/suppliers', { state: { creating: true } })}
            className="px-4 py-2 bg-primary text-primary-foreground text-[11px] font-semibold rounded-lg hover:brightness-110 active:scale-95 transition-all shadow-lg shadow-primary/20 flex items-center gap-1.5">
            <span className="material-symbols-outlined !text-[16px]">add</span> Add New Supplier</button>
        </div>
        <div className="flex-1 overflow-y-auto p-4">
          <InteractiveGrid
            columns={listColumns}
            data={suppliers}
            idKey="supplier_id"
            searchable
            onRowClick={(row) => navigate(`/party/suppliers/${row.supplier_id}`)}
            onEdit={(row) => navigate(`/party/suppliers/${row.supplier_id}`)}
            onDelete={(row) => handleDelete(row.supplier_id)}
            onAddRow={() => navigate('/party/suppliers', { state: { creating: true } })}
            addLabel="Add Supplier"
            loading={suppliersLoading}
            tableHeight="calc(100vh - 200px)"
          />
        </div>
      </div>
    )
  }

  // ===== FORM VIEW =====
  const formTabs = [
    { key: 'basic', label: 'Basic', icon: 'info' },
    { key: 'details', label: 'Details', icon: 'data_info_alert' },
  ]

  const siteColumns = [
    { key: 'site_name', header: 'Site Name', width: '180px',
      render: (row) => row.isNew ? (
        <Inp value={newSite?.site_name} onChange={v => setNewSite({ ...newSite, site_name: v })} placeholder="Name" />
      ) : editingSiteIds.has(row.supplier_site_id) ? (
        <Inp value={row.site_name || ''} onChange={v => siteUpdate(row.supplier_site_id, { site_name: v })} placeholder="Name" />
      ) : <span className="text-sm font-semibold text-on-surface">{row.site_name || '\u2014'}</span>
    },
    { key: 'site_number', header: 'Site Number', width: '130px',
      render: (row) => row.isNew ? (
        <Inp value={newSite?.site_number} onChange={v => setNewSite({ ...newSite, site_number: v })} placeholder="Number" />
      ) : editingSiteIds.has(row.supplier_site_id) ? (
        <Inp value={row.site_number || ''} onChange={v => siteUpdate(row.supplier_site_id, { site_number: v })} placeholder="Number" />
      ) : <span className="text-sm text-on-surface">{row.site_number || '\u2014'}</span>
    },
    { key: 'address_id', header: 'Address', width: '200px',
      render: (row) => {
        const val = row.isNew ? newSite?.address_id : row.address_id
        const onChange = (e) => row.isNew ? setNewSite({ ...newSite, address_id: e.target.value }) : siteUpdate(row.supplier_site_id, { address_id: e.target.value })
        const addr = addresses.find(a => a.address_id === val)
        const display = addr ? `${addr.address_line1 || ''}, ${addr.city || ''}` : '\u2014'
        return (row.isNew || editingSiteIds.has(row.supplier_site_id)) ? (
          <select value={val || ''} onChange={onChange}
            className="w-full bg-transparent border-b border-transparent hover:border-outline-variant focus:border-primary px-1 py-0.5 text-sm text-on-surface outline-none transition-all">
            <option value="">Select...</option>
            {addresses.map(a => <option key={a.address_id} value={a.address_id}>{a.address_line1}, {a.city}</option>)}
          </select>
        ) : <span className="text-sm text-outline truncate">{display}</span>
      }
    },
    { key: 'is_primary', header: 'Primary', width: '90px',
      render: (row) => {
        const val = row.isNew ? newSite?.is_primary : row.is_primary
        const onChange = (v) => row.isNew ? setNewSite({ ...newSite, is_primary: v }) : siteUpdate(row.supplier_site_id, { is_primary: v })
        return (row.isNew || editingSiteIds.has(row.supplier_site_id)) ? (
          <Toggle value={!!val} onChange={onChange} />
        ) : <Badge active={!!val} labelTrue="Yes" labelFalse="No" />
      }
    },
    { key: 'is_active', header: 'Active', width: '80px',
      render: (row) => {
        const val = row.isNew ? newSite?.is_active : row.is_active
        const onChange = (v) => row.isNew ? setNewSite({ ...newSite, is_active: v }) : siteUpdate(row.supplier_site_id, { is_active: v })
        if (row.isNew || editingSiteIds.has(row.supplier_site_id)) return <Toggle value={val !== false} onChange={onChange} />
        return <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${val !== false ? 'bg-green-500/10 text-green-500' : 'bg-outline-variant/30 text-outline'}`}>{val !== false ? 'ACTIVE' : 'INACTIVE'}</span>
      }
    },
  ]

  const siteData = newSite ? [{ isNew: true, supplier_site_id: 'new', ...newSite }, ...sites] : sites

  return (
    <div className="h-[calc(100vh-6.5rem)] flex flex-col">
      <div className="flex items-center justify-between px-4 py-3 border-b border-outline-variant">
        <div className="flex items-center gap-4">
          <button type="button" onClick={() => navigate('/party/suppliers', { replace: true })}
            className="p-2 text-outline hover:text-primary transition-colors rounded-lg hover:bg-primary/5" title="Back to list">
            <span className="material-symbols-outlined !text-[20px]">arrow_back</span></button>
          <div>
            <h1 className="text-[32px] font-semibold leading-10 tracking-tight text-on-surface">
              {isEdit ? (existingSupplier?.supplier_code || 'Edit Supplier') : 'New Supplier'}</h1>
            <p className="text-sm text-outline mt-1">Configure supplier details and sites</p>
          </div>
        </div>
        <button type="button" onClick={handleSave} disabled={saving}
          className="px-6 py-2 bg-primary text-primary-foreground text-[11px] font-semibold rounded-lg hover:brightness-110 active:scale-95 transition-all shadow-lg shadow-primary/20 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-1.5">
          <span className="material-symbols-outlined !text-[16px]">save</span>{saving ? 'Saving...' : 'Save'}</button>
      </div>

      <div className="flex-1 overflow-y-auto">
        <div className="bg-surface-container rounded-xl border border-outline-variant overflow-hidden m-4">
          <Tabs tabs={formTabs} activeTab={headerTab} onTabChange={setHeaderTab} />
          <div className="p-6">
            {headerTab === 'basic' && (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
                <div><Fld label="Supplier Code" required><Inp value={form.supplier_code} onChange={v => updateForm({ supplier_code: v })} placeholder="e.g. SUP-001" /></Fld></div>
                <div><Fld label="Currency"><Sel value={form.currency_code} onChange={v => updateForm({ currency_code: v })} options={CURRENCIES} label="-- Select --" /></Fld></div>
                <div><Fld label="Payment Term (Days)"><Inp value={form.payment_term_days} onChange={v => updateForm({ payment_term_days: v })} type="number" placeholder="30" /></Fld></div>
                <div><Fld label="Vendor Type"><Sel value={form.vendor_type_lookup_code} onChange={v => updateForm({ vendor_type_lookup_code: v })} options={VENDOR_TYPES} /></Fld></div>
                <div><Fld label="Payment Method"><Sel value={form.payment_method_code} onChange={v => updateForm({ payment_method_code: v })} options={PAYMENT_METHODS} /></Fld></div>
                <div className="flex items-center gap-3 pt-6">
                  <label className="text-[10px] text-on-surface-variant font-semibold tracking-wider uppercase">Active</label>
                  <Toggle value={form.is_active} onChange={v => updateForm({ is_active: v })} />
                </div>
              </div>
            )}
            {headerTab === 'details' && (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
                <div><Fld label="Supplier Code"><Inp value={form.supplier_code} onChange={v => updateForm({ supplier_code: v })} placeholder="Code" /></Fld></div>
                <div><Fld label="Currency"><Sel value={form.currency_code} onChange={v => updateForm({ currency_code: v })} options={CURRENCIES} label="-- Select --" /></Fld></div>
                <div><Fld label="Payment Term (Days)"><Inp value={form.payment_term_days} onChange={v => updateForm({ payment_term_days: v })} type="number" placeholder="30" /></Fld></div>
                <div><Fld label="Vendor Type"><Sel value={form.vendor_type_lookup_code} onChange={v => updateForm({ vendor_type_lookup_code: v })} options={VENDOR_TYPES} /></Fld></div>
                <div><Fld label="Payment Method"><Sel value={form.payment_method_code} onChange={v => updateForm({ payment_method_code: v })} options={PAYMENT_METHODS} /></Fld></div>
                <div className="flex items-center gap-3 pt-6">
                  <label className="text-[10px] text-on-surface-variant font-semibold tracking-wider uppercase">Active</label>
                  <Toggle value={form.is_active} onChange={v => updateForm({ is_active: v })} />
                </div>
              </div>
            )}
          </div>
        </div>

        {isEdit && (
          <div className="mx-4 mb-4">
            <InteractiveGrid
              title={`${sites.length} Supplier Site(s)`}
              columns={siteColumns}
              data={siteData}
              idKey="supplier_site_id"
              searchable
              selectedIds={selectedSiteIds}
              onSelect={(id) => { const n = new Set(selectedSiteIds); n.has(id) ? n.delete(id) : n.add(id); setSelectedSiteIds(n) }}
              onSelectAll={() => { if (selectedSiteIds.size === sites.length && sites.length > 0) setSelectedSiteIds(new Set()); else setSelectedSiteIds(new Set(sites.map(r => r.supplier_site_id))) }}
              onEditToolbar={() => { const n = new Set(editingSiteIds); selectedSiteIds.forEach(id => n.add(id)); setEditingSiteIds(n) }}
              onAddRow={() => setNewSite({ site_name: '', site_number: '', address_id: '', is_primary: false, is_active: true })}
              onSave={newSite ? () => siteCreate(newSite) : undefined}
              onReset={() => setNewSite(null)}
              onDelete={(row) => { if (!row.isNew && confirm('Remove this site?')) siteDelete(row.supplier_site_id) }}
              onEdit={(row) => { const n = new Set(editingSiteIds); n.add(row.supplier_site_id); setEditingSiteIds(n) }}
              addLabel="Add Site"
              loading={sitesLoading}
              tableHeight="calc(100vh - 520px)"
            />
          </div>
        )}
      </div>
    </div>
  )
}
