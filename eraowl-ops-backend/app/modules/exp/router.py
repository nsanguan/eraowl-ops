import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.exp.services import (
    ClaimHeaderService,
    ClaimLineService,
    ExpCategoryService,
)
from app.modules.exp.schemas import (
    ClaimHeaderCreate,
    ClaimHeaderUpdate,
    ClaimHeaderOut,
    ClaimLineCreate,
    ClaimLineUpdate,
    ClaimLineOut,
    ExpCategoryCreate,
    ExpCategoryUpdate,
    ExpCategoryOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


# --- Claim Headers ---
@router.get("/claim_headers", response_model=PaginatedResponse[ClaimHeaderOut])
async def list_claim_headers(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "view"),
):
    svc = ClaimHeaderService(db)
    filters = {"status": status_filter} if status_filter else None
    result = await svc.list(page, page_size, filters=filters)
    return PaginatedResponse(**result.model_dump())


@router.get("/claim_headers/{entity_id}", response_model=ClaimHeaderOut)
async def get_claim_header(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "view"),
):
    svc = ClaimHeaderService(db)
    return await svc.get(entity_id)


@router.post("/claim_headers", response_model=ClaimHeaderOut, status_code=status.HTTP_201_CREATED)
async def create_claim_header(
    data: ClaimHeaderCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "manage"),
):
    svc = ClaimHeaderService(db)
    return await svc.create(data)


@router.put("/claim_headers/{entity_id}", response_model=ClaimHeaderOut)
async def update_claim_header(
    entity_id: uuid.UUID,
    data: ClaimHeaderUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "manage"),
):
    svc = ClaimHeaderService(db)
    return await svc.update(entity_id, data)


@router.delete("/claim_headers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_claim_header(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "manage"),
):
    svc = ClaimHeaderService(db)
    await svc.delete(entity_id)


# --- Claim Lines ---
@router.get("/claim_lines", response_model=PaginatedResponse[ClaimLineOut])
async def list_claim_lines(
    claim_id: uuid.UUID = Query(...),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "view"),
):
    svc = ClaimLineService(db)
    result = await svc.list(page, page_size, filters={"claim_id": claim_id})
    return PaginatedResponse(**result.model_dump())


@router.get("/claim_lines/{entity_id}", response_model=ClaimLineOut)
async def get_claim_line(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "view"),
):
    svc = ClaimLineService(db)
    return await svc.get(entity_id)


@router.post("/claim_lines", response_model=ClaimLineOut, status_code=status.HTTP_201_CREATED)
async def create_claim_line(
    data: ClaimLineCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "manage"),
):
    svc = ClaimLineService(db)
    return await svc.create(data)


@router.put("/claim_lines/{entity_id}", response_model=ClaimLineOut)
async def update_claim_line(
    entity_id: uuid.UUID,
    data: ClaimLineUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "manage"),
):
    svc = ClaimLineService(db)
    return await svc.update(entity_id, data)


@router.delete("/claim_lines/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_claim_line(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "manage"),
):
    svc = ClaimLineService(db)
    await svc.delete(entity_id)


# --- Expense Categories ---
@router.get("/exp_categories", response_model=PaginatedResponse[ExpCategoryOut])
async def list_exp_categories(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "view"),
):
    svc = ExpCategoryService(db)
    result = await svc.list(page, page_size, search_cols=["category_code", "category_name"], search_term=search)
    return PaginatedResponse(**result.model_dump())


@router.get("/exp_categories/{entity_id}", response_model=ExpCategoryOut)
async def get_exp_category(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "view"),
):
    svc = ExpCategoryService(db)
    return await svc.get(entity_id)


@router.post("/exp_categories", response_model=ExpCategoryOut, status_code=status.HTTP_201_CREATED)
async def create_exp_category(
    data: ExpCategoryCreate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "manage"),
):
    svc = ExpCategoryService(db)
    return await svc.create(data)


@router.put("/exp_categories/{entity_id}", response_model=ExpCategoryOut)
async def update_exp_category(
    entity_id: uuid.UUID,
    data: ExpCategoryUpdate,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "manage"),
):
    svc = ExpCategoryService(db)
    return await svc.update(entity_id, data)


@router.delete("/exp_categories/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_exp_category(
    entity_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("exp", "manage"),
):
    svc = ExpCategoryService(db)
    await svc.delete(entity_id)
