import uuid
from datetime import date, datetime, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class AbcAssignmentsCreate(BaseModel):
    assignment_id: uuid.UUID
    item_id: uuid.UUID
    class_id: uuid.UUID
    warehouse_id: Optional[uuid.UUID] = None
    compile_date: Optional[date] = None
    annual_usage_value: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class AbcAssignmentsUpdate(BaseModel):
    assignment_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    class_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    compile_date: Optional[date] = None
    annual_usage_value: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class AbcAssignmentsOut(BaseModel):
    assignment_id: uuid.UUID
    item_id: uuid.UUID
    class_id: uuid.UUID
    warehouse_id: Optional[uuid.UUID] = None
    compile_date: Optional[date] = None
    annual_usage_value: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class AbcClassesCreate(BaseModel):
    class_id: uuid.UUID
    class_code: str
    class_name: str
    min_pct: Optional[float] = None
    max_pct: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class AbcClassesUpdate(BaseModel):
    class_id: Optional[uuid.UUID] = None
    class_code: Optional[str] = None
    class_name: Optional[str] = None
    min_pct: Optional[float] = None
    max_pct: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class AbcClassesOut(BaseModel):
    class_id: uuid.UUID
    class_code: str
    class_name: str
    min_pct: Optional[float] = None
    max_pct: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

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
    workflow_def_id: Optional[uuid.UUID] = None
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
    workflow_def_id: Optional[uuid.UUID] = None
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

class CostTypesCreate(BaseModel):
    cost_type_id: uuid.UUID
    cost_type_code: str
    cost_type_name: str
    costing_method: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class CostTypesUpdate(BaseModel):
    cost_type_id: Optional[uuid.UUID] = None
    cost_type_code: Optional[str] = None
    cost_type_name: Optional[str] = None
    costing_method: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class CostTypesOut(BaseModel):
    cost_type_id: uuid.UUID
    cost_type_code: str
    cost_type_name: str
    costing_method: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CycleCountSchedulesCreate(BaseModel):
    schedule_id: uuid.UUID
    schedule_code: str
    schedule_name: str
    class_code: Optional[str] = None
    frequency_days: Optional[int] = None
    warehouse_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1

class CycleCountSchedulesUpdate(BaseModel):
    schedule_id: Optional[uuid.UUID] = None
    schedule_code: Optional[str] = None
    schedule_name: Optional[str] = None
    class_code: Optional[str] = None
    frequency_days: Optional[int] = None
    warehouse_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class CycleCountSchedulesOut(BaseModel):
    schedule_id: uuid.UUID
    schedule_code: str
    schedule_name: str
    class_code: Optional[str] = None
    frequency_days: Optional[int] = None
    warehouse_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
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

class InspectionPlansCreate(BaseModel):
    plan_id: uuid.UUID
    plan_code: str
    plan_name: str
    item_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1

