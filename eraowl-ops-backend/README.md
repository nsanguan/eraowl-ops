# EraOwl-OPS Backend

FastAPI-based modular monolith backend for the EraOwl-OPS ERP platform.

## Tech Stack

- **Python 3.12+** — Runtime
- **FastAPI 0.115+** — Web framework
- **SQLModel / SQLAlchemy 2.0+** — ORM (async mode)
- **asyncpg** — PostgreSQL async driver
- **Alembic** — Database migrations
- **Pydantic v2** — Data validation
- **python-jose** — JWT handling
- **passlib + bcrypt** — Password hashing
- **slowapi** — Rate limiting
- **Redis** — Token blacklist & permission versioning

## Module Architecture

```
app/
├── core/                 # Framework-level utilities
│   ├── config.py         # Pydantic Settings (DB, Redis, JWT, CORS)
│   ├── database.py       # AsyncSession factory (pool_size=20)
│   ├── security.py       # bcrypt hash/verify, JWT create/decode
│   ├── dependencies.py   # get_current_user(), check_privilege()
│   ├── middleware.py     # RequestLoggingMiddleware
│   ├── exceptions.py     # AppError, UnauthorizedError, ForbiddenError
│   └── module_registry.py # Auto-discovers & mounts module routers
├── shared/              # Domain-level shared utilities
│   ├── base_model.py    # TimestampMixin, SoftDeleteMixin, UUID PK
│   ├── pagination.py    # PaginatedResponse, PaginationParams
│   ├── events.py        # In-process pub/sub event bus
│   └── module_base/     # BaseCRUDService, BaseGenericService, mixins
├── module_template/     # Scaffold for creating new modules
└── modules/             # Business modules
    ├── admin/           # IAM: users, roles, privileges, auth
    ├── mdm/             # Master Data Management
    │   ├── org_structure/  # Corporate → Company → BU → Site → Warehouse → Locator
    │   ├── party/          # TCA-lite: Address, Party, Supplier, Customer
    │   └── item/           # Item Master, UOM, Categories, Item-Org
    ├── bom/             # Bill of Materials w/ circular ref validation
    ├── po/              # Purchase Orders (composite CRUD)
    ├── gl/              # General Ledger (placeholder)
    └── om/              # Order Management (placeholder)
```

## API Endpoints

All routes auto-mounted under `/api/v1/{module}`. See each module's `router.py` for full endpoint lists.

### Admin (`/api/v1/admin/`)
- `POST /login`, `/refresh`, `/logout` — Authentication
- `GET/POST/PUT/DELETE /users`, `/users/{id}`, `/users/{id}/roles`, `/users/{id}/business-units` — User management
- `GET/POST/PUT/DELETE /roles`, `/roles/{id}`, `/roles/{id}/permissions` — Role management
- `GET /privileges`, `POST /privileges/seed` — Privilege management
- `GET /audit-logs` — Audit trail
- `GET/POST/PUT/DELETE /generic/{table}` — Dynamic CRUD for admin tables

### MDM (`/api/v1/{org_structure,party,item}/`)
Full CRUD for all entities: corporates, companies, business-units, sites, warehouses, locators, addresses, parties, party-sites, suppliers, customers, uoms, items, categories, etc.

### BOM (`/api/v1/bom/`)
- `GET/POST/PUT/DELETE /bom-headers`, `/bom-headers/{id}`
- `POST /bom-headers/{id}/approve` — Approve workflow
- `GET /bom-headers/{id}/explode?quantity=` — Multi-level BOM explosion
- `GET/POST/PUT/DELETE /bom-components`, `/bom-components/{id}`

### PO (`/api/v1/po/`)
- `GET/POST/PUT/DELETE /po_headers`, `/po_lines`, `/po_shipments`, `/po_distributions`, etc.
- `GET/POST/PUT /po_headers/{id}/composite` — Composite CRUD (header + lines + children in one call)
- `GET/POST/PUT/DELETE /generic/{table}` — Dynamic CRUD

### General
- `GET /health` — Health check

## Getting Started

```bash
# Install dependencies
poetry install

# Copy environment
cp .env.example .env
# Edit .env with your database credentials

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload --port 8000
```

## Database Schemas

PostgreSQL schemas for namespace isolation:

- `mdm` — Unified master data: org_structure, party, item, bom
- `admin` — Users, roles, privileges, audit, refresh_tokens
- `po` — Purchase Orders

## Migration

```bash
# Generate new migration
alembic revision --autogenerate -m "description"

# Apply
alembic upgrade head

# Rollback
alembic downgrade -1
```

## Adding a New Module

1. Copy `module_template/` to `modules/{your_module}/`
2. Define models, schemas, router, services, permissions, exceptions
3. Add the module to the search path in `alembic/env.py` for new models
4. The module is auto-discovered at startup by `module_registry.py`
