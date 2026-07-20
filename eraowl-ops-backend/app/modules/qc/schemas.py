import uuid
from datetime import date, datetime, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class AiAgentLogsCreate(BaseModel):
    agent_log_id: int
    agent_name: str
    execution_id: Optional[str] = None
    llm_config_id: Optional[int] = None
    log_type_code: str
    log_level: Optional[str] = None
    message: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    token_usage_prompt: Optional[int] = None
    token_usage_completion: Optional[int] = None
    token_usage_total: Optional[int] = None
    cost: Optional[float] = None
    duration_ms: Optional[int] = None
    tool_calls: Optional[dict] = None
    reasoning_trace: Optional[dict] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AiAgentLogsUpdate(BaseModel):
    agent_log_id: Optional[int] = None
    agent_name: Optional[str] = None
    execution_id: Optional[str] = None
    llm_config_id: Optional[int] = None
    log_type_code: Optional[str] = None
    log_level: Optional[str] = None
    message: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    token_usage_prompt: Optional[int] = None
    token_usage_completion: Optional[int] = None
    token_usage_total: Optional[int] = None
    cost: Optional[float] = None
    duration_ms: Optional[int] = None
    tool_calls: Optional[dict] = None
    reasoning_trace: Optional[dict] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AiAgentLogsOut(BaseModel):
    agent_log_id: int
    agent_name: str
    execution_id: Optional[str] = None
    llm_config_id: Optional[int] = None
    log_type_code: str
    log_level: Optional[str] = None
    message: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    token_usage_prompt: Optional[int] = None
    token_usage_completion: Optional[int] = None
    token_usage_total: Optional[int] = None
    cost: Optional[float] = None
    duration_ms: Optional[int] = None
    tool_calls: Optional[dict] = None
    reasoning_trace: Optional[dict] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class AiDecisionsCreate(BaseModel):
    decision_id: int
    decision_code: str
    decision_type_code: str
    decision_source: Optional[str] = None
    execution_id: Optional[str] = None
    model_id: Optional[int] = None
    input_summary: Optional[dict] = None
    output_decision: Optional[dict] = None
    confidence_score: Optional[float] = None
    human_review_required: Optional[str] = None
    human_reviewer: Optional[str] = None
    human_review_date: Optional[datetime] = None
    human_override: Optional[str] = None
    decision_status_code: Optional[str] = None
    compliance_tags: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AiDecisionsUpdate(BaseModel):
    decision_id: Optional[int] = None
    decision_code: Optional[str] = None
    decision_type_code: Optional[str] = None
    decision_source: Optional[str] = None
    execution_id: Optional[str] = None
    model_id: Optional[int] = None
    input_summary: Optional[dict] = None
    output_decision: Optional[dict] = None
    confidence_score: Optional[float] = None
    human_review_required: Optional[str] = None
    human_reviewer: Optional[str] = None
    human_review_date: Optional[datetime] = None
    human_override: Optional[str] = None
    decision_status_code: Optional[str] = None
    compliance_tags: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AiDecisionsOut(BaseModel):
    decision_id: int
    decision_code: str
    decision_type_code: str
    decision_source: Optional[str] = None
    execution_id: Optional[str] = None
    model_id: Optional[int] = None
    input_summary: Optional[dict] = None
    output_decision: Optional[dict] = None
    confidence_score: Optional[float] = None
    human_review_required: Optional[str] = None
    human_reviewer: Optional[str] = None
    human_review_date: Optional[datetime] = None
    human_override: Optional[str] = None
    decision_status_code: Optional[str] = None
    compliance_tags: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class AiModelRegistryCreate(BaseModel):
    registry_id: int
    model_code: str
    model_name: str
    model_type_code: str
    model_framework_code: Optional[str] = None
    model_version: str
    model_stage: Optional[str] = None
    model_status_code: Optional[str] = None
    model_artifact_url: Optional[str] = None
    model_card: Optional[dict] = None
    training_metrics: Optional[dict] = None
    validation_metrics: Optional[dict] = None
    fairness_metrics: Optional[dict] = None
    bias_assessment: Optional[dict] = None
    explainability_report: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AiModelRegistryUpdate(BaseModel):
    registry_id: Optional[int] = None
    model_code: Optional[str] = None
    model_name: Optional[str] = None
    model_type_code: Optional[str] = None
    model_framework_code: Optional[str] = None
    model_version: Optional[str] = None
    model_stage: Optional[str] = None
    model_status_code: Optional[str] = None
    model_artifact_url: Optional[str] = None
    model_card: Optional[dict] = None
    training_metrics: Optional[dict] = None
    validation_metrics: Optional[dict] = None
    fairness_metrics: Optional[dict] = None
    bias_assessment: Optional[dict] = None
    explainability_report: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AiModelRegistryOut(BaseModel):
    registry_id: int
    model_code: str
    model_name: str
    model_type_code: str
    model_framework_code: Optional[str] = None
    model_version: str
    model_stage: Optional[str] = None
    model_status_code: Optional[str] = None
    model_artifact_url: Optional[str] = None
    model_card: Optional[dict] = None
    training_metrics: Optional[dict] = None
    validation_metrics: Optional[dict] = None
    fairness_metrics: Optional[dict] = None
    bias_assessment: Optional[dict] = None
    explainability_report: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class AiWorkflowStateCreate(BaseModel):
    workflow_state_id: int
    workflow_name: str
    execution_id: str
    workflow_type_code: Optional[str] = None
    state_data: dict
    current_step: Optional[str] = None
    workflow_status_code: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_info: Optional[dict] = None
    meta_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AiWorkflowStateUpdate(BaseModel):
    workflow_state_id: Optional[int] = None
    workflow_name: Optional[str] = None
    execution_id: Optional[str] = None
    workflow_type_code: Optional[str] = None
    state_data: Optional[dict] = None
    current_step: Optional[str] = None
    workflow_status_code: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_info: Optional[dict] = None
    meta_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AiWorkflowStateOut(BaseModel):
    workflow_state_id: int
    workflow_name: str
    execution_id: str
    workflow_type_code: Optional[str] = None
    state_data: dict
    current_step: Optional[str] = None
    workflow_status_code: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_info: Optional[dict] = None
    meta_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class InspectionChecklistCreate(BaseModel):
    item_check_id: uuid.UUID
    plan_id: uuid.UUID
    parameter_name: str
    test_method: Optional[str] = None
    uom_code: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    expected_text: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InspectionChecklistUpdate(BaseModel):
    item_check_id: Optional[uuid.UUID] = None
    plan_id: Optional[uuid.UUID] = None
    parameter_name: Optional[str] = None
    test_method: Optional[str] = None
    uom_code: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    expected_text: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InspectionChecklistOut(BaseModel):
    item_check_id: uuid.UUID
    plan_id: uuid.UUID
    parameter_name: str
    test_method: Optional[str] = None
    uom_code: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    expected_text: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class InspectionOrdersCreate(BaseModel):
    inspection_id: uuid.UUID
    company_id: Optional[uuid.UUID] = None
    plan_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    inspector_id: Optional[uuid.UUID] = None
    source_type: str
    source_line_id: uuid.UUID
    lot_number: Optional[str] = None
    total_qty: float
    sample_qty: float
    status: Optional[str] = None
    disposition: Optional[str] = None
    decision_reason: Optional[str] = None
    inspected_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InspectionOrdersUpdate(BaseModel):
    inspection_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    plan_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    inspector_id: Optional[uuid.UUID] = None
    source_type: Optional[str] = None
    source_line_id: Optional[uuid.UUID] = None
    lot_number: Optional[str] = None
    total_qty: Optional[float] = None
    sample_qty: Optional[float] = None
    status: Optional[str] = None
    disposition: Optional[str] = None
    decision_reason: Optional[str] = None
    inspected_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InspectionOrdersOut(BaseModel):
    inspection_id: uuid.UUID
    company_id: Optional[uuid.UUID] = None
    plan_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    inspector_id: Optional[uuid.UUID] = None
    source_type: str
    source_line_id: uuid.UUID
    lot_number: Optional[str] = None
    total_qty: float
    sample_qty: float
    status: Optional[str] = None
    disposition: Optional[str] = None
    decision_reason: Optional[str] = None
    inspected_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class InspectionPlansCreate(BaseModel):
    plan_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    plan_name: str
    version: Optional[str] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InspectionPlansUpdate(BaseModel):
    plan_id: Optional[uuid.UUID] = None
    item_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    plan_name: Optional[str] = None
    version: Optional[str] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InspectionPlansOut(BaseModel):
    plan_id: uuid.UUID
    item_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    plan_name: str
    version: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class InspectionResultsCreate(BaseModel):
    result_line_id: uuid.UUID
    inspection_id: uuid.UUID
    item_check_id: uuid.UUID
    actual_value: Optional[float] = None
    actual_text: Optional[str] = None
    is_ok: bool
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InspectionResultsUpdate(BaseModel):
    result_line_id: Optional[uuid.UUID] = None
    inspection_id: Optional[uuid.UUID] = None
    item_check_id: Optional[uuid.UUID] = None
    actual_value: Optional[float] = None
    actual_text: Optional[str] = None
    is_ok: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InspectionResultsOut(BaseModel):
    result_line_id: uuid.UUID
    inspection_id: uuid.UUID
    item_check_id: uuid.UUID
    actual_value: Optional[float] = None
    actual_text: Optional[str] = None
    is_ok: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcAgentDefinitionsCreate(BaseModel):
    agent_definition_id: int
    agent_code: str
    agent_name: str
    agent_type_code: str
    agent_version: Optional[str] = None
    agent_status_code: Optional[str] = None
    llm_config_id: Optional[int] = None
    system_prompt: Optional[str] = None
    tools: Optional[dict] = None
    memory_config: Optional[dict] = None
    max_iterations: Optional[int] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcAgentDefinitionsUpdate(BaseModel):
    agent_definition_id: Optional[int] = None
    agent_code: Optional[str] = None
    agent_name: Optional[str] = None
    agent_type_code: Optional[str] = None
    agent_version: Optional[str] = None
    agent_status_code: Optional[str] = None
    llm_config_id: Optional[int] = None
    system_prompt: Optional[str] = None
    tools: Optional[dict] = None
    memory_config: Optional[dict] = None
    max_iterations: Optional[int] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcAgentDefinitionsOut(BaseModel):
    agent_definition_id: int
    agent_code: str
    agent_name: str
    agent_type_code: str
    agent_version: Optional[str] = None
    agent_status_code: Optional[str] = None
    llm_config_id: Optional[int] = None
    system_prompt: Optional[str] = None
    tools: Optional[dict] = None
    memory_config: Optional[dict] = None
    max_iterations: Optional[int] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcAlgorithmsCreate(BaseModel):
    algorithm_id: int
    algorithm_code: str
    algorithm_name: str
    algorithm_type_code: str
    algorithm_version: Optional[str] = None
    algorithm_status_code: Optional[str] = None
    description: Optional[str] = None
    input_schema: Optional[dict] = None
    output_schema: Optional[dict] = None
    configuration: Optional[dict] = None
    performance_metrics: Optional[dict] = None
    documentation_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcAlgorithmsUpdate(BaseModel):
    algorithm_id: Optional[int] = None
    algorithm_code: Optional[str] = None
    algorithm_name: Optional[str] = None
    algorithm_type_code: Optional[str] = None
    algorithm_version: Optional[str] = None
    algorithm_status_code: Optional[str] = None
    description: Optional[str] = None
    input_schema: Optional[dict] = None
    output_schema: Optional[dict] = None
    configuration: Optional[dict] = None
    performance_metrics: Optional[dict] = None
    documentation_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcAlgorithmsOut(BaseModel):
    algorithm_id: int
    algorithm_code: str
    algorithm_name: str
    algorithm_type_code: str
    algorithm_version: Optional[str] = None
    algorithm_status_code: Optional[str] = None
    description: Optional[str] = None
    input_schema: Optional[dict] = None
    output_schema: Optional[dict] = None
    configuration: Optional[dict] = None
    performance_metrics: Optional[dict] = None
    documentation_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcAuditFindingsCreate(BaseModel):
    audit_finding_id: int
    audit_id: int
    finding_number: str
    finding_type_code: str
    finding_severity_code: str
    finding_status_code: Optional[str] = None
    description: str
    criteria_reference: Optional[str] = None
    evidence: Optional[str] = None
    root_cause: Optional[str] = None
    corrective_action_plan: Optional[str] = None
    assigned_to: Optional[str] = None
    due_date: Optional[date] = None
    verification_method: Optional[str] = None
    verification_date: Optional[datetime] = None
    verified_by: Optional[str] = None
    closed_date: Optional[datetime] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcAuditFindingsUpdate(BaseModel):
    audit_finding_id: Optional[int] = None
    audit_id: Optional[int] = None
    finding_number: Optional[str] = None
    finding_type_code: Optional[str] = None
    finding_severity_code: Optional[str] = None
    finding_status_code: Optional[str] = None
    description: Optional[str] = None
    criteria_reference: Optional[str] = None
    evidence: Optional[str] = None
    root_cause: Optional[str] = None
    corrective_action_plan: Optional[str] = None
    assigned_to: Optional[str] = None
    due_date: Optional[date] = None
    verification_method: Optional[str] = None
    verification_date: Optional[datetime] = None
    verified_by: Optional[str] = None
    closed_date: Optional[datetime] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcAuditFindingsOut(BaseModel):
    audit_finding_id: int
    audit_id: int
    finding_number: str
    finding_type_code: str
    finding_severity_code: str
    finding_status_code: Optional[str] = None
    description: str
    criteria_reference: Optional[str] = None
    evidence: Optional[str] = None
    root_cause: Optional[str] = None
    corrective_action_plan: Optional[str] = None
    assigned_to: Optional[str] = None
    due_date: Optional[date] = None
    verification_method: Optional[str] = None
    verification_date: Optional[datetime] = None
    verified_by: Optional[str] = None
    closed_date: Optional[datetime] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcAuditsCreate(BaseModel):
    audit_id: int
    audit_number: str
    audit_title: str
    audit_type_code: str
    audit_standard_code: Optional[str] = None
    audit_status_code: str
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    scope_description: Optional[str] = None
    criteria_reference: Optional[str] = None
    lead_auditor_id: Optional[int] = None
    lead_auditor_name: Optional[str] = None
    audit_team: Optional[dict] = None
    planned_start_date: Optional[date] = None
    planned_end_date: Optional[date] = None
    actual_start_date: Optional[datetime] = None
    actual_end_date: Optional[datetime] = None
    overall_score: Optional[float] = None
    conclusion: Optional[str] = None
    recommendation: Optional[str] = None
    finding_count_critical: Optional[int] = None
    finding_count_major: Optional[int] = None
    finding_count_minor: Optional[int] = None
    finding_count_observation: Optional[int] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcAuditsUpdate(BaseModel):
    audit_id: Optional[int] = None
    audit_number: Optional[str] = None
    audit_title: Optional[str] = None
    audit_type_code: Optional[str] = None
    audit_standard_code: Optional[str] = None
    audit_status_code: Optional[str] = None
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    scope_description: Optional[str] = None
    criteria_reference: Optional[str] = None
    lead_auditor_id: Optional[int] = None
    lead_auditor_name: Optional[str] = None
    audit_team: Optional[dict] = None
    planned_start_date: Optional[date] = None
    planned_end_date: Optional[date] = None
    actual_start_date: Optional[datetime] = None
    actual_end_date: Optional[datetime] = None
    overall_score: Optional[float] = None
    conclusion: Optional[str] = None
    recommendation: Optional[str] = None
    finding_count_critical: Optional[int] = None
    finding_count_major: Optional[int] = None
    finding_count_minor: Optional[int] = None
    finding_count_observation: Optional[int] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcAuditsOut(BaseModel):
    audit_id: int
    audit_number: str
    audit_title: str
    audit_type_code: str
    audit_standard_code: Optional[str] = None
    audit_status_code: str
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    scope_description: Optional[str] = None
    criteria_reference: Optional[str] = None
    lead_auditor_id: Optional[int] = None
    lead_auditor_name: Optional[str] = None
    audit_team: Optional[dict] = None
    planned_start_date: Optional[date] = None
    planned_end_date: Optional[date] = None
    actual_start_date: Optional[datetime] = None
    actual_end_date: Optional[datetime] = None
    overall_score: Optional[float] = None
    conclusion: Optional[str] = None
    recommendation: Optional[str] = None
    finding_count_critical: Optional[int] = None
    finding_count_major: Optional[int] = None
    finding_count_minor: Optional[int] = None
    finding_count_observation: Optional[int] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcCapaActionsCreate(BaseModel):
    capa_action_id: int
    capa_id: int
    action_sequence: int
    action_type_code: Optional[str] = None
    action_description: str
    assigned_to: Optional[str] = None
    target_date: Optional[date] = None
    completed_date: Optional[datetime] = None
    action_status_code: Optional[str] = None
    completion_notes: Optional[str] = None
    effectiveness_score: Optional[int] = None
    attachment_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcCapaActionsUpdate(BaseModel):
    capa_action_id: Optional[int] = None
    capa_id: Optional[int] = None
    action_sequence: Optional[int] = None
    action_type_code: Optional[str] = None
    action_description: Optional[str] = None
    assigned_to: Optional[str] = None
    target_date: Optional[date] = None
    completed_date: Optional[datetime] = None
    action_status_code: Optional[str] = None
    completion_notes: Optional[str] = None
    effectiveness_score: Optional[int] = None
    attachment_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcCapaActionsOut(BaseModel):
    capa_action_id: int
    capa_id: int
    action_sequence: int
    action_type_code: Optional[str] = None
    action_description: str
    assigned_to: Optional[str] = None
    target_date: Optional[date] = None
    completed_date: Optional[datetime] = None
    action_status_code: Optional[str] = None
    completion_notes: Optional[str] = None
    effectiveness_score: Optional[int] = None
    attachment_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcCapaHeadersCreate(BaseModel):
    capa_id: int
    capa_number: str
    capa_title: str
    capa_type_code: str
    capa_source_code: Optional[str] = None
    source_ncr_id: Optional[int] = None
    source_audit_id: Optional[int] = None
    source_complaint_id: Optional[int] = None
    source_document_id: Optional[int] = None
    source_reference: Optional[str] = None
    capa_priority_code: Optional[str] = None
    capa_status_code: str
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    root_cause_analysis_id: Optional[int] = None
    root_cause_summary: Optional[str] = None
    problem_description: Optional[str] = None
    requested_by: Optional[str] = None
    requested_date: Optional[datetime] = None
    assigned_to: Optional[str] = None
    assigned_date: Optional[datetime] = None
    due_date: Optional[date] = None
    effectiveness_review_date: Optional[date] = None
    effectiveness_result: Optional[str] = None
    is_effective: Optional[str] = None
    closure_notes: Optional[str] = None
    closed_date: Optional[datetime] = None
    closed_by: Optional[str] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcCapaHeadersUpdate(BaseModel):
    capa_id: Optional[int] = None
    capa_number: Optional[str] = None
    capa_title: Optional[str] = None
    capa_type_code: Optional[str] = None
    capa_source_code: Optional[str] = None
    source_ncr_id: Optional[int] = None
    source_audit_id: Optional[int] = None
    source_complaint_id: Optional[int] = None
    source_document_id: Optional[int] = None
    source_reference: Optional[str] = None
    capa_priority_code: Optional[str] = None
    capa_status_code: Optional[str] = None
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    root_cause_analysis_id: Optional[int] = None
    root_cause_summary: Optional[str] = None
    problem_description: Optional[str] = None
    requested_by: Optional[str] = None
    requested_date: Optional[datetime] = None
    assigned_to: Optional[str] = None
    assigned_date: Optional[datetime] = None
    due_date: Optional[date] = None
    effectiveness_review_date: Optional[date] = None
    effectiveness_result: Optional[str] = None
    is_effective: Optional[str] = None
    closure_notes: Optional[str] = None
    closed_date: Optional[datetime] = None
    closed_by: Optional[str] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcCapaHeadersOut(BaseModel):
    capa_id: int
    capa_number: str
    capa_title: str
    capa_type_code: str
    capa_source_code: Optional[str] = None
    source_ncr_id: Optional[int] = None
    source_audit_id: Optional[int] = None
    source_complaint_id: Optional[int] = None
    source_document_id: Optional[int] = None
    source_reference: Optional[str] = None
    capa_priority_code: Optional[str] = None
    capa_status_code: str
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    root_cause_analysis_id: Optional[int] = None
    root_cause_summary: Optional[str] = None
    problem_description: Optional[str] = None
    requested_by: Optional[str] = None
    requested_date: Optional[datetime] = None
    assigned_to: Optional[str] = None
    assigned_date: Optional[datetime] = None
    due_date: Optional[date] = None
    effectiveness_review_date: Optional[date] = None
    effectiveness_result: Optional[str] = None
    is_effective: Optional[str] = None
    closure_notes: Optional[str] = None
    closed_date: Optional[datetime] = None
    closed_by: Optional[str] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcCharacteristicValueSetsCreate(BaseModel):
    value_set_id: int
    characteristic_id: int
    value_code: str
    value_name: Optional[str] = None
    display_sequence: Optional[int] = None
    is_default: Optional[str] = None
    enabled_flag: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcCharacteristicValueSetsUpdate(BaseModel):
    value_set_id: Optional[int] = None
    characteristic_id: Optional[int] = None
    value_code: Optional[str] = None
    value_name: Optional[str] = None
    display_sequence: Optional[int] = None
    is_default: Optional[str] = None
    enabled_flag: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcCharacteristicValueSetsOut(BaseModel):
    value_set_id: int
    characteristic_id: int
    value_code: str
    value_name: Optional[str] = None
    display_sequence: Optional[int] = None
    is_default: Optional[str] = None
    enabled_flag: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcCharacteristicsCreate(BaseModel):
    characteristic_id: int
    characteristic_code: str
    characteristic_name: str
    characteristic_type_code: str
    data_type_code: str
    uom_code: Optional[str] = None
    precision_decimal: Optional[int] = None
    display_sequence: Optional[int] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    regex_pattern: Optional[str] = None
    default_value: Optional[str] = None
    help_text: Optional[str] = None
    is_required: Optional[str] = None
    is_calculated: Optional[str] = None
    formula: Optional[str] = None
    parent_characteristic_id: Optional[int] = None
    conditional_visibility: Optional[dict] = None
    security_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcCharacteristicsUpdate(BaseModel):
    characteristic_id: Optional[int] = None
    characteristic_code: Optional[str] = None
    characteristic_name: Optional[str] = None
    characteristic_type_code: Optional[str] = None
    data_type_code: Optional[str] = None
    uom_code: Optional[str] = None
    precision_decimal: Optional[int] = None
    display_sequence: Optional[int] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    regex_pattern: Optional[str] = None
    default_value: Optional[str] = None
    help_text: Optional[str] = None
    is_required: Optional[str] = None
    is_calculated: Optional[str] = None
    formula: Optional[str] = None
    parent_characteristic_id: Optional[int] = None
    conditional_visibility: Optional[dict] = None
    security_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcCharacteristicsOut(BaseModel):
    characteristic_id: int
    characteristic_code: str
    characteristic_name: str
    characteristic_type_code: str
    data_type_code: str
    uom_code: Optional[str] = None
    precision_decimal: Optional[int] = None
    display_sequence: Optional[int] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    regex_pattern: Optional[str] = None
    default_value: Optional[str] = None
    help_text: Optional[str] = None
    is_required: Optional[str] = None
    is_calculated: Optional[str] = None
    formula: Optional[str] = None
    parent_characteristic_id: Optional[int] = None
    conditional_visibility: Optional[dict] = None
    security_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcComplaintInvestigationsCreate(BaseModel):
    investigation_id: int
    complaint_id: int
    investigation_type_code: Optional[str] = None
    investigator: Optional[str] = None
    investigation_date: Optional[datetime] = None
    findings: Optional[str] = None
    root_cause_analysis_id: Optional[int] = None
    action_taken: Optional[str] = None
    customer_communication: Optional[str] = None
    follow_up_required: Optional[str] = None
    follow_up_date: Optional[date] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcComplaintInvestigationsUpdate(BaseModel):
    investigation_id: Optional[int] = None
    complaint_id: Optional[int] = None
    investigation_type_code: Optional[str] = None
    investigator: Optional[str] = None
    investigation_date: Optional[datetime] = None
    findings: Optional[str] = None
    root_cause_analysis_id: Optional[int] = None
    action_taken: Optional[str] = None
    customer_communication: Optional[str] = None
    follow_up_required: Optional[str] = None
    follow_up_date: Optional[date] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcComplaintInvestigationsOut(BaseModel):
    investigation_id: int
    complaint_id: int
    investigation_type_code: Optional[str] = None
    investigator: Optional[str] = None
    investigation_date: Optional[datetime] = None
    findings: Optional[str] = None
    root_cause_analysis_id: Optional[int] = None
    action_taken: Optional[str] = None
    customer_communication: Optional[str] = None
    follow_up_required: Optional[str] = None
    follow_up_date: Optional[date] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcControlPlanCharacteristicsCreate(BaseModel):
    cp_characteristic_id: int
    control_plan_id: int
    characteristic_id: int
    spec_id: Optional[int] = None
    operation_code: Optional[str] = None
    process_step_code: Optional[str] = None
    characteristic_type_code: Optional[str] = None
    measurement_technique: Optional[str] = None
    sample_size: Optional[int] = None
    sampling_frequency: Optional[str] = None
    control_method: Optional[str] = None
    reaction_plan: Optional[str] = None
    responsible_party: Optional[str] = None
    document_reference: Optional[str] = None
    sequence_number: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcControlPlanCharacteristicsUpdate(BaseModel):
    cp_characteristic_id: Optional[int] = None
    control_plan_id: Optional[int] = None
    characteristic_id: Optional[int] = None
    spec_id: Optional[int] = None
    operation_code: Optional[str] = None
    process_step_code: Optional[str] = None
    characteristic_type_code: Optional[str] = None
    measurement_technique: Optional[str] = None
    sample_size: Optional[int] = None
    sampling_frequency: Optional[str] = None
    control_method: Optional[str] = None
    reaction_plan: Optional[str] = None
    responsible_party: Optional[str] = None
    document_reference: Optional[str] = None
    sequence_number: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcControlPlanCharacteristicsOut(BaseModel):
    cp_characteristic_id: int
    control_plan_id: int
    characteristic_id: int
    spec_id: Optional[int] = None
    operation_code: Optional[str] = None
    process_step_code: Optional[str] = None
    characteristic_type_code: Optional[str] = None
    measurement_technique: Optional[str] = None
    sample_size: Optional[int] = None
    sampling_frequency: Optional[str] = None
    control_method: Optional[str] = None
    reaction_plan: Optional[str] = None
    responsible_party: Optional[str] = None
    document_reference: Optional[str] = None
    sequence_number: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcControlPlansCreate(BaseModel):
    control_plan_id: int
    control_plan_number: str
    control_plan_title: str
    control_plan_type_code: str
    control_plan_version: Optional[str] = None
    control_plan_status: Optional[str] = None
    item_id: Optional[int] = None
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    process_code: Optional[str] = None
    fmea_id: Optional[int] = None
    revision_number: Optional[str] = None
    prepared_by: Optional[str] = None
    prepared_date: Optional[date] = None
    approved_by: Optional[str] = None
    approved_date: Optional[date] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcControlPlansUpdate(BaseModel):
    control_plan_id: Optional[int] = None
    control_plan_number: Optional[str] = None
    control_plan_title: Optional[str] = None
    control_plan_type_code: Optional[str] = None
    control_plan_version: Optional[str] = None
    control_plan_status: Optional[str] = None
    item_id: Optional[int] = None
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    process_code: Optional[str] = None
    fmea_id: Optional[int] = None
    revision_number: Optional[str] = None
    prepared_by: Optional[str] = None
    prepared_date: Optional[date] = None
    approved_by: Optional[str] = None
    approved_date: Optional[date] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcControlPlansOut(BaseModel):
    control_plan_id: int
    control_plan_number: str
    control_plan_title: str
    control_plan_type_code: str
    control_plan_version: Optional[str] = None
    control_plan_status: Optional[str] = None
    item_id: Optional[int] = None
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    process_code: Optional[str] = None
    fmea_id: Optional[int] = None
    revision_number: Optional[str] = None
    prepared_by: Optional[str] = None
    prepared_date: Optional[date] = None
    approved_by: Optional[str] = None
    approved_date: Optional[date] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcCostOfQualityCreate(BaseModel):
    coq_id: int
    coq_number: str
    coq_category_code: str
    coq_item_code: str
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    product_line_code: Optional[str] = None
    project_code: Optional[str] = None
    transaction_date: datetime
    amount: float
    currency_code: Optional[str] = None
    quantity: Optional[float] = None
    uom_code: Optional[str] = None
    source_type_code: Optional[str] = None
    source_id: Optional[int] = None
    gl_account_id: Optional[int] = None
    description: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcCostOfQualityUpdate(BaseModel):
    coq_id: Optional[int] = None
    coq_number: Optional[str] = None
    coq_category_code: Optional[str] = None
    coq_item_code: Optional[str] = None
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    product_line_code: Optional[str] = None
    project_code: Optional[str] = None
    transaction_date: Optional[datetime] = None
    amount: Optional[float] = None
    currency_code: Optional[str] = None
    quantity: Optional[float] = None
    uom_code: Optional[str] = None
    source_type_code: Optional[str] = None
    source_id: Optional[int] = None
    gl_account_id: Optional[int] = None
    description: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcCostOfQualityOut(BaseModel):
    coq_id: int
    coq_number: str
    coq_category_code: str
    coq_item_code: str
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    product_line_code: Optional[str] = None
    project_code: Optional[str] = None
    transaction_date: datetime
    amount: float
    currency_code: Optional[str] = None
    quantity: Optional[float] = None
    uom_code: Optional[str] = None
    source_type_code: Optional[str] = None
    source_id: Optional[int] = None
    gl_account_id: Optional[int] = None
    description: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcCustomerComplaintsCreate(BaseModel):
    complaint_id: int
    complaint_number: str
    complaint_title: Optional[str] = None
    complaint_type_code: str
    complaint_severity_code: str
    complaint_status_code: str
    customer_id: Optional[int] = None
    customer_name: Optional[str] = None
    customer_contact: Optional[str] = None
    order_id: Optional[int] = None
    order_line_id: Optional[int] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    quantity_affected: Optional[float] = None
    complaint_date: datetime
    received_date: Optional[datetime] = None
    response_required_date: Optional[date] = None
    description: Optional[str] = None
    investigation_summary: Optional[str] = None
    root_cause_summary: Optional[str] = None
    customer_response: Optional[str] = None
    rma_number: Optional[str] = None
    return_quantity: Optional[float] = None
    ncr_id: Optional[int] = None
    capa_id: Optional[int] = None
    assigned_to: Optional[str] = None
    due_date: Optional[date] = None
    closed_date: Optional[datetime] = None
    closed_by: Optional[str] = None
    recurrence_count: Optional[int] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcCustomerComplaintsUpdate(BaseModel):
    complaint_id: Optional[int] = None
    complaint_number: Optional[str] = None
    complaint_title: Optional[str] = None
    complaint_type_code: Optional[str] = None
    complaint_severity_code: Optional[str] = None
    complaint_status_code: Optional[str] = None
    customer_id: Optional[int] = None
    customer_name: Optional[str] = None
    customer_contact: Optional[str] = None
    order_id: Optional[int] = None
    order_line_id: Optional[int] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    quantity_affected: Optional[float] = None
    complaint_date: Optional[datetime] = None
    received_date: Optional[datetime] = None
    response_required_date: Optional[date] = None
    description: Optional[str] = None
    investigation_summary: Optional[str] = None
    root_cause_summary: Optional[str] = None
    customer_response: Optional[str] = None
    rma_number: Optional[str] = None
    return_quantity: Optional[float] = None
    ncr_id: Optional[int] = None
    capa_id: Optional[int] = None
    assigned_to: Optional[str] = None
    due_date: Optional[date] = None
    closed_date: Optional[datetime] = None
    closed_by: Optional[str] = None
    recurrence_count: Optional[int] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcCustomerComplaintsOut(BaseModel):
    complaint_id: int
    complaint_number: str
    complaint_title: Optional[str] = None
    complaint_type_code: str
    complaint_severity_code: str
    complaint_status_code: str
    customer_id: Optional[int] = None
    customer_name: Optional[str] = None
    customer_contact: Optional[str] = None
    order_id: Optional[int] = None
    order_line_id: Optional[int] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    quantity_affected: Optional[float] = None
    complaint_date: datetime
    received_date: Optional[datetime] = None
    response_required_date: Optional[date] = None
    description: Optional[str] = None
    investigation_summary: Optional[str] = None
    root_cause_summary: Optional[str] = None
    customer_response: Optional[str] = None
    rma_number: Optional[str] = None
    return_quantity: Optional[float] = None
    ncr_id: Optional[int] = None
    capa_id: Optional[int] = None
    assigned_to: Optional[str] = None
    due_date: Optional[date] = None
    closed_date: Optional[datetime] = None
    closed_by: Optional[str] = None
    recurrence_count: Optional[int] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcDefectMasterCreate(BaseModel):
    defect_id: int
    defect_code: str
    defect_name: str
    defect_type_code: str
    defect_severity_code: Optional[str] = None
    defect_category_code: Optional[str] = None
    description: Optional[str] = None
    is_visible_inspector: Optional[str] = None
    requires_containment: Optional[str] = None
    default_disposition: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcDefectMasterUpdate(BaseModel):
    defect_id: Optional[int] = None
    defect_code: Optional[str] = None
    defect_name: Optional[str] = None
    defect_type_code: Optional[str] = None
    defect_severity_code: Optional[str] = None
    defect_category_code: Optional[str] = None
    description: Optional[str] = None
    is_visible_inspector: Optional[str] = None
    requires_containment: Optional[str] = None
    default_disposition: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcDefectMasterOut(BaseModel):
    defect_id: int
    defect_code: str
    defect_name: str
    defect_type_code: str
    defect_severity_code: Optional[str] = None
    defect_category_code: Optional[str] = None
    description: Optional[str] = None
    is_visible_inspector: Optional[str] = None
    requires_containment: Optional[str] = None
    default_disposition: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcDefectOccurrencesCreate(BaseModel):
    defect_occurrence_id: int
    defect_id: int
    inspection_id: Optional[int] = None
    test_result_line_id: Optional[int] = None
    ncr_id: Optional[int] = None
    complaint_id: Optional[int] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    quantity: Optional[float] = None
    occurrence_date: datetime
    defect_cost: Optional[float] = None
    operator_id: Optional[int] = None
    shift_code: Optional[str] = None
    machine_id: Optional[int] = None
    process_step_code: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcDefectOccurrencesUpdate(BaseModel):
    defect_occurrence_id: Optional[int] = None
    defect_id: Optional[int] = None
    inspection_id: Optional[int] = None
    test_result_line_id: Optional[int] = None
    ncr_id: Optional[int] = None
    complaint_id: Optional[int] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    quantity: Optional[float] = None
    occurrence_date: Optional[datetime] = None
    defect_cost: Optional[float] = None
    operator_id: Optional[int] = None
    shift_code: Optional[str] = None
    machine_id: Optional[int] = None
    process_step_code: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcDefectOccurrencesOut(BaseModel):
    defect_occurrence_id: int
    defect_id: int
    inspection_id: Optional[int] = None
    test_result_line_id: Optional[int] = None
    ncr_id: Optional[int] = None
    complaint_id: Optional[int] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    quantity: Optional[float] = None
    occurrence_date: datetime
    defect_cost: Optional[float] = None
    operator_id: Optional[int] = None
    shift_code: Optional[str] = None
    machine_id: Optional[int] = None
    process_step_code: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcDocumentsCreate(BaseModel):
    document_id: int
    document_number: str
    document_title: str
    document_type_code: str
    document_status_code: Optional[str] = None
    document_version: Optional[str] = None
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    author_id: Optional[int] = None
    author_name: Optional[str] = None
    owner_id: Optional[int] = None
    owner_name: Optional[str] = None
    keywords: Optional[str] = None
    effective_date: Optional[date] = None
    review_date: Optional[date] = None
    review_cycle_days: Optional[int] = None
    obsolete_date: Optional[date] = None
    security_class_code: Optional[str] = None
    requires_training: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcDocumentsUpdate(BaseModel):
    document_id: Optional[int] = None
    document_number: Optional[str] = None
    document_title: Optional[str] = None
    document_type_code: Optional[str] = None
    document_status_code: Optional[str] = None
    document_version: Optional[str] = None
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    author_id: Optional[int] = None
    author_name: Optional[str] = None
    owner_id: Optional[int] = None
    owner_name: Optional[str] = None
    keywords: Optional[str] = None
    effective_date: Optional[date] = None
    review_date: Optional[date] = None
    review_cycle_days: Optional[int] = None
    obsolete_date: Optional[date] = None
    security_class_code: Optional[str] = None
    requires_training: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcDocumentsOut(BaseModel):
    document_id: int
    document_number: str
    document_title: str
    document_type_code: str
    document_status_code: Optional[str] = None
    document_version: Optional[str] = None
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    author_id: Optional[int] = None
    author_name: Optional[str] = None
    owner_id: Optional[int] = None
    owner_name: Optional[str] = None
    keywords: Optional[str] = None
    effective_date: Optional[date] = None
    review_date: Optional[date] = None
    review_cycle_days: Optional[int] = None
    obsolete_date: Optional[date] = None
    security_class_code: Optional[str] = None
    requires_training: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcEquipmentCalibrationCreate(BaseModel):
    calibration_id: int
    equipment_id: int
    calibration_number: str
    calibration_type_code: Optional[str] = None
    calibration_status_code: Optional[str] = None
    calibration_date: datetime
    calibrated_by: Optional[str] = None
    technician_id: Optional[int] = None
    calibration_lab: Optional[str] = None
    calibration_location: Optional[str] = None
    standard_used_id: Optional[int] = None
    standard_traceability: Optional[str] = None
    as_found_value: Optional[float] = None
    as_left_value: Optional[float] = None
    uncertainty: Optional[float] = None
    is_in_tolerance: Optional[str] = None
    certificate_number: Optional[str] = None
    certificate_file_url: Optional[str] = None
    certificate_expiry_date: Optional[date] = None
    next_calibration_due: Optional[date] = None
    environment_temp: Optional[float] = None
    environment_humidity: Optional[float] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcEquipmentCalibrationUpdate(BaseModel):
    calibration_id: Optional[int] = None
    equipment_id: Optional[int] = None
    calibration_number: Optional[str] = None
    calibration_type_code: Optional[str] = None
    calibration_status_code: Optional[str] = None
    calibration_date: Optional[datetime] = None
    calibrated_by: Optional[str] = None
    technician_id: Optional[int] = None
    calibration_lab: Optional[str] = None
    calibration_location: Optional[str] = None
    standard_used_id: Optional[int] = None
    standard_traceability: Optional[str] = None
    as_found_value: Optional[float] = None
    as_left_value: Optional[float] = None
    uncertainty: Optional[float] = None
    is_in_tolerance: Optional[str] = None
    certificate_number: Optional[str] = None
    certificate_file_url: Optional[str] = None
    certificate_expiry_date: Optional[date] = None
    next_calibration_due: Optional[date] = None
    environment_temp: Optional[float] = None
    environment_humidity: Optional[float] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcEquipmentCalibrationOut(BaseModel):
    calibration_id: int
    equipment_id: int
    calibration_number: str
    calibration_type_code: Optional[str] = None
    calibration_status_code: Optional[str] = None
    calibration_date: datetime
    calibrated_by: Optional[str] = None
    technician_id: Optional[int] = None
    calibration_lab: Optional[str] = None
    calibration_location: Optional[str] = None
    standard_used_id: Optional[int] = None
    standard_traceability: Optional[str] = None
    as_found_value: Optional[float] = None
    as_left_value: Optional[float] = None
    uncertainty: Optional[float] = None
    is_in_tolerance: Optional[str] = None
    certificate_number: Optional[str] = None
    certificate_file_url: Optional[str] = None
    certificate_expiry_date: Optional[date] = None
    next_calibration_due: Optional[date] = None
    environment_temp: Optional[float] = None
    environment_humidity: Optional[float] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcFailureAnalysisCreate(BaseModel):
    failure_analysis_id: int
    fa_number: str
    fa_type_code: str
    fa_status_code: Optional[str] = None
    ncr_id: Optional[int] = None
    complaint_id: Optional[int] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    failure_mode: Optional[str] = None
    failure_mechanism: Optional[str] = None
    failure_site: Optional[str] = None
    findings: Optional[str] = None
    conclusion: Optional[str] = None
    recommendation: Optional[str] = None
    root_cause_analysis_id: Optional[int] = None
    analyzed_by: Optional[str] = None
    analysis_date: Optional[datetime] = None
    evidence_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcFailureAnalysisUpdate(BaseModel):
    failure_analysis_id: Optional[int] = None
    fa_number: Optional[str] = None
    fa_type_code: Optional[str] = None
    fa_status_code: Optional[str] = None
    ncr_id: Optional[int] = None
    complaint_id: Optional[int] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    failure_mode: Optional[str] = None
    failure_mechanism: Optional[str] = None
    failure_site: Optional[str] = None
    findings: Optional[str] = None
    conclusion: Optional[str] = None
    recommendation: Optional[str] = None
    root_cause_analysis_id: Optional[int] = None
    analyzed_by: Optional[str] = None
    analysis_date: Optional[datetime] = None
    evidence_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcFailureAnalysisOut(BaseModel):
    failure_analysis_id: int
    fa_number: str
    fa_type_code: str
    fa_status_code: Optional[str] = None
    ncr_id: Optional[int] = None
    complaint_id: Optional[int] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    failure_mode: Optional[str] = None
    failure_mechanism: Optional[str] = None
    failure_site: Optional[str] = None
    findings: Optional[str] = None
    conclusion: Optional[str] = None
    recommendation: Optional[str] = None
    root_cause_analysis_id: Optional[int] = None
    analyzed_by: Optional[str] = None
    analysis_date: Optional[datetime] = None
    evidence_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcFmeaActionsCreate(BaseModel):
    fmea_action_id: int
    fmea_item_id: int
    action_sequence: int
    action_description: str
    action_type_code: Optional[str] = None
    assigned_to: Optional[str] = None
    target_date: Optional[date] = None
    completion_date: Optional[datetime] = None
    action_status_code: Optional[str] = None
    results: Optional[str] = None
    revised_severity: Optional[int] = None
    revised_occurrence: Optional[int] = None
    revised_detection: Optional[int] = None
    revised_rpn: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcFmeaActionsUpdate(BaseModel):
    fmea_action_id: Optional[int] = None
    fmea_item_id: Optional[int] = None
    action_sequence: Optional[int] = None
    action_description: Optional[str] = None
    action_type_code: Optional[str] = None
    assigned_to: Optional[str] = None
    target_date: Optional[date] = None
    completion_date: Optional[datetime] = None
    action_status_code: Optional[str] = None
    results: Optional[str] = None
    revised_severity: Optional[int] = None
    revised_occurrence: Optional[int] = None
    revised_detection: Optional[int] = None
    revised_rpn: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcFmeaActionsOut(BaseModel):
    fmea_action_id: int
    fmea_item_id: int
    action_sequence: int
    action_description: str
    action_type_code: Optional[str] = None
    assigned_to: Optional[str] = None
    target_date: Optional[date] = None
    completion_date: Optional[datetime] = None
    action_status_code: Optional[str] = None
    results: Optional[str] = None
    revised_severity: Optional[int] = None
    revised_occurrence: Optional[int] = None
    revised_detection: Optional[int] = None
    revised_rpn: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcFmeaHeadersCreate(BaseModel):
    fmea_id: int
    fmea_number: str
    fmea_title: str
    fmea_type_code: str
    fmea_status_code: Optional[str] = None
    fmea_version: Optional[str] = None
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    item_id: Optional[int] = None
    process_code: Optional[str] = None
    system_name: Optional[str] = None
    scope_description: Optional[str] = None
    team_members: Optional[dict] = None
    prepared_by: Optional[str] = None
    prepared_date: Optional[date] = None
    reviewed_by: Optional[str] = None
    reviewed_date: Optional[date] = None
    approved_by: Optional[str] = None
    approved_date: Optional[date] = None
    revision_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcFmeaHeadersUpdate(BaseModel):
    fmea_id: Optional[int] = None
    fmea_number: Optional[str] = None
    fmea_title: Optional[str] = None
    fmea_type_code: Optional[str] = None
    fmea_status_code: Optional[str] = None
    fmea_version: Optional[str] = None
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    item_id: Optional[int] = None
    process_code: Optional[str] = None
    system_name: Optional[str] = None
    scope_description: Optional[str] = None
    team_members: Optional[dict] = None
    prepared_by: Optional[str] = None
    prepared_date: Optional[date] = None
    reviewed_by: Optional[str] = None
    reviewed_date: Optional[date] = None
    approved_by: Optional[str] = None
    approved_date: Optional[date] = None
    revision_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcFmeaHeadersOut(BaseModel):
    fmea_id: int
    fmea_number: str
    fmea_title: str
    fmea_type_code: str
    fmea_status_code: Optional[str] = None
    fmea_version: Optional[str] = None
    organization_id: Optional[int] = None
    department_code: Optional[str] = None
    item_id: Optional[int] = None
    process_code: Optional[str] = None
    system_name: Optional[str] = None
    scope_description: Optional[str] = None
    team_members: Optional[dict] = None
    prepared_by: Optional[str] = None
    prepared_date: Optional[date] = None
    reviewed_by: Optional[str] = None
    reviewed_date: Optional[date] = None
    approved_by: Optional[str] = None
    approved_date: Optional[date] = None
    revision_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcFmeaItemsCreate(BaseModel):
    fmea_item_id: int
    fmea_id: int
    item_sequence: int
    function_requirement: Optional[str] = None
    failure_mode: str
    effect_of_failure: Optional[str] = None
    severity_rating: int
    cause_of_failure: Optional[str] = None
    occurrence_rating: int
    current_control_prevention: Optional[str] = None
    current_control_detection: Optional[str] = None
    detection_rating: int
    rpn_value: Optional[int] = None
    recommended_action: Optional[str] = None
    action_assigned_to: Optional[str] = None
    action_target_date: Optional[date] = None
    action_completed_date: Optional[datetime] = None
    action_result: Optional[str] = None
    revised_severity: Optional[int] = None
    revised_occurrence: Optional[int] = None
    revised_detection: Optional[int] = None
    revised_rpn: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcFmeaItemsUpdate(BaseModel):
    fmea_item_id: Optional[int] = None
    fmea_id: Optional[int] = None
    item_sequence: Optional[int] = None
    function_requirement: Optional[str] = None
    failure_mode: Optional[str] = None
    effect_of_failure: Optional[str] = None
    severity_rating: Optional[int] = None
    cause_of_failure: Optional[str] = None
    occurrence_rating: Optional[int] = None
    current_control_prevention: Optional[str] = None
    current_control_detection: Optional[str] = None
    detection_rating: Optional[int] = None
    rpn_value: Optional[int] = None
    recommended_action: Optional[str] = None
    action_assigned_to: Optional[str] = None
    action_target_date: Optional[date] = None
    action_completed_date: Optional[datetime] = None
    action_result: Optional[str] = None
    revised_severity: Optional[int] = None
    revised_occurrence: Optional[int] = None
    revised_detection: Optional[int] = None
    revised_rpn: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcFmeaItemsOut(BaseModel):
    fmea_item_id: int
    fmea_id: int
    item_sequence: int
    function_requirement: Optional[str] = None
    failure_mode: str
    effect_of_failure: Optional[str] = None
    severity_rating: int
    cause_of_failure: Optional[str] = None
    occurrence_rating: int
    current_control_prevention: Optional[str] = None
    current_control_detection: Optional[str] = None
    detection_rating: int
    rpn_value: Optional[int] = None
    recommended_action: Optional[str] = None
    action_assigned_to: Optional[str] = None
    action_target_date: Optional[date] = None
    action_completed_date: Optional[datetime] = None
    action_result: Optional[str] = None
    revised_severity: Optional[int] = None
    revised_occurrence: Optional[int] = None
    revised_detection: Optional[int] = None
    revised_rpn: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcHoldsCreate(BaseModel):
    hold_id: int
    hold_number: str
    hold_type_code: str
    hold_status_code: Optional[str] = None
    hold_reason: str
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    location_id: Optional[int] = None
    organization_id: Optional[int] = None
    quantity: Optional[float] = None
    uom_code: Optional[str] = None
    placed_by: Optional[str] = None
    placed_date: datetime
    source_inspection_id: Optional[int] = None
    source_ncr_id: Optional[int] = None
    release_authority: Optional[str] = None
    release_date: Optional[datetime] = None
    release_reason: Optional[str] = None
    release_condition: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcHoldsUpdate(BaseModel):
    hold_id: Optional[int] = None
    hold_number: Optional[str] = None
    hold_type_code: Optional[str] = None
    hold_status_code: Optional[str] = None
    hold_reason: Optional[str] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    location_id: Optional[int] = None
    organization_id: Optional[int] = None
    quantity: Optional[float] = None
    uom_code: Optional[str] = None
    placed_by: Optional[str] = None
    placed_date: Optional[datetime] = None
    source_inspection_id: Optional[int] = None
    source_ncr_id: Optional[int] = None
    release_authority: Optional[str] = None
    release_date: Optional[datetime] = None
    release_reason: Optional[str] = None
    release_condition: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcHoldsOut(BaseModel):
    hold_id: int
    hold_number: str
    hold_type_code: str
    hold_status_code: Optional[str] = None
    hold_reason: str
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    location_id: Optional[int] = None
    organization_id: Optional[int] = None
    quantity: Optional[float] = None
    uom_code: Optional[str] = None
    placed_by: Optional[str] = None
    placed_date: datetime
    source_inspection_id: Optional[int] = None
    source_ncr_id: Optional[int] = None
    release_authority: Optional[str] = None
    release_date: Optional[datetime] = None
    release_reason: Optional[str] = None
    release_condition: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcInspectionEquipmentCreate(BaseModel):
    inspection_equip_id: int
    inspection_id: int
    equipment_id: int
    usage_start_time: Optional[datetime] = None
    usage_end_time: Optional[datetime] = None
    calibration_verified: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcInspectionEquipmentUpdate(BaseModel):
    inspection_equip_id: Optional[int] = None
    inspection_id: Optional[int] = None
    equipment_id: Optional[int] = None
    usage_start_time: Optional[datetime] = None
    usage_end_time: Optional[datetime] = None
    calibration_verified: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcInspectionEquipmentOut(BaseModel):
    inspection_equip_id: int
    inspection_id: int
    equipment_id: int
    usage_start_time: Optional[datetime] = None
    usage_end_time: Optional[datetime] = None
    calibration_verified: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcInspectionLotsCreate(BaseModel):
    inspection_lot_id: int
    inspection_id: int
    lot_number: str
    item_id: Optional[int] = None
    serial_number: Optional[str] = None
    quantity: Optional[float] = None
    lot_status_code: Optional[str] = None
    supplier_lot_number: Optional[str] = None
    receipt_date: Optional[datetime] = None
    expiry_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcInspectionLotsUpdate(BaseModel):
    inspection_lot_id: Optional[int] = None
    inspection_id: Optional[int] = None
    lot_number: Optional[str] = None
    item_id: Optional[int] = None
    serial_number: Optional[str] = None
    quantity: Optional[float] = None
    lot_status_code: Optional[str] = None
    supplier_lot_number: Optional[str] = None
    receipt_date: Optional[datetime] = None
    expiry_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcInspectionLotsOut(BaseModel):
    inspection_lot_id: int
    inspection_id: int
    lot_number: str
    item_id: Optional[int] = None
    serial_number: Optional[str] = None
    quantity: Optional[float] = None
    lot_status_code: Optional[str] = None
    supplier_lot_number: Optional[str] = None
    receipt_date: Optional[datetime] = None
    expiry_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcInspectionRoutesCreate(BaseModel):
    inspection_route_id: int
    problem_id: int
    route_name: Optional[str] = None
    route_version: Optional[str] = None
    inspector_id: Optional[int] = None
    inspector_name: Optional[str] = None
    route_sequence: dict
    total_distance: Optional[float] = None
    total_duration: Optional[float] = None
    num_inspections: Optional[int] = None
    inspector_skills: Optional[dict] = None
    shift_start: Optional[datetime] = None
    shift_end: Optional[datetime] = None
    route_map_url: Optional[str] = None
    created_by_algorithm_id: Optional[int] = None
    solve_time_ms: Optional[int] = None
    objective_value: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcInspectionRoutesUpdate(BaseModel):
    inspection_route_id: Optional[int] = None
    problem_id: Optional[int] = None
    route_name: Optional[str] = None
    route_version: Optional[str] = None
    inspector_id: Optional[int] = None
    inspector_name: Optional[str] = None
    route_sequence: Optional[dict] = None
    total_distance: Optional[float] = None
    total_duration: Optional[float] = None
    num_inspections: Optional[int] = None
    inspector_skills: Optional[dict] = None
    shift_start: Optional[datetime] = None
    shift_end: Optional[datetime] = None
    route_map_url: Optional[str] = None
    created_by_algorithm_id: Optional[int] = None
    solve_time_ms: Optional[int] = None
    objective_value: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcInspectionRoutesOut(BaseModel):
    inspection_route_id: int
    problem_id: int
    route_name: Optional[str] = None
    route_version: Optional[str] = None
    inspector_id: Optional[int] = None
    inspector_name: Optional[str] = None
    route_sequence: dict
    total_distance: Optional[float] = None
    total_duration: Optional[float] = None
    num_inspections: Optional[int] = None
    inspector_skills: Optional[dict] = None
    shift_start: Optional[datetime] = None
    shift_end: Optional[datetime] = None
    route_map_url: Optional[str] = None
    created_by_algorithm_id: Optional[int] = None
    solve_time_ms: Optional[int] = None
    objective_value: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcInspectionsCreate(BaseModel):
    inspection_id: int
    inspection_number: str
    inspection_type_code: str
    source_type_code: Optional[str] = None
    source_document_id: Optional[int] = None
    source_document_line_id: Optional[int] = None
    source_transaction_id: Optional[str] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    batch_number: Optional[str] = None
    organization_id: Optional[int] = None
    supplier_id: Optional[int] = None
    customer_id: Optional[int] = None
    quality_plan_id: Optional[int] = None
    sampling_plan_id: Optional[int] = None
    inspection_location_id: Optional[int] = None
    inspection_location: Optional[str] = None
    inspector_id: Optional[int] = None
    inspector_name: Optional[str] = None
    inspection_quantity: Optional[float] = None
    sample_quantity: Optional[float] = None
    accepted_quantity: Optional[float] = None
    rejected_quantity: Optional[float] = None
    rework_quantity: Optional[float] = None
    scrapped_quantity: Optional[float] = None
    inspection_status_code: str
    disposition_code: Optional[str] = None
    overall_result_code: Optional[str] = None
    planned_date: Optional[datetime] = None
    started_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    ncr_id: Optional[int] = None
    hold_id: Optional[int] = None
    environment_temp: Optional[float] = None
    environment_humidity: Optional[float] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcInspectionsUpdate(BaseModel):
    inspection_id: Optional[int] = None
    inspection_number: Optional[str] = None
    inspection_type_code: Optional[str] = None
    source_type_code: Optional[str] = None
    source_document_id: Optional[int] = None
    source_document_line_id: Optional[int] = None
    source_transaction_id: Optional[str] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    batch_number: Optional[str] = None
    organization_id: Optional[int] = None
    supplier_id: Optional[int] = None
    customer_id: Optional[int] = None
    quality_plan_id: Optional[int] = None
    sampling_plan_id: Optional[int] = None
    inspection_location_id: Optional[int] = None
    inspection_location: Optional[str] = None
    inspector_id: Optional[int] = None
    inspector_name: Optional[str] = None
    inspection_quantity: Optional[float] = None
    sample_quantity: Optional[float] = None
    accepted_quantity: Optional[float] = None
    rejected_quantity: Optional[float] = None
    rework_quantity: Optional[float] = None
    scrapped_quantity: Optional[float] = None
    inspection_status_code: Optional[str] = None
    disposition_code: Optional[str] = None
    overall_result_code: Optional[str] = None
    planned_date: Optional[datetime] = None
    started_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    ncr_id: Optional[int] = None
    hold_id: Optional[int] = None
    environment_temp: Optional[float] = None
    environment_humidity: Optional[float] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcInspectionsOut(BaseModel):
    inspection_id: int
    inspection_number: str
    inspection_type_code: str
    source_type_code: Optional[str] = None
    source_document_id: Optional[int] = None
    source_document_line_id: Optional[int] = None
    source_transaction_id: Optional[str] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    batch_number: Optional[str] = None
    organization_id: Optional[int] = None
    supplier_id: Optional[int] = None
    customer_id: Optional[int] = None
    quality_plan_id: Optional[int] = None
    sampling_plan_id: Optional[int] = None
    inspection_location_id: Optional[int] = None
    inspection_location: Optional[str] = None
    inspector_id: Optional[int] = None
    inspector_name: Optional[str] = None
    inspection_quantity: Optional[float] = None
    sample_quantity: Optional[float] = None
    accepted_quantity: Optional[float] = None
    rejected_quantity: Optional[float] = None
    rework_quantity: Optional[float] = None
    scrapped_quantity: Optional[float] = None
    inspection_status_code: str
    disposition_code: Optional[str] = None
    overall_result_code: Optional[str] = None
    planned_date: Optional[datetime] = None
    started_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    ncr_id: Optional[int] = None
    hold_id: Optional[int] = None
    environment_temp: Optional[float] = None
    environment_humidity: Optional[float] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcIntegrationConnectionsCreate(BaseModel):
    connection_id: int
    connection_code: str
    connection_name: str
    integration_type_code: str
    target_system_code: str
    endpoint_url: Optional[str] = None
    auth_type_code: Optional[str] = None
    credentials_encrypted: Optional[str] = None
    connection_properties: Optional[dict] = None
    connection_status_code: Optional[str] = None
    heartbeat_interval_sec: Optional[int] = None
    last_heartbeat: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcIntegrationConnectionsUpdate(BaseModel):
    connection_id: Optional[int] = None
    connection_code: Optional[str] = None
    connection_name: Optional[str] = None
    integration_type_code: Optional[str] = None
    target_system_code: Optional[str] = None
    endpoint_url: Optional[str] = None
    auth_type_code: Optional[str] = None
    credentials_encrypted: Optional[str] = None
    connection_properties: Optional[dict] = None
    connection_status_code: Optional[str] = None
    heartbeat_interval_sec: Optional[int] = None
    last_heartbeat: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcIntegrationConnectionsOut(BaseModel):
    connection_id: int
    connection_code: str
    connection_name: str
    integration_type_code: str
    target_system_code: str
    endpoint_url: Optional[str] = None
    auth_type_code: Optional[str] = None
    credentials_encrypted: Optional[str] = None
    connection_properties: Optional[dict] = None
    connection_status_code: Optional[str] = None
    heartbeat_interval_sec: Optional[int] = None
    last_heartbeat: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcIntegrationLogsCreate(BaseModel):
    integration_log_id: int
    connection_id: int
    log_type_code: str
    log_status_code: Optional[str] = None
    direction_code: str
    request_data: Optional[dict] = None
    response_data: Optional[dict] = None
    error_message: Optional[str] = None
    execution_start: Optional[datetime] = None
    execution_end: Optional[datetime] = None
    duration_ms: Optional[int] = None
    retry_count: Optional[int] = None
    source_transaction_id: Optional[str] = None
    payload_size_bytes: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcIntegrationLogsUpdate(BaseModel):
    integration_log_id: Optional[int] = None
    connection_id: Optional[int] = None
    log_type_code: Optional[str] = None
    log_status_code: Optional[str] = None
    direction_code: Optional[str] = None
    request_data: Optional[dict] = None
    response_data: Optional[dict] = None
    error_message: Optional[str] = None
    execution_start: Optional[datetime] = None
    execution_end: Optional[datetime] = None
    duration_ms: Optional[int] = None
    retry_count: Optional[int] = None
    source_transaction_id: Optional[str] = None
    payload_size_bytes: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcIntegrationLogsOut(BaseModel):
    integration_log_id: int
    connection_id: int
    log_type_code: str
    log_status_code: Optional[str] = None
    direction_code: str
    request_data: Optional[dict] = None
    response_data: Optional[dict] = None
    error_message: Optional[str] = None
    execution_start: Optional[datetime] = None
    execution_end: Optional[datetime] = None
    duration_ms: Optional[int] = None
    retry_count: Optional[int] = None
    source_transaction_id: Optional[str] = None
    payload_size_bytes: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcKpiActualsCreate(BaseModel):
    kpi_actual_id: int
    kpi_definition_id: int
    actual_value: Optional[float] = None
    target_value: Optional[float] = None
    variance: Optional[float] = None
    variance_pct: Optional[float] = None
    evaluation_date: date
    period_type_code: Optional[str] = None
    period_start_date: Optional[date] = None
    period_end_date: Optional[date] = None
    entity_type_code: Optional[str] = None
    entity_id: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcKpiActualsUpdate(BaseModel):
    kpi_actual_id: Optional[int] = None
    kpi_definition_id: Optional[int] = None
    actual_value: Optional[float] = None
    target_value: Optional[float] = None
    variance: Optional[float] = None
    variance_pct: Optional[float] = None
    evaluation_date: Optional[date] = None
    period_type_code: Optional[str] = None
    period_start_date: Optional[date] = None
    period_end_date: Optional[date] = None
    entity_type_code: Optional[str] = None
    entity_id: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcKpiActualsOut(BaseModel):
    kpi_actual_id: int
    kpi_definition_id: int
    actual_value: Optional[float] = None
    target_value: Optional[float] = None
    variance: Optional[float] = None
    variance_pct: Optional[float] = None
    evaluation_date: date
    period_type_code: Optional[str] = None
    period_start_date: Optional[date] = None
    period_end_date: Optional[date] = None
    entity_type_code: Optional[str] = None
    entity_id: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcKpiDefinitionsCreate(BaseModel):
    kpi_definition_id: int
    kpi_code: str
    kpi_name: str
    kpi_category_code: str
    kpi_subcategory_code: Optional[str] = None
    description: Optional[str] = None
    formula: Optional[str] = None
    unit_of_measure: Optional[str] = None
    data_source: Optional[str] = None
    frequency_code: Optional[str] = None
    direction_code: Optional[str] = None
    target_value: Optional[float] = None
    threshold_green_from: Optional[float] = None
    threshold_green_to: Optional[float] = None
    threshold_yellow_from: Optional[float] = None
    threshold_yellow_to: Optional[float] = None
    threshold_red_from: Optional[float] = None
    threshold_red_to: Optional[float] = None
    owner_id: Optional[int] = None
    owner_name: Optional[str] = None
    is_calculated: Optional[str] = None
    calculation_sql: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcKpiDefinitionsUpdate(BaseModel):
    kpi_definition_id: Optional[int] = None
    kpi_code: Optional[str] = None
    kpi_name: Optional[str] = None
    kpi_category_code: Optional[str] = None
    kpi_subcategory_code: Optional[str] = None
    description: Optional[str] = None
    formula: Optional[str] = None
    unit_of_measure: Optional[str] = None
    data_source: Optional[str] = None
    frequency_code: Optional[str] = None
    direction_code: Optional[str] = None
    target_value: Optional[float] = None
    threshold_green_from: Optional[float] = None
    threshold_green_to: Optional[float] = None
    threshold_yellow_from: Optional[float] = None
    threshold_yellow_to: Optional[float] = None
    threshold_red_from: Optional[float] = None
    threshold_red_to: Optional[float] = None
    owner_id: Optional[int] = None
    owner_name: Optional[str] = None
    is_calculated: Optional[str] = None
    calculation_sql: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcKpiDefinitionsOut(BaseModel):
    kpi_definition_id: int
    kpi_code: str
    kpi_name: str
    kpi_category_code: str
    kpi_subcategory_code: Optional[str] = None
    description: Optional[str] = None
    formula: Optional[str] = None
    unit_of_measure: Optional[str] = None
    data_source: Optional[str] = None
    frequency_code: Optional[str] = None
    direction_code: Optional[str] = None
    target_value: Optional[float] = None
    threshold_green_from: Optional[float] = None
    threshold_green_to: Optional[float] = None
    threshold_yellow_from: Optional[float] = None
    threshold_yellow_to: Optional[float] = None
    threshold_red_from: Optional[float] = None
    threshold_red_to: Optional[float] = None
    owner_id: Optional[int] = None
    owner_name: Optional[str] = None
    is_calculated: Optional[str] = None
    calculation_sql: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcLanggraphExecutionsCreate(BaseModel):
    execution_id: int
    workflow_id: int
    execution_name: Optional[str] = None
    execution_status_code: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    current_node: Optional[str] = None
    execution_state: Optional[dict] = None
    checkpoints: Optional[dict] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    duration_ms: Optional[int] = None
    llm_calls_count: Optional[int] = None
    tool_calls_count: Optional[int] = None
    total_cost: Optional[float] = None
    triggered_by: Optional[str] = None
    source_inspection_id: Optional[int] = None
    source_ncr_id: Optional[int] = None
    source_complaint_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcLanggraphExecutionsUpdate(BaseModel):
    execution_id: Optional[int] = None
    workflow_id: Optional[int] = None
    execution_name: Optional[str] = None
    execution_status_code: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    current_node: Optional[str] = None
    execution_state: Optional[dict] = None
    checkpoints: Optional[dict] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    duration_ms: Optional[int] = None
    llm_calls_count: Optional[int] = None
    tool_calls_count: Optional[int] = None
    total_cost: Optional[float] = None
    triggered_by: Optional[str] = None
    source_inspection_id: Optional[int] = None
    source_ncr_id: Optional[int] = None
    source_complaint_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcLanggraphExecutionsOut(BaseModel):
    execution_id: int
    workflow_id: int
    execution_name: Optional[str] = None
    execution_status_code: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    current_node: Optional[str] = None
    execution_state: Optional[dict] = None
    checkpoints: Optional[dict] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    duration_ms: Optional[int] = None
    llm_calls_count: Optional[int] = None
    tool_calls_count: Optional[int] = None
    total_cost: Optional[float] = None
    triggered_by: Optional[str] = None
    source_inspection_id: Optional[int] = None
    source_ncr_id: Optional[int] = None
    source_complaint_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcLanggraphStatesCreate(BaseModel):
    state_id: int
    execution_id: int
    node_name: str
    state_data: dict
    is_checkpoint: Optional[str] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcLanggraphStatesUpdate(BaseModel):
    state_id: Optional[int] = None
    execution_id: Optional[int] = None
    node_name: Optional[str] = None
    state_data: Optional[dict] = None
    is_checkpoint: Optional[str] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcLanggraphStatesOut(BaseModel):
    state_id: int
    execution_id: int
    node_name: str
    state_data: dict
    is_checkpoint: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcLanggraphWorkflowsCreate(BaseModel):
    workflow_id: int
    workflow_code: str
    workflow_name: str
    workflow_type_code: Optional[str] = None
    workflow_version: Optional[str] = None
    workflow_status_code: Optional[str] = None
    dag_definition: dict
    state_schema: Optional[dict] = None
    checkpoint_enabled: Optional[str] = None
    hitl_nodes: Optional[dict] = None
    timeout_seconds: Optional[int] = None
    max_retries: Optional[int] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcLanggraphWorkflowsUpdate(BaseModel):
    workflow_id: Optional[int] = None
    workflow_code: Optional[str] = None
    workflow_name: Optional[str] = None
    workflow_type_code: Optional[str] = None
    workflow_version: Optional[str] = None
    workflow_status_code: Optional[str] = None
    dag_definition: Optional[dict] = None
    state_schema: Optional[dict] = None
    checkpoint_enabled: Optional[str] = None
    hitl_nodes: Optional[dict] = None
    timeout_seconds: Optional[int] = None
    max_retries: Optional[int] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcLanggraphWorkflowsOut(BaseModel):
    workflow_id: int
    workflow_code: str
    workflow_name: str
    workflow_type_code: Optional[str] = None
    workflow_version: Optional[str] = None
    workflow_status_code: Optional[str] = None
    dag_definition: dict
    state_schema: Optional[dict] = None
    checkpoint_enabled: Optional[str] = None
    hitl_nodes: Optional[dict] = None
    timeout_seconds: Optional[int] = None
    max_retries: Optional[int] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcLlmConfigsCreate(BaseModel):
    llm_config_id: int
    config_code: str
    config_name: str
    provider_code: str
    model_name: str
    api_endpoint: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    timeout_seconds: Optional[int] = None
    max_retries: Optional[int] = None
    config_status_code: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcLlmConfigsUpdate(BaseModel):
    llm_config_id: Optional[int] = None
    config_code: Optional[str] = None
    config_name: Optional[str] = None
    provider_code: Optional[str] = None
    model_name: Optional[str] = None
    api_endpoint: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    timeout_seconds: Optional[int] = None
    max_retries: Optional[int] = None
    config_status_code: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcLlmConfigsOut(BaseModel):
    llm_config_id: int
    config_code: str
    config_name: str
    provider_code: str
    model_name: str
    api_endpoint: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    timeout_seconds: Optional[int] = None
    max_retries: Optional[int] = None
    config_status_code: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcLotDispositionsCreate(BaseModel):
    lot_disposition_id: int
    disposition_number: str
    inspection_id: Optional[int] = None
    ncr_id: Optional[int] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    organization_id: Optional[int] = None
    quantity: Optional[float] = None
    disposition_code: str
    disposition_reason: Optional[str] = None
    disposition_date: datetime
    disposition_by: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    rework_instructions: Optional[str] = None
    scrap_instructions: Optional[str] = None
    return_instructions: Optional[str] = None
    sort_instructions: Optional[str] = None
    condition_use_as_is: Optional[str] = None
    cost_impact: Optional[float] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcLotDispositionsUpdate(BaseModel):
    lot_disposition_id: Optional[int] = None
    disposition_number: Optional[str] = None
    inspection_id: Optional[int] = None
    ncr_id: Optional[int] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    organization_id: Optional[int] = None
    quantity: Optional[float] = None
    disposition_code: Optional[str] = None
    disposition_reason: Optional[str] = None
    disposition_date: Optional[datetime] = None
    disposition_by: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    rework_instructions: Optional[str] = None
    scrap_instructions: Optional[str] = None
    return_instructions: Optional[str] = None
    sort_instructions: Optional[str] = None
    condition_use_as_is: Optional[str] = None
    cost_impact: Optional[float] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcLotDispositionsOut(BaseModel):
    lot_disposition_id: int
    disposition_number: str
    inspection_id: Optional[int] = None
    ncr_id: Optional[int] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    organization_id: Optional[int] = None
    quantity: Optional[float] = None
    disposition_code: str
    disposition_reason: Optional[str] = None
    disposition_date: datetime
    disposition_by: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    rework_instructions: Optional[str] = None
    scrap_instructions: Optional[str] = None
    return_instructions: Optional[str] = None
    sort_instructions: Optional[str] = None
    condition_use_as_is: Optional[str] = None
    cost_impact: Optional[float] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcMlModelsCreate(BaseModel):
    ml_model_id: int
    model_code: str
    model_name: str
    model_type_code: str
    model_framework_code: Optional[str] = None
    model_version: Optional[str] = None
    model_status_code: Optional[str] = None
    organization_id: Optional[int] = None
    description: Optional[str] = None
    problem_type_code: Optional[str] = None
    training_parameters: Optional[dict] = None
    model_architecture: Optional[dict] = None
    feature_columns: Optional[dict] = None
    target_column: Optional[str] = None
    training_data_query: Optional[str] = None
    training_results: Optional[dict] = None
    validation_results: Optional[dict] = None
    deployment_endpoint: Optional[str] = None
    deployment_date: Optional[datetime] = None
    monitoring_metrics: Optional[dict] = None
    retraining_frequency: Optional[str] = None
    last_trained_date: Optional[datetime] = None
    accuracy_score: Optional[float] = None
    precision_score: Optional[float] = None
    recall_score: Optional[float] = None
    f1_score: Optional[float] = None
    trained_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcMlModelsUpdate(BaseModel):
    ml_model_id: Optional[int] = None
    model_code: Optional[str] = None
    model_name: Optional[str] = None
    model_type_code: Optional[str] = None
    model_framework_code: Optional[str] = None
    model_version: Optional[str] = None
    model_status_code: Optional[str] = None
    organization_id: Optional[int] = None
    description: Optional[str] = None
    problem_type_code: Optional[str] = None
    training_parameters: Optional[dict] = None
    model_architecture: Optional[dict] = None
    feature_columns: Optional[dict] = None
    target_column: Optional[str] = None
    training_data_query: Optional[str] = None
    training_results: Optional[dict] = None
    validation_results: Optional[dict] = None
    deployment_endpoint: Optional[str] = None
    deployment_date: Optional[datetime] = None
    monitoring_metrics: Optional[dict] = None
    retraining_frequency: Optional[str] = None
    last_trained_date: Optional[datetime] = None
    accuracy_score: Optional[float] = None
    precision_score: Optional[float] = None
    recall_score: Optional[float] = None
    f1_score: Optional[float] = None
    trained_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcMlModelsOut(BaseModel):
    ml_model_id: int
    model_code: str
    model_name: str
    model_type_code: str
    model_framework_code: Optional[str] = None
    model_version: Optional[str] = None
    model_status_code: Optional[str] = None
    organization_id: Optional[int] = None
    description: Optional[str] = None
    problem_type_code: Optional[str] = None
    training_parameters: Optional[dict] = None
    model_architecture: Optional[dict] = None
    feature_columns: Optional[dict] = None
    target_column: Optional[str] = None
    training_data_query: Optional[str] = None
    training_results: Optional[dict] = None
    validation_results: Optional[dict] = None
    deployment_endpoint: Optional[str] = None
    deployment_date: Optional[datetime] = None
    monitoring_metrics: Optional[dict] = None
    retraining_frequency: Optional[str] = None
    last_trained_date: Optional[datetime] = None
    accuracy_score: Optional[float] = None
    precision_score: Optional[float] = None
    recall_score: Optional[float] = None
    f1_score: Optional[float] = None
    trained_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcMsaMeasurementsCreate(BaseModel):
    msa_measurement_id: int
    msa_study_id: int
    operator_id: Optional[int] = None
    operator_name: Optional[str] = None
    part_number: Optional[str] = None
    part_sequence: Optional[int] = None
    trial_number: Optional[int] = None
    measured_value: Optional[float] = None
    reference_value: Optional[float] = None
    bias: Optional[float] = None
    measurement_order: Optional[int] = None
    measurement_timestamp: Optional[datetime] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcMsaMeasurementsUpdate(BaseModel):
    msa_measurement_id: Optional[int] = None
    msa_study_id: Optional[int] = None
    operator_id: Optional[int] = None
    operator_name: Optional[str] = None
    part_number: Optional[str] = None
    part_sequence: Optional[int] = None
    trial_number: Optional[int] = None
    measured_value: Optional[float] = None
    reference_value: Optional[float] = None
    bias: Optional[float] = None
    measurement_order: Optional[int] = None
    measurement_timestamp: Optional[datetime] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcMsaMeasurementsOut(BaseModel):
    msa_measurement_id: int
    msa_study_id: int
    operator_id: Optional[int] = None
    operator_name: Optional[str] = None
    part_number: Optional[str] = None
    part_sequence: Optional[int] = None
    trial_number: Optional[int] = None
    measured_value: Optional[float] = None
    reference_value: Optional[float] = None
    bias: Optional[float] = None
    measurement_order: Optional[int] = None
    measurement_timestamp: Optional[datetime] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcMsaStudiesCreate(BaseModel):
    msa_study_id: int
    msa_study_number: str
    msa_study_name: str
    msa_type_code: str
    msa_status_code: Optional[str] = None
    equipment_id: Optional[int] = None
    characteristic_id: Optional[int] = None
    part_number: Optional[str] = None
    organization_id: Optional[int] = None
    number_of_operators: Optional[int] = None
    number_of_parts: Optional[int] = None
    number_of_trials: Optional[int] = None
    tolerance: Optional[float] = None
    process_variation: Optional[float] = None
    ndc_value: Optional[int] = None
    acceptance_criteria: Optional[str] = None
    conclusion: Optional[str] = None
    study_date: Optional[date] = None
    performed_by: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[date] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcMsaStudiesUpdate(BaseModel):
    msa_study_id: Optional[int] = None
    msa_study_number: Optional[str] = None
    msa_study_name: Optional[str] = None
    msa_type_code: Optional[str] = None
    msa_status_code: Optional[str] = None
    equipment_id: Optional[int] = None
    characteristic_id: Optional[int] = None
    part_number: Optional[str] = None
    organization_id: Optional[int] = None
    number_of_operators: Optional[int] = None
    number_of_parts: Optional[int] = None
    number_of_trials: Optional[int] = None
    tolerance: Optional[float] = None
    process_variation: Optional[float] = None
    ndc_value: Optional[int] = None
    acceptance_criteria: Optional[str] = None
    conclusion: Optional[str] = None
    study_date: Optional[date] = None
    performed_by: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[date] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcMsaStudiesOut(BaseModel):
    msa_study_id: int
    msa_study_number: str
    msa_study_name: str
    msa_type_code: str
    msa_status_code: Optional[str] = None
    equipment_id: Optional[int] = None
    characteristic_id: Optional[int] = None
    part_number: Optional[str] = None
    organization_id: Optional[int] = None
    number_of_operators: Optional[int] = None
    number_of_parts: Optional[int] = None
    number_of_trials: Optional[int] = None
    tolerance: Optional[float] = None
    process_variation: Optional[float] = None
    ndc_value: Optional[int] = None
    acceptance_criteria: Optional[str] = None
    conclusion: Optional[str] = None
    study_date: Optional[date] = None
    performed_by: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[date] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcNcrAttachmentsCreate(BaseModel):
    ncr_attachment_id: int
    ncr_id: int
    attachment_type_code: Optional[str] = None
    file_name: Optional[str] = None
    file_url: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcNcrAttachmentsUpdate(BaseModel):
    ncr_attachment_id: Optional[int] = None
    ncr_id: Optional[int] = None
    attachment_type_code: Optional[str] = None
    file_name: Optional[str] = None
    file_url: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcNcrAttachmentsOut(BaseModel):
    ncr_attachment_id: int
    ncr_id: int
    attachment_type_code: Optional[str] = None
    file_name: Optional[str] = None
    file_url: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcNcrContainmentCreate(BaseModel):
    containment_id: int
    ncr_id: int
    containment_type_code: str
    description: str
    assigned_to: Optional[str] = None
    target_date: Optional[date] = None
    completed_date: Optional[datetime] = None
    containment_status_code: Optional[str] = None
    effectiveness_review: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcNcrContainmentUpdate(BaseModel):
    containment_id: Optional[int] = None
    ncr_id: Optional[int] = None
    containment_type_code: Optional[str] = None
    description: Optional[str] = None
    assigned_to: Optional[str] = None
    target_date: Optional[date] = None
    completed_date: Optional[datetime] = None
    containment_status_code: Optional[str] = None
    effectiveness_review: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcNcrContainmentOut(BaseModel):
    containment_id: int
    ncr_id: int
    containment_type_code: str
    description: str
    assigned_to: Optional[str] = None
    target_date: Optional[date] = None
    completed_date: Optional[datetime] = None
    containment_status_code: Optional[str] = None
    effectiveness_review: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcNcrHeadersCreate(BaseModel):
    ncr_id: int
    ncr_number: str
    ncr_title: Optional[str] = None
    ncr_type_code: str
    ncr_severity_code: str
    ncr_status_code: str
    discovery_source_code: Optional[str] = None
    source_inspection_id: Optional[int] = None
    source_complaint_id: Optional[int] = None
    source_audit_id: Optional[int] = None
    source_document_id: Optional[int] = None
    source_document_type: Optional[str] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    organization_id: Optional[int] = None
    supplier_id: Optional[int] = None
    customer_id: Optional[int] = None
    quantity_affected: Optional[float] = None
    cost_affected: Optional[float] = None
    defect_id: Optional[int] = None
    defect_code: Optional[str] = None
    disposition_code: Optional[str] = None
    containment_required: Optional[str] = None
    root_cause_analysis_id: Optional[int] = None
    capa_id: Optional[int] = None
    reported_by: Optional[str] = None
    reported_date: Optional[datetime] = None
    assigned_to: Optional[str] = None
    assigned_date: Optional[datetime] = None
    investigation_summary: Optional[str] = None
    root_cause_summary: Optional[str] = None
    corrective_action_summary: Optional[str] = None
    due_date: Optional[date] = None
    closed_date: Optional[datetime] = None
    closed_by: Optional[str] = None
    recurrence_count: Optional[int] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcNcrHeadersUpdate(BaseModel):
    ncr_id: Optional[int] = None
    ncr_number: Optional[str] = None
    ncr_title: Optional[str] = None
    ncr_type_code: Optional[str] = None
    ncr_severity_code: Optional[str] = None
    ncr_status_code: Optional[str] = None
    discovery_source_code: Optional[str] = None
    source_inspection_id: Optional[int] = None
    source_complaint_id: Optional[int] = None
    source_audit_id: Optional[int] = None
    source_document_id: Optional[int] = None
    source_document_type: Optional[str] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    organization_id: Optional[int] = None
    supplier_id: Optional[int] = None
    customer_id: Optional[int] = None
    quantity_affected: Optional[float] = None
    cost_affected: Optional[float] = None
    defect_id: Optional[int] = None
    defect_code: Optional[str] = None
    disposition_code: Optional[str] = None
    containment_required: Optional[str] = None
    root_cause_analysis_id: Optional[int] = None
    capa_id: Optional[int] = None
    reported_by: Optional[str] = None
    reported_date: Optional[datetime] = None
    assigned_to: Optional[str] = None
    assigned_date: Optional[datetime] = None
    investigation_summary: Optional[str] = None
    root_cause_summary: Optional[str] = None
    corrective_action_summary: Optional[str] = None
    due_date: Optional[date] = None
    closed_date: Optional[datetime] = None
    closed_by: Optional[str] = None
    recurrence_count: Optional[int] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcNcrHeadersOut(BaseModel):
    ncr_id: int
    ncr_number: str
    ncr_title: Optional[str] = None
    ncr_type_code: str
    ncr_severity_code: str
    ncr_status_code: str
    discovery_source_code: Optional[str] = None
    source_inspection_id: Optional[int] = None
    source_complaint_id: Optional[int] = None
    source_audit_id: Optional[int] = None
    source_document_id: Optional[int] = None
    source_document_type: Optional[str] = None
    item_id: Optional[int] = None
    lot_number: Optional[str] = None
    serial_number: Optional[str] = None
    organization_id: Optional[int] = None
    supplier_id: Optional[int] = None
    customer_id: Optional[int] = None
    quantity_affected: Optional[float] = None
    cost_affected: Optional[float] = None
    defect_id: Optional[int] = None
    defect_code: Optional[str] = None
    disposition_code: Optional[str] = None
    containment_required: Optional[str] = None
    root_cause_analysis_id: Optional[int] = None
    capa_id: Optional[int] = None
    reported_by: Optional[str] = None
    reported_date: Optional[datetime] = None
    assigned_to: Optional[str] = None
    assigned_date: Optional[datetime] = None
    investigation_summary: Optional[str] = None
    root_cause_summary: Optional[str] = None
    corrective_action_summary: Optional[str] = None
    due_date: Optional[date] = None
    closed_date: Optional[datetime] = None
    closed_by: Optional[str] = None
    recurrence_count: Optional[int] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcNotificationsCreate(BaseModel):
    notification_id: int
    notification_number: str
    notification_type_code: str
    notification_severity: Optional[str] = None
    notification_status_code: Optional[str] = None
    title: str
    message_body: Optional[str] = None
    recipient_list: Optional[dict] = None
    source_type_code: Optional[str] = None
    source_id: Optional[int] = None
    action_required: Optional[str] = None
    due_date: Optional[datetime] = None
    escalation_level: Optional[int] = None
    acknowledged_by: Optional[str] = None
    acknowledged_date: Optional[datetime] = None
    actioned_by: Optional[str] = None
    actioned_date: Optional[datetime] = None
    closed_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcNotificationsUpdate(BaseModel):
    notification_id: Optional[int] = None
    notification_number: Optional[str] = None
    notification_type_code: Optional[str] = None
    notification_severity: Optional[str] = None
    notification_status_code: Optional[str] = None
    title: Optional[str] = None
    message_body: Optional[str] = None
    recipient_list: Optional[dict] = None
    source_type_code: Optional[str] = None
    source_id: Optional[int] = None
    action_required: Optional[str] = None
    due_date: Optional[datetime] = None
    escalation_level: Optional[int] = None
    acknowledged_by: Optional[str] = None
    acknowledged_date: Optional[datetime] = None
    actioned_by: Optional[str] = None
    actioned_date: Optional[datetime] = None
    closed_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcNotificationsOut(BaseModel):
    notification_id: int
    notification_number: str
    notification_type_code: str
    notification_severity: Optional[str] = None
    notification_status_code: Optional[str] = None
    title: str
    message_body: Optional[str] = None
    recipient_list: Optional[dict] = None
    source_type_code: Optional[str] = None
    source_id: Optional[int] = None
    action_required: Optional[str] = None
    due_date: Optional[datetime] = None
    escalation_level: Optional[int] = None
    acknowledged_by: Optional[str] = None
    acknowledged_date: Optional[datetime] = None
    actioned_by: Optional[str] = None
    actioned_date: Optional[datetime] = None
    closed_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcOptimizationProblemsCreate(BaseModel):
    problem_id: int
    problem_name: str
    problem_type_code: str
    problem_status_code: Optional[str] = None
    problem_version: Optional[str] = None
    organization_id: Optional[int] = None
    objective_type_code: str
    objective_function: Optional[dict] = None
    constraints: Optional[dict] = None
    variables: Optional[dict] = None
    parameters: Optional[dict] = None
    data_sources: Optional[dict] = None
    solver_type_code: Optional[str] = None
    solver_config: Optional[dict] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcOptimizationProblemsUpdate(BaseModel):
    problem_id: Optional[int] = None
    problem_name: Optional[str] = None
    problem_type_code: Optional[str] = None
    problem_status_code: Optional[str] = None
    problem_version: Optional[str] = None
    organization_id: Optional[int] = None
    objective_type_code: Optional[str] = None
    objective_function: Optional[dict] = None
    constraints: Optional[dict] = None
    variables: Optional[dict] = None
    parameters: Optional[dict] = None
    data_sources: Optional[dict] = None
    solver_type_code: Optional[str] = None
    solver_config: Optional[dict] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcOptimizationProblemsOut(BaseModel):
    problem_id: int
    problem_name: str
    problem_type_code: str
    problem_status_code: Optional[str] = None
    problem_version: Optional[str] = None
    organization_id: Optional[int] = None
    objective_type_code: str
    objective_function: Optional[dict] = None
    constraints: Optional[dict] = None
    variables: Optional[dict] = None
    parameters: Optional[dict] = None
    data_sources: Optional[dict] = None
    solver_type_code: Optional[str] = None
    solver_config: Optional[dict] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcOrtoolsProblemsCreate(BaseModel):
    ortools_problem_id: int
    problem_code: str
    problem_name: str
    problem_type_code: str
    problem_status_code: Optional[str] = None
    solver_type_code: Optional[str] = None
    algorithm_type_code: Optional[str] = None
    problem_data: Optional[dict] = None
    parameters: Optional[dict] = None
    solution_data: Optional[dict] = None
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_optimal: Optional[str] = None
    gap_pct: Optional[float] = None
    logs: Optional[str] = None
    execution_timestamp: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcOrtoolsProblemsUpdate(BaseModel):
    ortools_problem_id: Optional[int] = None
    problem_code: Optional[str] = None
    problem_name: Optional[str] = None
    problem_type_code: Optional[str] = None
    problem_status_code: Optional[str] = None
    solver_type_code: Optional[str] = None
    algorithm_type_code: Optional[str] = None
    problem_data: Optional[dict] = None
    parameters: Optional[dict] = None
    solution_data: Optional[dict] = None
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_optimal: Optional[str] = None
    gap_pct: Optional[float] = None
    logs: Optional[str] = None
    execution_timestamp: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcOrtoolsProblemsOut(BaseModel):
    ortools_problem_id: int
    problem_code: str
    problem_name: str
    problem_type_code: str
    problem_status_code: Optional[str] = None
    solver_type_code: Optional[str] = None
    algorithm_type_code: Optional[str] = None
    problem_data: Optional[dict] = None
    parameters: Optional[dict] = None
    solution_data: Optional[dict] = None
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_optimal: Optional[str] = None
    gap_pct: Optional[float] = None
    logs: Optional[str] = None
    execution_timestamp: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcPlanAttachmentsCreate(BaseModel):
    plan_attachment_id: int
    plan_id: int
    attachment_type_code: Optional[str] = None
    file_name: Optional[str] = None
    file_url: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPlanAttachmentsUpdate(BaseModel):
    plan_attachment_id: Optional[int] = None
    plan_id: Optional[int] = None
    attachment_type_code: Optional[str] = None
    file_name: Optional[str] = None
    file_url: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPlanAttachmentsOut(BaseModel):
    plan_attachment_id: int
    plan_id: int
    attachment_type_code: Optional[str] = None
    file_name: Optional[str] = None
    file_url: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcPlanElementsCreate(BaseModel):
    plan_element_id: int
    plan_id: int
    element_sequence: int
    characteristic_id: Optional[int] = None
    spec_id: Optional[int] = None
    test_method_id: Optional[int] = None
    sampling_plan_id: Optional[int] = None
    element_type_code: Optional[str] = None
    is_mandatory: Optional[str] = None
    is_control_characteristic: Optional[str] = None
    sample_size: Optional[float] = None
    frequency_code: Optional[str] = None
    instruction_text: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPlanElementsUpdate(BaseModel):
    plan_element_id: Optional[int] = None
    plan_id: Optional[int] = None
    element_sequence: Optional[int] = None
    characteristic_id: Optional[int] = None
    spec_id: Optional[int] = None
    test_method_id: Optional[int] = None
    sampling_plan_id: Optional[int] = None
    element_type_code: Optional[str] = None
    is_mandatory: Optional[str] = None
    is_control_characteristic: Optional[str] = None
    sample_size: Optional[float] = None
    frequency_code: Optional[str] = None
    instruction_text: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPlanElementsOut(BaseModel):
    plan_element_id: int
    plan_id: int
    element_sequence: int
    characteristic_id: Optional[int] = None
    spec_id: Optional[int] = None
    test_method_id: Optional[int] = None
    sampling_plan_id: Optional[int] = None
    element_type_code: Optional[str] = None
    is_mandatory: Optional[str] = None
    is_control_characteristic: Optional[str] = None
    sample_size: Optional[float] = None
    frequency_code: Optional[str] = None
    instruction_text: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcPlanTriggersCreate(BaseModel):
    plan_trigger_id: int
    plan_id: int
    trigger_type_code: str
    trigger_event_code: str
    trigger_source_code: Optional[str] = None
    source_document_type: Optional[str] = None
    priority: Optional[int] = None
    enabled_flag: Optional[str] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPlanTriggersUpdate(BaseModel):
    plan_trigger_id: Optional[int] = None
    plan_id: Optional[int] = None
    trigger_type_code: Optional[str] = None
    trigger_event_code: Optional[str] = None
    trigger_source_code: Optional[str] = None
    source_document_type: Optional[str] = None
    priority: Optional[int] = None
    enabled_flag: Optional[str] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPlanTriggersOut(BaseModel):
    plan_trigger_id: int
    plan_id: int
    trigger_type_code: str
    trigger_event_code: str
    trigger_source_code: Optional[str] = None
    source_document_type: Optional[str] = None
    priority: Optional[int] = None
    enabled_flag: Optional[str] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcPlansCreate(BaseModel):
    plan_id: int
    plan_number: str
    plan_name: str
    plan_type_code: str
    plan_category_code: Optional[str] = None
    plan_priority: Optional[int] = None
    plan_status_code: Optional[str] = None
    plan_version: Optional[str] = None
    plan_frequency_code: Optional[str] = None
    plan_source_code: Optional[str] = None
    is_mandatory: Optional[str] = None
    item_id: Optional[int] = None
    organization_id: Optional[int] = None
    supplier_id: Optional[int] = None
    customer_id: Optional[int] = None
    department_code: Optional[str] = None
    location_id: Optional[int] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    sampling_plan_id: Optional[int] = None
    spec_id: Optional[int] = None
    action_on_pass: Optional[str] = None
    action_on_fail: Optional[str] = None
    action_on_hold: Optional[str] = None
    description: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPlansUpdate(BaseModel):
    plan_id: Optional[int] = None
    plan_number: Optional[str] = None
    plan_name: Optional[str] = None
    plan_type_code: Optional[str] = None
    plan_category_code: Optional[str] = None
    plan_priority: Optional[int] = None
    plan_status_code: Optional[str] = None
    plan_version: Optional[str] = None
    plan_frequency_code: Optional[str] = None
    plan_source_code: Optional[str] = None
    is_mandatory: Optional[str] = None
    item_id: Optional[int] = None
    organization_id: Optional[int] = None
    supplier_id: Optional[int] = None
    customer_id: Optional[int] = None
    department_code: Optional[str] = None
    location_id: Optional[int] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    sampling_plan_id: Optional[int] = None
    spec_id: Optional[int] = None
    action_on_pass: Optional[str] = None
    action_on_fail: Optional[str] = None
    action_on_hold: Optional[str] = None
    description: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPlansOut(BaseModel):
    plan_id: int
    plan_number: str
    plan_name: str
    plan_type_code: str
    plan_category_code: Optional[str] = None
    plan_priority: Optional[int] = None
    plan_status_code: Optional[str] = None
    plan_version: Optional[str] = None
    plan_frequency_code: Optional[str] = None
    plan_source_code: Optional[str] = None
    is_mandatory: Optional[str] = None
    item_id: Optional[int] = None
    organization_id: Optional[int] = None
    supplier_id: Optional[int] = None
    customer_id: Optional[int] = None
    department_code: Optional[str] = None
    location_id: Optional[int] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    sampling_plan_id: Optional[int] = None
    spec_id: Optional[int] = None
    action_on_pass: Optional[str] = None
    action_on_fail: Optional[str] = None
    action_on_hold: Optional[str] = None
    description: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcPpapSubmissionsCreate(BaseModel):
    ppap_submission_id: int
    ppap_number: str
    ppap_level: int
    ppap_status_code: Optional[str] = None
    item_id: int
    organization_id: Optional[int] = None
    supplier_id: Optional[int] = None
    customer_id: Optional[int] = None
    customer_name: Optional[str] = None
    submission_date: date
    approval_date: Optional[date] = None
    approved_by: Optional[str] = None
    engineering_change_level: Optional[str] = None
    design_record_url: Optional[str] = None
    dfmea_ref: Optional[str] = None
    pfmea_ref: Optional[str] = None
    control_plan_ref: Optional[str] = None
    msa_ref: Optional[str] = None
    dimensional_results: Optional[str] = None
    material_test_results: Optional[str] = None
    process_flow_diagram: Optional[str] = None
    capability_studies: Optional[str] = None
    qualified_lab_doc: Optional[str] = None
    appearance_approval: Optional[str] = None
    sample_parts_ref: Optional[str] = None
    master_sample_ref: Optional[str] = None
    checking_aids_ref: Optional[str] = None
    customer_specific_reqs: Optional[dict] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPpapSubmissionsUpdate(BaseModel):
    ppap_submission_id: Optional[int] = None
    ppap_number: Optional[str] = None
    ppap_level: Optional[int] = None
    ppap_status_code: Optional[str] = None
    item_id: Optional[int] = None
    organization_id: Optional[int] = None
    supplier_id: Optional[int] = None
    customer_id: Optional[int] = None
    customer_name: Optional[str] = None
    submission_date: Optional[date] = None
    approval_date: Optional[date] = None
    approved_by: Optional[str] = None
    engineering_change_level: Optional[str] = None
    design_record_url: Optional[str] = None
    dfmea_ref: Optional[str] = None
    pfmea_ref: Optional[str] = None
    control_plan_ref: Optional[str] = None
    msa_ref: Optional[str] = None
    dimensional_results: Optional[str] = None
    material_test_results: Optional[str] = None
    process_flow_diagram: Optional[str] = None
    capability_studies: Optional[str] = None
    qualified_lab_doc: Optional[str] = None
    appearance_approval: Optional[str] = None
    sample_parts_ref: Optional[str] = None
    master_sample_ref: Optional[str] = None
    checking_aids_ref: Optional[str] = None
    customer_specific_reqs: Optional[dict] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPpapSubmissionsOut(BaseModel):
    ppap_submission_id: int
    ppap_number: str
    ppap_level: int
    ppap_status_code: Optional[str] = None
    item_id: int
    organization_id: Optional[int] = None
    supplier_id: Optional[int] = None
    customer_id: Optional[int] = None
    customer_name: Optional[str] = None
    submission_date: date
    approval_date: Optional[date] = None
    approved_by: Optional[str] = None
    engineering_change_level: Optional[str] = None
    design_record_url: Optional[str] = None
    dfmea_ref: Optional[str] = None
    pfmea_ref: Optional[str] = None
    control_plan_ref: Optional[str] = None
    msa_ref: Optional[str] = None
    dimensional_results: Optional[str] = None
    material_test_results: Optional[str] = None
    process_flow_diagram: Optional[str] = None
    capability_studies: Optional[str] = None
    qualified_lab_doc: Optional[str] = None
    appearance_approval: Optional[str] = None
    sample_parts_ref: Optional[str] = None
    master_sample_ref: Optional[str] = None
    checking_aids_ref: Optional[str] = None
    customer_specific_reqs: Optional[dict] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcPredictionsCreate(BaseModel):
    prediction_id: int
    prediction_code: str
    prediction_type_code: str
    ml_model_id: Optional[int] = None
    organization_id: Optional[int] = None
    entity_type_code: Optional[str] = None
    entity_id: Optional[int] = None
    prediction_horizon: Optional[str] = None
    predicted_value: Optional[float] = None
    predicted_probability: Optional[float] = None
    confidence_level: Optional[float] = None
    prediction_features: Optional[dict] = None
    prediction_timestamp: datetime
    actual_value: Optional[float] = None
    prediction_error: Optional[float] = None
    accuracy_metric: Optional[float] = None
    scenario_id: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPredictionsUpdate(BaseModel):
    prediction_id: Optional[int] = None
    prediction_code: Optional[str] = None
    prediction_type_code: Optional[str] = None
    ml_model_id: Optional[int] = None
    organization_id: Optional[int] = None
    entity_type_code: Optional[str] = None
    entity_id: Optional[int] = None
    prediction_horizon: Optional[str] = None
    predicted_value: Optional[float] = None
    predicted_probability: Optional[float] = None
    confidence_level: Optional[float] = None
    prediction_features: Optional[dict] = None
    prediction_timestamp: Optional[datetime] = None
    actual_value: Optional[float] = None
    prediction_error: Optional[float] = None
    accuracy_metric: Optional[float] = None
    scenario_id: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPredictionsOut(BaseModel):
    prediction_id: int
    prediction_code: str
    prediction_type_code: str
    ml_model_id: Optional[int] = None
    organization_id: Optional[int] = None
    entity_type_code: Optional[str] = None
    entity_id: Optional[int] = None
    prediction_horizon: Optional[str] = None
    predicted_value: Optional[float] = None
    predicted_probability: Optional[float] = None
    confidence_level: Optional[float] = None
    prediction_features: Optional[dict] = None
    prediction_timestamp: datetime
    actual_value: Optional[float] = None
    prediction_error: Optional[float] = None
    accuracy_metric: Optional[float] = None
    scenario_id: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcPromptTemplatesCreate(BaseModel):
    prompt_template_id: int
    template_code: str
    template_name: str
    template_version: Optional[str] = None
    template_type_code: str
    prompt_text: str
    input_variables: Optional[dict] = None
    output_parser: Optional[str] = None
    example_inputs: Optional[dict] = None
    llm_config_id: Optional[int] = None
    template_status_code: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPromptTemplatesUpdate(BaseModel):
    prompt_template_id: Optional[int] = None
    template_code: Optional[str] = None
    template_name: Optional[str] = None
    template_version: Optional[str] = None
    template_type_code: Optional[str] = None
    prompt_text: Optional[str] = None
    input_variables: Optional[dict] = None
    output_parser: Optional[str] = None
    example_inputs: Optional[dict] = None
    llm_config_id: Optional[int] = None
    template_status_code: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcPromptTemplatesOut(BaseModel):
    prompt_template_id: int
    template_code: str
    template_name: str
    template_version: Optional[str] = None
    template_type_code: str
    prompt_text: str
    input_variables: Optional[dict] = None
    output_parser: Optional[str] = None
    example_inputs: Optional[dict] = None
    llm_config_id: Optional[int] = None
    template_status_code: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcRootCauseAnalysisCreate(BaseModel):
    root_cause_analysis_id: int
    rca_number: str
    rca_method_code: str
    rca_title: Optional[str] = None
    rca_status_code: Optional[str] = None
    source_ncr_id: Optional[int] = None
    source_capa_id: Optional[int] = None
    source_complaint_id: Optional[int] = None
    source_type_code: Optional[str] = None
    facilitator: Optional[str] = None
    participants: Optional[str] = None
    problem_statement: Optional[str] = None
    analysis_description: Optional[str] = None
    conclusion: Optional[str] = None
    recommendation: Optional[str] = None
    rca_date: Optional[date] = None
    completed_date: Optional[datetime] = None
    attachment_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcRootCauseAnalysisUpdate(BaseModel):
    root_cause_analysis_id: Optional[int] = None
    rca_number: Optional[str] = None
    rca_method_code: Optional[str] = None
    rca_title: Optional[str] = None
    rca_status_code: Optional[str] = None
    source_ncr_id: Optional[int] = None
    source_capa_id: Optional[int] = None
    source_complaint_id: Optional[int] = None
    source_type_code: Optional[str] = None
    facilitator: Optional[str] = None
    participants: Optional[str] = None
    problem_statement: Optional[str] = None
    analysis_description: Optional[str] = None
    conclusion: Optional[str] = None
    recommendation: Optional[str] = None
    rca_date: Optional[date] = None
    completed_date: Optional[datetime] = None
    attachment_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcRootCauseAnalysisOut(BaseModel):
    root_cause_analysis_id: int
    rca_number: str
    rca_method_code: str
    rca_title: Optional[str] = None
    rca_status_code: Optional[str] = None
    source_ncr_id: Optional[int] = None
    source_capa_id: Optional[int] = None
    source_complaint_id: Optional[int] = None
    source_type_code: Optional[str] = None
    facilitator: Optional[str] = None
    participants: Optional[str] = None
    problem_statement: Optional[str] = None
    analysis_description: Optional[str] = None
    conclusion: Optional[str] = None
    recommendation: Optional[str] = None
    rca_date: Optional[date] = None
    completed_date: Optional[datetime] = None
    attachment_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcRootCauseCausesCreate(BaseModel):
    root_cause_cause_id: int
    root_cause_analysis_id: int
    cause_level: int
    cause_sequence: int
    cause_type_code: Optional[str] = None
    cause_description: str
    parent_cause_id: Optional[int] = None
    is_root_cause: Optional[str] = None
    evidence: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcRootCauseCausesUpdate(BaseModel):
    root_cause_cause_id: Optional[int] = None
    root_cause_analysis_id: Optional[int] = None
    cause_level: Optional[int] = None
    cause_sequence: Optional[int] = None
    cause_type_code: Optional[str] = None
    cause_description: Optional[str] = None
    parent_cause_id: Optional[int] = None
    is_root_cause: Optional[str] = None
    evidence: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcRootCauseCausesOut(BaseModel):
    root_cause_cause_id: int
    root_cause_analysis_id: int
    cause_level: int
    cause_sequence: int
    cause_type_code: Optional[str] = None
    cause_description: str
    parent_cause_id: Optional[int] = None
    is_root_cause: Optional[str] = None
    evidence: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcSampleContainersCreate(BaseModel):
    container_id: int
    container_code: str
    container_name: str
    container_type_code: str
    length_cm: Optional[float] = None
    width_cm: Optional[float] = None
    height_cm: Optional[float] = None
    max_weight_kg: Optional[float] = None
    temperature_zone_code: Optional[str] = None
    capacity: Optional[int] = None
    location_code: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSampleContainersUpdate(BaseModel):
    container_id: Optional[int] = None
    container_code: Optional[str] = None
    container_name: Optional[str] = None
    container_type_code: Optional[str] = None
    length_cm: Optional[float] = None
    width_cm: Optional[float] = None
    height_cm: Optional[float] = None
    max_weight_kg: Optional[float] = None
    temperature_zone_code: Optional[str] = None
    capacity: Optional[int] = None
    location_code: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSampleContainersOut(BaseModel):
    container_id: int
    container_code: str
    container_name: str
    container_type_code: str
    length_cm: Optional[float] = None
    width_cm: Optional[float] = None
    height_cm: Optional[float] = None
    max_weight_kg: Optional[float] = None
    temperature_zone_code: Optional[str] = None
    capacity: Optional[int] = None
    location_code: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcSamplePackingResultsCreate(BaseModel):
    packing_result_id: int
    problem_id: int
    container_id: int
    container_type_code: str
    container_dimensions: Optional[dict] = None
    packed_samples: dict
    utilization_pct: Optional[float] = None
    num_samples_packed: Optional[int] = None
    temperature_zones: Optional[dict] = None
    compatibility_rules: Optional[dict] = None
    retrieval_sequence: Optional[dict] = None
    visualization_3d_url: Optional[str] = None
    solve_time_ms: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSamplePackingResultsUpdate(BaseModel):
    packing_result_id: Optional[int] = None
    problem_id: Optional[int] = None
    container_id: Optional[int] = None
    container_type_code: Optional[str] = None
    container_dimensions: Optional[dict] = None
    packed_samples: Optional[dict] = None
    utilization_pct: Optional[float] = None
    num_samples_packed: Optional[int] = None
    temperature_zones: Optional[dict] = None
    compatibility_rules: Optional[dict] = None
    retrieval_sequence: Optional[dict] = None
    visualization_3d_url: Optional[str] = None
    solve_time_ms: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSamplePackingResultsOut(BaseModel):
    packing_result_id: int
    problem_id: int
    container_id: int
    container_type_code: str
    container_dimensions: Optional[dict] = None
    packed_samples: dict
    utilization_pct: Optional[float] = None
    num_samples_packed: Optional[int] = None
    temperature_zones: Optional[dict] = None
    compatibility_rules: Optional[dict] = None
    retrieval_sequence: Optional[dict] = None
    visualization_3d_url: Optional[str] = None
    solve_time_ms: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcSamplingPlanLinesCreate(BaseModel):
    sampling_plan_line_id: int
    sampling_plan_id: int
    lot_size_from: int
    lot_size_to: int
    sample_size: int
    accept_number: Optional[int] = None
    reject_number: Optional[int] = None
    additional_requirements: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSamplingPlanLinesUpdate(BaseModel):
    sampling_plan_line_id: Optional[int] = None
    sampling_plan_id: Optional[int] = None
    lot_size_from: Optional[int] = None
    lot_size_to: Optional[int] = None
    sample_size: Optional[int] = None
    accept_number: Optional[int] = None
    reject_number: Optional[int] = None
    additional_requirements: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSamplingPlanLinesOut(BaseModel):
    sampling_plan_line_id: int
    sampling_plan_id: int
    lot_size_from: int
    lot_size_to: int
    sample_size: int
    accept_number: Optional[int] = None
    reject_number: Optional[int] = None
    additional_requirements: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcSamplingPlansCreate(BaseModel):
    sampling_plan_id: int
    plan_code: str
    plan_name: str
    sampling_standard_code: Optional[str] = None
    sampling_type_code: str
    sampling_level_code: Optional[str] = None
    aql_value: Optional[float] = None
    ltpd_value: Optional[float] = None
    lot_size_from: Optional[int] = None
    lot_size_to: Optional[int] = None
    sample_size: int
    accept_number: Optional[int] = None
    reject_number: Optional[int] = None
    switching_rule_code: Optional[str] = None
    skip_lot_rule_code: Optional[str] = None
    is_restrictive: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSamplingPlansUpdate(BaseModel):
    sampling_plan_id: Optional[int] = None
    plan_code: Optional[str] = None
    plan_name: Optional[str] = None
    sampling_standard_code: Optional[str] = None
    sampling_type_code: Optional[str] = None
    sampling_level_code: Optional[str] = None
    aql_value: Optional[float] = None
    ltpd_value: Optional[float] = None
    lot_size_from: Optional[int] = None
    lot_size_to: Optional[int] = None
    sample_size: Optional[int] = None
    accept_number: Optional[int] = None
    reject_number: Optional[int] = None
    switching_rule_code: Optional[str] = None
    skip_lot_rule_code: Optional[str] = None
    is_restrictive: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSamplingPlansOut(BaseModel):
    sampling_plan_id: int
    plan_code: str
    plan_name: str
    sampling_standard_code: Optional[str] = None
    sampling_type_code: str
    sampling_level_code: Optional[str] = None
    aql_value: Optional[float] = None
    ltpd_value: Optional[float] = None
    lot_size_from: Optional[int] = None
    lot_size_to: Optional[int] = None
    sample_size: int
    accept_number: Optional[int] = None
    reject_number: Optional[int] = None
    switching_rule_code: Optional[str] = None
    skip_lot_rule_code: Optional[str] = None
    is_restrictive: Optional[str] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcScenariosCreate(BaseModel):
    scenario_id: int
    scenario_code: str
    scenario_name: str
    scenario_type_code: str
    scenario_status_code: Optional[str] = None
    organization_id: Optional[int] = None
    description: Optional[str] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    objectives: Optional[dict] = None
    input_parameters: Optional[dict] = None
    results: Optional[dict] = None
    comparison_notes: Optional[str] = None
    recommendation: Optional[str] = None
    created_by_algorithm_id: Optional[int] = None
    execution_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcScenariosUpdate(BaseModel):
    scenario_id: Optional[int] = None
    scenario_code: Optional[str] = None
    scenario_name: Optional[str] = None
    scenario_type_code: Optional[str] = None
    scenario_status_code: Optional[str] = None
    organization_id: Optional[int] = None
    description: Optional[str] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    objectives: Optional[dict] = None
    input_parameters: Optional[dict] = None
    results: Optional[dict] = None
    comparison_notes: Optional[str] = None
    recommendation: Optional[str] = None
    created_by_algorithm_id: Optional[int] = None
    execution_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcScenariosOut(BaseModel):
    scenario_id: int
    scenario_code: str
    scenario_name: str
    scenario_type_code: str
    scenario_status_code: Optional[str] = None
    organization_id: Optional[int] = None
    description: Optional[str] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    objectives: Optional[dict] = None
    input_parameters: Optional[dict] = None
    results: Optional[dict] = None
    comparison_notes: Optional[str] = None
    recommendation: Optional[str] = None
    created_by_algorithm_id: Optional[int] = None
    execution_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcScipyAnalysesCreate(BaseModel):
    scipy_analysis_id: int
    analysis_code: str
    analysis_name: str
    analysis_type_code: str
    analysis_status_code: Optional[str] = None
    input_data: Optional[dict] = None
    parameters: Optional[dict] = None
    result_data: Optional[dict] = None
    statistic_value: Optional[float] = None
    p_value: Optional[float] = None
    degrees_of_freedom: Optional[int] = None
    confidence_interval_lower: Optional[float] = None
    confidence_interval_upper: Optional[float] = None
    effect_size: Optional[float] = None
    conclusion: Optional[str] = None
    execution_timestamp: Optional[datetime] = None
    execution_time_ms: Optional[int] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcScipyAnalysesUpdate(BaseModel):
    scipy_analysis_id: Optional[int] = None
    analysis_code: Optional[str] = None
    analysis_name: Optional[str] = None
    analysis_type_code: Optional[str] = None
    analysis_status_code: Optional[str] = None
    input_data: Optional[dict] = None
    parameters: Optional[dict] = None
    result_data: Optional[dict] = None
    statistic_value: Optional[float] = None
    p_value: Optional[float] = None
    degrees_of_freedom: Optional[int] = None
    confidence_interval_lower: Optional[float] = None
    confidence_interval_upper: Optional[float] = None
    effect_size: Optional[float] = None
    conclusion: Optional[str] = None
    execution_timestamp: Optional[datetime] = None
    execution_time_ms: Optional[int] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcScipyAnalysesOut(BaseModel):
    scipy_analysis_id: int
    analysis_code: str
    analysis_name: str
    analysis_type_code: str
    analysis_status_code: Optional[str] = None
    input_data: Optional[dict] = None
    parameters: Optional[dict] = None
    result_data: Optional[dict] = None
    statistic_value: Optional[float] = None
    p_value: Optional[float] = None
    degrees_of_freedom: Optional[int] = None
    confidence_interval_lower: Optional[float] = None
    confidence_interval_upper: Optional[float] = None
    effect_size: Optional[float] = None
    conclusion: Optional[str] = None
    execution_timestamp: Optional[datetime] = None
    execution_time_ms: Optional[int] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcSolverConfigsCreate(BaseModel):
    solver_config_id: int
    solver_name: str
    solver_type_code: str
    solver_version: Optional[str] = None
    parameters: Optional[dict] = None
    algorithm_code: Optional[str] = None
    max_solve_time_seconds: Optional[int] = None
    max_iterations: Optional[int] = None
    tolerance: Optional[float] = None
    parallel_execution: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSolverConfigsUpdate(BaseModel):
    solver_config_id: Optional[int] = None
    solver_name: Optional[str] = None
    solver_type_code: Optional[str] = None
    solver_version: Optional[str] = None
    parameters: Optional[dict] = None
    algorithm_code: Optional[str] = None
    max_solve_time_seconds: Optional[int] = None
    max_iterations: Optional[int] = None
    tolerance: Optional[float] = None
    parallel_execution: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSolverConfigsOut(BaseModel):
    solver_config_id: int
    solver_name: str
    solver_type_code: str
    solver_version: Optional[str] = None
    parameters: Optional[dict] = None
    algorithm_code: Optional[str] = None
    max_solve_time_seconds: Optional[int] = None
    max_iterations: Optional[int] = None
    tolerance: Optional[float] = None
    parallel_execution: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcSpcAlertsCreate(BaseModel):
    spc_alert_id: int
    spc_chart_id: int
    spc_data_point_id: Optional[int] = None
    alert_type_code: str
    alert_severity_code: Optional[str] = None
    alert_status_code: Optional[str] = None
    rule_violated: Optional[str] = None
    description: Optional[str] = None
    assigned_to: Optional[str] = None
    acknowledged_date: Optional[datetime] = None
    resolved_date: Optional[datetime] = None
    resolution_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSpcAlertsUpdate(BaseModel):
    spc_alert_id: Optional[int] = None
    spc_chart_id: Optional[int] = None
    spc_data_point_id: Optional[int] = None
    alert_type_code: Optional[str] = None
    alert_severity_code: Optional[str] = None
    alert_status_code: Optional[str] = None
    rule_violated: Optional[str] = None
    description: Optional[str] = None
    assigned_to: Optional[str] = None
    acknowledged_date: Optional[datetime] = None
    resolved_date: Optional[datetime] = None
    resolution_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSpcAlertsOut(BaseModel):
    spc_alert_id: int
    spc_chart_id: int
    spc_data_point_id: Optional[int] = None
    alert_type_code: str
    alert_severity_code: Optional[str] = None
    alert_status_code: Optional[str] = None
    rule_violated: Optional[str] = None
    description: Optional[str] = None
    assigned_to: Optional[str] = None
    acknowledged_date: Optional[datetime] = None
    resolved_date: Optional[datetime] = None
    resolution_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcSpcChartsCreate(BaseModel):
    spc_chart_id: int
    chart_code: str
    chart_name: str
    chart_type_code: str
    characteristic_id: Optional[int] = None
    item_id: Optional[int] = None
    organization_id: Optional[int] = None
    subgroup_size: Optional[int] = None
    sampling_frequency_code: Optional[str] = None
    chart_version: Optional[str] = None
    chart_status_code: Optional[str] = None
    upper_spec_limit: Optional[float] = None
    lower_spec_limit: Optional[float] = None
    target_value: Optional[float] = None
    upper_control_limit: Optional[float] = None
    lower_control_limit: Optional[float] = None
    center_line: Optional[float] = None
    sigma_estimate: Optional[float] = None
    cp_value: Optional[float] = None
    cpk_value: Optional[float] = None
    pp_value: Optional[float] = None
    ppk_value: Optional[float] = None
    out_of_control_rules: Optional[dict] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSpcChartsUpdate(BaseModel):
    spc_chart_id: Optional[int] = None
    chart_code: Optional[str] = None
    chart_name: Optional[str] = None
    chart_type_code: Optional[str] = None
    characteristic_id: Optional[int] = None
    item_id: Optional[int] = None
    organization_id: Optional[int] = None
    subgroup_size: Optional[int] = None
    sampling_frequency_code: Optional[str] = None
    chart_version: Optional[str] = None
    chart_status_code: Optional[str] = None
    upper_spec_limit: Optional[float] = None
    lower_spec_limit: Optional[float] = None
    target_value: Optional[float] = None
    upper_control_limit: Optional[float] = None
    lower_control_limit: Optional[float] = None
    center_line: Optional[float] = None
    sigma_estimate: Optional[float] = None
    cp_value: Optional[float] = None
    cpk_value: Optional[float] = None
    pp_value: Optional[float] = None
    ppk_value: Optional[float] = None
    out_of_control_rules: Optional[dict] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSpcChartsOut(BaseModel):
    spc_chart_id: int
    chart_code: str
    chart_name: str
    chart_type_code: str
    characteristic_id: Optional[int] = None
    item_id: Optional[int] = None
    organization_id: Optional[int] = None
    subgroup_size: Optional[int] = None
    sampling_frequency_code: Optional[str] = None
    chart_version: Optional[str] = None
    chart_status_code: Optional[str] = None
    upper_spec_limit: Optional[float] = None
    lower_spec_limit: Optional[float] = None
    target_value: Optional[float] = None
    upper_control_limit: Optional[float] = None
    lower_control_limit: Optional[float] = None
    center_line: Optional[float] = None
    sigma_estimate: Optional[float] = None
    cp_value: Optional[float] = None
    cpk_value: Optional[float] = None
    pp_value: Optional[float] = None
    ppk_value: Optional[float] = None
    out_of_control_rules: Optional[dict] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcSpcDataPointsCreate(BaseModel):
    spc_data_point_id: int
    spc_chart_id: int
    subgroup_number: int
    sample_timestamp: datetime
    measurements: dict
    sample_mean: Optional[float] = None
    sample_range: Optional[float] = None
    sample_std_dev: Optional[float] = None
    sample_min: Optional[float] = None
    sample_max: Optional[float] = None
    ucl: Optional[float] = None
    lcl: Optional[float] = None
    center_line: Optional[float] = None
    usl: Optional[float] = None
    lsl: Optional[float] = None
    target_value: Optional[float] = None
    is_out_of_control: Optional[str] = None
    out_of_control_rules: Optional[dict] = None
    pattern_detected: Optional[str] = None
    operator_id: Optional[int] = None
    operator_name: Optional[str] = None
    equipment_id: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSpcDataPointsUpdate(BaseModel):
    spc_data_point_id: Optional[int] = None
    spc_chart_id: Optional[int] = None
    subgroup_number: Optional[int] = None
    sample_timestamp: Optional[datetime] = None
    measurements: Optional[dict] = None
    sample_mean: Optional[float] = None
    sample_range: Optional[float] = None
    sample_std_dev: Optional[float] = None
    sample_min: Optional[float] = None
    sample_max: Optional[float] = None
    ucl: Optional[float] = None
    lcl: Optional[float] = None
    center_line: Optional[float] = None
    usl: Optional[float] = None
    lsl: Optional[float] = None
    target_value: Optional[float] = None
    is_out_of_control: Optional[str] = None
    out_of_control_rules: Optional[dict] = None
    pattern_detected: Optional[str] = None
    operator_id: Optional[int] = None
    operator_name: Optional[str] = None
    equipment_id: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSpcDataPointsOut(BaseModel):
    spc_data_point_id: int
    spc_chart_id: int
    subgroup_number: int
    sample_timestamp: datetime
    measurements: dict
    sample_mean: Optional[float] = None
    sample_range: Optional[float] = None
    sample_std_dev: Optional[float] = None
    sample_min: Optional[float] = None
    sample_max: Optional[float] = None
    ucl: Optional[float] = None
    lcl: Optional[float] = None
    center_line: Optional[float] = None
    usl: Optional[float] = None
    lsl: Optional[float] = None
    target_value: Optional[float] = None
    is_out_of_control: Optional[str] = None
    out_of_control_rules: Optional[dict] = None
    pattern_detected: Optional[str] = None
    operator_id: Optional[int] = None
    operator_name: Optional[str] = None
    equipment_id: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcSpecLimitsCreate(BaseModel):
    spec_limit_id: int
    spec_id: int
    characteristic_id: int
    limit_type_code: str
    upper_limit: Optional[float] = None
    lower_limit: Optional[float] = None
    target_value: Optional[float] = None
    nominal_value: Optional[float] = None
    tolerance_plus: Optional[float] = None
    tolerance_minus: Optional[float] = None
    uom_code: Optional[str] = None
    sequence_number: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSpecLimitsUpdate(BaseModel):
    spec_limit_id: Optional[int] = None
    spec_id: Optional[int] = None
    characteristic_id: Optional[int] = None
    limit_type_code: Optional[str] = None
    upper_limit: Optional[float] = None
    lower_limit: Optional[float] = None
    target_value: Optional[float] = None
    nominal_value: Optional[float] = None
    tolerance_plus: Optional[float] = None
    tolerance_minus: Optional[float] = None
    uom_code: Optional[str] = None
    sequence_number: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSpecLimitsOut(BaseModel):
    spec_limit_id: int
    spec_id: int
    characteristic_id: int
    limit_type_code: str
    upper_limit: Optional[float] = None
    lower_limit: Optional[float] = None
    target_value: Optional[float] = None
    nominal_value: Optional[float] = None
    tolerance_plus: Optional[float] = None
    tolerance_minus: Optional[float] = None
    uom_code: Optional[str] = None
    sequence_number: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcSpecsCreate(BaseModel):
    spec_id: int
    spec_number: str
    spec_name: str
    spec_type_code: str
    spec_class_code: Optional[str] = None
    spec_version: Optional[str] = None
    spec_status_code: Optional[str] = None
    item_id: Optional[int] = None
    organization_id: Optional[int] = None
    customer_id: Optional[int] = None
    supplier_id: Optional[int] = None
    regulatory_standard: Optional[str] = None
    acceptance_criteria: Optional[str] = None
    aql_value: Optional[float] = None
    ltpd_value: Optional[float] = None
    test_method_id: Optional[int] = None
    sampling_plan_id: Optional[int] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSpecsUpdate(BaseModel):
    spec_id: Optional[int] = None
    spec_number: Optional[str] = None
    spec_name: Optional[str] = None
    spec_type_code: Optional[str] = None
    spec_class_code: Optional[str] = None
    spec_version: Optional[str] = None
    spec_status_code: Optional[str] = None
    item_id: Optional[int] = None
    organization_id: Optional[int] = None
    customer_id: Optional[int] = None
    supplier_id: Optional[int] = None
    regulatory_standard: Optional[str] = None
    acceptance_criteria: Optional[str] = None
    aql_value: Optional[float] = None
    ltpd_value: Optional[float] = None
    test_method_id: Optional[int] = None
    sampling_plan_id: Optional[int] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSpecsOut(BaseModel):
    spec_id: int
    spec_number: str
    spec_name: str
    spec_type_code: str
    spec_class_code: Optional[str] = None
    spec_version: Optional[str] = None
    spec_status_code: Optional[str] = None
    item_id: Optional[int] = None
    organization_id: Optional[int] = None
    customer_id: Optional[int] = None
    supplier_id: Optional[int] = None
    regulatory_standard: Optional[str] = None
    acceptance_criteria: Optional[str] = None
    aql_value: Optional[float] = None
    ltpd_value: Optional[float] = None
    test_method_id: Optional[int] = None
    sampling_plan_id: Optional[int] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcSupplierProfilesCreate(BaseModel):
    supplier_profile_id: int
    supplier_id: int
    supplier_code: Optional[str] = None
    supplier_name: Optional[str] = None
    quality_rating: Optional[str] = None
    quality_score: Optional[float] = None
    risk_level_code: Optional[str] = None
    approval_status_code: Optional[str] = None
    approval_date: Optional[date] = None
    last_audit_date: Optional[date] = None
    next_audit_date: Optional[date] = None
    certification_list: Optional[dict] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSupplierProfilesUpdate(BaseModel):
    supplier_profile_id: Optional[int] = None
    supplier_id: Optional[int] = None
    supplier_code: Optional[str] = None
    supplier_name: Optional[str] = None
    quality_rating: Optional[str] = None
    quality_score: Optional[float] = None
    risk_level_code: Optional[str] = None
    approval_status_code: Optional[str] = None
    approval_date: Optional[date] = None
    last_audit_date: Optional[date] = None
    next_audit_date: Optional[date] = None
    certification_list: Optional[dict] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSupplierProfilesOut(BaseModel):
    supplier_profile_id: int
    supplier_id: int
    supplier_code: Optional[str] = None
    supplier_name: Optional[str] = None
    quality_rating: Optional[str] = None
    quality_score: Optional[float] = None
    risk_level_code: Optional[str] = None
    approval_status_code: Optional[str] = None
    approval_date: Optional[date] = None
    last_audit_date: Optional[date] = None
    next_audit_date: Optional[date] = None
    certification_list: Optional[dict] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcSupplierScorecardsCreate(BaseModel):
    scorecard_id: int
    supplier_id: int
    scorecard_period: str
    scorecard_date: date
    quality_score: Optional[float] = None
    delivery_score: Optional[float] = None
    cost_score: Optional[float] = None
    service_score: Optional[float] = None
    overall_score: Optional[float] = None
    ppm_defective: Optional[float] = None
    defect_rate: Optional[float] = None
    first_pass_yield: Optional[float] = None
    lot_rejection_rate: Optional[float] = None
    incoming_inspection_count: Optional[int] = None
    ncr_count: Optional[int] = None
    capa_count: Optional[int] = None
    on_time_delivery_pct: Optional[float] = None
    total_shipments: Optional[int] = None
    scorecard_grade: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSupplierScorecardsUpdate(BaseModel):
    scorecard_id: Optional[int] = None
    supplier_id: Optional[int] = None
    scorecard_period: Optional[str] = None
    scorecard_date: Optional[date] = None
    quality_score: Optional[float] = None
    delivery_score: Optional[float] = None
    cost_score: Optional[float] = None
    service_score: Optional[float] = None
    overall_score: Optional[float] = None
    ppm_defective: Optional[float] = None
    defect_rate: Optional[float] = None
    first_pass_yield: Optional[float] = None
    lot_rejection_rate: Optional[float] = None
    incoming_inspection_count: Optional[int] = None
    ncr_count: Optional[int] = None
    capa_count: Optional[int] = None
    on_time_delivery_pct: Optional[float] = None
    total_shipments: Optional[int] = None
    scorecard_grade: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcSupplierScorecardsOut(BaseModel):
    scorecard_id: int
    supplier_id: int
    scorecard_period: str
    scorecard_date: date
    quality_score: Optional[float] = None
    delivery_score: Optional[float] = None
    cost_score: Optional[float] = None
    service_score: Optional[float] = None
    overall_score: Optional[float] = None
    ppm_defective: Optional[float] = None
    defect_rate: Optional[float] = None
    first_pass_yield: Optional[float] = None
    lot_rejection_rate: Optional[float] = None
    incoming_inspection_count: Optional[int] = None
    ncr_count: Optional[int] = None
    capa_count: Optional[int] = None
    on_time_delivery_pct: Optional[float] = None
    total_shipments: Optional[int] = None
    scorecard_grade: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcTestEquipmentCreate(BaseModel):
    equipment_id: int
    equipment_code: str
    equipment_name: str
    equipment_type_code: str
    manufacturer: Optional[str] = None
    model_number: Optional[str] = None
    serial_number: Optional[str] = None
    asset_number: Optional[str] = None
    location_code: Optional[str] = None
    department_code: Optional[str] = None
    range_min: Optional[float] = None
    range_max: Optional[float] = None
    accuracy: Optional[float] = None
    resolution: Optional[float] = None
    equipment_status_code: Optional[str] = None
    calibration_required: Optional[str] = None
    calibration_frequency_days: Optional[int] = None
    last_calibration_date: Optional[date] = None
    next_calibration_due: Optional[date] = None
    certified_flag: Optional[str] = None
    certification_ref: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcTestEquipmentUpdate(BaseModel):
    equipment_id: Optional[int] = None
    equipment_code: Optional[str] = None
    equipment_name: Optional[str] = None
    equipment_type_code: Optional[str] = None
    manufacturer: Optional[str] = None
    model_number: Optional[str] = None
    serial_number: Optional[str] = None
    asset_number: Optional[str] = None
    location_code: Optional[str] = None
    department_code: Optional[str] = None
    range_min: Optional[float] = None
    range_max: Optional[float] = None
    accuracy: Optional[float] = None
    resolution: Optional[float] = None
    equipment_status_code: Optional[str] = None
    calibration_required: Optional[str] = None
    calibration_frequency_days: Optional[int] = None
    last_calibration_date: Optional[date] = None
    next_calibration_due: Optional[date] = None
    certified_flag: Optional[str] = None
    certification_ref: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcTestEquipmentOut(BaseModel):
    equipment_id: int
    equipment_code: str
    equipment_name: str
    equipment_type_code: str
    manufacturer: Optional[str] = None
    model_number: Optional[str] = None
    serial_number: Optional[str] = None
    asset_number: Optional[str] = None
    location_code: Optional[str] = None
    department_code: Optional[str] = None
    range_min: Optional[float] = None
    range_max: Optional[float] = None
    accuracy: Optional[float] = None
    resolution: Optional[float] = None
    equipment_status_code: Optional[str] = None
    calibration_required: Optional[str] = None
    calibration_frequency_days: Optional[int] = None
    last_calibration_date: Optional[date] = None
    next_calibration_due: Optional[date] = None
    certified_flag: Optional[str] = None
    certification_ref: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcTestMethodsCreate(BaseModel):
    test_method_id: int
    method_code: str
    method_name: str
    method_type_code: str
    method_version: Optional[str] = None
    method_status_code: Optional[str] = None
    description: Optional[str] = None
    procedure_steps: Optional[str] = None
    sample_preparation: Optional[str] = None
    acceptance_criteria: Optional[str] = None
    equipment_requirements: Optional[str] = None
    training_requirements: Optional[str] = None
    certification_required: Optional[str] = None
    safety_requirements: Optional[str] = None
    reference_standard: Optional[str] = None
    reference_source: Optional[str] = None
    turnaround_time_hours: Optional[float] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcTestMethodsUpdate(BaseModel):
    test_method_id: Optional[int] = None
    method_code: Optional[str] = None
    method_name: Optional[str] = None
    method_type_code: Optional[str] = None
    method_version: Optional[str] = None
    method_status_code: Optional[str] = None
    description: Optional[str] = None
    procedure_steps: Optional[str] = None
    sample_preparation: Optional[str] = None
    acceptance_criteria: Optional[str] = None
    equipment_requirements: Optional[str] = None
    training_requirements: Optional[str] = None
    certification_required: Optional[str] = None
    safety_requirements: Optional[str] = None
    reference_standard: Optional[str] = None
    reference_source: Optional[str] = None
    turnaround_time_hours: Optional[float] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcTestMethodsOut(BaseModel):
    test_method_id: int
    method_code: str
    method_name: str
    method_type_code: str
    method_version: Optional[str] = None
    method_status_code: Optional[str] = None
    description: Optional[str] = None
    procedure_steps: Optional[str] = None
    sample_preparation: Optional[str] = None
    acceptance_criteria: Optional[str] = None
    equipment_requirements: Optional[str] = None
    training_requirements: Optional[str] = None
    certification_required: Optional[str] = None
    safety_requirements: Optional[str] = None
    reference_standard: Optional[str] = None
    reference_source: Optional[str] = None
    turnaround_time_hours: Optional[float] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcTestResultLinesCreate(BaseModel):
    test_result_line_id: int
    test_result_id: int
    characteristic_id: int
    spec_limit_id: Optional[int] = None
    measured_value: Optional[float] = None
    measured_text: Optional[str] = None
    measured_date: Optional[datetime] = None
    uom_code: Optional[str] = None
    deviation_from_target: Optional[float] = None
    deviation_pct: Optional[float] = None
    result_status_code: Optional[str] = None
    is_out_of_spec: Optional[str] = None
    is_warning: Optional[str] = None
    defect_code: Optional[str] = None
    defect_id: Optional[int] = None
    operator_id: Optional[int] = None
    equipment_id: Optional[int] = None
    test_timestamp: Optional[datetime] = None
    sequence_number: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcTestResultLinesUpdate(BaseModel):
    test_result_line_id: Optional[int] = None
    test_result_id: Optional[int] = None
    characteristic_id: Optional[int] = None
    spec_limit_id: Optional[int] = None
    measured_value: Optional[float] = None
    measured_text: Optional[str] = None
    measured_date: Optional[datetime] = None
    uom_code: Optional[str] = None
    deviation_from_target: Optional[float] = None
    deviation_pct: Optional[float] = None
    result_status_code: Optional[str] = None
    is_out_of_spec: Optional[str] = None
    is_warning: Optional[str] = None
    defect_code: Optional[str] = None
    defect_id: Optional[int] = None
    operator_id: Optional[int] = None
    equipment_id: Optional[int] = None
    test_timestamp: Optional[datetime] = None
    sequence_number: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcTestResultLinesOut(BaseModel):
    test_result_line_id: int
    test_result_id: int
    characteristic_id: int
    spec_limit_id: Optional[int] = None
    measured_value: Optional[float] = None
    measured_text: Optional[str] = None
    measured_date: Optional[datetime] = None
    uom_code: Optional[str] = None
    deviation_from_target: Optional[float] = None
    deviation_pct: Optional[float] = None
    result_status_code: Optional[str] = None
    is_out_of_spec: Optional[str] = None
    is_warning: Optional[str] = None
    defect_code: Optional[str] = None
    defect_id: Optional[int] = None
    operator_id: Optional[int] = None
    equipment_id: Optional[int] = None
    test_timestamp: Optional[datetime] = None
    sequence_number: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcTestResultsCreate(BaseModel):
    test_result_id: int
    inspection_id: int
    test_result_number: str
    test_result_status_code: Optional[str] = None
    overall_result_code: Optional[str] = None
    operator_id: Optional[int] = None
    operator_name: Optional[str] = None
    test_date: Optional[datetime] = None
    test_method_id: Optional[int] = None
    equipment_id: Optional[int] = None
    test_duration_minutes: Optional[float] = None
    calculation_mean: Optional[float] = None
    calculation_std_dev: Optional[float] = None
    calculation_range: Optional[float] = None
    calculation_cpk: Optional[float] = None
    calculation_ppk: Optional[float] = None
    is_retest: Optional[str] = None
    original_result_id: Optional[int] = None
    notes: Optional[str] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcTestResultsUpdate(BaseModel):
    test_result_id: Optional[int] = None
    inspection_id: Optional[int] = None
    test_result_number: Optional[str] = None
    test_result_status_code: Optional[str] = None
    overall_result_code: Optional[str] = None
    operator_id: Optional[int] = None
    operator_name: Optional[str] = None
    test_date: Optional[datetime] = None
    test_method_id: Optional[int] = None
    equipment_id: Optional[int] = None
    test_duration_minutes: Optional[float] = None
    calculation_mean: Optional[float] = None
    calculation_std_dev: Optional[float] = None
    calculation_range: Optional[float] = None
    calculation_cpk: Optional[float] = None
    calculation_ppk: Optional[float] = None
    is_retest: Optional[str] = None
    original_result_id: Optional[int] = None
    notes: Optional[str] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcTestResultsOut(BaseModel):
    test_result_id: int
    inspection_id: int
    test_result_number: str
    test_result_status_code: Optional[str] = None
    overall_result_code: Optional[str] = None
    operator_id: Optional[int] = None
    operator_name: Optional[str] = None
    test_date: Optional[datetime] = None
    test_method_id: Optional[int] = None
    equipment_id: Optional[int] = None
    test_duration_minutes: Optional[float] = None
    calculation_mean: Optional[float] = None
    calculation_std_dev: Optional[float] = None
    calculation_range: Optional[float] = None
    calculation_cpk: Optional[float] = None
    calculation_ppk: Optional[float] = None
    is_retest: Optional[str] = None
    original_result_id: Optional[int] = None
    notes: Optional[str] = None
    signed_by: Optional[str] = None
    signed_date: Optional[datetime] = None
    signature_meaning: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcTrainingAttendeesCreate(BaseModel):
    training_attendee_id: int
    training_course_id: int
    employee_id: int
    employee_name: Optional[str] = None
    training_date: datetime
    completion_date: Optional[datetime] = None
    trainer_id: Optional[int] = None
    trainer_name: Optional[str] = None
    attendance_status_code: Optional[str] = None
    assessment_score: Optional[float] = None
    assessment_result_code: Optional[str] = None
    certificate_number: Optional[str] = None
    certificate_issue_date: Optional[date] = None
    certificate_expiry_date: Optional[date] = None
    effectiveness_score: Optional[float] = None
    feedback_rating: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcTrainingAttendeesUpdate(BaseModel):
    training_attendee_id: Optional[int] = None
    training_course_id: Optional[int] = None
    employee_id: Optional[int] = None
    employee_name: Optional[str] = None
    training_date: Optional[datetime] = None
    completion_date: Optional[datetime] = None
    trainer_id: Optional[int] = None
    trainer_name: Optional[str] = None
    attendance_status_code: Optional[str] = None
    assessment_score: Optional[float] = None
    assessment_result_code: Optional[str] = None
    certificate_number: Optional[str] = None
    certificate_issue_date: Optional[date] = None
    certificate_expiry_date: Optional[date] = None
    effectiveness_score: Optional[float] = None
    feedback_rating: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcTrainingAttendeesOut(BaseModel):
    training_attendee_id: int
    training_course_id: int
    employee_id: int
    employee_name: Optional[str] = None
    training_date: datetime
    completion_date: Optional[datetime] = None
    trainer_id: Optional[int] = None
    trainer_name: Optional[str] = None
    attendance_status_code: Optional[str] = None
    assessment_score: Optional[float] = None
    assessment_result_code: Optional[str] = None
    certificate_number: Optional[str] = None
    certificate_issue_date: Optional[date] = None
    certificate_expiry_date: Optional[date] = None
    effectiveness_score: Optional[float] = None
    feedback_rating: Optional[int] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcTrainingCoursesCreate(BaseModel):
    training_course_id: int
    course_code: str
    course_name: str
    course_type_code: str
    course_category_code: Optional[str] = None
    course_version: Optional[str] = None
    course_status_code: Optional[str] = None
    description: Optional[str] = None
    duration_hours: Optional[float] = None
    delivery_method_code: Optional[str] = None
    certification_required: Optional[str] = None
    certification_validity_days: Optional[int] = None
    assessment_required: Optional[str] = None
    passing_score: Optional[float] = None
    trainer_qualification: Optional[str] = None
    cost_per_trainee: Optional[float] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcTrainingCoursesUpdate(BaseModel):
    training_course_id: Optional[int] = None
    course_code: Optional[str] = None
    course_name: Optional[str] = None
    course_type_code: Optional[str] = None
    course_category_code: Optional[str] = None
    course_version: Optional[str] = None
    course_status_code: Optional[str] = None
    description: Optional[str] = None
    duration_hours: Optional[float] = None
    delivery_method_code: Optional[str] = None
    certification_required: Optional[str] = None
    certification_validity_days: Optional[int] = None
    assessment_required: Optional[str] = None
    passing_score: Optional[float] = None
    trainer_qualification: Optional[str] = None
    cost_per_trainee: Optional[float] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcTrainingCoursesOut(BaseModel):
    training_course_id: int
    course_code: str
    course_name: str
    course_type_code: str
    course_category_code: Optional[str] = None
    course_version: Optional[str] = None
    course_status_code: Optional[str] = None
    description: Optional[str] = None
    duration_hours: Optional[float] = None
    delivery_method_code: Optional[str] = None
    certification_required: Optional[str] = None
    certification_validity_days: Optional[int] = None
    assessment_required: Optional[str] = None
    passing_score: Optional[float] = None
    trainer_qualification: Optional[str] = None
    cost_per_trainee: Optional[float] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class QcVectorDocumentsCreate(BaseModel):
    vector_document_id: int
    document_external_id: Optional[str] = None
    collection_name: str
    content: str
    meta_data: Optional[dict] = None
    embedding_model: Optional[str] = None
    chunk_sequence: Optional[int] = None
    token_count: Optional[int] = None
    source_document_id: Optional[int] = None
    source_type_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcVectorDocumentsUpdate(BaseModel):
    vector_document_id: Optional[int] = None
    document_external_id: Optional[str] = None
    collection_name: Optional[str] = None
    content: Optional[str] = None
    meta_data: Optional[dict] = None
    embedding_model: Optional[str] = None
    chunk_sequence: Optional[int] = None
    token_count: Optional[int] = None
    source_document_id: Optional[int] = None
    source_type_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class QcVectorDocumentsOut(BaseModel):
    vector_document_id: int
    document_external_id: Optional[str] = None
    collection_name: str
    content: str
    meta_data: Optional[dict] = None
    embedding_model: Optional[str] = None
    chunk_sequence: Optional[int] = None
    token_count: Optional[int] = None
    source_document_id: Optional[int] = None
    source_type_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}
