import uuid
from datetime import date, datetime, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class AiAgentLogsCreate(BaseModel):
    agent_log_id: int
    agent_id: int
    execution_id: str
    action_type: str
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    tool_calls: Optional[dict] = None
    llm_calls: Optional[dict] = None
    reasoning_trace: Optional[str] = None
    execution_time_ms: Optional[int] = None
    token_usage: Optional[dict] = None
    cost_amount: Optional[float] = None
    cost_currency: Optional[str] = None
    status_code: Optional[str] = None
    error_message: Optional[str] = None
    correlation_id: Optional[str] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None

class AiAgentLogsUpdate(BaseModel):
    agent_log_id: Optional[int] = None
    agent_id: Optional[int] = None
    execution_id: Optional[str] = None
    action_type: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    tool_calls: Optional[dict] = None
    llm_calls: Optional[dict] = None
    reasoning_trace: Optional[str] = None
    execution_time_ms: Optional[int] = None
    token_usage: Optional[dict] = None
    cost_amount: Optional[float] = None
    cost_currency: Optional[str] = None
    status_code: Optional[str] = None
    error_message: Optional[str] = None
    correlation_id: Optional[str] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None

class AiAgentLogsOut(BaseModel):
    agent_log_id: int
    agent_id: int
    execution_id: str
    action_type: str
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    tool_calls: Optional[dict] = None
    llm_calls: Optional[dict] = None
    reasoning_trace: Optional[str] = None
    execution_time_ms: Optional[int] = None
    token_usage: Optional[dict] = None
    cost_amount: Optional[float] = None
    cost_currency: Optional[str] = None
    status_code: Optional[str] = None
    error_message: Optional[str] = None
    correlation_id: Optional[str] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class AiDecisionsCreate(BaseModel):
    decision_id: int
    decision_type_code: str
    entity_type_code: str
    entity_id: int
    decision_data: dict
    confidence_score: Optional[float] = None
    explanation: Optional[str] = None
    decision_status_code: Optional[str] = None
    reviewed_by: Optional[str] = None
    review_date: Optional[datetime] = None
    review_comments: Optional[str] = None
    is_applied: Optional[str] = None
    applied_date: Optional[datetime] = None
    applied_by: Optional[str] = None
    rejection_reason: Optional[str] = None
    correlation_id: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class AiDecisionsUpdate(BaseModel):
    decision_id: Optional[int] = None
    decision_type_code: Optional[str] = None
    entity_type_code: Optional[str] = None
    entity_id: Optional[int] = None
    decision_data: Optional[dict] = None
    confidence_score: Optional[float] = None
    explanation: Optional[str] = None
    decision_status_code: Optional[str] = None
    reviewed_by: Optional[str] = None
    review_date: Optional[datetime] = None
    review_comments: Optional[str] = None
    is_applied: Optional[str] = None
    applied_date: Optional[datetime] = None
    applied_by: Optional[str] = None
    rejection_reason: Optional[str] = None
    correlation_id: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class AiDecisionsOut(BaseModel):
    decision_id: int
    decision_type_code: str
    entity_type_code: str
    entity_id: int
    decision_data: dict
    confidence_score: Optional[float] = None
    explanation: Optional[str] = None
    decision_status_code: Optional[str] = None
    reviewed_by: Optional[str] = None
    review_date: Optional[datetime] = None
    review_comments: Optional[str] = None
    is_applied: Optional[str] = None
    applied_date: Optional[datetime] = None
    applied_by: Optional[str] = None
    rejection_reason: Optional[str] = None
    correlation_id: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class AiModelRegistryCreate(BaseModel):
    registry_id: int
    model_name: str
    model_type_code: str
    model_framework: Optional[str] = None
    model_version: str
    model_artifact_uri: Optional[str] = None
    model_status_code: Optional[str] = None
    model_parameters: Optional[dict] = None
    model_metrics: Optional[dict] = None
    training_dataset: Optional[dict] = None
    validation_dataset: Optional[dict] = None
    test_dataset: Optional[dict] = None
    feature_list: Optional[dict] = None
    input_schema: Optional[dict] = None
    output_schema: Optional[dict] = None
    registered_by: Optional[str] = None
    registration_date: Optional[datetime] = None
    deployment_date: Optional[datetime] = None
    deprecation_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class AiModelRegistryUpdate(BaseModel):
    registry_id: Optional[int] = None
    model_name: Optional[str] = None
    model_type_code: Optional[str] = None
    model_framework: Optional[str] = None
    model_version: Optional[str] = None
    model_artifact_uri: Optional[str] = None
    model_status_code: Optional[str] = None
    model_parameters: Optional[dict] = None
    model_metrics: Optional[dict] = None
    training_dataset: Optional[dict] = None
    validation_dataset: Optional[dict] = None
    test_dataset: Optional[dict] = None
    feature_list: Optional[dict] = None
    input_schema: Optional[dict] = None
    output_schema: Optional[dict] = None
    registered_by: Optional[str] = None
    registration_date: Optional[datetime] = None
    deployment_date: Optional[datetime] = None
    deprecation_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class AiModelRegistryOut(BaseModel):
    registry_id: int
    model_name: str
    model_type_code: str
    model_framework: Optional[str] = None
    model_version: str
    model_artifact_uri: Optional[str] = None
    model_status_code: Optional[str] = None
    model_parameters: Optional[dict] = None
    model_metrics: Optional[dict] = None
    training_dataset: Optional[dict] = None
    validation_dataset: Optional[dict] = None
    test_dataset: Optional[dict] = None
    feature_list: Optional[dict] = None
    input_schema: Optional[dict] = None
    output_schema: Optional[dict] = None
    registered_by: Optional[str] = None
    registration_date: Optional[datetime] = None
    deployment_date: Optional[datetime] = None
    deprecation_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class AiWorkflowStateCreate(BaseModel):
    state_id: int
    workflow_type_code: str
    correlation_id: str
    state_data: dict
    state_status_code: Optional[str] = None
    parent_state_id: Optional[int] = None
    is_completed: Optional[str] = None
    completed_at: Optional[datetime] = None
    error_details: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class AiWorkflowStateUpdate(BaseModel):
    state_id: Optional[int] = None
    workflow_type_code: Optional[str] = None
    correlation_id: Optional[str] = None
    state_data: Optional[dict] = None
    state_status_code: Optional[str] = None
    parent_state_id: Optional[int] = None
    is_completed: Optional[str] = None
    completed_at: Optional[datetime] = None
    error_details: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class AiWorkflowStateOut(BaseModel):
    state_id: int
    workflow_type_code: str
    correlation_id: str
    state_data: dict
    state_status_code: Optional[str] = None
    parent_state_id: Optional[int] = None
    is_completed: Optional[str] = None
    completed_at: Optional[datetime] = None
    error_details: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaAdditionsCreate(BaseModel):
    addition_id: int
    transaction_id: int
    asset_id: int
    addition_source_code: str
    acquisition_date: date
    in_service_date: date
    purchase_order_id: Optional[int] = None
    po_line_id: Optional[int] = None
    invoice_id: Optional[int] = None
    supplier_id: Optional[int] = None
    supplier_name: Optional[str] = None
    purchase_price: Optional[float] = None
    freight_cost: Optional[float] = None
    installation_cost: Optional[float] = None
    testing_cost: Optional[float] = None
    other_costs: Optional[float] = None
    total_cost: float
    currency_code: Optional[str] = None
    project_id: Optional[int] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None

class FaAdditionsUpdate(BaseModel):
    addition_id: Optional[int] = None
    transaction_id: Optional[int] = None
    asset_id: Optional[int] = None
    addition_source_code: Optional[str] = None
    acquisition_date: Optional[date] = None
    in_service_date: Optional[date] = None
    purchase_order_id: Optional[int] = None
    po_line_id: Optional[int] = None
    invoice_id: Optional[int] = None
    supplier_id: Optional[int] = None
    supplier_name: Optional[str] = None
    purchase_price: Optional[float] = None
    freight_cost: Optional[float] = None
    installation_cost: Optional[float] = None
    testing_cost: Optional[float] = None
    other_costs: Optional[float] = None
    total_cost: Optional[float] = None
    currency_code: Optional[str] = None
    project_id: Optional[int] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None

class FaAdditionsOut(BaseModel):
    addition_id: int
    transaction_id: int
    asset_id: int
    addition_source_code: str
    acquisition_date: date
    in_service_date: date
    purchase_order_id: Optional[int] = None
    po_line_id: Optional[int] = None
    invoice_id: Optional[int] = None
    supplier_id: Optional[int] = None
    supplier_name: Optional[str] = None
    purchase_price: Optional[float] = None
    freight_cost: Optional[float] = None
    installation_cost: Optional[float] = None
    testing_cost: Optional[float] = None
    other_costs: Optional[float] = None
    total_cost: float
    currency_code: Optional[str] = None
    project_id: Optional[int] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaAdjustmentsCreate(BaseModel):
    adjustment_id: int
    transaction_id: int
    asset_id: int
    book_id: Optional[int] = None
    adjustment_type_code: str
    adjustment_amount: float
    adjustment_reason: Optional[str] = None
    old_cost: Optional[float] = None
    new_cost: Optional[float] = None
    old_salvage_value: Optional[float] = None
    new_salvage_value: Optional[float] = None
    old_useful_life: Optional[int] = None
    new_useful_life: Optional[int] = None
    old_deprn_method_id: Optional[int] = None
    new_deprn_method_id: Optional[int] = None
    effective_date: date
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None

class FaAdjustmentsUpdate(BaseModel):
    adjustment_id: Optional[int] = None
    transaction_id: Optional[int] = None
    asset_id: Optional[int] = None
    book_id: Optional[int] = None
    adjustment_type_code: Optional[str] = None
    adjustment_amount: Optional[float] = None
    adjustment_reason: Optional[str] = None
    old_cost: Optional[float] = None
    new_cost: Optional[float] = None
    old_salvage_value: Optional[float] = None
    new_salvage_value: Optional[float] = None
    old_useful_life: Optional[int] = None
    new_useful_life: Optional[int] = None
    old_deprn_method_id: Optional[int] = None
    new_deprn_method_id: Optional[int] = None
    effective_date: Optional[date] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None

