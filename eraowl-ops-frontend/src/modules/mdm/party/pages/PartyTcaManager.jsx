import { useState, useEffect, useCallback, useRef } from 'react'
import api from '../../../../api/client'
import { MasterDetailSplit } from '../../../../shared-ui-kit/components/ui/MasterDetailSplit'

const PARTY_TYPE_OPTIONS = ['ALL', 'ORGANIZATION', 'PERSON']
const SITE_USE_OPTIONS = ['BILL_TO', 'SHIP_TO', 'PAY_TO', 'OFFICE']

function TreeNode({ node, depth = 0, selected, onSelect, onToggle, expanded }) {
  const hasChildren = node.children?.length > 0
  const isOpen = expanded[node.node_id]
  const isSelected = selected === node.node_id
  const padLeft = depth * 20
  const iconMap = { profile: 'badge', role_group: 'assignment_ind', role_item: 'check_circle', site_group: 'location_on', site_item: 'pin_drop', site_use: 'flag' }
  return (
    <div>
      <div onClick={() => { if (hasChildren) onToggle(node.node_id); onSelect(node) }}
        className={`flex items-center gap-2 px-3 py-2 cursor-pointer transition-all rounded-lg mx-1 text-sm ${isSelected ? 'bg-primary/10 text-primary font-semibold shadow-sm' : 'text-on-surface hover:bg-surface-container-low'} ${depth === 0 ? 'mt-1' : ''}`}
        style={{ paddingLeft: `${12 + padLeft}px` }}>
        {hasChildren ? <span className={`material-symbols-outlined text-[16px] text-outline transition-transform ${isOpen ? 'rotate-90' : ''}`}>chevron_right</span> : <span className="w-4" />}
        <span className="material-symbols-outlined text-[16px]" style={{ color: isSelected ? 'var(--color-primary)' : 'var(--color-outline)' }}>{iconMap[node.node_type] || 'circle'}</span>
        <span className="flex-1 truncate">{node.label}</span>
        {node.node_type === 'site_use' && node.entity?.is_primary && <span className="text-[10px] px-1.5 py-0.5 rounded-full bg-success/10 text-success font-semibold">PRIMARY</span>}
      </div>
      {hasChildren && isOpen && (
        <div className="border-l-2 border-outline-variant/30 ml-5">
          {node.children.map((child) => <TreeNode key={child.node_id} node={child} depth={depth + 1} selected={selected} onSelect={onSelect} onToggle={onToggle} expanded={expanded} />)}
        </div>
      )}
    </div>
  )
}

function FormSkeleton() {
  return <div className="space-y-3 animate-pulse">{Array.from({ length: 4 }).map((_, i) => <div key={i} className="h-9 bg-surface-container-high rounded-lg" />)}</div>
}

