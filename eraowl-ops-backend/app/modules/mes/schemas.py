import uuid
from datetime import date, datetime, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class JobOrdersCreate(BaseModel):
    job_order_id: uuid.UUID
    wo_id: Optional[uuid.UUID] = None
    operation_id: Optional[uuid.UUID] = None
    work_center_id: uuid.UUID
    job_status: Optional[str] = None
    qty_produced: Optional[float] = None
    qty_scrap: Optional[float] = None

class JobOrdersUpdate(BaseModel):
    job_order_id: Optional[uuid.UUID] = None
    wo_id: Optional[uuid.UUID] = None
    operation_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    job_status: Optional[str] = None
    qty_produced: Optional[float] = None
    qty_scrap: Optional[float] = None

class JobOrdersOut(BaseModel):
    job_order_id: uuid.UUID
    wo_id: Optional[uuid.UUID] = None
    operation_id: Optional[uuid.UUID] = None
    work_center_id: uuid.UUID
    job_status: Optional[str] = None
    qty_produced: Optional[float] = None
    qty_scrap: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MachineTelemetryCreate(BaseModel):
    telemetry_id: uuid.UUID
    work_center_id: uuid.UUID
    job_order_id: Optional[uuid.UUID] = None
    metric_name: str
    metric_value: float
    metric_text: Optional[str] = None
    recorded_at: datetime

class MachineTelemetryUpdate(BaseModel):
    telemetry_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    job_order_id: Optional[uuid.UUID] = None
    metric_name: Optional[str] = None
    metric_value: Optional[float] = None
    metric_text: Optional[str] = None
    recorded_at: Optional[datetime] = None

class MachineTelemetryOut(BaseModel):
    telemetry_id: uuid.UUID
    work_center_id: uuid.UUID
    job_order_id: Optional[uuid.UUID] = None
    metric_name: str
    metric_value: float
    metric_text: Optional[str] = None
    recorded_at: datetime
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MesAiAgentLogsCreate(BaseModel):
    log_id: uuid.UUID
    agent_name: Optional[str] = None
    agent_type: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    reasoning: Optional[str] = None
    tool_calls: Optional[dict] = None
    llm_calls: Optional[dict] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    logged_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesAiAgentLogsUpdate(BaseModel):
    log_id: Optional[uuid.UUID] = None
    agent_name: Optional[str] = None
    agent_type: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    reasoning: Optional[str] = None
    tool_calls: Optional[dict] = None
    llm_calls: Optional[dict] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    logged_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesAiAgentLogsOut(BaseModel):
    log_id: uuid.UUID
    agent_name: Optional[str] = None
    agent_type: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    reasoning: Optional[str] = None
    tool_calls: Optional[dict] = None
    llm_calls: Optional[dict] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    logged_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesAiFeatureStoreCreate(BaseModel):
    feature_id: uuid.UUID
    feature_name: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    feature_data: Optional[dict] = None
    feature_timestamp: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesAiFeatureStoreUpdate(BaseModel):
    feature_id: Optional[uuid.UUID] = None
    feature_name: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    feature_data: Optional[dict] = None
    feature_timestamp: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesAiFeatureStoreOut(BaseModel):
    feature_id: uuid.UUID
    feature_name: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    feature_data: Optional[dict] = None
    feature_timestamp: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesAiModelRegistryCreate(BaseModel):
    registry_id: uuid.UUID
    model_name: Optional[str] = None
    model_version: Optional[str] = None
    model_type: Optional[str] = None
    framework: Optional[str] = None
    artifact_path: Optional[str] = None
    metrics: Optional[dict] = None
    status: Optional[str] = None
    registered_by: Optional[uuid.UUID] = None
    registered_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesAiModelRegistryUpdate(BaseModel):
    registry_id: Optional[uuid.UUID] = None
    model_name: Optional[str] = None
    model_version: Optional[str] = None
    model_type: Optional[str] = None
    framework: Optional[str] = None
    artifact_path: Optional[str] = None
    metrics: Optional[dict] = None
    status: Optional[str] = None
    registered_by: Optional[uuid.UUID] = None
    registered_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesAiModelRegistryOut(BaseModel):
    registry_id: uuid.UUID
    model_name: Optional[str] = None
    model_version: Optional[str] = None
    model_type: Optional[str] = None
    framework: Optional[str] = None
    artifact_path: Optional[str] = None
    metrics: Optional[dict] = None
    status: Optional[str] = None
    registered_by: Optional[uuid.UUID] = None
    registered_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesAiWorkflowStatesCreate(BaseModel):
    state_id: uuid.UUID
    workflow_type: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    state_data: Optional[dict] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesAiWorkflowStatesUpdate(BaseModel):
    state_id: Optional[uuid.UUID] = None
    workflow_type: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    state_data: Optional[dict] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesAiWorkflowStatesOut(BaseModel):
    state_id: uuid.UUID
    workflow_type: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    state_data: Optional[dict] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesAlertsCreate(BaseModel):
    alert_id: uuid.UUID
    alert_type: str
    severity: str
    source_type: Optional[str] = None
    source_id: Optional[uuid.UUID] = None
    title: Optional[str] = None
    message: Optional[str] = None
    status: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    assigned_at: Optional[datetime] = None
    acknowledged_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    resolution: Optional[str] = None
    escalation_level: Optional[int] = None
    alert_time: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesAlertsUpdate(BaseModel):
    alert_id: Optional[uuid.UUID] = None
    alert_type: Optional[str] = None
    severity: Optional[str] = None
    source_type: Optional[str] = None
    source_id: Optional[uuid.UUID] = None
    title: Optional[str] = None
    message: Optional[str] = None
    status: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    assigned_at: Optional[datetime] = None
    acknowledged_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    resolution: Optional[str] = None
    escalation_level: Optional[int] = None
    alert_time: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesAlertsOut(BaseModel):
    alert_id: uuid.UUID
    alert_type: str
    severity: str
    source_type: Optional[str] = None
    source_id: Optional[uuid.UUID] = None
    title: Optional[str] = None
    message: Optional[str] = None
    status: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    assigned_at: Optional[datetime] = None
    acknowledged_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    resolution: Optional[str] = None
    escalation_level: Optional[int] = None
    alert_time: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesAlgorithmsCreate(BaseModel):
    algorithm_id: uuid.UUID
    algorithm_type: Optional[str] = None
    algorithm_name: str
    description: Optional[str] = None
    inputs_json: Optional[dict] = None
    outputs_json: Optional[dict] = None
    config_json: Optional[dict] = None
    version: Optional[str] = None
    language: Optional[str] = None
    source_code: Optional[str] = None
    documentation: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesAlgorithmsUpdate(BaseModel):
    algorithm_id: Optional[uuid.UUID] = None
    algorithm_type: Optional[str] = None
    algorithm_name: Optional[str] = None
    description: Optional[str] = None
    inputs_json: Optional[dict] = None
    outputs_json: Optional[dict] = None
    config_json: Optional[dict] = None
    version: Optional[str] = None
    language: Optional[str] = None
    source_code: Optional[str] = None
    documentation: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesAlgorithmsOut(BaseModel):
    algorithm_id: uuid.UUID
    algorithm_type: Optional[str] = None
    algorithm_name: str
    description: Optional[str] = None
    inputs_json: Optional[dict] = None
    outputs_json: Optional[dict] = None
    config_json: Optional[dict] = None
    version: Optional[str] = None
    language: Optional[str] = None
    source_code: Optional[str] = None
    documentation: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesAndonBoardsCreate(BaseModel):
    board_id: uuid.UUID
    board_code: str
    board_name: Optional[str] = None
    location: Optional[str] = None
    display_config: Optional[dict] = None
    is_active: bool = True
    object_version_number: int = 1

class MesAndonBoardsUpdate(BaseModel):
    board_id: Optional[uuid.UUID] = None
    board_code: Optional[str] = None
    board_name: Optional[str] = None
    location: Optional[str] = None
    display_config: Optional[dict] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesAndonBoardsOut(BaseModel):
    board_id: uuid.UUID
    board_code: str
    board_name: Optional[str] = None
    location: Optional[str] = None
    display_config: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesAndonTriggersCreate(BaseModel):
    trigger_id: uuid.UUID
    board_id: Optional[uuid.UUID] = None
    alert_id: Optional[uuid.UUID] = None
    triggered_at: Optional[datetime] = None
    display_message: Optional[str] = None
    audio_played: Optional[bool] = None
    cleared_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesAndonTriggersUpdate(BaseModel):
    trigger_id: Optional[uuid.UUID] = None
    board_id: Optional[uuid.UUID] = None
    alert_id: Optional[uuid.UUID] = None
    triggered_at: Optional[datetime] = None
    display_message: Optional[str] = None
    audio_played: Optional[bool] = None
    cleared_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesAndonTriggersOut(BaseModel):
    trigger_id: uuid.UUID
    board_id: Optional[uuid.UUID] = None
    alert_id: Optional[uuid.UUID] = None
    triggered_at: Optional[datetime] = None
    display_message: Optional[str] = None
    audio_played: Optional[bool] = None
    cleared_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesBatchRecordMaterialsCreate(BaseModel):
    material_id: uuid.UUID
    batch_record_id: uuid.UUID
    item_code: Optional[str] = None
    item_name: Optional[str] = None
    planned_qty: Optional[float] = None
    actual_qty: Optional[float] = None
    uom: Optional[str] = None
    lot_number: Optional[str] = None
    added_at: Optional[datetime] = None
    added_by: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1

class MesBatchRecordMaterialsUpdate(BaseModel):
    material_id: Optional[uuid.UUID] = None
    batch_record_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    item_name: Optional[str] = None
    planned_qty: Optional[float] = None
    actual_qty: Optional[float] = None
    uom: Optional[str] = None
    lot_number: Optional[str] = None
    added_at: Optional[datetime] = None
    added_by: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesBatchRecordMaterialsOut(BaseModel):
    material_id: uuid.UUID
    batch_record_id: uuid.UUID
    item_code: Optional[str] = None
    item_name: Optional[str] = None
    planned_qty: Optional[float] = None
    actual_qty: Optional[float] = None
    uom: Optional[str] = None
    lot_number: Optional[str] = None
    added_at: Optional[datetime] = None
    added_by: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesBatchRecordStepsCreate(BaseModel):
    step_id: uuid.UUID
    batch_record_id: uuid.UUID
    step_sequence: int
    step_name: Optional[str] = None
    step_type: Optional[str] = None
    target_value: Optional[str] = None
    actual_value: Optional[str] = None
    uom: Optional[str] = None
    result: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    operator_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesBatchRecordStepsUpdate(BaseModel):
    step_id: Optional[uuid.UUID] = None
    batch_record_id: Optional[uuid.UUID] = None
    step_sequence: Optional[int] = None
    step_name: Optional[str] = None
    step_type: Optional[str] = None
    target_value: Optional[str] = None
    actual_value: Optional[str] = None
    uom: Optional[str] = None
    result: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    operator_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesBatchRecordStepsOut(BaseModel):
    step_id: uuid.UUID
    batch_record_id: uuid.UUID
    step_sequence: int
    step_name: Optional[str] = None
    step_type: Optional[str] = None
    target_value: Optional[str] = None
    actual_value: Optional[str] = None
    uom: Optional[str] = None
    result: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    operator_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesBatchRecordsCreate(BaseModel):
    batch_record_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    batch_number: str
    product_code: Optional[str] = None
    product_name: Optional[str] = None
    batch_size: Optional[float] = None
    uom: Optional[str] = None
    status: Optional[str] = None
    batch_start: Optional[datetime] = None
    batch_end: Optional[datetime] = None
    recipe_revision: Optional[str] = None
    reviewed_by: Optional[uuid.UUID] = None
    reviewed_at: Optional[datetime] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesBatchRecordsUpdate(BaseModel):
    batch_record_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    batch_number: Optional[str] = None
    product_code: Optional[str] = None
    product_name: Optional[str] = None
    batch_size: Optional[float] = None
    uom: Optional[str] = None
    status: Optional[str] = None
    batch_start: Optional[datetime] = None
    batch_end: Optional[datetime] = None
    recipe_revision: Optional[str] = None
    reviewed_by: Optional[uuid.UUID] = None
    reviewed_at: Optional[datetime] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesBatchRecordsOut(BaseModel):
    batch_record_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    batch_number: str
    product_code: Optional[str] = None
    product_name: Optional[str] = None
    batch_size: Optional[float] = None
    uom: Optional[str] = None
    status: Optional[str] = None
    batch_start: Optional[datetime] = None
    batch_end: Optional[datetime] = None
    recipe_revision: Optional[str] = None
    reviewed_by: Optional[uuid.UUID] = None
    reviewed_at: Optional[datetime] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
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

class MesCrewAssignmentsCreate(BaseModel):
    assignment_id: uuid.UUID
    crew_id: uuid.UUID
    operator_id: uuid.UUID
    role: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesCrewAssignmentsUpdate(BaseModel):
    assignment_id: Optional[uuid.UUID] = None
    crew_id: Optional[uuid.UUID] = None
    operator_id: Optional[uuid.UUID] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesCrewAssignmentsOut(BaseModel):
    assignment_id: uuid.UUID
    crew_id: uuid.UUID
    operator_id: uuid.UUID
    role: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesCrewsCreate(BaseModel):
    crew_id: uuid.UUID
    crew_code: str
    crew_name: str
    supervisor_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesCrewsUpdate(BaseModel):
    crew_id: Optional[uuid.UUID] = None
    crew_code: Optional[str] = None
    crew_name: Optional[str] = None
    supervisor_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesCrewsOut(BaseModel):
    crew_id: uuid.UUID
    crew_code: str
    crew_name: str
    supervisor_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesCribCompartmentsCreate(BaseModel):
    compartment_id: uuid.UUID
    crib_id: uuid.UUID
    compartment_code: Optional[str] = None
    width_cm: Optional[float] = None
    depth_cm: Optional[float] = None
    height_cm: Optional[float] = None
    max_weight_kg: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class MesCribCompartmentsUpdate(BaseModel):
    compartment_id: Optional[uuid.UUID] = None
    crib_id: Optional[uuid.UUID] = None
    compartment_code: Optional[str] = None
    width_cm: Optional[float] = None
    depth_cm: Optional[float] = None
    height_cm: Optional[float] = None
    max_weight_kg: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesCribCompartmentsOut(BaseModel):
    compartment_id: uuid.UUID
    crib_id: uuid.UUID
    compartment_code: Optional[str] = None
    width_cm: Optional[float] = None
    depth_cm: Optional[float] = None
    height_cm: Optional[float] = None
    max_weight_kg: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesCribPackingResultsCreate(BaseModel):
    packing_id: uuid.UUID
    crib_id: uuid.UUID
    tool_id: uuid.UUID
    compartment_id: Optional[uuid.UUID] = None
    position_x: Optional[float] = None
    position_y: Optional[float] = None
    position_z: Optional[float] = None
    rotation: Optional[str] = None
    packed_at: Optional[datetime] = None
    optimized: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1