class FaAdjustmentsOut(BaseModel):
    adjustment_id: int
    transaction_id: int
    asset_id: int
    book_id: Optional[int] = None
    adjustment_type_code: str
    adjustment_amount: float
    adjustment_reason: Optional[str] = None
    old_cost: Optional[float] = None
    new_cost: Optional[float] = None
    old_salvage_value: Optional[float] = None
    new_salvage_value: Optional[float] = None
    old_useful_life: Optional[int] = None
    new_useful_life: Optional[int] = None
    old_deprn_method_id: Optional[int] = None
    new_deprn_method_id: Optional[int] = None
    effective_date: date
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaAgentDefinitionsCreate(BaseModel):
    agent_id: int
    agent_name: str
    agent_description: Optional[str] = None
    agent_type_code: str
    llm_config_id: Optional[int] = None
    system_prompt: Optional[str] = None
    tools: Optional[dict] = None
    memory_config: Optional[dict] = None
    max_iterations: Optional[int] = None
    agent_version: Optional[str] = None
    agent_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaAgentDefinitionsUpdate(BaseModel):
    agent_id: Optional[int] = None
    agent_name: Optional[str] = None
    agent_description: Optional[str] = None
    agent_type_code: Optional[str] = None
    llm_config_id: Optional[int] = None
    system_prompt: Optional[str] = None
    tools: Optional[dict] = None
    memory_config: Optional[dict] = None
    max_iterations: Optional[int] = None
    agent_version: Optional[str] = None
    agent_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaAgentDefinitionsOut(BaseModel):
    agent_id: int
    agent_name: str
    agent_description: Optional[str] = None
    agent_type_code: str
    llm_config_id: Optional[int] = None
    system_prompt: Optional[str] = None
    tools: Optional[dict] = None
    memory_config: Optional[dict] = None
    max_iterations: Optional[int] = None
    agent_version: Optional[str] = None
    agent_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaAlgorithmsCreate(BaseModel):
    algorithm_id: int
    algorithm_name: str
    algorithm_type_code: str
    description: Optional[str] = None
    algorithm_inputs: Optional[dict] = None
    algorithm_outputs: Optional[dict] = None
    algorithm_config: Optional[dict] = None
    performance_metrics: Optional[dict] = None
    algorithm_version: Optional[str] = None
    documentation_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaAlgorithmsUpdate(BaseModel):
    algorithm_id: Optional[int] = None
    algorithm_name: Optional[str] = None
    algorithm_type_code: Optional[str] = None
    description: Optional[str] = None
    algorithm_inputs: Optional[dict] = None
    algorithm_outputs: Optional[dict] = None
    algorithm_config: Optional[dict] = None
    performance_metrics: Optional[dict] = None
    algorithm_version: Optional[str] = None
    documentation_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaAlgorithmsOut(BaseModel):
    algorithm_id: int
    algorithm_name: str
    algorithm_type_code: str
    description: Optional[str] = None
    algorithm_inputs: Optional[dict] = None
    algorithm_outputs: Optional[dict] = None
    algorithm_config: Optional[dict] = None
    performance_metrics: Optional[dict] = None
    algorithm_version: Optional[str] = None
    documentation_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaAssetAttachmentsCreate(BaseModel):
    attachment_id: int
    asset_id: int
    attachment_type_code: str
    file_name: str
    file_path: str
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    description: Optional[str] = None
    is_encrypted: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaAssetAttachmentsUpdate(BaseModel):
    attachment_id: Optional[int] = None
    asset_id: Optional[int] = None
    attachment_type_code: Optional[str] = None
    file_name: Optional[str] = None
    file_path: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    description: Optional[str] = None
    is_encrypted: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaAssetAttachmentsOut(BaseModel):
    attachment_id: int
    asset_id: int
    attachment_type_code: str
    file_name: str
    file_path: str
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    description: Optional[str] = None
    is_encrypted: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaAssetBookAssignmentsCreate(BaseModel):
    assignment_id: int
    asset_id: int
    book_id: int
    deprn_method_id: int
    deprn_convention_id: Optional[int] = None
    useful_life_months: int
    salvage_value: Optional[float] = None
    salvage_pct: Optional[float] = None
    deprn_start_date: date
    deprn_end_date: Optional[date] = None
    deprn_remaining_months: Optional[int] = None
    original_cost: float
    current_cost: Optional[float] = None
    accumulated_deprn: Optional[float] = None
    net_book_value: Optional[float] = None
    prior_ytd_deprn: Optional[float] = None
    prior_ltd_deprn: Optional[float] = None
    deprn_status_code: Optional[str] = None
    enable_bonus_deprn: Optional[str] = None
    bonus_deprn_pct: Optional[float] = None
    enable_section_179: Optional[str] = None
    section_179_amount: Optional[float] = None
    deprn_catchup_amount: Optional[float] = None
    last_deprn_period_id: Optional[int] = None
    last_deprn_date: Optional[date] = None
    prorate_factor: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaAssetBookAssignmentsUpdate(BaseModel):
    assignment_id: Optional[int] = None
    asset_id: Optional[int] = None
    book_id: Optional[int] = None
    deprn_method_id: Optional[int] = None
    deprn_convention_id: Optional[int] = None
    useful_life_months: Optional[int] = None
    salvage_value: Optional[float] = None
    salvage_pct: Optional[float] = None
    deprn_start_date: Optional[date] = None
    deprn_end_date: Optional[date] = None
    deprn_remaining_months: Optional[int] = None
    original_cost: Optional[float] = None
    current_cost: Optional[float] = None
    accumulated_deprn: Optional[float] = None
    net_book_value: Optional[float] = None
    prior_ytd_deprn: Optional[float] = None
    prior_ltd_deprn: Optional[float] = None
    deprn_status_code: Optional[str] = None
    enable_bonus_deprn: Optional[str] = None
    bonus_deprn_pct: Optional[float] = None
    enable_section_179: Optional[str] = None
    section_179_amount: Optional[float] = None
    deprn_catchup_amount: Optional[float] = None
    last_deprn_period_id: Optional[int] = None
    last_deprn_date: Optional[date] = None
    prorate_factor: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaAssetBookAssignmentsOut(BaseModel):
    assignment_id: int
    asset_id: int
    book_id: int
    deprn_method_id: int
    deprn_convention_id: Optional[int] = None
    useful_life_months: int
    salvage_value: Optional[float] = None
    salvage_pct: Optional[float] = None
    deprn_start_date: date
    deprn_end_date: Optional[date] = None
    deprn_remaining_months: Optional[int] = None
    original_cost: float
    current_cost: Optional[float] = None
    accumulated_deprn: Optional[float] = None
    net_book_value: Optional[float] = None
    prior_ytd_deprn: Optional[float] = None
    prior_ltd_deprn: Optional[float] = None
    deprn_status_code: Optional[str] = None
    enable_bonus_deprn: Optional[str] = None
    bonus_deprn_pct: Optional[float] = None
    enable_section_179: Optional[str] = None
    section_179_amount: Optional[float] = None
    deprn_catchup_amount: Optional[float] = None
    last_deprn_period_id: Optional[int] = None
    last_deprn_date: Optional[date] = None
    prorate_factor: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaAssetCategoriesCreate(BaseModel):
    asset_category_id: int
    category_code: str
    category_name: str
    description: Optional[str] = None
    parent_category_id: Optional[int] = None
    category_level: Optional[int] = None
    category_path: Optional[str] = None
    asset_type_id: int
    default_deprn_method_id: Optional[int] = None
    default_useful_life: Optional[int] = None
    default_useful_life_uom: Optional[str] = None
    default_salvage_pct: Optional[float] = None
    capitalization_threshold: Optional[float] = None
    asset_account_id: Optional[int] = None
    deprn_account_id: Optional[int] = None
    deprn_expense_account_id: Optional[int] = None
    cip_account_id: Optional[int] = None
    insurance_category_code: Optional[str] = None
    tax_category_code: Optional[str] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaAssetCategoriesUpdate(BaseModel):
    asset_category_id: Optional[int] = None
    category_code: Optional[str] = None
    category_name: Optional[str] = None
    description: Optional[str] = None
    parent_category_id: Optional[int] = None
    category_level: Optional[int] = None
    category_path: Optional[str] = None
    asset_type_id: Optional[int] = None
    default_deprn_method_id: Optional[int] = None
    default_useful_life: Optional[int] = None
    default_useful_life_uom: Optional[str] = None
    default_salvage_pct: Optional[float] = None
    capitalization_threshold: Optional[float] = None
    asset_account_id: Optional[int] = None
    deprn_account_id: Optional[int] = None
    deprn_expense_account_id: Optional[int] = None
    cip_account_id: Optional[int] = None
    insurance_category_code: Optional[str] = None
    tax_category_code: Optional[str] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaAssetCategoriesOut(BaseModel):
    asset_category_id: int
    category_code: str
    category_name: str
    description: Optional[str] = None
    parent_category_id: Optional[int] = None
    category_level: Optional[int] = None
    category_path: Optional[str] = None
    asset_type_id: int
    default_deprn_method_id: Optional[int] = None
    default_useful_life: Optional[int] = None
    default_useful_life_uom: Optional[str] = None
    default_salvage_pct: Optional[float] = None
    capitalization_threshold: Optional[float] = None
    asset_account_id: Optional[int] = None
    deprn_account_id: Optional[int] = None
    deprn_expense_account_id: Optional[int] = None
    cip_account_id: Optional[int] = None
    insurance_category_code: Optional[str] = None
    tax_category_code: Optional[str] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaAssetCategoryHierarchyCreate(BaseModel):
    hierarchy_id: int
    parent_category_id: int
    child_category_id: int
    hierarchy_level: int
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class FaAssetCategoryHierarchyUpdate(BaseModel):
    hierarchy_id: Optional[int] = None
    parent_category_id: Optional[int] = None
    child_category_id: Optional[int] = None
    hierarchy_level: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class FaAssetCategoryHierarchyOut(BaseModel):
    hierarchy_id: int
    parent_category_id: int
    child_category_id: int
    hierarchy_level: int
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaAssetComponentsCreate(BaseModel):
    component_id: int
    parent_asset_id: int
    component_asset_id: Optional[int] = None
    component_name: str
    component_description: Optional[str] = None
    component_type_code: Optional[str] = None
    quantity: Optional[float] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    useful_life_months: Optional[int] = None
    serial_number: Optional[str] = None
    install_date: Optional[date] = None
    removal_date: Optional[date] = None
    is_critical: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaAssetComponentsUpdate(BaseModel):
    component_id: Optional[int] = None
    parent_asset_id: Optional[int] = None
    component_asset_id: Optional[int] = None
    component_name: Optional[str] = None
    component_description: Optional[str] = None
    component_type_code: Optional[str] = None
    quantity: Optional[float] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    useful_life_months: Optional[int] = None
    serial_number: Optional[str] = None
    install_date: Optional[date] = None
    removal_date: Optional[date] = None
    is_critical: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaAssetComponentsOut(BaseModel):
    component_id: int
    parent_asset_id: int
    component_asset_id: Optional[int] = None
    component_name: str
    component_description: Optional[str] = None
    component_type_code: Optional[str] = None
    quantity: Optional[float] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    useful_life_months: Optional[int] = None
    serial_number: Optional[str] = None
    install_date: Optional[date] = None
    removal_date: Optional[date] = None
    is_critical: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaAssetCustomAttributesCreate(BaseModel):
    attribute_id: int
    asset_id: int
    attribute_name: str
    attribute_value: Optional[str] = None
    attribute_type_code: Optional[str] = None
    attribute_group: Optional[str] = None
    is_required: Optional[str] = None
    display_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaAssetCustomAttributesUpdate(BaseModel):
    attribute_id: Optional[int] = None
    asset_id: Optional[int] = None
    attribute_name: Optional[str] = None
    attribute_value: Optional[str] = None
    attribute_type_code: Optional[str] = None
    attribute_group: Optional[str] = None
    is_required: Optional[str] = None
    display_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaAssetCustomAttributesOut(BaseModel):
    attribute_id: int
    asset_id: int
    attribute_name: str
    attribute_value: Optional[str] = None
    attribute_type_code: Optional[str] = None
    attribute_group: Optional[str] = None
    is_required: Optional[str] = None
    display_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaAssetPhotosCreate(BaseModel):
    photo_id: int
    asset_id: int
    photo_type_code: Optional[str] = None
    photo_timestamp: datetime
    gps_location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    storage_path: str
    thumbnail_path: Optional[str] = None
    file_name: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    photographer_id: Optional[int] = None
    photographer_name: Optional[str] = None
    description: Optional[str] = None
    annotations: Optional[dict] = None
    is_primary: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaAssetPhotosUpdate(BaseModel):
    photo_id: Optional[int] = None
    asset_id: Optional[int] = None
    photo_type_code: Optional[str] = None
    photo_timestamp: Optional[datetime] = None
    gps_location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    storage_path: Optional[str] = None
    thumbnail_path: Optional[str] = None
    file_name: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    photographer_id: Optional[int] = None
    photographer_name: Optional[str] = None
    description: Optional[str] = None
    annotations: Optional[dict] = None
    is_primary: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaAssetPhotosOut(BaseModel):
    photo_id: int
    asset_id: int
    photo_type_code: Optional[str] = None
    photo_timestamp: datetime
    gps_location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    storage_path: str
    thumbnail_path: Optional[str] = None
    file_name: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    photographer_id: Optional[int] = None
    photographer_name: Optional[str] = None
    description: Optional[str] = None
    annotations: Optional[dict] = None
    is_primary: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaAssetStorageCreate(BaseModel):
    result_id: int
    problem_id: int
    container_id: int
    container_type_code: str
    container_dimensions: Optional[dict] = None
    stored_assets: Optional[dict] = None
    utilization_percentage: Optional[float] = None
    num_assets_stored: Optional[int] = None
    avg_accessibility_score: Optional[float] = None
    weight_capacity: Optional[float] = None
    security_requirements: Optional[dict] = None
    environmental_controls: Optional[dict] = None
    retrieval_sequence: Optional[dict] = None
    visualization_3d_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class FaAssetStorageUpdate(BaseModel):
    result_id: Optional[int] = None
    problem_id: Optional[int] = None
    container_id: Optional[int] = None
    container_type_code: Optional[str] = None
    container_dimensions: Optional[dict] = None
    stored_assets: Optional[dict] = None
    utilization_percentage: Optional[float] = None
    num_assets_stored: Optional[int] = None
    avg_accessibility_score: Optional[float] = None
    weight_capacity: Optional[float] = None
    security_requirements: Optional[dict] = None
    environmental_controls: Optional[dict] = None
    retrieval_sequence: Optional[dict] = None
    visualization_3d_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class FaAssetStorageOut(BaseModel):
    result_id: int
    problem_id: int
    container_id: int
    container_type_code: str
    container_dimensions: Optional[dict] = None
    stored_assets: Optional[dict] = None
    utilization_percentage: Optional[float] = None
    num_assets_stored: Optional[int] = None
    avg_accessibility_score: Optional[float] = None
    weight_capacity: Optional[float] = None
    security_requirements: Optional[dict] = None
    environmental_controls: Optional[dict] = None
    retrieval_sequence: Optional[dict] = None
    visualization_3d_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaAssetTagsCreate(BaseModel):
    tag_id: int
    asset_id: int
    tag_type_code: str
    tag_value: str
    tag_format: Optional[str] = None
    issued_date: Optional[date] = None
    issued_by: Optional[str] = None
    tag_status_code: Optional[str] = None
    printer_id: Optional[str] = None
    print_job_id: Optional[str] = None
    replaced_by_tag_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaAssetTagsUpdate(BaseModel):
    tag_id: Optional[int] = None
    asset_id: Optional[int] = None
    tag_type_code: Optional[str] = None
    tag_value: Optional[str] = None
    tag_format: Optional[str] = None
    issued_date: Optional[date] = None
    issued_by: Optional[str] = None
    tag_status_code: Optional[str] = None
    printer_id: Optional[str] = None
    print_job_id: Optional[str] = None
    replaced_by_tag_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaAssetTagsOut(BaseModel):
    tag_id: int
    asset_id: int
    tag_type_code: str
    tag_value: str
    tag_format: Optional[str] = None
    issued_date: Optional[date] = None
    issued_by: Optional[str] = None
    tag_status_code: Optional[str] = None
    printer_id: Optional[str] = None
    print_job_id: Optional[str] = None
    replaced_by_tag_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaAssetTypesCreate(BaseModel):
    asset_type_id: int
    asset_type_code: str
    asset_type_name: str
    asset_class_code: str
    description: Optional[str] = None
    default_deprn_method_id: Optional[int] = None
    default_useful_life: Optional[int] = None
    default_useful_life_uom: Optional[str] = None
    default_salvage_pct: Optional[float] = None
    capitalization_threshold: Optional[float] = None
    insurance_category_code: Optional[str] = None
    tax_category_code: Optional[str] = None
    min_useful_life: Optional[int] = None
    max_useful_life: Optional[int] = None
    is_depreciable: Optional[str] = None
    is_leaseable: Optional[str] = None
    is_cip_enabled: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaAssetTypesUpdate(BaseModel):
    asset_type_id: Optional[int] = None
    asset_type_code: Optional[str] = None
    asset_type_name: Optional[str] = None
    asset_class_code: Optional[str] = None
    description: Optional[str] = None
    default_deprn_method_id: Optional[int] = None
    default_useful_life: Optional[int] = None
    default_useful_life_uom: Optional[str] = None
    default_salvage_pct: Optional[float] = None
    capitalization_threshold: Optional[float] = None
    insurance_category_code: Optional[str] = None
    tax_category_code: Optional[str] = None
    min_useful_life: Optional[int] = None
    max_useful_life: Optional[int] = None
    is_depreciable: Optional[str] = None
    is_leaseable: Optional[str] = None
    is_cip_enabled: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaAssetTypesOut(BaseModel):
    asset_type_id: int
    asset_type_code: str
    asset_type_name: str
    asset_class_code: str
    description: Optional[str] = None
    default_deprn_method_id: Optional[int] = None
    default_useful_life: Optional[int] = None
    default_useful_life_uom: Optional[str] = None
    default_salvage_pct: Optional[float] = None
    capitalization_threshold: Optional[float] = None
    insurance_category_code: Optional[str] = None
    tax_category_code: Optional[str] = None
    min_useful_life: Optional[int] = None
    max_useful_life: Optional[int] = None
    is_depreciable: Optional[str] = None
    is_leaseable: Optional[str] = None
    is_cip_enabled: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaAssetsCreate(BaseModel):
    asset_id: int
    asset_number: str
    asset_name: str
    description: Optional[str] = None
    asset_type_id: int
    asset_category_id: int
    manufacturer_id: Optional[int] = None
    manufacturer_name: Optional[str] = None
    model_number: Optional[str] = None
    serial_number: Optional[str] = None
    manufacture_date: Optional[date] = None
    acquisition_date: date
    in_service_date: date
    original_cost: float
    current_cost: float
    salvage_value: Optional[float] = None
    accumulated_depreciation: Optional[float] = None
    net_book_value: float
    fair_value: Optional[float] = None
    currency_code: str
    gps_location: Optional[str] = None
    location_id: Optional[int] = None
    custodian_id: Optional[int] = None
    asset_status_code: str
    condition_code: Optional[str] = None
    criticality_code: Optional[str] = None
    barcode: Optional[str] = None
    qr_code: Optional[str] = None
    rfid_tag: Optional[str] = None
    source_code: str
    purchase_order_id: Optional[int] = None
    supplier_id: Optional[int] = None
    project_id: Optional[int] = None
    lease_id: Optional[int] = None
    parent_asset_id: Optional[int] = None
    warranty_id: Optional[int] = None
    insurance_policy_id: Optional[int] = None
    source_system_code: Optional[str] = None
    source_asset_id: Optional[str] = None
    source_transaction_id: Optional[str] = None
    book_type_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaAssetsUpdate(BaseModel):
    asset_id: Optional[int] = None
    asset_number: Optional[str] = None
    asset_name: Optional[str] = None
    description: Optional[str] = None
    asset_type_id: Optional[int] = None
    asset_category_id: Optional[int] = None
    manufacturer_id: Optional[int] = None
    manufacturer_name: Optional[str] = None
    model_number: Optional[str] = None
    serial_number: Optional[str] = None
    manufacture_date: Optional[date] = None
    acquisition_date: Optional[date] = None
    in_service_date: Optional[date] = None
    original_cost: Optional[float] = None
    current_cost: Optional[float] = None
    salvage_value: Optional[float] = None
    accumulated_depreciation: Optional[float] = None
    net_book_value: Optional[float] = None
    fair_value: Optional[float] = None
    currency_code: Optional[str] = None
    gps_location: Optional[str] = None
    location_id: Optional[int] = None
    custodian_id: Optional[int] = None
    asset_status_code: Optional[str] = None
    condition_code: Optional[str] = None
    criticality_code: Optional[str] = None
    barcode: Optional[str] = None
    qr_code: Optional[str] = None
    rfid_tag: Optional[str] = None
    source_code: Optional[str] = None
    purchase_order_id: Optional[int] = None
    supplier_id: Optional[int] = None
    project_id: Optional[int] = None
    lease_id: Optional[int] = None
    parent_asset_id: Optional[int] = None
    warranty_id: Optional[int] = None
    insurance_policy_id: Optional[int] = None
    source_system_code: Optional[str] = None
    source_asset_id: Optional[str] = None
    source_transaction_id: Optional[str] = None
    book_type_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaAssetsOut(BaseModel):
    asset_id: int
    asset_number: str
    asset_name: str
    description: Optional[str] = None
    asset_type_id: int
    asset_category_id: int
    manufacturer_id: Optional[int] = None
    manufacturer_name: Optional[str] = None
    model_number: Optional[str] = None
    serial_number: Optional[str] = None
    manufacture_date: Optional[date] = None
    acquisition_date: date
    in_service_date: date
    original_cost: float
    current_cost: float
    salvage_value: Optional[float] = None
    accumulated_depreciation: Optional[float] = None
    net_book_value: float
    fair_value: Optional[float] = None
    currency_code: str
    gps_location: Optional[str] = None
    location_id: Optional[int] = None
    custodian_id: Optional[int] = None
    asset_status_code: str
    condition_code: Optional[str] = None
    criticality_code: Optional[str] = None
    barcode: Optional[str] = None
    qr_code: Optional[str] = None
    rfid_tag: Optional[str] = None
    source_code: str
    purchase_order_id: Optional[int] = None
    supplier_id: Optional[int] = None
    project_id: Optional[int] = None
    lease_id: Optional[int] = None
    parent_asset_id: Optional[int] = None
    warranty_id: Optional[int] = None
    insurance_policy_id: Optional[int] = None
    source_system_code: Optional[str] = None
    source_asset_id: Optional[str] = None
    source_transaction_id: Optional[str] = None
    book_type_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaBonusDepreciationCreate(BaseModel):
    bonus_id: int
    asset_id: int
    book_id: Optional[int] = None
    bonus_type_code: str
    bonus_year: int
    bonus_percentage: float
    bonus_amount: Optional[float] = None
    eligible_amount: Optional[float] = None
    is_elected: Optional[str] = None
    election_date: Optional[date] = None
    carryforward_amount: Optional[float] = None
    carryforward_year: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaBonusDepreciationUpdate(BaseModel):
    bonus_id: Optional[int] = None
    asset_id: Optional[int] = None
    book_id: Optional[int] = None
    bonus_type_code: Optional[str] = None
    bonus_year: Optional[int] = None
    bonus_percentage: Optional[float] = None
    bonus_amount: Optional[float] = None
    eligible_amount: Optional[float] = None
    is_elected: Optional[str] = None
    election_date: Optional[date] = None
    carryforward_amount: Optional[float] = None
    carryforward_year: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaBonusDepreciationOut(BaseModel):
    bonus_id: int
    asset_id: int
    book_id: Optional[int] = None
    bonus_type_code: str
    bonus_year: int
    bonus_percentage: float
    bonus_amount: Optional[float] = None
    eligible_amount: Optional[float] = None
    is_elected: Optional[str] = None
    election_date: Optional[date] = None
    carryforward_amount: Optional[float] = None
    carryforward_year: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaBookTypesCreate(BaseModel):
    book_type_id: int
    book_type_code: str
    book_type_name: str
    description: Optional[str] = None
    is_primary: Optional[str] = None
    is_tax_book: Optional[str] = None
    is_reporting_book: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaBookTypesUpdate(BaseModel):
    book_type_id: Optional[int] = None
    book_type_code: Optional[str] = None
    book_type_name: Optional[str] = None
    description: Optional[str] = None
    is_primary: Optional[str] = None
    is_tax_book: Optional[str] = None
    is_reporting_book: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaBookTypesOut(BaseModel):
    book_type_id: int
    book_type_code: str
    book_type_name: str
    description: Optional[str] = None
    is_primary: Optional[str] = None
    is_tax_book: Optional[str] = None
    is_reporting_book: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaCipCostsCreate(BaseModel):
    cip_cost_id: int
    cip_project_id: int
    cost_type_code: str
    cost_date: date
    cost_amount: float
    description: Optional[str] = None
    reference_doc_type: Optional[str] = None
    reference_doc_number: Optional[str] = None
    reference_doc_id: Optional[int] = None
    supplier_id: Optional[int] = None
    po_line_id: Optional[int] = None
    invoice_id: Optional[int] = None
    is_capitalizable: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None

