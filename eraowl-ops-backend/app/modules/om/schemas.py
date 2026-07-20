import uuid
from datetime import date, datetime, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class AiAgentLogsCreate(BaseModel):
    log_id: uuid.UUID
    state_id: Optional[uuid.UUID] = None
    order_id: Optional[uuid.UUID] = None
    agent_name: str
    action: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class AiAgentLogsUpdate(BaseModel):
    log_id: Optional[uuid.UUID] = None
    state_id: Optional[uuid.UUID] = None
    order_id: Optional[uuid.UUID] = None
    agent_name: Optional[str] = None
    action: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class AiAgentLogsOut(BaseModel):
    log_id: uuid.UUID
    state_id: Optional[uuid.UUID] = None
    order_id: Optional[uuid.UUID] = None
    agent_name: str
    action: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class AiDecisionsCreate(BaseModel):
    decision_id: uuid.UUID
    order_id: Optional[uuid.UUID] = None
    log_id: Optional[uuid.UUID] = None
    decision_type: str
    decision_data: Optional[dict] = None
    reasoning: Optional[str] = None
    confidence_score: Optional[float] = None
    accepted: Optional[bool] = None
    accepted_by: Optional[uuid.UUID] = None
    accepted_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class AiDecisionsUpdate(BaseModel):
    decision_id: Optional[uuid.UUID] = None
    order_id: Optional[uuid.UUID] = None
    log_id: Optional[uuid.UUID] = None
    decision_type: Optional[str] = None
    decision_data: Optional[dict] = None
    reasoning: Optional[str] = None
    confidence_score: Optional[float] = None
    accepted: Optional[bool] = None
    accepted_by: Optional[uuid.UUID] = None
    accepted_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class AiDecisionsOut(BaseModel):
    decision_id: uuid.UUID
    order_id: Optional[uuid.UUID] = None
    log_id: Optional[uuid.UUID] = None
    decision_type: str
    decision_data: Optional[dict] = None
    reasoning: Optional[str] = None
    confidence_score: Optional[float] = None
    accepted: Optional[bool] = None
    accepted_by: Optional[uuid.UUID] = None
    accepted_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class AiWorkflowStateCreate(BaseModel):
    state_id: uuid.UUID
    order_id: uuid.UUID
    workflow_def_id: Optional[uuid.UUID] = None
    thread_id: Optional[str] = None
    state_data: dict
    status: Optional[str] = None
    checkpoint: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class AiWorkflowStateUpdate(BaseModel):
    state_id: Optional[uuid.UUID] = None
    order_id: Optional[uuid.UUID] = None
    workflow_def_id: Optional[uuid.UUID] = None
    thread_id: Optional[str] = None
    state_data: Optional[dict] = None
    status: Optional[str] = None
    checkpoint: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class AiWorkflowStateOut(BaseModel):
    state_id: uuid.UUID
    order_id: uuid.UUID
    workflow_def_id: Optional[uuid.UUID] = None
    thread_id: Optional[str] = None
    state_data: dict
    status: Optional[str] = None
    checkpoint: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CustomerAttributesCreate(BaseModel):
    partner_id: uuid.UUID
    credit_limit: Optional[float] = None
    price_list_id: Optional[uuid.UUID] = None
    currency_code: Optional[str] = None
    payment_term_days: Optional[int] = None
    default_warehouse_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class CustomerAttributesUpdate(BaseModel):
    partner_id: Optional[uuid.UUID] = None
    credit_limit: Optional[float] = None
    price_list_id: Optional[uuid.UUID] = None
    currency_code: Optional[str] = None
    payment_term_days: Optional[int] = None
    default_warehouse_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class CustomerAttributesOut(BaseModel):
    partner_id: uuid.UUID
    credit_limit: Optional[float] = None
    price_list_id: Optional[uuid.UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    currency_code: Optional[str] = None
    payment_term_days: Optional[int] = None
    default_warehouse_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    is_active: bool
    object_version_number: int
    model_config = {"from_attributes": True}

class ImportErrorLogCreate(BaseModel):
    error_id: uuid.UUID
    import_id: Optional[uuid.UUID] = None
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    error_data: Optional[dict] = None
    retryable: Optional[bool] = None
    resolved_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class ImportErrorLogUpdate(BaseModel):
    error_id: Optional[uuid.UUID] = None
    import_id: Optional[uuid.UUID] = None
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    error_data: Optional[dict] = None
    retryable: Optional[bool] = None
    resolved_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class ImportErrorLogOut(BaseModel):
    error_id: uuid.UUID
    import_id: Optional[uuid.UUID] = None
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    error_data: Optional[dict] = None
    retryable: Optional[bool] = None
    resolved_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class LineTypesCreate(BaseModel):
    line_type_id: uuid.UUID
    line_type_code: str
    line_type_name: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class LineTypesUpdate(BaseModel):
    line_type_id: Optional[uuid.UUID] = None
    line_type_code: Optional[str] = None
    line_type_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class LineTypesOut(BaseModel):
    line_type_id: uuid.UUID
    line_type_code: str
    line_type_name: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class OmHeadersCreate(BaseModel):
    so_id: uuid.UUID
    bu_id: Optional[uuid.UUID] = None
    customer_id: Optional[uuid.UUID] = None
    so_number: str
    order_date: date
    status: str
    order_type_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    currency_code: Optional[str] = None
    exchange_rate: Optional[float] = None
    payment_term_id: Optional[uuid.UUID] = None
    salesperson_id: Optional[uuid.UUID] = None
    requested_ship_date: Optional[date] = None
    promised_delivery_date: Optional[date] = None
    ship_to_address_id: Optional[uuid.UUID] = None
    bill_to_address_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    source_system: Optional[str] = None
    source_transaction_id: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    ship_from_warehouse_id: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class OmHeadersUpdate(BaseModel):
    so_id: Optional[uuid.UUID] = None
    bu_id: Optional[uuid.UUID] = None
    customer_id: Optional[uuid.UUID] = None
    so_number: Optional[str] = None
    order_date: Optional[date] = None
    status: Optional[str] = None
    order_type_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    currency_code: Optional[str] = None
    exchange_rate: Optional[float] = None
    payment_term_id: Optional[uuid.UUID] = None
    salesperson_id: Optional[uuid.UUID] = None
    requested_ship_date: Optional[date] = None
    promised_delivery_date: Optional[date] = None
    ship_to_address_id: Optional[uuid.UUID] = None
    bill_to_address_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    source_system: Optional[str] = None
    source_transaction_id: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    ship_from_warehouse_id: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class OmHeadersOut(BaseModel):
    so_id: uuid.UUID
    bu_id: Optional[uuid.UUID] = None
    customer_id: Optional[uuid.UUID] = None
    so_number: str
    order_date: date
    status: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    order_type_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    currency_code: Optional[str] = None
    exchange_rate: Optional[float] = None
    payment_term_id: Optional[uuid.UUID] = None
    salesperson_id: Optional[uuid.UUID] = None
    requested_ship_date: Optional[date] = None
    promised_delivery_date: Optional[date] = None
    ship_to_address_id: Optional[uuid.UUID] = None
    bill_to_address_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    source_system: Optional[str] = None
    source_transaction_id: Optional[str] = None
    is_active: bool
    object_version_number: int
    ship_from_warehouse_id: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class OmLinesCreate(BaseModel):
    so_line_id: uuid.UUID
    so_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    qty_ordered: float
    unit_price: float
    line_num: Optional[int] = None
    line_type_id: Optional[uuid.UUID] = None
    line_description: Optional[str] = None
    uom_code: Optional[str] = None
    need_by_date: Optional[date] = None
    promised_date: Optional[date] = None
    tax_rate_id: Optional[uuid.UUID] = None
    taxable_flag: Optional[bool] = None
    discount_pct: Optional[float] = None
    discount_amount: Optional[float] = None
    source_line_id: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class OmLinesUpdate(BaseModel):
    so_line_id: Optional[uuid.UUID] = None
    so_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    qty_ordered: Optional[float] = None
    unit_price: Optional[float] = None
    line_num: Optional[int] = None
    line_type_id: Optional[uuid.UUID] = None
    line_description: Optional[str] = None
    uom_code: Optional[str] = None
    need_by_date: Optional[date] = None
    promised_date: Optional[date] = None
    tax_rate_id: Optional[uuid.UUID] = None
    taxable_flag: Optional[bool] = None
    discount_pct: Optional[float] = None
    discount_amount: Optional[float] = None
    source_line_id: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class OmLinesOut(BaseModel):
    so_line_id: uuid.UUID
    so_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    qty_ordered: float
    unit_price: float
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    line_num: Optional[int] = None
    line_type_id: Optional[uuid.UUID] = None
    line_description: Optional[str] = None
    uom_code: Optional[str] = None
    need_by_date: Optional[date] = None
    promised_date: Optional[date] = None
    tax_rate_id: Optional[uuid.UUID] = None
    taxable_flag: Optional[bool] = None
    discount_pct: Optional[float] = None
    discount_amount: Optional[float] = None
    source_line_id: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class OmShipmentsCreate(BaseModel):
    om_shipment_id: uuid.UUID
    so_line_id: uuid.UUID
    so_id: uuid.UUID
    shipment_num: int
    ship_from_warehouse_id: Optional[uuid.UUID] = None
    ship_to_warehouse_id: Optional[uuid.UUID] = None
    ship_to_address_id: Optional[uuid.UUID] = None
    carrier_code: Optional[str] = None
    tracking_number: Optional[str] = None
    qty_ordered: float
    qty_shipped: Optional[float] = None
    qty_delivered: Optional[float] = None
    qty_invoiced: Optional[float] = None
    unit_price: Optional[float] = None
    requested_ship_date: Optional[date] = None
    actual_ship_date: Optional[datetime] = None
    requested_delivery_date: Optional[date] = None
    actual_delivery_date: Optional[datetime] = None
    notes: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class OmShipmentsUpdate(BaseModel):
    om_shipment_id: Optional[uuid.UUID] = None
    so_line_id: Optional[uuid.UUID] = None
    so_id: Optional[uuid.UUID] = None
    shipment_num: Optional[int] = None
    ship_from_warehouse_id: Optional[uuid.UUID] = None
    ship_to_warehouse_id: Optional[uuid.UUID] = None
    ship_to_address_id: Optional[uuid.UUID] = None
    carrier_code: Optional[str] = None
    tracking_number: Optional[str] = None
    qty_ordered: Optional[float] = None
    qty_shipped: Optional[float] = None
    qty_delivered: Optional[float] = None
    qty_invoiced: Optional[float] = None
    unit_price: Optional[float] = None
    requested_ship_date: Optional[date] = None
    actual_ship_date: Optional[datetime] = None
    requested_delivery_date: Optional[date] = None
    actual_delivery_date: Optional[datetime] = None
    notes: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class OmShipmentsOut(BaseModel):
    om_shipment_id: uuid.UUID
    so_line_id: uuid.UUID
    so_id: uuid.UUID
    shipment_num: int
    ship_from_warehouse_id: Optional[uuid.UUID] = None
    ship_to_warehouse_id: Optional[uuid.UUID] = None
    ship_to_address_id: Optional[uuid.UUID] = None
    carrier_code: Optional[str] = None
    tracking_number: Optional[str] = None
    qty_ordered: float
    qty_shipped: Optional[float] = None
    qty_delivered: Optional[float] = None
    qty_invoiced: Optional[float] = None
    unit_price: Optional[float] = None
    requested_ship_date: Optional[date] = None
    actual_ship_date: Optional[datetime] = None
    requested_delivery_date: Optional[date] = None
    actual_delivery_date: Optional[datetime] = None
    notes: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class OrderImportInterfaceCreate(BaseModel):
    import_id: uuid.UUID
    source_system: str
    source_transaction_id: str
    payload: dict
    status: Optional[str] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    order_id: Optional[uuid.UUID] = None
    processed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class OrderImportInterfaceUpdate(BaseModel):
    import_id: Optional[uuid.UUID] = None
    source_system: Optional[str] = None
    source_transaction_id: Optional[str] = None
    payload: Optional[dict] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    order_id: Optional[uuid.UUID] = None
    processed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class OrderImportInterfaceOut(BaseModel):
    import_id: uuid.UUID
    source_system: str
    source_transaction_id: str
    payload: dict
    status: Optional[str] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    order_id: Optional[uuid.UUID] = None
    processed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class OrderTypesCreate(BaseModel):
    order_type_id: uuid.UUID
    order_type_code: str
    order_type_name: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class OrderTypesUpdate(BaseModel):
    order_type_id: Optional[uuid.UUID] = None
    order_type_code: Optional[str] = None
    order_type_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class OrderTypesOut(BaseModel):
    order_type_id: uuid.UUID
    order_type_code: str
    order_type_name: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ShipmentTrackingCreate(BaseModel):
    tracking_id: uuid.UUID
    order_id: uuid.UUID
    carrier_code: Optional[str] = None
    tracking_number: Optional[str] = None
    ship_date: Optional[date] = None
    estimated_arrival: Optional[date] = None
    actual_arrival: Optional[date] = None
    status: Optional[str] = None
    shipment_data: Optional[dict] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ShipmentTrackingUpdate(BaseModel):
    tracking_id: Optional[uuid.UUID] = None
    order_id: Optional[uuid.UUID] = None
    carrier_code: Optional[str] = None
    tracking_number: Optional[str] = None
    ship_date: Optional[date] = None
    estimated_arrival: Optional[date] = None
    actual_arrival: Optional[date] = None
    status: Optional[str] = None
    shipment_data: Optional[dict] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ShipmentTrackingOut(BaseModel):
    tracking_id: uuid.UUID
    order_id: uuid.UUID
    carrier_code: Optional[str] = None
    tracking_number: Optional[str] = None
    ship_date: Optional[date] = None
    estimated_arrival: Optional[date] = None
    actual_arrival: Optional[date] = None
    status: Optional[str] = None
    shipment_data: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class WmsCallbacksCreate(BaseModel):
    callback_id: uuid.UUID
    queue_id: Optional[uuid.UUID] = None
    order_line_id: Optional[uuid.UUID] = None
    callback_type: str
    callback_data: Optional[dict] = None
    status: Optional[str] = None
    processed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class WmsCallbacksUpdate(BaseModel):
    callback_id: Optional[uuid.UUID] = None
    queue_id: Optional[uuid.UUID] = None
    order_line_id: Optional[uuid.UUID] = None
    callback_type: Optional[str] = None
    callback_data: Optional[dict] = None
    status: Optional[str] = None
    processed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class WmsCallbacksOut(BaseModel):
    callback_id: uuid.UUID
    queue_id: Optional[uuid.UUID] = None
    order_line_id: Optional[uuid.UUID] = None
    callback_type: str
    callback_data: Optional[dict] = None
    status: Optional[str] = None
    processed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class WmsTaskQueueCreate(BaseModel):
    queue_id: uuid.UUID
    order_line_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    qty_required: float
    qty_picked: Optional[float] = None
    qty_shipped: Optional[float] = None
    source_warehouse_id: Optional[uuid.UUID] = None
    dest_warehouse_id: Optional[uuid.UUID] = None
    priority: Optional[int] = None
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class WmsTaskQueueUpdate(BaseModel):
    queue_id: Optional[uuid.UUID] = None
    order_line_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    qty_required: Optional[float] = None
    qty_picked: Optional[float] = None
    qty_shipped: Optional[float] = None
    source_warehouse_id: Optional[uuid.UUID] = None
    dest_warehouse_id: Optional[uuid.UUID] = None
    priority: Optional[int] = None
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class WmsTaskQueueOut(BaseModel):
    queue_id: uuid.UUID
    order_line_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    qty_required: float
    qty_picked: Optional[float] = None
    qty_shipped: Optional[float] = None
    source_warehouse_id: Optional[uuid.UUID] = None
    dest_warehouse_id: Optional[uuid.UUID] = None
    priority: Optional[int] = None
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class WorkflowAssignmentsCreate(BaseModel):
    assignment_id: uuid.UUID
    task_id: uuid.UUID
    assignee_type: str
    assignee_value: str
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class WorkflowAssignmentsUpdate(BaseModel):
    assignment_id: Optional[uuid.UUID] = None
    task_id: Optional[uuid.UUID] = None
    assignee_type: Optional[str] = None
    assignee_value: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class WorkflowAssignmentsOut(BaseModel):
    assignment_id: uuid.UUID
    task_id: uuid.UUID
    assignee_type: str
    assignee_value: str
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class WorkflowDefinitionsCreate(BaseModel):
    workflow_def_id: uuid.UUID
    workflow_code: str
    workflow_name: str
    description: Optional[str] = None
    definition: dict
    version: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class WorkflowDefinitionsUpdate(BaseModel):
    workflow_def_id: Optional[uuid.UUID] = None
    workflow_code: Optional[str] = None
    workflow_name: Optional[str] = None
    description: Optional[str] = None
    definition: Optional[dict] = None
    version: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class WorkflowDefinitionsOut(BaseModel):
    workflow_def_id: uuid.UUID
    workflow_code: str
    workflow_name: str
    description: Optional[str] = None
    definition: dict
    version: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class WorkflowTasksCreate(BaseModel):
    task_id: uuid.UUID
    order_id: uuid.UUID
    workflow_def_id: Optional[uuid.UUID] = None
    step_name: str
    step_seq: int
    status: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    max_retries: Optional[int] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    assigned_to: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class WorkflowTasksUpdate(BaseModel):
    task_id: Optional[uuid.UUID] = None
    order_id: Optional[uuid.UUID] = None
    workflow_def_id: Optional[uuid.UUID] = None
    step_name: Optional[str] = None
    step_seq: Optional[int] = None
    status: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    max_retries: Optional[int] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    assigned_to: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class WorkflowTasksOut(BaseModel):
    task_id: uuid.UUID
    order_id: uuid.UUID
    workflow_def_id: Optional[uuid.UUID] = None
    step_name: str
    step_seq: int
    status: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    max_retries: Optional[int] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    assigned_to: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}
