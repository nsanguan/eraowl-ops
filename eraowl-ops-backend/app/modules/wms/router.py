import uuid
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.shared.pagination import PaginatedResponse
from app.modules.wms.services import (
    CycleCountService,
    PackingTaskService,
    PickingTaskService,
    PutawayTaskService,
    ReceivingScheduleService,
    ShipmentHeaderService,
    WarehouseZoneService,
)
from app.modules.wms.schemas import (
    CycleCountCreate,
    CycleCountUpdate,
    CycleCountOut,
    PackingTaskCreate,
    PackingTaskUpdate,
    PackingTaskOut,
    PickingTaskCreate,
    PickingTaskUpdate,
    PickingTaskOut,
    PutawayTaskCreate,
    PutawayTaskUpdate,
    PutawayTaskOut,
    ReceivingScheduleCreate,
    ReceivingScheduleUpdate,
    ReceivingScheduleOut,
    ShipmentHeaderCreate,
    ShipmentHeaderUpdate,
    ShipmentHeaderOut,
    WarehouseZoneCreate,
    WarehouseZoneUpdate,
    WarehouseZoneOut,
)

router = APIRouter(dependencies=[Depends(get_current_user)])


def _page(result):
    return PaginatedResponse(**result.model_dump())


# --- Cycle Counts ---
@router.get("/cycle_counts", response_model=PaginatedResponse[CycleCountOut])
async def list_cycle_counts(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view"),
):
    svc = CycleCountService(db)
    filters = {"status": status_filter} if status_filter else None
    return _page(await svc.list(page, page_size, filters=filters))


