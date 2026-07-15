from datetime import date, datetime
from typing import Optional
import uuid

from pydantic import BaseModel


# ---------------------------------------------------------------------------
# PoHeader
# ---------------------------------------------------------------------------

class CreatePoHeaderRequest(BaseModel):
    po_number: str
    status: str = "DRAFT"
    order_date: date
    supplier_id: Optional[uuid.UUID] = None
    supplier_site_id: Optional[uuid.UUID] = None
    currency_code: str = "THB"
    exchange_rate: float = 1.0
    payment_term_days: int = 30
    description: Optional[str] = None
    total_amount: float = 0.0
    business_unit_id: Optional[uuid.UUID] = None
    buyer_name: Optional[str] = None


class UpdatePoHeaderRequest(BaseModel):
    po_number: Optional[str] = None
    status: Optional[str] = None
    order_date: Optional[date] = None
    supplier_id: Optional[uuid.UUID] = None
    supplier_site_id: Optional[uuid.UUID] = None
    currency_code: Optional[str] = None
    exchange_rate: Optional[float] = None
    payment_term_days: Optional[int] = None
    description: Optional[str] = None
    total_amount: Optional[float] = None
    business_unit_id: Optional[uuid.UUID] = None
    buyer_name: Optional[str] = None


class PoHeaderResponse(BaseModel):
    po_id: uuid.UUID
    po_number: str
    status: str
    order_date: date
    supplier_id: Optional[uuid.UUID] = None
    supplier_site_id: Optional[uuid.UUID] = None
    currency_code: str
    exchange_rate: float
    payment_term_days: int
    description: Optional[str] = None
    total_amount: float
    business_unit_id: Optional[uuid.UUID] = None
    buyer_name: Optional[str] = None
    is_active: bool
    is_deleted: bool
    object_version_number: int
    created_at: datetime
    updated_at: datetime
    update_by: Optional[str] = None

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# PoLine
# ---------------------------------------------------------------------------

class CreatePoLineRequest(BaseModel):
    po_id: uuid.UUID
    line_num: int
    item_id: Optional[uuid.UUID] = None
    item_description: Optional[str] = None
    uom_id: Optional[uuid.UUID] = None
    qty_ordered: float = 0
    qty_received: float = 0
    qty_invoiced: float = 0
    unit_price: float = 0
    line_amount: float = 0
    tax_amount: float = 0
    charge_amount: float = 0
    need_by_date: Optional[date] = None
    promise_date: Optional[date] = None
    line_type: str = "GOODS"


class UpdatePoLineRequest(BaseModel):
    line_num: Optional[int] = None
    item_id: Optional[uuid.UUID] = None
    item_description: Optional[str] = None
    uom_id: Optional[uuid.UUID] = None
    qty_ordered: Optional[float] = None
    qty_received: Optional[float] = None
    qty_invoiced: Optional[float] = None
    unit_price: Optional[float] = None
    line_amount: Optional[float] = None
    tax_amount: Optional[float] = None
    charge_amount: Optional[float] = None
    need_by_date: Optional[date] = None
    promise_date: Optional[date] = None
    line_type: Optional[str] = None


class PoLineResponse(BaseModel):
    po_line_id: uuid.UUID
    po_id: uuid.UUID
    line_num: int
    item_id: Optional[uuid.UUID] = None
    item_description: Optional[str] = None
    uom_id: Optional[uuid.UUID] = None
    qty_ordered: float
    qty_received: float
    qty_invoiced: float
    unit_price: float
    line_amount: float
    tax_amount: float
    charge_amount: float
    need_by_date: Optional[date] = None
    promise_date: Optional[date] = None
    line_type: str
    is_active: bool
    is_deleted: bool
    object_version_number: int
    created_at: datetime
    updated_at: datetime
    update_by: Optional[str] = None

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# PoShipment
# ---------------------------------------------------------------------------

