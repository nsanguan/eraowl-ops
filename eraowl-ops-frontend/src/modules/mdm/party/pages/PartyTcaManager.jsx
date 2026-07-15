import { useState, useEffect, useCallback } from 'react'
import api from '../../../../api/client'
import { MasterDetailSplit } from '../../../../shared-ui-kit/components/ui/MasterDetailSplit'
import { SegmentedControl } from '../../../../shared-ui-kit/components/ui/SegmentedControl'
import { CardsRegion } from '../../../../shared-ui-kit/components/ui/CardsRegion'
import { StatCard } from '../../../../shared-ui-kit/components/ui/StatCard'

const PARTY_TYPE_OPTIONS = ['ALL', 'ORGANIZATION', 'PERSON']
const ROLE_FILTERS = ['ALL', 'SUPPLIER', 'CUSTOMER']

const TABS = [
  { value: 'profile', label: 'Profile' },
  { value: 'roles', label: 'Business Roles' },
  { value: 'sites', label: 'Addresses & Sites' },
  { value: 'contacts', label: 'Contacts' },
]

export default function PartyTcaManager() {
  const [parties, setParties] = useState([])
  const [loading, setLoading] = useState(true)
  const [selectedParty, setSelectedParty] = useState(null)
  const [tcaView, setTcaView] = useState(null)
  const [activeTab, setActiveTab] = useState('profile')
  const [partyFilter, setPartyFilter] = useState('ALL')
  const [roleFilter, setRoleFilter] = useState('ALL')
  const [searchQuery, setSearchQuery] = useState('')

  const fetchParties = useCallback(async () => {
    setLoading(true)
    try {
      const { data } = await api.get('/party/parties', { params: { page: 1, page_size: 100 } })
      setParties(data?.items || [])
    } catch {} finally { setLoading(false) }
  }, [])

  const fetchTcaView = useCallback(async (partyId) => {
    if (!partyId) return
    try {
      const { data } = await api.get(`/party/parties/${partyId}/tca-view`)
      setTcaView(data)
    } catch { setTcaView(null) }
  }, [])

  useEffect(() => { fetchParties() }, [fetchParties])

  useEffect(() => {
    if (selectedParty) fetchTcaView(selectedParty.party_id)
  }, [selectedParty, fetchTcaView])

  const filteredParties = parties.filter((p) => {
    if (partyFilter !== 'ALL' && p.party_type !== partyFilter) return false
    if (roleFilter !== 'ALL') {
      if (!tcaView || tcaView.party?.party_id !== p.party_id) return true
    }
    return true
  }).filter((p) =>
    !searchQuery || p.party_name?.toLowerCase().includes(searchQuery.toLowerCase()) ||
    p.party_number?.toLowerCase().includes(searchQuery.toLowerCase())
  )

  const siteCards = (tcaView?.sites || []).map((s) => ({
    id: s.party_site_id,
    title: s.site_name || s.party_site_number,
    subtitle: s.address ? `${s.address.address_line1}, ${s.address.city}` : '',
    badges: (s.site_uses || []).map((u) => ({
      label: u.site_use_type,
      color: u.is_primary ? 'oklch(0.55 0.14 150)' : 'oklch(0.55 0.03 260)',
    })),
    metadata: [
      { label: 'Number', value: s.party_site_number },
      ...(s.address?.state ? [{ label: 'State', value: s.address.state }] : []),
      ...(s.address?.postal_code ? [{ label: 'Postal', value: s.address.postal_code }] : []),
      ...(s.address?.country ? [{ label: 'Country', value: s.address.country }] : []),
    ],
  }))

  const totalSupplierCredit = 0
  const totalCustomerLimit = tcaView?.customer?.credit_limit || 0

  const handleRefresh = () => {
    if (selectedParty) fetchTcaView(selectedParty.party_id)
    fetchParties()
  }

  const handleDeleteSiteUse = async (siteUseId) => {
    if (!confirm('Remove this site use?')) return
    try { await api.delete(`/party/party-site-uses/${siteUseId}`); handleRefresh() } catch {}
  }

  const handleSetPrimarySite = async (siteId, useType) => {
    try {
      const { data: uses } = await api.get(`/party/party-site-uses`, { params: { party_site_id: siteId } })
      const items = uses?.items || []
      for (const u of items) {
        if (u.site_use_type === useType) {
          await api.put(`/party/party-site-uses/${u.site_use_id}`, { is_primary: true })
        } else if (u.is_primary && u.site_use_type === useType) {
          await api.put(`/party/party-site-uses/${u.site_use_id}`, { is_primary: false })
        }
      }
      handleRefresh()
    } catch {}
  }

  return (
    <div className="h-[calc(100vh-7rem)]">
    <MasterDetailSplit
      masterWidth="320px"
      masterContent={
        <div className="h-full flex flex-col">
          <div className="p-4 border-b border-outline-variant space-y-3">
            <h2 className="text-sm font-bold text-on-surface">Trading Community</h2>
            <input type="text" value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search by name or number..."
              className="w-full px-3 py-2 bg-surface-bright border border-outline-variant rounded-xl text-sm text-on-surface focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none" />
            <div className="flex gap-2">
              <select value={partyFilter} onChange={(e) => setPartyFilter(e.target.value)}
                className="flex-1 px-2 py-1.5 bg-surface-bright border border-outline-variant rounded-lg text-xs text-on-surface outline-none">
                {PARTY_TYPE_OPTIONS.map((o) => <option key={o} value={o}>{o === 'ALL' ? 'All Types' : o}</option>)}
              </select>
              <select value={roleFilter} onChange={(e) => setRoleFilter(e.target.value)}
                className="flex-1 px-2 py-1.5 bg-surface-bright border border-outline-variant rounded-lg text-xs text-on-surface outline-none">
                {ROLE_FILTERS.map((o) => <option key={o} value={o}>{o === 'ALL' ? 'All Roles' : o}</option>)}
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
                className={`w-full text-left px-4 py-3 transition-colors hover:bg-surface-container-low ${
                  selectedParty?.party_id === p.party_id ? 'bg-primary/5 border-l-2 border-primary' : 'border-l-2 border-transparent'
                }`}>
                <div className="text-sm font-semibold text-on-surface">{p.party_name}</div>
                <div className="flex items-center gap-2 mt-0.5">
                  <span className="text-[10px] text-outline font-mono">{p.party_number}</span>
                  <span className="text-[10px] px-1.5 py-0.5 rounded-full bg-primary/10 text-primary">{p.party_type}</span>
                </div>
              </button>
            ))}
          </div>
          <div className="p-3 border-t border-outline-variant text-[10px] text-outline text-center">
            {parties.length} parties
          </div>
        </div>
      }
      detailContent={
        <div className="h-full flex flex-col">
          {!selectedParty ? (
            <div className="flex items-center justify-center flex-1 text-outline text-sm">
              Select a party from the list to view details
            </div>
          ) : !tcaView ? (
            <div className="flex items-center justify-center flex-1 text-outline text-sm">Loading...</div>
          ) : (
            <>
              <div className="p-4 border-b border-outline-variant bg-surface-container-low/50">
                <div className="flex items-center justify-between">
                  <div>
                    <h2 className="text-lg font-bold text-on-surface">{tcaView.party.party_name}</h2>
                    <div className="flex items-center gap-3 mt-1">
                      <span className="text-[11px] font-mono text-outline">{tcaView.party.party_number}</span>
                      <span className="text-[11px] px-1.5 py-0.5 rounded-full bg-primary/10 text-primary font-medium">{tcaView.party.party_type}</span>
                      {tcaView.party.tax_reference && (
                        <span className="text-[11px] text-outline">Tax: {tcaView.party.tax_reference}</span>
                      )}
                    </div>
                  </div>
                  <div className="flex items-center gap-2">
                    <button onClick={handleRefresh} className="p-2 text-outline hover:text-primary transition-colors rounded-lg hover:bg-surface-container-high">
                      <span className="material-symbols-outlined text-[18px]">refresh</span>
                    </button>
                  </div>
                </div>
              </div>

              <SegmentedControl
                options={TABS}
                value={activeTab}
                onChange={setActiveTab}
              />

              <div className="flex-1 overflow-y-auto p-4 custom-scrollbar">
                {activeTab === 'profile' && (
                  <div className="space-y-4 max-w-2xl">
                    <div className="grid grid-cols-2 gap-4">
                      <StatCard title="Party Name" value={tcaView.party.party_name} icon="badge" />
                      <StatCard title="Party Number" value={tcaView.party.party_number} icon="pin" />
                      <StatCard title="Tax Reference" value={tcaView.party.tax_reference || '—'} icon="receipt" />
                      <StatCard title="Type" value={tcaView.party.party_type} icon="category" />
                    </div>
                    <div className="bg-surface-container-lowest border border-outline-variant rounded-xl p-4">
                      <h3 className="text-xs font-bold text-on-surface uppercase tracking-wider mb-3">Registry Information</h3>
                      <div className="grid grid-cols-2 gap-4 text-sm">
                        {[
                          ['Party ID', tcaView.party.party_id],
                          ['Status', tcaView.party.is_active ? 'Active' : 'Inactive'],
                          ['Created', new Date(tcaView.party.created_at).toLocaleDateString()],
                          ['Updated', new Date(tcaView.party.updated_at).toLocaleDateString()],
                        ].map(([label, value]) => (
                          <div key={label}>
                            <div className="text-[10px] font-semibold text-outline uppercase tracking-wider">{label}</div>
                            <div className="text-sm text-on-surface mt-0.5 break-all">{value}</div>
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                )}

                {activeTab === 'roles' && (
                  <div className="space-y-4 max-w-2xl">
                    <div className="flex flex-wrap gap-2">
                      {['SUPPLIER', 'CUSTOMER'].map((role) => {
                        const hasRole = (tcaView.roles || []).some((r) => r.role_type === role)
                        return (
                          <div key={role}
                            className={`flex items-center gap-2 px-3 py-2 rounded-xl border text-sm font-semibold transition-colors ${
                              hasRole ? 'bg-primary/10 border-primary/30 text-primary' : 'bg-surface-container-low border-outline-variant text-outline'
                            }`}>
                            <span className="material-symbols-outlined text-[16px]">
                              {role === 'SUPPLIER' ? 'conveyor_belt' : 'handshake'}
                            </span>
                            {role}
                            {hasRole && <span className="text-[10px] text-primary/60">✔ Active</span>}
                          </div>
                        )
                      })}
                    </div>

                    {tcaView.supplier && (
                      <div className="bg-surface-container-lowest border border-outline-variant rounded-xl p-4">
                        <h3 className="text-xs font-bold text-on-surface uppercase tracking-wider mb-3 flex items-center gap-2">
                          <span className="material-symbols-outlined text-[16px] text-primary">conveyor_belt</span> Supplier Profile
                        </h3>
                        <div className="grid grid-cols-2 gap-4 text-sm">
                          {[
                            ['Vendor Type', tcaView.supplier.vendor_type_lookup_code || '—'],
                            ['Payment Method', tcaView.supplier.payment_method_code || '—'],
                            ['Payment Terms', `${tcaView.supplier.payment_term_days} days`],
                          ].map(([label, value]) => (
                            <div key={label}>
                              <div className="text-[10px] font-semibold text-outline uppercase tracking-wider">{label}</div>
                              <div className="text-sm text-on-surface mt-0.5">{value}</div>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}

                    {tcaView.customer && (
                      <div className="bg-surface-container-lowest border border-outline-variant rounded-xl p-4">
                        <h3 className="text-xs font-bold text-on-surface uppercase tracking-wider mb-3 flex items-center gap-2">
                          <span className="material-symbols-outlined text-[16px] text-primary">handshake</span> Customer Profile
                        </h3>
                        <div className="grid grid-cols-2 gap-4 text-sm">
                          {[
                            ['Class Code', tcaView.customer.customer_class_code || '—'],
                            ['Credit Limit', tcaView.customer.credit_limit ? `${tcaView.customer.credit_limit.toLocaleString()} THB` : '—'],
                            ['Payment Terms', `${tcaView.customer.payment_term_days} days`],
                          ].map(([label, value]) => (
                            <div key={label}>
                              <div className="text-[10px] font-semibold text-outline uppercase tracking-wider">{label}</div>
                              <div className="text-sm text-on-surface mt-0.5">{value}</div>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}

                    {(!tcaView.supplier && !tcaView.customer) && (
                      <p className="text-sm text-outline py-4">No business roles configured for this party.</p>
                    )}
                  </div>
                )}

                {activeTab === 'sites' && (
                  <div className="space-y-4">
                    <div className="flex items-center justify-between">
                      <h3 className="text-sm font-bold text-on-surface">Locations ({siteCards.length})</h3>
                      <span className="text-[10px] text-outline bg-surface-container-high px-2 py-1 rounded-full">
                        {siteCards.filter((s) => s.badges.some((b) => b.label === 'BILL_TO')).length} bill-to
                      </span>
                    </div>
                    <CardsRegion
                      items={siteCards}
                      emptyMessage="No sites registered for this party."
                      onAction={(action, item) => {
                        if (action === 'delete-use') handleDeleteSiteUse(item.id)
                        if (action === 'set-primary') handleSetPrimarySite(item.id, 'BILL_TO')
                      }}
                    />
                  </div>
                )}

                {activeTab === 'contacts' && (
                  <div className="space-y-4">
                    <div className="bg-surface-container-lowest border border-outline-variant rounded-xl p-6 text-center">
                      <span className="material-symbols-outlined text-[48px] text-outline">contact_page</span>
                      <h3 className="text-sm font-semibold text-on-surface mt-2">Contact Management</h3>
                      <p className="text-sm text-outline mt-1 max-w-md mx-auto">
                        Link operational contacts to this party account. Contact assignment will be available in the next release.
                      </p>
                    </div>
                  </div>
                )}
              </div>
            </>
          )}
        </div>
      }
    />
    </div>
  )
}
