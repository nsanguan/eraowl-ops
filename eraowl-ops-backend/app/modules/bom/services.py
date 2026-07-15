import uuid
from datetime import date
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text
from sqlalchemy.sql import func

from app.modules.bom.models import BomHeader, BomComponent
from app.modules.bom.schemas import (
    BomHeaderCreate,
    BomHeaderUpdate,
    BomComponentCreate,
    BomComponentUpdate,
    BomExplodeItem,
)
from app.modules.bom.exceptions import BomNotFoundError, BomCircularReferenceError


class BomService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def _paginate(self, model, page: int, page_size: int, filters: dict | None = None):
        query = select(model).where(model.is_deleted == False)
        if filters:
            for col, val in filters.items():
                query = query.where(getattr(model, col) == val)
        count_q = select(func.count()).select_from(query.subquery())
        total = (await self.db.execute(count_q)).scalar() or 0
        rows = (await self.db.execute(query.offset((page - 1) * page_size).limit(page_size))).scalars().all()
        return list(rows), total

    async def _get_by_id(self, model, entity_id: uuid.UUID):
        pk_col = next(iter(model.__table__.primary_key.columns))
        row = (await self.db.execute(
            select(model).where(pk_col == entity_id, model.is_deleted == False)
        )).scalar_one_or_none()
        if not row:
            raise BomNotFoundError(entity=model.__name__)
        return row

    async def _create(self, model, data):
        instance = model(**data.model_dump())
        self.db.add(instance)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def _update(self, model, entity_id: uuid.UUID, data):
        instance = await self._get_by_id(model, entity_id)
        for key, val in data.model_dump(exclude_unset=True).items():
            setattr(instance, key, val)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def _delete(self, model, entity_id: uuid.UUID):
        instance = await self._get_by_id(model, entity_id)
        instance.is_deleted = True
        await self.db.commit()

    # --- Bom Headers ---
    async def list_bom_headers(self, page: int = 1, page_size: int = 20, item_id: uuid.UUID | None = None):
        from app.modules.mdm.item.models import Item

        base_q = select(BomHeader).where(BomHeader.is_deleted == False)
        if item_id:
            base_q = base_q.where(BomHeader.item_id == item_id)

        total = (await self.db.execute(
            select(func.count()).select_from(base_q.subquery())
        )).scalar() or 0

        rows = (await self.db.execute(
            base_q.offset((page - 1) * page_size).limit(page_size)
        )).scalars().all()

        if not rows:
            return [], total

        item_ids = [r.item_id for r in rows]
        code_result = await self.db.execute(
            select(Item.item_id, Item.item_code).where(Item.item_id.in_(item_ids))
        )
        code_map = {row[0]: row[1] for row in code_result.all()}

        items = []
        for row in rows:
            items.append({
                "bom_header_id": row.bom_header_id,
                "item_id": row.item_id,
                "item_code": code_map.get(row.item_id, "UNKNOWN"),
                "alternate_bom_code": row.alternate_bom_code,
                "revision": row.revision,
                "status": row.status,
                "effective_date_from": row.effective_date_from,
                "effective_date_to": row.effective_date_to,
                "is_deleted": row.is_deleted,
                "created_at": row.created_at,
                "updated_at": row.updated_at,
            })

        return items, total

    async def get_bom_header(self, entity_id: uuid.UUID):
        from app.modules.mdm.item.models import Item

        header = await self._get_by_id(BomHeader, entity_id)
        code_result = await self.db.execute(
            select(Item.item_code).where(Item.item_id == header.item_id)
        )
        item_code = code_result.scalar_one_or_none() or "UNKNOWN"

        return {
            "bom_header_id": header.bom_header_id,
            "item_id": header.item_id,
            "item_code": item_code,
            "alternate_bom_code": header.alternate_bom_code,
            "revision": header.revision,
            "status": header.status,
            "effective_date_from": header.effective_date_from,
            "effective_date_to": header.effective_date_to,
            "is_deleted": header.is_deleted,
            "created_at": header.created_at,
            "updated_at": header.updated_at,
        }

    async def create_bom_header(self, data: BomHeaderCreate):
        return await self._create(BomHeader, data)

    async def update_bom_header(self, entity_id: uuid.UUID, data: BomHeaderUpdate):
        return await self._update(BomHeader, entity_id, data)

    async def delete_bom_header(self, entity_id: uuid.UUID):
        await self._delete(BomHeader, entity_id)

    # --- Bom Lines ---
    async def list_bom_components(
        self, page: int = 1, page_size: int = 20, bom_header_id: uuid.UUID | None = None
    ):
        filters = {"bom_header_id": bom_header_id} if bom_header_id else None
        return await self._paginate(BomComponent, page, page_size, filters)

    async def get_bom_component(self, entity_id: uuid.UUID):
        return await self._get_by_id(BomComponent, entity_id)

    async def create_bom_component(self, data: BomComponentCreate):
        header = await self._get_by_id(BomHeader, data.bom_header_id)
        await self.validate_no_circular_reference(header.item_id, data.component_item_id)
        return await self._create(BomComponent, data)

    async def update_bom_component(self, entity_id: uuid.UUID, data: BomComponentUpdate):
        return await self._update(BomComponent, entity_id, data)

    async def delete_bom_component(self, entity_id: uuid.UUID):
        await self._delete(BomComponent, entity_id)

    async def validate_no_circular_reference(
        self, assembly_item_id: uuid.UUID, component_item_id: uuid.UUID
    ) -> None:
        if assembly_item_id == component_item_id:
            raise BomCircularReferenceError(
                item_id=str(component_item_id), ancestor_id=str(assembly_item_id)
            )

        visited = {component_item_id}

        async def dfs_check(current_item_id: uuid.UUID) -> bool:
            result = await self.db.execute(
                select(BomHeader).where(
                    BomHeader.item_id == current_item_id,
                    BomHeader.is_deleted == False,
                )
            )
            headers = result.scalars().all()

            for header in headers:
                lines_result = await self.db.execute(
                    select(BomComponent).where(
                        BomComponent.bom_header_id == header.bom_header_id,
                        BomComponent.is_deleted == False,
                    )
                )
                lines = lines_result.scalars().all()

                for line in lines:
                    if line.component_item_id == assembly_item_id:
                        raise BomCircularReferenceError(
                            item_id=str(component_item_id), ancestor_id=str(assembly_item_id)
                        )
                    if line.component_item_id not in visited:
                        visited.add(line.component_item_id)
                        await dfs_check(line.component_item_id)

        await dfs_check(component_item_id)

    async def approve_bom(self, bom_header_id: uuid.UUID):
        header = await self._get_by_id(BomHeader, bom_header_id)
        header.status = "ACTIVE"
        await self.db.commit()
        await self.db.refresh(header)
        return header

    async def explode_bom(self, item_id: uuid.UUID, quantity: float = 1.0) -> list[BomExplodeItem]:
        today = date.today()

        async def _explode(current_item_id: uuid.UUID, qty: float, level: int) -> list[BomExplodeItem]:
            result = await self.db.execute(
                select(BomHeader).where(
                    BomHeader.item_id == current_item_id,
                    BomHeader.status == "ACTIVE",
                    BomHeader.is_deleted == False,
                    BomHeader.effective_date_from <= today,
                    (BomHeader.effective_date_to >= today) | (BomHeader.effective_date_to == None),
                )
            )
            headers = result.scalars().all()

            items: list[BomExplodeItem] = []
            for header in headers:
                lines_result = await self.db.execute(
                    select(BomComponent).where(
                        BomComponent.bom_header_id == header.bom_header_id,
                        BomComponent.is_deleted == False,
                        BomComponent.effective_date_from <= today,
                        (BomComponent.effective_date_to >= today) | (BomComponent.effective_date_to == None),
                    )
                )
                lines = lines_result.scalars().all()

                for line in lines:
                    item_query = text(
                        "SELECT item_code, item_name FROM mdm.items WHERE item_id = :id AND is_deleted = false"
                    )
                    uom_query = text(
                        "SELECT uom_code FROM mdm.uoms WHERE uom_id = :id AND is_deleted = false"
                    )

                    item_row = (await self.db.execute(item_query, {"id": line.component_item_id})).fetchone()
                    uom_row = (await self.db.execute(uom_query, {"id": line.uom_id})).fetchone()

                    item_code = item_row[0] if item_row else "UNKNOWN"
                    item_name = item_row[1] if item_row else "UNKNOWN"
                    uom_code = uom_row[0] if uom_row else "UNKNOWN"

                    line_qty = qty * line.quantity_per
                    children = await _explode(line.component_item_id, line_qty, level + 1)

                    items.append(
                        BomExplodeItem(
                            item_id=current_item_id,
                            component_item_id=line.component_item_id,
                            item_code=item_code,
                            item_name=item_name,
                            quantity_per=line_qty,
                            uom_code=uom_code,
                            level=level,
                            children=children,
                        )
                    )

            return items

        return await _explode(item_id, quantity, 0)