class FaCipCostsUpdate(BaseModel):
    cip_cost_id: Optional[int] = None
    cip_project_id: Optional[int] = None
    cost_type_code: Optional[str] = None
    cost_date: Optional[date] = None
    cost_amount: Optional[float] = None
    description: Optional[str] = None
    reference_doc_type: Optional[str] = None
    reference_doc_number: Optional[str] = None
    reference_doc_id: Optional[int] = None
    supplier_id: Optional[int] = None
    po_line_id: Optional[int] = None
    invoice_id: Optional[int] = None
    is_capitalizable: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None

class FaCipCostsOut(BaseModel):
    cip_cost_id: int
    cip_project_id: int
    cost_type_code: str
    cost_date: date
    cost_amount: float
    description: Optional[str] = None
    reference_doc_type: Optional[str] = None
    reference_doc_number: Optional[str] = None
    reference_doc_id: Optional[int] = None
    supplier_id: Optional[int] = None
    po_line_id: Optional[int] = None
    invoice_id: Optional[int] = None
    is_capitalizable: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaCipProjectsCreate(BaseModel):
    cip_project_id: int
    project_code: str
    project_name: str
    description: Optional[str] = None
    asset_type_id: Optional[int] = None
    asset_category_id: Optional[int] = None
    start_date: date
    expected_completion_date: Optional[date] = None
    actual_completion_date: Optional[date] = None
    capitalization_date: Optional[date] = None
    cip_status_code: Optional[str] = None
    progress_pct: Optional[float] = None
    total_budget: Optional[float] = None
    total_costs: Optional[float] = None
    capitalized_cost: Optional[float] = None
    remaining_cost: Optional[float] = None
    material_cost: Optional[float] = None
    labor_cost: Optional[float] = None
    overhead_cost: Optional[float] = None
    interest_cost: Optional[float] = None
    other_cost: Optional[float] = None
    purchase_order_id: Optional[int] = None
    project_manager: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    target_asset_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None

class FaCipProjectsUpdate(BaseModel):
    cip_project_id: Optional[int] = None
    project_code: Optional[str] = None
    project_name: Optional[str] = None
    description: Optional[str] = None
    asset_type_id: Optional[int] = None
    asset_category_id: Optional[int] = None
    start_date: Optional[date] = None
    expected_completion_date: Optional[date] = None
    actual_completion_date: Optional[date] = None
    capitalization_date: Optional[date] = None
    cip_status_code: Optional[str] = None
    progress_pct: Optional[float] = None
    total_budget: Optional[float] = None
    total_costs: Optional[float] = None
    capitalized_cost: Optional[float] = None
    remaining_cost: Optional[float] = None
    material_cost: Optional[float] = None
    labor_cost: Optional[float] = None
    overhead_cost: Optional[float] = None
    interest_cost: Optional[float] = None
    other_cost: Optional[float] = None
    purchase_order_id: Optional[int] = None
    project_manager: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    target_asset_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None

class FaCipProjectsOut(BaseModel):
    cip_project_id: int
    project_code: str
    project_name: str
    description: Optional[str] = None
    asset_type_id: Optional[int] = None
    asset_category_id: Optional[int] = None
    start_date: date
    expected_completion_date: Optional[date] = None
    actual_completion_date: Optional[date] = None
    capitalization_date: Optional[date] = None
    cip_status_code: Optional[str] = None
    progress_pct: Optional[float] = None
    total_budget: Optional[float] = None
    total_costs: Optional[float] = None
    capitalized_cost: Optional[float] = None
    remaining_cost: Optional[float] = None
    material_cost: Optional[float] = None
    labor_cost: Optional[float] = None
    overhead_cost: Optional[float] = None
    interest_cost: Optional[float] = None
    other_cost: Optional[float] = None
    purchase_order_id: Optional[int] = None
    project_manager: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    target_asset_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaCountLinesCreate(BaseModel):
    count_line_id: int
    sheet_id: int
    count_id: int
    asset_id: int
    asset_number: str
    asset_description: Optional[str] = None
    expected_location_id: Optional[int] = None
    actual_location_id: Optional[int] = None
    expected_custodian_id: Optional[int] = None
    actual_custodian_id: Optional[int] = None
    barcode_expected: Optional[str] = None
    barcode_scanned: Optional[str] = None
    scan_id: Optional[int] = None
    scan_timestamp: Optional[datetime] = None
    scanned_by: Optional[int] = None
    gps_latitude: Optional[float] = None
    gps_longitude: Optional[float] = None
    gps_accuracy: Optional[float] = None
    is_scanned: Optional[str] = None
    line_status_code: Optional[str] = None
    variance_type_code: Optional[str] = None
    variance_notes: Optional[str] = None
    photo_id: Optional[int] = None
    signature_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class FaCountLinesUpdate(BaseModel):
    count_line_id: Optional[int] = None
    sheet_id: Optional[int] = None
    count_id: Optional[int] = None
    asset_id: Optional[int] = None
    asset_number: Optional[str] = None
    asset_description: Optional[str] = None
    expected_location_id: Optional[int] = None
    actual_location_id: Optional[int] = None
    expected_custodian_id: Optional[int] = None
    actual_custodian_id: Optional[int] = None
    barcode_expected: Optional[str] = None
    barcode_scanned: Optional[str] = None
    scan_id: Optional[int] = None
    scan_timestamp: Optional[datetime] = None
    scanned_by: Optional[int] = None
    gps_latitude: Optional[float] = None
    gps_longitude: Optional[float] = None
    gps_accuracy: Optional[float] = None
    is_scanned: Optional[str] = None
    line_status_code: Optional[str] = None
    variance_type_code: Optional[str] = None
    variance_notes: Optional[str] = None
    photo_id: Optional[int] = None
    signature_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class FaCountLinesOut(BaseModel):
    count_line_id: int
    sheet_id: int
    count_id: int
    asset_id: int
    asset_number: str
    asset_description: Optional[str] = None
    expected_location_id: Optional[int] = None
    actual_location_id: Optional[int] = None
    expected_custodian_id: Optional[int] = None
    actual_custodian_id: Optional[int] = None
    barcode_expected: Optional[str] = None
    barcode_scanned: Optional[str] = None
    scan_id: Optional[int] = None
    scan_timestamp: Optional[datetime] = None
    scanned_by: Optional[int] = None
    gps_latitude: Optional[float] = None
    gps_longitude: Optional[float] = None
    gps_accuracy: Optional[float] = None
    is_scanned: Optional[str] = None
    line_status_code: Optional[str] = None
    variance_type_code: Optional[str] = None
    variance_notes: Optional[str] = None
    photo_id: Optional[int] = None
    signature_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaCountRoutesCreate(BaseModel):
    result_id: int
    problem_id: int
    route_id: int
    counter_id: Optional[int] = None
    counter_name: Optional[str] = None
    team_id: Optional[int] = None
    route_sequence: Optional[dict] = None
    total_distance: Optional[float] = None
    total_duration: Optional[float] = None
    total_travel_time: Optional[float] = None
    total_count_time: Optional[float] = None
    num_assets: Optional[int] = None
    counter_skills: Optional[dict] = None
    shift_start: Optional[datetime] = None
    shift_end: Optional[datetime] = None
    high_value_assets_first: Optional[bool] = None
    critical_assets_first: Optional[bool] = None
    route_map_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class FaCountRoutesUpdate(BaseModel):
    result_id: Optional[int] = None
    problem_id: Optional[int] = None
    route_id: Optional[int] = None
    counter_id: Optional[int] = None
    counter_name: Optional[str] = None
    team_id: Optional[int] = None
    route_sequence: Optional[dict] = None
    total_distance: Optional[float] = None
    total_duration: Optional[float] = None
    total_travel_time: Optional[float] = None
    total_count_time: Optional[float] = None
    num_assets: Optional[int] = None
    counter_skills: Optional[dict] = None
    shift_start: Optional[datetime] = None
    shift_end: Optional[datetime] = None
    high_value_assets_first: Optional[bool] = None
    critical_assets_first: Optional[bool] = None
    route_map_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class FaCountRoutesOut(BaseModel):
    result_id: int
    problem_id: int
    route_id: int
    counter_id: Optional[int] = None
    counter_name: Optional[str] = None
    team_id: Optional[int] = None
    route_sequence: Optional[dict] = None
    total_distance: Optional[float] = None
    total_duration: Optional[float] = None
    total_travel_time: Optional[float] = None
    total_count_time: Optional[float] = None
    num_assets: Optional[int] = None
    counter_skills: Optional[dict] = None
    shift_start: Optional[datetime] = None
    shift_end: Optional[datetime] = None
    high_value_assets_first: Optional[bool] = None
    critical_assets_first: Optional[bool] = None
    route_map_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaCountSheetsCreate(BaseModel):
    sheet_id: int
    count_id: int
    sheet_number: str
    counter_id: Optional[int] = None
    counter_name: Optional[str] = None
    team_id: Optional[int] = None
    location_id: Optional[int] = None
    expected_count: Optional[int] = None
    scanned_count: Optional[int] = None
    sheet_status_code: Optional[str] = None
    assigned_date: Optional[datetime] = None
    started_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None
    synced_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class FaCountSheetsUpdate(BaseModel):
    sheet_id: Optional[int] = None
    count_id: Optional[int] = None
    sheet_number: Optional[str] = None
    counter_id: Optional[int] = None
    counter_name: Optional[str] = None
    team_id: Optional[int] = None
    location_id: Optional[int] = None
    expected_count: Optional[int] = None
    scanned_count: Optional[int] = None
    sheet_status_code: Optional[str] = None
    assigned_date: Optional[datetime] = None
    started_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None
    synced_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class FaCountSheetsOut(BaseModel):
    sheet_id: int
    count_id: int
    sheet_number: str
    counter_id: Optional[int] = None
    counter_name: Optional[str] = None
    team_id: Optional[int] = None
    location_id: Optional[int] = None
    expected_count: Optional[int] = None
    scanned_count: Optional[int] = None
    sheet_status_code: Optional[str] = None
    assigned_date: Optional[datetime] = None
    started_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None
    synced_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaCountVariancesCreate(BaseModel):
    variance_id: int
    count_line_id: int
    count_id: int
    asset_id: int
    variance_type_code: str
    variance_severity_code: Optional[str] = None
    expected_value: Optional[str] = None
    actual_value: Optional[str] = None
    variance_reason_code: Optional[str] = None
    variance_reason: Optional[str] = None
    investigator_id: Optional[int] = None
    investigation_notes: Optional[str] = None
    resolution_code: Optional[str] = None
    resolved_date: Optional[datetime] = None
    adjustment_amount: Optional[float] = None
    requires_adjustment: Optional[str] = None
    adjustment_pending: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaCountVariancesUpdate(BaseModel):
    variance_id: Optional[int] = None
    count_line_id: Optional[int] = None
    count_id: Optional[int] = None
    asset_id: Optional[int] = None
    variance_type_code: Optional[str] = None
    variance_severity_code: Optional[str] = None
    expected_value: Optional[str] = None
    actual_value: Optional[str] = None
    variance_reason_code: Optional[str] = None
    variance_reason: Optional[str] = None
    investigator_id: Optional[int] = None
    investigation_notes: Optional[str] = None
    resolution_code: Optional[str] = None
    resolved_date: Optional[datetime] = None
    adjustment_amount: Optional[float] = None
    requires_adjustment: Optional[str] = None
    adjustment_pending: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaCountVariancesOut(BaseModel):
    variance_id: int
    count_line_id: int
    count_id: int
    asset_id: int
    variance_type_code: str
    variance_severity_code: Optional[str] = None
    expected_value: Optional[str] = None
    actual_value: Optional[str] = None
    variance_reason_code: Optional[str] = None
    variance_reason: Optional[str] = None
    investigator_id: Optional[int] = None
    investigation_notes: Optional[str] = None
    resolution_code: Optional[str] = None
    resolved_date: Optional[datetime] = None
    adjustment_amount: Optional[float] = None
    requires_adjustment: Optional[str] = None
    adjustment_pending: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaCustodiansCreate(BaseModel):
    custodian_id: int
    custodian_code: str
    custodian_name: str
    custodian_type_code: Optional[str] = None
    employee_id: Optional[str] = None
    department_code: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    default_location_id: Optional[int] = None
    is_acknowledgment_req: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaCustodiansUpdate(BaseModel):
    custodian_id: Optional[int] = None
    custodian_code: Optional[str] = None
    custodian_name: Optional[str] = None
    custodian_type_code: Optional[str] = None
    employee_id: Optional[str] = None
    department_code: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    default_location_id: Optional[int] = None
    is_acknowledgment_req: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaCustodiansOut(BaseModel):
    custodian_id: int
    custodian_code: str
    custodian_name: str
    custodian_type_code: Optional[str] = None
    employee_id: Optional[str] = None
    department_code: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    default_location_id: Optional[int] = None
    is_acknowledgment_req: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaDeprnBookPeriodsCreate(BaseModel):
    period_id: int
    book_id: int
    period_name: str
    fiscal_year: int
    period_num: int
    period_type: Optional[str] = None
    start_date: date
    end_date: date
    period_status_code: Optional[str] = None
    deprn_run_date: Optional[datetime] = None
    deprn_posted_date: Optional[datetime] = None
    is_deprn_calculated: Optional[str] = None
    is_deprn_posted: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class FaDeprnBookPeriodsUpdate(BaseModel):
    period_id: Optional[int] = None
    book_id: Optional[int] = None
    period_name: Optional[str] = None
    fiscal_year: Optional[int] = None
    period_num: Optional[int] = None
    period_type: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    period_status_code: Optional[str] = None
    deprn_run_date: Optional[datetime] = None
    deprn_posted_date: Optional[datetime] = None
    is_deprn_calculated: Optional[str] = None
    is_deprn_posted: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class FaDeprnBookPeriodsOut(BaseModel):
    period_id: int
    book_id: int
    period_name: str
    fiscal_year: int
    period_num: int
    period_type: Optional[str] = None
    start_date: date
    end_date: date
    period_status_code: Optional[str] = None
    deprn_run_date: Optional[datetime] = None
    deprn_posted_date: Optional[datetime] = None
    is_deprn_calculated: Optional[str] = None
    is_deprn_posted: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaDeprnBooksCreate(BaseModel):
    book_id: int
    book_code: str
    book_name: str
    description: Optional[str] = None
    book_type_id: int
    currency_code: str
    fiscal_year_start_month: Optional[int] = None
    default_deprn_method_id: Optional[int] = None
    default_useful_life: Optional[int] = None
    capitalization_threshold: Optional[float] = None
    enable_bonus_deprn: Optional[str] = None
    enable_section_179: Optional[str] = None
    deprn_calendar_code: Optional[str] = None
    book_status_code: Optional[str] = None
    last_deprn_run_date: Optional[datetime] = None
    last_deprn_period_id: Optional[int] = None
    asset_account_id: Optional[int] = None
    deprn_account_id: Optional[int] = None
    deprn_expense_account_id: Optional[int] = None
    pnl_account_id: Optional[int] = None
    reporting_currency_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaDeprnBooksUpdate(BaseModel):
    book_id: Optional[int] = None
    book_code: Optional[str] = None
    book_name: Optional[str] = None
    description: Optional[str] = None
    book_type_id: Optional[int] = None
    currency_code: Optional[str] = None
    fiscal_year_start_month: Optional[int] = None
    default_deprn_method_id: Optional[int] = None
    default_useful_life: Optional[int] = None
    capitalization_threshold: Optional[float] = None
    enable_bonus_deprn: Optional[str] = None
    enable_section_179: Optional[str] = None
    deprn_calendar_code: Optional[str] = None
    book_status_code: Optional[str] = None
    last_deprn_run_date: Optional[datetime] = None
    last_deprn_period_id: Optional[int] = None
    asset_account_id: Optional[int] = None
    deprn_account_id: Optional[int] = None
    deprn_expense_account_id: Optional[int] = None
    pnl_account_id: Optional[int] = None
    reporting_currency_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaDeprnBooksOut(BaseModel):
    book_id: int
    book_code: str
    book_name: str
    description: Optional[str] = None
    book_type_id: int
    currency_code: str
    fiscal_year_start_month: Optional[int] = None
    default_deprn_method_id: Optional[int] = None
    default_useful_life: Optional[int] = None
    capitalization_threshold: Optional[float] = None
    enable_bonus_deprn: Optional[str] = None
    enable_section_179: Optional[str] = None
    deprn_calendar_code: Optional[str] = None
    book_status_code: Optional[str] = None
    last_deprn_run_date: Optional[datetime] = None
    last_deprn_period_id: Optional[int] = None
    asset_account_id: Optional[int] = None
    deprn_account_id: Optional[int] = None
    deprn_expense_account_id: Optional[int] = None
    pnl_account_id: Optional[int] = None
    reporting_currency_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaDeprnCalculationCreate(BaseModel):
    deprn_calc_id: int
    asset_id: int
    book_id: int
    period_id: int
    deprn_run_id: Optional[str] = None
    beginning_nbv: float
    deprn_amount: float
    ending_nbv: float
    ytd_deprn: Optional[float] = None
    ltd_deprn: Optional[float] = None
    bonus_deprn_amount: Optional[float] = None
    section_179_amount: Optional[float] = None
    deprn_status_code: Optional[str] = None
    deprn_posting_date: Optional[datetime] = None
    gl_journal_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None

