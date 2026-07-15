import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.sql import func

from app.modules.mdm.item.models import (
    Uom,
    UomConversion,
    ItemCategory,
    Item,
    ItemCategoryAssignment,
    ItemOrganization,
    ItemSupplierXref,
)
from app.modules.mdm.item.schemas import (
    UomCreate,
    UomUpdate,
    UomConversionCreate,
    UomConversionUpdate,
    ItemCategoryCreate,
    ItemCategoryUpdate,
    ItemCreate,
    ItemUpdate,
    ItemCategoryAssignmentCreate,
    ItemCategoryAssignmentUpdate,
    ItemOrganizationCreate,
    ItemOrganizationUpdate,
    ItemSupplierXrefCreate,
    ItemSupplierXrefUpdate,
)
from app.modules.mdm.item.exceptions import ItemNotFoundError


class ItemService:
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
            raise ItemNotFoundError(entity=model.__name__)
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

    # --- UOMs ---
    async def list_uoms(self, page: int = 1, page_size: int = 20):
        return await self._paginate(Uom, page, page_size)

    async def get_uom(self, entity_id: uuid.UUID):
        return await self._get_by_id(Uom, entity_id)

    async def create_uom(self, data: UomCreate):
        return await self._create(Uom, data)

    async def update_uom(self, entity_id: uuid.UUID, data: UomUpdate):
        return await self._update(Uom, entity_id, data)

    async def delete_uom(self, entity_id: uuid.UUID):
        await self._delete(Uom, entity_id)

    # --- UOM Conversions ---
    async def list_uom_conversions(
        self,
        page: int = 1,
        page_size: int = 20,
        from_uom_id: uuid.UUID | None = None,
        to_uom_id: uuid.UUID | None = None,
        item_id: uuid.UUID | None = None,
    ):
        filters = {}
        if from_uom_id:
            filters["from_uom_id"] = from_uom_id
        if to_uom_id:
            filters["to_uom_id"] = to_uom_id
        if item_id:
            filters["item_id"] = item_id
        return await self._paginate(UomConversion, page, page_size, filters or None)

    async def get_uom_conversion(self, entity_id: uuid.UUID):
        return await self._get_by_id(UomConversion, entity_id)

    async def create_uom_conversion(self, data: UomConversionCreate):
        return await self._create(UomConversion, data)

    async def update_uom_conversion(self, entity_id: uuid.UUID, data: UomConversionUpdate):
        return await self._update(UomConversion, entity_id, data)

    async def delete_uom_conversion(self, entity_id: uuid.UUID):
        await self._delete(UomConversion, entity_id)

    # --- Item Categories ---
    async def list_item_categories(
        self,
        page: int = 1,
        page_size: int = 20,
        category_set: str | None = None,
        parent_category_id: uuid.UUID | None = None,
    ):
        filters = {}
        if category_set:
            filters["category_set"] = category_set
        if parent_category_id:
            filters["parent_category_id"] = parent_category_id
        return await self._paginate(ItemCategory, page, page_size, filters or None)

    async def get_item_category(self, entity_id: uuid.UUID):
        return await self._get_by_id(ItemCategory, entity_id)

    async def create_item_category(self, data: ItemCategoryCreate):
        return await self._create(ItemCategory, data)

    async def update_item_category(self, entity_id: uuid.UUID, data: ItemCategoryUpdate):
        return await self._update(ItemCategory, entity_id, data)

    async def delete_item_category(self, entity_id: uuid.UUID):
        await self._delete(ItemCategory, entity_id)

    # --- Items ---
    async def list_items(
        self,
        page: int = 1,
        page_size: int = 20,
        item_type: str | None = None,
        status: str | None = None,
        primary_uom_id: uuid.UUID | None = None,
    ):
        filters = {}
        if item_type:
            filters["item_type"] = item_type
        if status:
            filters["status"] = status
        if primary_uom_id:
            filters["primary_uom_id"] = primary_uom_id
        return await self._paginate(Item, page, page_size, filters or None)

    async def get_item(self, entity_id: uuid.UUID):
        return await self._get_by_id(Item, entity_id)

    async def create_item(self, data: ItemCreate):
        return await self._create(Item, data)

    async def update_item(self, entity_id: uuid.UUID, data: ItemUpdate):
        return await self._update(Item, entity_id, data)

    async def delete_item(self, entity_id: uuid.UUID):
        await self._delete(Item, entity_id)

    # --- Item Category Assignments ---
    async def list_item_category_assignments(
        self,
        page: int = 1,
        page_size: int = 20,
        item_id: uuid.UUID | None = None,
        category_id: uuid.UUID | None = None,
    ):
        filters = {}
        if item_id:
            filters["item_id"] = item_id
        if category_id:
            filters["category_id"] = category_id
        return await self._paginate(ItemCategoryAssignment, page, page_size, filters or None)

    async def get_item_category_assignment(self, entity_id: uuid.UUID):
        return await self._get_by_id(ItemCategoryAssignment, entity_id)

    async def create_item_category_assignment(self, data: ItemCategoryAssignmentCreate):
        return await self._create(ItemCategoryAssignment, data)

    async def update_item_category_assignment(self, entity_id: uuid.UUID, data: ItemCategoryAssignmentUpdate):
        return await self._update(ItemCategoryAssignment, entity_id, data)

    async def delete_item_category_assignment(self, entity_id: uuid.UUID):
        await self._delete(ItemCategoryAssignment, entity_id)

    # --- Item Organizations ---
    async def list_item_organizations(
        self,
        page: int = 1,
        page_size: int = 20,
        item_id: uuid.UUID | None = None,
        warehouse_id: uuid.UUID | None = None,
    ):
        filters = {}
        if item_id:
            filters["item_id"] = item_id
        if warehouse_id:
            filters["warehouse_id"] = warehouse_id
        return await self._paginate(ItemOrganization, page, page_size, filters or None)

    async def get_item_organization(self, entity_id: uuid.UUID):
        return await self._get_by_id(ItemOrganization, entity_id)

    async def create_item_organization(self, data: ItemOrganizationCreate):
        return await self._create(ItemOrganization, data)

    async def update_item_organization(self, entity_id: uuid.UUID, data: ItemOrganizationUpdate):
        return await self._update(ItemOrganization, entity_id, data)

    async def delete_item_organization(self, entity_id: uuid.UUID):
        await self._delete(ItemOrganization, entity_id)

    # --- Item Supplier Xrefs ---
    async def list_item_supplier_xrefs(
        self,
        page: int = 1,
        page_size: int = 20,
        item_id: uuid.UUID | None = None,
        supplier_id: uuid.UUID | None = None,
    ):
        filters = {}
        if item_id:
            filters["item_id"] = item_id
        if supplier_id:
            filters["supplier_id"] = supplier_id
        return await self._paginate(ItemSupplierXref, page, page_size, filters or None)

    async def get_item_supplier_xref(self, entity_id: uuid.UUID):
        return await self._get_by_id(ItemSupplierXref, entity_id)

    async def create_item_supplier_xref(self, data: ItemSupplierXrefCreate):
        return await self._create(ItemSupplierXref, data)

    async def update_item_supplier_xref(self, entity_id: uuid.UUID, data: ItemSupplierXrefUpdate):
        return await self._update(ItemSupplierXref, entity_id, data)

    async def delete_item_supplier_xref(self, entity_id: uuid.UUID):
        await self._delete(ItemSupplierXref, entity_id)
