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
    id: 'supply_chain',
    label: 'Supply Chain',
    icon: 'local_shipping',
    color: 'oklch(0.55 0.14 80)',
    description: 'Procurement, BOM & inventory',
  },
  {
    id: 'financials',
    label: 'Financials',
    icon: 'account_balance',
    color: 'oklch(0.55 0.14 290)',
    description: 'General ledger, AP/AR & accounting',
  },
]

export const MODULE_REGISTRY = [
  {
    id: 'admin',
    label: 'Users',
    icon: 'group',
    path: '/admin/users',
    area: 'admin',
    module: 'admin',
    action: 'manage_users',
    keywords: ['user', 'account', 'people', 'staff'],
  },
  {
    id: 'roles',
    label: 'Roles',
    icon: 'shield',
    path: '/admin/roles',
    area: 'admin',
    module: 'admin',
    action: 'manage_roles',
    keywords: ['role', 'permission', 'access', 'security'],
  },
  {
    id: 'objects',
    label: 'Code Objects',
    icon: 'data_exploration',
    path: '/admin/objects',
    area: 'admin',
    module: 'admin',
    action: 'view_audit_logs',
    keywords: ['object', 'catalog', 'metadata', 'code', 'scanner'],
  },
  {
    id: 'org_structure',
    label: 'Org Structure',
    icon: 'account_tree',
    path: '/org-structure',
    area: 'admin',
    module: 'org_structure',
    action: 'view',
    keywords: ['organization', 'company', 'business unit', 'department', 'hierarchy'],
  },
  {
    id: 'items',
    label: 'Items',
    icon: 'inventory_2',
    path: '/items',
    area: 'mdm',
    module: 'item',
    action: 'view',
    keywords: ['item', 'product', 'material', 'goods', 'sku', 'catalog'],
  },
  {
    id: 'parties',
    label: 'Parties',
    icon: 'handshake',
    path: '/party',
    area: 'mdm',
    module: 'party',
    action: 'view',
    keywords: ['party', 'supplier', 'customer', 'vendor', 'contact'],
  },
  {
    id: 'bom',
    label: 'Bill of Materials',
    icon: 'layers',
    path: '/bom',
    area: 'supply_chain',
    module: 'bom',
    action: 'view',
    keywords: ['bom', 'bill of material', 'recipe', 'formula', 'component', 'assembly'],
  },
  {
    id: 'po',
    label: 'Purchase Orders',
    icon: 'shopping_cart',
    path: '/po',
    area: 'supply_chain',
    module: 'po',
    action: 'view',
    keywords: ['po', 'purchase order', 'procurement', 'buy', 'requisition'],
  },
  {
    id: 'gl',
    label: 'General Ledger',
    icon: 'account_balance',
    path: '/gl',
    area: 'financials',
    module: 'gl',
    action: 'view',
    keywords: ['gl', 'general ledger', 'accounting', 'journal', 'balance', 'financial'],
  },
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
