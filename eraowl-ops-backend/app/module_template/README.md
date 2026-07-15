# Module Template — Global Module Design

Use this blueprint when creating a NEW module.

## Quick Start
1. Copy `module_template/` → `modules/your_module/`
2. Edit `models.py` — define your entities
3. Edit `schemas.py` — define DTOs
4. Edit `services/crud.py` — add module-specific CRUD (optional)
5. Edit `router.py` — add composite endpoints (if needed)
6. Edit `permissions.py` — set MODULE_NAME + privileges

## Template Structure
```
your_module/
├── __init__.py
├── models.py          → SQLModel entities
├── schemas.py         → Pydantic v2 DTOs
├── router.py          → FastAPI CRUD + composite + generic
├── exceptions.py      → Custom exceptions
├── permissions.py     → RBAC privileges
├── dto/               → Per-entity DTOs (optional, use schemas.py for simple cases)
│   ├── __init__.py
│   └── schemas.py
└── services/
    ├── __init__.py
    ├── crud.py        → Thin CRUD service (extends BaseCRUDService)
    ├── composite.py   → Master-detail composite (if needed)
    └── generic.py     → Dynamic table CRUD (if needed)
```

## Base Classes Available
- `BaseCRUDService[ModelType]` — generic list/get/create/update/delete with pagination
- `BaseGenericService` — dynamic table CRUD with allowlist
- `UUIDPKMixin`, `AuditMixin`, `SoftDeleteMixin`, `ObjectVersionMixin` — shared model columns

## Standard Endpoints
| Method | Path | Purpose |
|--------|------|---------|
| GET | /api/v1/{module}/{entities} | List with pagination |
| GET | /api/v1/{module}/{entities}/{id} | Get by ID |
| POST | /api/v1/{module}/{entities} | Create |
| PUT | /api/v1/{module}/{entities}/{id} | Update |
| DELETE | /api/v1/{module}/{entities}/{id} | Soft-delete |
| GET | /api/v1/{module}/generic/{table} | Generic list (optional) |
| POST | /api/v1/{module}/generic/{table} | Generic create (optional) |
