import { useState, useEffect, useCallback } from 'react'
import api from '../../../api/client'
import { InteractiveGrid } from '../../../shared-ui-kit/components/ui/InteractiveGrid'
import { TreeGrid } from '../../../shared-ui-kit/components/ui/TreeGrid'
import { StatusChip } from '../../../shared-ui-kit/components/ui/StatusChip'
import { LovSection } from '../../../shared-ui-kit/components/ui/LovSection'
import PermissionGuard from '../../../components/PermissionGuard'

const BOM_STATUS_MAP = {
  'DRAFT': 'created',
  'PENDING_APPROVAL': 'pending',
  'ACTIVE': 'active',
  'INACTIVE': 'cancelled',
}

const COLUMNS = [
  { key: 'item_code', header: 'Item Number', width: '140px' },
  { key: 'revision', header: 'Revision', width: '100px' },
  { 
    key: 'status', 
    header: 'Status', 
    width: '140px',
    render: (row) => (
      <StatusChip 
        status={BOM_STATUS_MAP[row.status] || 'created'} 
        label={row.status} 
      />
    )
  },
  { key: 'effective_date_from', header: 'Effective From', width: '130px' },
  { key: 'effective_date_to', header: 'Effective To', width: '130px' },
]

const EMPTY_FORM = {
  item_id: '',
  revision: '',
  alternate_bom_code: '',
  effective_date_from: '',
  effective_date_to: '',
}