class MesCribPackingResultsUpdate(BaseModel):
    packing_id: Optional[uuid.UUID] = None
    crib_id: Optional[uuid.UUID] = None
    tool_id: Optional[uuid.UUID] = None
    compartment_id: Optional[uuid.UUID] = None
    position_x: Optional[float] = None
    position_y: Optional[float] = None
    position_z: Optional[float] = None
    rotation: Optional[str] = None
    packed_at: Optional[datetime] = None
    optimized: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesCribPackingResultsOut(BaseModel):
    packing_id: uuid.UUID
    crib_id: uuid.UUID
    tool_id: uuid.UUID
    compartment_id: Optional[uuid.UUID] = None
    position_x: Optional[float] = None
    position_y: Optional[float] = None
    position_z: Optional[float] = None
    rotation: Optional[str] = None
    packed_at: Optional[datetime] = None
    optimized: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesDeliveryRequestsCreate(BaseModel):
    request_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    request_number: Optional[str] = None
    from_location: Optional[str] = None
    to_location: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    qty_required: Optional[float] = None
    uom: Optional[str] = None
    requested_time: Optional[datetime] = None
    required_by_time: Optional[datetime] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    vehicle_id: Optional[uuid.UUID] = None
    assigned_route_id: Optional[uuid.UUID] = None
    delivered_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesDeliveryRequestsUpdate(BaseModel):
    request_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    request_number: Optional[str] = None
    from_location: Optional[str] = None
    to_location: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    qty_required: Optional[float] = None
    uom: Optional[str] = None
    requested_time: Optional[datetime] = None
    required_by_time: Optional[datetime] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    vehicle_id: Optional[uuid.UUID] = None
    assigned_route_id: Optional[uuid.UUID] = None
    delivered_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesDeliveryRequestsOut(BaseModel):
    request_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    request_number: Optional[str] = None
    from_location: Optional[str] = None
    to_location: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    qty_required: Optional[float] = None
    uom: Optional[str] = None
    requested_time: Optional[datetime] = None
    required_by_time: Optional[datetime] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    vehicle_id: Optional[uuid.UUID] = None
    assigned_route_id: Optional[uuid.UUID] = None
    delivered_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesDeliveryRoutesCreate(BaseModel):
    route_id: uuid.UUID
    route_name: Optional[str] = None
    vehicle_id: Optional[uuid.UUID] = None
    stops_json: Optional[dict] = None
    total_distance: Optional[float] = None
    total_duration_min: Optional[float] = None
    distance_uom: Optional[str] = None
    optimized: Optional[bool] = None
    optimization_result_id: Optional[uuid.UUID] = None
    route_date: Optional[date] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesDeliveryRoutesUpdate(BaseModel):
    route_id: Optional[uuid.UUID] = None
    route_name: Optional[str] = None
    vehicle_id: Optional[uuid.UUID] = None
    stops_json: Optional[dict] = None
    total_distance: Optional[float] = None
    total_duration_min: Optional[float] = None
    distance_uom: Optional[str] = None
    optimized: Optional[bool] = None
    optimization_result_id: Optional[uuid.UUID] = None
    route_date: Optional[date] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesDeliveryRoutesOut(BaseModel):
    route_id: uuid.UUID
    route_name: Optional[str] = None
    vehicle_id: Optional[uuid.UUID] = None
    stops_json: Optional[dict] = None
    total_distance: Optional[float] = None
    total_duration_min: Optional[float] = None
    distance_uom: Optional[str] = None
    optimized: Optional[bool] = None
    optimization_result_id: Optional[uuid.UUID] = None
    route_date: Optional[date] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesDigitalTwinModelsCreate(BaseModel):
    twin_id: uuid.UUID
    twin_name: str
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    config_json: Optional[dict] = None
    data_sources_json: Optional[dict] = None
    simulation_results: Optional[dict] = None
    last_sync: Optional[datetime] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesDigitalTwinModelsUpdate(BaseModel):
    twin_id: Optional[uuid.UUID] = None
    twin_name: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    config_json: Optional[dict] = None
    data_sources_json: Optional[dict] = None
    simulation_results: Optional[dict] = None
    last_sync: Optional[datetime] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesDigitalTwinModelsOut(BaseModel):
    twin_id: uuid.UUID
    twin_name: str
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    config_json: Optional[dict] = None
    data_sources_json: Optional[dict] = None
    simulation_results: Optional[dict] = None
    last_sync: Optional[datetime] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesDocumentInstancesCreate(BaseModel):
    instance_id: uuid.UUID
    document_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    instance_data: Optional[dict] = None
    generated_at: Optional[datetime] = None
    printed: Optional[bool] = None
    printed_at: Optional[datetime] = None
    signed_by: Optional[uuid.UUID] = None
    signed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesDocumentInstancesUpdate(BaseModel):
    instance_id: Optional[uuid.UUID] = None
    document_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    instance_data: Optional[dict] = None
    generated_at: Optional[datetime] = None
    printed: Optional[bool] = None
    printed_at: Optional[datetime] = None
    signed_by: Optional[uuid.UUID] = None
    signed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesDocumentInstancesOut(BaseModel):
    instance_id: uuid.UUID
    document_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    instance_data: Optional[dict] = None
    generated_at: Optional[datetime] = None
    printed: Optional[bool] = None
    printed_at: Optional[datetime] = None
    signed_by: Optional[uuid.UUID] = None
    signed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesDocumentsCreate(BaseModel):
    document_id: uuid.UUID
    document_code: str
    document_name: str
    document_type: Optional[str] = None
    template_id: Optional[uuid.UUID] = None
    content: Optional[str] = None
    file_url: Optional[str] = None
    version: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1

class MesDocumentsUpdate(BaseModel):
    document_id: Optional[uuid.UUID] = None
    document_code: Optional[str] = None
    document_name: Optional[str] = None
    document_type: Optional[str] = None
    template_id: Optional[uuid.UUID] = None
    content: Optional[str] = None
    file_url: Optional[str] = None
    version: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesDocumentsOut(BaseModel):
    document_id: uuid.UUID
    document_code: str
    document_name: str
    document_type: Optional[str] = None
    template_id: Optional[uuid.UUID] = None
    content: Optional[str] = None
    file_url: Optional[str] = None
    version: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesDowntimeEventsCreate(BaseModel):
    downtime_id: uuid.UUID
    equipment_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    operation_exec_id: Optional[uuid.UUID] = None
    downtime_category: Optional[str] = None
    downtime_reason_id: Optional[uuid.UUID] = None
    start_time: datetime
    end_time: Optional[datetime] = None
    duration_minutes: Optional[float] = None
    affected_qty: Optional[float] = None
    responsible: Optional[str] = None
    description: Optional[str] = None
    corrective_action: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesDowntimeEventsUpdate(BaseModel):
    downtime_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    operation_exec_id: Optional[uuid.UUID] = None
    downtime_category: Optional[str] = None
    downtime_reason_id: Optional[uuid.UUID] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration_minutes: Optional[float] = None
    affected_qty: Optional[float] = None
    responsible: Optional[str] = None
    description: Optional[str] = None
    corrective_action: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesDowntimeEventsOut(BaseModel):
    downtime_id: uuid.UUID
    equipment_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    operation_exec_id: Optional[uuid.UUID] = None
    downtime_category: Optional[str] = None
    downtime_reason_id: Optional[uuid.UUID] = None
    start_time: datetime
    end_time: Optional[datetime] = None
    duration_minutes: Optional[float] = None
    affected_qty: Optional[float] = None
    responsible: Optional[str] = None
    description: Optional[str] = None
    corrective_action: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MesDowntimeReasonsCreate(BaseModel):
    reason_id: uuid.UUID
    category: str
    reason_code: str
    reason_name: str
    sub_reason: Optional[str] = None
    is_planned: Optional[bool] = None
    requires_action: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1

class MesDowntimeReasonsUpdate(BaseModel):
    reason_id: Optional[uuid.UUID] = None
    category: Optional[str] = None
    reason_code: Optional[str] = None
    reason_name: Optional[str] = None
    sub_reason: Optional[str] = None
    is_planned: Optional[bool] = None
    requires_action: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesDowntimeReasonsOut(BaseModel):
    reason_id: uuid.UUID
    category: str
    reason_code: str
    reason_name: str
    sub_reason: Optional[str] = None
    is_planned: Optional[bool] = None
    requires_action: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesEnergyMetersCreate(BaseModel):
    meter_id: uuid.UUID
    meter_code: str
    meter_name: Optional[str] = None
    meter_type: Optional[str] = None
    equipment_id: Optional[uuid.UUID] = None
    location: Optional[str] = None
    uom: Optional[str] = None
    conversion_factor: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class MesEnergyMetersUpdate(BaseModel):
    meter_id: Optional[uuid.UUID] = None
    meter_code: Optional[str] = None
    meter_name: Optional[str] = None
    meter_type: Optional[str] = None
    equipment_id: Optional[uuid.UUID] = None
    location: Optional[str] = None
    uom: Optional[str] = None
    conversion_factor: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesEnergyMetersOut(BaseModel):
    meter_id: uuid.UUID
    meter_code: str
    meter_name: Optional[str] = None
    meter_type: Optional[str] = None
    equipment_id: Optional[uuid.UUID] = None
    location: Optional[str] = None
    uom: Optional[str] = None
    conversion_factor: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesEnergyReadingsCreate(BaseModel):
    reading_id: uuid.UUID
    meter_id: uuid.UUID
    reading_value: float
    reading_time: datetime
    cost_per_unit: Optional[float] = None
    total_cost: Optional[float] = None
    carbon_footprint_kg: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class MesEnergyReadingsUpdate(BaseModel):
    reading_id: Optional[uuid.UUID] = None
    meter_id: Optional[uuid.UUID] = None
    reading_value: Optional[float] = None
    reading_time: Optional[datetime] = None
    cost_per_unit: Optional[float] = None
    total_cost: Optional[float] = None
    carbon_footprint_kg: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesEnergyReadingsOut(BaseModel):
    reading_id: uuid.UUID
    meter_id: uuid.UUID
    reading_value: float
    reading_time: datetime
    cost_per_unit: Optional[float] = None
    total_cost: Optional[float] = None
    carbon_footprint_kg: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesEquipmentCreate(BaseModel):
    equipment_id: uuid.UUID
    equipment_code: str
    equipment_name: str
    equipment_type_id: Optional[uuid.UUID] = None
    equipment_class_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    status_id: Optional[uuid.UUID] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    install_date: Optional[date] = None
    warranty_expiry: Optional[date] = None
    capacity_rate: Optional[float] = None
    capacity_uom: Optional[str] = None
    power_rating: Optional[float] = None
    power_uom: Optional[str] = None
    description: Optional[str] = None
    asset_number: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesEquipmentUpdate(BaseModel):
    equipment_id: Optional[uuid.UUID] = None
    equipment_code: Optional[str] = None
    equipment_name: Optional[str] = None
    equipment_type_id: Optional[uuid.UUID] = None
    equipment_class_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    status_id: Optional[uuid.UUID] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    install_date: Optional[date] = None
    warranty_expiry: Optional[date] = None
    capacity_rate: Optional[float] = None
    capacity_uom: Optional[str] = None
    power_rating: Optional[float] = None
    power_uom: Optional[str] = None
    description: Optional[str] = None
    asset_number: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesEquipmentOut(BaseModel):
    equipment_id: uuid.UUID
    equipment_code: str
    equipment_name: str
    equipment_type_id: Optional[uuid.UUID] = None
    equipment_class_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    status_id: Optional[uuid.UUID] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    install_date: Optional[date] = None
    warranty_expiry: Optional[date] = None
    capacity_rate: Optional[float] = None
    capacity_uom: Optional[str] = None
    power_rating: Optional[float] = None
    power_uom: Optional[str] = None
    description: Optional[str] = None
    asset_number: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesEquipmentAssignmentsCreate(BaseModel):
    assignment_id: uuid.UUID
    equipment_id: uuid.UUID
    work_center_id: Optional[uuid.UUID] = None
    production_line_id: Optional[uuid.UUID] = None
    assigned_from: Optional[datetime] = None
    assigned_until: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesEquipmentAssignmentsUpdate(BaseModel):
    assignment_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    production_line_id: Optional[uuid.UUID] = None
    assigned_from: Optional[datetime] = None
    assigned_until: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesEquipmentAssignmentsOut(BaseModel):
    assignment_id: uuid.UUID
    equipment_id: uuid.UUID
    work_center_id: Optional[uuid.UUID] = None
    production_line_id: Optional[uuid.UUID] = None
    assigned_from: Optional[datetime] = None
    assigned_until: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesEquipmentCapabilitiesCreate(BaseModel):
    capability_id: uuid.UUID
    equipment_id: uuid.UUID
    operation_type: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    uom: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesEquipmentCapabilitiesUpdate(BaseModel):
    capability_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    operation_type: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    uom: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesEquipmentCapabilitiesOut(BaseModel):
    capability_id: uuid.UUID
    equipment_id: uuid.UUID
    operation_type: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    uom: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesEquipmentCertificationsCreate(BaseModel):
    certification_id: uuid.UUID
    equipment_id: uuid.UUID
    cert_type: Optional[str] = None
    cert_number: Optional[str] = None
    issue_date: Optional[date] = None
    expiry_date: Optional[date] = None
    cert_body: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesEquipmentCertificationsUpdate(BaseModel):
    certification_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    cert_type: Optional[str] = None
    cert_number: Optional[str] = None
    issue_date: Optional[date] = None
    expiry_date: Optional[date] = None
    cert_body: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesEquipmentCertificationsOut(BaseModel):
    certification_id: uuid.UUID
    equipment_id: uuid.UUID
    cert_type: Optional[str] = None
    cert_number: Optional[str] = None
    issue_date: Optional[date] = None
    expiry_date: Optional[date] = None
    cert_body: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesEquipmentClassesCreate(BaseModel):
    equipment_class_id: uuid.UUID
    class_code: str
    class_name: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesEquipmentClassesUpdate(BaseModel):
    equipment_class_id: Optional[uuid.UUID] = None
    class_code: Optional[str] = None
    class_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesEquipmentClassesOut(BaseModel):
    equipment_class_id: uuid.UUID
    class_code: str
    class_name: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesEquipmentConnectionsCreate(BaseModel):
    connection_id: uuid.UUID
    equipment_id: uuid.UUID
    protocol: Optional[str] = None
    endpoint: Optional[str] = None
    port: Optional[int] = None
    topic: Optional[str] = None
    config: Optional[dict] = None
    is_active: bool = True
    object_version_number: int = 1

