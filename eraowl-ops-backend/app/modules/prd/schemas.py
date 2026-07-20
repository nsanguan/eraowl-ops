import uuid
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class AiAgentLogsCreate(BaseModel):
    log_id: uuid.UUID
    state_id: Optional[uuid.UUID] = None
    doc_id: Optional[uuid.UUID] = None
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
    doc_id: Optional[uuid.UUID] = None
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
    doc_id: Optional[uuid.UUID] = None
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
    doc_id: Optional[uuid.UUID] = None
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
    doc_id: Optional[uuid.UUID] = None
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
    doc_id: Optional[uuid.UUID] = None
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
    doc_type: str
    doc_id: uuid.UUID
    thread_id: Optional[str] = None
    state_data: dict
    status: Optional[str] = None
    checkpoint: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class AiWorkflowStateUpdate(BaseModel):
    state_id: Optional[uuid.UUID] = None
    doc_type: Optional[str] = None
    doc_id: Optional[uuid.UUID] = None
    thread_id: Optional[str] = None
    state_data: Optional[dict] = None
    status: Optional[str] = None
    checkpoint: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class AiWorkflowStateOut(BaseModel):
    state_id: uuid.UUID
    doc_type: str
    doc_id: uuid.UUID
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

class BomComponentsExtCreate(BaseModel):
    comp_ext_id: uuid.UUID
    bom_id: uuid.UUID
    component_item_id: uuid.UUID
    quantity: float
    uom_code: Optional[str] = None
    supply_type: Optional[str] = None
    operation_seq: Optional[int] = None
    yield_pct: Optional[float] = None
    scrap_factor: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class BomComponentsExtUpdate(BaseModel):
    comp_ext_id: Optional[uuid.UUID] = None
    bom_id: Optional[uuid.UUID] = None
    component_item_id: Optional[uuid.UUID] = None
    quantity: Optional[float] = None
    uom_code: Optional[str] = None
    supply_type: Optional[str] = None
    operation_seq: Optional[int] = None
    yield_pct: Optional[float] = None
    scrap_factor: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class BomComponentsExtOut(BaseModel):
    comp_ext_id: uuid.UUID
    bom_id: uuid.UUID
    component_item_id: uuid.UUID
    quantity: float
    uom_code: Optional[str] = None
    supply_type: Optional[str] = None
    operation_seq: Optional[int] = None
    yield_pct: Optional[float] = None
    scrap_factor: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class EngineeringChangeOrdersCreate(BaseModel):
    eco_id: uuid.UUID
    eco_number: str
    eco_type: Optional[str] = None
    description: Optional[str] = None
    reason: Optional[str] = None
    status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    effectivity_date: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class EngineeringChangeOrdersUpdate(BaseModel):
    eco_id: Optional[uuid.UUID] = None
    eco_number: Optional[str] = None
    eco_type: Optional[str] = None
    description: Optional[str] = None
    reason: Optional[str] = None
    status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    effectivity_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class EngineeringChangeOrdersOut(BaseModel):
    eco_id: uuid.UUID
    eco_number: str
    eco_type: Optional[str] = None
    description: Optional[str] = None
    reason: Optional[str] = None
    status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    effectivity_date: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
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

class ImportInterfaceCreate(BaseModel):
    import_id: uuid.UUID
    source_system: str
    source_transaction_id: str
    payload: dict
    doc_type: Optional[str] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    processed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class ImportInterfaceUpdate(BaseModel):
    import_id: Optional[uuid.UUID] = None
    source_system: Optional[str] = None
    source_transaction_id: Optional[str] = None
    payload: Optional[dict] = None
    doc_type: Optional[str] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    processed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class ImportInterfaceOut(BaseModel):
    import_id: uuid.UUID
    source_system: str
    source_transaction_id: str
    payload: dict
    doc_type: Optional[str] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    processed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MpsEntriesCreate(BaseModel):
    mps_id: uuid.UUID
    item_id: uuid.UUID
    quantity: float
    due_date: date
    mps_type: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MpsEntriesUpdate(BaseModel):
    mps_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    quantity: Optional[float] = None
    due_date: Optional[date] = None
    mps_type: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MpsEntriesOut(BaseModel):
    mps_id: uuid.UUID
    item_id: uuid.UUID
    quantity: float
    due_date: date
    mps_type: Optional[str] = None
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