export default function BomPage() {
  const [bomHeaders, setBomHeaders] = useState([])
  const [loading, setLoading] = useState(false)
  const [selectedBom, setSelectedBom] = useState(null)
  const [explodedData, setExplodedData] = useState([])
  const [exploding, setExploding] = useState(false)
  const [approving, setApproving] = useState(false)
  const [items, setItems] = useState([])
  const [modalOpen, setModalOpen] = useState(false)
  const [editingBom, setEditingBom] = useState(null)
  const [form, setForm] = useState({ ...EMPTY_FORM })
  const [saving, setSaving] = useState(false)
  const [lovOpen, setLovOpen] = useState(false)

  const fetchBomHeaders = useCallback(async () => {
    setLoading(true)
    try {
      const { data } = await api.get('/bom/bom-headers', { 
        params: { page: 1, page_size: 100 } 
      })
      setBomHeaders(data.items || [])
    } catch (err) {
      console.error('Failed to fetch BOM headers:', err)
    } finally {
      setLoading(false)
    }
  }, [])

  const fetchItems = useCallback(async () => {
    try {
      const { data } = await api.get('/item/items', { params: { page: 1, page_size: 100 } })
      setItems(data.items || [])
    } catch (err) {
      console.error('Failed to fetch items:', err)
    }
  }, [])

  const fetchExplodedView = useCallback(async (bomHeaderId) => {
    if (!bomHeaderId) {
      setExplodedData([])
      return
    }
    setExploding(true)
    try {
      const { data } = await api.get(`/bom/bom-headers/${bomHeaderId}/explode`, {
        params: { quantity: 1.0 }
      })
      setExplodedData(data || [])
    } catch (err) {
      console.error('Failed to explode BOM:', err)
      setExplodedData([])
    } finally {
      setExploding(false)
    }
  }, [])

  const handleApprove = async () => {
    if (!selectedBom) return
    setApproving(true)
    try {
      await api.post(`/bom/bom-headers/${selectedBom.bom_header_id}/approve`)
      await fetchBomHeaders()
      const { data } = await api.get(`/bom/bom-headers/${selectedBom.bom_header_id}`)
      setSelectedBom(data)
    } catch (err) {
      console.error('Failed to approve BOM:', err)
      alert(err.response?.data?.detail?.message || 'Failed to approve BOM')
    } finally {
      setApproving(false)
    }
  }

  const handleRowClick = useCallback((row) => {
    setSelectedBom(row)
    fetchExplodedView(row.bom_header_id)
  }, [fetchExplodedView])

  const openAddModal = () => {
    setEditingBom(null)
    setForm({ ...EMPTY_FORM, effective_date_from: new Date().toISOString().slice(0, 10) })
    setModalOpen(true)
  }

  const openEditModal = (row) => {
    setEditingBom(row)
    setForm({
      item_id: row.item_id || '',
      revision: row.revision || '',
      alternate_bom_code: row.alternate_bom_code || '',
      effective_date_from: row.effective_date_from || '',
      effective_date_to: row.effective_date_to || '',
    })
    setModalOpen(true)
  }

  const closeModal = () => {
    setModalOpen(false)
    setEditingBom(null)
    setForm({ ...EMPTY_FORM })
  }

  const handleFormChange = (field, value) => {
    setForm(prev => ({ ...prev, [field]: value }))
  }

  const handleSave = async () => {
    if (!form.item_id || !form.revision || !form.effective_date_from) {
      alert('Please fill in required fields: Item, Revision, Effective From')
      return
    }
    setSaving(true)
    try {
      const payload = {
        item_id: form.item_id,
        revision: form.revision,
        alternate_bom_code: form.alternate_bom_code || null,
        effective_date_from: form.effective_date_from,
        effective_date_to: form.effective_date_to || null,
      }
      if (editingBom) {
        await api.put(`/bom/bom-headers/${editingBom.bom_header_id}`, payload)
      } else {
        await api.post('/bom/bom-headers', payload)
      }
      closeModal()
      await fetchBomHeaders()
    } catch (err) {
      alert(err.response?.data?.detail?.message || 'Failed to save BOM header')
    } finally {
      setSaving(false)
    }
  }

  const handleDelete = async (row) => {
    if (!confirm(`Delete BOM revision ${row.revision} for item ${row.item_code || row.item_id}?`)) return
    try {
      await api.delete(`/bom/bom-headers/${row.bom_header_id}`)
      if (selectedBom?.bom_header_id === row.bom_header_id) {
        setSelectedBom(null)
        setExplodedData([])
      }
      await fetchBomHeaders()
    } catch (err) {
      alert(err.response?.data?.detail?.message || 'Failed to delete BOM header')
    }
  }

  useEffect(() => {
    fetchBomHeaders()
    fetchItems()
  }, [fetchBomHeaders, fetchItems])

  const convertToTreeNodes = (items, parentId = 'root') => {
    if (!items || items.length === 0) return []
    return items.map((item, index) => {
      const nodeId = `${parentId}-${item.component_item_id}-${index}`
      return {
        id: nodeId,
        data: { ...item, level: item.level || 0 },
        children: item.children && item.children.length > 0 
          ? convertToTreeNodes(item.children, nodeId) : []
      }
    })
  }

  const treeData = convertToTreeNodes(explodedData)

  const treeColumns = [
    {
      id: 'item_code', header: 'Item Code', width: '120px',
      render: (row) => row.item_code || '-'
    },
    {
      id: 'quantity_per', header: 'Quantity', width: '100px', align: 'right',
      render: (row) => <span className="font-mono">{row.quantity_per?.toFixed(2) || '0.00'}</span>
    },
    {
      id: 'uom_code', header: 'UOM', width: '80px',
      render: (row) => row.uom_code || '-'
    },
    {
      id: 'level', header: 'Level', width: '80px', align: 'center',
      render: (row) => (
        <span className="px-2 py-0.5 bg-primary/10 text-primary rounded text-xs font-semibold">L{row.level}</span>
      )
    },
  ]

  const detailHeader = (
    <div className="flex items-center justify-between px-4 py-3 bg-surface-container-low border-b border-outline-variant">
      <div className="flex items-center gap-3">
        <span className="text-sm font-semibold text-on-surface">BOM Details</span>
        {selectedBom && (
          <StatusChip status={BOM_STATUS_MAP[selectedBom.status] || 'created'} label={selectedBom.status} />
        )}
      </div>
      {selectedBom && selectedBom.status === 'PENDING_APPROVAL' && (
        <PermissionGuard module="bom" action="approve" fallback="disable" tooltip="คุณไม่มีสิทธิ์อนุมัติ BOM">
          <button onClick={handleApprove} disabled={approving}
            className="px-4 py-1.5 bg-success text-white rounded-lg text-xs font-semibold hover:bg-success/90 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center gap-2">
            {approving ? (
              <><span className="material-symbols-outlined text-[16px] animate-spin">progress_activity</span> Approving...</>
            ) : (
              <><span className="material-symbols-outlined text-[16px]">check_circle</span> Approve BOM</>
            )}
          </button>
        </PermissionGuard>
      )}
    </div>
  )

  return (
    <div className="p-6 space-y-4">
      <div>
        <h1 className="text-2xl font-bold text-on-surface">Bill of Materials</h1>
        <p className="text-sm text-outline mt-1">Manage BOM structures and multi-level component hierarchies</p>
      </div>

      <div className="border border-outline-variant rounded-xl overflow-hidden bg-surface-container-lowest">
        <InteractiveGrid
          columns={COLUMNS}
          data={bomHeaders}
          loading={loading}
          idKey="bom_header_id"
          searchable
          onRowClick={handleRowClick}
          selectedIds={selectedBom ? new Set([selectedBom.bom_header_id]) : new Set()}
          onAddRow={openAddModal}
          onEdit={openEditModal}
          onDelete={handleDelete}
          addLabel="Add BOM"
          tableHeight="calc(100vh - 280px)"
        />
      </div>

      {selectedBom && (
        <div className="border border-outline-variant rounded-xl overflow-hidden bg-surface-container-lowest">
          {detailHeader}
          <div className="p-4 bg-surface-container-lowest border-b border-outline-variant">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              <div>
                <div className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">BOM ID</div>
                <div className="text-xs text-on-surface font-mono">{selectedBom.bom_header_id}</div>
              </div>
              <div>
                <div className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">Item Number</div>
                <div className="text-xs text-on-surface font-semibold">{selectedBom.item_code || selectedBom.item_id}</div>
              </div>
              <div>
                <div className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">Revision</div>
                <div className="text-xs text-on-surface font-semibold">{selectedBom.revision}</div>
              </div>
              <div>
                <div className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">Alternate Code</div>
                <div className="text-xs text-on-surface">{selectedBom.alternate_bom_code || '-'}</div>
              </div>
            </div>
          </div>
          <div className="px-4 py-2 bg-surface-container-low border-b border-outline-variant">
            <div className="flex items-center gap-2">
              <span className="material-symbols-outlined text-primary text-[18px]">account_tree</span>
              <span className="text-sm font-semibold text-on-surface">Multi-Level Structure (Exploded View)</span>
            </div>
          </div>
          <div className="h-[400px] overflow-auto">
            {exploding ? (
              <div className="flex items-center justify-center py-12">
                <div className="flex items-center gap-3 text-outline">
                  <span className="material-symbols-outlined text-[24px] animate-spin">progress_activity</span>
                  <span className="text-sm">Loading BOM structure...</span>
                </div>
              </div>
            ) : treeData.length > 0 ? (
              <TreeGrid data={treeData} columns={treeColumns}
                nodeLabelAccessor={(row) => row.item_name || 'Unnamed Item'}
                nodeIconAccessor={(row) => row.children && row.children.length > 0 ? 'inventory_2' : 'inventory'}
                nodeDescriptionAccessor={(row) => `Component: ${row.item_code || row.component_item_id}`}
              />
            ) : (
              <div className="flex flex-col items-center justify-center py-12 text-outline">
                <span className="material-symbols-outlined text-[48px] mb-2">account_tree</span>
                <p className="text-sm">No components found in this BOM</p>
                <p className="text-xs mt-1">Add components to see the structure</p>
              </div>
            )}
          </div>
        </div>
      )}

      {modalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40" onClick={closeModal}>
          <div className="bg-surface-container-highest rounded-xl shadow-xl max-w-lg w-full mx-4 p-6" onClick={e => e.stopPropagation()}>
            <div className="flex items-center justify-between mb-5">
              <h2 className="text-lg font-bold text-on-surface">
                {editingBom ? 'Edit BOM Header' : 'Add BOM Header'}
              </h2>
              <button onClick={closeModal} className="text-outline hover:text-on-surface">
                <span className="material-symbols-outlined">close</span>
              </button>
            </div>

            <div className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-outline mb-1">Item *</label>
                <button type="button" onClick={() => setLovOpen(true)}
                  className="w-full px-3 py-2 bg-surface-container-lowest border border-outline-variant rounded-lg text-sm text-left focus:border-primary focus:ring-1 focus:ring-primary flex items-center justify-between">
                  <span className={form.item_id ? 'text-on-surface' : 'text-outline'}>
                    {form.item_id ? items.find(i => i.item_id === form.item_id)?.item_code + ' - ' + items.find(i => i.item_id === form.item_id)?.item_name : '-- Select Item --'}
                  </span>
                  <span className="material-symbols-outlined text-[18px] text-outline">search</span>
                </button>
                {form.item_id && (
                  <button type="button" onClick={() => handleFormChange('item_id', '')}
                    className="mt-1 text-xs text-outline hover:text-on-surface">
                    Clear
                  </button>
                )}
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-semibold text-outline mb-1">Revision *</label>
                  <input type="text" value={form.revision} onChange={e => handleFormChange('revision', e.target.value)}
                    className="w-full px-3 py-2 bg-surface-container-lowest border border-outline-variant rounded-lg text-sm text-on-surface focus:border-primary focus:ring-1 focus:ring-primary"
                    placeholder="e.g. A" />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-outline mb-1">Alternate Code</label>
                  <input type="text" value={form.alternate_bom_code} onChange={e => handleFormChange('alternate_bom_code', e.target.value)}
                    className="w-full px-3 py-2 bg-surface-container-lowest border border-outline-variant rounded-lg text-sm text-on-surface focus:border-primary focus:ring-1 focus:ring-primary"
                    placeholder="e.g. ALT-001" />
                </div>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-semibold text-outline mb-1">Effective From *</label>
                  <input type="date" value={form.effective_date_from} onChange={e => handleFormChange('effective_date_from', e.target.value)}
                    className="w-full px-3 py-2 bg-surface-container-lowest border border-outline-variant rounded-lg text-sm text-on-surface focus:border-primary focus:ring-1 focus:ring-primary" />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-outline mb-1">Effective To</label>
                  <input type="date" value={form.effective_date_to} onChange={e => handleFormChange('effective_date_to', e.target.value)}
                    className="w-full px-3 py-2 bg-surface-container-lowest border border-outline-variant rounded-lg text-sm text-on-surface focus:border-primary focus:ring-1 focus:ring-primary" />
                </div>
              </div>
            </div>

            <div className="flex justify-end gap-3 mt-6 pt-4 border-t border-outline-variant">
              <button onClick={closeModal}
                className="px-4 py-2 text-sm font-semibold text-on-surface bg-surface-container-low border border-outline-variant rounded-lg hover:bg-surface-container-high transition-colors">
                Cancel
              </button>
              <button onClick={handleSave} disabled={saving}
                className="px-4 py-2 text-sm font-semibold text-white bg-primary rounded-lg hover:bg-primary/90 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center gap-2">
                {saving ? (
                  <><span className="material-symbols-outlined text-[16px] animate-spin">progress_activity</span> Saving...</>
                ) : (
                  <><span className="material-symbols-outlined text-[16px]">save</span> {editingBom ? 'Update' : 'Create'}</>
                )}
              </button>
            </div>
          </div>
        </div>
      )}

      <LovSection
        isOpen={lovOpen}
        onClose={() => setLovOpen(false)}
        onSelect={(row) => {
          handleFormChange('item_id', row.item_id)
          setLovOpen(false)
        }}
        title="Item"
        columns={[
          { key: 'item_code', header: 'Item Code', width: '120px' },
          { key: 'item_name', header: 'Item Name', width: '200px' },
          { key: 'item_type', header: 'Type', width: '100px' },
        ]}
        data={items}
        searchOptions={[
          { key: 'item_code', label: 'Item Code' },
          { key: 'item_name', label: 'Item Name' },
        ]}
      />
    </div>
  )
}