class FaDeprnCalculationUpdate(BaseModel):
    deprn_calc_id: Optional[int] = None
    asset_id: Optional[int] = None
    book_id: Optional[int] = None
    period_id: Optional[int] = None
    deprn_run_id: Optional[str] = None
    beginning_nbv: Optional[float] = None
    deprn_amount: Optional[float] = None
    ending_nbv: Optional[float] = None
    ytd_deprn: Optional[float] = None
    ltd_deprn: Optional[float] = None
    bonus_deprn_amount: Optional[float] = None
    section_179_amount: Optional[float] = None
    deprn_status_code: Optional[str] = None
    deprn_posting_date: Optional[datetime] = None
    gl_journal_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None

class FaDeprnCalculationOut(BaseModel):
    deprn_calc_id: int
    asset_id: int
    book_id: int
    period_id: int
    deprn_run_id: Optional[str] = None
    beginning_nbv: float
    deprn_amount: float
    ending_nbv: float
    ytd_deprn: Optional[float] = None
    ltd_deprn: Optional[float] = None
    bonus_deprn_amount: Optional[float] = None
    section_179_amount: Optional[float] = None
    deprn_status_code: Optional[str] = None
    deprn_posting_date: Optional[datetime] = None
    gl_journal_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaDeprnConventionsCreate(BaseModel):
    deprn_convention_id: int
    convention_code: str
    convention_name: str
    description: Optional[str] = None
    convention_rule: Optional[str] = None
    first_year_factor: Optional[float] = None
    last_year_factor: Optional[float] = None
    is_prorate: Optional[str] = None
    is_mid_month: Optional[str] = None
    is_mid_quarter: Optional[str] = None
    is_half_year: Optional[str] = None
    is_full_year: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaDeprnConventionsUpdate(BaseModel):
    deprn_convention_id: Optional[int] = None
    convention_code: Optional[str] = None
    convention_name: Optional[str] = None
    description: Optional[str] = None
    convention_rule: Optional[str] = None
    first_year_factor: Optional[float] = None
    last_year_factor: Optional[float] = None
    is_prorate: Optional[str] = None
    is_mid_month: Optional[str] = None
    is_mid_quarter: Optional[str] = None
    is_half_year: Optional[str] = None
    is_full_year: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaDeprnConventionsOut(BaseModel):
    deprn_convention_id: int
    convention_code: str
    convention_name: str
    description: Optional[str] = None
    convention_rule: Optional[str] = None
    first_year_factor: Optional[float] = None
    last_year_factor: Optional[float] = None
    is_prorate: Optional[str] = None
    is_mid_month: Optional[str] = None
    is_mid_quarter: Optional[str] = None
    is_half_year: Optional[str] = None
    is_full_year: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaDeprnMethodsCreate(BaseModel):
    deprn_method_id: int
    method_code: str
    method_name: str
    description: Optional[str] = None
    method_type_code: str
    deprn_formula: Optional[str] = None
    deprn_parameter_1: Optional[float] = None
    deprn_parameter_2: Optional[float] = None
    switch_to_sl: Optional[str] = None
    switch_over_method_id: Optional[int] = None
    is_accelerated: Optional[str] = None
    is_macrs: Optional[str] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class FaDeprnMethodsUpdate(BaseModel):
    deprn_method_id: Optional[int] = None
    method_code: Optional[str] = None
    method_name: Optional[str] = None
    description: Optional[str] = None
    method_type_code: Optional[str] = None
    deprn_formula: Optional[str] = None
    deprn_parameter_1: Optional[float] = None
    deprn_parameter_2: Optional[float] = None
    switch_to_sl: Optional[str] = None
    switch_over_method_id: Optional[int] = None
    is_accelerated: Optional[str] = None
    is_macrs: Optional[str] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class FaDeprnMethodsOut(BaseModel):
    deprn_method_id: int
    method_code: str
    method_name: str
    description: Optional[str] = None
    method_type_code: str
    deprn_formula: Optional[str] = None
    deprn_parameter_1: Optional[float] = None
    deprn_parameter_2: Optional[float] = None
    switch_to_sl: Optional[str] = None
    switch_over_method_id: Optional[int] = None
    is_accelerated: Optional[str] = None
    is_macrs: Optional[str] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaGroupAssetMembersCreate(BaseModel):
    member_id: int
    group_id: int
    asset_id: int
    inclusion_date: date
    removal_date: Optional[date] = None
    member_cost: Optional[float] = None
    member_weight_pct: Optional[float] = None
    is_active: bool = True
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class FaGroupAssetMembersUpdate(BaseModel):
    member_id: Optional[int] = None
    group_id: Optional[int] = None
    asset_id: Optional[int] = None
    inclusion_date: Optional[date] = None
    removal_date: Optional[date] = None
    member_cost: Optional[float] = None
    member_weight_pct: Optional[float] = None
    is_active: Optional[bool] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class FaGroupAssetMembersOut(BaseModel):
    member_id: int
    group_id: int
    asset_id: int
    inclusion_date: date
    removal_date: Optional[date] = None
    member_cost: Optional[float] = None
    member_weight_pct: Optional[float] = None
    is_active: bool
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaGroupAssetsCreate(BaseModel):
    group_id: int
    group_code: str
    group_name: str
    description: Optional[str] = None
    group_type_code: str
    total_cost: Optional[float] = None
    total_accumulated_deprn: Optional[float] = None
    total_nbv: Optional[float] = None
    average_useful_life: Optional[int] = None
    deprn_method_id: Optional[int] = None
    member_count: Optional[int] = None
    group_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaGroupAssetsUpdate(BaseModel):
    group_id: Optional[int] = None
    group_code: Optional[str] = None
    group_name: Optional[str] = None
    description: Optional[str] = None
    group_type_code: Optional[str] = None
    total_cost: Optional[float] = None
    total_accumulated_deprn: Optional[float] = None
    total_nbv: Optional[float] = None
    average_useful_life: Optional[int] = None
    deprn_method_id: Optional[int] = None
    member_count: Optional[int] = None
    group_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaGroupAssetsOut(BaseModel):
    group_id: int
    group_code: str
    group_name: str
    description: Optional[str] = None
    group_type_code: str
    total_cost: Optional[float] = None
    total_accumulated_deprn: Optional[float] = None
    total_nbv: Optional[float] = None
    average_useful_life: Optional[int] = None
    deprn_method_id: Optional[int] = None
    member_count: Optional[int] = None
    group_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaImpairmentsCreate(BaseModel):
    impairment_id: int
    transaction_id: int
    asset_id: int
    book_id: Optional[int] = None
    impairment_date: date
    impairment_indicator_code: Optional[str] = None
    old_carrying_amount: Optional[float] = None
    recoverable_amount: Optional[float] = None
    impairment_amount: Optional[float] = None
    new_carrying_amount: Optional[float] = None
    fair_value: Optional[float] = None
    cost_to_sell: Optional[float] = None
    value_in_use: Optional[float] = None
    impairment_reason: Optional[str] = None
    impairment_test_method: Optional[str] = None
    impairment_report_url: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None

class FaImpairmentsUpdate(BaseModel):
    impairment_id: Optional[int] = None
    transaction_id: Optional[int] = None
    asset_id: Optional[int] = None
    book_id: Optional[int] = None
    impairment_date: Optional[date] = None
    impairment_indicator_code: Optional[str] = None
    old_carrying_amount: Optional[float] = None
    recoverable_amount: Optional[float] = None
    impairment_amount: Optional[float] = None
    new_carrying_amount: Optional[float] = None
    fair_value: Optional[float] = None
    cost_to_sell: Optional[float] = None
    value_in_use: Optional[float] = None
    impairment_reason: Optional[str] = None
    impairment_test_method: Optional[str] = None
    impairment_report_url: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None