class InspectionPlansUpdate(BaseModel):
    plan_id: Optional[uuid.UUID] = None
    plan_code: Optional[str] = None
    plan_name: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class InspectionPlansOut(BaseModel):
    plan_id: uuid.UUID
    plan_code: str
    plan_name: str
    item_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class InspectionResultsCreate(BaseModel):
    result_id: uuid.UUID
    transaction_id: Optional[uuid.UUID] = None
    plan_id: Optional[uuid.UUID] = None
    inspector_id: Optional[uuid.UUID] = None
    result: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class InspectionResultsUpdate(BaseModel):
    result_id: Optional[uuid.UUID] = None
    transaction_id: Optional[uuid.UUID] = None
    plan_id: Optional[uuid.UUID] = None
    inspector_id: Optional[uuid.UUID] = None
    result: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class InspectionResultsOut(BaseModel):
    result_id: uuid.UUID
    transaction_id: Optional[uuid.UUID] = None
    plan_id: Optional[uuid.UUID] = None
    inspector_id: Optional[uuid.UUID] = None
    result: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class InvCycleCountsCreate(BaseModel):
    cycle_count_id: uuid.UUID
    warehouse_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    count_sequence: Optional[int] = None
    expected_qty: Optional[float] = None
    actual_qty: Optional[float] = None
    variance_qty: Optional[float] = None
    count_date: Optional[date] = None
    counted_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InvCycleCountsUpdate(BaseModel):
    cycle_count_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    count_sequence: Optional[int] = None
    expected_qty: Optional[float] = None
    actual_qty: Optional[float] = None
    variance_qty: Optional[float] = None
    count_date: Optional[date] = None
    counted_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InvCycleCountsOut(BaseModel):
    cycle_count_id: uuid.UUID
    warehouse_id: uuid.UUID
    item_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    count_sequence: Optional[int] = None
    expected_qty: Optional[float] = None
    actual_qty: Optional[float] = None
    variance_qty: Optional[float] = None
    count_date: Optional[date] = None
    counted_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class InvOnhandBalancesCreate(BaseModel):
    onhand_id: uuid.UUID
    item_id: uuid.UUID
    warehouse_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    qty_onhand: float
    qty_reserved: Optional[float] = None
    qty_available: Optional[float] = None
    unit_cost: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InvOnhandBalancesUpdate(BaseModel):
    onhand_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    qty_onhand: Optional[float] = None
    qty_reserved: Optional[float] = None
    qty_available: Optional[float] = None
    unit_cost: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InvOnhandBalancesOut(BaseModel):
    onhand_id: uuid.UUID
    item_id: uuid.UUID
    warehouse_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    qty_onhand: float
    qty_reserved: Optional[float] = None
    qty_available: Optional[float] = None
    unit_cost: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class InvReservationsCreate(BaseModel):
    reservation_id: uuid.UUID
    item_id: uuid.UUID
    warehouse_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    qty_reserved: float
    source_doc_id: Optional[uuid.UUID] = None
    source_line_id: Optional[uuid.UUID] = None
    source_doc_type: Optional[str] = None
    demand_type: Optional[str] = None
    demand_date: Optional[date] = None
    status: Optional[str] = None
    is_active: bool = True
    reservation_no: Optional[str] = None
    reservation_date: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InvReservationsUpdate(BaseModel):
    reservation_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    qty_reserved: Optional[float] = None
    source_doc_id: Optional[uuid.UUID] = None
    source_line_id: Optional[uuid.UUID] = None
    source_doc_type: Optional[str] = None
    demand_type: Optional[str] = None
    demand_date: Optional[date] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    reservation_no: Optional[str] = None
    reservation_date: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InvReservationsOut(BaseModel):
    reservation_id: uuid.UUID
    item_id: uuid.UUID
    warehouse_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    qty_reserved: float
    source_doc_id: Optional[uuid.UUID] = None
    source_line_id: Optional[uuid.UUID] = None
    source_doc_type: Optional[str] = None
    demand_type: Optional[str] = None
    demand_date: Optional[date] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    reservation_no: Optional[str] = None
    reservation_date: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class InvTransactionTypesCreate(BaseModel):
    transaction_type_id: uuid.UUID
    transaction_type_code: str
    transaction_type_name: str
    direction: str
    is_active: bool = True

class InvTransactionTypesUpdate(BaseModel):
    transaction_type_id: Optional[uuid.UUID] = None
    transaction_type_code: Optional[str] = None
    transaction_type_name: Optional[str] = None
    direction: Optional[str] = None
    is_active: Optional[bool] = None

class InvTransactionTypesOut(BaseModel):
    transaction_type_id: uuid.UUID
    transaction_type_code: str
    transaction_type_name: str
    direction: str
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ItemAttributesCreate(BaseModel):
    item_id: uuid.UUID
    item_type: Optional[str] = None
    item_status: Optional[str] = None
    abc_class: Optional[str] = None
    lot_control_flag: Optional[bool] = None
    serial_control_flag: Optional[bool] = None
    shelf_life_days: Optional[int] = None
    minimum_quantity: Optional[float] = None
    maximum_quantity: Optional[float] = None
    safety_stock: Optional[float] = None
    reorder_point: Optional[float] = None
    reorder_quantity: Optional[float] = None
    unit_cost: Optional[float] = None
    average_cost: Optional[float] = None
    last_cost: Optional[float] = None
    standard_cost: Optional[float] = None
    cost_method: Optional[str] = None
    cycle_count_enabled: Optional[bool] = None
    cycle_count_frequency: Optional[int] = None
    default_warehouse_id: Optional[uuid.UUID] = None
    attribute_category: Optional[str] = None
    attribute1: Optional[str] = None
    attribute2: Optional[str] = None
    attribute3: Optional[str] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    is_active: bool = True
    company_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None

