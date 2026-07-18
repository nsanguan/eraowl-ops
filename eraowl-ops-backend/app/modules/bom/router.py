import uuid
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.bom.services import BomService
from app.modules.bom.schemas import (
    BomHeaderOut,
    BomHeaderCreate,
    BomHeaderUpdate,
    BomComponentOut,
    BomComponentCreate,
    BomComponentUpdate,
    BomExplodeItem,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


# --- Bom Headers ---
@router.get("/bom-headers", response_model=PaginatedResponse[BomHeaderOut])
async def list_bom_headers(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    item_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("bom", "view"),
):
    svc = BomService(db)
    items, total = await svc.list_bom_headers(page, page_size, item_id)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/bom-headers/{entity_id}", response_model=BomHeaderOut)
async def get_bom_header(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("bom", "view"),
):
    svc = BomService(db)
    return await svc.get_bom_header(entity_id)


@router.post("/bom-headers", response_model=BomHeaderOut, status_code=201)
async def create_bom_header(
    data: BomHeaderCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("bom", "create"),
):
    svc = BomService(db)
    return await svc.create_bom_header(data)


@router.put("/bom-headers/{entity_id}", response_model=BomHeaderOut)
async def update_bom_header(
    entity_id: uuid.UUID,
    data: BomHeaderUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("bom", "edit"),
):
    svc = BomService(db)
    return await svc.update_bom_header(entity_id, data)


@router.delete("/bom-headers/{entity_id}", status_code=204)
async def delete_bom_header(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("bom", "edit"),
):
    svc = BomService(db)
    await svc.delete_bom_header(entity_id)


@router.post("/bom-headers/{entity_id}/approve", response_model=BomHeaderOut)
async def approve_bom(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("bom", "approve"),
):
    svc = BomService(db)
    return await svc.approve_bom(entity_id)


@router.get("/bom-headers/{entity_id}/explode", response_model=list[BomExplodeItem])
async def explode_bom(
    entity_id: uuid.UUID,
    quantity: float = Query(1.0, ge=0),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("bom", "view"),
):
    svc = BomService(db)
    header = await svc.get_bom_header(entity_id)
    return await svc.explode_bom(header.item_id, quantity)


# --- Bom Lines ---
@router.get("/bom-components", response_model=PaginatedResponse[BomComponentOut])
async def list_bom_components(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    bom_header_id: uuid.UUID | None = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("bom", "view"),
):
    svc = BomService(db)
    items, total = await svc.list_bom_components(page, page_size, bom_header_id)
    total_pages = max(1, (total + page_size - 1) // page_size)
    return PaginatedResponse(items=items, total=total, page=page, page_size=page_size, total_pages=total_pages)


@router.get("/bom-components/{entity_id}", response_model=BomComponentOut)
async def get_bom_component(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("bom", "view"),
):
    svc = BomService(db)
    return await svc.get_bom_component(entity_id)


@router.post("/bom-components", response_model=BomComponentOut, status_code=201)
async def create_bom_component(
    data: BomComponentCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("bom", "create"),
):
    svc = BomService(db)
    return await svc.create_bom_component(data)


@router.put("/bom-components/{entity_id}", response_model=BomComponentOut)
async def update_bom_component(
    entity_id: uuid.UUID,
    data: BomComponentUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("bom", "edit"),
):
    svc = BomService(db)
    return await svc.update_bom_component(entity_id, data)


@router.delete("/bom-components/{entity_id}", status_code=204)
async def delete_bom_component(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("bom", "edit"),
):
    svc = BomService(db)
    await svc.delete_bom_component(entity_id)