class MesEquipmentConnectionsUpdate(BaseModel):
    connection_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    protocol: Optional[str] = None
    endpoint: Optional[str] = None
    port: Optional[int] = None
    topic: Optional[str] = None
    config: Optional[dict] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesEquipmentConnectionsOut(BaseModel):
    connection_id: uuid.UUID
    equipment_id: uuid.UUID
    protocol: Optional[str] = None
    endpoint: Optional[str] = None
    port: Optional[int] = None
    topic: Optional[str] = None
    config: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesEquipmentDataPointsCreate(BaseModel):
    point_id: uuid.UUID
    equipment_id: uuid.UUID
    point_code: str
    point_name: Optional[str] = None
    data_type: Optional[str] = None
    uom: Optional[str] = None
    sampling_rate: Optional[int] = None
    scaling_factor: Optional[float] = None
    offset_value: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class MesEquipmentDataPointsUpdate(BaseModel):
    point_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    point_code: Optional[str] = None
    point_name: Optional[str] = None
    data_type: Optional[str] = None
    uom: Optional[str] = None
    sampling_rate: Optional[int] = None
    scaling_factor: Optional[float] = None
    offset_value: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesEquipmentDataPointsOut(BaseModel):
    point_id: uuid.UUID
    equipment_id: uuid.UUID
    point_code: str
    point_name: Optional[str] = None
    data_type: Optional[str] = None
    uom: Optional[str] = None
    sampling_rate: Optional[int] = None
    scaling_factor: Optional[float] = None
    offset_value: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesEquipmentLocationsCreate(BaseModel):
    location_id: uuid.UUID
    location_code: str
    location_name: str
    area: Optional[str] = None
    line: Optional[str] = None
    cell: Optional[str] = None
    station: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesEquipmentLocationsUpdate(BaseModel):
    location_id: Optional[uuid.UUID] = None
    location_code: Optional[str] = None
    location_name: Optional[str] = None
    area: Optional[str] = None
    line: Optional[str] = None
    cell: Optional[str] = None
    station: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesEquipmentLocationsOut(BaseModel):
    location_id: uuid.UUID
    location_code: str
    location_name: str
    area: Optional[str] = None
    line: Optional[str] = None
    cell: Optional[str] = None
    station: Optional[str] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesEquipmentStatusesCreate(BaseModel):
    status_id: uuid.UUID
    status_code: str
    status_name: str
    is_running: Optional[bool] = None
    is_idle: Optional[bool] = None
    is_down: Optional[bool] = None
    color: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesEquipmentStatusesUpdate(BaseModel):
    status_id: Optional[uuid.UUID] = None
    status_code: Optional[str] = None
    status_name: Optional[str] = None
    is_running: Optional[bool] = None
    is_idle: Optional[bool] = None
    is_down: Optional[bool] = None
    color: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesEquipmentStatusesOut(BaseModel):
    status_id: uuid.UUID
    status_code: str
    status_name: str
    is_running: Optional[bool] = None
    is_idle: Optional[bool] = None
    is_down: Optional[bool] = None
    color: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesEquipmentTypesCreate(BaseModel):
    equipment_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesEquipmentTypesUpdate(BaseModel):
    equipment_type_id: Optional[uuid.UUID] = None
    type_code: Optional[str] = None
    type_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesEquipmentTypesOut(BaseModel):
    equipment_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesGenealogyCreate(BaseModel):
    genealogy_id: uuid.UUID
    parent_type: Optional[str] = None
    parent_id: Optional[uuid.UUID] = None
    parent_lot: Optional[str] = None
    parent_serial: Optional[str] = None
    child_type: Optional[str] = None
    child_id: Optional[uuid.UUID] = None
    child_lot: Optional[str] = None
    child_serial: Optional[str] = None
    qty: Optional[float] = None
    uom: Optional[str] = None
    operation_exec_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    genealogy_date: Optional[datetime] = None
    direction: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesGenealogyUpdate(BaseModel):
    genealogy_id: Optional[uuid.UUID] = None
    parent_type: Optional[str] = None
    parent_id: Optional[uuid.UUID] = None
    parent_lot: Optional[str] = None
    parent_serial: Optional[str] = None
    child_type: Optional[str] = None
    child_id: Optional[uuid.UUID] = None
    child_lot: Optional[str] = None
    child_serial: Optional[str] = None
    qty: Optional[float] = None
    uom: Optional[str] = None
    operation_exec_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    genealogy_date: Optional[datetime] = None
    direction: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesGenealogyOut(BaseModel):
    genealogy_id: uuid.UUID
    parent_type: Optional[str] = None
    parent_id: Optional[uuid.UUID] = None
    parent_lot: Optional[str] = None
    parent_serial: Optional[str] = None
    child_type: Optional[str] = None
    child_id: Optional[uuid.UUID] = None
    child_lot: Optional[str] = None
    child_serial: Optional[str] = None
    qty: Optional[float] = None
    uom: Optional[str] = None
    operation_exec_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    genealogy_date: Optional[datetime] = None
    direction: Optional[str] = None
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

class MesGenealogySnapshotsCreate(BaseModel):
    snapshot_id: uuid.UUID
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    snapshot_data: Optional[dict] = None
    snapshot_at: Optional[datetime] = None
    reason: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesGenealogySnapshotsUpdate(BaseModel):
    snapshot_id: Optional[uuid.UUID] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    snapshot_data: Optional[dict] = None
    snapshot_at: Optional[datetime] = None
    reason: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesGenealogySnapshotsOut(BaseModel):
    snapshot_id: uuid.UUID
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    snapshot_data: Optional[dict] = None
    snapshot_at: Optional[datetime] = None
    reason: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesInstructionAcknowledgmentsCreate(BaseModel):
    ack_id: uuid.UUID
    instruction_id: uuid.UUID
    operator_id: uuid.UUID
    acknowledged_at: Optional[datetime] = None
    understood: Optional[bool] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesInstructionAcknowledgmentsUpdate(BaseModel):
    ack_id: Optional[uuid.UUID] = None
    instruction_id: Optional[uuid.UUID] = None
    operator_id: Optional[uuid.UUID] = None
    acknowledged_at: Optional[datetime] = None
    understood: Optional[bool] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesInstructionAcknowledgmentsOut(BaseModel):
    ack_id: uuid.UUID
    instruction_id: uuid.UUID
    operator_id: uuid.UUID
    acknowledged_at: Optional[datetime] = None
    understood: Optional[bool] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesInstructionVersionsCreate(BaseModel):
    version_id: uuid.UUID
    instruction_id: uuid.UUID
    version_number: int
    content: Optional[str] = None
    change_notes: Optional[str] = None
    effective_date: Optional[date] = None
    reviewed_by: Optional[uuid.UUID] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesInstructionVersionsUpdate(BaseModel):
    version_id: Optional[uuid.UUID] = None
    instruction_id: Optional[uuid.UUID] = None
    version_number: Optional[int] = None
    content: Optional[str] = None
    change_notes: Optional[str] = None
    effective_date: Optional[date] = None
    reviewed_by: Optional[uuid.UUID] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesInstructionVersionsOut(BaseModel):
    version_id: uuid.UUID
    instruction_id: uuid.UUID
    version_number: int
    content: Optional[str] = None
    change_notes: Optional[str] = None
    effective_date: Optional[date] = None
    reviewed_by: Optional[uuid.UUID] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesInstructionsCreate(BaseModel):
    instruction_id: uuid.UUID
    instruction_code: str
    instruction_name: str
    instruction_type: Optional[str] = None
    current_version: Optional[int] = None
    content: Optional[str] = None
    duration_seconds: Optional[int] = None
    safety_warnings: Optional[str] = None
    quality_checks: Optional[str] = None
    department: Optional[str] = None
    category: Optional[str] = None
    is_controlled: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1

class MesInstructionsUpdate(BaseModel):
    instruction_id: Optional[uuid.UUID] = None
    instruction_code: Optional[str] = None
    instruction_name: Optional[str] = None
    instruction_type: Optional[str] = None
    current_version: Optional[int] = None
    content: Optional[str] = None
    duration_seconds: Optional[int] = None
    safety_warnings: Optional[str] = None
    quality_checks: Optional[str] = None
    department: Optional[str] = None
    category: Optional[str] = None
    is_controlled: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesInstructionsOut(BaseModel):
    instruction_id: uuid.UUID
    instruction_code: str
    instruction_name: str
    instruction_type: Optional[str] = None
    current_version: Optional[int] = None
    content: Optional[str] = None
    duration_seconds: Optional[int] = None
    safety_warnings: Optional[str] = None
    quality_checks: Optional[str] = None
    department: Optional[str] = None
    category: Optional[str] = None
    is_controlled: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesIntegrationConnectionsCreate(BaseModel):
    connection_id: uuid.UUID
    connection_code: str
    connection_name: Optional[str] = None
    integration_type: Optional[str] = None
    endpoint_url: Optional[str] = None
    auth_type: Optional[str] = None
    auth_credentials: Optional[str] = None
    config_json: Optional[dict] = None
    schedule: Optional[str] = None
    is_active: bool = True
    last_sync: Optional[datetime] = None
    status: Optional[str] = None
    object_version_number: int = 1

class MesIntegrationConnectionsUpdate(BaseModel):
    connection_id: Optional[uuid.UUID] = None
    connection_code: Optional[str] = None
    connection_name: Optional[str] = None
    integration_type: Optional[str] = None
    endpoint_url: Optional[str] = None
    auth_type: Optional[str] = None
    auth_credentials: Optional[str] = None
    config_json: Optional[dict] = None
    schedule: Optional[str] = None
    is_active: Optional[bool] = None
    last_sync: Optional[datetime] = None
    status: Optional[str] = None
    object_version_number: Optional[int] = None

class MesIntegrationConnectionsOut(BaseModel):
    connection_id: uuid.UUID
    connection_code: str
    connection_name: Optional[str] = None
    integration_type: Optional[str] = None
    endpoint_url: Optional[str] = None
    auth_type: Optional[str] = None
    auth_credentials: Optional[str] = None
    config_json: Optional[dict] = None
    schedule: Optional[str] = None
    is_active: bool
    last_sync: Optional[datetime] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesIntegrationLogsCreate(BaseModel):
    log_id: uuid.UUID
    connection_id: uuid.UUID
    direction: Optional[str] = None
    status: Optional[str] = None
    request_data: Optional[dict] = None
    response_data: Optional[dict] = None
    error_message: Optional[str] = None
    duration_ms: Optional[int] = None
    logged_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesIntegrationLogsUpdate(BaseModel):
    log_id: Optional[uuid.UUID] = None
    connection_id: Optional[uuid.UUID] = None
    direction: Optional[str] = None
    status: Optional[str] = None
    request_data: Optional[dict] = None
    response_data: Optional[dict] = None
    error_message: Optional[str] = None
    duration_ms: Optional[int] = None
    logged_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesIntegrationLogsOut(BaseModel):
    log_id: uuid.UUID
    connection_id: uuid.UUID
    direction: Optional[str] = None
    status: Optional[str] = None
    request_data: Optional[dict] = None
    response_data: Optional[dict] = None
    error_message: Optional[str] = None
    duration_ms: Optional[int] = None
    logged_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesKpiActualsCreate(BaseModel):
    actual_id: uuid.UUID
    kpi_id: uuid.UUID
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    actual_value: float
    target_value: Optional[float] = None
    variance: Optional[float] = None
    period_start: Optional[date] = None
    period_end: Optional[date] = None
    recorded_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesKpiActualsUpdate(BaseModel):
    actual_id: Optional[uuid.UUID] = None
    kpi_id: Optional[uuid.UUID] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    actual_value: Optional[float] = None
    target_value: Optional[float] = None
    variance: Optional[float] = None
    period_start: Optional[date] = None
    period_end: Optional[date] = None
    recorded_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesKpiActualsOut(BaseModel):
    actual_id: uuid.UUID
    kpi_id: uuid.UUID
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    actual_value: float
    target_value: Optional[float] = None
    variance: Optional[float] = None
    period_start: Optional[date] = None
    period_end: Optional[date] = None
    recorded_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesKpiDefinitionsCreate(BaseModel):
    kpi_id: uuid.UUID
    kpi_code: str
    kpi_name: str
    kpi_category: Optional[str] = None
    formula: Optional[str] = None
    uom: Optional[str] = None
    higher_is_better: Optional[bool] = None
    target_value: Optional[float] = None
    warning_threshold: Optional[float] = None
    critical_threshold: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class MesKpiDefinitionsUpdate(BaseModel):
    kpi_id: Optional[uuid.UUID] = None
    kpi_code: Optional[str] = None
    kpi_name: Optional[str] = None
    kpi_category: Optional[str] = None
    formula: Optional[str] = None
    uom: Optional[str] = None
    higher_is_better: Optional[bool] = None
    target_value: Optional[float] = None
    warning_threshold: Optional[float] = None
    critical_threshold: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesKpiDefinitionsOut(BaseModel):
    kpi_id: uuid.UUID
    kpi_code: str
    kpi_name: str
    kpi_category: Optional[str] = None
    formula: Optional[str] = None
    uom: Optional[str] = None
    higher_is_better: Optional[bool] = None
    target_value: Optional[float] = None
    warning_threshold: Optional[float] = None
    critical_threshold: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesLaborAssignmentsCreate(BaseModel):
    labor_assignment_id: uuid.UUID
    operator_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    operation_exec_id: Optional[uuid.UUID] = None
    labor_type: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration_minutes: Optional[float] = None
    skill_applied: Optional[str] = None
    cert_used: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesLaborAssignmentsUpdate(BaseModel):
    labor_assignment_id: Optional[uuid.UUID] = None
    operator_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    operation_exec_id: Optional[uuid.UUID] = None
    labor_type: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration_minutes: Optional[float] = None
    skill_applied: Optional[str] = None
    cert_used: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesLaborAssignmentsOut(BaseModel):
    labor_assignment_id: uuid.UUID
    operator_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    operation_exec_id: Optional[uuid.UUID] = None
    labor_type: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration_minutes: Optional[float] = None
    skill_applied: Optional[str] = None
    cert_used: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MesLaborTimeCollectionCreate(BaseModel):
    time_id: uuid.UUID
    operator_id: uuid.UUID
    clock_in: datetime
    clock_out: Optional[datetime] = None
    duration_minutes: Optional[float] = None
    work_center_id: Optional[uuid.UUID] = None
    shift_id: Optional[uuid.UUID] = None
    is_overtime: Optional[bool] = None
    is_break: Optional[bool] = None
    absence_type: Optional[str] = None
    recorded_by: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesLaborTimeCollectionUpdate(BaseModel):
    time_id: Optional[uuid.UUID] = None
    operator_id: Optional[uuid.UUID] = None
    clock_in: Optional[datetime] = None
    clock_out: Optional[datetime] = None
    duration_minutes: Optional[float] = None
    work_center_id: Optional[uuid.UUID] = None
    shift_id: Optional[uuid.UUID] = None
    is_overtime: Optional[bool] = None
    is_break: Optional[bool] = None
    absence_type: Optional[str] = None
    recorded_by: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesLaborTimeCollectionOut(BaseModel):
    time_id: uuid.UUID
    operator_id: uuid.UUID
    clock_in: datetime
    clock_out: Optional[datetime] = None
    duration_minutes: Optional[float] = None
    work_center_id: Optional[uuid.UUID] = None
    shift_id: Optional[uuid.UUID] = None
    is_overtime: Optional[bool] = None
    is_break: Optional[bool] = None
    absence_type: Optional[str] = None
    recorded_by: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MesLineBalancingCreate(BaseModel):
    balance_id: uuid.UUID
    production_line_id: uuid.UUID
    product_id: Optional[uuid.UUID] = None
    takt_time_seconds: Optional[float] = None
    cycle_time_seconds: Optional[float] = None
    station_count: Optional[int] = None
    balance_efficiency: Optional[float] = None
    as_of_date: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1

class MesLineBalancingUpdate(BaseModel):
    balance_id: Optional[uuid.UUID] = None
    production_line_id: Optional[uuid.UUID] = None
    product_id: Optional[uuid.UUID] = None
    takt_time_seconds: Optional[float] = None
    cycle_time_seconds: Optional[float] = None
    station_count: Optional[int] = None
    balance_efficiency: Optional[float] = None
    as_of_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesLineBalancingOut(BaseModel):
    balance_id: uuid.UUID
    production_line_id: uuid.UUID
    product_id: Optional[uuid.UUID] = None
    takt_time_seconds: Optional[float] = None
    cycle_time_seconds: Optional[float] = None
    station_count: Optional[int] = None
    balance_efficiency: Optional[float] = None
    as_of_date: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesLlmConfigsCreate(BaseModel):
    config_id: uuid.UUID
    config_name: Optional[str] = None
    provider: Optional[str] = None
    model_name: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    parameters: Optional[dict] = None
    is_default: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1

