# EraOwl-OPS

AI-powered ERP platform built as a **Modular Monolith** (FastAPI backend) with a **Decoupled React frontend**.

## Architecture

| Layer | Technology | Version |
|-------|------------|---------|
| Backend | Python, FastAPI, SQLModel/SQLAlchemy (async), asyncpg | 3.12+ / 0.115+ |
| Database | PostgreSQL (external: `202.71.1.13:5435`) | 15+ |
| Cache | Redis (token blacklist, permission versioning) | 7 |
| Frontend | React, Vite, react-router-dom, Tailwind CSS, Zustand | 19 / 6 / 7 / 4 / 5 |
| Auth | JWT (Access + Refresh), bcrypt, httpOnly cookies | — |
| Infra | Docker Compose (3 services), Nginx reverse-proxy | — |

## Backend Modules

### Module Structure
Every module under `app/modules/{name}/` has: `models.py`, `schemas.py`, `router.py`, `services.py`, `permissions.py`, `exceptions.py`. Sub-modules (e.g., `mdm/org_structure`) follow the same pattern. Modules are auto-discovered at startup by `app/core/module_registry.py` and mounted at `/api/v1/{module_name}`.

| Module | Status | Entities | Endpoints |
|--------|--------|----------|-----------|
| `admin` | ✅ Complete | User, Role, Privilege, UserRole, RolePrivilege, UserBusinessUnit, AuditLog, RefreshToken | login, refresh, logout, users CRUD, roles CRUD, privileges, audit-logs, generic CRUD |
| `mdm/org_structure` | ✅ Complete | OrgCorporate, OrgCompany, OrgBusinessUnit, OrgSite, OrgWarehouse, OrgWarehouseLocator | Full CRUD per entity |
| `mdm/party` | ✅ Complete | Address, Party, PartySite, PartySiteUse, PartyRole, Supplier, Customer | Full CRUD per entity |
| `mdm/item` | ✅ Complete | UOM, UOMConversion, ItemCategory, Item, ItemCategoryAssignment, ItemOrganization, ItemSupplierXref | Full CRUD per entity |
| `bom` | ✅ Complete | BomHeader, BomLine | CRUD + approve + multi-level explode with circular ref validation |
| `po` | ✅ Complete (backend) | PoHeader, PoLine, PoShipment, PoDistribution, PoRelease, PoAmendment, PoApproval | Full CRUD per entity + composite CRUD + generic CRUD |
| `gl` | 🔜 Placeholder | — | — |
| `om` | 🔜 Placeholder | — | — |

### Key Backend Patterns
- **Models**: SQLModel `table=True`, `__table_args__={"schema": "..."}`, UUID PKs, `is_active`/`is_deleted`/`created_at`/`updated_at` on all entities
- **CRUD**: `BaseCRUDService<T>` from `app/shared/module_base/crud.py` for generic list/get/create/update/delete with soft-delete, pagination, search, filters
- **Permissions**: Declarative `permissions.py` per module — guarded by `check_privilege(module, action)` from `app/core/dependencies.py`
- **Auth**: `get_current_user()` dependency checks JWT + permission version. `check_privilege()` does DB-level RBAC verification (not token-only)
- **DB**: 3 PostgreSQL schemas (`mdm`, `admin`, `po`), single Alembic migration chain

## Frontend Pages

| Route | Page | Module |
|-------|------|--------|
| `/login` | Login form | admin |
| `/` | Welcome dashboard | — |
| `/admin/users` | User Management (CRUD, role assignment, CSV export) | admin |
| `/admin/roles` | Role Management (permission matrix grid) | admin |
| `/org-structure` | Org Structure (6-tab: Corporate → Company → BU → Site → Warehouse → Locator) | mdm |
| `/party` | Party Management (4-tab: Addresses, Parties, Suppliers, Customers) | mdm |
| `/items` | Item Management (3-tab: Items, Categories, UOMs) | mdm |
| `/bom` | BOM Management (2-tab: Headers, Lines) | bom |

### Shared UI Kit
33 reusable React components under `src/shared-ui-kit/` (adapted from AxonOS):

| Category | Components |
|----------|-----------|
| **Data** | `InteractiveGrid` (primary table), `TreeGrid`, `MasterDetailSplit` |
| **Layout** | `AppShell`, `Sidebar`, `Header`, `MenuTree`, `TopStatusBar`, `ErrorBoundary` |
| **Display** | `PageHeader`, `StatCard`, `StatusChip`, `BadgeList`, `CardsRegion`, `AccordionRegion`, `TimelineRegion` |
| **Interaction** | `Wizard`, `ShuttleControl`, `SegmentedControl`, `FilterPopover`, `FacetedSearch`, `SmartSearch`, `LovModal`, `SwitchToggle`, `ProgressBar`, `RangeSlider`, `RatingStars`, `NumberSpinner`, `ColorPicker`, `DateRangePicker`, `RichTextEditor`, `DropzoneUpload`, `CommentsRegion`, `HeroRegion`, `MediaList` |
| **Auth/Theme** | `AuthGate`, `ThemeRoller`, `ThemeProvider`, `LoginModal`, `PreferencesModal` |

### Frontend Stack
- **React 19** + **react-router-dom 7** — SPA routing with auth guards (`ProtectedRoute`)
- **Zustand 5** — State management (`authStore.js`: login, logout, token lifecycle)
- **Axios** — HTTP client with interceptor-based auto-refresh on 401
- **Tailwind CSS 4** — via `@tailwindcss/vite` plugin. Custom dark/light themes in OKLCH color space
- **Material Symbols** — Icon font
- **Inter** and **JetBrains Mono** — Fonts