class ItemAttributesUpdate(BaseModel):
    item_id: Optional[uuid.UUID] = None
    item_type: Optional[str] = None
    item_status: Optional[str] = None
    abc_class: Optional[str] = None
    lot_control_flag: Optional[bool] = None
    serial_control_flag: Optional[bool] = None
    shelf_life_days: Optional[int] = None
    minimum_quantity: Optional[float] = None
    maximum_quantity: Optional[float] = None
    safety_stock: Optional[float] = None
    reorder_point: Optional[float] = None
    reorder_quantity: Optional[float] = None
    unit_cost: Optional[float] = None
    average_cost: Optional[float] = None
    last_cost: Optional[float] = None
    standard_cost: Optional[float] = None
    cost_method: Optional[str] = None
    cycle_count_enabled: Optional[bool] = None
    cycle_count_frequency: Optional[int] = None
    default_warehouse_id: Optional[uuid.UUID] = None
    attribute_category: Optional[str] = None
    attribute1: Optional[str] = None
    attribute2: Optional[str] = None
    attribute3: Optional[str] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    is_active: Optional[bool] = None
    company_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None

class ItemAttributesOut(BaseModel):
    item_id: uuid.UUID
    item_type: Optional[str] = None
    item_status: Optional[str] = None
    abc_class: Optional[str] = None
    lot_control_flag: Optional[bool] = None
    serial_control_flag: Optional[bool] = None
    shelf_life_days: Optional[int] = None
    minimum_quantity: Optional[float] = None
    maximum_quantity: Optional[float] = None
    safety_stock: Optional[float] = None
    reorder_point: Optional[float] = None
    reorder_quantity: Optional[float] = None
    unit_cost: Optional[float] = None
    average_cost: Optional[float] = None
    last_cost: Optional[float] = None
    standard_cost: Optional[float] = None
    cost_method: Optional[str] = None
    cycle_count_enabled: Optional[bool] = None
    cycle_count_frequency: Optional[int] = None
    default_warehouse_id: Optional[uuid.UUID] = None
    attribute_category: Optional[str] = None
    attribute1: Optional[str] = None
    attribute2: Optional[str] = None
    attribute3: Optional[str] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ItemCostsCreate(BaseModel):
    cost_id: uuid.UUID
    item_id: uuid.UUID
    cost_type_id: uuid.UUID
    unit_cost: Optional[float] = None
    currency_code: Optional[str] = None
    effective_date: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1

class ItemCostsUpdate(BaseModel):
    cost_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    cost_type_id: Optional[uuid.UUID] = None
    unit_cost: Optional[float] = None
    currency_code: Optional[str] = None
    effective_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class ItemCostsOut(BaseModel):
    cost_id: uuid.UUID
    item_id: uuid.UUID
    cost_type_id: uuid.UUID
    unit_cost: Optional[float] = None
    currency_code: Optional[str] = None
    effective_date: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class LotGenealogyCreate(BaseModel):
    geneology_id: uuid.UUID
    lot_id: uuid.UUID
    parent_lot_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    quantity: Optional[float] = None
    transaction_id: Optional[uuid.UUID] = None
    direction: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class LotGenealogyUpdate(BaseModel):
    geneology_id: Optional[uuid.UUID] = None
    lot_id: Optional[uuid.UUID] = None
    parent_lot_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    quantity: Optional[float] = None
    transaction_id: Optional[uuid.UUID] = None
    direction: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class LotGenealogyOut(BaseModel):
    geneology_id: uuid.UUID
    lot_id: uuid.UUID
    parent_lot_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    quantity: Optional[float] = None
    transaction_id: Optional[uuid.UUID] = None
    direction: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class LotMasterCreate(BaseModel):
    lot_id: uuid.UUID
    item_id: uuid.UUID
    lot_number: str
    lot_grade: Optional[str] = None
    lot_status: Optional[str] = None
    manufacturing_date: Optional[date] = None
    expiration_date: Optional[date] = None
    expiry_alert_days: Optional[int] = None
    origin: Optional[str] = None
    supplier_id: Optional[uuid.UUID] = None
    supplier_lot_number: Optional[str] = None
    received_date: Optional[date] = None
    unit_cost: Optional[float] = None
    is_active: bool = True