class MesLlmConfigsUpdate(BaseModel):
    config_id: Optional[uuid.UUID] = None
    config_name: Optional[str] = None
    provider: Optional[str] = None
    model_name: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    parameters: Optional[dict] = None
    is_default: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesLlmConfigsOut(BaseModel):
    config_id: uuid.UUID
    config_name: Optional[str] = None
    provider: Optional[str] = None
    model_name: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    parameters: Optional[dict] = None
    is_default: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesMachineAlarmsCreate(BaseModel):
    alarm_id: uuid.UUID
    equipment_id: uuid.UUID
    alarm_code: Optional[str] = None
    alarm_description: Optional[str] = None
    severity: Optional[str] = None
    alarm_start: datetime
    alarm_end: Optional[datetime] = None
    acknowledged: Optional[bool] = None
    acknowledged_by: Optional[uuid.UUID] = None
    acknowledged_at: Optional[datetime] = None
    cleared_by: Optional[uuid.UUID] = None
    cleared_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesMachineAlarmsUpdate(BaseModel):
    alarm_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    alarm_code: Optional[str] = None
    alarm_description: Optional[str] = None
    severity: Optional[str] = None
    alarm_start: Optional[datetime] = None
    alarm_end: Optional[datetime] = None
    acknowledged: Optional[bool] = None
    acknowledged_by: Optional[uuid.UUID] = None
    acknowledged_at: Optional[datetime] = None
    cleared_by: Optional[uuid.UUID] = None
    cleared_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesMachineAlarmsOut(BaseModel):
    alarm_id: uuid.UUID
    equipment_id: uuid.UUID
    alarm_code: Optional[str] = None
    alarm_description: Optional[str] = None
    severity: Optional[str] = None
    alarm_start: datetime
    alarm_end: Optional[datetime] = None
    acknowledged: Optional[bool] = None
    acknowledged_by: Optional[uuid.UUID] = None
    acknowledged_at: Optional[datetime] = None
    cleared_by: Optional[uuid.UUID] = None
    cleared_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MesMachineDataValuesCreate(BaseModel):
    value_id: uuid.UUID
    point_id: uuid.UUID
    equipment_id: uuid.UUID
    value_numeric: Optional[float] = None
    value_text: Optional[str] = None
    quality_flag: Optional[str] = None
    recorded_at: datetime
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesMachineDataValuesUpdate(BaseModel):
    value_id: Optional[uuid.UUID] = None
    point_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    value_numeric: Optional[float] = None
    value_text: Optional[str] = None
    quality_flag: Optional[str] = None
    recorded_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesMachineDataValuesOut(BaseModel):
    value_id: uuid.UUID
    point_id: uuid.UUID
    equipment_id: uuid.UUID
    value_numeric: Optional[float] = None
    value_text: Optional[str] = None
    quality_flag: Optional[str] = None
    recorded_at: datetime
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MesMachineEventsCreate(BaseModel):
    event_id: uuid.UUID
    equipment_id: uuid.UUID
    event_type: str
    event_code: Optional[str] = None
    event_description: Optional[str] = None
    severity: Optional[str] = None
    event_time: datetime
    acknowledged: Optional[bool] = None
    acknowledged_by: Optional[uuid.UUID] = None
    acknowledged_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesMachineEventsUpdate(BaseModel):
    event_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    event_type: Optional[str] = None
    event_code: Optional[str] = None
    event_description: Optional[str] = None
    severity: Optional[str] = None
    event_time: Optional[datetime] = None
    acknowledged: Optional[bool] = None
    acknowledged_by: Optional[uuid.UUID] = None
    acknowledged_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesMachineEventsOut(BaseModel):
    event_id: uuid.UUID
    equipment_id: uuid.UUID
    event_type: str
    event_code: Optional[str] = None
    event_description: Optional[str] = None
    severity: Optional[str] = None
    event_time: datetime
    acknowledged: Optional[bool] = None
    acknowledged_by: Optional[uuid.UUID] = None
    acknowledged_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MesMachineProgramsCreate(BaseModel):
    program_id: uuid.UUID
    equipment_id: uuid.UUID
    program_code: Optional[str] = None
    program_name: Optional[str] = None
    program_version: Optional[str] = None
    program_data: Optional[str] = None
    loaded_at: Optional[datetime] = None
    loaded_by: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1

class MesMachineProgramsUpdate(BaseModel):
    program_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    program_code: Optional[str] = None
    program_name: Optional[str] = None
    program_version: Optional[str] = None
    program_data: Optional[str] = None
    loaded_at: Optional[datetime] = None
    loaded_by: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesMachineProgramsOut(BaseModel):
    program_id: uuid.UUID
    equipment_id: uuid.UUID
    program_code: Optional[str] = None
    program_name: Optional[str] = None
    program_version: Optional[str] = None
    program_data: Optional[str] = None
    loaded_at: Optional[datetime] = None
    loaded_by: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesMaintenanceHistoryCreate(BaseModel):
    history_id: uuid.UUID
    mwo_id: uuid.UUID
    equipment_id: uuid.UUID
    maintenance_date: Optional[date] = None
    description: Optional[str] = None
    parts_used: Optional[str] = None
    findings: Optional[str] = None
    recommendations: Optional[str] = None
    downtime_minutes: Optional[int] = None
    cost_total: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class MesMaintenanceHistoryUpdate(BaseModel):
    history_id: Optional[uuid.UUID] = None
    mwo_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    maintenance_date: Optional[date] = None
    description: Optional[str] = None
    parts_used: Optional[str] = None
    findings: Optional[str] = None
    recommendations: Optional[str] = None
    downtime_minutes: Optional[int] = None
    cost_total: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesMaintenanceHistoryOut(BaseModel):
    history_id: uuid.UUID
    mwo_id: uuid.UUID
    equipment_id: uuid.UUID
    maintenance_date: Optional[date] = None
    description: Optional[str] = None
    parts_used: Optional[str] = None
    findings: Optional[str] = None
    recommendations: Optional[str] = None
    downtime_minutes: Optional[int] = None
    cost_total: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesMaintenancePartsCreate(BaseModel):
    part_id: uuid.UUID
    mwo_id: uuid.UUID
    item_code: Optional[str] = None
    item_name: Optional[str] = None
    qty_used: Optional[float] = None
    uom: Optional[str] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class MesMaintenancePartsUpdate(BaseModel):
    part_id: Optional[uuid.UUID] = None
    mwo_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    item_name: Optional[str] = None
    qty_used: Optional[float] = None
    uom: Optional[str] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesMaintenancePartsOut(BaseModel):
    part_id: uuid.UUID
    mwo_id: uuid.UUID
    item_code: Optional[str] = None
    item_name: Optional[str] = None
    qty_used: Optional[float] = None
    uom: Optional[str] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesMaintenanceSchedulesCreate(BaseModel):
    schedule_id: uuid.UUID
    equipment_id: uuid.UUID
    maintenance_type: Optional[str] = None
    frequency_value: Optional[int] = None
    frequency_uom: Optional[str] = None
    last_performed: Optional[date] = None
    next_due: Optional[date] = None
    estimated_duration_min: Optional[int] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesMaintenanceSchedulesUpdate(BaseModel):
    schedule_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    maintenance_type: Optional[str] = None
    frequency_value: Optional[int] = None
    frequency_uom: Optional[str] = None
    last_performed: Optional[date] = None
    next_due: Optional[date] = None
    estimated_duration_min: Optional[int] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesMaintenanceSchedulesOut(BaseModel):
    schedule_id: uuid.UUID
    equipment_id: uuid.UUID
    maintenance_type: Optional[str] = None
    frequency_value: Optional[int] = None
    frequency_uom: Optional[str] = None
    last_performed: Optional[date] = None
    next_due: Optional[date] = None
    estimated_duration_min: Optional[int] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesMaintenanceWorkOrdersCreate(BaseModel):
    mwo_id: uuid.UUID
    equipment_id: uuid.UUID
    schedule_id: Optional[uuid.UUID] = None
    maintenance_type: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    requested_date: Optional[date] = None
    scheduled_date: Optional[date] = None
    completed_date: Optional[date] = None
    downtime_minutes: Optional[int] = None
    cost_estimated: Optional[float] = None
    cost_actual: Optional[float] = None
    technician_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1

class MesMaintenanceWorkOrdersUpdate(BaseModel):
    mwo_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    schedule_id: Optional[uuid.UUID] = None
    maintenance_type: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    requested_date: Optional[date] = None
    scheduled_date: Optional[date] = None
    completed_date: Optional[date] = None
    downtime_minutes: Optional[int] = None
    cost_estimated: Optional[float] = None
    cost_actual: Optional[float] = None
    technician_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesMaintenanceWorkOrdersOut(BaseModel):
    mwo_id: uuid.UUID
    equipment_id: uuid.UUID
    schedule_id: Optional[uuid.UUID] = None
    maintenance_type: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    requested_date: Optional[date] = None
    scheduled_date: Optional[date] = None
    completed_date: Optional[date] = None
    downtime_minutes: Optional[int] = None
    cost_estimated: Optional[float] = None
    cost_actual: Optional[float] = None
    technician_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesMaterialConsumptionCreate(BaseModel):
    consumption_id: uuid.UUID
    execution_id: uuid.UUID
    operation_exec_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    item_name: Optional[str] = None
    planned_qty: Optional[float] = None
    actual_qty: float
    variance_qty: Optional[float] = None
    uom: Optional[str] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    supplier_lot: Optional[str] = None
    expiry_date: Optional[date] = None
    consumption_type: Optional[str] = None
    consumed_at: Optional[datetime] = None
    consumed_by: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesMaterialConsumptionUpdate(BaseModel):
    consumption_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    operation_exec_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    item_name: Optional[str] = None
    planned_qty: Optional[float] = None
    actual_qty: Optional[float] = None
    variance_qty: Optional[float] = None
    uom: Optional[str] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    supplier_lot: Optional[str] = None
    expiry_date: Optional[date] = None
    consumption_type: Optional[str] = None
    consumed_at: Optional[datetime] = None
    consumed_by: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesMaterialConsumptionOut(BaseModel):
    consumption_id: uuid.UUID
    execution_id: uuid.UUID
    operation_exec_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    item_name: Optional[str] = None
    planned_qty: Optional[float] = None
    actual_qty: float
    variance_qty: Optional[float] = None
    uom: Optional[str] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    supplier_lot: Optional[str] = None
    expiry_date: Optional[date] = None
    consumption_type: Optional[str] = None
    consumed_at: Optional[datetime] = None
    consumed_by: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MesMaterialIssuesCreate(BaseModel):
    issue_id: uuid.UUID
    execution_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    qty_issued: float
    uom: Optional[str] = None
    from_location: Optional[str] = None
    to_location: Optional[str] = None
    lot_number: Optional[str] = None
    issued_at: Optional[datetime] = None
    issued_by: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesMaterialIssuesUpdate(BaseModel):
    issue_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    qty_issued: Optional[float] = None
    uom: Optional[str] = None
    from_location: Optional[str] = None
    to_location: Optional[str] = None
    lot_number: Optional[str] = None
    issued_at: Optional[datetime] = None
    issued_by: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesMaterialIssuesOut(BaseModel):
    issue_id: uuid.UUID
    execution_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    qty_issued: float
    uom: Optional[str] = None
    from_location: Optional[str] = None
    to_location: Optional[str] = None
    lot_number: Optional[str] = None
    issued_at: Optional[datetime] = None
    issued_by: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MesMaterialReturnsCreate(BaseModel):
    return_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    qty_returned: float
    uom: Optional[str] = None
    return_reason: Optional[str] = None
    lot_number: Optional[str] = None
    returned_at: Optional[datetime] = None
    returned_by: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesMaterialReturnsUpdate(BaseModel):
    return_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    qty_returned: Optional[float] = None
    uom: Optional[str] = None
    return_reason: Optional[str] = None
    lot_number: Optional[str] = None
    returned_at: Optional[datetime] = None
    returned_by: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesMaterialReturnsOut(BaseModel):
    return_id: uuid.UUID
    execution_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    qty_returned: float
    uom: Optional[str] = None
    return_reason: Optional[str] = None
    lot_number: Optional[str] = None
    returned_at: Optional[datetime] = None
    returned_by: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MesMlModelVersionsCreate(BaseModel):
    version_id: uuid.UUID
    model_id: uuid.UUID
    version_number: int
    model_artifact: Optional[str] = None
    training_data_info: Optional[str] = None
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    trained_by: Optional[uuid.UUID] = None
    trained_at: Optional[datetime] = None
    is_production: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1

