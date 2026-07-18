export const FUNCTIONAL_AREAS = [
  {
    id: 'admin',
    label: 'Administration',
    icon: 'admin_panel_settings',
    color: 'oklch(0.55 0.15 260)',
    description: 'System administration & user management',
  },
  {
    id: 'mdm',
    label: 'Master Data',
    icon: 'database',
    color: 'oklch(0.55 0.14 150)',
    description: 'Items, organizations, parties & master data',
  },
  {
    id: 'scm',
    label: 'Supply Chain',
    icon: 'local_shipping',
    color: 'oklch(0.55 0.14 80)',
    description: 'Planning, procurement, inventory & logistics',
  },
  {
    id: 'financials',
    label: 'Financials',
    icon: 'account_balance',
    color: 'oklch(0.55 0.14 290)',
    description: 'General ledger, AP/AR, FA, tax & accounting',
  },
  {
    id: 'manufacturing',
    label: 'Manufacturing',
    icon: 'precision_manufacturing',
    color: 'oklch(0.55 0.14 30)',
    description: 'Production, MES, quality control & EAM',
  },
  {
    id: 'sales',
    label: 'Sales & OM',
    icon: 'point_of_sale',
    color: 'oklch(0.55 0.14 190)',
    description: 'Order management, customer portal & CRM',
  },
  {
    id: 'ai',
    label: 'AI & Intelligence',
    icon: 'psychology',
    color: 'oklch(0.55 0.14 330)',
    description: 'AI-powered planning, optimization & automation',
  },
  {
    id: 'collab',
    label: 'Collaboration',
    icon: 'group',
    color: 'oklch(0.55 0.14 100)',
    description: 'Team communication and productivity tools',
  },
]