class FaImpairmentsOut(BaseModel):
    impairment_id: int
    transaction_id: int
    asset_id: int
    book_id: Optional[int] = None
    impairment_date: date
    impairment_indicator_code: Optional[str] = None
    old_carrying_amount: Optional[float] = None
    recoverable_amount: Optional[float] = None
    impairment_amount: Optional[float] = None
    new_carrying_amount: Optional[float] = None
    fair_value: Optional[float] = None
    cost_to_sell: Optional[float] = None
    value_in_use: Optional[float] = None
    impairment_reason: Optional[str] = None
    impairment_test_method: Optional[str] = None
    impairment_report_url: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaInsuranceClaimsCreate(BaseModel):
    claim_id: int
    policy_id: int
    asset_id: Optional[int] = None
    claim_number: str
    claim_date: date
    claim_type_code: str
    claim_amount: float
    approved_amount: Optional[float] = None
    paid_amount: Optional[float] = None
    deductible_applied: Optional[float] = None
    claim_status_code: Optional[str] = None
    incident_description: Optional[str] = None
    incident_date: Optional[date] = None
    incident_location_id: Optional[int] = None
    adjuster_name: Optional[str] = None
    adjuster_phone: Optional[str] = None
    settlement_date: Optional[date] = None
    claim_document_url: Optional[str] = None
    rejection_reason: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaInsuranceClaimsUpdate(BaseModel):
    claim_id: Optional[int] = None
    policy_id: Optional[int] = None
    asset_id: Optional[int] = None
    claim_number: Optional[str] = None
    claim_date: Optional[date] = None
    claim_type_code: Optional[str] = None
    claim_amount: Optional[float] = None
    approved_amount: Optional[float] = None
    paid_amount: Optional[float] = None
    deductible_applied: Optional[float] = None
    claim_status_code: Optional[str] = None
    incident_description: Optional[str] = None
    incident_date: Optional[date] = None
    incident_location_id: Optional[int] = None
    adjuster_name: Optional[str] = None
    adjuster_phone: Optional[str] = None
    settlement_date: Optional[date] = None
    claim_document_url: Optional[str] = None
    rejection_reason: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaInsuranceClaimsOut(BaseModel):
    claim_id: int
    policy_id: int
    asset_id: Optional[int] = None
    claim_number: str
    claim_date: date
    claim_type_code: str
    claim_amount: float
    approved_amount: Optional[float] = None
    paid_amount: Optional[float] = None
    deductible_applied: Optional[float] = None
    claim_status_code: Optional[str] = None
    incident_description: Optional[str] = None
    incident_date: Optional[date] = None
    incident_location_id: Optional[int] = None
    adjuster_name: Optional[str] = None
    adjuster_phone: Optional[str] = None
    settlement_date: Optional[date] = None
    claim_document_url: Optional[str] = None
    rejection_reason: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaInsurancePoliciesCreate(BaseModel):
    policy_id: int
    policy_number: str
    policy_name: str
    insurance_company: str
    coverage_type_code: str
    coverage_amount: float
    deductible_amount: Optional[float] = None
    premium_amount: float
    premium_frequency: Optional[str] = None
    effective_date: date
    expiration_date: date
    auto_renewal: Optional[str] = None
    policy_status_code: Optional[str] = None
    policy_document_url: Optional[str] = None
    broker_name: Optional[str] = None
    broker_contact: Optional[str] = None
    terms_conditions: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaInsurancePoliciesUpdate(BaseModel):
    policy_id: Optional[int] = None
    policy_number: Optional[str] = None
    policy_name: Optional[str] = None
    insurance_company: Optional[str] = None
    coverage_type_code: Optional[str] = None
    coverage_amount: Optional[float] = None
    deductible_amount: Optional[float] = None
    premium_amount: Optional[float] = None
    premium_frequency: Optional[str] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    auto_renewal: Optional[str] = None
    policy_status_code: Optional[str] = None
    policy_document_url: Optional[str] = None
    broker_name: Optional[str] = None
    broker_contact: Optional[str] = None
    terms_conditions: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaInsurancePoliciesOut(BaseModel):
    policy_id: int
    policy_number: str
    policy_name: str
    insurance_company: str
    coverage_type_code: str
    coverage_amount: float
    deductible_amount: Optional[float] = None
    premium_amount: float
    premium_frequency: Optional[str] = None
    effective_date: date
    expiration_date: date
    auto_renewal: Optional[str] = None
    policy_status_code: Optional[str] = None
    policy_document_url: Optional[str] = None
    broker_name: Optional[str] = None
    broker_contact: Optional[str] = None
    terms_conditions: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaIntegrationConnectionsCreate(BaseModel):
    connection_id: int
    connection_name: str
    system_code: str
    integration_type_code: str
    endpoint_url: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    authentication_type: Optional[str] = None
    connection_properties: Optional[dict] = None
    is_active: bool = True
    last_test_date: Optional[datetime] = None
    last_test_status: Optional[str] = None
    error_count: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class FaIntegrationConnectionsUpdate(BaseModel):
    connection_id: Optional[int] = None
    connection_name: Optional[str] = None
    system_code: Optional[str] = None
    integration_type_code: Optional[str] = None
    endpoint_url: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    authentication_type: Optional[str] = None
    connection_properties: Optional[dict] = None
    is_active: Optional[bool] = None
    last_test_date: Optional[datetime] = None
    last_test_status: Optional[str] = None
    error_count: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class FaIntegrationConnectionsOut(BaseModel):
    connection_id: int
    connection_name: str
    system_code: str
    integration_type_code: str
    endpoint_url: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    authentication_type: Optional[str] = None
    connection_properties: Optional[dict] = None
    is_active: bool
    last_test_date: Optional[datetime] = None
    last_test_status: Optional[str] = None
    error_count: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaIntegrationLogsCreate(BaseModel):
    log_id: int
    connection_id: int
    integration_direction: str
    transaction_type: Optional[str] = None
    request_data: Optional[dict] = None
    response_data: Optional[dict] = None
    status_code: str
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    execution_time_ms: Optional[int] = None
    correlation_id: Optional[str] = None
    source_transaction_id: Optional[str] = None
    processed_timestamp: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class FaIntegrationLogsUpdate(BaseModel):
    log_id: Optional[int] = None
    connection_id: Optional[int] = None
    integration_direction: Optional[str] = None
    transaction_type: Optional[str] = None
    request_data: Optional[dict] = None
    response_data: Optional[dict] = None
    status_code: Optional[str] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    execution_time_ms: Optional[int] = None
    correlation_id: Optional[str] = None
    source_transaction_id: Optional[str] = None
    processed_timestamp: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class FaIntegrationLogsOut(BaseModel):
    log_id: int
    connection_id: int
    integration_direction: str
    transaction_type: Optional[str] = None
    request_data: Optional[dict] = None
    response_data: Optional[dict] = None
    status_code: str
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    execution_time_ms: Optional[int] = None
    correlation_id: Optional[str] = None
    source_transaction_id: Optional[str] = None
    processed_timestamp: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaLanggraphExecutionsCreate(BaseModel):
    execution_id: int
    workflow_id: int
    execution_name: Optional[str] = None
    input_data: Optional[dict] = None
    current_state: Optional[dict] = None
    execution_status_code: Optional[str] = None
    current_node: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_details: Optional[dict] = None
    retry_count: Optional[int] = None
    max_retries: Optional[int] = None
    checkpoint_data: Optional[dict] = None
    result_data: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    created_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class FaLanggraphExecutionsUpdate(BaseModel):
    execution_id: Optional[int] = None
    workflow_id: Optional[int] = None
    execution_name: Optional[str] = None
    input_data: Optional[dict] = None
    current_state: Optional[dict] = None
    execution_status_code: Optional[str] = None
    current_node: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_details: Optional[dict] = None
    retry_count: Optional[int] = None
    max_retries: Optional[int] = None
    checkpoint_data: Optional[dict] = None
    result_data: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    created_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class FaLanggraphExecutionsOut(BaseModel):
    execution_id: int
    workflow_id: int
    execution_name: Optional[str] = None
    input_data: Optional[dict] = None
    current_state: Optional[dict] = None
    execution_status_code: Optional[str] = None
    current_node: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_details: Optional[dict] = None
    retry_count: Optional[int] = None
    max_retries: Optional[int] = None
    checkpoint_data: Optional[dict] = None
    result_data: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    created_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaLanggraphStatesCreate(BaseModel):
    state_id: int
    execution_id: int
    node_id: str
    node_type: Optional[str] = None
    state_data: Optional[dict] = None
    node_input: Optional[dict] = None
    node_output: Optional[dict] = None
    node_status_code: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    retry_attempt: Optional[int] = None
    tool_calls: Optional[dict] = None
    llm_calls: Optional[dict] = None
    human_input: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class FaLanggraphStatesUpdate(BaseModel):
    state_id: Optional[int] = None
    execution_id: Optional[int] = None
    node_id: Optional[str] = None
    node_type: Optional[str] = None
    state_data: Optional[dict] = None
    node_input: Optional[dict] = None
    node_output: Optional[dict] = None
    node_status_code: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    retry_attempt: Optional[int] = None
    tool_calls: Optional[dict] = None
    llm_calls: Optional[dict] = None
    human_input: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class FaLanggraphStatesOut(BaseModel):
    state_id: int
    execution_id: int
    node_id: str
    node_type: Optional[str] = None
    state_data: Optional[dict] = None
    node_input: Optional[dict] = None
    node_output: Optional[dict] = None
    node_status_code: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    retry_attempt: Optional[int] = None
    tool_calls: Optional[dict] = None
    llm_calls: Optional[dict] = None
    human_input: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaLanggraphWorkflowsCreate(BaseModel):
    workflow_id: int
    workflow_name: str
    workflow_description: Optional[str] = None
    dag_definition: dict
    state_schema: Optional[dict] = None
    checkpoint_enabled: Optional[bool] = None
    hitl_nodes: Optional[dict] = None
    workflow_version: Optional[str] = None
    workflow_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaLanggraphWorkflowsUpdate(BaseModel):
    workflow_id: Optional[int] = None
    workflow_name: Optional[str] = None
    workflow_description: Optional[str] = None
    dag_definition: Optional[dict] = None
    state_schema: Optional[dict] = None
    checkpoint_enabled: Optional[bool] = None
    hitl_nodes: Optional[dict] = None
    workflow_version: Optional[str] = None
    workflow_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaLanggraphWorkflowsOut(BaseModel):
    workflow_id: int
    workflow_name: str
    workflow_description: Optional[str] = None
    dag_definition: dict
    state_schema: Optional[dict] = None
    checkpoint_enabled: Optional[bool] = None
    hitl_nodes: Optional[dict] = None
    workflow_version: Optional[str] = None
    workflow_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaLeaseAssetsCreate(BaseModel):
    lease_asset_id: int
    lease_id: int
    asset_id: int
    is_primary_asset: Optional[str] = None
    allocated_cost: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class FaLeaseAssetsUpdate(BaseModel):
    lease_asset_id: Optional[int] = None
    lease_id: Optional[int] = None
    asset_id: Optional[int] = None
    is_primary_asset: Optional[str] = None
    allocated_cost: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class FaLeaseAssetsOut(BaseModel):
    lease_asset_id: int
    lease_id: int
    asset_id: int
    is_primary_asset: Optional[str] = None
    allocated_cost: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaLeaseSchedulesCreate(BaseModel):
    schedule_id: int
    lease_id: int
    payment_num: int
    payment_date: date
    payment_amount: float
    interest_amount: Optional[float] = None
    principal_amount: Optional[float] = None
    outstanding_liability: Optional[float] = None
    rou_amortization: Optional[float] = None
    rou_balance: Optional[float] = None
    payment_status_code: Optional[str] = None
    actual_payment_date: Optional[date] = None
    actual_payment_amount: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class FaLeaseSchedulesUpdate(BaseModel):
    schedule_id: Optional[int] = None
    lease_id: Optional[int] = None
    payment_num: Optional[int] = None
    payment_date: Optional[date] = None
    payment_amount: Optional[float] = None
    interest_amount: Optional[float] = None
    principal_amount: Optional[float] = None
    outstanding_liability: Optional[float] = None
    rou_amortization: Optional[float] = None
    rou_balance: Optional[float] = None
    payment_status_code: Optional[str] = None
    actual_payment_date: Optional[date] = None
    actual_payment_amount: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class FaLeaseSchedulesOut(BaseModel):
    schedule_id: int
    lease_id: int
    payment_num: int
    payment_date: date
    payment_amount: float
    interest_amount: Optional[float] = None
    principal_amount: Optional[float] = None
    outstanding_liability: Optional[float] = None
    rou_amortization: Optional[float] = None
    rou_balance: Optional[float] = None
    payment_status_code: Optional[str] = None
    actual_payment_date: Optional[date] = None
    actual_payment_amount: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaLeasesCreate(BaseModel):
    lease_id: int
    lease_number: str
    lease_name: str
    lease_type_code: str
    lease_class_code: Optional[str] = None
    lease_status_code: Optional[str] = None
    lessor_name: Optional[str] = None
    lessor_reference: Optional[str] = None
    commencement_date: date
    termination_date: Optional[date] = None
    lease_term_months: int
    lease_end_date: date
    renewal_options: Optional[dict] = None
    purchase_options: Optional[dict] = None
    termination_options: Optional[dict] = None
    fixed_payment_amount: float
    variable_payment_desc: Optional[str] = None
    variable_payment_amount: Optional[float] = None
    residual_value_guarantee: Optional[float] = None
    initial_direct_costs: Optional[float] = None
    prepayments: Optional[float] = None
    lease_incentives: Optional[float] = None
    discount_rate: Optional[float] = None
    incremental_borrowing_rate: Optional[float] = None
    lease_liability: Optional[float] = None
    rou_asset_cost: Optional[float] = None
    rou_asset_accumulated_deprn: Optional[float] = None
    rou_asset_nbv: Optional[float] = None
    currency_code: Optional[str] = None
    payment_frequency: Optional[str] = None
    modification_details: Optional[dict] = None
    disclosure_notes: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaLeasesUpdate(BaseModel):
    lease_id: Optional[int] = None
    lease_number: Optional[str] = None
    lease_name: Optional[str] = None
    lease_type_code: Optional[str] = None
    lease_class_code: Optional[str] = None
    lease_status_code: Optional[str] = None
    lessor_name: Optional[str] = None
    lessor_reference: Optional[str] = None
    commencement_date: Optional[date] = None
    termination_date: Optional[date] = None
    lease_term_months: Optional[int] = None
    lease_end_date: Optional[date] = None
    renewal_options: Optional[dict] = None
    purchase_options: Optional[dict] = None
    termination_options: Optional[dict] = None
    fixed_payment_amount: Optional[float] = None
    variable_payment_desc: Optional[str] = None
    variable_payment_amount: Optional[float] = None
    residual_value_guarantee: Optional[float] = None
    initial_direct_costs: Optional[float] = None
    prepayments: Optional[float] = None
    lease_incentives: Optional[float] = None
    discount_rate: Optional[float] = None
    incremental_borrowing_rate: Optional[float] = None
    lease_liability: Optional[float] = None
    rou_asset_cost: Optional[float] = None
    rou_asset_accumulated_deprn: Optional[float] = None
    rou_asset_nbv: Optional[float] = None
    currency_code: Optional[str] = None
    payment_frequency: Optional[str] = None
    modification_details: Optional[dict] = None
    disclosure_notes: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaLeasesOut(BaseModel):
    lease_id: int
    lease_number: str
    lease_name: str
    lease_type_code: str
    lease_class_code: Optional[str] = None
    lease_status_code: Optional[str] = None
    lessor_name: Optional[str] = None
    lessor_reference: Optional[str] = None
    commencement_date: date
    termination_date: Optional[date] = None
    lease_term_months: int
    lease_end_date: date
    renewal_options: Optional[dict] = None
    purchase_options: Optional[dict] = None
    termination_options: Optional[dict] = None
    fixed_payment_amount: float
    variable_payment_desc: Optional[str] = None
    variable_payment_amount: Optional[float] = None
    residual_value_guarantee: Optional[float] = None
    initial_direct_costs: Optional[float] = None
    prepayments: Optional[float] = None
    lease_incentives: Optional[float] = None
    discount_rate: Optional[float] = None
    incremental_borrowing_rate: Optional[float] = None
    lease_liability: Optional[float] = None
    rou_asset_cost: Optional[float] = None
    rou_asset_accumulated_deprn: Optional[float] = None
    rou_asset_nbv: Optional[float] = None
    currency_code: Optional[str] = None
    payment_frequency: Optional[str] = None
    modification_details: Optional[dict] = None
    disclosure_notes: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaLlmConfigsCreate(BaseModel):
    llm_config_id: int
    config_name: str
    provider_name: str
    model_name: str
    api_key_encrypted: Optional[str] = None
    api_endpoint: Optional[str] = None
    parameters: Optional[dict] = None
    max_tokens: Optional[int] = None
    temperature: Optional[float] = None
    timeout_seconds: Optional[int] = None
    cost_per_1k_input: Optional[float] = None
    cost_per_1k_output: Optional[float] = None
    config_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaLlmConfigsUpdate(BaseModel):
    llm_config_id: Optional[int] = None
    config_name: Optional[str] = None
    provider_name: Optional[str] = None
    model_name: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    api_endpoint: Optional[str] = None
    parameters: Optional[dict] = None
    max_tokens: Optional[int] = None
    temperature: Optional[float] = None
    timeout_seconds: Optional[int] = None
    cost_per_1k_input: Optional[float] = None
    cost_per_1k_output: Optional[float] = None
    config_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaLlmConfigsOut(BaseModel):
    llm_config_id: int
    config_name: str
    provider_name: str
    model_name: str
    api_key_encrypted: Optional[str] = None
    api_endpoint: Optional[str] = None
    parameters: Optional[dict] = None
    max_tokens: Optional[int] = None
    temperature: Optional[float] = None
    timeout_seconds: Optional[int] = None
    cost_per_1k_input: Optional[float] = None
    cost_per_1k_output: Optional[float] = None
    config_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaLocationsCreate(BaseModel):
    location_id: int
    location_code: str
    location_name: str
    description: Optional[str] = None
    location_type_code: Optional[str] = None
    parent_location_id: Optional[int] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    gps_location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    supervisor_id: Optional[int] = None
    security_level_code: Optional[str] = None
    environmental_controls: Optional[dict] = None
    is_indoor: Optional[str] = None
    floor_plan_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaLocationsUpdate(BaseModel):
    location_id: Optional[int] = None
    location_code: Optional[str] = None
    location_name: Optional[str] = None
    description: Optional[str] = None
    location_type_code: Optional[str] = None
    parent_location_id: Optional[int] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    gps_location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    supervisor_id: Optional[int] = None
    security_level_code: Optional[str] = None
    environmental_controls: Optional[dict] = None
    is_indoor: Optional[str] = None
    floor_plan_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaLocationsOut(BaseModel):
    location_id: int
    location_code: str
    location_name: str
    description: Optional[str] = None
    location_type_code: Optional[str] = None
    parent_location_id: Optional[int] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    gps_location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    supervisor_id: Optional[int] = None
    security_level_code: Optional[str] = None
    environmental_controls: Optional[dict] = None
    is_indoor: Optional[str] = None
    floor_plan_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaMlModelsCreate(BaseModel):
    model_id: int
    model_name: str
    model_type_code: str
    model_framework: Optional[str] = None
    model_version: Optional[str] = None
    description: Optional[str] = None
    training_data_config: Optional[dict] = None
    training_parameters: Optional[dict] = None
    training_results: Optional[dict] = None
    validation_results: Optional[dict] = None
    model_artifact_path: Optional[str] = None
    model_endpoint_url: Optional[str] = None
    model_status_code: Optional[str] = None
    deployment_date: Optional[datetime] = None
    retraining_frequency: Optional[str] = None
    last_trained_date: Optional[datetime] = None
    accuracy_metrics: Optional[dict] = None
    feature_importance: Optional[dict] = None
    monitoring_config: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaMlModelsUpdate(BaseModel):
    model_id: Optional[int] = None
    model_name: Optional[str] = None
    model_type_code: Optional[str] = None
    model_framework: Optional[str] = None
    model_version: Optional[str] = None
    description: Optional[str] = None
    training_data_config: Optional[dict] = None
    training_parameters: Optional[dict] = None
    training_results: Optional[dict] = None
    validation_results: Optional[dict] = None
    model_artifact_path: Optional[str] = None
    model_endpoint_url: Optional[str] = None
    model_status_code: Optional[str] = None
    deployment_date: Optional[datetime] = None
    retraining_frequency: Optional[str] = None
    last_trained_date: Optional[datetime] = None
    accuracy_metrics: Optional[dict] = None
    feature_importance: Optional[dict] = None
    monitoring_config: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaMlModelsOut(BaseModel):
    model_id: int
    model_name: str
    model_type_code: str
    model_framework: Optional[str] = None
    model_version: Optional[str] = None
    description: Optional[str] = None
    training_data_config: Optional[dict] = None
    training_parameters: Optional[dict] = None
    training_results: Optional[dict] = None
    validation_results: Optional[dict] = None
    model_artifact_path: Optional[str] = None
    model_endpoint_url: Optional[str] = None
    model_status_code: Optional[str] = None
    deployment_date: Optional[datetime] = None
    retraining_frequency: Optional[str] = None
    last_trained_date: Optional[datetime] = None
    accuracy_metrics: Optional[dict] = None
    feature_importance: Optional[dict] = None
    monitoring_config: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaMobileDevicesCreate(BaseModel):
    device_id: int
    device_name: str
    device_type_code: str
    device_os: Optional[str] = None
    device_model: Optional[str] = None
    device_serial: Optional[str] = None
    imei_number: Optional[str] = None
    mac_address: Optional[str] = None
    device_status_code: Optional[str] = None
    assigned_to: Optional[int] = None
    last_sync_date: Optional[datetime] = None
    last_location: Optional[str] = None
    app_version: Optional[str] = None
    battery_level: Optional[int] = None
    storage_available: Optional[int] = None
    push_token: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaMobileDevicesUpdate(BaseModel):
    device_id: Optional[int] = None
    device_name: Optional[str] = None
    device_type_code: Optional[str] = None
    device_os: Optional[str] = None
    device_model: Optional[str] = None
    device_serial: Optional[str] = None
    imei_number: Optional[str] = None
    mac_address: Optional[str] = None
    device_status_code: Optional[str] = None
    assigned_to: Optional[int] = None
    last_sync_date: Optional[datetime] = None
    last_location: Optional[str] = None
    app_version: Optional[str] = None
    battery_level: Optional[int] = None
    storage_available: Optional[int] = None
    push_token: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaMobileDevicesOut(BaseModel):
    device_id: int
    device_name: str
    device_type_code: str
    device_os: Optional[str] = None
    device_model: Optional[str] = None
    device_serial: Optional[str] = None
    imei_number: Optional[str] = None
    mac_address: Optional[str] = None
    device_status_code: Optional[str] = None
    assigned_to: Optional[int] = None
    last_sync_date: Optional[datetime] = None
    last_location: Optional[str] = None
    app_version: Optional[str] = None
    battery_level: Optional[int] = None
    storage_available: Optional[int] = None
    push_token: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaMobileScansCreate(BaseModel):
    scan_id: int
    count_id: int
    asset_id: int
    asset_number: str
    barcode_scanned: Optional[str] = None
    scan_type_code: str
    scan_timestamp: datetime
    gps_location: Optional[str] = None
    gps_latitude: Optional[float] = None
    gps_longitude: Optional[float] = None
    gps_accuracy: Optional[float] = None
    expected_location_id: Optional[int] = None
    actual_location_id: Optional[int] = None
    scan_status_code: str
    variance_reason_code: Optional[str] = None
    variance_notes: Optional[str] = None
    counter_id: int
    counter_name: Optional[str] = None
    device_id: Optional[int] = None
    device_name: Optional[str] = None
    notes: Optional[str] = None
    note_type_code: Optional[str] = None
    sync_status_code: Optional[str] = None
    sync_timestamp: Optional[datetime] = None
    sync_error: Optional[str] = None
    batch_id: Optional[str] = None
    source_system_code: Optional[str] = None
    source_scan_id: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaMobileScansUpdate(BaseModel):
    scan_id: Optional[int] = None
    count_id: Optional[int] = None
    asset_id: Optional[int] = None
    asset_number: Optional[str] = None
    barcode_scanned: Optional[str] = None
    scan_type_code: Optional[str] = None
    scan_timestamp: Optional[datetime] = None
    gps_location: Optional[str] = None
    gps_latitude: Optional[float] = None
    gps_longitude: Optional[float] = None
    gps_accuracy: Optional[float] = None
    expected_location_id: Optional[int] = None
    actual_location_id: Optional[int] = None
    scan_status_code: Optional[str] = None
    variance_reason_code: Optional[str] = None
    variance_notes: Optional[str] = None
    counter_id: Optional[int] = None
    counter_name: Optional[str] = None
    device_id: Optional[int] = None
    device_name: Optional[str] = None
    notes: Optional[str] = None
    note_type_code: Optional[str] = None
    sync_status_code: Optional[str] = None
    sync_timestamp: Optional[datetime] = None
    sync_error: Optional[str] = None
    batch_id: Optional[str] = None
    source_system_code: Optional[str] = None
    source_scan_id: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaMobileScansOut(BaseModel):
    scan_id: int
    count_id: int
    asset_id: int
    asset_number: str
    barcode_scanned: Optional[str] = None
    scan_type_code: str
    scan_timestamp: datetime
    gps_location: Optional[str] = None
    gps_latitude: Optional[float] = None
    gps_longitude: Optional[float] = None
    gps_accuracy: Optional[float] = None
    expected_location_id: Optional[int] = None
    actual_location_id: Optional[int] = None
    scan_status_code: str
    variance_reason_code: Optional[str] = None
    variance_notes: Optional[str] = None
    counter_id: int
    counter_name: Optional[str] = None
    device_id: Optional[int] = None
    device_name: Optional[str] = None
    notes: Optional[str] = None
    note_type_code: Optional[str] = None
    sync_status_code: Optional[str] = None
    sync_timestamp: Optional[datetime] = None
    sync_error: Optional[str] = None
    batch_id: Optional[str] = None
    source_system_code: Optional[str] = None
    source_scan_id: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaMobileSyncBatchesCreate(BaseModel):
    batch_id: str
    mobile_user_id: Optional[int] = None
    device_id: Optional[int] = None
    batch_timestamp: Optional[datetime] = None
    batch_status_code: Optional[str] = None
    record_count: Optional[int] = None
    photo_count: Optional[int] = None
    signature_count: Optional[int] = None
    success_count: Optional[int] = None
    error_count: Optional[int] = None
    conflict_count: Optional[int] = None
    error_details: Optional[dict] = None
    conflict_details: Optional[dict] = None
    processed_timestamp: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class FaMobileSyncBatchesUpdate(BaseModel):
    batch_id: Optional[str] = None
    mobile_user_id: Optional[int] = None
    device_id: Optional[int] = None
    batch_timestamp: Optional[datetime] = None
    batch_status_code: Optional[str] = None
    record_count: Optional[int] = None
    photo_count: Optional[int] = None
    signature_count: Optional[int] = None
    success_count: Optional[int] = None
    error_count: Optional[int] = None
    conflict_count: Optional[int] = None
    error_details: Optional[dict] = None
    conflict_details: Optional[dict] = None
    processed_timestamp: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class FaMobileSyncBatchesOut(BaseModel):
    batch_id: str
    mobile_user_id: Optional[int] = None
    device_id: Optional[int] = None
    batch_timestamp: Optional[datetime] = None
    batch_status_code: Optional[str] = None
    record_count: Optional[int] = None
    photo_count: Optional[int] = None
    signature_count: Optional[int] = None
    success_count: Optional[int] = None
    error_count: Optional[int] = None
    conflict_count: Optional[int] = None
    error_details: Optional[dict] = None
    conflict_details: Optional[dict] = None
    processed_timestamp: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaMobileUsersCreate(BaseModel):
    mobile_user_id: int
    custodian_id: int
    username: str
    role_code: str
    permissions: Optional[dict] = None
    assigned_devices: Optional[dict] = None
    last_login: Optional[datetime] = None
    is_online: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaMobileUsersUpdate(BaseModel):
    mobile_user_id: Optional[int] = None
    custodian_id: Optional[int] = None
    username: Optional[str] = None
    role_code: Optional[str] = None
    permissions: Optional[dict] = None
    assigned_devices: Optional[dict] = None
    last_login: Optional[datetime] = None
    is_online: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaMobileUsersOut(BaseModel):
    mobile_user_id: int
    custodian_id: int
    username: str
    role_code: str
    permissions: Optional[dict] = None
    assigned_devices: Optional[dict] = None
    last_login: Optional[datetime] = None
    is_online: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaOptimizationProblemsCreate(BaseModel):
    problem_id: int
    problem_name: str
    problem_type_code: str
    problem_description: Optional[str] = None
    objective_type_code: str
    objective_function: Optional[dict] = None
    constraints: Optional[dict] = None
    variables: Optional[dict] = None
    parameters: Optional[dict] = None
    data_sources: Optional[dict] = None
    solver_type_code: Optional[str] = None
    solver_config: Optional[dict] = None
    problem_status_code: Optional[str] = None
    solution_id: Optional[int] = None
    solve_time_ms: Optional[int] = None
    objective_value: Optional[float] = None
    solution_results: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class FaOptimizationProblemsUpdate(BaseModel):
    problem_id: Optional[int] = None
    problem_name: Optional[str] = None
    problem_type_code: Optional[str] = None
    problem_description: Optional[str] = None
    objective_type_code: Optional[str] = None
    objective_function: Optional[dict] = None
    constraints: Optional[dict] = None
    variables: Optional[dict] = None
    parameters: Optional[dict] = None
    data_sources: Optional[dict] = None
    solver_type_code: Optional[str] = None
    solver_config: Optional[dict] = None
    problem_status_code: Optional[str] = None
    solution_id: Optional[int] = None
    solve_time_ms: Optional[int] = None
    objective_value: Optional[float] = None
    solution_results: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class FaOptimizationProblemsOut(BaseModel):
    problem_id: int
    problem_name: str
    problem_type_code: str
    problem_description: Optional[str] = None
    objective_type_code: str
    objective_function: Optional[dict] = None
    constraints: Optional[dict] = None
    variables: Optional[dict] = None
    parameters: Optional[dict] = None
    data_sources: Optional[dict] = None
    solver_type_code: Optional[str] = None
    solver_config: Optional[dict] = None
    problem_status_code: Optional[str] = None
    solution_id: Optional[int] = None
    solve_time_ms: Optional[int] = None
    objective_value: Optional[float] = None
    solution_results: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaOrtoolsProblemsCreate(BaseModel):
    ortools_problem_id: int
    problem_name: str
    ortools_problem_type: str
    problem_definition: dict
    problem_data: Optional[dict] = None
    solver_parameters: Optional[dict] = None
    solution_results: Optional[dict] = None
    solution_quality_code: Optional[str] = None
    solve_time_seconds: Optional[float] = None
    objective_value: Optional[float] = None
    is_optimal: Optional[bool] = None
    gap_pct: Optional[float] = None
    execution_log: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaOrtoolsProblemsUpdate(BaseModel):
    ortools_problem_id: Optional[int] = None
    problem_name: Optional[str] = None
    ortools_problem_type: Optional[str] = None
    problem_definition: Optional[dict] = None
    problem_data: Optional[dict] = None
    solver_parameters: Optional[dict] = None
    solution_results: Optional[dict] = None
    solution_quality_code: Optional[str] = None
    solve_time_seconds: Optional[float] = None
    objective_value: Optional[float] = None
    is_optimal: Optional[bool] = None
    gap_pct: Optional[float] = None
    execution_log: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaOrtoolsProblemsOut(BaseModel):
    ortools_problem_id: int
    problem_name: str
    ortools_problem_type: str
    problem_definition: dict
    problem_data: Optional[dict] = None
    solver_parameters: Optional[dict] = None
    solution_results: Optional[dict] = None
    solution_quality_code: Optional[str] = None
    solve_time_seconds: Optional[float] = None
    objective_value: Optional[float] = None
    is_optimal: Optional[bool] = None
    gap_pct: Optional[float] = None
    execution_log: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaPhotosCreate(BaseModel):
    photo_id: int
    entity_type_code: str
    entity_id: int
    photo_type_code: Optional[str] = None
    file_name: str
    storage_path: str
    thumbnail_path: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    gps_location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    taken_by: Optional[str] = None
    taken_timestamp: Optional[datetime] = None
    device_id: Optional[int] = None
    annotations: Optional[dict] = None
    is_synced: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaPhotosUpdate(BaseModel):
    photo_id: Optional[int] = None
    entity_type_code: Optional[str] = None
    entity_id: Optional[int] = None
    photo_type_code: Optional[str] = None
    file_name: Optional[str] = None
    storage_path: Optional[str] = None
    thumbnail_path: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    gps_location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    taken_by: Optional[str] = None
    taken_timestamp: Optional[datetime] = None
    device_id: Optional[int] = None
    annotations: Optional[dict] = None
    is_synced: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaPhotosOut(BaseModel):
    photo_id: int
    entity_type_code: str
    entity_id: int
    photo_type_code: Optional[str] = None
    file_name: str
    storage_path: str
    thumbnail_path: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    gps_location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    taken_by: Optional[str] = None
    taken_timestamp: Optional[datetime] = None
    device_id: Optional[int] = None
    annotations: Optional[dict] = None
    is_synced: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaPhysicalCountsCreate(BaseModel):
    count_id: int
    count_name: str
    description: Optional[str] = None
    count_type_code: str
    count_status_code: Optional[str] = None
    count_start_date: Optional[datetime] = None
    count_end_date: Optional[datetime] = None
    planned_date: Optional[date] = None
    scope_json: Optional[dict] = None
    expected_asset_count: Optional[int] = None
    scanned_asset_count: Optional[int] = None
    missing_asset_count: Optional[int] = None
    excess_asset_count: Optional[int] = None
    wrong_location_count: Optional[int] = None
    variance_pct: Optional[float] = None
    location_id: Optional[int] = None
    asset_category_id: Optional[int] = None
    custodian_id: Optional[int] = None
    supervisor_id: Optional[int] = None
    count_team_count: Optional[int] = None
    is_mobile_enabled: Optional[str] = None
    sync_status_code: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaPhysicalCountsUpdate(BaseModel):
    count_id: Optional[int] = None
    count_name: Optional[str] = None
    description: Optional[str] = None
    count_type_code: Optional[str] = None
    count_status_code: Optional[str] = None
    count_start_date: Optional[datetime] = None
    count_end_date: Optional[datetime] = None
    planned_date: Optional[date] = None
    scope_json: Optional[dict] = None
    expected_asset_count: Optional[int] = None
    scanned_asset_count: Optional[int] = None
    missing_asset_count: Optional[int] = None
    excess_asset_count: Optional[int] = None
    wrong_location_count: Optional[int] = None
    variance_pct: Optional[float] = None
    location_id: Optional[int] = None
    asset_category_id: Optional[int] = None
    custodian_id: Optional[int] = None
    supervisor_id: Optional[int] = None
    count_team_count: Optional[int] = None
    is_mobile_enabled: Optional[str] = None
    sync_status_code: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaPhysicalCountsOut(BaseModel):
    count_id: int
    count_name: str
    description: Optional[str] = None
    count_type_code: str
    count_status_code: Optional[str] = None
    count_start_date: Optional[datetime] = None
    count_end_date: Optional[datetime] = None
    planned_date: Optional[date] = None
    scope_json: Optional[dict] = None
    expected_asset_count: Optional[int] = None
    scanned_asset_count: Optional[int] = None
    missing_asset_count: Optional[int] = None
    excess_asset_count: Optional[int] = None
    wrong_location_count: Optional[int] = None
    variance_pct: Optional[float] = None
    location_id: Optional[int] = None
    asset_category_id: Optional[int] = None
    custodian_id: Optional[int] = None
    supervisor_id: Optional[int] = None
    count_team_count: Optional[int] = None
    is_mobile_enabled: Optional[str] = None
    sync_status_code: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaPredictionActualsCreate(BaseModel):
    actual_id: int
    prediction_id: int
    entity_type_code: str
    entity_id: int
    actual_value: Optional[float] = None
    actual_date: Optional[date] = None
    actual_label: Optional[str] = None
    actual_details: Optional[dict] = None
    prediction_error: Optional[float] = None
    error_pct: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class FaPredictionActualsUpdate(BaseModel):
    actual_id: Optional[int] = None
    prediction_id: Optional[int] = None
    entity_type_code: Optional[str] = None
    entity_id: Optional[int] = None
    actual_value: Optional[float] = None
    actual_date: Optional[date] = None
    actual_label: Optional[str] = None
    actual_details: Optional[dict] = None
    prediction_error: Optional[float] = None
    error_pct: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class FaPredictionActualsOut(BaseModel):
    actual_id: int
    prediction_id: int
    entity_type_code: str
    entity_id: int
    actual_value: Optional[float] = None
    actual_date: Optional[date] = None
    actual_label: Optional[str] = None
    actual_details: Optional[dict] = None
    prediction_error: Optional[float] = None
    error_pct: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaPredictionsCreate(BaseModel):
    prediction_id: int
    model_id: int
    prediction_type_code: str
    entity_type_code: str
    entity_id: int
    prediction_date: datetime
    prediction_horizon: Optional[str] = None
    prediction_value: Optional[float] = None
    prediction_probability: Optional[float] = None
    prediction_label: Optional[str] = None
    prediction_features: Optional[dict] = None
    prediction_explanation: Optional[str] = None
    confidence_score: Optional[float] = None
    scenario_id: Optional[int] = None
    actual_value: Optional[float] = None
    actual_outcome_date: Optional[datetime] = None
    prediction_error: Optional[float] = None
    is_validated: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaPredictionsUpdate(BaseModel):
    prediction_id: Optional[int] = None
    model_id: Optional[int] = None
    prediction_type_code: Optional[str] = None
    entity_type_code: Optional[str] = None
    entity_id: Optional[int] = None
    prediction_date: Optional[datetime] = None
    prediction_horizon: Optional[str] = None
    prediction_value: Optional[float] = None
    prediction_probability: Optional[float] = None
    prediction_label: Optional[str] = None
    prediction_features: Optional[dict] = None
    prediction_explanation: Optional[str] = None
    confidence_score: Optional[float] = None
    scenario_id: Optional[int] = None
    actual_value: Optional[float] = None
    actual_outcome_date: Optional[datetime] = None
    prediction_error: Optional[float] = None
    is_validated: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaPredictionsOut(BaseModel):
    prediction_id: int
    model_id: int
    prediction_type_code: str
    entity_type_code: str
    entity_id: int
    prediction_date: datetime
    prediction_horizon: Optional[str] = None
    prediction_value: Optional[float] = None
    prediction_probability: Optional[float] = None
    prediction_label: Optional[str] = None
    prediction_features: Optional[dict] = None
    prediction_explanation: Optional[str] = None
    confidence_score: Optional[float] = None
    scenario_id: Optional[int] = None
    actual_value: Optional[float] = None
    actual_outcome_date: Optional[datetime] = None
    prediction_error: Optional[float] = None
    is_validated: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaPromptTemplatesCreate(BaseModel):
    prompt_id: int
    template_name: str
    template_type_code: str
    template_text: str
    template_variables: Optional[dict] = None
    template_version: Optional[str] = None
    llm_config_id: Optional[int] = None
    output_schema: Optional[dict] = None
    example_outputs: Optional[dict] = None
    performance_metrics: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaPromptTemplatesUpdate(BaseModel):
    prompt_id: Optional[int] = None
    template_name: Optional[str] = None
    template_type_code: Optional[str] = None
    template_text: Optional[str] = None
    template_variables: Optional[dict] = None
    template_version: Optional[str] = None
    llm_config_id: Optional[int] = None
    output_schema: Optional[dict] = None
    example_outputs: Optional[dict] = None
    performance_metrics: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaPromptTemplatesOut(BaseModel):
    prompt_id: int
    template_name: str
    template_type_code: str
    template_text: str
    template_variables: Optional[dict] = None
    template_version: Optional[str] = None
    llm_config_id: Optional[int] = None
    output_schema: Optional[dict] = None
    example_outputs: Optional[dict] = None
    performance_metrics: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaReinstatementsCreate(BaseModel):
    reinstatement_id: int
    transaction_id: int
    asset_id: int
    retirement_id: int
    reinstatement_date: date
    reinstatement_amount: Optional[float] = None
    reinstatement_reason: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaReinstatementsUpdate(BaseModel):
    reinstatement_id: Optional[int] = None
    transaction_id: Optional[int] = None
    asset_id: Optional[int] = None
    retirement_id: Optional[int] = None
    reinstatement_date: Optional[date] = None
    reinstatement_amount: Optional[float] = None
    reinstatement_reason: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaReinstatementsOut(BaseModel):
    reinstatement_id: int
    transaction_id: int
    asset_id: int
    retirement_id: int
    reinstatement_date: date
    reinstatement_amount: Optional[float] = None
    reinstatement_reason: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaReportSchedulesCreate(BaseModel):
    schedule_id: int
    report_id: int
    schedule_name: str
    frequency_code: str
    cron_expression: Optional[str] = None
    parameters: Optional[dict] = None
    recipients: Optional[dict] = None
    output_format: Optional[str] = None
    distribution_list: Optional[dict] = None
    last_run_date: Optional[datetime] = None
    next_run_date: Optional[datetime] = None
    schedule_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaReportSchedulesUpdate(BaseModel):
    schedule_id: Optional[int] = None
    report_id: Optional[int] = None
    schedule_name: Optional[str] = None
    frequency_code: Optional[str] = None
    cron_expression: Optional[str] = None
    parameters: Optional[dict] = None
    recipients: Optional[dict] = None
    output_format: Optional[str] = None
    distribution_list: Optional[dict] = None
    last_run_date: Optional[datetime] = None
    next_run_date: Optional[datetime] = None
    schedule_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaReportSchedulesOut(BaseModel):
    schedule_id: int
    report_id: int
    schedule_name: str
    frequency_code: str
    cron_expression: Optional[str] = None
    parameters: Optional[dict] = None
    recipients: Optional[dict] = None
    output_format: Optional[str] = None
    distribution_list: Optional[dict] = None
    last_run_date: Optional[datetime] = None
    next_run_date: Optional[datetime] = None
    schedule_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaReportsCreate(BaseModel):
    report_id: int
    report_code: str
    report_name: str
    description: Optional[str] = None
    report_type_code: str
    report_parameters: Optional[dict] = None
    output_format: Optional[str] = None
    report_template: Optional[str] = None
    is_scheduled: Optional[str] = None
    schedule_cron: Optional[str] = None
    last_generated_date: Optional[datetime] = None
    last_generated_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class FaReportsUpdate(BaseModel):
    report_id: Optional[int] = None
    report_code: Optional[str] = None
    report_name: Optional[str] = None
    description: Optional[str] = None
    report_type_code: Optional[str] = None
    report_parameters: Optional[dict] = None
    output_format: Optional[str] = None
    report_template: Optional[str] = None
    is_scheduled: Optional[str] = None
    schedule_cron: Optional[str] = None
    last_generated_date: Optional[datetime] = None
    last_generated_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class FaReportsOut(BaseModel):
    report_id: int
    report_code: str
    report_name: str
    description: Optional[str] = None
    report_type_code: str
    report_parameters: Optional[dict] = None
    output_format: Optional[str] = None
    report_template: Optional[str] = None
    is_scheduled: Optional[str] = None
    schedule_cron: Optional[str] = None
    last_generated_date: Optional[datetime] = None
    last_generated_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaRetirementsCreate(BaseModel):
    retirement_id: int
    transaction_id: int
    asset_id: int
    retirement_type_code: str
    retirement_date: date
    original_cost: Optional[float] = None
    accumulated_deprn: Optional[float] = None
    net_book_value: Optional[float] = None
    proceeds_amount: Optional[float] = None
    gain_loss_amount: Optional[float] = None
    buyer_name: Optional[str] = None
    buyer_reference: Optional[str] = None
    retirement_reason: Optional[str] = None
    is_partial: Optional[str] = None
    component_id: Optional[int] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaRetirementsUpdate(BaseModel):
    retirement_id: Optional[int] = None
    transaction_id: Optional[int] = None
    asset_id: Optional[int] = None
    retirement_type_code: Optional[str] = None
    retirement_date: Optional[date] = None
    original_cost: Optional[float] = None
    accumulated_deprn: Optional[float] = None
    net_book_value: Optional[float] = None
    proceeds_amount: Optional[float] = None
    gain_loss_amount: Optional[float] = None
    buyer_name: Optional[str] = None
    buyer_reference: Optional[str] = None
    retirement_reason: Optional[str] = None
    is_partial: Optional[str] = None
    component_id: Optional[int] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaRetirementsOut(BaseModel):
    retirement_id: int
    transaction_id: int
    asset_id: int
    retirement_type_code: str
    retirement_date: date
    original_cost: Optional[float] = None
    accumulated_deprn: Optional[float] = None
    net_book_value: Optional[float] = None
    proceeds_amount: Optional[float] = None
    gain_loss_amount: Optional[float] = None
    buyer_name: Optional[str] = None
    buyer_reference: Optional[str] = None
    retirement_reason: Optional[str] = None
    is_partial: Optional[str] = None
    component_id: Optional[int] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaRevaluationsCreate(BaseModel):
    revaluation_id: int
    transaction_id: int
    asset_id: int
    book_id: Optional[int] = None
    revaluation_date: date
    old_cost: Optional[float] = None
    new_cost: Optional[float] = None
    old_accumulated_deprn: Optional[float] = None
    new_accumulated_deprn: Optional[float] = None
    old_nbv: Optional[float] = None
    new_nbv: Optional[float] = None
    revaluation_surplus: Optional[float] = None
    revaluation_deficit: Optional[float] = None
    revaluation_reason_code: Optional[str] = None
    appraiser_name: Optional[str] = None
    appraiser_company: Optional[str] = None
    appraisal_date: Optional[date] = None
    appraisal_report_url: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaRevaluationsUpdate(BaseModel):
    revaluation_id: Optional[int] = None
    transaction_id: Optional[int] = None
    asset_id: Optional[int] = None
    book_id: Optional[int] = None
    revaluation_date: Optional[date] = None
    old_cost: Optional[float] = None
    new_cost: Optional[float] = None
    old_accumulated_deprn: Optional[float] = None
    new_accumulated_deprn: Optional[float] = None
    old_nbv: Optional[float] = None
    new_nbv: Optional[float] = None
    revaluation_surplus: Optional[float] = None
    revaluation_deficit: Optional[float] = None
    revaluation_reason_code: Optional[str] = None
    appraiser_name: Optional[str] = None
    appraiser_company: Optional[str] = None
    appraisal_date: Optional[date] = None
    appraisal_report_url: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaRevaluationsOut(BaseModel):
    revaluation_id: int
    transaction_id: int
    asset_id: int
    book_id: Optional[int] = None
    revaluation_date: date
    old_cost: Optional[float] = None
    new_cost: Optional[float] = None
    old_accumulated_deprn: Optional[float] = None
    new_accumulated_deprn: Optional[float] = None
    old_nbv: Optional[float] = None
    new_nbv: Optional[float] = None
    revaluation_surplus: Optional[float] = None
    revaluation_deficit: Optional[float] = None
    revaluation_reason_code: Optional[str] = None
    appraiser_name: Optional[str] = None
    appraiser_company: Optional[str] = None
    appraisal_date: Optional[date] = None
    appraisal_report_url: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaScenariosCreate(BaseModel):
    scenario_id: int
    scenario_name: str
    scenario_type_code: str
    description: Optional[str] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    objectives: Optional[dict] = None
    parameters: Optional[dict] = None
    base_scenario_id: Optional[int] = None
    results: Optional[dict] = None
    comparison_notes: Optional[str] = None
    is_approved: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class FaScenariosUpdate(BaseModel):
    scenario_id: Optional[int] = None
    scenario_name: Optional[str] = None
    scenario_type_code: Optional[str] = None
    description: Optional[str] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    objectives: Optional[dict] = None
    parameters: Optional[dict] = None
    base_scenario_id: Optional[int] = None
    results: Optional[dict] = None
    comparison_notes: Optional[str] = None
    is_approved: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class FaScenariosOut(BaseModel):
    scenario_id: int
    scenario_name: str
    scenario_type_code: str
    description: Optional[str] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    objectives: Optional[dict] = None
    parameters: Optional[dict] = None
    base_scenario_id: Optional[int] = None
    results: Optional[dict] = None
    comparison_notes: Optional[str] = None
    is_approved: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaScipyAnalysesCreate(BaseModel):
    analysis_id: int
    analysis_name: str
    analysis_type_code: str
    input_data: Optional[dict] = None
    analysis_parameters: Optional[dict] = None
    results: Optional[dict] = None
    statistical_metrics: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    execution_log: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaScipyAnalysesUpdate(BaseModel):
    analysis_id: Optional[int] = None
    analysis_name: Optional[str] = None
    analysis_type_code: Optional[str] = None
    input_data: Optional[dict] = None
    analysis_parameters: Optional[dict] = None
    results: Optional[dict] = None
    statistical_metrics: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    execution_log: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaScipyAnalysesOut(BaseModel):
    analysis_id: int
    analysis_name: str
    analysis_type_code: str
    input_data: Optional[dict] = None
    analysis_parameters: Optional[dict] = None
    results: Optional[dict] = None
    statistical_metrics: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    execution_log: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaSignaturesCreate(BaseModel):
    signature_id: int
    entity_type_code: str
    entity_id: int
    signature_type_code: str
    signer_name: str
    signer_role: Optional[str] = None
    signature_timestamp: datetime
    signature_data: Optional[str] = None
    storage_path: Optional[str] = None
    gps_location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    device_id: Optional[int] = None
    ip_address: Optional[str] = None
    certificate_ref: Optional[str] = None
    is_verified: Optional[str] = None
    verified_by: Optional[str] = None
    verification_date: Optional[datetime] = None
    is_synced: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaSignaturesUpdate(BaseModel):
    signature_id: Optional[int] = None
    entity_type_code: Optional[str] = None
    entity_id: Optional[int] = None
    signature_type_code: Optional[str] = None
    signer_name: Optional[str] = None
    signer_role: Optional[str] = None
    signature_timestamp: Optional[datetime] = None
    signature_data: Optional[str] = None
    storage_path: Optional[str] = None
    gps_location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    device_id: Optional[int] = None
    ip_address: Optional[str] = None
    certificate_ref: Optional[str] = None
    is_verified: Optional[str] = None
    verified_by: Optional[str] = None
    verification_date: Optional[datetime] = None
    is_synced: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaSignaturesOut(BaseModel):
    signature_id: int
    entity_type_code: str
    entity_id: int
    signature_type_code: str
    signer_name: str
    signer_role: Optional[str] = None
    signature_timestamp: datetime
    signature_data: Optional[str] = None
    storage_path: Optional[str] = None
    gps_location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    device_id: Optional[int] = None
    ip_address: Optional[str] = None
    certificate_ref: Optional[str] = None
    is_verified: Optional[str] = None
    verified_by: Optional[str] = None
    verification_date: Optional[datetime] = None
    is_synced: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaSolverConfigsCreate(BaseModel):
    solver_config_id: int
    solver_name: str
    solver_type_code: str
    solver_version: Optional[str] = None
    solver_parameters: Optional[dict] = None
    supported_algorithms: Optional[dict] = None
    max_solve_time_ms: Optional[int] = None
    enable_parallel: Optional[bool] = None
    max_threads: Optional[int] = None
    enable_warm_start: Optional[bool] = None
    performance_metrics: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaSolverConfigsUpdate(BaseModel):
    solver_config_id: Optional[int] = None
    solver_name: Optional[str] = None
    solver_type_code: Optional[str] = None
    solver_version: Optional[str] = None
    solver_parameters: Optional[dict] = None
    supported_algorithms: Optional[dict] = None
    max_solve_time_ms: Optional[int] = None
    enable_parallel: Optional[bool] = None
    max_threads: Optional[int] = None
    enable_warm_start: Optional[bool] = None
    performance_metrics: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaSolverConfigsOut(BaseModel):
    solver_config_id: int
    solver_name: str
    solver_type_code: str
    solver_version: Optional[str] = None
    solver_parameters: Optional[dict] = None
    supported_algorithms: Optional[dict] = None
    max_solve_time_ms: Optional[int] = None
    enable_parallel: Optional[bool] = None
    max_threads: Optional[int] = None
    enable_warm_start: Optional[bool] = None
    performance_metrics: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaTaxPaymentsCreate(BaseModel):
    tax_payment_id: int
    tax_record_id: int
    payment_amount: float
    payment_date: date
    payment_reference: Optional[str] = None
    payment_method: Optional[str] = None
    paid_by: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    tenant_id: Optional[str] = None