class MesMlModelVersionsUpdate(BaseModel):
    version_id: Optional[uuid.UUID] = None
    model_id: Optional[uuid.UUID] = None
    version_number: Optional[int] = None
    model_artifact: Optional[str] = None
    training_data_info: Optional[str] = None
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    trained_by: Optional[uuid.UUID] = None
    trained_at: Optional[datetime] = None
    is_production: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesMlModelVersionsOut(BaseModel):
    version_id: uuid.UUID
    model_id: uuid.UUID
    version_number: int
    model_artifact: Optional[str] = None
    training_data_info: Optional[str] = None
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    trained_by: Optional[uuid.UUID] = None
    trained_at: Optional[datetime] = None
    is_production: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesMlModelsCreate(BaseModel):
    model_id: uuid.UUID
    model_type: Optional[str] = None
    model_name: str
    framework: Optional[str] = None
    description: Optional[str] = None
    training_params: Optional[dict] = None
    training_metrics: Optional[dict] = None
    validation_metrics: Optional[dict] = None
    feature_importance: Optional[dict] = None
    deployment_status: Optional[str] = None
    endpoint_url: Optional[str] = None
    monitoring_metrics: Optional[dict] = None
    retraining_schedule: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesMlModelsUpdate(BaseModel):
    model_id: Optional[uuid.UUID] = None
    model_type: Optional[str] = None
    model_name: Optional[str] = None
    framework: Optional[str] = None
    description: Optional[str] = None
    training_params: Optional[dict] = None
    training_metrics: Optional[dict] = None
    validation_metrics: Optional[dict] = None
    feature_importance: Optional[dict] = None
    deployment_status: Optional[str] = None
    endpoint_url: Optional[str] = None
    monitoring_metrics: Optional[dict] = None
    retraining_schedule: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesMlModelsOut(BaseModel):
    model_id: uuid.UUID
    model_type: Optional[str] = None
    model_name: str
    framework: Optional[str] = None
    description: Optional[str] = None
    training_params: Optional[dict] = None
    training_metrics: Optional[dict] = None
    validation_metrics: Optional[dict] = None
    feature_importance: Optional[dict] = None
    deployment_status: Optional[str] = None
    endpoint_url: Optional[str] = None
    monitoring_metrics: Optional[dict] = None
    retraining_schedule: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesNotificationsCreate(BaseModel):
    notification_id: uuid.UUID
    notification_type: Optional[str] = None
    recipient_id: Optional[uuid.UUID] = None
    recipient_email: Optional[str] = None
    recipient_phone: Optional[str] = None
    subject: Optional[str] = None
    message: Optional[str] = None
    channel: Optional[str] = None
    status: Optional[str] = None
    sent_at: Optional[datetime] = None
    delivered_at: Optional[datetime] = None
    read_at: Optional[datetime] = None
    error_message: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesNotificationsUpdate(BaseModel):
    notification_id: Optional[uuid.UUID] = None
    notification_type: Optional[str] = None
    recipient_id: Optional[uuid.UUID] = None
    recipient_email: Optional[str] = None
    recipient_phone: Optional[str] = None
    subject: Optional[str] = None
    message: Optional[str] = None
    channel: Optional[str] = None
    status: Optional[str] = None
    sent_at: Optional[datetime] = None
    delivered_at: Optional[datetime] = None
    read_at: Optional[datetime] = None
    error_message: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesNotificationsOut(BaseModel):
    notification_id: uuid.UUID
    notification_type: Optional[str] = None
    recipient_id: Optional[uuid.UUID] = None
    recipient_email: Optional[str] = None
    recipient_phone: Optional[str] = None
    subject: Optional[str] = None
    message: Optional[str] = None
    channel: Optional[str] = None
    status: Optional[str] = None
    sent_at: Optional[datetime] = None
    delivered_at: Optional[datetime] = None
    read_at: Optional[datetime] = None
    error_message: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesOeeCalculationsCreate(BaseModel):
    oee_id: uuid.UUID
    equipment_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    production_line_id: Optional[uuid.UUID] = None
    shift_id: Optional[uuid.UUID] = None
    calculation_date: date
    period_type: Optional[str] = None
    available_time_min: Optional[float] = None
    operating_time_min: Optional[float] = None
    downtime_min: Optional[float] = None
    ideal_cycle_time: Optional[float] = None
    total_parts: Optional[int] = None
    good_parts: Optional[int] = None
    defect_parts: Optional[int] = None
    availability_pct: Optional[float] = None
    performance_pct: Optional[float] = None
    quality_pct: Optional[float] = None
    oee_pct: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesOeeCalculationsUpdate(BaseModel):
    oee_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    production_line_id: Optional[uuid.UUID] = None
    shift_id: Optional[uuid.UUID] = None
    calculation_date: Optional[date] = None
    period_type: Optional[str] = None
    available_time_min: Optional[float] = None
    operating_time_min: Optional[float] = None
    downtime_min: Optional[float] = None
    ideal_cycle_time: Optional[float] = None
    total_parts: Optional[int] = None
    good_parts: Optional[int] = None
    defect_parts: Optional[int] = None
    availability_pct: Optional[float] = None
    performance_pct: Optional[float] = None
    quality_pct: Optional[float] = None
    oee_pct: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesOeeCalculationsOut(BaseModel):
    oee_id: uuid.UUID
    equipment_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    production_line_id: Optional[uuid.UUID] = None
    shift_id: Optional[uuid.UUID] = None
    calculation_date: date
    period_type: Optional[str] = None
    available_time_min: Optional[float] = None
    operating_time_min: Optional[float] = None
    downtime_min: Optional[float] = None
    ideal_cycle_time: Optional[float] = None
    total_parts: Optional[int] = None
    good_parts: Optional[int] = None
    defect_parts: Optional[int] = None
    availability_pct: Optional[float] = None
    performance_pct: Optional[float] = None
    quality_pct: Optional[float] = None
    oee_pct: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MesOeeLossesCreate(BaseModel):
    loss_id: uuid.UUID
    oee_id: uuid.UUID
    loss_category: Optional[str] = None
    loss_type: Optional[str] = None
    loss_minutes: Optional[float] = None
    loss_description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesOeeLossesUpdate(BaseModel):
    loss_id: Optional[uuid.UUID] = None
    oee_id: Optional[uuid.UUID] = None
    loss_category: Optional[str] = None
    loss_type: Optional[str] = None
    loss_minutes: Optional[float] = None
    loss_description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesOeeLossesOut(BaseModel):
    loss_id: uuid.UUID
    oee_id: uuid.UUID
    loss_category: Optional[str] = None
    loss_type: Optional[str] = None
    loss_minutes: Optional[float] = None
    loss_description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesOeeTargetsCreate(BaseModel):
    target_id: uuid.UUID
    equipment_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    oee_target: Optional[float] = None
    availability_target: Optional[float] = None
    performance_target: Optional[float] = None
    quality_target: Optional[float] = None
    effective_from: Optional[date] = None
    effective_until: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1

class MesOeeTargetsUpdate(BaseModel):
    target_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    oee_target: Optional[float] = None
    availability_target: Optional[float] = None
    performance_target: Optional[float] = None
    quality_target: Optional[float] = None
    effective_from: Optional[date] = None
    effective_until: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesOeeTargetsOut(BaseModel):
    target_id: uuid.UUID
    equipment_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    oee_target: Optional[float] = None
    availability_target: Optional[float] = None
    performance_target: Optional[float] = None
    quality_target: Optional[float] = None
    effective_from: Optional[date] = None
    effective_until: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesOperationExecutionCreate(BaseModel):
    operation_exec_id: uuid.UUID
    execution_id: uuid.UUID
    operation_sequence: int
    operation_code: Optional[str] = None
    operation_name: Optional[str] = None
    work_center_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    planned_qty: Optional[float] = None
    completed_qty: Optional[float] = None
    scrapped_qty: Optional[float] = None
    rework_qty: Optional[float] = None
    setup_time_minutes: Optional[float] = None
    run_time_minutes: Optional[float] = None
    wait_time_minutes: Optional[float] = None
    move_time_minutes: Optional[float] = None
    queue_time_minutes: Optional[float] = None
    standard_cycle_time: Optional[float] = None
    actual_cycle_time: Optional[float] = None
    efficiency_pct: Optional[float] = None
    yield_pct: Optional[float] = None
    scrap_code: Optional[str] = None
    rework_code: Optional[str] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    operator_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    instructions: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesOperationExecutionUpdate(BaseModel):
    operation_exec_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    operation_sequence: Optional[int] = None
    operation_code: Optional[str] = None
    operation_name: Optional[str] = None
    work_center_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    planned_qty: Optional[float] = None
    completed_qty: Optional[float] = None
    scrapped_qty: Optional[float] = None
    rework_qty: Optional[float] = None
    setup_time_minutes: Optional[float] = None
    run_time_minutes: Optional[float] = None
    wait_time_minutes: Optional[float] = None
    move_time_minutes: Optional[float] = None
    queue_time_minutes: Optional[float] = None
    standard_cycle_time: Optional[float] = None
    actual_cycle_time: Optional[float] = None
    efficiency_pct: Optional[float] = None
    yield_pct: Optional[float] = None
    scrap_code: Optional[str] = None
    rework_code: Optional[str] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    operator_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    instructions: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesOperationExecutionOut(BaseModel):
    operation_exec_id: uuid.UUID
    execution_id: uuid.UUID
    operation_sequence: int
    operation_code: Optional[str] = None
    operation_name: Optional[str] = None
    work_center_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    planned_qty: Optional[float] = None
    completed_qty: Optional[float] = None
    scrapped_qty: Optional[float] = None
    rework_qty: Optional[float] = None
    setup_time_minutes: Optional[float] = None
    run_time_minutes: Optional[float] = None
    wait_time_minutes: Optional[float] = None
    move_time_minutes: Optional[float] = None
    queue_time_minutes: Optional[float] = None
    standard_cycle_time: Optional[float] = None
    actual_cycle_time: Optional[float] = None
    efficiency_pct: Optional[float] = None
    yield_pct: Optional[float] = None
    scrap_code: Optional[str] = None
    rework_code: Optional[str] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    operator_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    instructions: Optional[str] = None
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

class MesOperationStepsCreate(BaseModel):
    step_id: uuid.UUID
    operation_exec_id: uuid.UUID
    step_sequence: int
    step_description: Optional[str] = None
    instruction_id: Optional[uuid.UUID] = None
    target_value: Optional[str] = None
    actual_value: Optional[str] = None
    uom: Optional[str] = None
    pass_fail: Optional[str] = None
    result: Optional[str] = None
    step_start: Optional[datetime] = None
    step_end: Optional[datetime] = None
    signed_by: Optional[uuid.UUID] = None
    signed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesOperationStepsUpdate(BaseModel):
    step_id: Optional[uuid.UUID] = None
    operation_exec_id: Optional[uuid.UUID] = None
    step_sequence: Optional[int] = None
    step_description: Optional[str] = None
    instruction_id: Optional[uuid.UUID] = None
    target_value: Optional[str] = None
    actual_value: Optional[str] = None
    uom: Optional[str] = None
    pass_fail: Optional[str] = None
    result: Optional[str] = None
    step_start: Optional[datetime] = None
    step_end: Optional[datetime] = None
    signed_by: Optional[uuid.UUID] = None
    signed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesOperationStepsOut(BaseModel):
    step_id: uuid.UUID
    operation_exec_id: uuid.UUID
    step_sequence: int
    step_description: Optional[str] = None
    instruction_id: Optional[uuid.UUID] = None
    target_value: Optional[str] = None
    actual_value: Optional[str] = None
    uom: Optional[str] = None
    pass_fail: Optional[str] = None
    result: Optional[str] = None
    step_start: Optional[datetime] = None
    step_end: Optional[datetime] = None
    signed_by: Optional[uuid.UUID] = None
    signed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MesOperatorAssignmentsCreate(BaseModel):
    assignment_id: uuid.UUID
    operator_id: uuid.UUID
    work_center_id: Optional[uuid.UUID] = None
    station_id: Optional[uuid.UUID] = None
    assigned_from: Optional[datetime] = None
    assigned_until: Optional[datetime] = None
    role: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesOperatorAssignmentsUpdate(BaseModel):
    assignment_id: Optional[uuid.UUID] = None
    operator_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    station_id: Optional[uuid.UUID] = None
    assigned_from: Optional[datetime] = None
    assigned_until: Optional[datetime] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesOperatorAssignmentsOut(BaseModel):
    assignment_id: uuid.UUID
    operator_id: uuid.UUID
    work_center_id: Optional[uuid.UUID] = None
    station_id: Optional[uuid.UUID] = None
    assigned_from: Optional[datetime] = None
    assigned_until: Optional[datetime] = None
    role: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesOperatorCertificationsCreate(BaseModel):
    cert_id: uuid.UUID
    operator_id: uuid.UUID
    cert_type: Optional[str] = None
    cert_number: Optional[str] = None
    issue_date: Optional[date] = None
    expiry_date: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1

class MesOperatorCertificationsUpdate(BaseModel):
    cert_id: Optional[uuid.UUID] = None
    operator_id: Optional[uuid.UUID] = None
    cert_type: Optional[str] = None
    cert_number: Optional[str] = None
    issue_date: Optional[date] = None
    expiry_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesOperatorCertificationsOut(BaseModel):
    cert_id: uuid.UUID
    operator_id: uuid.UUID
    cert_type: Optional[str] = None
    cert_number: Optional[str] = None
    issue_date: Optional[date] = None
    expiry_date: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesOperatorPerformanceCreate(BaseModel):
    performance_id: uuid.UUID
    operator_id: uuid.UUID
    evaluation_date: Optional[date] = None
    productivity_score: Optional[float] = None
    quality_score: Optional[float] = None
    efficiency_score: Optional[float] = None
    error_rate: Optional[float] = None
    safety_incidents: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1

class MesOperatorPerformanceUpdate(BaseModel):
    performance_id: Optional[uuid.UUID] = None
    operator_id: Optional[uuid.UUID] = None
    evaluation_date: Optional[date] = None
    productivity_score: Optional[float] = None
    quality_score: Optional[float] = None
    efficiency_score: Optional[float] = None
    error_rate: Optional[float] = None
    safety_incidents: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesOperatorPerformanceOut(BaseModel):
    performance_id: uuid.UUID
    operator_id: uuid.UUID
    evaluation_date: Optional[date] = None
    productivity_score: Optional[float] = None
    quality_score: Optional[float] = None
    efficiency_score: Optional[float] = None
    error_rate: Optional[float] = None
    safety_incidents: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesOperatorSchedulesCreate(BaseModel):
    schedule_id: uuid.UUID
    operator_id: uuid.UUID
    shift_id: Optional[uuid.UUID] = None
    schedule_date: date
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    is_overtime: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1

class MesOperatorSchedulesUpdate(BaseModel):
    schedule_id: Optional[uuid.UUID] = None
    operator_id: Optional[uuid.UUID] = None
    shift_id: Optional[uuid.UUID] = None
    schedule_date: Optional[date] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    is_overtime: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesOperatorSchedulesOut(BaseModel):
    schedule_id: uuid.UUID
    operator_id: uuid.UUID
    shift_id: Optional[uuid.UUID] = None
    schedule_date: date
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    is_overtime: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesOperatorSkillsCreate(BaseModel):
    skill_id: uuid.UUID
    operator_id: uuid.UUID
    skill_code: Optional[str] = None
    skill_name: Optional[str] = None
    proficiency_level: Optional[int] = None
    certified: Optional[bool] = None
    certified_date: Optional[date] = None
    expiry_date: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1

class MesOperatorSkillsUpdate(BaseModel):
    skill_id: Optional[uuid.UUID] = None
    operator_id: Optional[uuid.UUID] = None
    skill_code: Optional[str] = None
    skill_name: Optional[str] = None
    proficiency_level: Optional[int] = None
    certified: Optional[bool] = None
    certified_date: Optional[date] = None
    expiry_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesOperatorSkillsOut(BaseModel):
    skill_id: uuid.UUID
    operator_id: uuid.UUID
    skill_code: Optional[str] = None
    skill_name: Optional[str] = None
    proficiency_level: Optional[int] = None
    certified: Optional[bool] = None
    certified_date: Optional[date] = None
    expiry_date: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesOperatorTrainingCreate(BaseModel):
    training_id: uuid.UUID
    operator_id: uuid.UUID
    training_course: Optional[str] = None
    training_date: Optional[date] = None
    expiry_date: Optional[date] = None
    trainer: Optional[str] = None
    score: Optional[float] = None
    passed: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1

class MesOperatorTrainingUpdate(BaseModel):
    training_id: Optional[uuid.UUID] = None
    operator_id: Optional[uuid.UUID] = None
    training_course: Optional[str] = None
    training_date: Optional[date] = None
    expiry_date: Optional[date] = None
    trainer: Optional[str] = None
    score: Optional[float] = None
    passed: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesOperatorTrainingOut(BaseModel):
    training_id: uuid.UUID
    operator_id: uuid.UUID
    training_course: Optional[str] = None
    training_date: Optional[date] = None
    expiry_date: Optional[date] = None
    trainer: Optional[str] = None
    score: Optional[float] = None
    passed: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesOperatorsCreate(BaseModel):
    operator_id: uuid.UUID
    employee_code: str
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    hire_date: Optional[date] = None
    is_active: bool = True
    badge_rfid: Optional[str] = None
    department: Optional[str] = None
    job_title: Optional[str] = None
    object_version_number: int = 1

class MesOperatorsUpdate(BaseModel):
    operator_id: Optional[uuid.UUID] = None
    employee_code: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    hire_date: Optional[date] = None
    is_active: Optional[bool] = None
    badge_rfid: Optional[str] = None
    department: Optional[str] = None
    job_title: Optional[str] = None
    object_version_number: Optional[int] = None

