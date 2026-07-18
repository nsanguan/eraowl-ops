# EraOwl-OPS Agent Instructions

## Project Overview

EraOwl-OPS is an AI-powered ERP platform built as a **Modular Monolith** (FastAPI backend) with a **Decoupled React frontend**.

- **Backend**: Python 3.12+, FastAPI, SQLModel/SQLAlchemy 2.0+ (async), asyncpg, Alembic, Pydantic v2
- **Frontend**: React 19, Vite 6, react-router-dom 7, Tailwind CSS 4, Zustand 5, axios
- **Database**: PostgreSQL 15+ with schema-based namespace isolation
- **Cache**: Redis 7 (token blacklist, permission versioning)
- **Auth**: JWT (Access + Refresh tokens), bcrypt, httpOnly cookies, permission versioning

## Backend Conventions

### Module Structure
Every module under `app/modules/{name}/` must follow this structure:

```
admin/
├── models.py        # SQLModel entities (SQLModel, table=True)
├── schemas.py       # Pydantic v2 request/response schemas
├── router.py        # FastAPI APIRouter with endpoints
├── services.py      # Business logic (or services/ directory for complex modules)
├── permissions.py   # Declarative privilege definitions
└── exceptions.py    # Custom exceptions
```

Modules are auto-discovered by `app/core/module_registry.py` which mounts each module's `router` at `/api/v1/{module_name}`. Sub-modules (e.g., `mdm/org_structure`) are also auto-discovered recursively.

### Model Conventions (models.py)
- Inherit from `SQLModel` with `table=True`
- Set `__tablename__` and `__table_args__ = {"schema": "..."}` (PostgreSQL schema isolation)
- UUID primary key: `entity_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))`
- Standard fields on every entity: `is_active`, `is_deleted`, `created_at`, `updated_at`
- Timestamps use `server_default=func.now()` and `onupdate=func.now()` for `updated_at`
- Use `Optional[datetime]` for nullable timestamp fields

### Router Conventions (router.py)
- `router = APIRouter()` at module level
- Endpoints use entity_id path parameter consistently (e.g., `/bom-headers/{entity_id}`)
- Pagination via Query params: `page: int = Query(1, ge=1)`, `page_size: int = Query(20, ge=1, le=100)`
- Return type: `PaginatedResponse[ModelOut]` for list endpoints
- Service instantiation: `svc = SomeService(db)` where `db: AsyncSession = Depends(get_db)`
- Use `Depends(get_service)` factory function pattern when service needs db
- Standard endpoints per entity: list (GET), get (GET /{id}), create (POST, 201), update (PUT /{id}), delete (DELETE /{id}, 204)

### Service Conventions (services.py)
- Services use `BaseCRUDService<T>` from `app/shared/module_base/crud.py` for generic CRUD
  ```python
  class UserService(BaseCRUDService[User]):
      def __init__(self, db: AsyncSession):
          super().__init__(db, User)
  ```
- `BaseCRUDService` provides: `list()`, `get()`, `create()`, `update()`, `delete()` with soft-delete, pagination, search, and filter support
- For custom modules, implement helper methods: `_paginate()`, `_get_by_id()`, `_create()`, `_update()`, `_delete()`

### Permission Conventions (permissions.py)
- Declarative format per module:
  ```python
  MODULE_NAME = "admin"
  PRIVILEGES = [
      {"action": "view", "description": "View admin"},
      {"action": "manage_users", "description": "Manage users"},
  ]
  ```
- Guard endpoints with `check_privilege(module, action)` from `app/core/dependencies.py`

### Shared Base Classes
Location: `app/shared/module_base/`
- `crud.py`: `BaseCRUDService<M>` — generic CRUD with pagination, search, filters, soft-delete
- `generic.py`: `BaseGenericService` — dynamic table CRUD for admin-style interfaces
- `mixins.py`: `UUIDPKMixin`, `AuditMixin`, `SoftDeleteMixin`, `ObjectVersionMixin`