class FaTaxPaymentsUpdate(BaseModel):
    tax_payment_id: Optional[int] = None
    tax_record_id: Optional[int] = None
    payment_amount: Optional[float] = None
    payment_date: Optional[date] = None
    payment_reference: Optional[str] = None
    payment_method: Optional[str] = None
    paid_by: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    tenant_id: Optional[str] = None

class FaTaxPaymentsOut(BaseModel):
    tax_payment_id: int
    tax_record_id: int
    payment_amount: float
    payment_date: date
    payment_reference: Optional[str] = None
    payment_method: Optional[str] = None
    paid_by: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaTaxRecordsCreate(BaseModel):
    tax_record_id: int
    asset_id: int
    tax_type_code: str
    tax_jurisdiction: str
    tax_rate: Optional[float] = None
    assessed_value: Optional[float] = None
    tax_amount: Optional[float] = None
    tax_year: int
    assessment_date: Optional[date] = None
    due_date: Optional[date] = None
    payment_date: Optional[date] = None
    tax_status_code: Optional[str] = None
    exemption_code: Optional[str] = None
    exemption_amount: Optional[float] = None
    filing_reference: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaTaxRecordsUpdate(BaseModel):
    tax_record_id: Optional[int] = None
    asset_id: Optional[int] = None
    tax_type_code: Optional[str] = None
    tax_jurisdiction: Optional[str] = None
    tax_rate: Optional[float] = None
    assessed_value: Optional[float] = None
    tax_amount: Optional[float] = None
    tax_year: Optional[int] = None
    assessment_date: Optional[date] = None
    due_date: Optional[date] = None
    payment_date: Optional[date] = None
    tax_status_code: Optional[str] = None
    exemption_code: Optional[str] = None
    exemption_amount: Optional[float] = None
    filing_reference: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaTaxRecordsOut(BaseModel):
    tax_record_id: int
    asset_id: int
    tax_type_code: str
    tax_jurisdiction: str
    tax_rate: Optional[float] = None
    assessed_value: Optional[float] = None
    tax_amount: Optional[float] = None
    tax_year: int
    assessment_date: Optional[date] = None
    due_date: Optional[date] = None
    payment_date: Optional[date] = None
    tax_status_code: Optional[str] = None
    exemption_code: Optional[str] = None
    exemption_amount: Optional[float] = None
    filing_reference: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaTransactionsCreate(BaseModel):
    transaction_id: int
    asset_id: int
    book_id: Optional[int] = None
    transaction_type_code: str
    transaction_number: str
    transaction_date: date
    period_id: Optional[int] = None
    posting_date: Optional[date] = None
    asset_number: Optional[str] = None
    asset_name: Optional[str] = None
    asset_type_id: Optional[int] = None
    asset_category_id: Optional[int] = None
    location_id: Optional[int] = None
    custodian_id: Optional[int] = None
    from_location_id: Optional[int] = None
    to_location_id: Optional[int] = None
    from_custodian_id: Optional[int] = None
    to_custodian_id: Optional[int] = None
    cost_amount: Optional[float] = None
    deprn_amount: Optional[float] = None
    nbv_amount: Optional[float] = None
    proceeds_amount: Optional[float] = None
    gain_loss_amount: Optional[float] = None
    revaluation_surplus: Optional[float] = None
    impairment_amount: Optional[float] = None
    quantity: Optional[float] = None
    currency_code: Optional[str] = None
    reference_doc_type: Optional[str] = None
    reference_doc_number: Optional[str] = None
    reference_doc_id: Optional[int] = None
    description: Optional[str] = None
    reason_code: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    reversal_transaction_id: Optional[int] = None
    is_reversed: Optional[str] = None
    source_system_code: Optional[str] = None
    source_transaction_id: Optional[str] = None
    transaction_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaTransactionsUpdate(BaseModel):
    transaction_id: Optional[int] = None
    asset_id: Optional[int] = None
    book_id: Optional[int] = None
    transaction_type_code: Optional[str] = None
    transaction_number: Optional[str] = None
    transaction_date: Optional[date] = None
    period_id: Optional[int] = None
    posting_date: Optional[date] = None
    asset_number: Optional[str] = None
    asset_name: Optional[str] = None
    asset_type_id: Optional[int] = None
    asset_category_id: Optional[int] = None
    location_id: Optional[int] = None
    custodian_id: Optional[int] = None
    from_location_id: Optional[int] = None
    to_location_id: Optional[int] = None
    from_custodian_id: Optional[int] = None
    to_custodian_id: Optional[int] = None
    cost_amount: Optional[float] = None
    deprn_amount: Optional[float] = None
    nbv_amount: Optional[float] = None
    proceeds_amount: Optional[float] = None
    gain_loss_amount: Optional[float] = None
    revaluation_surplus: Optional[float] = None
    impairment_amount: Optional[float] = None
    quantity: Optional[float] = None
    currency_code: Optional[str] = None
    reference_doc_type: Optional[str] = None
    reference_doc_number: Optional[str] = None
    reference_doc_id: Optional[int] = None
    description: Optional[str] = None
    reason_code: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    reversal_transaction_id: Optional[int] = None
    is_reversed: Optional[str] = None
    source_system_code: Optional[str] = None
    source_transaction_id: Optional[str] = None
    transaction_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaTransactionsOut(BaseModel):
    transaction_id: int
    asset_id: int
    book_id: Optional[int] = None
    transaction_type_code: str
    transaction_number: str
    transaction_date: date
    period_id: Optional[int] = None
    posting_date: Optional[date] = None
    asset_number: Optional[str] = None
    asset_name: Optional[str] = None
    asset_type_id: Optional[int] = None
    asset_category_id: Optional[int] = None
    location_id: Optional[int] = None
    custodian_id: Optional[int] = None
    from_location_id: Optional[int] = None
    to_location_id: Optional[int] = None
    from_custodian_id: Optional[int] = None
    to_custodian_id: Optional[int] = None
    cost_amount: Optional[float] = None
    deprn_amount: Optional[float] = None
    nbv_amount: Optional[float] = None
    proceeds_amount: Optional[float] = None
    gain_loss_amount: Optional[float] = None
    revaluation_surplus: Optional[float] = None
    impairment_amount: Optional[float] = None
    quantity: Optional[float] = None
    currency_code: Optional[str] = None
    reference_doc_type: Optional[str] = None
    reference_doc_number: Optional[str] = None
    reference_doc_id: Optional[int] = None
    description: Optional[str] = None
    reason_code: Optional[str] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    reversal_transaction_id: Optional[int] = None
    is_reversed: Optional[str] = None
    source_system_code: Optional[str] = None
    source_transaction_id: Optional[str] = None
    transaction_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaTransfersCreate(BaseModel):
    transfer_id: int
    transaction_id: int
    asset_id: int
    transfer_type_code: str
    transfer_date: date
    from_location_id: Optional[int] = None
    to_location_id: Optional[int] = None
    from_custodian_id: Optional[int] = None
    to_custodian_id: Optional[int] = None
    from_organization_id: Optional[int] = None
    to_organization_id: Optional[int] = None
    from_entity_id: Optional[int] = None
    to_entity_id: Optional[int] = None
    transfer_reason: Optional[str] = None
    is_custodian_acknowledged: Optional[str] = None
    custodian_acknowledged_date: Optional[datetime] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaTransfersUpdate(BaseModel):
    transfer_id: Optional[int] = None
    transaction_id: Optional[int] = None
    asset_id: Optional[int] = None
    transfer_type_code: Optional[str] = None
    transfer_date: Optional[date] = None
    from_location_id: Optional[int] = None
    to_location_id: Optional[int] = None
    from_custodian_id: Optional[int] = None
    to_custodian_id: Optional[int] = None
    from_organization_id: Optional[int] = None
    to_organization_id: Optional[int] = None
    from_entity_id: Optional[int] = None
    to_entity_id: Optional[int] = None
    transfer_reason: Optional[str] = None
    is_custodian_acknowledged: Optional[str] = None
    custodian_acknowledged_date: Optional[datetime] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None