class MesOperatorsOut(BaseModel):
    operator_id: uuid.UUID
    employee_code: str
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    hire_date: Optional[date] = None
    is_active: bool
    badge_rfid: Optional[str] = None
    department: Optional[str] = None
    job_title: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesOptimizationProblemsCreate(BaseModel):
    problem_id: uuid.UUID
    problem_type: Optional[str] = None
    problem_name: Optional[str] = None
    objective: Optional[str] = None
    constraints_json: Optional[dict] = None
    parameters: Optional[dict] = None
    algorithm_id: Optional[uuid.UUID] = None
    solver_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    submitted_at: Optional[datetime] = None
    solved_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesOptimizationProblemsUpdate(BaseModel):
    problem_id: Optional[uuid.UUID] = None
    problem_type: Optional[str] = None
    problem_name: Optional[str] = None
    objective: Optional[str] = None
    constraints_json: Optional[dict] = None
    parameters: Optional[dict] = None
    algorithm_id: Optional[uuid.UUID] = None
    solver_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    submitted_at: Optional[datetime] = None
    solved_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesOptimizationProblemsOut(BaseModel):
    problem_id: uuid.UUID
    problem_type: Optional[str] = None
    problem_name: Optional[str] = None
    objective: Optional[str] = None
    constraints_json: Optional[dict] = None
    parameters: Optional[dict] = None
    algorithm_id: Optional[uuid.UUID] = None
    solver_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    submitted_at: Optional[datetime] = None
    solved_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesOptimizationResultsCreate(BaseModel):
    result_id: uuid.UUID
    problem_id: uuid.UUID
    objective_value: Optional[float] = None
    solution_json: Optional[dict] = None
    solve_time_ms: Optional[int] = None
    gap_pct: Optional[float] = None
    is_optimal: Optional[bool] = None
    iterations: Optional[int] = None
    solver_log: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesOptimizationResultsUpdate(BaseModel):
    result_id: Optional[uuid.UUID] = None
    problem_id: Optional[uuid.UUID] = None
    objective_value: Optional[float] = None
    solution_json: Optional[dict] = None
    solve_time_ms: Optional[int] = None
    gap_pct: Optional[float] = None
    is_optimal: Optional[bool] = None
    iterations: Optional[int] = None
    solver_log: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesOptimizationResultsOut(BaseModel):
    result_id: uuid.UUID
    problem_id: uuid.UUID
    objective_value: Optional[float] = None
    solution_json: Optional[dict] = None
    solve_time_ms: Optional[int] = None
    gap_pct: Optional[float] = None
    is_optimal: Optional[bool] = None
    iterations: Optional[int] = None
    solver_log: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesOrtoolsProblemsCreate(BaseModel):
    problem_id: uuid.UUID
    problem_type: Optional[str] = None
    problem_name: Optional[str] = None
    problem_data: Optional[dict] = None
    solver_config: Optional[dict] = None
    solution_data: Optional[dict] = None
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_optimal: Optional[bool] = None
    solver_log: Optional[str] = None
    solved_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesOrtoolsProblemsUpdate(BaseModel):
    problem_id: Optional[uuid.UUID] = None
    problem_type: Optional[str] = None
    problem_name: Optional[str] = None
    problem_data: Optional[dict] = None
    solver_config: Optional[dict] = None
    solution_data: Optional[dict] = None
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_optimal: Optional[bool] = None
    solver_log: Optional[str] = None
    solved_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesOrtoolsProblemsOut(BaseModel):
    problem_id: uuid.UUID
    problem_type: Optional[str] = None
    problem_name: Optional[str] = None
    problem_data: Optional[dict] = None
    solver_config: Optional[dict] = None
    solution_data: Optional[dict] = None
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_optimal: Optional[bool] = None
    solver_log: Optional[str] = None
    solved_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesPerformanceActualsCreate(BaseModel):
    actual_id: uuid.UUID
    metric_id: uuid.UUID
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    actual_value: float
    target_value: Optional[float] = None
    variance: Optional[float] = None
    period_start: Optional[date] = None
    period_end: Optional[date] = None
    recorded_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesPerformanceActualsUpdate(BaseModel):
    actual_id: Optional[uuid.UUID] = None
    metric_id: Optional[uuid.UUID] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    actual_value: Optional[float] = None
    target_value: Optional[float] = None
    variance: Optional[float] = None
    period_start: Optional[date] = None
    period_end: Optional[date] = None
    recorded_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesPerformanceActualsOut(BaseModel):
    actual_id: uuid.UUID
    metric_id: uuid.UUID
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    actual_value: float
    target_value: Optional[float] = None
    variance: Optional[float] = None
    period_start: Optional[date] = None
    period_end: Optional[date] = None
    recorded_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesPerformanceMetricsCreate(BaseModel):
    metric_id: uuid.UUID
    metric_code: str
    metric_name: str
    metric_category: Optional[str] = None
    calculation_method: Optional[str] = None
    uom: Optional[str] = None
    higher_is_better: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1

class MesPerformanceMetricsUpdate(BaseModel):
    metric_id: Optional[uuid.UUID] = None
    metric_code: Optional[str] = None
    metric_name: Optional[str] = None
    metric_category: Optional[str] = None
    calculation_method: Optional[str] = None
    uom: Optional[str] = None
    higher_is_better: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesPerformanceMetricsOut(BaseModel):
    metric_id: uuid.UUID
    metric_code: str
    metric_name: str
    metric_category: Optional[str] = None
    calculation_method: Optional[str] = None
    uom: Optional[str] = None
    higher_is_better: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesPredictionsCreate(BaseModel):
    prediction_id: uuid.UUID
    model_id: Optional[uuid.UUID] = None
    prediction_type: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    predicted_value: Optional[float] = None
    probability: Optional[float] = None
    confidence_lower: Optional[float] = None
    confidence_upper: Optional[float] = None
    features_json: Optional[dict] = None
    actual_value: Optional[float] = None
    prediction_error: Optional[float] = None
    horizon: Optional[str] = None
    predicted_at: Optional[datetime] = None
    scenario_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1

class MesPredictionsUpdate(BaseModel):
    prediction_id: Optional[uuid.UUID] = None
    model_id: Optional[uuid.UUID] = None
    prediction_type: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    predicted_value: Optional[float] = None
    probability: Optional[float] = None
    confidence_lower: Optional[float] = None
    confidence_upper: Optional[float] = None
    features_json: Optional[dict] = None
    actual_value: Optional[float] = None
    prediction_error: Optional[float] = None
    horizon: Optional[str] = None
    predicted_at: Optional[datetime] = None
    scenario_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesPredictionsOut(BaseModel):
    prediction_id: uuid.UUID
    model_id: Optional[uuid.UUID] = None
    prediction_type: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    predicted_value: Optional[float] = None
    probability: Optional[float] = None
    confidence_lower: Optional[float] = None
    confidence_upper: Optional[float] = None
    features_json: Optional[dict] = None
    actual_value: Optional[float] = None
    prediction_error: Optional[float] = None
    horizon: Optional[str] = None
    predicted_at: Optional[datetime] = None
    scenario_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesProductionCellsCreate(BaseModel):
    cell_id: uuid.UUID
    cell_code: str
    cell_name: str
    production_line_id: Optional[uuid.UUID] = None
    cell_type: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesProductionCellsUpdate(BaseModel):
    cell_id: Optional[uuid.UUID] = None
    cell_code: Optional[str] = None
    cell_name: Optional[str] = None
    production_line_id: Optional[uuid.UUID] = None
    cell_type: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesProductionCellsOut(BaseModel):
    cell_id: uuid.UUID
    cell_code: str
    cell_name: str
    production_line_id: Optional[uuid.UUID] = None
    cell_type: Optional[str] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesProductionLinesCreate(BaseModel):
    production_line_id: uuid.UUID
    line_code: str
    line_name: str
    line_type: Optional[str] = None
    site_id: Optional[uuid.UUID] = None
    supervisor_id: Optional[uuid.UUID] = None
    takt_time_seconds: Optional[float] = None
    cycle_time_seconds: Optional[float] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesProductionLinesUpdate(BaseModel):
    production_line_id: Optional[uuid.UUID] = None
    line_code: Optional[str] = None
    line_name: Optional[str] = None
    line_type: Optional[str] = None
    site_id: Optional[uuid.UUID] = None
    supervisor_id: Optional[uuid.UUID] = None
    takt_time_seconds: Optional[float] = None
    cycle_time_seconds: Optional[float] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesProductionLinesOut(BaseModel):
    production_line_id: uuid.UUID
    line_code: str
    line_name: str
    line_type: Optional[str] = None
    site_id: Optional[uuid.UUID] = None
    supervisor_id: Optional[uuid.UUID] = None
    takt_time_seconds: Optional[float] = None
    cycle_time_seconds: Optional[float] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesPromptTemplatesCreate(BaseModel):
    template_id: uuid.UUID
    template_name: str
    template_type: Optional[str] = None
    template_text: Optional[str] = None
    variables_json: Optional[dict] = None
    version: Optional[int] = None
    llm_config_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1

class MesPromptTemplatesUpdate(BaseModel):
    template_id: Optional[uuid.UUID] = None
    template_name: Optional[str] = None
    template_type: Optional[str] = None
    template_text: Optional[str] = None
    variables_json: Optional[dict] = None
    version: Optional[int] = None
    llm_config_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesPromptTemplatesOut(BaseModel):
    template_id: uuid.UUID
    template_name: str
    template_type: Optional[str] = None
    template_text: Optional[str] = None
    variables_json: Optional[dict] = None
    version: Optional[int] = None
    llm_config_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesQualityHoldsCreate(BaseModel):
    hold_id: uuid.UUID
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    hold_reason: Optional[str] = None
    hold_qty: Optional[float] = None
    hold_date: Optional[datetime] = None
    released_date: Optional[datetime] = None
    held_by: Optional[uuid.UUID] = None
    released_by: Optional[uuid.UUID] = None
    disposition: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesQualityHoldsUpdate(BaseModel):
    hold_id: Optional[uuid.UUID] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    hold_reason: Optional[str] = None
    hold_qty: Optional[float] = None
    hold_date: Optional[datetime] = None
    released_date: Optional[datetime] = None
    held_by: Optional[uuid.UUID] = None
    released_by: Optional[uuid.UUID] = None
    disposition: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesQualityHoldsOut(BaseModel):
    hold_id: uuid.UUID
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    hold_reason: Optional[str] = None
    hold_qty: Optional[float] = None
    hold_date: Optional[datetime] = None
    released_date: Optional[datetime] = None
    held_by: Optional[uuid.UUID] = None
    released_by: Optional[uuid.UUID] = None
    disposition: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesQualityInspectionsCreate(BaseModel):
    inspection_id: uuid.UUID
    operation_exec_id: uuid.UUID
    inspection_type: Optional[str] = None
    inspector_id: Optional[uuid.UUID] = None
    inspection_time: Optional[datetime] = None
    result: Optional[str] = None
    measured_value: Optional[float] = None
    spec_min: Optional[float] = None
    spec_max: Optional[float] = None
    uom: Optional[str] = None
    defect_code: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesQualityInspectionsUpdate(BaseModel):
    inspection_id: Optional[uuid.UUID] = None
    operation_exec_id: Optional[uuid.UUID] = None
    inspection_type: Optional[str] = None
    inspector_id: Optional[uuid.UUID] = None
    inspection_time: Optional[datetime] = None
    result: Optional[str] = None
    measured_value: Optional[float] = None
    spec_min: Optional[float] = None
    spec_max: Optional[float] = None
    uom: Optional[str] = None
    defect_code: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesQualityInspectionsOut(BaseModel):
    inspection_id: uuid.UUID
    operation_exec_id: uuid.UUID
    inspection_type: Optional[str] = None
    inspector_id: Optional[uuid.UUID] = None
    inspection_time: Optional[datetime] = None
    result: Optional[str] = None
    measured_value: Optional[float] = None
    spec_min: Optional[float] = None
    spec_max: Optional[float] = None
    uom: Optional[str] = None
    defect_code: Optional[str] = None
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

class MesQualitySpcDataCreate(BaseModel):
    spc_id: uuid.UUID
    inspection_id: Optional[uuid.UUID] = None
    operation_exec_id: uuid.UUID
    sample_size: Optional[int] = None
    mean_value: Optional[float] = None
    std_dev: Optional[float] = None
    cp: Optional[float] = None
    cpk: Optional[float] = None
    usl: Optional[float] = None
    lsl: Optional[float] = None
    out_of_control: Optional[bool] = None
    sample_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesQualitySpcDataUpdate(BaseModel):
    spc_id: Optional[uuid.UUID] = None
    inspection_id: Optional[uuid.UUID] = None
    operation_exec_id: Optional[uuid.UUID] = None
    sample_size: Optional[int] = None
    mean_value: Optional[float] = None
    std_dev: Optional[float] = None
    cp: Optional[float] = None
    cpk: Optional[float] = None
    usl: Optional[float] = None
    lsl: Optional[float] = None
    out_of_control: Optional[bool] = None
    sample_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesQualitySpcDataOut(BaseModel):
    spc_id: uuid.UUID
    inspection_id: Optional[uuid.UUID] = None
    operation_exec_id: uuid.UUID
    sample_size: Optional[int] = None
    mean_value: Optional[float] = None
    std_dev: Optional[float] = None
    cp: Optional[float] = None
    cpk: Optional[float] = None
    usl: Optional[float] = None
    lsl: Optional[float] = None
    out_of_control: Optional[bool] = None
    sample_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesResourceAvailabilityCreate(BaseModel):
    availability_id: uuid.UUID
    resource_id: uuid.UUID
    available_from: Optional[datetime] = None
    available_until: Optional[datetime] = None
    available_qty: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class MesResourceAvailabilityUpdate(BaseModel):
    availability_id: Optional[uuid.UUID] = None
    resource_id: Optional[uuid.UUID] = None
    available_from: Optional[datetime] = None
    available_until: Optional[datetime] = None
    available_qty: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesResourceAvailabilityOut(BaseModel):
    availability_id: uuid.UUID
    resource_id: uuid.UUID
    available_from: Optional[datetime] = None
    available_until: Optional[datetime] = None
    available_qty: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesResourceCostsCreate(BaseModel):
    cost_id: uuid.UUID
    resource_id: uuid.UUID
    cost_type: Optional[str] = None
    cost_rate: Optional[float] = None
    cost_uom: Optional[str] = None
    currency: Optional[str] = None
    effective_from: Optional[date] = None
    effective_until: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1

class MesResourceCostsUpdate(BaseModel):
    cost_id: Optional[uuid.UUID] = None
    resource_id: Optional[uuid.UUID] = None
    cost_type: Optional[str] = None
    cost_rate: Optional[float] = None
    cost_uom: Optional[str] = None
    currency: Optional[str] = None
    effective_from: Optional[date] = None
    effective_until: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesResourceCostsOut(BaseModel):
    cost_id: uuid.UUID
    resource_id: uuid.UUID
    cost_type: Optional[str] = None
    cost_rate: Optional[float] = None
    cost_uom: Optional[str] = None
    currency: Optional[str] = None
    effective_from: Optional[date] = None
    effective_until: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesResourceTypesCreate(BaseModel):
    resource_type_id: uuid.UUID
    type_code: str
    type_name: str
    is_active: bool = True
    object_version_number: int = 1