class LotMasterUpdate(BaseModel):
    lot_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    lot_grade: Optional[str] = None
    lot_status: Optional[str] = None
    manufacturing_date: Optional[date] = None
    expiration_date: Optional[date] = None
    expiry_alert_days: Optional[int] = None
    origin: Optional[str] = None
    supplier_id: Optional[uuid.UUID] = None
    supplier_lot_number: Optional[str] = None
    received_date: Optional[date] = None
    unit_cost: Optional[float] = None
    is_active: Optional[bool] = None

class LotMasterOut(BaseModel):
    lot_id: uuid.UUID
    item_id: uuid.UUID
    lot_number: str
    lot_grade: Optional[str] = None
    lot_status: Optional[str] = None
    manufacturing_date: Optional[date] = None
    expiration_date: Optional[date] = None
    expiry_alert_days: Optional[int] = None
    origin: Optional[str] = None
    supplier_id: Optional[uuid.UUID] = None
    supplier_lot_number: Optional[str] = None
    received_date: Optional[date] = None
    unit_cost: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class LotOnhandCreate(BaseModel):
    lot_onhand_id: uuid.UUID
    lot_id: uuid.UUID
    item_id: uuid.UUID
    warehouse_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    qty_onhand: float
    qty_reserved: Optional[float] = None
    qty_available: Optional[float] = None
    unit_cost: Optional[float] = None
    is_active: bool = True

class LotOnhandUpdate(BaseModel):
    lot_onhand_id: Optional[uuid.UUID] = None
    lot_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    qty_onhand: Optional[float] = None
    qty_reserved: Optional[float] = None
    qty_available: Optional[float] = None
    unit_cost: Optional[float] = None
    is_active: Optional[bool] = None

class LotOnhandOut(BaseModel):
    lot_onhand_id: uuid.UUID
    lot_id: uuid.UUID
    item_id: uuid.UUID
    warehouse_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    qty_onhand: float
    qty_reserved: Optional[float] = None
    qty_available: Optional[float] = None
    unit_cost: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class LpnContentsCreate(BaseModel):
    content_id: uuid.UUID
    lpn_id: uuid.UUID
    item_id: uuid.UUID
    lot_id: Optional[uuid.UUID] = None
    serial_id: Optional[uuid.UUID] = None
    quantity: float
    is_active: bool = True
    object_version_number: int = 1