@router.get("/cycle_counts/{entity_id}", response_model=CycleCountOut)
async def get_cycle_count(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view")):
    return await CycleCountService(db).get(entity_id)


@router.post("/cycle_counts", response_model=CycleCountOut, status_code=status.HTTP_201_CREATED)
async def create_cycle_count(data: CycleCountCreate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await CycleCountService(db).create(data)


@router.put("/cycle_counts/{entity_id}", response_model=CycleCountOut)
async def update_cycle_count(entity_id: uuid.UUID, data: CycleCountUpdate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await CycleCountService(db).update(entity_id, data)


@router.delete("/cycle_counts/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cycle_count(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    await CycleCountService(db).delete(entity_id)


# --- Packing Tasks ---
@router.get("/packing_tasks", response_model=PaginatedResponse[PackingTaskOut])
async def list_packing_tasks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view"),
):
    svc = PackingTaskService(db)
    filters = {"status": status_filter} if status_filter else None
    return _page(await svc.list(page, page_size, filters=filters))


@router.get("/packing_tasks/{entity_id}", response_model=PackingTaskOut)
async def get_packing_task(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view")):
    return await PackingTaskService(db).get(entity_id)


@router.post("/packing_tasks", response_model=PackingTaskOut, status_code=status.HTTP_201_CREATED)
async def create_packing_task(data: PackingTaskCreate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await PackingTaskService(db).create(data)


@router.put("/packing_tasks/{entity_id}", response_model=PackingTaskOut)
async def update_packing_task(entity_id: uuid.UUID, data: PackingTaskUpdate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await PackingTaskService(db).update(entity_id, data)


@router.delete("/packing_tasks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_packing_task(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    await PackingTaskService(db).delete(entity_id)


# --- Picking Tasks ---
@router.get("/picking_tasks", response_model=PaginatedResponse[PickingTaskOut])
async def list_picking_tasks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view"),
):
    svc = PickingTaskService(db)
    filters = {"status": status_filter} if status_filter else None
    return _page(await svc.list(page, page_size, filters=filters))


@router.get("/picking_tasks/{entity_id}", response_model=PickingTaskOut)
async def get_picking_task(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view")):
    return await PickingTaskService(db).get(entity_id)


@router.post("/picking_tasks", response_model=PickingTaskOut, status_code=status.HTTP_201_CREATED)
async def create_picking_task(data: PickingTaskCreate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await PickingTaskService(db).create(data)


@router.put("/picking_tasks/{entity_id}", response_model=PickingTaskOut)
async def update_picking_task(entity_id: uuid.UUID, data: PickingTaskUpdate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await PickingTaskService(db).update(entity_id, data)


@router.delete("/picking_tasks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_picking_task(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    await PickingTaskService(db).delete(entity_id)


# --- Putaway Tasks ---
@router.get("/putaway_tasks", response_model=PaginatedResponse[PutawayTaskOut])
async def list_putaway_tasks(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view"),
):
    svc = PutawayTaskService(db)
    filters = {"status": status_filter} if status_filter else None
    return _page(await svc.list(page, page_size, filters=filters))


@router.get("/putaway_tasks/{entity_id}", response_model=PutawayTaskOut)
async def get_putaway_task(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view")):
    return await PutawayTaskService(db).get(entity_id)


@router.post("/putaway_tasks", response_model=PutawayTaskOut, status_code=status.HTTP_201_CREATED)
async def create_putaway_task(data: PutawayTaskCreate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await PutawayTaskService(db).create(data)


@router.put("/putaway_tasks/{entity_id}", response_model=PutawayTaskOut)
async def update_putaway_task(entity_id: uuid.UUID, data: PutawayTaskUpdate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await PutawayTaskService(db).update(entity_id, data)


@router.delete("/putaway_tasks/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_putaway_task(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    await PutawayTaskService(db).delete(entity_id)


# --- Receiving Schedules ---
@router.get("/receiving_schedules", response_model=PaginatedResponse[ReceivingScheduleOut])
async def list_receiving_schedules(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view"),
):
    svc = ReceivingScheduleService(db)
    filters = {"status": status_filter} if status_filter else None
    return _page(await svc.list(page, page_size, filters=filters))


@router.get("/receiving_schedules/{entity_id}", response_model=ReceivingScheduleOut)
async def get_receiving_schedule(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view")):
    return await ReceivingScheduleService(db).get(entity_id)


@router.post("/receiving_schedules", response_model=ReceivingScheduleOut, status_code=status.HTTP_201_CREATED)
async def create_receiving_schedule(data: ReceivingScheduleCreate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await ReceivingScheduleService(db).create(data)


@router.put("/receiving_schedules/{entity_id}", response_model=ReceivingScheduleOut)
async def update_receiving_schedule(entity_id: uuid.UUID, data: ReceivingScheduleUpdate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await ReceivingScheduleService(db).update(entity_id, data)


@router.delete("/receiving_schedules/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_receiving_schedule(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    await ReceivingScheduleService(db).delete(entity_id)


# --- Shipment Headers ---
@router.get("/shipment_headers", response_model=PaginatedResponse[ShipmentHeaderOut])
async def list_shipment_headers(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    status_filter: Optional[str] = Query(None, alias="status"),
    db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view"),
):
    svc = ShipmentHeaderService(db)
    filters = {"status": status_filter} if status_filter else None
    return _page(await svc.list(page, page_size, filters=filters))


@router.get("/shipment_headers/{entity_id}", response_model=ShipmentHeaderOut)
async def get_shipment_header(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view")):
    return await ShipmentHeaderService(db).get(entity_id)


@router.post("/shipment_headers", response_model=ShipmentHeaderOut, status_code=status.HTTP_201_CREATED)
async def create_shipment_header(data: ShipmentHeaderCreate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await ShipmentHeaderService(db).create(data)


@router.put("/shipment_headers/{entity_id}", response_model=ShipmentHeaderOut)
async def update_shipment_header(entity_id: uuid.UUID, data: ShipmentHeaderUpdate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await ShipmentHeaderService(db).update(entity_id, data)


@router.delete("/shipment_headers/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shipment_header(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    await ShipmentHeaderService(db).delete(entity_id)


# --- Warehouse Zones ---
@router.get("/warehouse_zones", response_model=PaginatedResponse[WarehouseZoneOut])
async def list_warehouse_zones(
    page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100),
    search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view"),
):
    svc = WarehouseZoneService(db)
    return _page(await svc.list(page, page_size, search_cols=["zone_code", "zone_name"], search_term=search))


@router.get("/warehouse_zones/{entity_id}", response_model=WarehouseZoneOut)
async def get_warehouse_zone(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "view")):
    return await WarehouseZoneService(db).get(entity_id)


@router.post("/warehouse_zones", response_model=WarehouseZoneOut, status_code=status.HTTP_201_CREATED)
async def create_warehouse_zone(data: WarehouseZoneCreate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await WarehouseZoneService(db).create(data)


@router.put("/warehouse_zones/{entity_id}", response_model=WarehouseZoneOut)
async def update_warehouse_zone(entity_id: uuid.UUID, data: WarehouseZoneUpdate, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    return await WarehouseZoneService(db).update(entity_id, data)


@router.delete("/warehouse_zones/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_warehouse_zone(entity_id: uuid.UUID, db: AsyncSession = Depends(get_db), _priv=check_privilege("wms", "manage")):
    await WarehouseZoneService(db).delete(entity_id)