class FaTransfersOut(BaseModel):
    transfer_id: int
    transaction_id: int
    asset_id: int
    transfer_type_code: str
    transfer_date: date
    from_location_id: Optional[int] = None
    to_location_id: Optional[int] = None
    from_custodian_id: Optional[int] = None
    to_custodian_id: Optional[int] = None
    from_organization_id: Optional[int] = None
    to_organization_id: Optional[int] = None
    from_entity_id: Optional[int] = None
    to_entity_id: Optional[int] = None
    transfer_reason: Optional[str] = None
    is_custodian_acknowledged: Optional[str] = None
    custodian_acknowledged_date: Optional[datetime] = None
    approval_status: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    entity_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaVectorDocumentsCreate(BaseModel):
    document_id: int
    document_name: str
    document_type_code: str
    content: str
    content_chunks: Optional[dict] = None
    embeddings: Optional[str] = None
    meta_data: Optional[dict] = None
    source_url: Optional[str] = None
    document_version: Optional[str] = None
    chunk_count: Optional[int] = None
    is_indexed: Optional[str] = None
    indexed_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaVectorDocumentsUpdate(BaseModel):
    document_id: Optional[int] = None
    document_name: Optional[str] = None
    document_type_code: Optional[str] = None
    content: Optional[str] = None
    content_chunks: Optional[dict] = None
    embeddings: Optional[str] = None
    meta_data: Optional[dict] = None
    source_url: Optional[str] = None
    document_version: Optional[str] = None
    chunk_count: Optional[int] = None
    is_indexed: Optional[str] = None
    indexed_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaVectorDocumentsOut(BaseModel):
    document_id: int
    document_name: str
    document_type_code: str
    content: str
    content_chunks: Optional[dict] = None
    embeddings: Optional[str] = None
    meta_data: Optional[dict] = None
    source_url: Optional[str] = None
    document_version: Optional[str] = None
    chunk_count: Optional[int] = None
    is_indexed: Optional[str] = None
    indexed_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class FaWarrantiesCreate(BaseModel):
    warranty_id: int
    warranty_number: str
    warranty_type_code: str
    warranty_provider: str
    provider_contact: Optional[str] = None
    start_date: date
    end_date: date
    warranty_term_months: int
    coverage_type_code: Optional[str] = None
    coverage_description: Optional[str] = None
    exclusions: Optional[str] = None
    deductible_amount: Optional[float] = None
    coverage_limit: Optional[float] = None
    is_transferable: Optional[str] = None
    warranty_doc_url: Optional[str] = None
    warranty_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class FaWarrantiesUpdate(BaseModel):
    warranty_id: Optional[int] = None
    warranty_number: Optional[str] = None
    warranty_type_code: Optional[str] = None
    warranty_provider: Optional[str] = None
    provider_contact: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    warranty_term_months: Optional[int] = None
    coverage_type_code: Optional[str] = None
    coverage_description: Optional[str] = None
    exclusions: Optional[str] = None
    deductible_amount: Optional[float] = None
    coverage_limit: Optional[float] = None
    is_transferable: Optional[str] = None
    warranty_doc_url: Optional[str] = None
    warranty_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class FaWarrantiesOut(BaseModel):
    warranty_id: int
    warranty_number: str
    warranty_type_code: str
    warranty_provider: str
    provider_contact: Optional[str] = None
    start_date: date
    end_date: date
    warranty_term_months: int
    coverage_type_code: Optional[str] = None
    coverage_description: Optional[str] = None
    exclusions: Optional[str] = None
    deductible_amount: Optional[float] = None
    coverage_limit: Optional[float] = None
    is_transferable: Optional[str] = None
    warranty_doc_url: Optional[str] = None
    warranty_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class FaWarrantyClaimsCreate(BaseModel):
    claim_id: int
    warranty_id: int
    asset_id: int
    claim_number: str
    claim_date: date
    claim_type_code: str
    claim_amount: Optional[float] = None
    approved_amount: Optional[float] = None
    claim_status_code: Optional[str] = None
    issue_description: Optional[str] = None
    resolution_description: Optional[str] = None
    resolution_date: Optional[date] = None
    service_provider: Optional[str] = None
    claim_doc_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class FaWarrantyClaimsUpdate(BaseModel):
    claim_id: Optional[int] = None
    warranty_id: Optional[int] = None
    asset_id: Optional[int] = None
    claim_number: Optional[str] = None
    claim_date: Optional[date] = None
    claim_type_code: Optional[str] = None
    claim_amount: Optional[float] = None
    approved_amount: Optional[float] = None
    claim_status_code: Optional[str] = None
    issue_description: Optional[str] = None
    resolution_description: Optional[str] = None
    resolution_date: Optional[date] = None
    service_provider: Optional[str] = None
    claim_doc_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class FaWarrantyClaimsOut(BaseModel):
    claim_id: int
    warranty_id: int
    asset_id: int
    claim_number: str
    claim_date: date
    claim_type_code: str
    claim_amount: Optional[float] = None
    approved_amount: Optional[float] = None
    claim_status_code: Optional[str] = None
    issue_description: Optional[str] = None
    resolution_description: Optional[str] = None
    resolution_date: Optional[date] = None
    service_provider: Optional[str] = None
    claim_doc_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}