class LpnContentsUpdate(BaseModel):
    content_id: Optional[uuid.UUID] = None
    lpn_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    lot_id: Optional[uuid.UUID] = None
    serial_id: Optional[uuid.UUID] = None
    quantity: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class LpnContentsOut(BaseModel):
    content_id: uuid.UUID
    lpn_id: uuid.UUID
    item_id: uuid.UUID
    lot_id: Optional[uuid.UUID] = None
    serial_id: Optional[uuid.UUID] = None
    quantity: float
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class LpnMasterCreate(BaseModel):
    lpn_id: uuid.UUID
    lpn_number: str
    lpn_type: Optional[str] = None
    parent_lpn_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    lot_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    weight_kg: Optional[float] = None
    volume_cbm: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class LpnMasterUpdate(BaseModel):
    lpn_id: Optional[uuid.UUID] = None
    lpn_number: Optional[str] = None
    lpn_type: Optional[str] = None
    parent_lpn_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    lot_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    weight_kg: Optional[float] = None
    volume_cbm: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class LpnMasterOut(BaseModel):
    lpn_id: uuid.UUID
    lpn_number: str
    lpn_type: Optional[str] = None
    parent_lpn_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    lot_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    weight_kg: Optional[float] = None
    volume_cbm: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MaterialTransactionsCreate(BaseModel):
    transaction_id: uuid.UUID
    transaction_type_id: Optional[uuid.UUID] = None
    transaction_type: str
    transaction_source: Optional[str] = None
    source_doc_id: Optional[uuid.UUID] = None
    source_doc_type: Optional[str] = None
    source_line_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    warehouse_id: uuid.UUID
    location_from_id: Optional[uuid.UUID] = None
    location_to_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    qty: float
    uom_code: Optional[str] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    currency_code: Optional[str] = None
    reference_number: Optional[str] = None
    description: Optional[str] = None
    transaction_date: datetime
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MaterialTransactionsUpdate(BaseModel):
    transaction_id: Optional[uuid.UUID] = None
    transaction_type_id: Optional[uuid.UUID] = None
    transaction_type: Optional[str] = None
    transaction_source: Optional[str] = None
    source_doc_id: Optional[uuid.UUID] = None
    source_doc_type: Optional[str] = None
    source_line_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    location_from_id: Optional[uuid.UUID] = None
    location_to_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    qty: Optional[float] = None
    uom_code: Optional[str] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    currency_code: Optional[str] = None
    reference_number: Optional[str] = None
    description: Optional[str] = None
    transaction_date: Optional[datetime] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MaterialTransactionsOut(BaseModel):
    transaction_id: uuid.UUID
    transaction_type_id: Optional[uuid.UUID] = None
    transaction_type: str
    transaction_source: Optional[str] = None
    source_doc_id: Optional[uuid.UUID] = None
    source_doc_type: Optional[str] = None
    source_line_id: Optional[uuid.UUID] = None
    item_id: uuid.UUID
    warehouse_id: uuid.UUID
    location_from_id: Optional[uuid.UUID] = None
    location_to_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    qty: float
    uom_code: Optional[str] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    currency_code: Optional[str] = None
    reference_number: Optional[str] = None
    description: Optional[str] = None
    transaction_date: datetime
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MoveOrderHeadersCreate(BaseModel):
    move_order_id: uuid.UUID
    move_order_number: str
    source_warehouse_id: Optional[uuid.UUID] = None
    dest_warehouse_id: Optional[uuid.UUID] = None
    move_type: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MoveOrderHeadersUpdate(BaseModel):
    move_order_id: Optional[uuid.UUID] = None
    move_order_number: Optional[str] = None
    source_warehouse_id: Optional[uuid.UUID] = None
    dest_warehouse_id: Optional[uuid.UUID] = None
    move_type: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MoveOrderHeadersOut(BaseModel):
    move_order_id: uuid.UUID
    move_order_number: str
    source_warehouse_id: Optional[uuid.UUID] = None
    dest_warehouse_id: Optional[uuid.UUID] = None
    move_type: Optional[str] = None
    status: Optional[str] = None
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

class MoveOrderLinesCreate(BaseModel):
    move_line_id: uuid.UUID
    move_order_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    qty_requested: float
    qty_moved: Optional[float] = None
    from_location_id: Optional[uuid.UUID] = None
    to_location_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MoveOrderLinesUpdate(BaseModel):
    move_line_id: Optional[uuid.UUID] = None
    move_order_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    qty_requested: Optional[float] = None
    qty_moved: Optional[float] = None
    from_location_id: Optional[uuid.UUID] = None
    to_location_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MoveOrderLinesOut(BaseModel):
    move_line_id: uuid.UUID
    move_order_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    qty_requested: float
    qty_moved: Optional[float] = None
    from_location_id: Optional[uuid.UUID] = None
    to_location_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class PhysicalInventoryHeadersCreate(BaseModel):
    inv_header_id: uuid.UUID
    inventory_number: str
    warehouse_id: uuid.UUID
    description: Optional[str] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PhysicalInventoryHeadersUpdate(BaseModel):
    inv_header_id: Optional[uuid.UUID] = None
    inventory_number: Optional[str] = None
    warehouse_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PhysicalInventoryHeadersOut(BaseModel):
    inv_header_id: uuid.UUID
    inventory_number: str
    warehouse_id: uuid.UUID
    description: Optional[str] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class PhysicalInventoryLinesCreate(BaseModel):
    inv_line_id: uuid.UUID
    inv_header_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    expected_qty: Optional[float] = None
    actual_qty: Optional[float] = None
    variance_qty: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PhysicalInventoryLinesUpdate(BaseModel):
    inv_line_id: Optional[uuid.UUID] = None
    inv_header_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    expected_qty: Optional[float] = None
    actual_qty: Optional[float] = None
    variance_qty: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PhysicalInventoryLinesOut(BaseModel):
    inv_line_id: uuid.UUID
    inv_header_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    expected_qty: Optional[float] = None
    actual_qty: Optional[float] = None
    variance_qty: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ReplenishmentRulesCreate(BaseModel):
    rule_id: uuid.UUID
    rule_code: str
    rule_name: str
    rule_type: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    min_qty: Optional[float] = None
    max_qty: Optional[float] = None
    reorder_point: Optional[float] = None
    safety_stock: Optional[float] = None
    lead_time_days: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1