class MrpRecommendationsCreate(BaseModel):
    recommendation_id: uuid.UUID
    item_id: uuid.UUID
    recommendation_type: str
    quantity: float
    due_date: Optional[date] = None
    order_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpRecommendationsUpdate(BaseModel):
    recommendation_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    recommendation_type: Optional[str] = None
    quantity: Optional[float] = None
    due_date: Optional[date] = None
    order_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MrpRecommendationsOut(BaseModel):
    recommendation_id: uuid.UUID
    item_id: uuid.UUID
    recommendation_type: str
    quantity: float
    due_date: Optional[date] = None
    order_id: Optional[uuid.UUID] = None
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

class ProdWorkOrdersCreate(BaseModel):
    wo_id: uuid.UUID
    routing_id: uuid.UUID
    wo_number: str
    qty_target: float
    uom_code: Optional[str] = None
    status: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ProdWorkOrdersUpdate(BaseModel):
    wo_id: Optional[uuid.UUID] = None
    routing_id: Optional[uuid.UUID] = None
    wo_number: Optional[str] = None
    qty_target: Optional[float] = None
    uom_code: Optional[str] = None
    status: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ProdWorkOrdersOut(BaseModel):
    wo_id: uuid.UUID
    routing_id: uuid.UUID
    wo_number: str
    qty_target: float
    uom_code: Optional[str] = None
    status: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ProductionCalendarCreate(BaseModel):
    calendar_id: uuid.UUID
    calendar_code: str
    calendar_name: str
    start_date: date
    end_date: date
    is_active: bool = True
    object_version_number: int = 1

class ProductionCalendarUpdate(BaseModel):
    calendar_id: Optional[uuid.UUID] = None
    calendar_code: Optional[str] = None
    calendar_name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class ProductionCalendarOut(BaseModel):
    calendar_id: uuid.UUID
    calendar_code: str
    calendar_name: str
    start_date: date
    end_date: date
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ResourcesCreate(BaseModel):
    resource_id: uuid.UUID
    resource_code: str
    resource_name: str
    resource_type: Optional[str] = None
    work_center_id: Optional[uuid.UUID] = None
    cost_rate: Optional[float] = None
    overtime_rate: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class ResourcesUpdate(BaseModel):
    resource_id: Optional[uuid.UUID] = None
    resource_code: Optional[str] = None
    resource_name: Optional[str] = None
    resource_type: Optional[str] = None
    work_center_id: Optional[uuid.UUID] = None
    cost_rate: Optional[float] = None
    overtime_rate: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class ResourcesOut(BaseModel):
    resource_id: uuid.UUID
    resource_code: str
    resource_name: str
    resource_type: Optional[str] = None
    work_center_id: Optional[uuid.UUID] = None
    cost_rate: Optional[float] = None
    overtime_rate: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class RoutingHeadersCreate(BaseModel):
    routing_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    mfg_mode: str
    routing_name: str
    is_active: bool = True

class RoutingHeadersUpdate(BaseModel):
    routing_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    mfg_mode: Optional[str] = None
    routing_name: Optional[str] = None
    is_active: Optional[bool] = None