export const MODULE_REGISTRY = [
  { id: 'admin', label: 'Users', icon: 'group', path: '/admin/users', area: 'admin', module: 'admin', action: 'manage_users', keywords: ['user', 'account', 'people', 'staff'] },
  { id: 'roles', label: 'Roles', icon: 'shield', path: '/admin/roles', area: 'admin', module: 'admin', action: 'manage_roles', keywords: ['role', 'permission', 'access', 'security'] },
  { id: 'objects', label: 'Code Objects', icon: 'data_exploration', path: '/admin/objects', area: 'admin', module: 'admin', action: 'view_audit_logs', keywords: ['object', 'catalog', 'metadata', 'code', 'scanner'] },
  { id: 'personalize', label: 'User Personalize', icon: 'tune', path: '/admin/personalize', area: 'admin', module: 'admin', action: 'personalize', keywords: ['personalize', 'ui', 'layout', 'theme', 'personalization', 'page', 'component'] },
  { id: 'org_structure', label: 'Org Structure', icon: 'account_tree', path: '/org-structure', area: 'admin', module: 'org_structure', action: 'view', keywords: ['organization', 'company', 'business unit', 'department', 'hierarchy'] },
  { id: 'core', label: 'Core', icon: 'settings', path: '/core', area: 'admin', module: 'core', action: 'view', keywords: ['core', 'central', 'reference', 'identity'] },
  { id: 'items', label: 'Items', icon: 'inventory_2', path: '/items', area: 'mdm', module: 'item', action: 'view', keywords: ['item', 'product', 'material', 'goods', 'sku', 'catalog'] },
  { id: 'parties', label: 'Parties', icon: 'handshake', path: '/party', area: 'mdm', module: 'party', action: 'view', keywords: ['party', 'supplier', 'customer', 'vendor', 'contact'] },
  { id: 'suppliers', label: 'Suppliers', icon: 'local_shipping', path: '/party/suppliers', area: 'mdm', module: 'party', action: 'view', keywords: ['supplier', 'vendor', 'procurement', 'sourcing'] },
  { id: 'customers', label: 'Customers', icon: 'group', path: '/party/customers', area: 'mdm', module: 'party', action: 'view', keywords: ['customer', 'client', 'buyer', 'account'] },
  { id: 'tca', label: 'TCA Manager', icon: 'diversity_3', path: '/party/tca', area: 'mdm', module: 'party', action: 'view', keywords: ['tca', 'trading community', 'party', 'master data', 'hierarchy'] },
  { id: 'po', label: 'Purchase Orders', icon: 'shopping_cart', path: '/po', area: 'scm', module: 'po', action: 'view', keywords: ['po', 'purchase order', 'procurement', 'buy', 'requisition'] },
  { id: 'bom', label: 'Bill of Materials', icon: 'layers', path: '/bom', area: 'scm', module: 'bom', action: 'view', keywords: ['bom', 'bill of material', 'recipe', 'formula', 'component', 'assembly'] },
  { id: 'inv', label: 'Inventory', icon: 'inventory', path: '/inv', area: 'scm', module: 'inv', action: 'view', keywords: ['inventory', 'stock', 'warehouse', 'bin', 'lot'] },
  { id: 'wms', label: 'Warehouse', icon: 'warehouse', path: '/wms', area: 'scm', module: 'wms', action: 'view', keywords: ['wms', 'warehouse', 'putaway', 'picking', 'shipping'] },
  { id: 'log', label: 'Logistics', icon: 'local_shipping', path: '/log', area: 'scm', module: 'log', action: 'view', keywords: ['logistics', 'shipping', 'carrier', 'freight', 'tracking'] },
  { id: 'sup', label: 'Supplier Portal', icon: 'conveyor_belt', path: '/sup', area: 'scm', module: 'sup', action: 'view', keywords: ['supplier', 'vendor', 'portal', 'procurement'] },
  { id: 'scm', label: 'SCM Planning', icon: 'route', path: '/scm', area: 'scm', module: 'scm', action: 'view', keywords: ['supply chain', 'planning', 'forecast', 'demand', 'scheduling'] },
  { id: 'gl', label: 'General Ledger', icon: 'account_balance', path: '/gl', area: 'financials', module: 'gl', action: 'view', keywords: ['gl', 'general ledger', 'accounting', 'journal', 'balance', 'financial'] },
  { id: 'ap', label: 'Accounts Payable', icon: 'payments', path: '/ap', area: 'financials', module: 'ap', action: 'view', keywords: ['ap', 'payable', 'invoice', 'payment', 'vendor'] },
  { id: 'ar', label: 'Accounts Receivable', icon: 'receipt_long', path: '/ar', area: 'financials', module: 'ar', action: 'view', keywords: ['ar', 'receivable', 'invoice', 'customer', 'collection'] },
  { id: 'fa', label: 'Fixed Assets', icon: 'business', path: '/fa', area: 'financials', module: 'fa', action: 'view', keywords: ['fixed asset', 'depreciation', 'capital', 'equipment'] },
  { id: 'tax', label: 'Tax Management', icon: 'receipt', path: '/tax', area: 'financials', module: 'tax', action: 'view', keywords: ['tax', 'vat', 'withholding', 'filing', 'report'] },
  { id: 'exp', label: 'Expenses', icon: 'credit_card', path: '/exp', area: 'financials', module: 'exp', action: 'view', keywords: ['expense', 'reimbursement', 'travel', 'claim'] },
  { id: 'prod', label: 'Production', icon: 'manufacturing', path: '/prod', area: 'manufacturing', module: 'prod', action: 'view', keywords: ['production', 'manufacturing', 'work order', 'routing'] },
  { id: 'mes', label: 'MES', icon: 'settings', path: '/mes', area: 'manufacturing', module: 'mes', action: 'view', keywords: ['mes', 'execution', 'shop floor', 'machine', 'labor'] },
  { id: 'qc', label: 'Quality Control', icon: 'fact_check', path: '/qc', area: 'manufacturing', module: 'qc', action: 'view', keywords: ['quality', 'inspection', 'test', 'ncr', 'compliance'] },
  { id: 'eam', label: 'EAM', icon: 'build', path: '/eam', area: 'manufacturing', module: 'eam', action: 'view', keywords: ['eam', 'maintenance', 'asset', 'repair', 'work order'] },
  { id: 'om', label: 'Order Management', icon: 'point_of_sale', path: '/om', area: 'sales', module: 'om', action: 'view', keywords: ['om', 'order', 'sales', 'customer', 'quote', 'return'] },
  { id: 'ai', label: 'AI Engine', icon: 'psychology', path: '/ai', area: 'ai', module: 'ai', action: 'view', keywords: ['ai', 'machine learning', 'forecast', 'optimization', 'nlp'] },
  { id: 'collab', label: 'Collaboration', icon: 'group', path: '/collaboration', area: 'collab', module: 'collaboration', action: 'view', keywords: ['collaboration', 'discuss', 'chat', 'task', 'team', 'calendar'] },
]

export function getAccessibleModules(privileges) {
  if (!privileges || privileges.length === 0) return []

  return MODULE_REGISTRY.filter((mod) =>
    privileges.some(
      (p) =>
        p.module === mod.module &&
        (p.action === mod.action || p.action === 'manage' || p.action === 'view')
    )
  )
}

export function getModulesByArea(privileges) {
  const accessible = getAccessibleModules(privileges)
  const grouped = {}

  for (const area of FUNCTIONAL_AREAS) {
    const modules = accessible.filter((m) => m.area === area.id)
    if (modules.length > 0) {
      grouped[area.id] = { ...area, modules }
    }
  }

  return grouped
}

export function getFirstAccessiblePath(privileges) {
  const accessible = getAccessibleModules(privileges)
  return accessible.length > 0 ? accessible[0].path : '/'
}