### Auth Flow
1. Login form → `POST /api/v1/admin/login` → Access Token (memory/localStorage) + Refresh Token (localStorage)
2. Axios interceptor attaches `Authorization: Bearer <access_token>` to all requests
3. On 401 → interceptor calls `POST /api/v1/admin/refresh` → rotates tokens automatically
4. If refresh fails → clear storage → redirect to `/login`

## Database

PostgreSQL schemas for namespace isolation:

```
mdm             — Unified master data: org_structure (6) + party (7) + item (7) + bom (2)
admin           — Users, roles, privileges, audit, refresh_tokens
po              — Purchase Order headers, lines, shipments, distributions
```

Connection: `postgresql+asyncpg://eraowlopsadmin@{password}@202.71.1.13:5435/eraowlops`

## Design System

An EraOwl Design System (EODS v1.0.0) is maintained at `design/eraowl-ds/`:
- **Design Tokens**: 350+ CSS custom properties (colors, typography, spacing, shadows, animation, z-index, layout)
- **Component CSS**: 12 CSS files with `.eods-` prefixed classes for buttons, forms, interactive grid, dialog, cards, navigation, dashboard, badges, and utilities
- **JS Library**: 1496-line vanilla JS utility (`eods.` namespace) with notifications, modals, AJAX, validation, DOM helpers, theme toggling
- **Documentation**: README, Tailwind CSS v4 integration guide, tokens reference, components overview, accessibility, responsive design, dark mode, best practices
- **Tailwind Integration**: All design tokens mapped to Tailwind CSS v4 `@theme` directive in the frontend's `index.css`
- **React Integration**: CSS powers 33 shared-ui-kit components (InteractiveGrid, Sidebar, StatCard, StatusChip, Dialog, Wizard, etc.)

## Infrastructure

### Docker Compose
```
services:
  backend    — FastAPI app (port 8000, multi-stage Python 3.12-slim build)
  frontend   — Nginx-served React app (port 3001, Node 22 → Nginx build)
  redis      — Token blacklist & permission versioning (port 6379, redis:7-alpine)
network: eraowlops-global-network (bridge)
```

### Dockerfiles
- **Backend** (`eraowl-ops-backend/Dockerfile`): Two-stage build (builder + runner). Non-root `appuser`. Exposes 8000.
- **Frontend** (`eraowl-ops-frontend/Dockerfile`): Two-stage (Node 22 builder → Nginx runner). Proxies `/api/` to `backend:8000`.

## Project Structure

```
eraowl-ops/
├── eraowl-ops-backend/             # FastAPI application
│   ├── app/
│   │   ├── core/                   # Framework: config, database, security, deps, middleware, module_registry
│   │   ├── shared/                 # Shared: base_model, pagination, events, module_base (CRUD, generic, mixins)
│   │   ├── module_template/        # Scaffold for creating new modules
│   │   └── modules/                # Business modules
│   │       ├── admin/              # IAM
│   │       ├── mdm/                # Master Data (org_structure, party, item)
│   │       ├── bom/                # Bill of Materials
│   │       ├── po/                 # Purchase Orders
│   │       ├── gl/                 # (placeholder)
│   │       └── om/                 # (placeholder)
│   ├── alembic/                    # DB migrations (single chain)
│   ├── scripts/                    # SQL schema/seed + Python seed scripts
│   ├── Dockerfile                  # Multi-stage Python 3.12-slim
│   └── pyproject.toml              # Python dependencies
├── eraowl-ops-frontend/            # React application
│   ├── src/
│   │   ├── App.jsx                 # Router definitions
│   │   ├── api/client.js           # Axios instance with auth interceptor
│   │   ├── store/authStore.js      # Zustand auth state
│   │   ├── components/             # Layout, Header, ProtectedRoute
│   │   ├── modules/                # Page components per module
│   │   ├── shared-ui-kit/          # 33 reusable UI components
│   │   └── module_template/        # Frontend module scaffold guide
│   ├── Dockerfile                  # Node 22 → Nginx
│   ├── nginx.conf                  # SPA config with /api/ proxy
│   └── vite.config.js              # Dev server: 5173, proxy /api → :8000
├── design/eraowl-ds/               # EraOwl Design System (EODS) — React + Tailwind CSS design tokens & components
├── requirements/                   # Project documentation
├── docker-compose.yml              # 3-service orchestration
├── .env.example                    # Environment template
└── AGENTS.md                       # AI agent instructions
```

## Quick Start

```bash
# 1. Clone and configure
cp .env.example .env          # Edit with your DB credentials
cp eraowl-ops-backend/.env.example eraowl-ops-backend/.env

# 2. Run with Docker
docker compose up -d

# Or run locally:

# Backend
cd eraowl-ops-backend
pip install -r requirements.txt  # or: pip install -e .
alembic upgrade head
uvicorn app.main:app --reload --port 8000

# Frontend (separate terminal)
cd eraowl-ops-frontend
npm install
npm run dev                     # Starts at http://localhost:5173

# Database seed
psql -h 202.71.1.13 -p 5435 -U eraowlopsadmin -d eraowlops -f scripts/001_schema.sql
```

## Key Links
- **Requirements doc**: `requirements/Implementation_v3_1.md` — Full implementation plan and status
- **Agent instructions**: `AGENTS.md` — AI agent conventions for this project
- **Design system docs**: `design/eraowl-ds/README.md` — EraOwl Design System (React + Tailwind CSS tokens & component CSS)
- **Tailwind integration**: `design/eraowl-ds/TAILWIND_INTEGRATION.md` — How design tokens map to Tailwind CSS v4
- **Backend README**: `eraowl-ops-backend/README.md` — Backend API reference and conventions
- **Frontend README**: `eraowl-ops-frontend/README.md` — Frontend page and component guide
