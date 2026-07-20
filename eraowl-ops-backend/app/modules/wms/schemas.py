import uuid
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


# --- Cycle Counts ---
class CycleCountCreate(BaseModel):
    warehouse_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    expected_qty: float
    actual_qty: Optional[float] = None
    variance_qty: Optional[float] = None
    status: str = "PENDING"
    counted_by: Optional[uuid.UUID] = None
    counted_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class CycleCountUpdate(BaseModel):
    warehouse_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    expected_qty: Optional[float] = None
    actual_qty: Optional[float] = None
    variance_qty: Optional[float] = None
    status: Optional[str] = None
    counted_by: Optional[uuid.UUID] = None
    counted_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class CycleCountOut(BaseModel):
    count_id: uuid.UUID
    warehouse_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    expected_qty: float
    actual_qty: Optional[float] = None
    variance_qty: Optional[float] = None
    status: str
    counted_by: Optional[uuid.UUID] = None
    counted_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

    model_config = {"from_attributes": True}


# --- Packing Tasks ---
class PackingTaskCreate(BaseModel):
    so_id: Optional[uuid.UUID] = None
    picking_id: Optional[uuid.UUID] = None
    package_code: str
    weight_kg: Optional[float] = None
    volume_cbm: Optional[float] = None
    status: str = "PENDING"
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class PackingTaskUpdate(BaseModel):
    so_id: Optional[uuid.UUID] = None
    picking_id: Optional[uuid.UUID] = None
    package_code: Optional[str] = None
    weight_kg: Optional[float] = None
    volume_cbm: Optional[float] = None
    status: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class PackingTaskOut(BaseModel):
    packing_id: uuid.UUID
    so_id: Optional[uuid.UUID] = None
    picking_id: Optional[uuid.UUID] = None
    package_code: str
    weight_kg: Optional[float] = None
    volume_cbm: Optional[float] = None
    status: str
    created_at: datetime
    updated_at: datetime
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

    model_config = {"from_attributes": True}


# --- Picking Tasks ---
class PickingTaskCreate(BaseModel):
    so_line_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    from_location: Optional[uuid.UUID] = None
    qty_required: float
    qty_picked: float = 0
    status: str = "PENDING"
    assigned_to: Optional[uuid.UUID] = None
    completed_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class PickingTaskUpdate(BaseModel):
    so_line_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    from_location: Optional[uuid.UUID] = None
    qty_required: Optional[float] = None
    qty_picked: Optional[float] = None
    status: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    completed_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class PickingTaskOut(BaseModel):
    picking_id: uuid.UUID
    so_line_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    from_location: Optional[uuid.UUID] = None
    qty_required: float
    qty_picked: float
    status: str
    assigned_to: Optional[uuid.UUID] = None
    completed_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

    model_config = {"from_attributes": True}


# --- Putaway Tasks ---
class PutawayTaskCreate(BaseModel):
    receiving_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    from_location: Optional[uuid.UUID] = None
    to_location: Optional[uuid.UUID] = None
    qty: float
    status: str = "PENDING"
    assigned_to: Optional[uuid.UUID] = None
    completed_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class PutawayTaskUpdate(BaseModel):
    receiving_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    from_location: Optional[uuid.UUID] = None
    to_location: Optional[uuid.UUID] = None
    qty: Optional[float] = None
    status: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    completed_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class PutawayTaskOut(BaseModel):
    putaway_id: uuid.UUID
    receiving_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    from_location: Optional[uuid.UUID] = None
    to_location: Optional[uuid.UUID] = None
    qty: float
    status: str
    assigned_to: Optional[uuid.UUID] = None
    completed_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

    model_config = {"from_attributes": True}


# --- Receiving Schedules ---
class ReceivingScheduleCreate(BaseModel):
    warehouse_id: uuid.UUID
    po_id: Optional[uuid.UUID] = None
    asn_id: Optional[uuid.UUID] = None
    scheduled_date: date
    status: str = "SCHEDULED"
    dock_door: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class ReceivingScheduleUpdate(BaseModel):
    warehouse_id: Optional[uuid.UUID] = None
    po_id: Optional[uuid.UUID] = None
    asn_id: Optional[uuid.UUID] = None
    scheduled_date: Optional[date] = None
    status: Optional[str] = None
    dock_door: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class ReceivingScheduleOut(BaseModel):
    receiving_id: uuid.UUID
    warehouse_id: uuid.UUID
    po_id: Optional[uuid.UUID] = None
    asn_id: Optional[uuid.UUID] = None
    scheduled_date: date
    status: str
    dock_door: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

    model_config = {"from_attributes": True}


# --- Shipment Headers ---
class ShipmentHeaderCreate(BaseModel):
    so_id: Optional[uuid.UUID] = None
    packing_id: Optional[uuid.UUID] = None
    trip_id: Optional[uuid.UUID] = None
    shipment_code: str
    status: str = "PENDING"
    shipped_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class ShipmentHeaderUpdate(BaseModel):
    so_id: Optional[uuid.UUID] = None
    packing_id: Optional[uuid.UUID] = None
    trip_id: Optional[uuid.UUID] = None
    shipment_code: Optional[str] = None
    status: Optional[str] = None
    shipped_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class ShipmentHeaderOut(BaseModel):
    shipment_id: uuid.UUID
    so_id: Optional[uuid.UUID] = None
    packing_id: Optional[uuid.UUID] = None
    trip_id: Optional[uuid.UUID] = None
    shipment_code: str
    status: str
    shipped_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

    model_config = {"from_attributes": True}


# --- Warehouse Zones ---
class WarehouseZoneCreate(BaseModel):
    warehouse_id: uuid.UUID
    zone_code: str
    zone_name: str
    zone_type: str
    is_active: bool = True


class WarehouseZoneUpdate(BaseModel):
    warehouse_id: Optional[uuid.UUID] = None
    zone_code: Optional[str] = None
    zone_name: Optional[str] = None
    zone_type: Optional[str] = None
    is_active: Optional[bool] = None


class WarehouseZoneOut(BaseModel):
    zone_id: uuid.UUID
    warehouse_id: uuid.UUID
    zone_code: str
    zone_name: str
    zone_type: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    update_by: Optional[uuid.UUID] = None

    model_config = {"from_attributes": True}
