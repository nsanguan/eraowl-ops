import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.sql import func

from app.modules.mdm.party.models import (
    Address, Party, PartySite, PartySiteUse, PartyRole, Supplier, Customer,
)
from app.modules.mdm.party.schemas import (
    AddressCreate, AddressUpdate,
    PartyCreate, PartyUpdate,
    PartySiteCreate, PartySiteUpdate,
    PartySiteUseCreate, PartySiteUseUpdate,
    PartyRoleCreate, PartyRoleUpdate,
    SupplierCreate, SupplierUpdate,
    CustomerCreate, CustomerUpdate,
)
from app.modules.mdm.party.exceptions import PartyNotFoundError


class PartyService:
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
            raise PartyNotFoundError(entity=model.__name__)
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

    # --- Addresses ---
    async def list_addresses(self, page: int = 1, page_size: int = 20):
        return await self._paginate(Address, page, page_size)

    async def get_address(self, entity_id: uuid.UUID):
        return await self._get_by_id(Address, entity_id)

    async def create_address(self, data: AddressCreate):
        return await self._create(Address, data)

    async def update_address(self, entity_id: uuid.UUID, data: AddressUpdate):
        return await self._update(Address, entity_id, data)

    async def delete_address(self, entity_id: uuid.UUID):
        await self._delete(Address, entity_id)

    # --- Parties ---
    async def list_parties(self, page: int = 1, page_size: int = 20, party_type: str | None = None):
        filters = {"party_type": party_type} if party_type else None
        return await self._paginate(Party, page, page_size, filters)

    async def get_party(self, entity_id: uuid.UUID):
        return await self._get_by_id(Party, entity_id)

    async def create_party(self, data: PartyCreate):
        return await self._create(Party, data)

    async def update_party(self, entity_id: uuid.UUID, data: PartyUpdate):
        return await self._update(Party, entity_id, data)

    async def delete_party(self, entity_id: uuid.UUID):
        await self._delete(Party, entity_id)

    # --- Party Sites ---
    async def list_party_sites(self, page: int = 1, page_size: int = 20, party_id: uuid.UUID | None = None):
        filters = {"party_id": party_id} if party_id else None
        return await self._paginate(PartySite, page, page_size, filters)

    async def get_party_site(self, entity_id: uuid.UUID):
        return await self._get_by_id(PartySite, entity_id)

    async def create_party_site(self, data: PartySiteCreate):
        return await self._create(PartySite, data)

    async def update_party_site(self, entity_id: uuid.UUID, data: PartySiteUpdate):
        return await self._update(PartySite, entity_id, data)

    async def delete_party_site(self, entity_id: uuid.UUID):
        await self._delete(PartySite, entity_id)

    # --- Party Site Uses ---
    async def list_party_site_uses(self, page: int = 1, page_size: int = 20, party_site_id: uuid.UUID | None = None):
        filters = {"party_site_id": party_site_id} if party_site_id else None
        return await self._paginate(PartySiteUse, page, page_size, filters)

    async def get_party_site_use(self, entity_id: uuid.UUID):
        return await self._get_by_id(PartySiteUse, entity_id)

    async def create_party_site_use(self, data: PartySiteUseCreate):
        return await self._create(PartySiteUse, data)

    async def update_party_site_use(self, entity_id: uuid.UUID, data: PartySiteUseUpdate):
        return await self._update(PartySiteUse, entity_id, data)

    async def delete_party_site_use(self, entity_id: uuid.UUID):
        await self._delete(PartySiteUse, entity_id)

    # --- Party Roles ---
    async def list_party_roles(self, page: int = 1, page_size: int = 20, party_id: uuid.UUID | None = None):
        filters = {"party_id": party_id} if party_id else None
        return await self._paginate(PartyRole, page, page_size, filters)

    async def get_party_role(self, entity_id: uuid.UUID):
        return await self._get_by_id(PartyRole, entity_id)

    async def create_party_role(self, data: PartyRoleCreate):
        return await self._create(PartyRole, data)

    async def update_party_role(self, entity_id: uuid.UUID, data: PartyRoleUpdate):
        return await self._update(PartyRole, entity_id, data)

    async def delete_party_role(self, entity_id: uuid.UUID):
        await self._delete(PartyRole, entity_id)

    # --- Suppliers ---
    async def list_suppliers(self, page: int = 1, page_size: int = 20, party_id: uuid.UUID | None = None):
        filters = {"party_id": party_id} if party_id else None
        return await self._paginate(Supplier, page, page_size, filters)

    async def get_supplier(self, entity_id: uuid.UUID):
        return await self._get_by_id(Supplier, entity_id)

    async def create_supplier(self, data: SupplierCreate):
        return await self._create(Supplier, data)

    async def update_supplier(self, entity_id: uuid.UUID, data: SupplierUpdate):
        return await self._update(Supplier, entity_id, data)

    async def delete_supplier(self, entity_id: uuid.UUID):
        await self._delete(Supplier, entity_id)

    # --- Customers ---
    async def list_customers(self, page: int = 1, page_size: int = 20, party_id: uuid.UUID | None = None):
        filters = {"party_id": party_id} if party_id else None
        return await self._paginate(Customer, page, page_size, filters)

    async def get_customer(self, entity_id: uuid.UUID):
        return await self._get_by_id(Customer, entity_id)

    async def create_customer(self, data: CustomerCreate):
        return await self._create(Customer, data)

    async def update_customer(self, entity_id: uuid.UUID, data: CustomerUpdate):
        return await self._update(Customer, entity_id, data)

    async def delete_customer(self, entity_id: uuid.UUID):
        await self._delete(Customer, entity_id)