export default function PartyTcaManager() {
  const [parties, setParties] = useState([])
  const [loading, setLoading] = useState(true)
  const [selectedParty, setSelectedParty] = useState(null)
  const [treeData, setTreeData] = useState([])
  const [treeLoading, setTreeLoading] = useState(false)
  const [expanded, setExpanded] = useState({})
  const [selectedNode, setSelectedNode] = useState(null)
  const [savingNode, setSavingNode] = useState(false)
  const [showAddRole, setShowAddRole] = useState(false)
  const [showAddSite, setShowAddSite] = useState(false)
  const [addSiteForm, setAddSiteForm] = useState({ country: 'Thailand', address_line1: '', city: '', site_name: '' })
  const [partyFilter, setPartyFilter] = useState('ALL')
  const [searchQuery, setSearchQuery] = useState('')

  // Guard against stale async responses
  const fetchIdRef = useRef(0)
  const selectedNodeRef = useRef(null)
  const detailPanelRef = useRef(null)

  const fetchParties = useCallback(async () => {
    setLoading(true)
    try {
      const { data } = await api.get('/party/parties', { params: { page: 1, page_size: 100 } })
      console.log('Fetched parties:', data?.items?.length || 0, 'items')
      setParties(data?.items || [])
    } catch (err) {
      console.error('Failed to fetch parties:', err)
    } finally {
      setLoading(false)
    }
  }, [])

  const fetchTree = useCallback(async (partyId, preserveNodeId) => {
    if (!partyId) return
    const id = ++fetchIdRef.current
    setTreeLoading(true)
    console.log(`[fetchTree #${id}] START for party ${partyId}, preserveNode=${preserveNodeId}`)
    try {
      const { data } = await api.get(`/party/parties/${partyId}/tree`)
      // Ignore stale response from a previous/faster request
      if (id !== fetchIdRef.current) {
        console.log(`[fetchTree #${id}] STALE — skipping, latest is #${fetchIdRef.current}`)
        return
      }
      console.log(`[fetchTree #${id}] SUCCESS — tree nodes:`, data?.tree?.length)
      setTreeData(data?.tree || [])
      if (preserveNodeId && selectedNodeRef.current) {
        const find = (nodes) => {
          for (const n of nodes) {
            if (n.node_id === preserveNodeId) return n
            if (n.children) { const f = find(n.children); if (f) return f }
          }
          return null
        }
        const restored = find(data?.tree || [])
        if (restored) {
          console.log(`[fetchTree #${id}] Restored node: ${restored.node_id}`)
          setSelectedNode(restored)
        }
      }
    } catch (err) {
      console.error(`[fetchTree #${id}] FAILED:`, err)
      if (id === fetchIdRef.current) setTreeData([])
    } finally {
      if (id === fetchIdRef.current) setTreeLoading(false)
    }
  }, [])

  useEffect(() => { fetchParties() }, [fetchParties])

  // Party change — resets only when party_id actually differs
  useEffect(() => {
    if (!selectedParty) return
    const partyId = selectedParty.party_id
    console.log('Party changed to:', partyId)
    setSelectedNode(null)
    selectedNodeRef.current = null
    setExpanded({})
    setTreeData([])
    // Reset right-panel scroll to top
    if (detailPanelRef.current) detailPanelRef.current.scrollTop = 0
    fetchTree(partyId)
  }, [selectedParty?.party_id])

  const handleTreeNodeSelect = (node) => {
    console.log('Tree node selected:', node?.node_id, node?.node_type)
    setSelectedNode(node)
    selectedNodeRef.current = node?.node_id || null
  }

  const handleTreeSave = async (nodeType, action, entity) => {
    setSavingNode(true)
    try {
      const { data } = await api.post(`/party/parties/${selectedParty.party_id}/tree/update-node`, { node_type: nodeType, action, entity })
      console.log('Tree save OK:', nodeType, action, data)
      await fetchTree(selectedParty.party_id, selectedNodeRef.current)
    } catch (err) {
      console.error('Tree save failed:', err)
      alert(err.response?.data?.detail?.message || 'Failed to update')
    } finally {
      setSavingNode(false)
    }
  }

  const handleTreeDelete = async (node) => {
    if (node.node_type === 'role_item') await handleTreeSave('role_item', 'delete', { party_role_id: node.entity?.party_role_id })
    else if (node.node_type === 'site_item') await handleTreeSave('site_item', 'delete', { party_site_id: node.entity?.party_site_id })
    else if (node.node_type === 'site_use') await handleTreeSave('site_use', 'delete', { site_use_id: node.entity?.site_use_id })
  }

  const handleAddRole = async (roleType) => {
    setSavingNode(true)
    try {
      await api.post(`/party/parties/${selectedParty.party_id}/tree/update-node`, { node_type: 'role_item', action: 'add', entity: { role_type: roleType } })
      console.log('Role added:', roleType)
      await fetchTree(selectedParty.party_id, selectedNodeRef.current)
      setShowAddRole(false)
    } catch (err) {
      console.error('Add role failed:', err)
      alert(err.response?.data?.detail?.message || 'Failed to add role')
    } finally { setSavingNode(false) }
  }

  const handleAddSite = async () => {
    setSavingNode(true)
    try {
      await api.post(`/party/parties/${selectedParty.party_id}/tree/update-node`, { node_type: 'site_item', action: 'add', entity: addSiteForm })
      console.log('Site added:', addSiteForm.site_name)
      await fetchTree(selectedParty.party_id, selectedNodeRef.current)
      setShowAddSite(false)
      setAddSiteForm({ country: 'Thailand', address_line1: '', city: '', site_name: '' })
    } catch (err) {
      console.error('Add site failed:', err)
      alert(err.response?.data?.detail?.message || 'Failed to add site')
    } finally { setSavingNode(false) }
  }

  const filteredParties = parties.filter((p) => {
    if (partyFilter !== 'ALL' && p.party_type !== partyFilter) return false
    return true
  }).filter((p) => !searchQuery || p.party_name?.toLowerCase().includes(searchQuery.toLowerCase()) || p.party_number?.toLowerCase().includes(searchQuery.toLowerCase()))

  const renderForm = () => {
    if (savingNode) return <FormSkeleton />
    if (!selectedNode) return (
      <div className="flex flex-col items-center justify-center h-full text-outline">
        <span className="material-symbols-outlined text-[48px]">touch_app</span>
        <p className="text-sm mt-2">Select a tree node to manage</p>
      </div>
    )
    const nt = selectedNode.node_type
    if (nt === 'profile') return <ProfileForm node={selectedNode} onSave={handleTreeSave} onCancel={() => setSelectedNode(null)} />
    if (nt === 'role_item') return <RoleForm node={selectedNode} onDelete={handleTreeDelete} onCancel={() => setSelectedNode(null)} />
    if (nt === 'site_item') return <SiteForm node={selectedNode} onSave={handleTreeSave} onDelete={handleTreeDelete} onCancel={() => setSelectedNode(null)} />
    if (nt === 'site_use') return <SiteUseForm node={selectedNode} onSave={handleTreeSave} onDelete={handleTreeDelete} onCancel={() => setSelectedNode(null)} />
    return <div className="text-sm text-outline p-4">Select a node to edit</div>
  }

  return (
    <div className="h-[calc(100vh-6.5rem)]">
    <MasterDetailSplit masterWidth="320px"
      masterContent={
        <div className="h-full flex flex-col">
          <div className="p-4 border-b border-outline-variant space-y-3">
            <h2 className="text-sm font-bold text-on-surface">Trading Community</h2>
            <input type="text" value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} placeholder="Search by name or number..."
              className="w-full px-3 py-2 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none" />
            <div className="flex gap-2">
              <select value={partyFilter} onChange={(e) => setPartyFilter(e.target.value)} className="flex-1 px-2 py-1.5 bg-surface-bright border border-outline-variant rounded-lg text-xs text-on-surface outline-none">
                {PARTY_TYPE_OPTIONS.map((o) => <option key={o} value={o}>{o === 'ALL' ? 'All Types' : o}</option>)}
              </select>
            </div>
          </div>
          <div className="flex-1 overflow-y-auto divide-y divide-outline-variant/30">
            {loading ? (
              <div className="flex items-center justify-center py-12 text-outline text-sm">Loading...</div>
            ) : filteredParties.length === 0 ? (
              <div className="flex items-center justify-center py-12 text-outline text-sm">No parties found.</div>
            ) : filteredParties.map((p) => (
              <button key={p.party_id} onClick={() => setSelectedParty(p)}
                className={`w-full text-left px-4 py-3 transition-colors hover:bg-surface-container-low ${selectedParty?.party_id === p.party_id ? 'bg-primary/5 border-l-2 border-primary' : 'border-l-2 border-transparent'}`}>
                <div className="text-sm font-semibold text-on-surface">{p.party_name}</div>
                <div className="flex items-center gap-2 mt-0.5">
                  <span className="text-[10px] text-outline font-mono">{p.party_number}</span>
                  <span className="text-[10px] px-1.5 py-0.5 rounded-full bg-primary/10 text-primary">{p.party_type}</span>
                </div>
              </button>
            ))}
          </div>
          <div className="p-3 border-t border-outline-variant text-[10px] text-outline text-center">{parties.length} parties</div>
        </div>
      }
      detailContent={
        <div className="h-full flex flex-col" key={selectedParty?.party_id || 'empty'}>
          {!selectedParty ? (
            <div className="flex items-center justify-center flex-1 text-outline text-sm">Select a party from the list</div>
          ) : (
            <div className="flex flex-1 overflow-hidden" ref={detailPanelRef}>
              <div className="w-1/2 border-r border-outline-variant overflow-y-auto p-3 bg-surface-container-lowest/50">
                <div className="flex items-center justify-between mb-2 px-1">
                  <h3 className="text-xs font-bold text-on-surface uppercase tracking-wider">TCA Tree</h3>
                  <button onClick={() => fetchTree(selectedParty.party_id, selectedNodeRef.current)} className="p-1 text-outline hover:text-primary rounded hover:bg-surface-container-high transition-colors">
                    <span className="material-symbols-outlined text-[16px]">refresh</span>
                  </button>
                </div>
                {treeLoading && treeData.length === 0 ? (
                  <div className="text-sm text-outline py-8 text-center">Loading tree...</div>
                ) : treeData.length > 0 ? (
                  <div className={treeLoading ? 'opacity-60 pointer-events-none transition-opacity' : ''}>
                    {treeData.map((node) => <TreeNode key={node.node_id} node={node} depth={0} selected={selectedNode?.node_id} onSelect={handleTreeNodeSelect} onToggle={(nid) => setExpanded((p) => ({ ...p, [nid]: !p[nid] }))} expanded={expanded} />)}
                  </div>
                ) : (
                  <div className="text-sm text-outline py-8 text-center">No tree data available</div>
                )}
                <div className="flex gap-2 mt-3 px-1">
                  <button onClick={() => setShowAddRole(true)} className="flex items-center gap-1 px-3 py-1.5 bg-primary/10 text-primary rounded-lg text-[10px] font-semibold hover:bg-primary/20 transition-colors">
                    <span className="material-symbols-outlined text-[14px]">add</span> Role
                  </button>
                  <button onClick={() => setShowAddSite(true)} className="flex items-center gap-1 px-3 py-1.5 bg-primary/10 text-primary rounded-lg text-[10px] font-semibold hover:bg-primary/20 transition-colors">
                    <span className="material-symbols-outlined text-[14px]">add_location</span> Site
                  </button>
                </div>
              </div>
              <div className="w-1/2 overflow-y-auto p-4 bg-surface-container-lowest">
                <h3 className="text-xs font-bold text-on-surface uppercase tracking-wider mb-3">{selectedNode?.label || 'Node Details'}</h3>
                {renderForm()}
              </div>
            </div>
          )}
        </div>
      }
    />

    {showAddRole && (
      <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40" onClick={() => setShowAddRole(false)}>
        <div className="bg-surface-container rounded-2xl border border-outline-variant shadow-2xl w-full max-w-sm p-5" onClick={(e) => e.stopPropagation()}>
          <h2 className="text-sm font-bold text-on-surface mb-3">Add Business Role</h2>
          <div className="space-y-2">
            {['SUPPLIER', 'CUSTOMER'].map((r) => (
              <button key={r} onClick={() => handleAddRole(r)}
                className="w-full flex items-center gap-3 px-4 py-3 bg-surface-container-lowest border border-outline-variant rounded-xl hover:bg-surface-container-low hover:border-primary/30 transition-all text-left">
                <span className="material-symbols-outlined text-[20px] text-primary">{r === 'SUPPLIER' ? 'conveyor_belt' : 'handshake'}</span>
                <div><div className="text-sm font-semibold text-on-surface">{r}</div><div className="text-[10px] text-outline">Register as a {r.toLowerCase()}</div></div>
              </button>
            ))}
          </div>
          <button onClick={() => setShowAddRole(false)} className="w-full mt-3 px-3 py-2 bg-surface-container-low border border-outline-variant rounded-xl text-xs font-semibold text-outline">Cancel</button>
        </div>
      </div>
    )}

    {showAddSite && (
      <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40" onClick={() => setShowAddSite(false)}>
        <div className="bg-surface-container rounded-2xl border border-outline-variant shadow-2xl w-full max-w-md p-5" onClick={(e) => e.stopPropagation()}>
          <h2 className="text-sm font-bold text-on-surface mb-3">Add New Site</h2>
          <div className="space-y-3">
            {['site_name', 'country', 'address_line1', 'city', 'state', 'postal_code'].map((f) => (
              <div key={f}>
                <label className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1 block">{f.replace(/_/g, ' ')}</label>
                <input type="text" value={addSiteForm[f] || ''} onChange={(e) => setAddSiteForm((p) => ({ ...p, [f]: e.target.value }))}
                  className="w-full px-3 py-2 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface outline-none focus:border-primary focus:ring-2 focus:ring-primary/20" />
              </div>
            ))}
          </div>
          <div className="flex justify-end gap-3 mt-5">
            <button onClick={() => setShowAddSite(false)} className="px-4 py-2 text-sm font-semibold text-on-surface-variant bg-surface-container-low border border-outline-variant rounded-xl">Cancel</button>
            <button onClick={handleAddSite} className="px-4 py-2 text-sm font-semibold text-white bg-primary rounded-xl hover:opacity-90">Create Site</button>
          </div>
        </div>
      </div>
    )}
    </div>
  )
}

