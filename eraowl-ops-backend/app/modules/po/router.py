import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.modules.po.dto.schemas import (
    CreatePoAmendmentRequest,
    CreatePoApprovalRequest,
    CreatePoCompositeRequest,
    CreatePoDistributionRequest,
    CreatePoHeaderRequest,
    CreatePoLineRequest,
    CreatePoReleaseRequest,
    CreatePoShipmentRequest,
    PoAmendmentResponse,
    PoApprovalResponse,
    PoDistributionResponse,
    PoHeaderResponse,
    PoLineResponse,
    PoReleaseResponse,
    PoShipmentResponse,
    UpdatePoAmendmentRequest,
    UpdatePoApprovalRequest,
    UpdatePoCompositeRequest,
    UpdatePoDistributionRequest,
    UpdatePoHeaderRequest,
    UpdatePoLineRequest,
    UpdatePoReleaseRequest,
    UpdatePoShipmentRequest,
)
from app.modules.po.services.composite import PoCompositeService
from app.modules.po.services.crud import (
    PoAmendmentService,
    PoApprovalService,
    PoDistributionService,
    PoLineService,
    PoReleaseService,
    PoShipmentService,
)
from app.modules.po.services.generic import GenericPoService

router = APIRouter(dependencies=[Depends(get_current_user)])


# ---------------------------------------------------------------------------
# PoHeader thin CRUD
# ---------------------------------------------------------------------------