class CreatePoShipmentRequest(BaseModel):
    po_id: uuid.UUID
    po_line_id: uuid.UUID
    shipment_num: int
    qty_ordered: float = 0
    qty_received: float = 0
    qty_accepted: float = 0
    qty_rejected: float = 0
    expected_receipt_date: Optional[date] = None
    actual_receipt_date: Optional[date] = None
    warehouse_id: Optional[uuid.UUID] = None
    locator_id: Optional[uuid.UUID] = None


class UpdatePoShipmentRequest(BaseModel):
    shipment_num: Optional[int] = None
    qty_ordered: Optional[float] = None
    qty_received: Optional[float] = None
    qty_accepted: Optional[float] = None
    qty_rejected: Optional[float] = None
    expected_receipt_date: Optional[date] = None
    actual_receipt_date: Optional[date] = None
    warehouse_id: Optional[uuid.UUID] = None
    locator_id: Optional[uuid.UUID] = None


class PoShipmentResponse(BaseModel):
    po_shipment_id: uuid.UUID
    po_id: uuid.UUID
    po_line_id: uuid.UUID
    shipment_num: int
    qty_ordered: float
    qty_received: float
    qty_accepted: float
    qty_rejected: float
    expected_receipt_date: Optional[date] = None
    actual_receipt_date: Optional[date] = None
    warehouse_id: Optional[uuid.UUID] = None
    locator_id: Optional[uuid.UUID] = None
    is_active: bool
    is_deleted: bool
    object_version_number: int
    created_at: datetime
    updated_at: datetime
    update_by: Optional[str] = None

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# PoDistribution
# ---------------------------------------------------------------------------

class CreatePoDistributionRequest(BaseModel):
    po_id: uuid.UUID
    po_line_id: uuid.UUID
    po_shipment_id: Optional[uuid.UUID] = None
    distribution_num: int
    account_code: Optional[str] = None
    amount: float = 0.0
    percent: float = 100.0


class UpdatePoDistributionRequest(BaseModel):
    distribution_num: Optional[int] = None
    account_code: Optional[str] = None
    amount: Optional[float] = None
    percent: Optional[float] = None


class PoDistributionResponse(BaseModel):
    distribution_id: uuid.UUID
    po_id: uuid.UUID
    po_line_id: uuid.UUID
    po_shipment_id: Optional[uuid.UUID] = None
    distribution_num: int
    account_code: Optional[str] = None
    amount: float
    percent: float
    is_active: bool
    is_deleted: bool
    object_version_number: int
    created_at: datetime
    updated_at: datetime
    update_by: Optional[str] = None

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# PoRelease
# ---------------------------------------------------------------------------

class CreatePoReleaseRequest(BaseModel):
    po_id: uuid.UUID
    release_num: int
    release_amount: float = 0.0
    release_date: Optional[date] = None
    expected_delivery_date: Optional[date] = None
    status: str = "OPEN"


class UpdatePoReleaseRequest(BaseModel):
    release_num: Optional[int] = None
    release_amount: Optional[float] = None
    release_date: Optional[date] = None
    expected_delivery_date: Optional[date] = None
    status: Optional[str] = None


class PoReleaseResponse(BaseModel):
    release_id: uuid.UUID
    po_id: uuid.UUID
    release_num: int
    release_amount: float
    release_date: Optional[date] = None
    expected_delivery_date: Optional[date] = None
    status: str
    is_active: bool
    is_deleted: bool
    object_version_number: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# PoAmendment
# ---------------------------------------------------------------------------

class CreatePoAmendmentRequest(BaseModel):
    po_id: uuid.UUID
    amendment_num: int
    change_type: str
    change_data: Optional[dict] = None
    reason: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[date] = None


class UpdatePoAmendmentRequest(BaseModel):
    amendment_num: Optional[int] = None
    change_type: Optional[str] = None
    change_data: Optional[dict] = None
    reason: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[date] = None


class PoAmendmentResponse(BaseModel):
    amendment_id: uuid.UUID
    po_id: uuid.UUID
    amendment_num: int
    change_type: str
    change_data: Optional[dict] = None
    reason: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[date] = None
    is_active: bool
    is_deleted: bool
    object_version_number: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# PoApproval
# ---------------------------------------------------------------------------

