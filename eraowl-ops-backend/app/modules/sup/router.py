import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.sup.services import (
    PortalUserService,
    RfqResponseService,
    ShipmentAdviceService,
)
from app.modules.sup.schemas import (
    PortalUserCreate,
    PortalUserUpdate,
    PortalUserOut,
    RfqResponseCreate,
    RfqResponseUpdate,
    RfqResponseOut,
    ShipmentAdviceCreate,
    ShipmentAdviceUpdate,
    ShipmentAdviceOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


# --- Portal Users ---
@router.get("/portal_users", response_model=PaginatedResponse[PortalUserOut])
async def list_portal_users(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "view"),
):
    svc = PortalUserService(db)
    result = await svc.list(page, page_size, search_cols=["email", "full_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())


@router.get("/portal_users/{entity_id}", response_model=PortalUserOut)
async def get_portal_user(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "view"),
):
    svc = PortalUserService(db)
    return await svc.get(entity_id)


@router.post("/portal_users", response_model=PortalUserOut, status_code=status.HTTP_201_CREATED)
async def create_portal_user(
    data: PortalUserCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "manage"),
):
    svc = PortalUserService(db)
    return await svc.create(data)


@router.put("/portal_users/{entity_id}", response_model=PortalUserOut)
async def update_portal_user(
    entity_id: uuid.UUID,
    data: PortalUserUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "manage"),
):
    svc = PortalUserService(db)
    return await svc.update(entity_id, data)


@router.delete("/portal_users/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_portal_user(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "manage"),
):
    svc = PortalUserService(db)
    await svc.delete(entity_id)


# --- RFQ Responses ---
@router.get("/rfq_responses", response_model=PaginatedResponse[RfqResponseOut])
async def list_rfq_responses(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "view"),
):
    svc = RfqResponseService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())


@router.get("/rfq_responses/{entity_id}", response_model=RfqResponseOut)
async def get_rfq_response(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "view"),
):
    svc = RfqResponseService(db)
    return await svc.get(entity_id)


@router.post("/rfq_responses", response_model=RfqResponseOut, status_code=status.HTTP_201_CREATED)
async def create_rfq_response(
    data: RfqResponseCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "manage"),
):
    svc = RfqResponseService(db)
    return await svc.create(data)


@router.put("/rfq_responses/{entity_id}", response_model=RfqResponseOut)
async def update_rfq_response(
    entity_id: uuid.UUID,
    data: RfqResponseUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "manage"),
):
    svc = RfqResponseService(db)
    return await svc.update(entity_id, data)


@router.delete("/rfq_responses/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_rfq_response(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "manage"),
):
    svc = RfqResponseService(db)
    await svc.delete(entity_id)


# --- Shipment Advices (ASN) ---
@router.get("/shipment_advices", response_model=PaginatedResponse[ShipmentAdviceOut])
async def list_shipment_advices(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "view"),
):
    svc = ShipmentAdviceService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())


@router.get("/shipment_advices/{entity_id}", response_model=ShipmentAdviceOut)
async def get_shipment_advice(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "view"),
):
    svc = ShipmentAdviceService(db)
    return await svc.get(entity_id)


@router.post("/shipment_advices", response_model=ShipmentAdviceOut, status_code=status.HTTP_201_CREATED)
async def create_shipment_advice(
    data: ShipmentAdviceCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "manage"),
):
    svc = ShipmentAdviceService(db)
    return await svc.create(data)


@router.put("/shipment_advices/{entity_id}", response_model=ShipmentAdviceOut)
async def update_shipment_advice(
    entity_id: uuid.UUID,
    data: ShipmentAdviceUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "manage"),
):
    svc = ShipmentAdviceService(db)
    return await svc.update(entity_id, data)


@router.delete("/shipment_advices/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shipment_advice(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("sup", "manage"),
):
    svc = ShipmentAdviceService(db)
    await svc.delete(entity_id)