@router.get("/po_headers", response_model=list[PoHeaderResponse])
async def list_po_headers(
    status_filter: Optional[str] = Query(None, alias="status"),
    supplier_id: Optional[uuid.UUID] = Query(None),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = GenericPoService(db)
    filters = {}
    if status_filter:
        filters["status"] = status_filter
    if supplier_id:
        filters["supplier_id"] = supplier_id
    return await svc.list_all("po_headers", filters)


@router.get("/po_headers/{po_id}", response_model=PoHeaderResponse)
async def get_po_header(
    po_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = GenericPoService(db)
    return await svc.get_one("po_headers", str(po_id))


@router.post("/po_headers", response_model=PoHeaderResponse, status_code=status.HTTP_201_CREATED)
async def create_po_header(
    data: CreatePoHeaderRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "create"),
):
    svc = GenericPoService(db)
    return await svc.create("po_headers", data.model_dump())


@router.put("/po_headers/{po_id}", response_model=PoHeaderResponse)
async def update_po_header(
    po_id: uuid.UUID,
    data: UpdatePoHeaderRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = GenericPoService(db)
    return await svc.update("po_headers", str(po_id), data.model_dump(exclude_unset=True))


@router.delete("/po_headers/{po_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_po_header(
    po_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = GenericPoService(db)
    await svc.delete("po_headers", str(po_id))


# ---------------------------------------------------------------------------
# PoLine thin CRUD
# ---------------------------------------------------------------------------

@router.get("/po_lines", response_model=list[PoLineResponse])
async def list_po_lines(
    po_id: uuid.UUID = Query(..., alias="po_id"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = PoLineService(db)
    return await svc.list_by_po_id(po_id)


@router.get("/po_lines/{line_id}", response_model=PoLineResponse)
async def get_po_line(
    line_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = PoLineService(db)
    return await svc.get(line_id)


@router.post("/po_lines", response_model=PoLineResponse, status_code=status.HTTP_201_CREATED)
async def create_po_line(
    data: CreatePoLineRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "create"),
):
    svc = PoLineService(db)
    return await svc.create(data)


@router.put("/po_lines/{line_id}", response_model=PoLineResponse)
async def update_po_line(
    line_id: uuid.UUID,
    data: UpdatePoLineRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = PoLineService(db)
    return await svc.update(line_id, data)


@router.delete("/po_lines/{line_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_po_line(
    line_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = PoLineService(db)
    await svc.delete(line_id)


# ---------------------------------------------------------------------------
# PoShipment thin CRUD
# ---------------------------------------------------------------------------

@router.get("/po_shipments", response_model=list[PoShipmentResponse])
async def list_po_shipments(
    po_line_id: uuid.UUID = Query(...),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = PoShipmentService(db)
    return await svc.list_by_po_line_id(po_line_id)


@router.get("/po_shipments/{shipment_id}", response_model=PoShipmentResponse)
async def get_po_shipment(
    shipment_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = PoShipmentService(db)
    return await svc.get(shipment_id)


@router.post("/po_shipments", response_model=PoShipmentResponse, status_code=status.HTTP_201_CREATED)
async def create_po_shipment(
    data: CreatePoShipmentRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "create"),
):
    svc = PoShipmentService(db)
    return await svc.create(data)


@router.put("/po_shipments/{shipment_id}", response_model=PoShipmentResponse)
async def update_po_shipment(
    shipment_id: uuid.UUID,
    data: UpdatePoShipmentRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = PoShipmentService(db)
    return await svc.update(shipment_id, data)


@router.delete("/po_shipments/{shipment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_po_shipment(
    shipment_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = PoShipmentService(db)
    await svc.delete(shipment_id)


# ---------------------------------------------------------------------------
# PoDistribution thin CRUD
# ---------------------------------------------------------------------------

@router.get("/po_distributions", response_model=list[PoDistributionResponse])
async def list_po_distributions(
    po_shipment_id: uuid.UUID = Query(...),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = PoDistributionService(db)
    return await svc.list_by_po_shipment_id(po_shipment_id)


@router.get("/po_distributions/{dist_id}", response_model=PoDistributionResponse)
async def get_po_distribution(
    dist_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = PoDistributionService(db)
    return await svc.get(dist_id)


@router.post("/po_distributions", response_model=PoDistributionResponse, status_code=status.HTTP_201_CREATED)
async def create_po_distribution(
    data: CreatePoDistributionRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "create"),
):
    svc = PoDistributionService(db)
    return await svc.create(data)


@router.put("/po_distributions/{dist_id}", response_model=PoDistributionResponse)
async def update_po_distribution(
    dist_id: uuid.UUID,
    data: UpdatePoDistributionRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = PoDistributionService(db)
    return await svc.update(dist_id, data)


@router.delete("/po_distributions/{dist_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_po_distribution(
    dist_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = PoDistributionService(db)
    await svc.delete(dist_id)


# ---------------------------------------------------------------------------
# PoRelease thin CRUD
# ---------------------------------------------------------------------------

@router.get("/po_releases", response_model=list[PoReleaseResponse])
async def list_po_releases(
    po_id: uuid.UUID = Query(..., alias="po_id"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = PoReleaseService(db)
    return await svc.list_by_po_id(po_id)


@router.get("/po_releases/{release_id}", response_model=PoReleaseResponse)
async def get_po_release(
    release_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = PoReleaseService(db)
    return await svc.get(release_id)


@router.post("/po_releases", response_model=PoReleaseResponse, status_code=status.HTTP_201_CREATED)
async def create_po_release(
    data: CreatePoReleaseRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "create"),
):
    svc = PoReleaseService(db)
    return await svc.create(data)


@router.put("/po_releases/{release_id}", response_model=PoReleaseResponse)
async def update_po_release(
    release_id: uuid.UUID,
    data: UpdatePoReleaseRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = PoReleaseService(db)
    return await svc.update(release_id, data)


@router.delete("/po_releases/{release_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_po_release(
    release_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = PoReleaseService(db)
    await svc.delete(release_id)


# ---------------------------------------------------------------------------
# PoAmendment thin CRUD
# ---------------------------------------------------------------------------

@router.get("/po_amendments", response_model=list[PoAmendmentResponse])
async def list_po_amendments(
    po_id: uuid.UUID = Query(..., alias="po_id"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = PoAmendmentService(db)
    return await svc.list_by_po_id(po_id)


@router.get("/po_amendments/{amendment_id}", response_model=PoAmendmentResponse)
async def get_po_amendment(
    amendment_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = PoAmendmentService(db)
    return await svc.get(amendment_id)


@router.post("/po_amendments", response_model=PoAmendmentResponse, status_code=status.HTTP_201_CREATED)
async def create_po_amendment(
    data: CreatePoAmendmentRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "create"),
):
    svc = PoAmendmentService(db)
    return await svc.create(data)


@router.put("/po_amendments/{amendment_id}", response_model=PoAmendmentResponse)
async def update_po_amendment(
    amendment_id: uuid.UUID,
    data: UpdatePoAmendmentRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = PoAmendmentService(db)
    return await svc.update(amendment_id, data)


@router.delete("/po_amendments/{amendment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_po_amendment(
    amendment_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = PoAmendmentService(db)
    await svc.delete(amendment_id)


# ---------------------------------------------------------------------------
# PoApproval thin CRUD
# ---------------------------------------------------------------------------

@router.get("/po_approvals", response_model=list[PoApprovalResponse])
async def list_po_approvals(
    po_id: uuid.UUID = Query(..., alias="po_id"),
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = PoApprovalService(db)
    return await svc.list_by_po_id(po_id)


@router.get("/po_approvals/{approval_id}", response_model=PoApprovalResponse)
async def get_po_approval(
    approval_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = PoApprovalService(db)
    return await svc.get(approval_id)


@router.post("/po_approvals", response_model=PoApprovalResponse, status_code=status.HTTP_201_CREATED)
async def create_po_approval(
    data: CreatePoApprovalRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "create"),
):
    svc = PoApprovalService(db)
    return await svc.create(data)


@router.put("/po_approvals/{approval_id}", response_model=PoApprovalResponse)
async def update_po_approval(
    approval_id: uuid.UUID,
    data: UpdatePoApprovalRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = PoApprovalService(db)
    return await svc.update(approval_id, data)


@router.delete("/po_approvals/{approval_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_po_approval(
    approval_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = PoApprovalService(db)
    await svc.delete(approval_id)


# ---------------------------------------------------------------------------
# Composite endpoints
# ---------------------------------------------------------------------------

@router.get("/po_headers/{po_id}/composite")
async def get_po_composite(
    po_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "view"),
):
    svc = PoCompositeService(db)
    return await svc.get_composite(po_id)


@router.post("/po_headers/composite", status_code=status.HTTP_201_CREATED)
async def create_po_composite(
    data: CreatePoCompositeRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "create"),
):
    svc = PoCompositeService(db)
    return await svc.create_composite(data)


@router.put("/po_headers/{po_id}/composite")
async def update_po_composite(
    po_id: uuid.UUID,
    data: UpdatePoCompositeRequest,
    db: AsyncSession = Depends(get_db),
    _priv=check_privilege("po", "edit"),
):
    svc = PoCompositeService(db)
    return await svc.update_composite(po_id, data)


# ---------------------------------------------------------------------------
# Generic CRUD
# ---------------------------------------------------------------------------

@router.get("/generic/{table_name}")
async def generic_list(
    table_name: str,
    db: AsyncSession = Depends(get_db),
    _user=Depends(get_current_user),
    _priv=check_privilege("po", "view"),
):
    svc = GenericPoService(db)
    return await svc.list_all(table_name)


@router.post("/generic/{table_name}", status_code=status.HTTP_201_CREATED)
async def generic_create(
    table_name: str,
    body: dict,
    db: AsyncSession = Depends(get_db),
    _user=Depends(get_current_user),
    _priv=check_privilege("po", "create"),
):
    svc = GenericPoService(db)
    return await svc.create(table_name, body)


@router.get("/generic/{table_name}/{entity_id}")
async def generic_get(
    table_name: str,
    entity_id: str,
    db: AsyncSession = Depends(get_db),
    _user=Depends(get_current_user),
    _priv=check_privilege("po", "view"),
):
    svc = GenericPoService(db)
    return await svc.get_one(table_name, entity_id)


@router.put("/generic/{table_name}/{entity_id}")
async def generic_update(
    table_name: str,
    entity_id: str,
    body: dict,
    db: AsyncSession = Depends(get_db),
    _user=Depends(get_current_user),
    _priv=check_privilege("po", "edit"),
):
    svc = GenericPoService(db)
    return await svc.update(table_name, entity_id, body)


@router.delete("/generic/{table_name}/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def generic_delete(
    table_name: str,
    entity_id: str,
    db: AsyncSession = Depends(get_db),
    _user=Depends(get_current_user),
    _priv=check_privilege("po", "edit"),
):
    svc = GenericPoService(db)
    await svc.delete(table_name, entity_id)
