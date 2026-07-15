from typing import Optional
import uuid
from datetime import date, datetime
from pydantic import BaseModel


class BomHeaderCreate(BaseModel):
    item_id: uuid.UUID
    alternate_bom_code: Optional[str] = None
    revision: str
    status: str = "PENDING_APPROVAL"
    effective_date_from: date
    effective_date_to: Optional[date] = None


class BomHeaderUpdate(BaseModel):
    item_id: Optional[uuid.UUID] = None
    alternate_bom_code: Optional[str] = None
    revision: str
    status: Optional[str] = None
    effective_date_from: Optional[date] = None
    effective_date_to: Optional[date] = None


class BomHeaderOut(BaseModel):
    bom_header_id: uuid.UUID
    item_id: uuid.UUID
    alternate_bom_code: Optional[str]
    revision: str
    status: str
    effective_date_from: date
    effective_date_to: Optional[date]
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class BomLineCreate(BaseModel):
    bom_header_id: uuid.UUID
    component_item_id: uuid.UUID
    quantity_per: float = 1.0
    uom_id: uuid.UUID
    operation_seq: Optional[int] = None
    effective_date_from: date
    effective_date_to: Optional[date] = None


class BomLineUpdate(BaseModel):
    component_item_id: Optional[uuid.UUID] = None
    quantity_per: Optional[float] = None
    uom_id: Optional[uuid.UUID] = None
    operation_seq: Optional[int] = None
    effective_date_from: Optional[date] = None
    effective_date_to: Optional[date] = None


class BomLineOut(BaseModel):
    bom_line_id: uuid.UUID
    bom_header_id: uuid.UUID
    component_item_id: uuid.UUID
    quantity_per: float
    uom_id: uuid.UUID
    operation_seq: Optional[int]
    effective_date_from: date
    effective_date_to: Optional[date]
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class BomExplodeItem(BaseModel):
    item_id: uuid.UUID
    component_item_id: uuid.UUID
    item_code: str
    item_name: str
    quantity_per: float
    uom_code: str
    level: int
    children: list["BomExplodeItem"] = []
