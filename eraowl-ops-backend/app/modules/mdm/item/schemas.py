from typing import Optional
import uuid
from datetime import datetime
from pydantic import BaseModel


class UomCreate(BaseModel):
    uom_code: str
    uom_name: str
    uom_type: str
    is_active: bool = True


class UomUpdate(BaseModel):
    uom_code: Optional[str] = None
    uom_name: Optional[str] = None
    uom_type: Optional[str] = None
    is_active: Optional[bool] = None


class UomOut(BaseModel):
    uom_id: uuid.UUID
    uom_code: str
    uom_name: str
    uom_type: str
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class UomConversionCreate(BaseModel):
    from_uom_id: uuid.UUID
    to_uom_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    conversion_factor: float = 1.0
    is_active: bool = True


class UomConversionUpdate(BaseModel):
    from_uom_id: Optional[uuid.UUID] = None
    to_uom_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    conversion_factor: Optional[float] = None
    is_active: Optional[bool] = None


class UomConversionOut(BaseModel):
    uom_conversion_id: uuid.UUID
    from_uom_id: uuid.UUID
    to_uom_id: uuid.UUID
    item_id: Optional[uuid.UUID]
    conversion_factor: float
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ItemCategoryCreate(BaseModel):
    category_set: str
    category_code: str
    category_name: str
    parent_category_id: Optional[uuid.UUID] = None
    is_active: bool = True


class ItemCategoryUpdate(BaseModel):
    category_set: Optional[str] = None
    category_code: Optional[str] = None
    category_name: Optional[str] = None
    parent_category_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None


class ItemCategoryOut(BaseModel):
    item_category_id: uuid.UUID
    category_set: str
    category_code: str
    category_name: str
    parent_category_id: Optional[uuid.UUID]
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ItemCreate(BaseModel):
    item_code: str
    item_name: str
    item_type: str
    primary_uom_id: uuid.UUID
    status: str = "ACTIVE"
    description: Optional[str] = None
    is_active: bool = True


class ItemUpdate(BaseModel):
    item_code: Optional[str] = None
    item_name: Optional[str] = None
    item_type: Optional[str] = None
    primary_uom_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class ItemOut(BaseModel):
    item_id: uuid.UUID
    item_code: str
    item_name: str
    item_type: str
    primary_uom_id: uuid.UUID
    status: str
    description: Optional[str]
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ItemCategoryAssignmentCreate(BaseModel):
    item_id: uuid.UUID
    category_id: uuid.UUID
    is_active: bool = True


class ItemCategoryAssignmentUpdate(BaseModel):
    item_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None


class ItemCategoryAssignmentOut(BaseModel):
    item_category_assignment_id: uuid.UUID
    item_id: uuid.UUID
    category_id: uuid.UUID
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ItemOrganizationCreate(BaseModel):
    item_id: uuid.UUID
    warehouse_id: uuid.UUID
    min_qty: float = 0.0
    max_qty: Optional[float] = None
    lead_time_days: int = 0
    costing_method: str = "STANDARD"
    standard_cost: Optional[float] = None
    is_enabled: bool = True
    is_active: bool = True


class ItemOrganizationUpdate(BaseModel):
    warehouse_id: Optional[uuid.UUID] = None
    min_qty: Optional[float] = None
    max_qty: Optional[float] = None
    lead_time_days: Optional[int] = None
    costing_method: Optional[str] = None
    standard_cost: Optional[float] = None
    is_enabled: Optional[bool] = None
    is_active: Optional[bool] = None


class ItemOrganizationOut(BaseModel):
    item_organization_id: uuid.UUID
    item_id: uuid.UUID
    warehouse_id: uuid.UUID
    min_qty: float
    max_qty: Optional[float]
    lead_time_days: int
    costing_method: str
    standard_cost: Optional[float]
    is_enabled: bool
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ItemSupplierXrefCreate(BaseModel):
    item_id: uuid.UUID
    supplier_id: uuid.UUID
    supplier_item_code: str
    is_preferred: bool = False
    is_active: bool = True


class ItemSupplierXrefUpdate(BaseModel):
    supplier_id: Optional[uuid.UUID] = None
    supplier_item_code: Optional[str] = None
    is_preferred: Optional[bool] = None
    is_active: Optional[bool] = None


class ItemSupplierXrefOut(BaseModel):
    item_supplier_xref_id: uuid.UUID
    item_id: uuid.UUID
    supplier_id: uuid.UUID
    supplier_item_code: str
    is_preferred: bool
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
