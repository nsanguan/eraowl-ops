"""
Base CRUD Service — Global Module Design
=========================================

Thin CRUD service that every entity in every module can reuse.
Eliminates repetitive list/get/create/update/delete methods.

Usage:
    class UserService(BaseCRUDService[User]):
        def __init__(self, db: AsyncSession):
            super().__init__(db, User)
"""

from __future__ import annotations

import uuid
from typing import Any, Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy import and_, func, select, text, update as sa_update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel

M = TypeVar("M", bound=SQLModel)


class PaginatedResult(BaseModel):
    """Standard paginated response — every list endpoint returns this shape."""

    items: list[Any]
    total: int
    page: int
    page_size: int
    total_pages: int


class BaseCRUDService(Generic[M]):
    """
    Generic CRUD service for any SQLModel entity.

    Provides list with pagination, get-by-id, create, update, soft-delete.
    Adapted from PO module's BasePOCrud pattern.
    """

    def __init__(self, db: AsyncSession, model: type[M]):
        self.db = db
        self.model = model

    @property
    def _pk_col(self) -> str:
        """Discover the primary key column name dynamically."""
        return list(self.model.__table__.primary_key.columns)[0].name

    async def list(
        self,
        page: int = 1,
        page_size: int = 20,
        filters: dict[str, Any] | None = None,
        search_cols: list[str] | None = None,
        search_term: str | None = None,
        order_by: Any | None = None,
    ) -> PaginatedResult:
        conditions = [self.model.is_deleted == False] if hasattr(self.model, "is_deleted") else []

        if filters:
            for col, val in filters.items():
                if val is not None:
                    conditions.append(getattr(self.model, col) == val)

        if search_term and search_cols:
            from sqlalchemy import or_
            like_patterns = [
                getattr(self.model, col).ilike(f"%{search_term}%")
                for col in search_cols
                if hasattr(self.model, col)
            ]
            if like_patterns:
                conditions.append(or_(*like_patterns))

        where = and_(*conditions) if conditions else text("TRUE")

        total_q = select(func.count()).select_from(self.model).where(where)
        total = (await self.db.execute(total_q)).scalar() or 0

        q = select(self.model).where(where)
        if order_by:
            q = q.order_by(order_by)
        else:
            q = q.order_by(self.model.created_at.desc()) if hasattr(self.model, "created_at") else q

        offset = (page - 1) * page_size
        q = q.offset(offset).limit(page_size)
        rows = (await self.db.execute(q)).scalars().all()
        total_pages = max(1, (total + page_size - 1) // page_size)

        return PaginatedResult(
            items=list(rows),
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )

    async def get(self, entity_id: uuid.UUID | str) -> M:
        from app.core.exceptions import NotFoundError

        pk = getattr(self.model, self._pk_col)
        q = select(self.model).where(pk == entity_id)
        if hasattr(self.model, "is_deleted"):
            q = q.where(self.model.is_deleted == False)
        row = (await self.db.execute(q)).scalar_one_or_none()
        if not row:
            raise NotFoundError(entity=self.model.__name__)
        return row

    async def create(self, data: BaseModel | dict[str, Any]) -> M:
        if isinstance(data, BaseModel):
            data_dict = data.model_dump(exclude_unset=True)
        else:
            data_dict = dict(data)
        instance = self.model(**data_dict)
        self.db.add(instance)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def update(self, entity_id: uuid.UUID | str, data: BaseModel | dict[str, Any]) -> M:
        instance = await self.get(entity_id)
        if isinstance(data, BaseModel):
            data_dict = data.model_dump(exclude_unset=True)
        else:
            data_dict = dict(data)
        for key, val in data_dict.items():
            if hasattr(instance, key):
                setattr(instance, key, val)
        if hasattr(instance, "object_version_number"):
            instance.object_version_number = (instance.object_version_number or 0) + 1
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def delete(self, entity_id: uuid.UUID | str) -> None:
        instance = await self.get(entity_id)
        if hasattr(instance, "is_deleted"):
            instance.is_deleted = True
        else:
            await self.db.delete(instance)
        await self.db.commit()
