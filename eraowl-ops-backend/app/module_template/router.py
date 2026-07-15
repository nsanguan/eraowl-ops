from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.shared.module_base.crud import BaseCRUDService
from app.shared.module_base.generic import BaseGenericService

router = APIRouter()


# ---------------------------------------------------------------------------
# 1. Standard CRUD endpoints — extend BaseCRUDService per entity
# ---------------------------------------------------------------------------

# Template:
#   GET    /entities       → svc.list(page, page_size, filters)
#   GET    /entities/{id}  → svc.get(id)
#   POST   /entities       → svc.create(data)
#   PUT    /entities/{id}  → svc.update(id, data)
#   DELETE /entities/{id}  → svc.delete(id)


# ---------------------------------------------------------------------------
# 2. Composite endpoints — master-detail operations
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# 3. Generic CRUD — dynamic table access via BaseGenericService
# ---------------------------------------------------------------------------

# Template:
#   GET  /generic/{table}      → svc.list_all(table)
#   POST /generic/{table}      → svc.create(table, data)
