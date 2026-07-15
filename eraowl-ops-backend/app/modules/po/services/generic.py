import uuid
from datetime import datetime

from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.po.models import (
    PoAmendment,
    PoApproval,
    PoDistribution,
    PoHeader,
    PoLine,
    PoRelease,
    PoShipment,
)


class GenericPoService:
    """
    Dynamic CRUD for any PO table by name.
    Mirrors axon-os GenericService pattern with allowlist.
    """

    ALLOWED_TABLES = {
        "po_headers": PoHeader,
        "po_lines": PoLine,
        "po_shipments": PoShipment,
        "po_distributions": PoDistribution,
        "po_releases": PoRelease,
        "po_amendments": PoAmendment,
        "po_approvals": PoApproval,
    }

    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_all(self, table_name: str, filters: dict | None = None) -> list:
        model = self._resolve(table_name)
        query = select(model)

        has_is_deleted = hasattr(model, "is_deleted")
        if has_is_deleted:
            query = query.where(model.is_deleted == False)

        if filters:
            for col, val in filters.items():
                if hasattr(model, col):
                    query = query.where(getattr(model, col) == val)

        rows = (await self.db.execute(query)).scalars().all()
        return [self._to_dict(r) for r in rows]

    async def get_one(self, table_name: str, entity_id: str) -> dict:
        model = self._resolve(table_name)
        pk_col = list(model.__table__.primary_key.columns)[0].name
        pk_val = self._coerce_pk(pk_col, entity_id)

        query = select(model).where(getattr(model, pk_col) == pk_val)
        if hasattr(model, "is_deleted"):
            query = query.where(model.is_deleted == False)

        row = (await self.db.execute(query)).scalar_one_or_none()
        if not row:
            from app.core.exceptions import NotFoundError
            raise NotFoundError(entity=f"{table_name}[{entity_id}]")
        return self._to_dict(row)

    async def create(self, table_name: str, data: dict) -> dict:
        model = self._resolve(table_name)
        filtered = self._filter_columns(model, data)
        instance = model(**filtered)
        self.db.add(instance)
        await self.db.commit()
        await self.db.refresh(instance)
        return self._to_dict(instance)

    async def update(self, table_name: str, entity_id: str, data: dict) -> dict:
        model = self._resolve(table_name)
        pk_col = list(model.__table__.primary_key.columns)[0].name
        pk_val = self._coerce_pk(pk_col, entity_id)

        query = select(model).where(getattr(model, pk_col) == pk_val)
        if hasattr(model, "is_deleted"):
            query = query.where(model.is_deleted == False)

        row = (await self.db.execute(query)).scalar_one_or_none()
        if not row:
            from app.core.exceptions import NotFoundError
            raise NotFoundError(entity=f"{table_name}[{entity_id}]")

        filtered = self._filter_columns(model, data, exclude_pk=True)
        for key, val in filtered.items():
            setattr(row, key, val)

        if hasattr(row, "object_version_number"):
            row.object_version_number = (row.object_version_number or 0) + 1

        await self.db.commit()
        await self.db.refresh(row)
        return self._to_dict(row)

    async def delete(self, table_name: str, entity_id: str) -> None:
        model = self._resolve(table_name)
        pk_col = list(model.__table__.primary_key.columns)[0].name
        pk_val = self._coerce_pk(pk_col, entity_id)

        query = select(model).where(getattr(model, pk_col) == pk_val)
        if hasattr(model, "is_deleted"):
            query = query.where(model.is_deleted == False)

        row = (await self.db.execute(query)).scalar_one_or_none()
        if not row:
            from app.core.exceptions import NotFoundError
            raise NotFoundError(entity=f"{table_name}[{entity_id}]")

        if hasattr(row, "is_deleted"):
            row.is_deleted = True
        else:
            await self.db.delete(row)

        await self.db.commit()

    def _resolve(self, table_name: str):
        model = self.ALLOWED_TABLES.get(table_name)
        if not model:
            from app.core.exceptions import NotFoundError
            raise NotFoundError(entity=f"Table '{table_name}'")
        return model

    def _filter_columns(self, model, data: dict, exclude_pk: bool = False) -> dict:
        pk_names = {c.name for c in model.__table__.primary_key.columns}
        col_names = {c.name for c in model.__table__.columns}
        filtered = {}
        for key, val in data.items():
            if key not in col_names:
                continue
            if exclude_pk and key in pk_names:
                continue
            filtered[key] = val
        return filtered

    def _coerce_pk(self, pk_col: str, value: str):
        """Coerce a string PK value to the appropriate type (uuid, int, etc.)."""
        if "id" in pk_col.lower():
            try:
                return uuid.UUID(value)
            except ValueError:
                pass
        return value

    def _to_dict(self, instance) -> dict:
        result = {}
        for column in instance.__table__.columns:
            val = getattr(instance, column.name)
            if isinstance(val, uuid.UUID):
                result[column.name] = str(val)
            elif isinstance(val, datetime):
                result[column.name] = val.isoformat()
            else:
                result[column.name] = val
        return result
