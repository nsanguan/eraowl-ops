import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.sql import func

from app.modules.mdm.org_structure.models import (
    OrgCorporate, OrgCompany, OrgBusinessUnit,
    OrgSite, OrgWarehouse, OrgWarehouseLocator,
)
from app.modules.mdm.org_structure.schemas import (
    OrgCorporateCreate, OrgCorporateUpdate,
    OrgCompanyCreate, OrgCompanyUpdate,
    OrgBusinessUnitCreate, OrgBusinessUnitUpdate,
    OrgSiteCreate, OrgSiteUpdate,
    OrgWarehouseCreate, OrgWarehouseUpdate,
    OrgWarehouseLocatorCreate, OrgWarehouseLocatorUpdate,
)
from app.modules.mdm.org_structure.exceptions import OrgStructureNotFoundError


class OrgStructureService:
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
            raise OrgStructureNotFoundError(entity=model.__name__)
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

    # --- Corporates ---
    async def list_corporates(self, page: int = 1, page_size: int = 20):
        return await self._paginate(OrgCorporate, page, page_size)

    async def get_corporate(self, entity_id: uuid.UUID):
        return await self._get_by_id(OrgCorporate, entity_id)

    async def create_corporate(self, data: OrgCorporateCreate):
        return await self._create(OrgCorporate, data)

    async def update_corporate(self, entity_id: uuid.UUID, data: OrgCorporateUpdate):
        return await self._update(OrgCorporate, entity_id, data)

    async def delete_corporate(self, entity_id: uuid.UUID):
        await self._delete(OrgCorporate, entity_id)

    # --- Companies ---
    async def list_companies(self, page: int = 1, page_size: int = 20):
        return await self._paginate(OrgCompany, page, page_size)

    async def get_company(self, entity_id: uuid.UUID):
        return await self._get_by_id(OrgCompany, entity_id)

    async def create_company(self, data: OrgCompanyCreate):
        return await self._create(OrgCompany, data)

    async def update_company(self, entity_id: uuid.UUID, data: OrgCompanyUpdate):
        return await self._update(OrgCompany, entity_id, data)

    async def delete_company(self, entity_id: uuid.UUID):
        await self._delete(OrgCompany, entity_id)

    # --- Business Units ---
    async def list_business_units(self, page: int = 1, page_size: int = 20, company_id: uuid.UUID | None = None):
        filters = {"company_id": company_id} if company_id else None
        return await self._paginate(OrgBusinessUnit, page, page_size, filters)

    async def get_business_unit(self, entity_id: uuid.UUID):
        return await self._get_by_id(OrgBusinessUnit, entity_id)

    async def create_business_unit(self, data: OrgBusinessUnitCreate):
        return await self._create(OrgBusinessUnit, data)

    async def update_business_unit(self, entity_id: uuid.UUID, data: OrgBusinessUnitUpdate):
        return await self._update(OrgBusinessUnit, entity_id, data)

    async def delete_business_unit(self, entity_id: uuid.UUID):
        await self._delete(OrgBusinessUnit, entity_id)

    # --- Sites ---
    async def list_sites(self, page: int = 1, page_size: int = 20, business_unit_id: uuid.UUID | None = None):
        filters = {"business_unit_id": business_unit_id} if business_unit_id else None
        return await self._paginate(OrgSite, page, page_size, filters)

    async def get_site(self, entity_id: uuid.UUID):
        return await self._get_by_id(OrgSite, entity_id)

    async def create_site(self, data: OrgSiteCreate):
        return await self._create(OrgSite, data)

    async def update_site(self, entity_id: uuid.UUID, data: OrgSiteUpdate):
        return await self._update(OrgSite, entity_id, data)

    async def delete_site(self, entity_id: uuid.UUID):
        await self._delete(OrgSite, entity_id)

    # --- Warehouses ---
    async def list_warehouses(self, page: int = 1, page_size: int = 20, site_id: uuid.UUID | None = None):
        filters = {"site_id": site_id} if site_id else None
        return await self._paginate(OrgWarehouse, page, page_size, filters)

    async def get_warehouse(self, entity_id: uuid.UUID):
        return await self._get_by_id(OrgWarehouse, entity_id)

    async def create_warehouse(self, data: OrgWarehouseCreate):
        return await self._create(OrgWarehouse, data)

    async def update_warehouse(self, entity_id: uuid.UUID, data: OrgWarehouseUpdate):
        return await self._update(OrgWarehouse, entity_id, data)

    async def delete_warehouse(self, entity_id: uuid.UUID):
        await self._delete(OrgWarehouse, entity_id)

    # --- Warehouse Locators ---
    async def list_locators(self, page: int = 1, page_size: int = 20, warehouse_id: uuid.UUID | None = None):
        filters = {"warehouse_id": warehouse_id} if warehouse_id else None
        return await self._paginate(OrgWarehouseLocator, page, page_size, filters)

    async def get_locator(self, entity_id: uuid.UUID):
        return await self._get_by_id(OrgWarehouseLocator, entity_id)

    async def create_locator(self, data: OrgWarehouseLocatorCreate):
        return await self._create(OrgWarehouseLocator, data)

    async def update_locator(self, entity_id: uuid.UUID, data: OrgWarehouseLocatorUpdate):
        return await self._update(OrgWarehouseLocator, entity_id, data)

    async def delete_locator(self, entity_id: uuid.UUID):
        await self._delete(OrgWarehouseLocator, entity_id)
