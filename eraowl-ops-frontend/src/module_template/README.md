# Global Module & Page Template — EraOwl-OPS

## Quick Start: New Module Backend

```bash
cp -r app/module_template/ app/modules/your_module
```
Then edit `models.py`, `schemas.py`, `services/crud.py`, `router.py`, `permissions.py`.

## Quick Start: New Module Frontend Page

```bash
cp src/module_template/Layout.jsx src/modules/your_module/pages/YourPage.jsx
cp src/module_template/Header.jsx src/components/Header.jsx   # if starting fresh
```

## Standard Layout (AppShell Pattern)

```
+-----------------------------------------------------------+
|  Sidebar (fixed, w-64)    |  Header (fixed, h-16, left-64)|
|                           +--------------------------------|
|  [EO] EraOwl-OPS          |  [MD] ModuleLabel              |
|  AI ERP Platform          |                                |
|                           |  home  bell  theme  help  [AU] |
|  ◄ Navigation Links       |                                |
|                           +--------------------------------|
|                           |  Home > Module > Page Title    |
|  ───────────────────      |                                |
|  [IN] Module User         |  ┌─ Content (Outlet) ───────┐  |
|  ERA OPS                  |  │                           │  |
|                           |  └──────────────────────────┘  |
+-----------------------------------------------------------+
```

## Header Component (`components/Header.jsx`)

- **No search bar** (removed from Global Design)
- **Left side**: Module initials badge + module label
- **Right side**: Home, Notifications (with red dot), Theme toggle (light/dark), Help dropdown (Documentation, About), User avatar + initials, Sign Out
- **All colors use design tokens** (`bg-surface-container`, `border-outline-variant`, `text-on-surface`)
- **Dark mode**: Theme toggle persisted to localStorage

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `onNavigate` | `(path) => void` | — | Route navigation callback |
| `homeUrl` | `string` | — | External home URL (overrides onNavigate) |
| `helpUrl` | `string` | — | Docs URL for Help > Documentation |
| `userLabel` | `string` | `'Admin User'` | Display name in top-right |
| `userInitials` | `string` | `'AU'` | Avatar initials (2 chars) |
| `moduleLabel` | `string` | — | Module name shown next to badge |
| `moduleInitials` | `string` | — | Module initials in badge (2 chars) |

## Standard Page Layout (`Layout.jsx`)

### Sidebar
- Fixed 64px width, `bg-surface-dim`
- Brand logo + name
- Navigation links (replace per module)
- User info footer

### Content Area
- `ml-64` (offset for sidebar)
- `mt-16` (offset for header)
- Breadcrumb nav bar
- `<Outlet />` for page content

## Customization Guide

1. **New module page**: Copy `Layout.jsx`, update `menuItems`, `moduleLabel`, `moduleInitials`
2. **No sidebar needed**: Remove the `<aside>` and `ml-64` from `<main>`
3. **Custom topbar buttons**: Add buttons in the Header's action section

## Backend Module Template

### Folder Structure
```
app/module_template/
├── __init__.py
├── models.py          → SQLModel entities (UUIDPKMixin, AuditMixin, SoftDeleteMixin)
├── schemas.py         → Pydantic v2 Create/Update/Response DTOs
├── router.py          → CRUD + optional composite/generic endpoints
├── exceptions.py      → Module-specific errors
├── permissions.py     → RBAC privilege declarations
└── services/
    ├── __init__.py
    ├── crud.py        → Extends BaseCRUDService
    └── generic.py     → Extends BaseGenericService (optional)
```

### Shared Base Classes (`app/shared/module_base/`)
- `BaseCRUDService[Model]` — list/get/create/update/delete with pagination
- `BaseGenericService` — dynamic table CRUD with allowlist
- `UUIDPKMixin`, `AuditMixin`, `SoftDeleteMixin`, `ObjectVersionMixin`

### Standard API Endpoints
```
GET    /api/v1/{module}/{entities}           → List (paginated)
GET    /api/v1/{module}/{entities}/{id}       → Get by ID
POST   /api/v1/{module}/{entities}            → Create
PUT    /api/v1/{module}/{entities}/{id}       → Update
DELETE /api/v1/{module}/{entities}/{id}       → Soft/hard delete
GET    /api/v1/{module}/generic/{table}       → Generic list (optional)
```
