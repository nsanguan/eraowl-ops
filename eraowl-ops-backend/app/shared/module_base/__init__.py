"""
Global Module Design — Shared Base Classes
===========================================

Reusable base classes for building consistent modules across the EraOwl-OPS platform.
All modules follow the same patterns derived from the PO module:

  Module/
  ├── models.py           → Entity definitions (SQLModel)
  ├── schemas.py          → Pydantic v2 DTOs (Create/Update/Response)
  ├── services/
  │   ├── crud.py         → Thin CRUD per entity
  │   ├── composite.py    → Master-detail composite operations
  │   └── generic.py      → Dynamic table CRUD (optional)
  ├── router.py            → FastAPI endpoints
  ├── exceptions.py        → Custom exceptions
  └── permissions.py       → RBAC privilege declarations

Usage:
  from app.shared.module_base.crud import BaseCRUDService, PaginatedResult
  from app.shared.module_base.generic import BaseGenericService
  from app.shared.module_base.mixins import AuditMixin, SoftDeleteMixin
"""

from app.shared.module_base.crud import BaseCRUDService, PaginatedResult
from app.shared.module_base.generic import BaseGenericService
from app.shared.module_base.mixins import AuditMixin, SoftDeleteMixin, UUIDPKMixin

__all__ = [
    "BaseCRUDService",
    "PaginatedResult",
    "BaseGenericService",
    "AuditMixin",
    "SoftDeleteMixin",
    "UUIDPKMixin",
]
