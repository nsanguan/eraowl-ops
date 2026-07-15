import uuid
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.mdm.party.services import PartyService
from app.modules.mdm.party.schemas import (
    AddressOut, AddressCreate, AddressUpdate,
    PartyOut, PartyCreate, PartyUpdate,
    PartySiteOut, PartySiteCreate, PartySiteUpdate,
    PartySiteUseOut, PartySiteUseCreate, PartySiteUseUpdate,
    PartyRoleOut, PartyRoleCreate, PartyRoleUpdate,
    SupplierOut, SupplierCreate, SupplierUpdate,
    CustomerOut, CustomerCreate, CustomerUpdate,
    CompositePartyCreate, TcaPartyView,
    TreeResponse, TreeUpdateRequest,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


def _build_paginated(items, total, page, page_size):
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


# --- TCA Composite ---
@router.post("/parties/composite", response_model=TcaPartyView, status_code=201)
async def create_composite_party(
    data: CompositePartyCreate,
    db: AsyncSession = Depends(get_db),
):
    svc = PartyService(db)
    party = await svc.create_composite_party(data)
    return await svc.get_tca_view(party.party_id)


@router.get("/parties/{party_id}/tca-view", response_model=TcaPartyView)
async def get_tca_view(
    party_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
):
    svc = PartyService(db)
    return await svc.get_tca_view(party_id)


# --- TCA Tree ---
@router.get("/parties/{party_id}/tree", response_model=TreeResponse)
async def get_party_tree(
    party_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
):
    svc = PartyService(db)
    tree = await svc.get_party_tree(party_id)
    return {"tree": tree}


@router.post("/parties/{party_id}/tree/update-node", status_code=204)
async def update_tree_node(
    party_id: uuid.UUID,
    data: TreeUpdateRequest,
    db: AsyncSession = Depends(get_db),
):
    svc = PartyService(db)
    await svc.update_tree_node(party_id, data.node_type, data.action, data.entity)


# --- Addresses ---
@router.get("/addresses", response_model=PaginatedResponse[AddressOut])
async def list_addresses(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    svc = PartyService(db)
    items, total = await svc.list_addresses(page, page_size)
    return _build_paginated(items, total, page, page_size)


@router.get("/addresses/{entity_id}", response_model=AddressOut)
async def get_address(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.get_address(entity_id)


@router.post("/addresses", response_model=AddressOut, status_code=201)
async def create_address(data: AddressCreate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.create_address(data)


@router.put("/addresses/{entity_id}", response_model=AddressOut)
async def update_address(entity_id: uuid.UUID, data: AddressUpdate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.update_address(entity_id, data)


@router.delete("/addresses/{entity_id}", status_code=204)
async def delete_address(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    await svc.delete_address(entity_id)


# --- Parties ---
@router.get("/parties", response_model=PaginatedResponse[PartyOut])
async def list_parties(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    party_type: str | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = PartyService(db)
    items, total = await svc.list_parties(page, page_size, party_type)
    return _build_paginated(items, total, page, page_size)


@router.get("/parties/{entity_id}", response_model=PartyOut)
async def get_party(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.get_party(entity_id)


@router.post("/parties", response_model=PartyOut, status_code=201)
async def create_party(data: PartyCreate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.create_party(data)


@router.put("/parties/{entity_id}", response_model=PartyOut)
async def update_party(entity_id: uuid.UUID, data: PartyUpdate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.update_party(entity_id, data)


@router.delete("/parties/{entity_id}", status_code=204)
async def delete_party(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    await svc.delete_party(entity_id)


# --- Party Sites ---
@router.get("/party-sites", response_model=PaginatedResponse[PartySiteOut])
async def list_party_sites(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    party_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = PartyService(db)
    items, total = await svc.list_party_sites(page, page_size, party_id)
    return _build_paginated(items, total, page, page_size)


@router.get("/party-sites/{entity_id}", response_model=PartySiteOut)
async def get_party_site(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.get_party_site(entity_id)


@router.post("/party-sites", response_model=PartySiteOut, status_code=201)
async def create_party_site(data: PartySiteCreate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.create_party_site(data)


@router.put("/party-sites/{entity_id}", response_model=PartySiteOut)
async def update_party_site(entity_id: uuid.UUID, data: PartySiteUpdate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.update_party_site(entity_id, data)


@router.delete("/party-sites/{entity_id}", status_code=204)
async def delete_party_site(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    await svc.delete_party_site(entity_id)


# --- Party Site Uses ---
@router.get("/party-site-uses", response_model=PaginatedResponse[PartySiteUseOut])
async def list_party_site_uses(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    party_site_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = PartyService(db)
    items, total = await svc.list_party_site_uses(page, page_size, party_site_id)
    return _build_paginated(items, total, page, page_size)


@router.get("/party-site-uses/{entity_id}", response_model=PartySiteUseOut)
async def get_party_site_use(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.get_party_site_use(entity_id)


@router.post("/party-site-uses", response_model=PartySiteUseOut, status_code=201)
async def create_party_site_use(data: PartySiteUseCreate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.create_party_site_use(data)


@router.put("/party-site-uses/{entity_id}", response_model=PartySiteUseOut)
async def update_party_site_use(entity_id: uuid.UUID, data: PartySiteUseUpdate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.update_party_site_use(entity_id, data)


@router.delete("/party-site-uses/{entity_id}", status_code=204)
async def delete_party_site_use(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    await svc.delete_party_site_use(entity_id)


# --- Party Roles ---
@router.get("/party-roles", response_model=PaginatedResponse[PartyRoleOut])
async def list_party_roles(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    party_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = PartyService(db)
    items, total = await svc.list_party_roles(page, page_size, party_id)
    return _build_paginated(items, total, page, page_size)


@router.get("/party-roles/{entity_id}", response_model=PartyRoleOut)
async def get_party_role(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.get_party_role(entity_id)


@router.post("/party-roles", response_model=PartyRoleOut, status_code=201)
async def create_party_role(data: PartyRoleCreate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.create_party_role(data)


@router.put("/party-roles/{entity_id}", response_model=PartyRoleOut)
async def update_party_role(entity_id: uuid.UUID, data: PartyRoleUpdate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.update_party_role(entity_id, data)


@router.delete("/party-roles/{entity_id}", status_code=204)
async def delete_party_role(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    await svc.delete_party_role(entity_id)


# --- Suppliers ---
@router.get("/suppliers", response_model=PaginatedResponse[SupplierOut])
async def list_suppliers(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    party_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = PartyService(db)
    items, total = await svc.list_suppliers(page, page_size, party_id)
    return _build_paginated(items, total, page, page_size)


@router.get("/suppliers/{entity_id}", response_model=SupplierOut)
async def get_supplier(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.get_supplier(entity_id)


@router.post("/suppliers", response_model=SupplierOut, status_code=201)
async def create_supplier(data: SupplierCreate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.create_supplier(data)


@router.put("/suppliers/{entity_id}", response_model=SupplierOut)
async def update_supplier(entity_id: uuid.UUID, data: SupplierUpdate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.update_supplier(entity_id, data)


@router.delete("/suppliers/{entity_id}", status_code=204)
async def delete_supplier(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    await svc.delete_supplier(entity_id)


# --- Customers ---
@router.get("/customers", response_model=PaginatedResponse[CustomerOut])
async def list_customers(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    party_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    svc = PartyService(db)
    items, total = await svc.list_customers(page, page_size, party_id)
    return _build_paginated(items, total, page, page_size)


@router.get("/customers/{entity_id}", response_model=CustomerOut)
async def get_customer(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.get_customer(entity_id)


@router.post("/customers", response_model=CustomerOut, status_code=201)
async def create_customer(data: CustomerCreate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.create_customer(data)


@router.put("/customers/{entity_id}", response_model=CustomerOut)
async def update_customer(entity_id: uuid.UUID, data: CustomerUpdate, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    return await svc.update_customer(entity_id, data)


@router.delete("/customers/{entity_id}", status_code=204)
async def delete_customer(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    svc = PartyService(db)
    await svc.delete_customer(entity_id)