class CreatePoApprovalRequest(BaseModel):
    po_id: uuid.UUID
    approval_level: int
    approver_id: Optional[uuid.UUID] = None
    approver_name: Optional[str] = None
    status: str = "PENDING"
    comments: Optional[str] = None
    approved_date: Optional[datetime] = None


class UpdatePoApprovalRequest(BaseModel):
    approval_level: Optional[int] = None
    approver_id: Optional[uuid.UUID] = None
    approver_name: Optional[str] = None
    status: Optional[str] = None
    comments: Optional[str] = None
    approved_date: Optional[datetime] = None


class PoApprovalResponse(BaseModel):
    approval_id: uuid.UUID
    po_id: uuid.UUID
    approval_level: int
    approver_id: Optional[uuid.UUID] = None
    approver_name: Optional[str] = None
    status: str
    comments: Optional[str] = None
    approved_date: Optional[datetime] = None
    is_active: bool
    is_deleted: bool
    object_version_number: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Composite request / response types
# ---------------------------------------------------------------------------

class CreatePoDistributionItem(BaseModel):
    distribution_num: int
    account_code: Optional[str] = None
    amount: float = 0.0
    percent: float = 100.0


class CreatePoShipmentItem(BaseModel):
    shipment_num: int
    qty_ordered: float = 0
    qty_received: float = 0
    qty_accepted: float = 0
    qty_rejected: float = 0
    expected_receipt_date: Optional[date] = None
    actual_receipt_date: Optional[date] = None
    warehouse_id: Optional[uuid.UUID] = None
    locator_id: Optional[uuid.UUID] = None
    distributions: list[CreatePoDistributionItem] = []


class CreatePoLineItem(BaseModel):
    line_num: int
    item_id: Optional[uuid.UUID] = None
    item_description: Optional[str] = None
    uom_id: Optional[uuid.UUID] = None
    qty_ordered: float = 0
    qty_received: float = 0
    qty_invoiced: float = 0
    unit_price: float = 0
    line_amount: float = 0
    tax_amount: float = 0
    charge_amount: float = 0
    need_by_date: Optional[date] = None
    promise_date: Optional[date] = None
    line_type: str = "GOODS"
    shipments: list[CreatePoShipmentItem] = []


class CreatePoCompositeRequest(BaseModel):
    header: CreatePoHeaderRequest
    lines: list[CreatePoLineItem] = []
    releases: list[CreatePoReleaseRequest] = []
    amendments: list[CreatePoAmendmentRequest] = []


class UpdatePoDistributionItem(BaseModel):
    distribution_id: Optional[uuid.UUID] = None
    distribution_num: int
    account_code: Optional[str] = None
    amount: float = 0.0
    percent: float = 100.0


class UpdatePoShipmentItem(BaseModel):
    po_shipment_id: Optional[uuid.UUID] = None
    shipment_num: int
    qty_ordered: float = 0
    qty_received: float = 0
    qty_accepted: float = 0
    qty_rejected: float = 0
    expected_receipt_date: Optional[date] = None
    actual_receipt_date: Optional[date] = None
    warehouse_id: Optional[uuid.UUID] = None
    locator_id: Optional[uuid.UUID] = None
    distributions: list[UpdatePoDistributionItem] = []


class UpdatePoLineItem(BaseModel):
    po_line_id: Optional[uuid.UUID] = None
    line_num: int
    item_id: Optional[uuid.UUID] = None
    item_description: Optional[str] = None
    uom_id: Optional[uuid.UUID] = None
    qty_ordered: float = 0
    qty_received: float = 0
    qty_invoiced: float = 0
    unit_price: float = 0
    line_amount: float = 0
    tax_amount: float = 0
    charge_amount: float = 0
    need_by_date: Optional[date] = None
    promise_date: Optional[date] = None
    line_type: str = "GOODS"
    shipments: list[UpdatePoShipmentItem] = []


class UpdatePoCompositeRequest(BaseModel):
    header: UpdatePoHeaderRequest
    lines: list[UpdatePoLineItem] = []
    releases: list[UpdatePoReleaseRequest] = []
    amendments: list[UpdatePoAmendmentRequest] = []