function ProfileForm({ node, onSave, onCancel }) {
  const [form, setForm] = useState({ ...node.entity })
  const handleChange = (k, v) => setForm((p) => ({ ...p, [k]: v }))
  return (
    <div className="space-y-3">
      {['party_name', 'party_number', 'party_type', 'tax_reference'].map((f) => (
        <div key={f}>
          <label className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1 block">{f.replace('_', ' ')}</label>
          <input type="text" value={form[f] || ''} onChange={(e) => handleChange(f, e.target.value)} className="w-full px-3 py-2 bg-surface-bright border border-outline-variant rounded-lg text-sm text-on-surface outline-none focus:border-primary focus:ring-1 focus:ring-primary" />
        </div>
      ))}
      <div className="flex gap-2 pt-2">
        <button onClick={() => onSave('profile', 'update', form)} className="flex-1 px-3 py-2 bg-primary text-primary-foreground rounded-lg text-xs font-semibold hover:opacity-90">Save</button>
        <button onClick={onCancel} className="px-3 py-2 bg-surface-container-low border border-outline-variant rounded-lg text-xs font-semibold text-outline">Cancel</button>
      </div>
    </div>
  )
}

function RoleForm({ node, onDelete, onCancel }) {
  return (
    <div className="space-y-3">
      <div className="flex items-center gap-3 p-3 rounded-xl border border-outline-variant bg-surface-container-lowest">
        <span className="material-symbols-outlined text-[24px] text-primary">{node.label === 'SUPPLIER' ? 'conveyor_belt' : 'handshake'}</span>
        <div className="flex-1"><div className="text-sm font-semibold text-on-surface">{node.label} Account</div><div className="text-[10px] text-outline">Active role for this party</div></div>
        <span className="px-2 py-1 text-[10px] font-semibold rounded-full bg-success/10 text-success">ACTIVE</span>
      </div>
      <button onClick={() => { if (confirm(`Deactivate ${node.label} role?`)) onDelete(node) }}
        className="w-full px-3 py-2 bg-error/10 text-error rounded-lg text-xs font-semibold hover:bg-error/20 transition-colors flex items-center justify-center gap-2">
        <span className="material-symbols-outlined text-[16px]">block</span> Deactivate {node.label}
      </button>
      <button onClick={onCancel} className="w-full px-3 py-2 bg-surface-container-low border border-outline-variant rounded-lg text-xs font-semibold text-outline">Close</button>
    </div>
  )
}