class MesResourceTypesUpdate(BaseModel):
    resource_type_id: Optional[uuid.UUID] = None
    type_code: Optional[str] = None
    type_name: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesResourceTypesOut(BaseModel):
    resource_type_id: uuid.UUID
    type_code: str
    type_name: str
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesResourcesCreate(BaseModel):
    resource_id: uuid.UUID
    resource_code: str
    resource_name: str
    resource_type_id: Optional[uuid.UUID] = None
    resource_type: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesResourcesUpdate(BaseModel):
    resource_id: Optional[uuid.UUID] = None
    resource_code: Optional[str] = None
    resource_name: Optional[str] = None
    resource_type_id: Optional[uuid.UUID] = None
    resource_type: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesResourcesOut(BaseModel):
    resource_id: uuid.UUID
    resource_code: str
    resource_name: str
    resource_type_id: Optional[uuid.UUID] = None
    resource_type: Optional[str] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesScenariosCreate(BaseModel):
    scenario_id: uuid.UUID
    scenario_type: Optional[str] = None
    scenario_name: str
    description: Optional[str] = None
    assumptions_json: Optional[dict] = None
    constraints_json: Optional[dict] = None
    objectives_json: Optional[dict] = None
    results_json: Optional[dict] = None
    comparison_json: Optional[dict] = None
    recommendations: Optional[str] = None
    created_by: Optional[uuid.UUID] = None
    is_baseline: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1

class MesScenariosUpdate(BaseModel):
    scenario_id: Optional[uuid.UUID] = None
    scenario_type: Optional[str] = None
    scenario_name: Optional[str] = None
    description: Optional[str] = None
    assumptions_json: Optional[dict] = None
    constraints_json: Optional[dict] = None
    objectives_json: Optional[dict] = None
    results_json: Optional[dict] = None
    comparison_json: Optional[dict] = None
    recommendations: Optional[str] = None
    created_by: Optional[uuid.UUID] = None
    is_baseline: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesScenariosOut(BaseModel):
    scenario_id: uuid.UUID
    scenario_type: Optional[str] = None
    scenario_name: str
    description: Optional[str] = None
    assumptions_json: Optional[dict] = None
    constraints_json: Optional[dict] = None
    objectives_json: Optional[dict] = None
    results_json: Optional[dict] = None
    comparison_json: Optional[dict] = None
    recommendations: Optional[str] = None
    created_by: Optional[uuid.UUID] = None
    is_baseline: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesScheduleResultsCreate(BaseModel):
    result_id: uuid.UUID
    problem_id: uuid.UUID
    schedule_json: Optional[dict] = None
    makespan: Optional[float] = None
    total_tardiness: Optional[float] = None
    machine_utilization: Optional[dict] = None
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_optimal: Optional[bool] = None
    reschedule_trigger: Optional[str] = None
    is_applied: Optional[bool] = None
    applied_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesScheduleResultsUpdate(BaseModel):
    result_id: Optional[uuid.UUID] = None
    problem_id: Optional[uuid.UUID] = None
    schedule_json: Optional[dict] = None
    makespan: Optional[float] = None
    total_tardiness: Optional[float] = None
    machine_utilization: Optional[dict] = None
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_optimal: Optional[bool] = None
    reschedule_trigger: Optional[str] = None
    is_applied: Optional[bool] = None
    applied_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesScheduleResultsOut(BaseModel):
    result_id: uuid.UUID
    problem_id: uuid.UUID
    schedule_json: Optional[dict] = None
    makespan: Optional[float] = None
    total_tardiness: Optional[float] = None
    machine_utilization: Optional[dict] = None
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_optimal: Optional[bool] = None
    reschedule_trigger: Optional[str] = None
    is_applied: Optional[bool] = None
    applied_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesSchedulingProblemsCreate(BaseModel):
    problem_id: uuid.UUID
    schedule_type: Optional[str] = None
    problem_name: Optional[str] = None
    jobs_json: Optional[dict] = None
    machines_json: Optional[dict] = None
    processing_times: Optional[dict] = None
    setup_times: Optional[dict] = None
    due_dates: Optional[dict] = None
    priorities: Optional[dict] = None
    constraints_json: Optional[dict] = None
    objective: Optional[str] = None
    horizon_start: Optional[datetime] = None
    horizon_end: Optional[datetime] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesSchedulingProblemsUpdate(BaseModel):
    problem_id: Optional[uuid.UUID] = None
    schedule_type: Optional[str] = None
    problem_name: Optional[str] = None
    jobs_json: Optional[dict] = None
    machines_json: Optional[dict] = None
    processing_times: Optional[dict] = None
    setup_times: Optional[dict] = None
    due_dates: Optional[dict] = None
    priorities: Optional[dict] = None
    constraints_json: Optional[dict] = None
    objective: Optional[str] = None
    horizon_start: Optional[datetime] = None
    horizon_end: Optional[datetime] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesSchedulingProblemsOut(BaseModel):
    problem_id: uuid.UUID
    schedule_type: Optional[str] = None
    problem_name: Optional[str] = None
    jobs_json: Optional[dict] = None
    machines_json: Optional[dict] = None
    processing_times: Optional[dict] = None
    setup_times: Optional[dict] = None
    due_dates: Optional[dict] = None
    priorities: Optional[dict] = None
    constraints_json: Optional[dict] = None
    objective: Optional[str] = None
    horizon_start: Optional[datetime] = None
    horizon_end: Optional[datetime] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesScipyAnalysesCreate(BaseModel):
    analysis_id: uuid.UUID
    analysis_type: Optional[str] = None
    analysis_name: Optional[str] = None
    input_data: Optional[dict] = None
    method: Optional[str] = None
    parameters: Optional[dict] = None
    result_data: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    performed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesScipyAnalysesUpdate(BaseModel):
    analysis_id: Optional[uuid.UUID] = None
    analysis_type: Optional[str] = None
    analysis_name: Optional[str] = None
    input_data: Optional[dict] = None
    method: Optional[str] = None
    parameters: Optional[dict] = None
    result_data: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    performed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesScipyAnalysesOut(BaseModel):
    analysis_id: uuid.UUID
    analysis_type: Optional[str] = None
    analysis_name: Optional[str] = None
    input_data: Optional[dict] = None
    method: Optional[str] = None
    parameters: Optional[dict] = None
    result_data: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    performed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesSensorCalibrationsCreate(BaseModel):
    calibration_id: uuid.UUID
    sensor_id: uuid.UUID
    calibration_date: date
    calibrated_by: Optional[str] = None
    result: Optional[str] = None
    as_found: Optional[dict] = None
    as_left: Optional[dict] = None
    certificate_number: Optional[str] = None
    next_calibration_due: Optional[date] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesSensorCalibrationsUpdate(BaseModel):
    calibration_id: Optional[uuid.UUID] = None
    sensor_id: Optional[uuid.UUID] = None
    calibration_date: Optional[date] = None
    calibrated_by: Optional[str] = None
    result: Optional[str] = None
    as_found: Optional[dict] = None
    as_left: Optional[dict] = None
    certificate_number: Optional[str] = None
    next_calibration_due: Optional[date] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesSensorCalibrationsOut(BaseModel):
    calibration_id: uuid.UUID
    sensor_id: uuid.UUID
    calibration_date: date
    calibrated_by: Optional[str] = None
    result: Optional[str] = None
    as_found: Optional[dict] = None
    as_left: Optional[dict] = None
    certificate_number: Optional[str] = None
    next_calibration_due: Optional[date] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesSensorsCreate(BaseModel):
    sensor_id: uuid.UUID
    sensor_code: str
    sensor_name: Optional[str] = None
    equipment_id: Optional[uuid.UUID] = None
    sensor_type_id: Optional[uuid.UUID] = None
    model: Optional[str] = None
    range_min: Optional[float] = None
    range_max: Optional[float] = None
    accuracy: Optional[str] = None
    resolution: Optional[str] = None
    uom: Optional[str] = None
    location_on_equipment: Optional[str] = None
    status: Optional[str] = None
    last_calibrated: Optional[date] = None
    calibration_due: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1

class MesSensorsUpdate(BaseModel):
    sensor_id: Optional[uuid.UUID] = None
    sensor_code: Optional[str] = None
    sensor_name: Optional[str] = None
    equipment_id: Optional[uuid.UUID] = None
    sensor_type_id: Optional[uuid.UUID] = None
    model: Optional[str] = None
    range_min: Optional[float] = None
    range_max: Optional[float] = None
    accuracy: Optional[str] = None
    resolution: Optional[str] = None
    uom: Optional[str] = None
    location_on_equipment: Optional[str] = None
    status: Optional[str] = None
    last_calibrated: Optional[date] = None
    calibration_due: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesSensorsOut(BaseModel):
    sensor_id: uuid.UUID
    sensor_code: str
    sensor_name: Optional[str] = None
    equipment_id: Optional[uuid.UUID] = None
    sensor_type_id: Optional[uuid.UUID] = None
    model: Optional[str] = None
    range_min: Optional[float] = None
    range_max: Optional[float] = None
    accuracy: Optional[str] = None
    resolution: Optional[str] = None
    uom: Optional[str] = None
    location_on_equipment: Optional[str] = None
    status: Optional[str] = None
    last_calibrated: Optional[date] = None
    calibration_due: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesShiftHandoversCreate(BaseModel):
    handover_id: uuid.UUID
    work_center_id: uuid.UUID
    from_shift_id: Optional[uuid.UUID] = None
    to_shift_id: Optional[uuid.UUID] = None
    handover_time: Optional[datetime] = None
    notes: Optional[str] = None
    issues_reported: Optional[str] = None
    pending_tasks: Optional[str] = None
    handed_by: Optional[uuid.UUID] = None
    received_by: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesShiftHandoversUpdate(BaseModel):
    handover_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    from_shift_id: Optional[uuid.UUID] = None
    to_shift_id: Optional[uuid.UUID] = None
    handover_time: Optional[datetime] = None
    notes: Optional[str] = None
    issues_reported: Optional[str] = None
    pending_tasks: Optional[str] = None
    handed_by: Optional[uuid.UUID] = None
    received_by: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesShiftHandoversOut(BaseModel):
    handover_id: uuid.UUID
    work_center_id: uuid.UUID
    from_shift_id: Optional[uuid.UUID] = None
    to_shift_id: Optional[uuid.UUID] = None
    handover_time: Optional[datetime] = None
    notes: Optional[str] = None
    issues_reported: Optional[str] = None
    pending_tasks: Optional[str] = None
    handed_by: Optional[uuid.UUID] = None
    received_by: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MesShiftSchedulesCreate(BaseModel):
    schedule_id: uuid.UUID
    work_center_id: uuid.UUID
    shift_id: uuid.UUID
    schedule_date: date
    crew_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1

class MesShiftSchedulesUpdate(BaseModel):
    schedule_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    shift_id: Optional[uuid.UUID] = None
    schedule_date: Optional[date] = None
    crew_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesShiftSchedulesOut(BaseModel):
    schedule_id: uuid.UUID
    work_center_id: uuid.UUID
    shift_id: uuid.UUID
    schedule_date: date
    crew_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesShiftsCreate(BaseModel):
    shift_id: uuid.UUID
    shift_code: str
    shift_name: str
    start_time: str
    end_time: str
    duration_hours: Optional[float] = None
    is_night_shift: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1

class MesShiftsUpdate(BaseModel):
    shift_id: Optional[uuid.UUID] = None
    shift_code: Optional[str] = None
    shift_name: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    duration_hours: Optional[float] = None
    is_night_shift: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesShiftsOut(BaseModel):
    shift_id: uuid.UUID
    shift_code: str
    shift_name: str
    start_time: str
    end_time: str
    duration_hours: Optional[float] = None
    is_night_shift: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesSolverConfigsCreate(BaseModel):
    solver_id: uuid.UUID
    solver_name: str
    solver_type: Optional[str] = None
    version: Optional[str] = None
    parameters: Optional[dict] = None
    is_default: Optional[bool] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesSolverConfigsUpdate(BaseModel):
    solver_id: Optional[uuid.UUID] = None
    solver_name: Optional[str] = None
    solver_type: Optional[str] = None
    version: Optional[str] = None
    parameters: Optional[dict] = None
    is_default: Optional[bool] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesSolverConfigsOut(BaseModel):
    solver_id: uuid.UUID
    solver_name: str
    solver_type: Optional[str] = None
    version: Optional[str] = None
    parameters: Optional[dict] = None
    is_default: Optional[bool] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesStationAssignmentsCreate(BaseModel):
    assignment_id: uuid.UUID
    station_id: uuid.UUID
    work_center_id: Optional[uuid.UUID] = None
    assigned_from: Optional[datetime] = None
    assigned_until: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesStationAssignmentsUpdate(BaseModel):
    assignment_id: Optional[uuid.UUID] = None
    station_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    assigned_from: Optional[datetime] = None
    assigned_until: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesStationAssignmentsOut(BaseModel):
    assignment_id: uuid.UUID
    station_id: uuid.UUID
    work_center_id: Optional[uuid.UUID] = None
    assigned_from: Optional[datetime] = None
    assigned_until: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesStationTypesCreate(BaseModel):
    station_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesStationTypesUpdate(BaseModel):
    station_type_id: Optional[uuid.UUID] = None
    type_code: Optional[str] = None
    type_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesStationTypesOut(BaseModel):
    station_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesStationsCreate(BaseModel):
    station_id: uuid.UUID
    station_code: str
    station_name: str
    station_type_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    location: Optional[str] = None
    has_hmi: Optional[bool] = None
    has_scanner: Optional[bool] = None
    has_printer: Optional[bool] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesStationsUpdate(BaseModel):
    station_id: Optional[uuid.UUID] = None
    station_code: Optional[str] = None
    station_name: Optional[str] = None
    station_type_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    location: Optional[str] = None
    has_hmi: Optional[bool] = None
    has_scanner: Optional[bool] = None
    has_printer: Optional[bool] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesStationsOut(BaseModel):
    station_id: uuid.UUID
    station_code: str
    station_name: str
    station_type_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    location: Optional[str] = None
    has_hmi: Optional[bool] = None
    has_scanner: Optional[bool] = None
    has_printer: Optional[bool] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesToolCribsCreate(BaseModel):
    crib_id: uuid.UUID
    crib_code: str
    crib_name: Optional[str] = None
    location: Optional[str] = None
    dimensions: Optional[dict] = None
    total_capacity: Optional[int] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesToolCribsUpdate(BaseModel):
    crib_id: Optional[uuid.UUID] = None
    crib_code: Optional[str] = None
    crib_name: Optional[str] = None
    location: Optional[str] = None
    dimensions: Optional[dict] = None
    total_capacity: Optional[int] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesToolCribsOut(BaseModel):
    crib_id: uuid.UUID
    crib_code: str
    crib_name: Optional[str] = None
    location: Optional[str] = None
    dimensions: Optional[dict] = None
    total_capacity: Optional[int] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesToolingAssignmentsCreate(BaseModel):
    assignment_id: uuid.UUID
    tool_id: uuid.UUID
    operation_exec_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    assigned_at: Optional[datetime] = None
    returned_at: Optional[datetime] = None
    usage_count: Optional[int] = None
    assigned_by: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1