### Database
- 5 PostgreSQL schemas: `admin`, `mdm`, `bom`, `po`, `collab`
- Each module's models specify `__table_args__ = {"schema": "..."}`
- Single Alembic migration chain (all schemas in one history)
- DB connection: external at `202.71.1.13:5435`, configured via `DATABASE_URL` env var
- Async engine with pool_size=20

### Adding a New Module
1. Copy `app/module_template/` to `app/modules/{name}/`
2. Define models, schemas, router, services, permissions, exceptions following the patterns above
3. Add model import in `alembic/env.py` if it's a new model
4. The module router is auto-discovered at startup — no wiring needed

## Frontend Conventions

### Module Structure
```
modules/{name}/
├── pages/           # Page components (1 per route)
├── components/      # Module-specific components
├── api/             # API call functions
└── routes.jsx       # Route definitions (exported for App.jsx)
```

### Page Conventions
- Each page is a tabbed interface using shared-ui-kit components
- Primary data table: `InteractiveGrid` from `shared-ui-kit/components/ui/InteractiveGrid`
- Layout via `Layout` component (sidebar + breadcrumbs + Outlet)
- Routes defined in `App.jsx`:
  ```jsx
  <Route path="/items" element={<ItemPage />} />
  ```

### State Management
- Zustand store in `src/store/authStore.js` for auth state
- Access token in memory/state + `localStorage` (both access and refresh tokens)
- Axios interceptor (`src/api/client.js`) auto-refreshes on 401, redirects to `/login` on failure

### Styling
- Tailwind CSS v4 with `@tailwindcss/vite` plugin
- Custom CSS variables for dark/light themes (OKLCH color space) in `src/index.css`
- Material Symbols icon font
- Inter and JetBrains Mono fonts

### Shared UI Kit
33 reusable components under `src/shared-ui-kit/`:
- **InteractiveGrid** — primary data table with pagination, search, CRUD, custom columns
- **PageHeader**, **StatCard**, **StatusChip** — layout/display
- **AppShell**, **Sidebar**, **Header**, **MenuTree** — application shell
- **Wizard**, **TreeGrid**, **ShuttleControl**, **SegmentedControl** — advanced interactions
- **AuthGate**, **ThemeRoller**, **ThemeProvider** — auth/theming

Import from `shared-ui-kit/index.ts`.

### Design System
The project has a dedicated EraOwl Design System (EODS) at `design/eraowl-ds/` with design tokens, component CSS, and JS utilities. All tokens map to Tailwind CSS v4 via the `@theme` directive in `index.css`. Component CSS uses the `.eods-` prefix (e.g., `.eods-btn--primary`, `.eods-ig`). See `design/eraowl-ds/README.md` for full documentation.

### Frontend Page Patterns (observed in existing pages)
- Tab-based interface: each page manages multiple entity types via tab switching
- CRUD operations through InteractiveGrid's built-in row editing and modal dialogs
- API calls through the shared axios instance at `src/api/client.js`

## Completion Checklist
After making changes:
1. Backend lint: `ruff check .` or `mypy .`
2. Frontend build: `npm run build`
3. DB migration: `alembic upgrade head`

## Key Files
- `eraowl-ops-backend/app/main.py` — FastAPI entrypoint, CORS, rate limit, module discovery
- `eraowl-ops-backend/app/core/config.py` — Pydantic Settings (all env vars)
- `eraowl-ops-backend/app/core/module_registry.py` — Auto-discovers module routers
- `eraowl-ops-backend/app/core/dependencies.py` — `get_current_user()`, `check_privilege()`
- `eraowl-ops-backend/app/shared/module_base/crud.py` — `BaseCRUDService<T>`
- `eraowl-ops-frontend/src/App.jsx` — Route definitions
- `eraowl-ops-frontend/src/api/client.js` — Axios instance with auth interceptor
- `eraowl-ops-frontend/src/store/authStore.js` — Zustand auth state
- `docker-compose.yml` — Backend + Frontend + Redis orchestration