function SiteForm({ node, onSave, onDelete, onCancel }) {
  const [form, setForm] = useState({ site_name: node.entity?.site_name || '', country: node.entity?.address?.country || '', address_line1: node.entity?.address?.address_line1 || '', city: node.entity?.address?.city || '', state: node.entity?.address?.state || '', postal_code: node.entity?.address?.postal_code || '' })
  return (
    <div className="space-y-3">
      {['site_name', 'country', 'address_line1', 'city', 'state', 'postal_code'].map((f) => (
        <div key={f}>
          <label className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1 block">{f.replace(/_/g, ' ')}</label>
          <input type="text" value={form[f] || ''} onChange={(e) => setForm((p) => ({ ...p, [f]: e.target.value }))} className="w-full px-3 py-2 bg-surface-bright border border-outline-variant rounded-lg text-sm text-on-surface outline-none focus:border-primary focus:ring-1 focus:ring-primary" />
        </div>
      ))}
      <div className="flex gap-2 pt-2">
        <button onClick={() => onSave('site_item', 'update', { ...form, party_site_id: node.entity?.party_site_id })} className="flex-1 px-3 py-2 bg-primary text-primary-foreground rounded-lg text-xs font-semibold hover:opacity-90">Save</button>
        <button onClick={() => { if (confirm('Delete this site?')) onDelete(node) }} className="px-3 py-2 bg-error/10 text-error rounded-lg text-xs font-semibold hover:bg-error/20">Delete</button>
        <button onClick={onCancel} className="px-3 py-2 bg-surface-container-low border border-outline-variant rounded-lg text-xs font-semibold text-outline">Cancel</button>
      </div>
    </div>
  )
}