class RoutingHeadersOut(BaseModel):
    routing_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    mfg_mode: str
    routing_name: str
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class RoutingOperationsCreate(BaseModel):
    operation_id: uuid.UUID
    routing_id: uuid.UUID
    operation_seq: int
    operation_code: str
    site_id: Optional[uuid.UUID] = None
    standard_run_hours: Optional[float] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class RoutingOperationsUpdate(BaseModel):
    operation_id: Optional[uuid.UUID] = None
    routing_id: Optional[uuid.UUID] = None
    operation_seq: Optional[int] = None
    operation_code: Optional[str] = None
    site_id: Optional[uuid.UUID] = None
    standard_run_hours: Optional[float] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class RoutingOperationsOut(BaseModel):
    operation_id: uuid.UUID
    routing_id: uuid.UUID
    operation_seq: int
    operation_code: str
    site_id: Optional[uuid.UUID] = None
    standard_run_hours: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class WipMovementsCreate(BaseModel):
    movement_id: uuid.UUID
    work_order_id: uuid.UUID
    from_operation_seq: Optional[int] = None
    to_operation_seq: Optional[int] = None
    item_id: Optional[uuid.UUID] = None
    qty: float
    movement_type: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class WipMovementsUpdate(BaseModel):
    movement_id: Optional[uuid.UUID] = None
    work_order_id: Optional[uuid.UUID] = None
    from_operation_seq: Optional[int] = None
    to_operation_seq: Optional[int] = None
    item_id: Optional[uuid.UUID] = None
    qty: Optional[float] = None
    movement_type: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class WipMovementsOut(BaseModel):
    movement_id: uuid.UUID
    work_order_id: uuid.UUID
    from_operation_seq: Optional[int] = None
    to_operation_seq: Optional[int] = None
    item_id: Optional[uuid.UUID] = None
    qty: float
    movement_type: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class WorkCentersCreate(BaseModel):
    work_center_id: uuid.UUID
    center_code: str
    center_name: str
    center_type: Optional[str] = None
    department: Optional[str] = None
    site_id: Optional[uuid.UUID] = None
    capacity_hours: Optional[float] = None
    efficiency_pct: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class WorkCentersUpdate(BaseModel):
    work_center_id: Optional[uuid.UUID] = None
    center_code: Optional[str] = None
    center_name: Optional[str] = None
    center_type: Optional[str] = None
    department: Optional[str] = None
    site_id: Optional[uuid.UUID] = None
    capacity_hours: Optional[float] = None
    efficiency_pct: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class WorkCentersOut(BaseModel):
    work_center_id: uuid.UUID
    center_code: str
    center_name: str
    center_type: Optional[str] = None
    department: Optional[str] = None
    site_id: Optional[uuid.UUID] = None
    capacity_hours: Optional[float] = None
    efficiency_pct: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class WorkOrderOperationsCreate(BaseModel):
    wo_operation_id: uuid.UUID
    work_order_id: uuid.UUID
    operation_id: Optional[uuid.UUID] = None
    operation_seq: int
    operation_code: Optional[str] = None
    description: Optional[str] = None
    work_center_id: Optional[uuid.UUID] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    qty_completed: Optional[float] = None
    qty_scrapped: Optional[float] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class WorkOrderOperationsUpdate(BaseModel):
    wo_operation_id: Optional[uuid.UUID] = None
    work_order_id: Optional[uuid.UUID] = None
    operation_id: Optional[uuid.UUID] = None
    operation_seq: Optional[int] = None
    operation_code: Optional[str] = None
    description: Optional[str] = None
    work_center_id: Optional[uuid.UUID] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    qty_completed: Optional[float] = None
    qty_scrapped: Optional[float] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class WorkOrderOperationsOut(BaseModel):
    wo_operation_id: uuid.UUID
    work_order_id: uuid.UUID
    operation_id: Optional[uuid.UUID] = None
    operation_seq: int
    operation_code: Optional[str] = None
    description: Optional[str] = None
    work_center_id: Optional[uuid.UUID] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    qty_completed: Optional[float] = None
    qty_scrapped: Optional[float] = None
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

class WorkOrderRequirementsCreate(BaseModel):
    requirement_id: uuid.UUID
    work_order_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    qty_required: float
    qty_issued: Optional[float] = None
    qty_scrapped: Optional[float] = None
    uom_code: Optional[str] = None
    operation_seq: Optional[int] = None
    supply_type: Optional[str] = None
    requirement_date: Optional[date] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class WorkOrderRequirementsUpdate(BaseModel):
    requirement_id: Optional[uuid.UUID] = None
    work_order_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    qty_required: Optional[float] = None
    qty_issued: Optional[float] = None
    qty_scrapped: Optional[float] = None
    uom_code: Optional[str] = None
    operation_seq: Optional[int] = None
    supply_type: Optional[str] = None
    requirement_date: Optional[date] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class WorkOrderRequirementsOut(BaseModel):
    requirement_id: uuid.UUID
    work_order_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    qty_required: float
    qty_issued: Optional[float] = None
    qty_scrapped: Optional[float] = None
    uom_code: Optional[str] = None
    operation_seq: Optional[int] = None
    supply_type: Optional[str] = None
    requirement_date: Optional[date] = None
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
    doc_type: str
    doc_id: uuid.UUID
    step_name: str
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
    is_active: bool = True
    object_version_number: int = 1

class WorkflowTasksUpdate(BaseModel):
    task_id: Optional[uuid.UUID] = None
    doc_type: Optional[str] = None
    doc_id: Optional[uuid.UUID] = None
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
    doc_type: str
    doc_id: uuid.UUID
    step_name: str
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
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}
