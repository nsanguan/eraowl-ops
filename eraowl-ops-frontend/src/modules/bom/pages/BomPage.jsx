import { useState, useEffect, useCallback } from 'react'
import api from '../../../api/client'
import { InteractiveGrid } from '../../../shared-ui-kit/components/ui/InteractiveGrid'
import { TreeGrid } from '../../../shared-ui-kit/components/ui/TreeGrid'
import { StatusChip } from '../../../shared-ui-kit/components/ui/StatusChip'
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

export default function BomPage() {
  const [bomHeaders, setBomHeaders] = useState([])
  const [loading, setLoading] = useState(false)
  const [selectedBom, setSelectedBom] = useState(null)
  const [explodedData, setExplodedData] = useState([])
  const [exploding, setExploding] = useState(false)
  const [approving, setApproving] = useState(false)

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

  useEffect(() => {
    fetchBomHeaders()
  }, [fetchBomHeaders])

  const convertToTreeNodes = (items, parentId = 'root') => {
    if (!items || items.length === 0) return []
    
    return items.map((item, index) => {
      const nodeId = `${parentId}-${item.component_item_id}-${index}`
      const node = {
        id: nodeId,
        data: {
          ...item,
          level: item.level || 0,
        },
        children: item.children && item.children.length > 0 
          ? convertToTreeNodes(item.children, nodeId)
          : []
      }
      return node
    })
  }

  const treeData = convertToTreeNodes(explodedData)

  const treeColumns = [
    {
      id: 'item_code',
      header: 'Item Code',
      width: '120px',
      render: (row) => row.item_code || '-'
    },
    {
      id: 'quantity_per',
      header: 'Quantity',
      width: '100px',
      align: 'right',
      render: (row) => (
        <span className="font-mono">{row.quantity_per?.toFixed(2) || '0.00'}</span>
      )
    },
    {
      id: 'uom_code',
      header: 'UOM',
      width: '80px',
      render: (row) => row.uom_code || '-'
    },
    {
      id: 'level',
      header: 'Level',
      width: '80px',
      align: 'center',
      render: (row) => (
        <span className="px-2 py-0.5 bg-primary/10 text-primary rounded text-xs font-semibold">
          L{row.level}
        </span>
      )
    },
  ]

  const detailHeader = (
    <div className="flex items-center justify-between px-4 py-3 bg-surface-container-low border-b border-outline-variant">
      <div className="flex items-center gap-3">
        <span className="text-sm font-semibold text-on-surface">BOM Details</span>
        {selectedBom && (
          <StatusChip 
            status={BOM_STATUS_MAP[selectedBom.status] || 'created'} 
            label={selectedBom.status} 
          />
        )}
      </div>
      
      {selectedBom && selectedBom.status === 'PENDING_APPROVAL' && (
        <PermissionGuard
          module="bom"
          action="approve"
          fallback="disable"
          tooltip="คุณไม่มีสิทธิ์อนุมัติ BOM"
        >
          <button
            onClick={handleApprove}
            disabled={approving}
            className="px-4 py-1.5 bg-success text-white rounded-lg text-xs font-semibold hover:bg-success/90 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center gap-2"
          >
            {approving ? (
              <>
                <span className="material-symbols-outlined text-[16px] animate-spin">progress_activity</span>
                Approving...
              </>
            ) : (
              <>
                <span className="material-symbols-outlined text-[16px]">check_circle</span>
                Approve BOM
              </>
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
        <p className="text-sm text-outline mt-1">
          Manage BOM structures and multi-level component hierarchies
        </p>
      </div>

      <div className="border border-outline-variant rounded-xl overflow-hidden bg-surface-container-lowest">
        <InteractiveGrid
          columns={COLUMNS}
          data={bomHeaders}
          loading={loading}
          idKey="bom_header_id"
          searchable
          onRowClick={handleRowClick}
          selectedIds={selectedBom ? [selectedBom.bom_header_id] : []}
          tableHeight="calc(100vh - 280px)"
        />
      </div>

      {selectedBom && (
        <div className="border border-outline-variant rounded-xl overflow-hidden bg-surface-container-lowest">
          {detailHeader}
          
          <div className="p-4 bg-surface-container-lowest border-b border-outline-variant">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              <div>
                <div className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">
                  BOM ID
                </div>
                <div className="text-xs text-on-surface font-mono">
                  {selectedBom.bom_header_id}
                </div>
              </div>
              <div>
                <div className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">
                  Item Number
                </div>
                <div className="text-xs text-on-surface font-semibold">
                  {selectedBom.item_code || selectedBom.item_id}
                </div>
              </div>
              <div>
                <div className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">
                  Revision
                </div>
                <div className="text-xs text-on-surface font-semibold">
                  {selectedBom.revision}
                </div>
              </div>
              <div>
                <div className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1">
                  Alternate Code
                </div>
                <div className="text-xs text-on-surface">
                  {selectedBom.alternate_bom_code || '-'}
                </div>
              </div>
            </div>
          </div>

          <div className="px-4 py-2 bg-surface-container-low border-b border-outline-variant">
            <div className="flex items-center gap-2">
              <span className="material-symbols-outlined text-primary text-[18px]">
                account_tree
              </span>
              <span className="text-sm font-semibold text-on-surface">
                Multi-Level Structure (Exploded View)
              </span>
            </div>
          </div>
          
          <div className="h-[400px] overflow-auto">
            {exploding ? (
              <div className="flex items-center justify-center py-12">
                <div className="flex items-center gap-3 text-outline">
                  <span className="material-symbols-outlined text-[24px] animate-spin">
                    progress_activity
                  </span>
                  <span className="text-sm">Loading BOM structure...</span>
                </div>
              </div>
            ) : treeData.length > 0 ? (
              <TreeGrid
                data={treeData}
                columns={treeColumns}
                nodeLabelAccessor={(row) => row.item_name || 'Unnamed Item'}
                nodeIconAccessor={(row) => 
                  row.children && row.children.length > 0 ? 'inventory_2' : 'inventory'
                }
                nodeDescriptionAccessor={(row) => `Component: ${row.item_code || row.component_item_id}`}
              />
            ) : (
              <div className="flex flex-col items-center justify-center py-12 text-outline">
                <span className="material-symbols-outlined text-[48px] mb-2">
                  account_tree
                </span>
                <p className="text-sm">No components found in this BOM</p>
                <p className="text-xs mt-1">Add components to see the structure</p>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  )
}