function SiteUseForm({ node, onSave, onDelete, onCancel }) {
  const [useType, setUseType] = useState(node.entity?.site_use_type || 'BILL_TO')
  const [isPrimary, setIsPrimary] = useState(node.entity?.is_primary || false)
  return (
    <div className="space-y-3">
      <div>
        <label className="text-[10px] font-semibold uppercase tracking-wider text-outline mb-1 block">Site Use Type</label>
        <select value={useType} onChange={(e) => setUseType(e.target.value)} className="w-full px-3 py-2 bg-surface-bright border border-outline-variant rounded-lg text-sm text-on-surface outline-none">
          {SITE_USE_OPTIONS.map((o) => <option key={o} value={o}>{o}</option>)}
        </select>
      </div>
      <label className="flex items-center gap-2 text-sm text-on-surface cursor-pointer">
        <input type="checkbox" checked={isPrimary} onChange={(e) => setIsPrimary(e.target.checked)} className="accent-primary w-4 h-4" /> Primary {useType}
      </label>
      <div className="flex gap-2 pt-2">
        <button onClick={() => onSave('site_use', 'update', { site_use_id: node.entity?.site_use_id, site_use_type: useType, is_primary: isPrimary })} className="flex-1 px-3 py-2 bg-primary text-primary-foreground rounded-lg text-xs font-semibold hover:opacity-90">Save</button>
        <button onClick={() => { if (confirm('Remove this site use?')) onDelete(node) }} className="px-3 py-2 bg-error/10 text-error rounded-lg text-xs font-semibold hover:bg-error/20">Remove</button>
        <button onClick={onCancel} className="px-3 py-2 bg-surface-container-low border border-outline-variant rounded-lg text-xs font-semibold text-outline">Close</button>
      </div>
    </div>
  )
}
