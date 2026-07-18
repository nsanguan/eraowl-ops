"""
Base Generic Service — Global Module Design
============================================

Dynamic CRUD by table name with allowlist.
Any module can create a GenericService by passing its ALLOWED_TABLES.

Usage:
    class AdminGenericService(BaseGenericService):
        ALLOWED_TABLES = {"users": User, "roles": Role, ...}

    svc = AdminGenericService(db)
    users = await svc.list_all("users")
"""

from __future__ import annotations

import uuid
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel


class BaseGenericService:
    """
    Dynamic CRUD for any allowed table.

    Subclass and define ALLOWED_TABLES to restrict which tables
    are accessible through this service.
    """

    ALLOWED_TABLES: dict[str, type[SQLModel]] = {}

    def __init__(self, db: AsyncSession):
        self.db = db

    def _resolve(self, table_name: str) -> type[SQLModel]:
        from app.core.exceptions import NotFoundError

        model = self.ALLOWED_TABLES.get(table_name)
        if not model:
            raise NotFoundError(entity=f"Table '{table_name}'")
        return model

    def _pk_col(self, model: type[SQLModel]) -> str:
        return list(model.__table__.primary_key.columns)[0].name

    async def list_all(self, table_name: str, filters: dict | None = None) -> list[dict]:
        model = self._resolve(table_name)
        q = select(model)
        if hasattr(model, "is_deleted"):
            q = q.where(model.is_deleted == False)
        if filters:
            for col, val in filters.items():
                if hasattr(model, col) and val is not None:
                    q = q.where(getattr(model, col) == val)
        rows = (await self.db.execute(q)).scalars().all()
        return [self._to_dict(r) for r in rows]

    async def get_one(self, table_name: str, entity_id: str) -> dict:
        from app.core.exceptions import NotFoundError

        model = self._resolve(table_name)
        pk = getattr(model, self._pk_col(model))
        q = select(model).where(pk == self._coerce_id(entity_id, pk))
        if hasattr(model, "is_deleted"):
            q = q.where(model.is_deleted == False)
        row = (await self.db.execute(q)).scalar_one_or_none()
        if not row:
            raise NotFoundError(entity=f"{table_name}[{entity_id}]")
        return self._to_dict(row)

    async def create(self, table_name: str, data: dict) -> dict:
        model = self._resolve(table_name)
        valid = {k: v for k, v in data.items() if hasattr(model, k)}
        instance = model(**valid)
        self.db.add(instance)
        await self.db.commit()
        await self.db.refresh(instance)
        return self._to_dict(instance)

    async def update(self, table_name: str, entity_id: str, data: dict) -> dict:
        from app.core.exceptions import NotFoundError

        model = self._resolve(table_name)
        pk = getattr(model, self._pk_col(model))
        q = select(model).where(pk == self._coerce_id(entity_id, pk))
        row = (await self.db.execute(q)).scalar_one_or_none()
        if not row:
            raise NotFoundError(entity=f"{table_name}[{entity_id}]")
        valid = {k: v for k, v in data.items() if hasattr(row, k)}
        for k, v in valid.items():
            setattr(row, k, v)
        await self.db.commit()
        await self.db.refresh(row)
        return self._to_dict(row)

    async def delete(self, table_name: str, entity_id: str) -> None:
        model = self._resolve(table_name)
        pk = getattr(model, self._pk_col(model))
        q = select(model).where(pk == self._coerce_id(entity_id, pk))
        row = (await self.db.execute(q)).scalar_one_or_none()
        if not row:
            return
        if hasattr(row, "is_deleted"):
            row.is_deleted = True
        else:
            await self.db.delete(row)
        await self.db.commit()

    def _to_dict(self, instance: SQLModel) -> dict:
        """Convert SQLModel instance to dict, handling datetime/uuid."""
        return {col.name: getattr(instance, col.name) for col in instance.__table__.columns}

    def _coerce_id(self, entity_id: str, pk_col) -> Any:
        """Convert string ID to the correct Python type (UUID, int, etc.)."""
        if str(pk_col.type) == "UUID":
            return uuid.UUID(entity_id)
        return entity_id