class ReplenishmentRulesUpdate(BaseModel):
    rule_id: Optional[uuid.UUID] = None
    rule_code: Optional[str] = None
    rule_name: Optional[str] = None
    rule_type: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    min_qty: Optional[float] = None
    max_qty: Optional[float] = None
    reorder_point: Optional[float] = None
    safety_stock: Optional[float] = None
    lead_time_days: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class ReplenishmentRulesOut(BaseModel):
    rule_id: uuid.UUID
    rule_code: str
    rule_name: str
    rule_type: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    min_qty: Optional[float] = None
    max_qty: Optional[float] = None
    reorder_point: Optional[float] = None
    safety_stock: Optional[float] = None
    lead_time_days: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class SerialCreate(BaseModel):
    serial_id: uuid.UUID
    serial_number: str
    item_id: uuid.UUID
    warehouse_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    lot_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    current_status: Optional[str] = None
    manufacture_date: Optional[date] = None
    expiry_date: Optional[date] = None
    unit_cost: Optional[float] = None
    is_active: bool = True

class SerialUpdate(BaseModel):
    serial_id: Optional[uuid.UUID] = None
    serial_number: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    warehouse_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    lot_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    current_status: Optional[str] = None
    manufacture_date: Optional[date] = None
    expiry_date: Optional[date] = None
    unit_cost: Optional[float] = None
    is_active: Optional[bool] = None

class SerialOut(BaseModel):
    serial_id: uuid.UUID
    serial_number: str
    item_id: uuid.UUID
    warehouse_id: uuid.UUID
    location_id: Optional[uuid.UUID] = None
    lot_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    current_status: Optional[str] = None
    manufacture_date: Optional[date] = None
    expiry_date: Optional[date] = None
    unit_cost: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class SerialGenealogyCreate(BaseModel):
    geneology_id: uuid.UUID
    serial_id: uuid.UUID
    parent_serial_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    transaction_id: Optional[uuid.UUID] = None
    direction: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class SerialGenealogyUpdate(BaseModel):
    geneology_id: Optional[uuid.UUID] = None
    serial_id: Optional[uuid.UUID] = None
    parent_serial_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    transaction_id: Optional[uuid.UUID] = None
    direction: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class SerialGenealogyOut(BaseModel):
    geneology_id: uuid.UUID
    serial_id: uuid.UUID
    parent_serial_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    transaction_id: Optional[uuid.UUID] = None
    direction: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class TransferOrderLinesCreate(BaseModel):
    transfer_line_id: uuid.UUID
    transfer_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    qty_requested: float
    qty_shipped: Optional[float] = None
    qty_received: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TransferOrderLinesUpdate(BaseModel):
    transfer_line_id: Optional[uuid.UUID] = None
    transfer_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    qty_requested: Optional[float] = None
    qty_shipped: Optional[float] = None
    qty_received: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TransferOrderLinesOut(BaseModel):
    transfer_line_id: uuid.UUID
    transfer_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    qty_requested: float
    qty_shipped: Optional[float] = None
    qty_received: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TransferOrdersCreate(BaseModel):
    transfer_id: uuid.UUID
    transfer_number: str
    source_warehouse_id: uuid.UUID
    dest_warehouse_id: uuid.UUID
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TransferOrdersUpdate(BaseModel):
    transfer_id: Optional[uuid.UUID] = None
    transfer_number: Optional[str] = None
    source_warehouse_id: Optional[uuid.UUID] = None
    dest_warehouse_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TransferOrdersOut(BaseModel):
    transfer_id: uuid.UUID
    transfer_number: str
    source_warehouse_id: uuid.UUID
    dest_warehouse_id: uuid.UUID
    status: Optional[str] = None
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
    workflow_def_id: Optional[uuid.UUID] = None
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
    doc_type: str
    doc_id: uuid.UUID
    workflow_def_id: Optional[uuid.UUID] = None
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
