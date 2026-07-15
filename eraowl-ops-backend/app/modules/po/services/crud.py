import uuid

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.po.dto.schemas import (
    CreatePoLineRequest,
    CreatePoShipmentRequest,
    CreatePoDistributionRequest,
    CreatePoReleaseRequest,
    CreatePoAmendmentRequest,
    CreatePoApprovalRequest,
    UpdatePoLineRequest,
    UpdatePoShipmentRequest,
    UpdatePoDistributionRequest,
    UpdatePoReleaseRequest,
    UpdatePoAmendmentRequest,
    UpdatePoApprovalRequest,
)
from app.modules.po.models import (
    PoLine,
    PoShipment,
    PoDistribution,
    PoRelease,
    PoAmendment,
    PoApproval,
)


class BasePOCrud:
    """Generic CRUD base for PO child entities."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def _list(self, model, filters: dict | None = None, order_by=None):
        query = select(model).where(model.is_deleted == False)
        if filters:
            for col, val in filters.items():
                query = query.where(getattr(model, col) == val)
        if order_by:
            query = query.order_by(order_by)
        rows = (await self.db.execute(query)).scalars().all()
        return list(rows)

    async def _get(self, model, entity_id: uuid.UUID):
        pk_col = list(model.__table__.primary_key.columns)[0].name
        query = select(model).where(
            and_(getattr(model, pk_col) == entity_id, model.is_deleted == False)
        )
        row = (await self.db.execute(query)).scalar_one_or_none()
        if not row:
            from app.core.exceptions import NotFoundError
            raise NotFoundError(entity=model.__name__)
        return row

    async def _create(self, model, data):
        instance = model(**data.model_dump())
        self.db.add(instance)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def _update(self, model, entity_id: uuid.UUID, data):
        pk_col = list(model.__table__.primary_key.columns)[0].name
        query = select(model).where(
            and_(getattr(model, pk_col) == entity_id, model.is_deleted == False)
        )
        row = (await self.db.execute(query)).scalar_one_or_none()
        if not row:
            from app.core.exceptions import NotFoundError
            raise NotFoundError(entity=model.__name__)
        for key, val in data.model_dump(exclude_unset=True).items():
            setattr(row, key, val)
        row.object_version_number = (row.object_version_number or 0) + 1
        await self.db.commit()
        await self.db.refresh(row)
        return row

    async def _delete(self, model, entity_id: uuid.UUID):
        pk_col = list(model.__table__.primary_key.columns)[0].name
        query = select(model).where(
            and_(getattr(model, pk_col) == entity_id, model.is_deleted == False)
        )
        row = (await self.db.execute(query)).scalar_one_or_none()
        if not row:
            from app.core.exceptions import NotFoundError
            raise NotFoundError(entity=model.__name__)
        row.is_deleted = True
        await self.db.commit()


class PoLineService(BasePOCrud):
    async def list_by_po_id(self, po_id: uuid.UUID):
        return await self._list(PoLine, {"po_id": po_id}, order_by=PoLine.line_num)

    async def get(self, entity_id: uuid.UUID):
        return await self._get(PoLine, entity_id)

    async def create(self, data: CreatePoLineRequest):
        return await self._create(PoLine, data)

    async def update(self, entity_id: uuid.UUID, data: UpdatePoLineRequest):
        return await self._update(PoLine, entity_id, data)

    async def delete(self, entity_id: uuid.UUID):
        await self._delete(PoLine, entity_id)


class PoShipmentService(BasePOCrud):
    async def list_by_po_line_id(self, po_line_id: uuid.UUID):
        return await self._list(PoShipment, {"po_line_id": po_line_id}, order_by=PoShipment.shipment_num)

    async def get(self, entity_id: uuid.UUID):
        return await self._get(PoShipment, entity_id)

    async def create(self, data: CreatePoShipmentRequest):
        return await self._create(PoShipment, data)

    async def update(self, entity_id: uuid.UUID, data: UpdatePoShipmentRequest):
        return await self._update(PoShipment, entity_id, data)

    async def delete(self, entity_id: uuid.UUID):
        await self._delete(PoShipment, entity_id)


class PoDistributionService(BasePOCrud):
    async def list_by_po_shipment_id(self, po_shipment_id: uuid.UUID):
        return await self._list(PoDistribution, {"po_shipment_id": po_shipment_id}, order_by=PoDistribution.distribution_num)

    async def get(self, entity_id: uuid.UUID):
        return await self._get(PoDistribution, entity_id)

    async def create(self, data: CreatePoDistributionRequest):
        return await self._create(PoDistribution, data)

    async def update(self, entity_id: uuid.UUID, data: UpdatePoDistributionRequest):
        return await self._update(PoDistribution, entity_id, data)

    async def delete(self, entity_id: uuid.UUID):
        await self._delete(PoDistribution, entity_id)


class PoReleaseService(BasePOCrud):
    async def list_by_po_id(self, po_id: uuid.UUID):
        return await self._list(PoRelease, {"po_id": po_id}, order_by=PoRelease.release_num)

    async def get(self, entity_id: uuid.UUID):
        return await self._get(PoRelease, entity_id)

    async def create(self, data: CreatePoReleaseRequest):
        return await self._create(PoRelease, data)

    async def update(self, entity_id: uuid.UUID, data: UpdatePoReleaseRequest):
        return await self._update(PoRelease, entity_id, data)

    async def delete(self, entity_id: uuid.UUID):
        await self._delete(PoRelease, entity_id)


class PoAmendmentService(BasePOCrud):
    async def list_by_po_id(self, po_id: uuid.UUID):
        return await self._list(PoAmendment, {"po_id": po_id}, order_by=PoAmendment.amendment_num)

    async def get(self, entity_id: uuid.UUID):
        return await self._get(PoAmendment, entity_id)

    async def create(self, data: CreatePoAmendmentRequest):
        return await self._create(PoAmendment, data)

    async def update(self, entity_id: uuid.UUID, data: UpdatePoAmendmentRequest):
        return await self._update(PoAmendment, entity_id, data)

    async def delete(self, entity_id: uuid.UUID):
        await self._delete(PoAmendment, entity_id)


class PoApprovalService(BasePOCrud):
    async def list_by_po_id(self, po_id: uuid.UUID):
        return await self._list(PoApproval, {"po_id": po_id}, order_by=PoApproval.approval_level)

    async def get(self, entity_id: uuid.UUID):
        return await self._get(PoApproval, entity_id)

    async def create(self, data: CreatePoApprovalRequest):
        return await self._create(PoApproval, data)

    async def update(self, entity_id: uuid.UUID, data: UpdatePoApprovalRequest):
        return await self._update(PoApproval, entity_id, data)

    async def delete(self, entity_id: uuid.UUID):
        await self._delete(PoApproval, entity_id)