class MesToolingAssignmentsUpdate(BaseModel):
    assignment_id: Optional[uuid.UUID] = None
    tool_id: Optional[uuid.UUID] = None
    operation_exec_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    assigned_at: Optional[datetime] = None
    returned_at: Optional[datetime] = None
    usage_count: Optional[int] = None
    assigned_by: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesToolingAssignmentsOut(BaseModel):
    assignment_id: uuid.UUID
    tool_id: uuid.UUID
    operation_exec_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    assigned_at: Optional[datetime] = None
    returned_at: Optional[datetime] = None
    usage_count: Optional[int] = None
    assigned_by: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesToolingLifeTrackingCreate(BaseModel):
    tracking_id: uuid.UUID
    tool_id: uuid.UUID
    usage_count: Optional[int] = None
    max_usage_life: Optional[int] = None
    total_runtime_hours: Optional[float] = None
    max_runtime_hours: Optional[float] = None
    wear_percentage: Optional[float] = None
    last_maintenance: Optional[datetime] = None
    next_maintenance_due: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class MesToolingLifeTrackingUpdate(BaseModel):
    tracking_id: Optional[uuid.UUID] = None
    tool_id: Optional[uuid.UUID] = None
    usage_count: Optional[int] = None
    max_usage_life: Optional[int] = None
    total_runtime_hours: Optional[float] = None
    max_runtime_hours: Optional[float] = None
    wear_percentage: Optional[float] = None
    last_maintenance: Optional[datetime] = None
    next_maintenance_due: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesToolingLifeTrackingOut(BaseModel):
    tracking_id: uuid.UUID
    tool_id: uuid.UUID
    usage_count: Optional[int] = None
    max_usage_life: Optional[int] = None
    total_runtime_hours: Optional[float] = None
    max_runtime_hours: Optional[float] = None
    wear_percentage: Optional[float] = None
    last_maintenance: Optional[datetime] = None
    next_maintenance_due: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesToolingMasterCreate(BaseModel):
    tool_id: uuid.UUID
    tool_code: str
    tool_name: str
    tool_type_id: Optional[uuid.UUID] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None
    shelf_life_count: Optional[int] = None
    shelf_life_uom: Optional[str] = None
    dimensions: Optional[str] = None
    weight_kg: Optional[float] = None
    rfid_tag: Optional[str] = None
    barcode: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesToolingMasterUpdate(BaseModel):
    tool_id: Optional[uuid.UUID] = None
    tool_code: Optional[str] = None
    tool_name: Optional[str] = None
    tool_type_id: Optional[uuid.UUID] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None
    shelf_life_count: Optional[int] = None
    shelf_life_uom: Optional[str] = None
    dimensions: Optional[str] = None
    weight_kg: Optional[float] = None
    rfid_tag: Optional[str] = None
    barcode: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesToolingMasterOut(BaseModel):
    tool_id: uuid.UUID
    tool_code: str
    tool_name: str
    tool_type_id: Optional[uuid.UUID] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None
    shelf_life_count: Optional[int] = None
    shelf_life_uom: Optional[str] = None
    dimensions: Optional[str] = None
    weight_kg: Optional[float] = None
    rfid_tag: Optional[str] = None
    barcode: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesToolingTypesCreate(BaseModel):
    tool_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesToolingTypesUpdate(BaseModel):
    tool_type_id: Optional[uuid.UUID] = None
    type_code: Optional[str] = None
    type_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesToolingTypesOut(BaseModel):
    tool_type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesVectorStoreConfigsCreate(BaseModel):
    config_id: uuid.UUID
    config_name: Optional[str] = None
    store_type: Optional[str] = None
    connection_string: Optional[str] = None
    embedding_model: Optional[str] = None
    collection_name: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesVectorStoreConfigsUpdate(BaseModel):
    config_id: Optional[uuid.UUID] = None
    config_name: Optional[str] = None
    store_type: Optional[str] = None
    connection_string: Optional[str] = None
    embedding_model: Optional[str] = None
    collection_name: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesVectorStoreConfigsOut(BaseModel):
    config_id: uuid.UUID
    config_name: Optional[str] = None
    store_type: Optional[str] = None
    connection_string: Optional[str] = None
    embedding_model: Optional[str] = None
    collection_name: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesVectorStoreDocumentsCreate(BaseModel):
    doc_id: uuid.UUID
    config_id: uuid.UUID
    title: Optional[str] = None
    content: Optional[str] = None
    meta_data: Optional[dict] = None
    embedding_id: Optional[str] = None
    chunk_index: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1

class MesVectorStoreDocumentsUpdate(BaseModel):
    doc_id: Optional[uuid.UUID] = None
    config_id: Optional[uuid.UUID] = None
    title: Optional[str] = None
    content: Optional[str] = None
    meta_data: Optional[dict] = None
    embedding_id: Optional[str] = None
    chunk_index: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesVectorStoreDocumentsOut(BaseModel):
    doc_id: uuid.UUID
    config_id: uuid.UUID
    title: Optional[str] = None
    content: Optional[str] = None
    meta_data: Optional[dict] = None
    embedding_id: Optional[str] = None
    chunk_index: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesWorkCenterCalendarsCreate(BaseModel):
    calendar_id: uuid.UUID
    work_center_id: uuid.UUID
    calendar_date: date
    shift_id: Optional[uuid.UUID] = None
    available_hours: Optional[float] = None
    is_working_day: Optional[bool] = None
    is_active: bool = True
    object_version_number: int = 1

class MesWorkCenterCalendarsUpdate(BaseModel):
    calendar_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    calendar_date: Optional[date] = None
    shift_id: Optional[uuid.UUID] = None
    available_hours: Optional[float] = None
    is_working_day: Optional[bool] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesWorkCenterCalendarsOut(BaseModel):
    calendar_id: uuid.UUID
    work_center_id: uuid.UUID
    calendar_date: date
    shift_id: Optional[uuid.UUID] = None
    available_hours: Optional[float] = None
    is_working_day: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesWorkCenterCapacitiesCreate(BaseModel):
    capacity_id: uuid.UUID
    work_center_id: uuid.UUID
    capacity_type: Optional[str] = None
    capacity_value: float
    uom: Optional[str] = None
    effective_from: Optional[date] = None
    effective_until: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1

class MesWorkCenterCapacitiesUpdate(BaseModel):
    capacity_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    capacity_type: Optional[str] = None
    capacity_value: Optional[float] = None
    uom: Optional[str] = None
    effective_from: Optional[date] = None
    effective_until: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesWorkCenterCapacitiesOut(BaseModel):
    capacity_id: uuid.UUID
    work_center_id: uuid.UUID
    capacity_type: Optional[str] = None
    capacity_value: float
    uom: Optional[str] = None
    effective_from: Optional[date] = None
    effective_until: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesWorkCenterConstraintsCreate(BaseModel):
    constraint_id: uuid.UUID
    work_center_id: uuid.UUID
    constraint_type: Optional[str] = None
    constraint_name: Optional[str] = None
    max_capacity: Optional[float] = None
    is_bottleneck: Optional[bool] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesWorkCenterConstraintsUpdate(BaseModel):
    constraint_id: Optional[uuid.UUID] = None
    work_center_id: Optional[uuid.UUID] = None
    constraint_type: Optional[str] = None
    constraint_name: Optional[str] = None
    max_capacity: Optional[float] = None
    is_bottleneck: Optional[bool] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesWorkCenterConstraintsOut(BaseModel):
    constraint_id: uuid.UUID
    work_center_id: uuid.UUID
    constraint_type: Optional[str] = None
    constraint_name: Optional[str] = None
    max_capacity: Optional[float] = None
    is_bottleneck: Optional[bool] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesWorkCenterTypesCreate(BaseModel):
    work_center_type_id: uuid.UUID
    type_code: str
    type_name: str
    is_automated: Optional[bool] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesWorkCenterTypesUpdate(BaseModel):
    work_center_type_id: Optional[uuid.UUID] = None
    type_code: Optional[str] = None
    type_name: Optional[str] = None
    is_automated: Optional[bool] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesWorkCenterTypesOut(BaseModel):
    work_center_type_id: uuid.UUID
    type_code: str
    type_name: str
    is_automated: Optional[bool] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesWorkCentersCreate(BaseModel):
    work_center_id: uuid.UUID
    site_id: Optional[uuid.UUID] = None
    center_code: str
    center_name: str
    center_type: str
    work_center_type_id: Optional[uuid.UUID] = None
    capacity_per_shift: Optional[float] = None
    efficiency_rate: Optional[float] = None
    iot_gateway_topic: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesWorkCentersUpdate(BaseModel):
    work_center_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    center_code: Optional[str] = None
    center_name: Optional[str] = None
    center_type: Optional[str] = None
    work_center_type_id: Optional[uuid.UUID] = None
    capacity_per_shift: Optional[float] = None
    efficiency_rate: Optional[float] = None
    iot_gateway_topic: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesWorkCentersOut(BaseModel):
    work_center_id: uuid.UUID
    site_id: Optional[uuid.UUID] = None
    center_code: str
    center_name: str
    center_type: str
    work_center_type_id: Optional[uuid.UUID] = None
    capacity_per_shift: Optional[float] = None
    efficiency_rate: Optional[float] = None
    iot_gateway_topic: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesWorkOrderExecutionCreate(BaseModel):
    execution_id: uuid.UUID
    work_order_id: Optional[uuid.UUID] = None
    work_order_number: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    product_id: Optional[uuid.UUID] = None
    product_code: Optional[str] = None
    product_name: Optional[str] = None
    planned_qty: float
    started_qty: Optional[float] = None
    completed_qty: Optional[float] = None
    scrapped_qty: Optional[float] = None
    rework_qty: Optional[float] = None
    bom_revision: Optional[str] = None
    routing_revision: Optional[str] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    due_date: Optional[date] = None
    project_id: Optional[uuid.UUID] = None
    project_code: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesWorkOrderExecutionUpdate(BaseModel):
    execution_id: Optional[uuid.UUID] = None
    work_order_id: Optional[uuid.UUID] = None
    work_order_number: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    product_id: Optional[uuid.UUID] = None
    product_code: Optional[str] = None
    product_name: Optional[str] = None
    planned_qty: Optional[float] = None
    started_qty: Optional[float] = None
    completed_qty: Optional[float] = None
    scrapped_qty: Optional[float] = None
    rework_qty: Optional[float] = None
    bom_revision: Optional[str] = None
    routing_revision: Optional[str] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    due_date: Optional[date] = None
    project_id: Optional[uuid.UUID] = None
    project_code: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MesWorkOrderExecutionOut(BaseModel):
    execution_id: uuid.UUID
    work_order_id: Optional[uuid.UUID] = None
    work_order_number: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    product_id: Optional[uuid.UUID] = None
    product_code: Optional[str] = None
    product_name: Optional[str] = None
    planned_qty: float
    started_qty: Optional[float] = None
    completed_qty: Optional[float] = None
    scrapped_qty: Optional[float] = None
    rework_qty: Optional[float] = None
    bom_revision: Optional[str] = None
    routing_revision: Optional[str] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    due_date: Optional[date] = None
    project_id: Optional[uuid.UUID] = None
    project_code: Optional[str] = None
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

class MesWorkOrderHoldsCreate(BaseModel):
    hold_id: uuid.UUID
    execution_id: uuid.UUID
    hold_type: Optional[str] = None
    hold_reason: Optional[str] = None
    hold_date: Optional[datetime] = None
    released_date: Optional[datetime] = None
    held_by: Optional[uuid.UUID] = None
    released_by: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1

class MesWorkOrderHoldsUpdate(BaseModel):
    hold_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    hold_type: Optional[str] = None
    hold_reason: Optional[str] = None
    hold_date: Optional[datetime] = None
    released_date: Optional[datetime] = None
    held_by: Optional[uuid.UUID] = None
    released_by: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesWorkOrderHoldsOut(BaseModel):
    hold_id: uuid.UUID
    execution_id: uuid.UUID
    hold_type: Optional[str] = None
    hold_reason: Optional[str] = None
    hold_date: Optional[datetime] = None
    released_date: Optional[datetime] = None
    held_by: Optional[uuid.UUID] = None
    released_by: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesWorkOrderSignaturesCreate(BaseModel):
    signature_id: uuid.UUID
    execution_id: uuid.UUID
    signature_type: Optional[str] = None
    signed_by: Optional[uuid.UUID] = None
    signed_at: Optional[datetime] = None
    signature_data: Optional[str] = None
    remarks: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesWorkOrderSignaturesUpdate(BaseModel):
    signature_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    signature_type: Optional[str] = None
    signed_by: Optional[uuid.UUID] = None
    signed_at: Optional[datetime] = None
    signature_data: Optional[str] = None
    remarks: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesWorkOrderSignaturesOut(BaseModel):
    signature_id: uuid.UUID
    execution_id: uuid.UUID
    signature_type: Optional[str] = None
    signed_by: Optional[uuid.UUID] = None
    signed_at: Optional[datetime] = None
    signature_data: Optional[str] = None
    remarks: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesWorkflowDefinitionsCreate(BaseModel):
    workflow_id: uuid.UUID
    workflow_name: str
    workflow_type: Optional[str] = None
    nodes_json: Optional[dict] = None
    edges_json: Optional[dict] = None
    config_json: Optional[dict] = None
    version: Optional[int] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class MesWorkflowDefinitionsUpdate(BaseModel):
    workflow_id: Optional[uuid.UUID] = None
    workflow_name: Optional[str] = None
    workflow_type: Optional[str] = None
    nodes_json: Optional[dict] = None
    edges_json: Optional[dict] = None
    config_json: Optional[dict] = None
    version: Optional[int] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesWorkflowDefinitionsOut(BaseModel):
    workflow_id: uuid.UUID
    workflow_name: str
    workflow_type: Optional[str] = None
    nodes_json: Optional[dict] = None
    edges_json: Optional[dict] = None
    config_json: Optional[dict] = None
    version: Optional[int] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MesWorkflowExecutionsCreate(BaseModel):
    execution_id: uuid.UUID
    workflow_id: uuid.UUID
    status: Optional[str] = None
    state_json: Optional[dict] = None
    checkpoint_json: Optional[dict] = None
    inputs_json: Optional[dict] = None
    outputs_json: Optional[dict] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    execution_metrics: Optional[dict] = None
    is_active: bool = True
    object_version_number: int = 1

class MesWorkflowExecutionsUpdate(BaseModel):
    execution_id: Optional[uuid.UUID] = None
    workflow_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    state_json: Optional[dict] = None
    checkpoint_json: Optional[dict] = None
    inputs_json: Optional[dict] = None
    outputs_json: Optional[dict] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    execution_metrics: Optional[dict] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MesWorkflowExecutionsOut(BaseModel):
    execution_id: uuid.UUID
    workflow_id: uuid.UUID
    status: Optional[str] = None
    state_json: Optional[dict] = None
    checkpoint_json: Optional[dict] = None
    inputs_json: Optional[dict] = None
    outputs_json: Optional[dict] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    execution_metrics: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class WorkCentersCreate(BaseModel):
    work_center_id: uuid.UUID
    site_id: Optional[uuid.UUID] = None
    center_code: str
    center_name: str
    center_type: str
    iot_gateway_topic: Optional[str] = None
    status: Optional[str] = None

class WorkCentersUpdate(BaseModel):
    work_center_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    center_code: Optional[str] = None
    center_name: Optional[str] = None
    center_type: Optional[str] = None
    iot_gateway_topic: Optional[str] = None
    status: Optional[str] = None

class WorkCentersOut(BaseModel):
    work_center_id: uuid.UUID
    site_id: Optional[uuid.UUID] = None
    center_code: str
    center_name: str
    center_type: str
    iot_gateway_topic: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}
