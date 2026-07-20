import uuid
from datetime import date, datetime, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class EamAiAgentLogsCreate(BaseModel):
    log_id: int
    thread_id: Optional[str] = None
    state_id: Optional[int] = None
    agent_name: Optional[str] = None
    agent_type: Optional[str] = None
    action: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    reasoning: Optional[str] = None
    llm_calls: Optional[int] = None
    tool_calls: Optional[int] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    tenant_id: Optional[str] = None

class EamAiAgentLogsUpdate(BaseModel):
    log_id: Optional[int] = None
    thread_id: Optional[str] = None
    state_id: Optional[int] = None
    agent_name: Optional[str] = None
    agent_type: Optional[str] = None
    action: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    reasoning: Optional[str] = None
    llm_calls: Optional[int] = None
    tool_calls: Optional[int] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    tenant_id: Optional[str] = None

class EamAiAgentLogsOut(BaseModel):
    log_id: int
    thread_id: Optional[str] = None
    state_id: Optional[int] = None
    agent_name: Optional[str] = None
    agent_type: Optional[str] = None
    action: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    reasoning: Optional[str] = None
    llm_calls: Optional[int] = None
    tool_calls: Optional[int] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    created_at: Optional[datetime] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamAiDecisionsCreate(BaseModel):
    decision_id: int
    thread_id: Optional[str] = None
    doc_id: Optional[str] = None
    decision_type: str
    decision_data: dict
    reasoning: Optional[str] = None
    confidence_score: Optional[float] = None
    accepted: Optional[bool] = None
    accepted_by: Optional[str] = None
    accepted_date: Optional[datetime] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamAiDecisionsUpdate(BaseModel):
    decision_id: Optional[int] = None
    thread_id: Optional[str] = None
    doc_id: Optional[str] = None
    decision_type: Optional[str] = None
    decision_data: Optional[dict] = None
    reasoning: Optional[str] = None
    confidence_score: Optional[float] = None
    accepted: Optional[bool] = None
    accepted_by: Optional[str] = None
    accepted_date: Optional[datetime] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamAiDecisionsOut(BaseModel):
    decision_id: int
    thread_id: Optional[str] = None
    doc_id: Optional[str] = None
    decision_type: str
    decision_data: dict
    reasoning: Optional[str] = None
    confidence_score: Optional[float] = None
    accepted: Optional[bool] = None
    accepted_by: Optional[str] = None
    accepted_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamAiWorkflowStateCreate(BaseModel):
    state_id: int
    thread_id: str
    workflow_id: Optional[int] = None
    workflow_name: Optional[str] = None
    doc_type: Optional[str] = None
    doc_id: Optional[str] = None
    status: Optional[str] = None
    checkpoint: Optional[dict] = None
    context: Optional[dict] = None
    results: Optional[dict] = None
    errors: Optional[dict] = None
    parent_state_id: Optional[int] = None
    completed_at: Optional[datetime] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamAiWorkflowStateUpdate(BaseModel):
    state_id: Optional[int] = None
    thread_id: Optional[str] = None
    workflow_id: Optional[int] = None
    workflow_name: Optional[str] = None
    doc_type: Optional[str] = None
    doc_id: Optional[str] = None
    status: Optional[str] = None
    checkpoint: Optional[dict] = None
    context: Optional[dict] = None
    results: Optional[dict] = None
    errors: Optional[dict] = None
    parent_state_id: Optional[int] = None
    completed_at: Optional[datetime] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamAiWorkflowStateOut(BaseModel):
    state_id: int
    thread_id: str
    workflow_id: Optional[int] = None
    workflow_name: Optional[str] = None
    doc_type: Optional[str] = None
    doc_id: Optional[str] = None
    status: Optional[str] = None
    checkpoint: Optional[dict] = None
    context: Optional[dict] = None
    results: Optional[dict] = None
    errors: Optional[dict] = None
    parent_state_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamAlertsCreate(BaseModel):
    alert_id: int
    alert_number: str
    alert_type_code: str
    alert_source_type: Optional[str] = None
    alert_source_id: Optional[int] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    severity_code: str
    title: str
    message: Optional[str] = None
    action_required: Optional[str] = None
    assigned_to: Optional[str] = None
    alert_status_code: Optional[str] = None
    acknowledged_by: Optional[str] = None
    acknowledged_date: Optional[datetime] = None
    resolved_by: Optional[str] = None
    resolved_date: Optional[datetime] = None
    resolution_notes: Optional[str] = None
    escalation_level: Optional[int] = None
    escalation_time: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamAlertsUpdate(BaseModel):
    alert_id: Optional[int] = None
    alert_number: Optional[str] = None
    alert_type_code: Optional[str] = None
    alert_source_type: Optional[str] = None
    alert_source_id: Optional[int] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    severity_code: Optional[str] = None
    title: Optional[str] = None
    message: Optional[str] = None
    action_required: Optional[str] = None
    assigned_to: Optional[str] = None
    alert_status_code: Optional[str] = None
    acknowledged_by: Optional[str] = None
    acknowledged_date: Optional[datetime] = None
    resolved_by: Optional[str] = None
    resolved_date: Optional[datetime] = None
    resolution_notes: Optional[str] = None
    escalation_level: Optional[int] = None
    escalation_time: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamAlertsOut(BaseModel):
    alert_id: int
    alert_number: str
    alert_type_code: str
    alert_source_type: Optional[str] = None
    alert_source_id: Optional[int] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    severity_code: str
    title: str
    message: Optional[str] = None
    action_required: Optional[str] = None
    assigned_to: Optional[str] = None
    alert_status_code: Optional[str] = None
    acknowledged_by: Optional[str] = None
    acknowledged_date: Optional[datetime] = None
    resolved_by: Optional[str] = None
    resolved_date: Optional[datetime] = None
    resolution_notes: Optional[str] = None
    escalation_level: Optional[int] = None
    escalation_time: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class EamAssetAttachmentsCreate(BaseModel):
    attachment_id: int
    asset_id: int
    attachment_type_code: str
    attachment_name: str
    description: Optional[str] = None
    file_url: Optional[str] = None
    file_type: Optional[str] = None
    file_size_bytes: Optional[int] = None
    attachment_date: Optional[date] = None
    revision_number: Optional[str] = None
    is_primary: Optional[bool] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamAssetAttachmentsUpdate(BaseModel):
    attachment_id: Optional[int] = None
    asset_id: Optional[int] = None
    attachment_type_code: Optional[str] = None
    attachment_name: Optional[str] = None
    description: Optional[str] = None
    file_url: Optional[str] = None
    file_type: Optional[str] = None
    file_size_bytes: Optional[int] = None
    attachment_date: Optional[date] = None
    revision_number: Optional[str] = None
    is_primary: Optional[bool] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamAssetAttachmentsOut(BaseModel):
    attachment_id: int
    asset_id: int
    attachment_type_code: str
    attachment_name: str
    description: Optional[str] = None
    file_url: Optional[str] = None
    file_type: Optional[str] = None
    file_size_bytes: Optional[int] = None
    attachment_date: Optional[date] = None
    revision_number: Optional[str] = None
    is_primary: Optional[bool] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamAssetBomCreate(BaseModel):
    asset_bom_id: int
    asset_id: int
    component_id: Optional[int] = None
    item_id: int
    item_code: str
    item_name: str
    description: Optional[str] = None
    quantity_per_asset: float
    unit_of_measure: Optional[str] = None
    usage_type_code: Optional[str] = None
    interchangeability_code: Optional[str] = None
    superseded_by_item_id: Optional[int] = None
    vendor_item_code: Optional[str] = None
    manufacturer_item_code: Optional[str] = None
    manufacturer_id: Optional[int] = None
    unit_cost: Optional[float] = None
    lead_time_days: Optional[int] = None
    min_stock_level: Optional[float] = None
    max_stock_level: Optional[float] = None
    reorder_point: Optional[float] = None
    safety_stock: Optional[float] = None
    storage_location_id: Optional[int] = None
    shelf_life_days: Optional[int] = None
    requires_certification: Optional[bool] = None
    hazardous_material: Optional[bool] = None
    critical_spare: Optional[bool] = None
    long_lead_item: Optional[bool] = None
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
    site_id: Optional[int] = None

class EamAssetBomUpdate(BaseModel):
    asset_bom_id: Optional[int] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    item_id: Optional[int] = None
    item_code: Optional[str] = None
    item_name: Optional[str] = None
    description: Optional[str] = None
    quantity_per_asset: Optional[float] = None
    unit_of_measure: Optional[str] = None
    usage_type_code: Optional[str] = None
    interchangeability_code: Optional[str] = None
    superseded_by_item_id: Optional[int] = None
    vendor_item_code: Optional[str] = None
    manufacturer_item_code: Optional[str] = None
    manufacturer_id: Optional[int] = None
    unit_cost: Optional[float] = None
    lead_time_days: Optional[int] = None
    min_stock_level: Optional[float] = None
    max_stock_level: Optional[float] = None
    reorder_point: Optional[float] = None
    safety_stock: Optional[float] = None
    storage_location_id: Optional[int] = None
    shelf_life_days: Optional[int] = None
    requires_certification: Optional[bool] = None
    hazardous_material: Optional[bool] = None
    critical_spare: Optional[bool] = None
    long_lead_item: Optional[bool] = None
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
    site_id: Optional[int] = None

class EamAssetBomOut(BaseModel):
    asset_bom_id: int
    asset_id: int
    component_id: Optional[int] = None
    item_id: int
    item_code: str
    item_name: str
    description: Optional[str] = None
    quantity_per_asset: float
    unit_of_measure: Optional[str] = None
    usage_type_code: Optional[str] = None
    interchangeability_code: Optional[str] = None
    superseded_by_item_id: Optional[int] = None
    vendor_item_code: Optional[str] = None
    manufacturer_item_code: Optional[str] = None
    manufacturer_id: Optional[int] = None
    unit_cost: Optional[float] = None
    lead_time_days: Optional[int] = None
    min_stock_level: Optional[float] = None
    max_stock_level: Optional[float] = None
    reorder_point: Optional[float] = None
    safety_stock: Optional[float] = None
    storage_location_id: Optional[int] = None
    shelf_life_days: Optional[int] = None
    requires_certification: Optional[bool] = None
    hazardous_material: Optional[bool] = None
    critical_spare: Optional[bool] = None
    long_lead_item: Optional[bool] = None
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
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamAssetCategoriesCreate(BaseModel):
    category_id: int
    category_code: str
    category_name: str
    description: Optional[str] = None
    parent_category_id: Optional[int] = None
    category_level: Optional[int] = None
    asset_type_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamAssetCategoriesUpdate(BaseModel):
    category_id: Optional[int] = None
    category_code: Optional[str] = None
    category_name: Optional[str] = None
    description: Optional[str] = None
    parent_category_id: Optional[int] = None
    category_level: Optional[int] = None
    asset_type_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamAssetCategoriesOut(BaseModel):
    category_id: int
    category_code: str
    category_name: str
    description: Optional[str] = None
    parent_category_id: Optional[int] = None
    category_level: Optional[int] = None
    asset_type_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamAssetCriticalityCreate(BaseModel):
    criticality_code: str
    criticality_name: str
    description: Optional[str] = None
    impact_level: int
    default_color_code: Optional[str] = None
    safety_impact: Optional[bool] = None
    environmental_impact: Optional[bool] = None
    operational_impact: Optional[bool] = None
    financial_impact: Optional[bool] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: bool = True

class EamAssetCriticalityUpdate(BaseModel):
    criticality_code: Optional[str] = None
    criticality_name: Optional[str] = None
    description: Optional[str] = None
    impact_level: Optional[int] = None
    default_color_code: Optional[str] = None
    safety_impact: Optional[bool] = None
    environmental_impact: Optional[bool] = None
    operational_impact: Optional[bool] = None
    financial_impact: Optional[bool] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: Optional[bool] = None

class EamAssetCriticalityOut(BaseModel):
    criticality_code: str
    criticality_name: str
    description: Optional[str] = None
    impact_level: int
    default_color_code: Optional[str] = None
    safety_impact: Optional[bool] = None
    environmental_impact: Optional[bool] = None
    operational_impact: Optional[bool] = None
    financial_impact: Optional[bool] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: bool
    model_config = {"from_attributes": True}

class EamAssetHierarchyCreate(BaseModel):
    hierarchy_id: int
    parent_asset_id: int
    child_asset_id: int
    relationship_type_code: str
    position_description: Optional[str] = None
    quantity: Optional[float] = None
    sort_order: Optional[int] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    is_critical_component: Optional[bool] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamAssetHierarchyUpdate(BaseModel):
    hierarchy_id: Optional[int] = None
    parent_asset_id: Optional[int] = None
    child_asset_id: Optional[int] = None
    relationship_type_code: Optional[str] = None
    position_description: Optional[str] = None
    quantity: Optional[float] = None
    sort_order: Optional[int] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    is_critical_component: Optional[bool] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamAssetHierarchyOut(BaseModel):
    hierarchy_id: int
    parent_asset_id: int
    child_asset_id: int
    relationship_type_code: str
    position_description: Optional[str] = None
    quantity: Optional[float] = None
    sort_order: Optional[int] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    is_critical_component: Optional[bool] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamAssetTypesCreate(BaseModel):
    asset_type_id: int
    asset_type_code: str
    asset_type_name: str
    description: Optional[str] = None
    parent_asset_type_id: Optional[int] = None
    asset_class_code: str
    default_criticality_code: Optional[str] = None
    default_condition_code: Optional[str] = None
    depreciation_method: Optional[str] = None
    depreciation_life_months: Optional[int] = None
    insurance_required: Optional[bool] = None
    regulatory_category: Optional[str] = None
    has_serial_number: Optional[bool] = None
    has_warranty: Optional[bool] = None
    condition_based_maintenance: Optional[bool] = None
    default_maintenance_strategy: Optional[str] = None
    custom_attributes_schema: Optional[dict] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamAssetTypesUpdate(BaseModel):
    asset_type_id: Optional[int] = None
    asset_type_code: Optional[str] = None
    asset_type_name: Optional[str] = None
    description: Optional[str] = None
    parent_asset_type_id: Optional[int] = None
    asset_class_code: Optional[str] = None
    default_criticality_code: Optional[str] = None
    default_condition_code: Optional[str] = None
    depreciation_method: Optional[str] = None
    depreciation_life_months: Optional[int] = None
    insurance_required: Optional[bool] = None
    regulatory_category: Optional[str] = None
    has_serial_number: Optional[bool] = None
    has_warranty: Optional[bool] = None
    condition_based_maintenance: Optional[bool] = None
    default_maintenance_strategy: Optional[str] = None
    custom_attributes_schema: Optional[dict] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamAssetTypesOut(BaseModel):
    asset_type_id: int
    asset_type_code: str
    asset_type_name: str
    description: Optional[str] = None
    parent_asset_type_id: Optional[int] = None
    asset_class_code: str
    default_criticality_code: Optional[str] = None
    default_condition_code: Optional[str] = None
    depreciation_method: Optional[str] = None
    depreciation_life_months: Optional[int] = None
    insurance_required: Optional[bool] = None
    regulatory_category: Optional[str] = None
    has_serial_number: Optional[bool] = None
    has_warranty: Optional[bool] = None
    condition_based_maintenance: Optional[bool] = None
    default_maintenance_strategy: Optional[str] = None
    custom_attributes_schema: Optional[dict] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamAssetVendorsCreate(BaseModel):
    vendor_id: int
    vendor_code: str
    vendor_name: str
    vendor_type_code: str
    contact_person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    service_capabilities: Optional[str] = None
    service_area: Optional[str] = None
    certifications: Optional[dict] = None
    performance_rating: Optional[float] = None
    contract_id: Optional[int] = None
    preferred_vendor: Optional[bool] = None
    vendor_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamAssetVendorsUpdate(BaseModel):
    vendor_id: Optional[int] = None
    vendor_code: Optional[str] = None
    vendor_name: Optional[str] = None
    vendor_type_code: Optional[str] = None
    contact_person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    service_capabilities: Optional[str] = None
    service_area: Optional[str] = None
    certifications: Optional[dict] = None
    performance_rating: Optional[float] = None
    contract_id: Optional[int] = None
    preferred_vendor: Optional[bool] = None
    vendor_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamAssetVendorsOut(BaseModel):
    vendor_id: int
    vendor_code: str
    vendor_name: str
    vendor_type_code: str
    contact_person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    service_capabilities: Optional[str] = None
    service_area: Optional[str] = None
    certifications: Optional[dict] = None
    performance_rating: Optional[float] = None
    contract_id: Optional[int] = None
    preferred_vendor: Optional[bool] = None
    vendor_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamAssetsCreate(BaseModel):
    asset_id: int
    asset_number: str
    asset_name: str
    description: Optional[str] = None
    asset_type_id: int
    asset_class_code: str
    category_id: Optional[int] = None
    criticality_code: Optional[str] = None
    manufacturer_id: Optional[int] = None
    manufacturer_name: Optional[str] = None
    model_number: Optional[str] = None
    serial_number: Optional[str] = None
    manufacture_date: Optional[date] = None
    commission_date: Optional[date] = None
    in_service_date: Optional[date] = None
    warranty_end_date: Optional[date] = None
    warranty_terms: Optional[str] = None
    functional_location_id: Optional[int] = None
    physical_location_id: Optional[int] = None
    asset_status_code: str
    condition_code: Optional[str] = None
    acquisition_cost: Optional[float] = None
    replacement_value: Optional[float] = None
    book_value: Optional[float] = None
    salvage_value: Optional[float] = None
    currency_code: Optional[str] = None
    ownership_code: Optional[str] = None
    lease_start_date: Optional[date] = None
    lease_end_date: Optional[date] = None
    depreciation_method: Optional[str] = None
    depreciation_start_date: Optional[date] = None
    useful_life_months: Optional[int] = None
    insurance_policy_number: Optional[str] = None
    insurance_coverage: Optional[float] = None
    insurance_expiry_date: Optional[date] = None
    barcode: Optional[str] = None
    rfid_tag: Optional[str] = None
    qr_code: Optional[str] = None
    asset_image_url: Optional[str] = None
    source_system_code: Optional[str] = None
    source_asset_id: Optional[str] = None
    source_transaction_id: Optional[str] = None
    custom_attributes: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamAssetsUpdate(BaseModel):
    asset_id: Optional[int] = None
    asset_number: Optional[str] = None
    asset_name: Optional[str] = None
    description: Optional[str] = None
    asset_type_id: Optional[int] = None
    asset_class_code: Optional[str] = None
    category_id: Optional[int] = None
    criticality_code: Optional[str] = None
    manufacturer_id: Optional[int] = None
    manufacturer_name: Optional[str] = None
    model_number: Optional[str] = None
    serial_number: Optional[str] = None
    manufacture_date: Optional[date] = None
    commission_date: Optional[date] = None
    in_service_date: Optional[date] = None
    warranty_end_date: Optional[date] = None
    warranty_terms: Optional[str] = None
    functional_location_id: Optional[int] = None
    physical_location_id: Optional[int] = None
    asset_status_code: Optional[str] = None
    condition_code: Optional[str] = None
    acquisition_cost: Optional[float] = None
    replacement_value: Optional[float] = None
    book_value: Optional[float] = None
    salvage_value: Optional[float] = None
    currency_code: Optional[str] = None
    ownership_code: Optional[str] = None
    lease_start_date: Optional[date] = None
    lease_end_date: Optional[date] = None
    depreciation_method: Optional[str] = None
    depreciation_start_date: Optional[date] = None
    useful_life_months: Optional[int] = None
    insurance_policy_number: Optional[str] = None
    insurance_coverage: Optional[float] = None
    insurance_expiry_date: Optional[date] = None
    barcode: Optional[str] = None
    rfid_tag: Optional[str] = None
    qr_code: Optional[str] = None
    asset_image_url: Optional[str] = None
    source_system_code: Optional[str] = None
    source_asset_id: Optional[str] = None
    source_transaction_id: Optional[str] = None
    custom_attributes: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamAssetsOut(BaseModel):
    asset_id: int
    asset_number: str
    asset_name: str
    description: Optional[str] = None
    asset_type_id: int
    asset_class_code: str
    category_id: Optional[int] = None
    criticality_code: Optional[str] = None
    manufacturer_id: Optional[int] = None
    manufacturer_name: Optional[str] = None
    model_number: Optional[str] = None
    serial_number: Optional[str] = None
    manufacture_date: Optional[date] = None
    commission_date: Optional[date] = None
    in_service_date: Optional[date] = None
    warranty_end_date: Optional[date] = None
    warranty_terms: Optional[str] = None
    functional_location_id: Optional[int] = None
    physical_location_id: Optional[int] = None
    asset_status_code: str
    condition_code: Optional[str] = None
    acquisition_cost: Optional[float] = None
    replacement_value: Optional[float] = None
    book_value: Optional[float] = None
    salvage_value: Optional[float] = None
    currency_code: Optional[str] = None
    ownership_code: Optional[str] = None
    lease_start_date: Optional[date] = None
    lease_end_date: Optional[date] = None
    depreciation_method: Optional[str] = None
    depreciation_start_date: Optional[date] = None
    useful_life_months: Optional[int] = None
    insurance_policy_number: Optional[str] = None
    insurance_coverage: Optional[float] = None
    insurance_expiry_date: Optional[date] = None
    barcode: Optional[str] = None
    rfid_tag: Optional[str] = None
    qr_code: Optional[str] = None
    asset_image_url: Optional[str] = None
    source_system_code: Optional[str] = None
    source_asset_id: Optional[str] = None
    source_transaction_id: Optional[str] = None
    custom_attributes: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamAuditLogCreate(BaseModel):
    audit_id: int
    table_name: str
    record_id: int
    action_type: str
    old_values: Optional[dict] = None
    new_values: Optional[dict] = None
    changed_by: Optional[str] = None
    change_date: Optional[datetime] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamAuditLogUpdate(BaseModel):
    audit_id: Optional[int] = None
    table_name: Optional[str] = None
    record_id: Optional[int] = None
    action_type: Optional[str] = None
    old_values: Optional[dict] = None
    new_values: Optional[dict] = None
    changed_by: Optional[str] = None
    change_date: Optional[datetime] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamAuditLogOut(BaseModel):
    audit_id: int
    table_name: str
    record_id: int
    action_type: str
    old_values: Optional[dict] = None
    new_values: Optional[dict] = None
    changed_by: Optional[str] = None
    change_date: Optional[datetime] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamBudgetsCreate(BaseModel):
    budget_id: int
    budget_year: int
    budget_code: str
    budget_name: str
    description: Optional[str] = None
    budget_category_code: str
    asset_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    planned_amount: float
    actual_amount: Optional[float] = None
    committed_amount: Optional[float] = None
    variance_amount: Optional[float] = None
    currency_code: Optional[str] = None
    budget_status_code: Optional[str] = None
    fiscal_period: Optional[str] = None
    approval_required: Optional[bool] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamBudgetsUpdate(BaseModel):
    budget_id: Optional[int] = None
    budget_year: Optional[int] = None
    budget_code: Optional[str] = None
    budget_name: Optional[str] = None
    description: Optional[str] = None
    budget_category_code: Optional[str] = None
    asset_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    planned_amount: Optional[float] = None
    actual_amount: Optional[float] = None
    committed_amount: Optional[float] = None
    variance_amount: Optional[float] = None
    currency_code: Optional[str] = None
    budget_status_code: Optional[str] = None
    fiscal_period: Optional[str] = None
    approval_required: Optional[bool] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamBudgetsOut(BaseModel):
    budget_id: int
    budget_year: int
    budget_code: str
    budget_name: str
    description: Optional[str] = None
    budget_category_code: str
    asset_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    planned_amount: float
    actual_amount: Optional[float] = None
    committed_amount: Optional[float] = None
    variance_amount: Optional[float] = None
    currency_code: Optional[str] = None
    budget_status_code: Optional[str] = None
    fiscal_period: Optional[str] = None
    approval_required: Optional[bool] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class EamCalibrationRequirementsCreate(BaseModel):
    cal_req_id: int
    asset_id: Optional[int] = None
    tool_id: Optional[int] = None
    calibration_code: str
    calibration_name: str
    description: Optional[str] = None
    calibration_type_code: str
    frequency_days: int
    tolerance_range: Optional[str] = None
    accuracy_requirement: Optional[str] = None
    standard_reference: Optional[str] = None
    calibration_procedure: Optional[str] = None
    requires_certificate: Optional[bool] = None
    requires_traceability: Optional[bool] = None
    assigned_to_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamCalibrationRequirementsUpdate(BaseModel):
    cal_req_id: Optional[int] = None
    asset_id: Optional[int] = None
    tool_id: Optional[int] = None
    calibration_code: Optional[str] = None
    calibration_name: Optional[str] = None
    description: Optional[str] = None
    calibration_type_code: Optional[str] = None
    frequency_days: Optional[int] = None
    tolerance_range: Optional[str] = None
    accuracy_requirement: Optional[str] = None
    standard_reference: Optional[str] = None
    calibration_procedure: Optional[str] = None
    requires_certificate: Optional[bool] = None
    requires_traceability: Optional[bool] = None
    assigned_to_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamCalibrationRequirementsOut(BaseModel):
    cal_req_id: int
    asset_id: Optional[int] = None
    tool_id: Optional[int] = None
    calibration_code: str
    calibration_name: str
    description: Optional[str] = None
    calibration_type_code: str
    frequency_days: int
    tolerance_range: Optional[str] = None
    accuracy_requirement: Optional[str] = None
    standard_reference: Optional[str] = None
    calibration_procedure: Optional[str] = None
    requires_certificate: Optional[bool] = None
    requires_traceability: Optional[bool] = None
    assigned_to_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamCalibrationResultsCreate(BaseModel):
    cal_result_id: int
    cal_req_id: int
    work_order_id: Optional[int] = None
    asset_id: Optional[int] = None
    tool_id: Optional[int] = None
    calibration_date: date
    calibrated_by: Optional[str] = None
    calibration_lab: Optional[str] = None
    certificate_number: Optional[str] = None
    certificate_url: Optional[str] = None
    as_found_value: Optional[float] = None
    as_left_value: Optional[float] = None
    result_code: str
    result_notes: Optional[str] = None
    adjustment_made: Optional[str] = None
    next_due_date: Optional[date] = None
    traceability_info: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamCalibrationResultsUpdate(BaseModel):
    cal_result_id: Optional[int] = None
    cal_req_id: Optional[int] = None
    work_order_id: Optional[int] = None
    asset_id: Optional[int] = None
    tool_id: Optional[int] = None
    calibration_date: Optional[date] = None
    calibrated_by: Optional[str] = None
    calibration_lab: Optional[str] = None
    certificate_number: Optional[str] = None
    certificate_url: Optional[str] = None
    as_found_value: Optional[float] = None
    as_left_value: Optional[float] = None
    result_code: Optional[str] = None
    result_notes: Optional[str] = None
    adjustment_made: Optional[str] = None
    next_due_date: Optional[date] = None
    traceability_info: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamCalibrationResultsOut(BaseModel):
    cal_result_id: int
    cal_req_id: int
    work_order_id: Optional[int] = None
    asset_id: Optional[int] = None
    tool_id: Optional[int] = None
    calibration_date: date
    calibrated_by: Optional[str] = None
    calibration_lab: Optional[str] = None
    certificate_number: Optional[str] = None
    certificate_url: Optional[str] = None
    as_found_value: Optional[float] = None
    as_left_value: Optional[float] = None
    result_code: str
    result_notes: Optional[str] = None
    adjustment_made: Optional[str] = None
    next_due_date: Optional[date] = None
    traceability_info: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class EamComplianceRecordsCreate(BaseModel):
    compliance_record_id: int
    compliance_req_id: int
    asset_id: Optional[int] = None
    work_order_id: Optional[int] = None
    inspection_id: Optional[int] = None
    due_date: Optional[date] = None
    completed_date: Optional[date] = None
    result_code: Optional[str] = None
    result_notes: Optional[str] = None
    corrective_action: Optional[str] = None
    verified_by: Optional[str] = None
    verified_date: Optional[date] = None
    attachment_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamComplianceRecordsUpdate(BaseModel):
    compliance_record_id: Optional[int] = None
    compliance_req_id: Optional[int] = None
    asset_id: Optional[int] = None
    work_order_id: Optional[int] = None
    inspection_id: Optional[int] = None
    due_date: Optional[date] = None
    completed_date: Optional[date] = None
    result_code: Optional[str] = None
    result_notes: Optional[str] = None
    corrective_action: Optional[str] = None
    verified_by: Optional[str] = None
    verified_date: Optional[date] = None
    attachment_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamComplianceRecordsOut(BaseModel):
    compliance_record_id: int
    compliance_req_id: int
    asset_id: Optional[int] = None
    work_order_id: Optional[int] = None
    inspection_id: Optional[int] = None
    due_date: Optional[date] = None
    completed_date: Optional[date] = None
    result_code: Optional[str] = None
    result_notes: Optional[str] = None
    corrective_action: Optional[str] = None
    verified_by: Optional[str] = None
    verified_date: Optional[date] = None
    attachment_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class EamComplianceRequirementsCreate(BaseModel):
    compliance_req_id: int
    requirement_code: str
    requirement_name: str
    description: Optional[str] = None
    regulatory_body: str
    regulation_reference: Optional[str] = None
    asset_type_id: Optional[int] = None
    applicability: Optional[str] = None
    frequency_days: Optional[int] = None
    requires_inspection: Optional[bool] = None
    requires_certification: Optional[bool] = None
    requires_training: Optional[bool] = None
    penalty_for_non_compliance: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class EamComplianceRequirementsUpdate(BaseModel):
    compliance_req_id: Optional[int] = None
    requirement_code: Optional[str] = None
    requirement_name: Optional[str] = None
    description: Optional[str] = None
    regulatory_body: Optional[str] = None
    regulation_reference: Optional[str] = None
    asset_type_id: Optional[int] = None
    applicability: Optional[str] = None
    frequency_days: Optional[int] = None
    requires_inspection: Optional[bool] = None
    requires_certification: Optional[bool] = None
    requires_training: Optional[bool] = None
    penalty_for_non_compliance: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class EamComplianceRequirementsOut(BaseModel):
    compliance_req_id: int
    requirement_code: str
    requirement_name: str
    description: Optional[str] = None
    regulatory_body: str
    regulation_reference: Optional[str] = None
    asset_type_id: Optional[int] = None
    applicability: Optional[str] = None
    frequency_days: Optional[int] = None
    requires_inspection: Optional[bool] = None
    requires_certification: Optional[bool] = None
    requires_training: Optional[bool] = None
    penalty_for_non_compliance: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamComponentsCreate(BaseModel):
    component_id: int
    component_code: str
    component_name: str
    description: Optional[str] = None
    component_type_code: str
    asset_id: int
    parent_component_id: Optional[int] = None
    manufacturer_id: Optional[int] = None
    manufacturer_part_no: Optional[str] = None
    serial_number: Optional[str] = None
    model_number: Optional[str] = None
    criticality_code: Optional[str] = None
    position_description: Optional[str] = None
    quantity_per_asset: Optional[float] = None
    unit_of_measure: Optional[str] = None
    expected_life_months: Optional[int] = None
    replacement_cost: Optional[float] = None
    warranty_end_date: Optional[date] = None
    remaining_useful_life: Optional[float] = None
    rul_prediction_date: Optional[datetime] = None
    condition_code: Optional[str] = None
    last_replacement_date: Optional[date] = None
    last_inspection_date: Optional[date] = None
    installation_date: Optional[date] = None
    component_status_code: Optional[str] = None
    custom_attributes: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamComponentsUpdate(BaseModel):
    component_id: Optional[int] = None
    component_code: Optional[str] = None
    component_name: Optional[str] = None
    description: Optional[str] = None
    component_type_code: Optional[str] = None
    asset_id: Optional[int] = None
    parent_component_id: Optional[int] = None
    manufacturer_id: Optional[int] = None
    manufacturer_part_no: Optional[str] = None
    serial_number: Optional[str] = None
    model_number: Optional[str] = None
    criticality_code: Optional[str] = None
    position_description: Optional[str] = None
    quantity_per_asset: Optional[float] = None
    unit_of_measure: Optional[str] = None
    expected_life_months: Optional[int] = None
    replacement_cost: Optional[float] = None
    warranty_end_date: Optional[date] = None
    remaining_useful_life: Optional[float] = None
    rul_prediction_date: Optional[datetime] = None
    condition_code: Optional[str] = None
    last_replacement_date: Optional[date] = None
    last_inspection_date: Optional[date] = None
    installation_date: Optional[date] = None
    component_status_code: Optional[str] = None
    custom_attributes: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamComponentsOut(BaseModel):
    component_id: int
    component_code: str
    component_name: str
    description: Optional[str] = None
    component_type_code: str
    asset_id: int
    parent_component_id: Optional[int] = None
    manufacturer_id: Optional[int] = None
    manufacturer_part_no: Optional[str] = None
    serial_number: Optional[str] = None
    model_number: Optional[str] = None
    criticality_code: Optional[str] = None
    position_description: Optional[str] = None
    quantity_per_asset: Optional[float] = None
    unit_of_measure: Optional[str] = None
    expected_life_months: Optional[int] = None
    replacement_cost: Optional[float] = None
    warranty_end_date: Optional[date] = None
    remaining_useful_life: Optional[float] = None
    rul_prediction_date: Optional[datetime] = None
    condition_code: Optional[str] = None
    last_replacement_date: Optional[date] = None
    last_inspection_date: Optional[date] = None
    installation_date: Optional[date] = None
    component_status_code: Optional[str] = None
    custom_attributes: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamConditionMonitoringProgramsCreate(BaseModel):
    cm_program_id: int
    program_code: str
    program_name: str
    description: Optional[str] = None
    technology_code: str
    asset_id: int
    component_id: Optional[int] = None
    frequency_days: Optional[int] = None
    route_name: Optional[str] = None
    baseline_data: Optional[dict] = None
    thresholds: Optional[dict] = None
    program_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamConditionMonitoringProgramsUpdate(BaseModel):
    cm_program_id: Optional[int] = None
    program_code: Optional[str] = None
    program_name: Optional[str] = None
    description: Optional[str] = None
    technology_code: Optional[str] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    frequency_days: Optional[int] = None
    route_name: Optional[str] = None
    baseline_data: Optional[dict] = None
    thresholds: Optional[dict] = None
    program_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamConditionMonitoringProgramsOut(BaseModel):
    cm_program_id: int
    program_code: str
    program_name: str
    description: Optional[str] = None
    technology_code: str
    asset_id: int
    component_id: Optional[int] = None
    frequency_days: Optional[int] = None
    route_name: Optional[str] = None
    baseline_data: Optional[dict] = None
    thresholds: Optional[dict] = None
    program_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamConditionReadingsCreate(BaseModel):
    reading_id: int
    cm_program_id: int
    meter_id: Optional[int] = None
    asset_id: int
    reading_time: datetime
    reading_value: float
    baseline_value: Optional[float] = None
    deviation_pct: Optional[float] = None
    severity_code: Optional[str] = None
    trend_direction: Optional[str] = None
    spectrum_data: Optional[dict] = None
    thermogram_url: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class EamConditionReadingsUpdate(BaseModel):
    reading_id: Optional[int] = None
    cm_program_id: Optional[int] = None
    meter_id: Optional[int] = None
    asset_id: Optional[int] = None
    reading_time: Optional[datetime] = None
    reading_value: Optional[float] = None
    baseline_value: Optional[float] = None
    deviation_pct: Optional[float] = None
    severity_code: Optional[str] = None
    trend_direction: Optional[str] = None
    spectrum_data: Optional[dict] = None
    thermogram_url: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class EamConditionReadingsOut(BaseModel):
    reading_id: int
    cm_program_id: int
    meter_id: Optional[int] = None
    asset_id: int
    reading_time: datetime
    reading_value: float
    baseline_value: Optional[float] = None
    deviation_pct: Optional[float] = None
    severity_code: Optional[str] = None
    trend_direction: Optional[str] = None
    spectrum_data: Optional[dict] = None
    thermogram_url: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamContractAssetsCreate(BaseModel):
    contract_asset_id: int
    contract_id: int
    asset_id: int
    coverage_start_date: Optional[date] = None
    coverage_end_date: Optional[date] = None
    coverage_details: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class EamContractAssetsUpdate(BaseModel):
    contract_asset_id: Optional[int] = None
    contract_id: Optional[int] = None
    asset_id: Optional[int] = None
    coverage_start_date: Optional[date] = None
    coverage_end_date: Optional[date] = None
    coverage_details: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class EamContractAssetsOut(BaseModel):
    contract_asset_id: int
    contract_id: int
    asset_id: int
    coverage_start_date: Optional[date] = None
    coverage_end_date: Optional[date] = None
    coverage_details: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamCraftsCreate(BaseModel):
    craft_code: str
    craft_name: str
    description: Optional[str] = None
    trade_group_code: Optional[str] = None
    hourly_rate: Optional[float] = None
    overtime_rate: Optional[float] = None
    travel_rate: Optional[float] = None
    requires_certification: Optional[bool] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: bool = True

class EamCraftsUpdate(BaseModel):
    craft_code: Optional[str] = None
    craft_name: Optional[str] = None
    description: Optional[str] = None
    trade_group_code: Optional[str] = None
    hourly_rate: Optional[float] = None
    overtime_rate: Optional[float] = None
    travel_rate: Optional[float] = None
    requires_certification: Optional[bool] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: Optional[bool] = None

class EamCraftsOut(BaseModel):
    craft_code: str
    craft_name: str
    description: Optional[str] = None
    trade_group_code: Optional[str] = None
    hourly_rate: Optional[float] = None
    overtime_rate: Optional[float] = None
    travel_rate: Optional[float] = None
    requires_certification: Optional[bool] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: bool
    model_config = {"from_attributes": True}

class EamDecommissionPlansCreate(BaseModel):
    decommission_plan_id: int
    plan_number: str
    plan_name: str
    description: Optional[str] = None
    asset_id: int
    planned_date: Optional[date] = None
    actual_date: Optional[date] = None
    reason: Optional[str] = None
    decommission_method: Optional[str] = None
    steps_required: Optional[dict] = None
    approvals_required: Optional[dict] = None
    environmental_considerations: Optional[str] = None
    safety_considerations: Optional[str] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    disposal_proceeds: Optional[float] = None
    net_proceeds: Optional[float] = None
    plan_status_code: Optional[str] = None
    certificate_of_disposal_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamDecommissionPlansUpdate(BaseModel):
    decommission_plan_id: Optional[int] = None
    plan_number: Optional[str] = None
    plan_name: Optional[str] = None
    description: Optional[str] = None
    asset_id: Optional[int] = None
    planned_date: Optional[date] = None
    actual_date: Optional[date] = None
    reason: Optional[str] = None
    decommission_method: Optional[str] = None
    steps_required: Optional[dict] = None
    approvals_required: Optional[dict] = None
    environmental_considerations: Optional[str] = None
    safety_considerations: Optional[str] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    disposal_proceeds: Optional[float] = None
    net_proceeds: Optional[float] = None
    plan_status_code: Optional[str] = None
    certificate_of_disposal_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamDecommissionPlansOut(BaseModel):
    decommission_plan_id: int
    plan_number: str
    plan_name: str
    description: Optional[str] = None
    asset_id: int
    planned_date: Optional[date] = None
    actual_date: Optional[date] = None
    reason: Optional[str] = None
    decommission_method: Optional[str] = None
    steps_required: Optional[dict] = None
    approvals_required: Optional[dict] = None
    environmental_considerations: Optional[str] = None
    safety_considerations: Optional[str] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    disposal_proceeds: Optional[float] = None
    net_proceeds: Optional[float] = None
    plan_status_code: Optional[str] = None
    certificate_of_disposal_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class EamDocumentAssignmentsCreate(BaseModel):
    document_assignment_id: int
    document_id: int
    assignment_type: str
    assignment_id: int
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class EamDocumentAssignmentsUpdate(BaseModel):
    document_assignment_id: Optional[int] = None
    document_id: Optional[int] = None
    assignment_type: Optional[str] = None
    assignment_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class EamDocumentAssignmentsOut(BaseModel):
    document_assignment_id: int
    document_id: int
    assignment_type: str
    assignment_id: int
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamDocumentsCreate(BaseModel):
    document_id: int
    document_number: str
    document_name: str
    description: Optional[str] = None
    document_type_code: str
    revision_number: Optional[str] = None
    revision_date: Optional[date] = None
    author: Optional[str] = None
    owner: Optional[str] = None
    file_url: Optional[str] = None
    file_type: Optional[str] = None
    file_size_bytes: Optional[int] = None
    keywords: Optional[str] = None
    document_status_code: Optional[str] = None
    superseded_by_document_id: Optional[int] = None
    approval_required: Optional[bool] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamDocumentsUpdate(BaseModel):
    document_id: Optional[int] = None
    document_number: Optional[str] = None
    document_name: Optional[str] = None
    description: Optional[str] = None
    document_type_code: Optional[str] = None
    revision_number: Optional[str] = None
    revision_date: Optional[date] = None
    author: Optional[str] = None
    owner: Optional[str] = None
    file_url: Optional[str] = None
    file_type: Optional[str] = None
    file_size_bytes: Optional[int] = None
    keywords: Optional[str] = None
    document_status_code: Optional[str] = None
    superseded_by_document_id: Optional[int] = None
    approval_required: Optional[bool] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamDocumentsOut(BaseModel):
    document_id: int
    document_number: str
    document_name: str
    description: Optional[str] = None
    document_type_code: str
    revision_number: Optional[str] = None
    revision_date: Optional[date] = None
    author: Optional[str] = None
    owner: Optional[str] = None
    file_url: Optional[str] = None
    file_type: Optional[str] = None
    file_size_bytes: Optional[int] = None
    keywords: Optional[str] = None
    document_status_code: Optional[str] = None
    superseded_by_document_id: Optional[int] = None
    approval_required: Optional[bool] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamFailureCodesCreate(BaseModel):
    failure_code_id: int
    failure_code: str
    failure_name: str
    description: Optional[str] = None
    failure_type_code: str
    parent_failure_code_id: Optional[int] = None
    asset_type_id: Optional[int] = None
    component_type_code: Optional[str] = None
    is_safety_related: Optional[bool] = None
    is_environmental: Optional[bool] = None
    default_severity: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamFailureCodesUpdate(BaseModel):
    failure_code_id: Optional[int] = None
    failure_code: Optional[str] = None
    failure_name: Optional[str] = None
    description: Optional[str] = None
    failure_type_code: Optional[str] = None
    parent_failure_code_id: Optional[int] = None
    asset_type_id: Optional[int] = None
    component_type_code: Optional[str] = None
    is_safety_related: Optional[bool] = None
    is_environmental: Optional[bool] = None
    default_severity: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamFailureCodesOut(BaseModel):
    failure_code_id: int
    failure_code: str
    failure_name: str
    description: Optional[str] = None
    failure_type_code: str
    parent_failure_code_id: Optional[int] = None
    asset_type_id: Optional[int] = None
    component_type_code: Optional[str] = None
    is_safety_related: Optional[bool] = None
    is_environmental: Optional[bool] = None
    default_severity: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamFailureHistoryCreate(BaseModel):
    failure_history_id: int
    asset_id: int
    component_id: Optional[int] = None
    work_order_id: Optional[int] = None
    failure_code_id: Optional[int] = None
    failure_date: datetime
    detection_date: Optional[datetime] = None
    repair_date: Optional[datetime] = None
    downtime_hours: Optional[float] = None
    repair_hours: Optional[float] = None
    repair_cost: Optional[float] = None
    production_loss_cost: Optional[float] = None
    total_cost: Optional[float] = None
    failure_severity: Optional[str] = None
    failure_description: Optional[str] = None
    root_cause: Optional[str] = None
    corrective_action: Optional[str] = None
    is_recurring: Optional[bool] = None
    related_failure_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamFailureHistoryUpdate(BaseModel):
    failure_history_id: Optional[int] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    work_order_id: Optional[int] = None
    failure_code_id: Optional[int] = None
    failure_date: Optional[datetime] = None
    detection_date: Optional[datetime] = None
    repair_date: Optional[datetime] = None
    downtime_hours: Optional[float] = None
    repair_hours: Optional[float] = None
    repair_cost: Optional[float] = None
    production_loss_cost: Optional[float] = None
    total_cost: Optional[float] = None
    failure_severity: Optional[str] = None
    failure_description: Optional[str] = None
    root_cause: Optional[str] = None
    corrective_action: Optional[str] = None
    is_recurring: Optional[bool] = None
    related_failure_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamFailureHistoryOut(BaseModel):
    failure_history_id: int
    asset_id: int
    component_id: Optional[int] = None
    work_order_id: Optional[int] = None
    failure_code_id: Optional[int] = None
    failure_date: datetime
    detection_date: Optional[datetime] = None
    repair_date: Optional[datetime] = None
    downtime_hours: Optional[float] = None
    repair_hours: Optional[float] = None
    repair_cost: Optional[float] = None
    production_loss_cost: Optional[float] = None
    total_cost: Optional[float] = None
    failure_severity: Optional[str] = None
    failure_description: Optional[str] = None
    root_cause: Optional[str] = None
    corrective_action: Optional[str] = None
    is_recurring: Optional[bool] = None
    related_failure_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class EamFmeaItemsCreate(BaseModel):
    fmea_item_id: int
    fmea_study_id: int
    item_sequence: int
    function_description: Optional[str] = None
    potential_failure_mode: str
    potential_effect: Optional[str] = None
    severity_rating: int
    potential_cause: Optional[str] = None
    occurrence_rating: int
    current_controls: Optional[str] = None
    detection_rating: int
    rpn: Optional[int] = None
    recommended_action: Optional[str] = None
    action_assigned_to: Optional[str] = None
    action_due_date: Optional[date] = None
    action_completed_date: Optional[date] = None
    action_taken: Optional[str] = None
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
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamFmeaItemsUpdate(BaseModel):
    fmea_item_id: Optional[int] = None
    fmea_study_id: Optional[int] = None
    item_sequence: Optional[int] = None
    function_description: Optional[str] = None
    potential_failure_mode: Optional[str] = None
    potential_effect: Optional[str] = None
    severity_rating: Optional[int] = None
    potential_cause: Optional[str] = None
    occurrence_rating: Optional[int] = None
    current_controls: Optional[str] = None
    detection_rating: Optional[int] = None
    rpn: Optional[int] = None
    recommended_action: Optional[str] = None
    action_assigned_to: Optional[str] = None
    action_due_date: Optional[date] = None
    action_completed_date: Optional[date] = None
    action_taken: Optional[str] = None
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
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamFmeaItemsOut(BaseModel):
    fmea_item_id: int
    fmea_study_id: int
    item_sequence: int
    function_description: Optional[str] = None
    potential_failure_mode: str
    potential_effect: Optional[str] = None
    severity_rating: int
    potential_cause: Optional[str] = None
    occurrence_rating: int
    current_controls: Optional[str] = None
    detection_rating: int
    rpn: Optional[int] = None
    recommended_action: Optional[str] = None
    action_assigned_to: Optional[str] = None
    action_due_date: Optional[date] = None
    action_completed_date: Optional[date] = None
    action_taken: Optional[str] = None
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
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamFmeaStudiesCreate(BaseModel):
    fmea_study_id: int
    study_code: str
    study_name: str
    description: Optional[str] = None
    asset_id: int
    component_id: Optional[int] = None
    system_description: Optional[str] = None
    fmea_type_code: Optional[str] = None
    study_status_code: Optional[str] = None
    fmea_facilitator: Optional[str] = None
    fmea_team_members: Optional[dict] = None
    study_date: Optional[date] = None
    revision_number: Optional[str] = None
    approval_date: Optional[date] = None
    approved_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamFmeaStudiesUpdate(BaseModel):
    fmea_study_id: Optional[int] = None
    study_code: Optional[str] = None
    study_name: Optional[str] = None
    description: Optional[str] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    system_description: Optional[str] = None
    fmea_type_code: Optional[str] = None
    study_status_code: Optional[str] = None
    fmea_facilitator: Optional[str] = None
    fmea_team_members: Optional[dict] = None
    study_date: Optional[date] = None
    revision_number: Optional[str] = None
    approval_date: Optional[date] = None
    approved_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamFmeaStudiesOut(BaseModel):
    fmea_study_id: int
    study_code: str
    study_name: str
    description: Optional[str] = None
    asset_id: int
    component_id: Optional[int] = None
    system_description: Optional[str] = None
    fmea_type_code: Optional[str] = None
    study_status_code: Optional[str] = None
    fmea_facilitator: Optional[str] = None
    fmea_team_members: Optional[dict] = None
    study_date: Optional[date] = None
    revision_number: Optional[str] = None
    approval_date: Optional[date] = None
    approved_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamFunctionalLocationsCreate(BaseModel):
    functional_location_id: int
    location_code: str
    location_name: str
    description: Optional[str] = None
    location_type_code: str
    parent_location_id: Optional[int] = None
    location_path: Optional[str] = None
    gps_latitude: Optional[float] = None
    gps_longitude: Optional[float] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state_province: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    site_id_ref: Optional[int] = None
    supervisor_id: Optional[int] = None
    safety_zone_code: Optional[str] = None
    environmental_zone_code: Optional[str] = None
    has_confined_space: Optional[bool] = None
    has_hazardous_materials: Optional[bool] = None
    permits_required: Optional[dict] = None
    location_drawing_url: Optional[str] = None
    p_and_id_url: Optional[str] = None
    location_status_code: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamFunctionalLocationsUpdate(BaseModel):
    functional_location_id: Optional[int] = None
    location_code: Optional[str] = None
    location_name: Optional[str] = None
    description: Optional[str] = None
    location_type_code: Optional[str] = None
    parent_location_id: Optional[int] = None
    location_path: Optional[str] = None
    gps_latitude: Optional[float] = None
    gps_longitude: Optional[float] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state_province: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    site_id_ref: Optional[int] = None
    supervisor_id: Optional[int] = None
    safety_zone_code: Optional[str] = None
    environmental_zone_code: Optional[str] = None
    has_confined_space: Optional[bool] = None
    has_hazardous_materials: Optional[bool] = None
    permits_required: Optional[dict] = None
    location_drawing_url: Optional[str] = None
    p_and_id_url: Optional[str] = None
    location_status_code: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamFunctionalLocationsOut(BaseModel):
    functional_location_id: int
    location_code: str
    location_name: str
    description: Optional[str] = None
    location_type_code: str
    parent_location_id: Optional[int] = None
    location_path: Optional[str] = None
    gps_latitude: Optional[float] = None
    gps_longitude: Optional[float] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state_province: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    site_id_ref: Optional[int] = None
    supervisor_id: Optional[int] = None
    safety_zone_code: Optional[str] = None
    environmental_zone_code: Optional[str] = None
    has_confined_space: Optional[bool] = None
    has_hazardous_materials: Optional[bool] = None
    permits_required: Optional[dict] = None
    location_drawing_url: Optional[str] = None
    p_and_id_url: Optional[str] = None
    location_status_code: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamInspectionsCreate(BaseModel):
    inspection_id: int
    inspection_number: str
    inspection_name: str
    description: Optional[str] = None
    inspection_type_code: str
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    work_order_id: Optional[int] = None
    checklist_json: Optional[dict] = None
    frequency_days: Optional[int] = None
    last_inspection_date: Optional[date] = None
    next_inspection_date: Optional[date] = None
    inspector_id: Optional[int] = None
    inspector_name: Optional[str] = None
    inspection_date: Optional[date] = None
    result_code: Optional[str] = None
    result_summary: Optional[str] = None
    deficiencies_found: Optional[dict] = None
    corrective_action_id: Optional[int] = None
    certificate_issued: Optional[bool] = None
    certificate_number: Optional[str] = None
    certificate_expiry: Optional[date] = None
    regulatory_body: Optional[str] = None
    inspection_status_code: Optional[str] = None
    inspection_document_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamInspectionsUpdate(BaseModel):
    inspection_id: Optional[int] = None
    inspection_number: Optional[str] = None
    inspection_name: Optional[str] = None
    description: Optional[str] = None
    inspection_type_code: Optional[str] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    work_order_id: Optional[int] = None
    checklist_json: Optional[dict] = None
    frequency_days: Optional[int] = None
    last_inspection_date: Optional[date] = None
    next_inspection_date: Optional[date] = None
    inspector_id: Optional[int] = None
    inspector_name: Optional[str] = None
    inspection_date: Optional[date] = None
    result_code: Optional[str] = None
    result_summary: Optional[str] = None
    deficiencies_found: Optional[dict] = None
    corrective_action_id: Optional[int] = None
    certificate_issued: Optional[bool] = None
    certificate_number: Optional[str] = None
    certificate_expiry: Optional[date] = None
    regulatory_body: Optional[str] = None
    inspection_status_code: Optional[str] = None
    inspection_document_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamInspectionsOut(BaseModel):
    inspection_id: int
    inspection_number: str
    inspection_name: str
    description: Optional[str] = None
    inspection_type_code: str
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    work_order_id: Optional[int] = None
    checklist_json: Optional[dict] = None
    frequency_days: Optional[int] = None
    last_inspection_date: Optional[date] = None
    next_inspection_date: Optional[date] = None
    inspector_id: Optional[int] = None
    inspector_name: Optional[str] = None
    inspection_date: Optional[date] = None
    result_code: Optional[str] = None
    result_summary: Optional[str] = None
    deficiencies_found: Optional[dict] = None
    corrective_action_id: Optional[int] = None
    certificate_issued: Optional[bool] = None
    certificate_number: Optional[str] = None
    certificate_expiry: Optional[date] = None
    regulatory_body: Optional[str] = None
    inspection_status_code: Optional[str] = None
    inspection_document_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class EamIntegrationConnectionsCreate(BaseModel):
    connection_id: int
    connection_code: str
    connection_name: str
    connection_type_code: str
    protocol_code: str
    endpoint_url: Optional[str] = None
    authentication_type: Optional[str] = None
    credentials_encrypted: Optional[str] = None
    schedule_cron: Optional[str] = None
    connection_status: Optional[str] = None
    last_sync_date: Optional[datetime] = None
    sync_frequency_min: Optional[int] = None
    retry_count: Optional[int] = None
    timeout_seconds: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamIntegrationConnectionsUpdate(BaseModel):
    connection_id: Optional[int] = None
    connection_code: Optional[str] = None
    connection_name: Optional[str] = None
    connection_type_code: Optional[str] = None
    protocol_code: Optional[str] = None
    endpoint_url: Optional[str] = None
    authentication_type: Optional[str] = None
    credentials_encrypted: Optional[str] = None
    schedule_cron: Optional[str] = None
    connection_status: Optional[str] = None
    last_sync_date: Optional[datetime] = None
    sync_frequency_min: Optional[int] = None
    retry_count: Optional[int] = None
    timeout_seconds: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamIntegrationConnectionsOut(BaseModel):
    connection_id: int
    connection_code: str
    connection_name: str
    connection_type_code: str
    protocol_code: str
    endpoint_url: Optional[str] = None
    authentication_type: Optional[str] = None
    credentials_encrypted: Optional[str] = None
    schedule_cron: Optional[str] = None
    connection_status: Optional[str] = None
    last_sync_date: Optional[datetime] = None
    sync_frequency_min: Optional[int] = None
    retry_count: Optional[int] = None
    timeout_seconds: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamIntegrationLogsCreate(BaseModel):
    log_id: int
    connection_id: int
    log_type_code: str
    direction: str
    status_code: str
    payload_sent: Optional[dict] = None
    payload_received: Optional[dict] = None
    error_message: Optional[str] = None
    records_processed: Optional[int] = None
    records_failed: Optional[int] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration_ms: Optional[int] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None

class EamIntegrationLogsUpdate(BaseModel):
    log_id: Optional[int] = None
    connection_id: Optional[int] = None
    log_type_code: Optional[str] = None
    direction: Optional[str] = None
    status_code: Optional[str] = None
    payload_sent: Optional[dict] = None
    payload_received: Optional[dict] = None
    error_message: Optional[str] = None
    records_processed: Optional[int] = None
    records_failed: Optional[int] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration_ms: Optional[int] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None

class EamIntegrationLogsOut(BaseModel):
    log_id: int
    connection_id: int
    log_type_code: str
    direction: str
    status_code: str
    payload_sent: Optional[dict] = None
    payload_received: Optional[dict] = None
    error_message: Optional[str] = None
    records_processed: Optional[int] = None
    records_failed: Optional[int] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration_ms: Optional[int] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamJsaCreate(BaseModel):
    jsa_id: int
    jsa_number: str
    work_order_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    jsa_date: Optional[date] = None
    prepared_by: Optional[str] = None
    reviewed_by: Optional[str] = None
    approved_by: Optional[str] = None
    jsa_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamJsaUpdate(BaseModel):
    jsa_id: Optional[int] = None
    jsa_number: Optional[str] = None
    work_order_id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    jsa_date: Optional[date] = None
    prepared_by: Optional[str] = None
    reviewed_by: Optional[str] = None
    approved_by: Optional[str] = None
    jsa_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamJsaOut(BaseModel):
    jsa_id: int
    jsa_number: str
    work_order_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    jsa_date: Optional[date] = None
    prepared_by: Optional[str] = None
    reviewed_by: Optional[str] = None
    approved_by: Optional[str] = None
    jsa_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamJsaStepsCreate(BaseModel):
    jsa_step_id: int
    jsa_id: int
    step_sequence: int
    step_description: str
    hazards: Optional[str] = None
    controls: Optional[str] = None
    responsible_party: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class EamJsaStepsUpdate(BaseModel):
    jsa_step_id: Optional[int] = None
    jsa_id: Optional[int] = None
    step_sequence: Optional[int] = None
    step_description: Optional[str] = None
    hazards: Optional[str] = None
    controls: Optional[str] = None
    responsible_party: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class EamJsaStepsOut(BaseModel):
    jsa_step_id: int
    jsa_id: int
    step_sequence: int
    step_description: str
    hazards: Optional[str] = None
    controls: Optional[str] = None
    responsible_party: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamKitContentsCreate(BaseModel):
    kit_content_id: int
    kit_id: int
    item_id: int
    item_code: str
    quantity: float
    unit_of_measure: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamKitContentsUpdate(BaseModel):
    kit_content_id: Optional[int] = None
    kit_id: Optional[int] = None
    item_id: Optional[int] = None
    item_code: Optional[str] = None
    quantity: Optional[float] = None
    unit_of_measure: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamKitContentsOut(BaseModel):
    kit_content_id: int
    kit_id: int
    item_id: int
    item_code: str
    quantity: float
    unit_of_measure: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamKitsCreate(BaseModel):
    kit_id: int
    kit_code: str
    kit_name: str
    description: Optional[str] = None
    pm_template_id: Optional[int] = None
    kit_location: Optional[str] = None
    kit_status_code: Optional[str] = None
    kit_cost: Optional[float] = None
    last_restock_date: Optional[datetime] = None
    kit_version: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamKitsUpdate(BaseModel):
    kit_id: Optional[int] = None
    kit_code: Optional[str] = None
    kit_name: Optional[str] = None
    description: Optional[str] = None
    pm_template_id: Optional[int] = None
    kit_location: Optional[str] = None
    kit_status_code: Optional[str] = None
    kit_cost: Optional[float] = None
    last_restock_date: Optional[datetime] = None
    kit_version: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamKitsOut(BaseModel):
    kit_id: int
    kit_code: str
    kit_name: str
    description: Optional[str] = None
    pm_template_id: Optional[int] = None
    kit_location: Optional[str] = None
    kit_status_code: Optional[str] = None
    kit_cost: Optional[float] = None
    last_restock_date: Optional[datetime] = None
    kit_version: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamKpiDefinitionsCreate(BaseModel):
    kpi_code: str
    kpi_name: str
    description: Optional[str] = None
    formula: str
    unit_of_measure: Optional[str] = None
    higher_is_better: Optional[bool] = None
    benchmark_value: Optional[float] = None
    target_value: Optional[float] = None
    warning_threshold: Optional[float] = None
    critical_threshold: Optional[float] = None
    kpi_category: Optional[str] = None
    calculation_frequency: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: bool = True

class EamKpiDefinitionsUpdate(BaseModel):
    kpi_code: Optional[str] = None
    kpi_name: Optional[str] = None
    description: Optional[str] = None
    formula: Optional[str] = None
    unit_of_measure: Optional[str] = None
    higher_is_better: Optional[bool] = None
    benchmark_value: Optional[float] = None
    target_value: Optional[float] = None
    warning_threshold: Optional[float] = None
    critical_threshold: Optional[float] = None
    kpi_category: Optional[str] = None
    calculation_frequency: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: Optional[bool] = None

class EamKpiDefinitionsOut(BaseModel):
    kpi_code: str
    kpi_name: str
    description: Optional[str] = None
    formula: str
    unit_of_measure: Optional[str] = None
    higher_is_better: Optional[bool] = None
    benchmark_value: Optional[float] = None
    target_value: Optional[float] = None
    warning_threshold: Optional[float] = None
    critical_threshold: Optional[float] = None
    kpi_category: Optional[str] = None
    calculation_frequency: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: bool
    model_config = {"from_attributes": True}

class EamKpiValuesCreate(BaseModel):
    kpi_value_id: int
    kpi_code: str
    asset_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    calculation_date: date
    period_type: str
    period_start_date: date
    period_end_date: date
    actual_value: float
    target_value: Optional[float] = None
    benchmark_value: Optional[float] = None
    variance_pct: Optional[float] = None
    status_code: Optional[str] = None
    calculation_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamKpiValuesUpdate(BaseModel):
    kpi_value_id: Optional[int] = None
    kpi_code: Optional[str] = None
    asset_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    calculation_date: Optional[date] = None
    period_type: Optional[str] = None
    period_start_date: Optional[date] = None
    period_end_date: Optional[date] = None
    actual_value: Optional[float] = None
    target_value: Optional[float] = None
    benchmark_value: Optional[float] = None
    variance_pct: Optional[float] = None
    status_code: Optional[str] = None
    calculation_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamKpiValuesOut(BaseModel):
    kpi_value_id: int
    kpi_code: str
    asset_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    calculation_date: date
    period_type: str
    period_start_date: date
    period_end_date: date
    actual_value: float
    target_value: Optional[float] = None
    benchmark_value: Optional[float] = None
    variance_pct: Optional[float] = None
    status_code: Optional[str] = None
    calculation_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamLanggraphWorkflowsCreate(BaseModel):
    workflow_id: int
    workflow_name: str
    workflow_description: Optional[str] = None
    workflow_domain: Optional[str] = None
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
    organization_id: Optional[int] = None

class EamLanggraphWorkflowsUpdate(BaseModel):
    workflow_id: Optional[int] = None
    workflow_name: Optional[str] = None
    workflow_description: Optional[str] = None
    workflow_domain: Optional[str] = None
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
    organization_id: Optional[int] = None

class EamLanggraphWorkflowsOut(BaseModel):
    workflow_id: int
    workflow_name: str
    workflow_description: Optional[str] = None
    workflow_domain: Optional[str] = None
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
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamLlmConfigsCreate(BaseModel):
    llm_config_id: int
    config_name: str
    provider: str
    model_name: str
    api_endpoint: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    parameters: Optional[dict] = None
    max_retries: Optional[int] = None
    timeout_seconds: Optional[int] = None
    cost_per_1k_tokens: Optional[float] = None
    config_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class EamLlmConfigsUpdate(BaseModel):
    llm_config_id: Optional[int] = None
    config_name: Optional[str] = None
    provider: Optional[str] = None
    model_name: Optional[str] = None
    api_endpoint: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    parameters: Optional[dict] = None
    max_retries: Optional[int] = None
    timeout_seconds: Optional[int] = None
    cost_per_1k_tokens: Optional[float] = None
    config_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class EamLlmConfigsOut(BaseModel):
    llm_config_id: int
    config_name: str
    provider: str
    model_name: str
    api_endpoint: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    parameters: Optional[dict] = None
    max_retries: Optional[int] = None
    timeout_seconds: Optional[int] = None
    cost_per_1k_tokens: Optional[float] = None
    config_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamLotoCreate(BaseModel):
    loto_id: int
    loto_number: str
    work_order_id: Optional[int] = None
    equipment_id: Optional[int] = None
    asset_id: Optional[int] = None
    description: str
    energy_sources: dict
    isolation_points: Optional[dict] = None
    lock_type: Optional[str] = None
    number_of_locks: Optional[int] = None
    applied_by: str
    applied_date: datetime
    removed_by: Optional[str] = None
    removed_date: Optional[datetime] = None
    verification_method: Optional[str] = None
    verified_by: Optional[str] = None
    verified_date: Optional[datetime] = None
    loto_status_code: Optional[str] = None
    notes: Optional[str] = None
    loto_diagram_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamLotoUpdate(BaseModel):
    loto_id: Optional[int] = None
    loto_number: Optional[str] = None
    work_order_id: Optional[int] = None
    equipment_id: Optional[int] = None
    asset_id: Optional[int] = None
    description: Optional[str] = None
    energy_sources: Optional[dict] = None
    isolation_points: Optional[dict] = None
    lock_type: Optional[str] = None
    number_of_locks: Optional[int] = None
    applied_by: Optional[str] = None
    applied_date: Optional[datetime] = None
    removed_by: Optional[str] = None
    removed_date: Optional[datetime] = None
    verification_method: Optional[str] = None
    verified_by: Optional[str] = None
    verified_date: Optional[datetime] = None
    loto_status_code: Optional[str] = None
    notes: Optional[str] = None
    loto_diagram_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamLotoOut(BaseModel):
    loto_id: int
    loto_number: str
    work_order_id: Optional[int] = None
    equipment_id: Optional[int] = None
    asset_id: Optional[int] = None
    description: str
    energy_sources: dict
    isolation_points: Optional[dict] = None
    lock_type: Optional[str] = None
    number_of_locks: Optional[int] = None
    applied_by: str
    applied_date: datetime
    removed_by: Optional[str] = None
    removed_date: Optional[datetime] = None
    verification_method: Optional[str] = None
    verified_by: Optional[str] = None
    verified_date: Optional[datetime] = None
    loto_status_code: Optional[str] = None
    notes: Optional[str] = None
    loto_diagram_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamMaintenanceCostsCreate(BaseModel):
    cost_id: int
    work_order_id: Optional[int] = None
    asset_id: int
    component_id: Optional[int] = None
    cost_category_code: str
    cost_type_code: str
    cost_amount: float
    currency_code: Optional[str] = None
    cost_date: date
    description: Optional[str] = None
    reference_type: Optional[str] = None
    reference_id: Optional[int] = None
    posted_to_gl: Optional[bool] = None
    gl_posting_date: Optional[datetime] = None
    gl_account_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamMaintenanceCostsUpdate(BaseModel):
    cost_id: Optional[int] = None
    work_order_id: Optional[int] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    cost_category_code: Optional[str] = None
    cost_type_code: Optional[str] = None
    cost_amount: Optional[float] = None
    currency_code: Optional[str] = None
    cost_date: Optional[date] = None
    description: Optional[str] = None
    reference_type: Optional[str] = None
    reference_id: Optional[int] = None
    posted_to_gl: Optional[bool] = None
    gl_posting_date: Optional[datetime] = None
    gl_account_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamMaintenanceCostsOut(BaseModel):
    cost_id: int
    work_order_id: Optional[int] = None
    asset_id: int
    component_id: Optional[int] = None
    cost_category_code: str
    cost_type_code: str
    cost_amount: float
    currency_code: Optional[str] = None
    cost_date: date
    description: Optional[str] = None
    reference_type: Optional[str] = None
    reference_id: Optional[int] = None
    posted_to_gl: Optional[bool] = None
    gl_posting_date: Optional[datetime] = None
    gl_account_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamMeterAssignmentsCreate(BaseModel):
    meter_assignment_id: int
    meter_id: int
    asset_id: int
    component_id: Optional[int] = None
    installation_date: Optional[date] = None
    removal_date: Optional[date] = None
    initial_reading: Optional[float] = None
    last_reading: Optional[float] = None
    last_reading_date: Optional[datetime] = None
    cumulative_reading: Optional[bool] = None
    assignment_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamMeterAssignmentsUpdate(BaseModel):
    meter_assignment_id: Optional[int] = None
    meter_id: Optional[int] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    installation_date: Optional[date] = None
    removal_date: Optional[date] = None
    initial_reading: Optional[float] = None
    last_reading: Optional[float] = None
    last_reading_date: Optional[datetime] = None
    cumulative_reading: Optional[bool] = None
    assignment_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamMeterAssignmentsOut(BaseModel):
    meter_assignment_id: int
    meter_id: int
    asset_id: int
    component_id: Optional[int] = None
    installation_date: Optional[date] = None
    removal_date: Optional[date] = None
    initial_reading: Optional[float] = None
    last_reading: Optional[float] = None
    last_reading_date: Optional[datetime] = None
    cumulative_reading: Optional[bool] = None
    assignment_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamMeterReadingsCreate(BaseModel):
    time: datetime
    meter_id: int
    asset_id: int
    reading_value: float
    reading_value_text: Optional[str] = None
    unit_code: str
    reading_method_code: Optional[str] = None
    operator_id: Optional[int] = None
    quality_flag: Optional[str] = None
    alarm_status: Optional[str] = None
    source_system_code: Optional[str] = None
    source_reading_id: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None

class EamMeterReadingsUpdate(BaseModel):
    time: Optional[datetime] = None
    meter_id: Optional[int] = None
    asset_id: Optional[int] = None
    reading_value: Optional[float] = None
    reading_value_text: Optional[str] = None
    unit_code: Optional[str] = None
    reading_method_code: Optional[str] = None
    operator_id: Optional[int] = None
    quality_flag: Optional[str] = None
    alarm_status: Optional[str] = None
    source_system_code: Optional[str] = None
    source_reading_id: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None

class EamMeterReadingsOut(BaseModel):
    time: datetime
    meter_id: int
    asset_id: int
    reading_value: float
    reading_value_text: Optional[str] = None
    unit_code: str
    reading_method_code: Optional[str] = None
    operator_id: Optional[int] = None
    quality_flag: Optional[str] = None
    alarm_status: Optional[str] = None
    source_system_code: Optional[str] = None
    source_reading_id: Optional[str] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamMetersCreate(BaseModel):
    meter_id: int
    meter_code: str
    meter_name: str
    description: Optional[str] = None
    meter_type_code: str
    unit_of_measure: str
    data_type_code: Optional[str] = None
    possible_values: Optional[dict] = None
    reading_source_code: Optional[str] = None
    reading_frequency: Optional[str] = None
    warning_threshold_high: Optional[float] = None
    warning_threshold_low: Optional[float] = None
    critical_threshold_high: Optional[float] = None
    critical_threshold_low: Optional[float] = None
    decimal_precision: Optional[int] = None
    meter_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamMetersUpdate(BaseModel):
    meter_id: Optional[int] = None
    meter_code: Optional[str] = None
    meter_name: Optional[str] = None
    description: Optional[str] = None
    meter_type_code: Optional[str] = None
    unit_of_measure: Optional[str] = None
    data_type_code: Optional[str] = None
    possible_values: Optional[dict] = None
    reading_source_code: Optional[str] = None
    reading_frequency: Optional[str] = None
    warning_threshold_high: Optional[float] = None
    warning_threshold_low: Optional[float] = None
    critical_threshold_high: Optional[float] = None
    critical_threshold_low: Optional[float] = None
    decimal_precision: Optional[int] = None
    meter_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamMetersOut(BaseModel):
    meter_id: int
    meter_code: str
    meter_name: str
    description: Optional[str] = None
    meter_type_code: str
    unit_of_measure: str
    data_type_code: Optional[str] = None
    possible_values: Optional[dict] = None
    reading_source_code: Optional[str] = None
    reading_frequency: Optional[str] = None
    warning_threshold_high: Optional[float] = None
    warning_threshold_low: Optional[float] = None
    critical_threshold_high: Optional[float] = None
    critical_threshold_low: Optional[float] = None
    decimal_precision: Optional[int] = None
    meter_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamMlModelsCreate(BaseModel):
    model_id: int
    model_code: str
    model_name: str
    description: Optional[str] = None
    model_type_code: str
    model_framework: str
    model_version: str
    model_parameters: Optional[dict] = None
    training_data_source: Optional[str] = None
    training_parameters: Optional[dict] = None
    training_date: Optional[datetime] = None
    training_duration_sec: Optional[int] = None
    training_accuracy: Optional[float] = None
    training_loss: Optional[float] = None
    validation_accuracy: Optional[float] = None
    validation_loss: Optional[float] = None
    test_accuracy: Optional[float] = None
    feature_importance: Optional[dict] = None
    model_artifacts_url: Optional[str] = None
    deployment_status: Optional[str] = None
    deployment_date: Optional[datetime] = None
    inference_endpoint_url: Optional[str] = None
    monitoring_metrics: Optional[dict] = None
    retraining_schedule: Optional[str] = None
    last_retrained_date: Optional[datetime] = None
    parent_model_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamMlModelsUpdate(BaseModel):
    model_id: Optional[int] = None
    model_code: Optional[str] = None
    model_name: Optional[str] = None
    description: Optional[str] = None
    model_type_code: Optional[str] = None
    model_framework: Optional[str] = None
    model_version: Optional[str] = None
    model_parameters: Optional[dict] = None
    training_data_source: Optional[str] = None
    training_parameters: Optional[dict] = None
    training_date: Optional[datetime] = None
    training_duration_sec: Optional[int] = None
    training_accuracy: Optional[float] = None
    training_loss: Optional[float] = None
    validation_accuracy: Optional[float] = None
    validation_loss: Optional[float] = None
    test_accuracy: Optional[float] = None
    feature_importance: Optional[dict] = None
    model_artifacts_url: Optional[str] = None
    deployment_status: Optional[str] = None
    deployment_date: Optional[datetime] = None
    inference_endpoint_url: Optional[str] = None
    monitoring_metrics: Optional[dict] = None
    retraining_schedule: Optional[str] = None
    last_retrained_date: Optional[datetime] = None
    parent_model_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamMlModelsOut(BaseModel):
    model_id: int
    model_code: str
    model_name: str
    description: Optional[str] = None
    model_type_code: str
    model_framework: str
    model_version: str
    model_parameters: Optional[dict] = None
    training_data_source: Optional[str] = None
    training_parameters: Optional[dict] = None
    training_date: Optional[datetime] = None
    training_duration_sec: Optional[int] = None
    training_accuracy: Optional[float] = None
    training_loss: Optional[float] = None
    validation_accuracy: Optional[float] = None
    validation_loss: Optional[float] = None
    test_accuracy: Optional[float] = None
    feature_importance: Optional[dict] = None
    model_artifacts_url: Optional[str] = None
    deployment_status: Optional[str] = None
    deployment_date: Optional[datetime] = None
    inference_endpoint_url: Optional[str] = None
    monitoring_metrics: Optional[dict] = None
    retraining_schedule: Optional[str] = None
    last_retrained_date: Optional[datetime] = None
    parent_model_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamNotificationsCreate(BaseModel):
    notification_id: int
    alert_id: Optional[int] = None
    notification_type_code: str
    recipient_type: str
    recipient_address: Optional[str] = None
    subject: Optional[str] = None
    message: Optional[str] = None
    sent_date: Optional[datetime] = None
    read_date: Optional[datetime] = None
    delivery_status_code: Optional[str] = None
    failure_reason: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class EamNotificationsUpdate(BaseModel):
    notification_id: Optional[int] = None
    alert_id: Optional[int] = None
    notification_type_code: Optional[str] = None
    recipient_type: Optional[str] = None
    recipient_address: Optional[str] = None
    subject: Optional[str] = None
    message: Optional[str] = None
    sent_date: Optional[datetime] = None
    read_date: Optional[datetime] = None
    delivery_status_code: Optional[str] = None
    failure_reason: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class EamNotificationsOut(BaseModel):
    notification_id: int
    alert_id: Optional[int] = None
    notification_type_code: str
    recipient_type: str
    recipient_address: Optional[str] = None
    subject: Optional[str] = None
    message: Optional[str] = None
    sent_date: Optional[datetime] = None
    read_date: Optional[datetime] = None
    delivery_status_code: Optional[str] = None
    failure_reason: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamOptimizationProblemsCreate(BaseModel):
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
    solution_quality: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamOptimizationProblemsUpdate(BaseModel):
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
    solution_quality: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamOptimizationProblemsOut(BaseModel):
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
    solution_quality: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamOptimizationSolutionsCreate(BaseModel):
    solution_id: int
    problem_id: int
    solution_name: Optional[str] = None
    solution_data: dict
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    solution_quality: Optional[str] = None
    solver_log: Optional[str] = None
    solution_version: Optional[int] = None
    is_best: Optional[bool] = None
    is_feasible: Optional[bool] = None
    constraint_violations: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamOptimizationSolutionsUpdate(BaseModel):
    solution_id: Optional[int] = None
    problem_id: Optional[int] = None
    solution_name: Optional[str] = None
    solution_data: Optional[dict] = None
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    solution_quality: Optional[str] = None
    solver_log: Optional[str] = None
    solution_version: Optional[int] = None
    is_best: Optional[bool] = None
    is_feasible: Optional[bool] = None
    constraint_violations: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamOptimizationSolutionsOut(BaseModel):
    solution_id: int
    problem_id: int
    solution_name: Optional[str] = None
    solution_data: dict
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    solution_quality: Optional[str] = None
    solver_log: Optional[str] = None
    solution_version: Optional[int] = None
    is_best: Optional[bool] = None
    is_feasible: Optional[bool] = None
    constraint_violations: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamOrtoolsProblemsCreate(BaseModel):
    ortools_problem_id: int
    problem_id: Optional[int] = None
    problem_type_code: str
    solver_type: Optional[str] = None
    problem_data: dict
    solver_parameters: Optional[dict] = None
    solution_data: Optional[dict] = None
    solve_time_ms: Optional[int] = None
    solution_quality: Optional[str] = None
    solver_log: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class EamOrtoolsProblemsUpdate(BaseModel):
    ortools_problem_id: Optional[int] = None
    problem_id: Optional[int] = None
    problem_type_code: Optional[str] = None
    solver_type: Optional[str] = None
    problem_data: Optional[dict] = None
    solver_parameters: Optional[dict] = None
    solution_data: Optional[dict] = None
    solve_time_ms: Optional[int] = None
    solution_quality: Optional[str] = None
    solver_log: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class EamOrtoolsProblemsOut(BaseModel):
    ortools_problem_id: int
    problem_id: Optional[int] = None
    problem_type_code: str
    solver_type: Optional[str] = None
    problem_data: dict
    solver_parameters: Optional[dict] = None
    solution_data: Optional[dict] = None
    solve_time_ms: Optional[int] = None
    solution_quality: Optional[str] = None
    solver_log: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamPermitsCreate(BaseModel):
    permit_id: int
    permit_number: str
    permit_type_code: str
    work_order_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    description: Optional[str] = None
    issuer_id: int
    issuer_name: Optional[str] = None
    recipient_id: int
    recipient_name: Optional[str] = None
    issued_date: Optional[datetime] = None
    effective_start: Optional[datetime] = None
    effective_end: Optional[datetime] = None
    extended_end: Optional[datetime] = None
    permit_status_code: Optional[str] = None
    conditions: Optional[str] = None
    special_requirements: Optional[str] = None
    cancellation_notes: Optional[str] = None
    permit_document_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamPermitsUpdate(BaseModel):
    permit_id: Optional[int] = None
    permit_number: Optional[str] = None
    permit_type_code: Optional[str] = None
    work_order_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    description: Optional[str] = None
    issuer_id: Optional[int] = None
    issuer_name: Optional[str] = None
    recipient_id: Optional[int] = None
    recipient_name: Optional[str] = None
    issued_date: Optional[datetime] = None
    effective_start: Optional[datetime] = None
    effective_end: Optional[datetime] = None
    extended_end: Optional[datetime] = None
    permit_status_code: Optional[str] = None
    conditions: Optional[str] = None
    special_requirements: Optional[str] = None
    cancellation_notes: Optional[str] = None
    permit_document_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamPermitsOut(BaseModel):
    permit_id: int
    permit_number: str
    permit_type_code: str
    work_order_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    description: Optional[str] = None
    issuer_id: int
    issuer_name: Optional[str] = None
    recipient_id: int
    recipient_name: Optional[str] = None
    issued_date: Optional[datetime] = None
    effective_start: Optional[datetime] = None
    effective_end: Optional[datetime] = None
    extended_end: Optional[datetime] = None
    permit_status_code: Optional[str] = None
    conditions: Optional[str] = None
    special_requirements: Optional[str] = None
    cancellation_notes: Optional[str] = None
    permit_document_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamPhysicalLocationsCreate(BaseModel):
    physical_location_id: int
    location_code: str
    location_name: str
    description: Optional[str] = None
    location_type_code: str
    parent_location_id: Optional[int] = None
    location_path: Optional[str] = None
    functional_location_id: Optional[int] = None
    gps_latitude: Optional[float] = None
    gps_longitude: Optional[float] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state_province: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    floor_area_sqm: Optional[float] = None
    max_weight_kg: Optional[float] = None
    max_height_m: Optional[float] = None
    climate_controlled: Optional[bool] = None
    hazmat_capable: Optional[bool] = None
    location_map_url: Optional[str] = None
    location_status_code: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamPhysicalLocationsUpdate(BaseModel):
    physical_location_id: Optional[int] = None
    location_code: Optional[str] = None
    location_name: Optional[str] = None
    description: Optional[str] = None
    location_type_code: Optional[str] = None
    parent_location_id: Optional[int] = None
    location_path: Optional[str] = None
    functional_location_id: Optional[int] = None
    gps_latitude: Optional[float] = None
    gps_longitude: Optional[float] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state_province: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    floor_area_sqm: Optional[float] = None
    max_weight_kg: Optional[float] = None
    max_height_m: Optional[float] = None
    climate_controlled: Optional[bool] = None
    hazmat_capable: Optional[bool] = None
    location_map_url: Optional[str] = None
    location_status_code: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamPhysicalLocationsOut(BaseModel):
    physical_location_id: int
    location_code: str
    location_name: str
    description: Optional[str] = None
    location_type_code: str
    parent_location_id: Optional[int] = None
    location_path: Optional[str] = None
    functional_location_id: Optional[int] = None
    gps_latitude: Optional[float] = None
    gps_longitude: Optional[float] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state_province: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    floor_area_sqm: Optional[float] = None
    max_weight_kg: Optional[float] = None
    max_height_m: Optional[float] = None
    climate_controlled: Optional[bool] = None
    hazmat_capable: Optional[bool] = None
    location_map_url: Optional[str] = None
    location_status_code: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamPmAssignmentsCreate(BaseModel):
    pm_assignment_id: int
    pm_template_id: int
    asset_id: int
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    assignment_status_code: Optional[str] = None
    custom_frequency_value: Optional[float] = None
    custom_frequency_uom: Optional[str] = None
    last_performed_date: Optional[datetime] = None
    next_due_date: Optional[datetime] = None
    meter_trigger_value: Optional[float] = None
    meter_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamPmAssignmentsUpdate(BaseModel):
    pm_assignment_id: Optional[int] = None
    pm_template_id: Optional[int] = None
    asset_id: Optional[int] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    assignment_status_code: Optional[str] = None
    custom_frequency_value: Optional[float] = None
    custom_frequency_uom: Optional[str] = None
    last_performed_date: Optional[datetime] = None
    next_due_date: Optional[datetime] = None
    meter_trigger_value: Optional[float] = None
    meter_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamPmAssignmentsOut(BaseModel):
    pm_assignment_id: int
    pm_template_id: int
    asset_id: int
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    assignment_status_code: Optional[str] = None
    custom_frequency_value: Optional[float] = None
    custom_frequency_uom: Optional[str] = None
    last_performed_date: Optional[datetime] = None
    next_due_date: Optional[datetime] = None
    meter_trigger_value: Optional[float] = None
    meter_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamPmScheduleOptimizedCreate(BaseModel):
    pm_sched_opt_id: int
    pm_sched_problem_id: int
    pm_schedule_id: Optional[int] = None
    asset_id: int
    pm_template_id: Optional[int] = None
    scheduled_date: date
    scheduled_time_slot: Optional[str] = None
    technician_id: Optional[int] = None
    estimated_hours: Optional[float] = None
    priority_score: Optional[float] = None
    sequence_order: Optional[int] = None
    constraint_satisfied: Optional[bool] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None

class EamPmScheduleOptimizedUpdate(BaseModel):
    pm_sched_opt_id: Optional[int] = None
    pm_sched_problem_id: Optional[int] = None
    pm_schedule_id: Optional[int] = None
    asset_id: Optional[int] = None
    pm_template_id: Optional[int] = None
    scheduled_date: Optional[date] = None
    scheduled_time_slot: Optional[str] = None
    technician_id: Optional[int] = None
    estimated_hours: Optional[float] = None
    priority_score: Optional[float] = None
    sequence_order: Optional[int] = None
    constraint_satisfied: Optional[bool] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None

class EamPmScheduleOptimizedOut(BaseModel):
    pm_sched_opt_id: int
    pm_sched_problem_id: int
    pm_schedule_id: Optional[int] = None
    asset_id: int
    pm_template_id: Optional[int] = None
    scheduled_date: date
    scheduled_time_slot: Optional[str] = None
    technician_id: Optional[int] = None
    estimated_hours: Optional[float] = None
    priority_score: Optional[float] = None
    sequence_order: Optional[int] = None
    constraint_satisfied: Optional[bool] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamPmSchedulesCreate(BaseModel):
    pm_schedule_id: int
    pm_assignment_id: int
    pm_template_id: int
    asset_id: int
    work_order_id: Optional[int] = None
    due_date: datetime
    earliest_date: Optional[datetime] = None
    latest_date: Optional[datetime] = None
    scheduled_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None
    schedule_status_code: Optional[str] = None
    generation_date: Optional[datetime] = None
    frequency_value: Optional[float] = None
    frequency_uom: Optional[str] = None
    meter_reading_at_gen: Optional[float] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamPmSchedulesUpdate(BaseModel):
    pm_schedule_id: Optional[int] = None
    pm_assignment_id: Optional[int] = None
    pm_template_id: Optional[int] = None
    asset_id: Optional[int] = None
    work_order_id: Optional[int] = None
    due_date: Optional[datetime] = None
    earliest_date: Optional[datetime] = None
    latest_date: Optional[datetime] = None
    scheduled_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None
    schedule_status_code: Optional[str] = None
    generation_date: Optional[datetime] = None
    frequency_value: Optional[float] = None
    frequency_uom: Optional[str] = None
    meter_reading_at_gen: Optional[float] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamPmSchedulesOut(BaseModel):
    pm_schedule_id: int
    pm_assignment_id: int
    pm_template_id: int
    asset_id: int
    work_order_id: Optional[int] = None
    due_date: datetime
    earliest_date: Optional[datetime] = None
    latest_date: Optional[datetime] = None
    scheduled_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None
    schedule_status_code: Optional[str] = None
    generation_date: Optional[datetime] = None
    frequency_value: Optional[float] = None
    frequency_uom: Optional[str] = None
    meter_reading_at_gen: Optional[float] = None
    notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamPmSchedulingProblemsCreate(BaseModel):
    pm_sched_problem_id: int
    problem_id: int
    planning_horizon_days: int
    schedule_start_date: date
    schedule_end_date: Optional[date] = None
    objective_weight_cost: Optional[float] = None
    objective_weight_downtime: Optional[float] = None
    objective_weight_workload: Optional[float] = None
    technician_availability: Optional[dict] = None
    production_schedule: Optional[dict] = None
    asset_availability: Optional[dict] = None
    resource_limits: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamPmSchedulingProblemsUpdate(BaseModel):
    pm_sched_problem_id: Optional[int] = None
    problem_id: Optional[int] = None
    planning_horizon_days: Optional[int] = None
    schedule_start_date: Optional[date] = None
    schedule_end_date: Optional[date] = None
    objective_weight_cost: Optional[float] = None
    objective_weight_downtime: Optional[float] = None
    objective_weight_workload: Optional[float] = None
    technician_availability: Optional[dict] = None
    production_schedule: Optional[dict] = None
    asset_availability: Optional[dict] = None
    resource_limits: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamPmSchedulingProblemsOut(BaseModel):
    pm_sched_problem_id: int
    problem_id: int
    planning_horizon_days: int
    schedule_start_date: date
    schedule_end_date: Optional[date] = None
    objective_weight_cost: Optional[float] = None
    objective_weight_downtime: Optional[float] = None
    objective_weight_workload: Optional[float] = None
    technician_availability: Optional[dict] = None
    production_schedule: Optional[dict] = None
    asset_availability: Optional[dict] = None
    resource_limits: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamPmTemplatesCreate(BaseModel):
    pm_template_id: int
    template_code: str
    template_name: str
    description: Optional[str] = None
    asset_type_id: Optional[int] = None
    work_order_type_code: Optional[str] = None
    frequency_type_code: str
    frequency_value: float
    frequency_uom: str
    tolerance_before_pct: Optional[float] = None
    tolerance_after_pct: Optional[float] = None
    estimated_hours: Optional[float] = None
    estimated_cost: Optional[float] = None
    requires_downtime: Optional[bool] = None
    requires_permit: Optional[bool] = None
    requires_loto: Optional[bool] = None
    requires_inspection: Optional[bool] = None
    requires_measurements: Optional[bool] = None
    craft_code: Optional[str] = None
    priority_code: Optional[str] = None
    safety_requirements: Optional[str] = None
    procedure_text: Optional[str] = None
    checklist_json: Optional[dict] = None
    template_version: Optional[str] = None
    template_status_code: Optional[str] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    approval_required: Optional[bool] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamPmTemplatesUpdate(BaseModel):
    pm_template_id: Optional[int] = None
    template_code: Optional[str] = None
    template_name: Optional[str] = None
    description: Optional[str] = None
    asset_type_id: Optional[int] = None
    work_order_type_code: Optional[str] = None
    frequency_type_code: Optional[str] = None
    frequency_value: Optional[float] = None
    frequency_uom: Optional[str] = None
    tolerance_before_pct: Optional[float] = None
    tolerance_after_pct: Optional[float] = None
    estimated_hours: Optional[float] = None
    estimated_cost: Optional[float] = None
    requires_downtime: Optional[bool] = None
    requires_permit: Optional[bool] = None
    requires_loto: Optional[bool] = None
    requires_inspection: Optional[bool] = None
    requires_measurements: Optional[bool] = None
    craft_code: Optional[str] = None
    priority_code: Optional[str] = None
    safety_requirements: Optional[str] = None
    procedure_text: Optional[str] = None
    checklist_json: Optional[dict] = None
    template_version: Optional[str] = None
    template_status_code: Optional[str] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    approval_required: Optional[bool] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamPmTemplatesOut(BaseModel):
    pm_template_id: int
    template_code: str
    template_name: str
    description: Optional[str] = None
    asset_type_id: Optional[int] = None
    work_order_type_code: Optional[str] = None
    frequency_type_code: str
    frequency_value: float
    frequency_uom: str
    tolerance_before_pct: Optional[float] = None
    tolerance_after_pct: Optional[float] = None
    estimated_hours: Optional[float] = None
    estimated_cost: Optional[float] = None
    requires_downtime: Optional[bool] = None
    requires_permit: Optional[bool] = None
    requires_loto: Optional[bool] = None
    requires_inspection: Optional[bool] = None
    requires_measurements: Optional[bool] = None
    craft_code: Optional[str] = None
    priority_code: Optional[str] = None
    safety_requirements: Optional[str] = None
    procedure_text: Optional[str] = None
    checklist_json: Optional[dict] = None
    template_version: Optional[str] = None
    template_status_code: Optional[str] = None
    effective_start_date: Optional[date] = None
    effective_end_date: Optional[date] = None
    approval_required: Optional[bool] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamPredictionsCreate(BaseModel):
    prediction_id: int
    model_id: int
    prediction_type_code: str
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    prediction_date: datetime
    prediction_horizon_days: Optional[int] = None
    predicted_value: float
    predicted_value_min: Optional[float] = None
    predicted_value_max: Optional[float] = None
    prediction_probability: Optional[float] = None
    confidence_score: Optional[float] = None
    features_used: Optional[dict] = None
    feature_values: Optional[dict] = None
    actual_value: Optional[float] = None
    prediction_error: Optional[float] = None
    prediction_accuracy: Optional[float] = None
    is_validated: Optional[bool] = None
    scenario_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamPredictionsUpdate(BaseModel):
    prediction_id: Optional[int] = None
    model_id: Optional[int] = None
    prediction_type_code: Optional[str] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    prediction_date: Optional[datetime] = None
    prediction_horizon_days: Optional[int] = None
    predicted_value: Optional[float] = None
    predicted_value_min: Optional[float] = None
    predicted_value_max: Optional[float] = None
    prediction_probability: Optional[float] = None
    confidence_score: Optional[float] = None
    features_used: Optional[dict] = None
    feature_values: Optional[dict] = None
    actual_value: Optional[float] = None
    prediction_error: Optional[float] = None
    prediction_accuracy: Optional[float] = None
    is_validated: Optional[bool] = None
    scenario_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamPredictionsOut(BaseModel):
    prediction_id: int
    model_id: int
    prediction_type_code: str
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    prediction_date: datetime
    prediction_horizon_days: Optional[int] = None
    predicted_value: float
    predicted_value_min: Optional[float] = None
    predicted_value_max: Optional[float] = None
    prediction_probability: Optional[float] = None
    confidence_score: Optional[float] = None
    features_used: Optional[dict] = None
    feature_values: Optional[dict] = None
    actual_value: Optional[float] = None
    prediction_error: Optional[float] = None
    prediction_accuracy: Optional[float] = None
    is_validated: Optional[bool] = None
    scenario_id: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamPredictiveMaintenanceCreate(BaseModel):
    pdm_id: int
    asset_id: int
    component_id: Optional[int] = None
    model_id: Optional[int] = None
    prediction_id: Optional[int] = None
    health_score: Optional[float] = None
    rul_days: Optional[float] = None
    rul_confidence: Optional[float] = None
    failure_probability: Optional[float] = None
    predicted_failure_mode: Optional[str] = None
    recommended_action: Optional[str] = None
    priority_code: Optional[str] = None
    work_order_id: Optional[int] = None
    alert_id: Optional[int] = None
    pdm_status_code: Optional[str] = None
    evaluation_date: Optional[datetime] = None
    actual_failure_date: Optional[datetime] = None
    prediction_accuracy: Optional[float] = None
    model_retrained: Optional[bool] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamPredictiveMaintenanceUpdate(BaseModel):
    pdm_id: Optional[int] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    model_id: Optional[int] = None
    prediction_id: Optional[int] = None
    health_score: Optional[float] = None
    rul_days: Optional[float] = None
    rul_confidence: Optional[float] = None
    failure_probability: Optional[float] = None
    predicted_failure_mode: Optional[str] = None
    recommended_action: Optional[str] = None
    priority_code: Optional[str] = None
    work_order_id: Optional[int] = None
    alert_id: Optional[int] = None
    pdm_status_code: Optional[str] = None
    evaluation_date: Optional[datetime] = None
    actual_failure_date: Optional[datetime] = None
    prediction_accuracy: Optional[float] = None
    model_retrained: Optional[bool] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamPredictiveMaintenanceOut(BaseModel):
    pdm_id: int
    asset_id: int
    component_id: Optional[int] = None
    model_id: Optional[int] = None
    prediction_id: Optional[int] = None
    health_score: Optional[float] = None
    rul_days: Optional[float] = None
    rul_confidence: Optional[float] = None
    failure_probability: Optional[float] = None
    predicted_failure_mode: Optional[str] = None
    recommended_action: Optional[str] = None
    priority_code: Optional[str] = None
    work_order_id: Optional[int] = None
    alert_id: Optional[int] = None
    pdm_status_code: Optional[str] = None
    evaluation_date: Optional[datetime] = None
    actual_failure_date: Optional[datetime] = None
    prediction_accuracy: Optional[float] = None
    model_retrained: Optional[bool] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamPromptTemplatesCreate(BaseModel):
    prompt_template_id: int
    template_code: str
    template_name: str
    description: Optional[str] = None
    template_type_code: str
    llm_config_id: Optional[int] = None
    system_prompt: str
    user_prompt_template: Optional[str] = None
    variables_json: Optional[dict] = None
    output_schema: Optional[dict] = None
    template_version: Optional[str] = None
    template_status_code: Optional[str] = None
    usage_count: Optional[int] = None
    avg_response_time_ms: Optional[int] = None
    avg_cost_per_call: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class EamPromptTemplatesUpdate(BaseModel):
    prompt_template_id: Optional[int] = None
    template_code: Optional[str] = None
    template_name: Optional[str] = None
    description: Optional[str] = None
    template_type_code: Optional[str] = None
    llm_config_id: Optional[int] = None
    system_prompt: Optional[str] = None
    user_prompt_template: Optional[str] = None
    variables_json: Optional[dict] = None
    output_schema: Optional[dict] = None
    template_version: Optional[str] = None
    template_status_code: Optional[str] = None
    usage_count: Optional[int] = None
    avg_response_time_ms: Optional[int] = None
    avg_cost_per_call: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class EamPromptTemplatesOut(BaseModel):
    prompt_template_id: int
    template_code: str
    template_name: str
    description: Optional[str] = None
    template_type_code: str
    llm_config_id: Optional[int] = None
    system_prompt: str
    user_prompt_template: Optional[str] = None
    variables_json: Optional[dict] = None
    output_schema: Optional[dict] = None
    template_version: Optional[str] = None
    template_status_code: Optional[str] = None
    usage_count: Optional[int] = None
    avg_response_time_ms: Optional[int] = None
    avg_cost_per_call: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamRcaActionsCreate(BaseModel):
    rca_action_id: int
    rca_study_id: int
    rca_cause_id: Optional[int] = None
    action_description: str
    action_type_code: Optional[str] = None
    assigned_to: Optional[str] = None
    due_date: Optional[date] = None
    completed_date: Optional[date] = None
    action_status_code: Optional[str] = None
    effectiveness_review: Optional[str] = None
    effectiveness_rating: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamRcaActionsUpdate(BaseModel):
    rca_action_id: Optional[int] = None
    rca_study_id: Optional[int] = None
    rca_cause_id: Optional[int] = None
    action_description: Optional[str] = None
    action_type_code: Optional[str] = None
    assigned_to: Optional[str] = None
    due_date: Optional[date] = None
    completed_date: Optional[date] = None
    action_status_code: Optional[str] = None
    effectiveness_review: Optional[str] = None
    effectiveness_rating: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamRcaActionsOut(BaseModel):
    rca_action_id: int
    rca_study_id: int
    rca_cause_id: Optional[int] = None
    action_description: str
    action_type_code: Optional[str] = None
    assigned_to: Optional[str] = None
    due_date: Optional[date] = None
    completed_date: Optional[date] = None
    action_status_code: Optional[str] = None
    effectiveness_review: Optional[str] = None
    effectiveness_rating: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamRcaCausesCreate(BaseModel):
    rca_cause_id: int
    rca_study_id: int
    parent_cause_id: Optional[int] = None
    cause_level: int
    cause_description: str
    cause_type_code: Optional[str] = None
    evidence: Optional[str] = None
    category_code: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamRcaCausesUpdate(BaseModel):
    rca_cause_id: Optional[int] = None
    rca_study_id: Optional[int] = None
    parent_cause_id: Optional[int] = None
    cause_level: Optional[int] = None
    cause_description: Optional[str] = None
    cause_type_code: Optional[str] = None
    evidence: Optional[str] = None
    category_code: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamRcaCausesOut(BaseModel):
    rca_cause_id: int
    rca_study_id: int
    parent_cause_id: Optional[int] = None
    cause_level: int
    cause_description: str
    cause_type_code: Optional[str] = None
    evidence: Optional[str] = None
    category_code: Optional[str] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamRcaStudiesCreate(BaseModel):
    rca_study_id: int
    study_code: str
    study_name: str
    description: Optional[str] = None
    work_order_id: Optional[int] = None
    asset_id: Optional[int] = None
    failure_history_id: Optional[int] = None
    rca_method_code: str
    study_status_code: Optional[str] = None
    problem_statement: str
    rca_facilitator: Optional[str] = None
    rca_participants: Optional[dict] = None
    study_date: Optional[date] = None
    conclusion: Optional[str] = None
    recommendation: Optional[str] = None
    revision_number: Optional[str] = None
    approval_date: Optional[date] = None
    approved_by: Optional[str] = None
    ai_generated: Optional[bool] = None
    ai_confidence_score: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamRcaStudiesUpdate(BaseModel):
    rca_study_id: Optional[int] = None
    study_code: Optional[str] = None
    study_name: Optional[str] = None
    description: Optional[str] = None
    work_order_id: Optional[int] = None
    asset_id: Optional[int] = None
    failure_history_id: Optional[int] = None
    rca_method_code: Optional[str] = None
    study_status_code: Optional[str] = None
    problem_statement: Optional[str] = None
    rca_facilitator: Optional[str] = None
    rca_participants: Optional[dict] = None
    study_date: Optional[date] = None
    conclusion: Optional[str] = None
    recommendation: Optional[str] = None
    revision_number: Optional[str] = None
    approval_date: Optional[date] = None
    approved_by: Optional[str] = None
    ai_generated: Optional[bool] = None
    ai_confidence_score: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamRcaStudiesOut(BaseModel):
    rca_study_id: int
    study_code: str
    study_name: str
    description: Optional[str] = None
    work_order_id: Optional[int] = None
    asset_id: Optional[int] = None
    failure_history_id: Optional[int] = None
    rca_method_code: str
    study_status_code: Optional[str] = None
    problem_statement: str
    rca_facilitator: Optional[str] = None
    rca_participants: Optional[dict] = None
    study_date: Optional[date] = None
    conclusion: Optional[str] = None
    recommendation: Optional[str] = None
    revision_number: Optional[str] = None
    approval_date: Optional[date] = None
    approved_by: Optional[str] = None
    ai_generated: Optional[bool] = None
    ai_confidence_score: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamRcmAnalysesCreate(BaseModel):
    rcm_analysis_id: int
    rcm_study_id: int
    function_description: str
    functional_failure: str
    failure_mode: str
    failure_effect: Optional[str] = None
    failure_consequence: Optional[str] = None
    severity_rating: Optional[int] = None
    occurrence_rating: Optional[int] = None
    detection_rating: Optional[int] = None
    rpn: Optional[int] = None
    is_hidden_failure: Optional[bool] = None
    task_type_code: Optional[str] = None
    recommended_task: Optional[str] = None
    task_interval: Optional[str] = None
    task_description: Optional[str] = None
    responsible_group: Optional[str] = None
    analysis_sequence: int
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamRcmAnalysesUpdate(BaseModel):
    rcm_analysis_id: Optional[int] = None
    rcm_study_id: Optional[int] = None
    function_description: Optional[str] = None
    functional_failure: Optional[str] = None
    failure_mode: Optional[str] = None
    failure_effect: Optional[str] = None
    failure_consequence: Optional[str] = None
    severity_rating: Optional[int] = None
    occurrence_rating: Optional[int] = None
    detection_rating: Optional[int] = None
    rpn: Optional[int] = None
    is_hidden_failure: Optional[bool] = None
    task_type_code: Optional[str] = None
    recommended_task: Optional[str] = None
    task_interval: Optional[str] = None
    task_description: Optional[str] = None
    responsible_group: Optional[str] = None
    analysis_sequence: Optional[int] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamRcmAnalysesOut(BaseModel):
    rcm_analysis_id: int
    rcm_study_id: int
    function_description: str
    functional_failure: str
    failure_mode: str
    failure_effect: Optional[str] = None
    failure_consequence: Optional[str] = None
    severity_rating: Optional[int] = None
    occurrence_rating: Optional[int] = None
    detection_rating: Optional[int] = None
    rpn: Optional[int] = None
    is_hidden_failure: Optional[bool] = None
    task_type_code: Optional[str] = None
    recommended_task: Optional[str] = None
    task_interval: Optional[str] = None
    task_description: Optional[str] = None
    responsible_group: Optional[str] = None
    analysis_sequence: int
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamRcmStudiesCreate(BaseModel):
    rcm_study_id: int
    study_code: str
    study_name: str
    description: Optional[str] = None
    asset_id: int
    system_boundary: Optional[str] = None
    study_status_code: Optional[str] = None
    rcm_facilitator: Optional[str] = None
    rcm_team_members: Optional[dict] = None
    study_date: Optional[date] = None
    revision_number: Optional[str] = None
    approval_date: Optional[date] = None
    approved_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamRcmStudiesUpdate(BaseModel):
    rcm_study_id: Optional[int] = None
    study_code: Optional[str] = None
    study_name: Optional[str] = None
    description: Optional[str] = None
    asset_id: Optional[int] = None
    system_boundary: Optional[str] = None
    study_status_code: Optional[str] = None
    rcm_facilitator: Optional[str] = None
    rcm_team_members: Optional[dict] = None
    study_date: Optional[date] = None
    revision_number: Optional[str] = None
    approval_date: Optional[date] = None
    approved_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamRcmStudiesOut(BaseModel):
    rcm_study_id: int
    study_code: str
    study_name: str
    description: Optional[str] = None
    asset_id: int
    system_boundary: Optional[str] = None
    study_status_code: Optional[str] = None
    rcm_facilitator: Optional[str] = None
    rcm_team_members: Optional[dict] = None
    study_date: Optional[date] = None
    revision_number: Optional[str] = None
    approval_date: Optional[date] = None
    approved_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamSafetyPlansCreate(BaseModel):
    safety_plan_id: int
    plan_code: str
    plan_name: str
    description: Optional[str] = None
    work_order_id: Optional[int] = None
    plan_type_code: str
    plan_status_code: Optional[str] = None
    hazards_identified: Optional[dict] = None
    ppe_required: Optional[dict] = None
    safety_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamSafetyPlansUpdate(BaseModel):
    safety_plan_id: Optional[int] = None
    plan_code: Optional[str] = None
    plan_name: Optional[str] = None
    description: Optional[str] = None
    work_order_id: Optional[int] = None
    plan_type_code: Optional[str] = None
    plan_status_code: Optional[str] = None
    hazards_identified: Optional[dict] = None
    ppe_required: Optional[dict] = None
    safety_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamSafetyPlansOut(BaseModel):
    safety_plan_id: int
    plan_code: str
    plan_name: str
    description: Optional[str] = None
    work_order_id: Optional[int] = None
    plan_type_code: str
    plan_status_code: Optional[str] = None
    hazards_identified: Optional[dict] = None
    ppe_required: Optional[dict] = None
    safety_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamScenariosCreate(BaseModel):
    scenario_id: int
    scenario_code: str
    scenario_name: str
    description: Optional[str] = None
    scenario_type_code: str
    problem_id: Optional[int] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    parameters: Optional[dict] = None
    objectives: Optional[dict] = None
    results: Optional[dict] = None
    scenario_status_code: Optional[str] = None
    execution_date: Optional[datetime] = None
    execution_duration_ms: Optional[int] = None
    created_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamScenariosUpdate(BaseModel):
    scenario_id: Optional[int] = None
    scenario_code: Optional[str] = None
    scenario_name: Optional[str] = None
    description: Optional[str] = None
    scenario_type_code: Optional[str] = None
    problem_id: Optional[int] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    parameters: Optional[dict] = None
    objectives: Optional[dict] = None
    results: Optional[dict] = None
    scenario_status_code: Optional[str] = None
    execution_date: Optional[datetime] = None
    execution_duration_ms: Optional[int] = None
    created_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamScenariosOut(BaseModel):
    scenario_id: int
    scenario_code: str
    scenario_name: str
    description: Optional[str] = None
    scenario_type_code: str
    problem_id: Optional[int] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    parameters: Optional[dict] = None
    objectives: Optional[dict] = None
    results: Optional[dict] = None
    scenario_status_code: Optional[str] = None
    execution_date: Optional[datetime] = None
    execution_duration_ms: Optional[int] = None
    created_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamScipyAnalysesCreate(BaseModel):
    scipy_analysis_id: int
    analysis_name: str
    analysis_type_code: str
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    input_data: dict
    parameters: Optional[dict] = None
    results: dict
    quality_metrics: Optional[dict] = None
    analysis_date: Optional[datetime] = None
    execution_time_ms: Optional[int] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamScipyAnalysesUpdate(BaseModel):
    scipy_analysis_id: Optional[int] = None
    analysis_name: Optional[str] = None
    analysis_type_code: Optional[str] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    input_data: Optional[dict] = None
    parameters: Optional[dict] = None
    results: Optional[dict] = None
    quality_metrics: Optional[dict] = None
    analysis_date: Optional[datetime] = None
    execution_time_ms: Optional[int] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamScipyAnalysesOut(BaseModel):
    scipy_analysis_id: int
    analysis_name: str
    analysis_type_code: str
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    input_data: dict
    parameters: Optional[dict] = None
    results: dict
    quality_metrics: Optional[dict] = None
    analysis_date: Optional[datetime] = None
    execution_time_ms: Optional[int] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamServiceContractsCreate(BaseModel):
    contract_id: int
    contract_number: str
    contract_name: str
    description: Optional[str] = None
    contract_type_code: str
    vendor_id: int
    vendor_name: Optional[str] = None
    start_date: date
    end_date: date
    renewal_date: Optional[date] = None
    contract_value: Optional[float] = None
    currency_code: Optional[str] = None
    payment_terms: Optional[str] = None
    sla_response_time_hours: Optional[float] = None
    sla_resolution_time_hours: Optional[float] = None
    penalty_rate: Optional[float] = None
    coverage_description: Optional[str] = None
    exclusions: Optional[str] = None
    contract_status_code: Optional[str] = None
    auto_renew: Optional[bool] = None
    approval_required: Optional[bool] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    contract_document_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamServiceContractsUpdate(BaseModel):
    contract_id: Optional[int] = None
    contract_number: Optional[str] = None
    contract_name: Optional[str] = None
    description: Optional[str] = None
    contract_type_code: Optional[str] = None
    vendor_id: Optional[int] = None
    vendor_name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    renewal_date: Optional[date] = None
    contract_value: Optional[float] = None
    currency_code: Optional[str] = None
    payment_terms: Optional[str] = None
    sla_response_time_hours: Optional[float] = None
    sla_resolution_time_hours: Optional[float] = None
    penalty_rate: Optional[float] = None
    coverage_description: Optional[str] = None
    exclusions: Optional[str] = None
    contract_status_code: Optional[str] = None
    auto_renew: Optional[bool] = None
    approval_required: Optional[bool] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    contract_document_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamServiceContractsOut(BaseModel):
    contract_id: int
    contract_number: str
    contract_name: str
    description: Optional[str] = None
    contract_type_code: str
    vendor_id: int
    vendor_name: Optional[str] = None
    start_date: date
    end_date: date
    renewal_date: Optional[date] = None
    contract_value: Optional[float] = None
    currency_code: Optional[str] = None
    payment_terms: Optional[str] = None
    sla_response_time_hours: Optional[float] = None
    sla_resolution_time_hours: Optional[float] = None
    penalty_rate: Optional[float] = None
    coverage_description: Optional[str] = None
    exclusions: Optional[str] = None
    contract_status_code: Optional[str] = None
    auto_renew: Optional[bool] = None
    approval_required: Optional[bool] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    contract_document_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamSparePartsConsumptionCreate(BaseModel):
    consumption_id: int
    work_order_id: int
    asset_bom_id: Optional[int] = None
    item_id: int
    item_code: str
    quantity_required: float
    quantity_issued: Optional[float] = None
    quantity_consumed: Optional[float] = None
    quantity_returned: Optional[float] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    warehouse_id: Optional[int] = None
    bin_location: Optional[str] = None
    issued_date: Optional[datetime] = None
    issued_by: Optional[str] = None
    returned_date: Optional[datetime] = None
    returned_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamSparePartsConsumptionUpdate(BaseModel):
    consumption_id: Optional[int] = None
    work_order_id: Optional[int] = None
    asset_bom_id: Optional[int] = None
    item_id: Optional[int] = None
    item_code: Optional[str] = None
    quantity_required: Optional[float] = None
    quantity_issued: Optional[float] = None
    quantity_consumed: Optional[float] = None
    quantity_returned: Optional[float] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    warehouse_id: Optional[int] = None
    bin_location: Optional[str] = None
    issued_date: Optional[datetime] = None
    issued_by: Optional[str] = None
    returned_date: Optional[datetime] = None
    returned_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamSparePartsConsumptionOut(BaseModel):
    consumption_id: int
    work_order_id: int
    asset_bom_id: Optional[int] = None
    item_id: int
    item_code: str
    quantity_required: float
    quantity_issued: Optional[float] = None
    quantity_consumed: Optional[float] = None
    quantity_returned: Optional[float] = None
    unit_cost: Optional[float] = None
    total_cost: Optional[float] = None
    warehouse_id: Optional[int] = None
    bin_location: Optional[str] = None
    issued_date: Optional[datetime] = None
    issued_by: Optional[str] = None
    returned_date: Optional[datetime] = None
    returned_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamSparePartsStorageCreate(BaseModel):
    result_id: int
    storage_opt_problem_id: int
    container_id: int
    container_type_code: str
    container_dimensions: Optional[dict] = None
    packed_parts: Optional[dict] = None
    utilization_percentage: Optional[float] = None
    num_parts_packed: Optional[int] = None
    avg_accessibility_score: Optional[float] = None
    weight_capacity: Optional[float] = None
    compatibility_rules: Optional[dict] = None
    fifo_required: Optional[bool] = None
    retrieval_sequence: Optional[dict] = None
    visualization_3d_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class EamSparePartsStorageUpdate(BaseModel):
    result_id: Optional[int] = None
    storage_opt_problem_id: Optional[int] = None
    container_id: Optional[int] = None
    container_type_code: Optional[str] = None
    container_dimensions: Optional[dict] = None
    packed_parts: Optional[dict] = None
    utilization_percentage: Optional[float] = None
    num_parts_packed: Optional[int] = None
    avg_accessibility_score: Optional[float] = None
    weight_capacity: Optional[float] = None
    compatibility_rules: Optional[dict] = None
    fifo_required: Optional[bool] = None
    retrieval_sequence: Optional[dict] = None
    visualization_3d_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class EamSparePartsStorageOut(BaseModel):
    result_id: int
    storage_opt_problem_id: int
    container_id: int
    container_type_code: str
    container_dimensions: Optional[dict] = None
    packed_parts: Optional[dict] = None
    utilization_percentage: Optional[float] = None
    num_parts_packed: Optional[int] = None
    avg_accessibility_score: Optional[float] = None
    weight_capacity: Optional[float] = None
    compatibility_rules: Optional[dict] = None
    fifo_required: Optional[bool] = None
    retrieval_sequence: Optional[dict] = None
    visualization_3d_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamStorageLocationsCreate(BaseModel):
    storage_location_id: int
    location_code: str
    location_name: str
    location_type_code: str
    parent_location_id: Optional[int] = None
    physical_location_id: Optional[int] = None
    width_cm: Optional[float] = None
    depth_cm: Optional[float] = None
    height_cm: Optional[float] = None
    max_weight_kg: Optional[float] = None
    climate_controlled: Optional[bool] = None
    hazmat_capable: Optional[bool] = None
    fifo_required: Optional[bool] = None
    picking_zone: Optional[str] = None
    location_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamStorageLocationsUpdate(BaseModel):
    storage_location_id: Optional[int] = None
    location_code: Optional[str] = None
    location_name: Optional[str] = None
    location_type_code: Optional[str] = None
    parent_location_id: Optional[int] = None
    physical_location_id: Optional[int] = None
    width_cm: Optional[float] = None
    depth_cm: Optional[float] = None
    height_cm: Optional[float] = None
    max_weight_kg: Optional[float] = None
    climate_controlled: Optional[bool] = None
    hazmat_capable: Optional[bool] = None
    fifo_required: Optional[bool] = None
    picking_zone: Optional[str] = None
    location_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamStorageLocationsOut(BaseModel):
    storage_location_id: int
    location_code: str
    location_name: str
    location_type_code: str
    parent_location_id: Optional[int] = None
    physical_location_id: Optional[int] = None
    width_cm: Optional[float] = None
    depth_cm: Optional[float] = None
    height_cm: Optional[float] = None
    max_weight_kg: Optional[float] = None
    climate_controlled: Optional[bool] = None
    hazmat_capable: Optional[bool] = None
    fifo_required: Optional[bool] = None
    picking_zone: Optional[str] = None
    location_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamStorageOptimizationProblemsCreate(BaseModel):
    storage_opt_problem_id: int
    problem_id: int
    storage_location_id: Optional[int] = None
    objective_weight_space: Optional[float] = None
    objective_weight_access: Optional[float] = None
    objective_weight_fifo: Optional[float] = None
    constraints: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class EamStorageOptimizationProblemsUpdate(BaseModel):
    storage_opt_problem_id: Optional[int] = None
    problem_id: Optional[int] = None
    storage_location_id: Optional[int] = None
    objective_weight_space: Optional[float] = None
    objective_weight_access: Optional[float] = None
    objective_weight_fifo: Optional[float] = None
    constraints: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class EamStorageOptimizationProblemsOut(BaseModel):
    storage_opt_problem_id: int
    problem_id: int
    storage_location_id: Optional[int] = None
    objective_weight_space: Optional[float] = None
    objective_weight_access: Optional[float] = None
    objective_weight_fifo: Optional[float] = None
    constraints: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamTechnicianCertificationsCreate(BaseModel):
    certification_id: int
    technician_id: int
    certification_code: str
    certification_name: str
    issuing_body: Optional[str] = None
    certification_level: Optional[str] = None
    date_obtained: date
    expiry_date: Optional[date] = None
    renewal_required: Optional[bool] = None
    renewal_interval_months: Optional[int] = None
    attachment_url: Optional[str] = None
    verification_status: Optional[str] = None
    verified_by: Optional[str] = None
    verified_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class EamTechnicianCertificationsUpdate(BaseModel):
    certification_id: Optional[int] = None
    technician_id: Optional[int] = None
    certification_code: Optional[str] = None
    certification_name: Optional[str] = None
    issuing_body: Optional[str] = None
    certification_level: Optional[str] = None
    date_obtained: Optional[date] = None
    expiry_date: Optional[date] = None
    renewal_required: Optional[bool] = None
    renewal_interval_months: Optional[int] = None
    attachment_url: Optional[str] = None
    verification_status: Optional[str] = None
    verified_by: Optional[str] = None
    verified_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class EamTechnicianCertificationsOut(BaseModel):
    certification_id: int
    technician_id: int
    certification_code: str
    certification_name: str
    issuing_body: Optional[str] = None
    certification_level: Optional[str] = None
    date_obtained: date
    expiry_date: Optional[date] = None
    renewal_required: Optional[bool] = None
    renewal_interval_months: Optional[int] = None
    attachment_url: Optional[str] = None
    verification_status: Optional[str] = None
    verified_by: Optional[str] = None
    verified_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamTechnicianRoutesCreate(BaseModel):
    result_id: int
    routing_problem_id: int
    route_id: int
    technician_id: Optional[int] = None
    technician_name: Optional[str] = None
    vehicle_id: Optional[int] = None
    route_sequence: dict
    total_distance: Optional[float] = None
    total_duration: Optional[float] = None
    total_travel_time: Optional[float] = None
    total_work_time: Optional[float] = None
    num_work_orders: Optional[int] = None
    technician_skills: Optional[dict] = None
    tools_carried: Optional[dict] = None
    parts_available: Optional[dict] = None
    shift_start: Optional[datetime] = None
    shift_end: Optional[datetime] = None
    route_map_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class EamTechnicianRoutesUpdate(BaseModel):
    result_id: Optional[int] = None
    routing_problem_id: Optional[int] = None
    route_id: Optional[int] = None
    technician_id: Optional[int] = None
    technician_name: Optional[str] = None
    vehicle_id: Optional[int] = None
    route_sequence: Optional[dict] = None
    total_distance: Optional[float] = None
    total_duration: Optional[float] = None
    total_travel_time: Optional[float] = None
    total_work_time: Optional[float] = None
    num_work_orders: Optional[int] = None
    technician_skills: Optional[dict] = None
    tools_carried: Optional[dict] = None
    parts_available: Optional[dict] = None
    shift_start: Optional[datetime] = None
    shift_end: Optional[datetime] = None
    route_map_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None

class EamTechnicianRoutesOut(BaseModel):
    result_id: int
    routing_problem_id: int
    route_id: int
    technician_id: Optional[int] = None
    technician_name: Optional[str] = None
    vehicle_id: Optional[int] = None
    route_sequence: dict
    total_distance: Optional[float] = None
    total_duration: Optional[float] = None
    total_travel_time: Optional[float] = None
    total_work_time: Optional[float] = None
    num_work_orders: Optional[int] = None
    technician_skills: Optional[dict] = None
    tools_carried: Optional[dict] = None
    parts_available: Optional[dict] = None
    shift_start: Optional[datetime] = None
    shift_end: Optional[datetime] = None
    route_map_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamTechnicianRoutingProblemsCreate(BaseModel):
    routing_problem_id: int
    problem_id: int
    routing_date: date
    depot_location_id: Optional[int] = None
    depot_latitude: Optional[float] = None
    depot_longitude: Optional[float] = None
    max_work_orders_per_tech: Optional[int] = None
    max_travel_time_min: Optional[int] = None
    objective_weight_travel: Optional[float] = None
    objective_weight_priority: Optional[float] = None
    objective_weight_balance: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamTechnicianRoutingProblemsUpdate(BaseModel):
    routing_problem_id: Optional[int] = None
    problem_id: Optional[int] = None
    routing_date: Optional[date] = None
    depot_location_id: Optional[int] = None
    depot_latitude: Optional[float] = None
    depot_longitude: Optional[float] = None
    max_work_orders_per_tech: Optional[int] = None
    max_travel_time_min: Optional[int] = None
    objective_weight_travel: Optional[float] = None
    objective_weight_priority: Optional[float] = None
    objective_weight_balance: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None

class EamTechnicianRoutingProblemsOut(BaseModel):
    routing_problem_id: int
    problem_id: int
    routing_date: date
    depot_location_id: Optional[int] = None
    depot_latitude: Optional[float] = None
    depot_longitude: Optional[float] = None
    max_work_orders_per_tech: Optional[int] = None
    max_travel_time_min: Optional[int] = None
    objective_weight_travel: Optional[float] = None
    objective_weight_priority: Optional[float] = None
    objective_weight_balance: Optional[float] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamTechnicianSkillsCreate(BaseModel):
    skill_id: int
    technician_id: int
    skill_code: str
    skill_name: str
    skill_level: int
    years_experience: Optional[int] = None
    certification_name: Optional[str] = None
    certification_number: Optional[str] = None
    certification_date: Optional[date] = None
    certification_expiry: Optional[date] = None
    certified_by: Optional[str] = None
    is_mandatory: Optional[bool] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None

class EamTechnicianSkillsUpdate(BaseModel):
    skill_id: Optional[int] = None
    technician_id: Optional[int] = None
    skill_code: Optional[str] = None
    skill_name: Optional[str] = None
    skill_level: Optional[int] = None
    years_experience: Optional[int] = None
    certification_name: Optional[str] = None
    certification_number: Optional[str] = None
    certification_date: Optional[date] = None
    certification_expiry: Optional[date] = None
    certified_by: Optional[str] = None
    is_mandatory: Optional[bool] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None

class EamTechnicianSkillsOut(BaseModel):
    skill_id: int
    technician_id: int
    skill_code: str
    skill_name: str
    skill_level: int
    years_experience: Optional[int] = None
    certification_name: Optional[str] = None
    certification_number: Optional[str] = None
    certification_date: Optional[date] = None
    certification_expiry: Optional[date] = None
    certified_by: Optional[str] = None
    is_mandatory: Optional[bool] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamTechniciansCreate(BaseModel):
    technician_id: int
    technician_code: str
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    primary_craft_code: Optional[str] = None
    location_id: Optional[int] = None
    location_description: Optional[str] = None
    supervisor_id: Optional[int] = None
    hire_date: Optional[date] = None
    hourly_rate: Optional[float] = None
    overtime_rate: Optional[float] = None
    is_contractor: Optional[bool] = None
    contractor_company: Optional[str] = None
    employee_id: Optional[str] = None
    shift_preference: Optional[str] = None
    max_travel_distance_km: Optional[float] = None
    technician_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamTechniciansUpdate(BaseModel):
    technician_id: Optional[int] = None
    technician_code: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    primary_craft_code: Optional[str] = None
    location_id: Optional[int] = None
    location_description: Optional[str] = None
    supervisor_id: Optional[int] = None
    hire_date: Optional[date] = None
    hourly_rate: Optional[float] = None
    overtime_rate: Optional[float] = None
    is_contractor: Optional[bool] = None
    contractor_company: Optional[str] = None
    employee_id: Optional[str] = None
    shift_preference: Optional[str] = None
    max_travel_distance_km: Optional[float] = None
    technician_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamTechniciansOut(BaseModel):
    technician_id: int
    technician_code: str
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    primary_craft_code: Optional[str] = None
    location_id: Optional[int] = None
    location_description: Optional[str] = None
    supervisor_id: Optional[int] = None
    hire_date: Optional[date] = None
    hourly_rate: Optional[float] = None
    overtime_rate: Optional[float] = None
    is_contractor: Optional[bool] = None
    contractor_company: Optional[str] = None
    employee_id: Optional[str] = None
    shift_preference: Optional[str] = None
    max_travel_distance_km: Optional[float] = None
    technician_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamToolsCreate(BaseModel):
    tool_id: int
    tool_code: str
    tool_name: str
    description: Optional[str] = None
    tool_type_code: str
    manufacturer_id: Optional[int] = None
    model_number: Optional[str] = None
    serial_number: Optional[str] = None
    specifications: Optional[str] = None
    location_id: Optional[int] = None
    location_description: Optional[str] = None
    tool_status_code: Optional[str] = None
    calibration_required: Optional[bool] = None
    calibration_frequency_days: Optional[int] = None
    last_calibration_date: Optional[date] = None
    next_calibration_date: Optional[date] = None
    calibration_standard: Optional[str] = None
    tool_cost: Optional[float] = None
    replacement_cost: Optional[float] = None
    rfid_tag: Optional[str] = None
    barcode: Optional[str] = None
    tool_image_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamToolsUpdate(BaseModel):
    tool_id: Optional[int] = None
    tool_code: Optional[str] = None
    tool_name: Optional[str] = None
    description: Optional[str] = None
    tool_type_code: Optional[str] = None
    manufacturer_id: Optional[int] = None
    model_number: Optional[str] = None
    serial_number: Optional[str] = None
    specifications: Optional[str] = None
    location_id: Optional[int] = None
    location_description: Optional[str] = None
    tool_status_code: Optional[str] = None
    calibration_required: Optional[bool] = None
    calibration_frequency_days: Optional[int] = None
    last_calibration_date: Optional[date] = None
    next_calibration_date: Optional[date] = None
    calibration_standard: Optional[str] = None
    tool_cost: Optional[float] = None
    replacement_cost: Optional[float] = None
    rfid_tag: Optional[str] = None
    barcode: Optional[str] = None
    tool_image_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamToolsOut(BaseModel):
    tool_id: int
    tool_code: str
    tool_name: str
    description: Optional[str] = None
    tool_type_code: str
    manufacturer_id: Optional[int] = None
    model_number: Optional[str] = None
    serial_number: Optional[str] = None
    specifications: Optional[str] = None
    location_id: Optional[int] = None
    location_description: Optional[str] = None
    tool_status_code: Optional[str] = None
    calibration_required: Optional[bool] = None
    calibration_frequency_days: Optional[int] = None
    last_calibration_date: Optional[date] = None
    next_calibration_date: Optional[date] = None
    calibration_standard: Optional[str] = None
    tool_cost: Optional[float] = None
    replacement_cost: Optional[float] = None
    rfid_tag: Optional[str] = None
    barcode: Optional[str] = None
    tool_image_url: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamVectorDocumentsCreate(BaseModel):
    vector_doc_id: int
    document_id: Optional[int] = None
    chunk_id: str
    chunk_text: str
    chunk_sequence: Optional[int] = None
    embedding: Optional[str] = None
    meta_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None

class EamVectorDocumentsUpdate(BaseModel):
    vector_doc_id: Optional[int] = None
    document_id: Optional[int] = None
    chunk_id: Optional[str] = None
    chunk_text: Optional[str] = None
    chunk_sequence: Optional[int] = None
    embedding: Optional[str] = None
    meta_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None

class EamVectorDocumentsOut(BaseModel):
    vector_doc_id: int
    document_id: Optional[int] = None
    chunk_id: str
    chunk_text: str
    chunk_sequence: Optional[int] = None
    embedding: Optional[str] = None
    meta_data: Optional[dict] = None
    creation_date: Optional[datetime] = None
    tenant_id: Optional[str] = None
    model_config = {"from_attributes": True}

class EamWarrantiesCreate(BaseModel):
    warranty_id: int
    warranty_number: str
    warranty_name: str
    description: Optional[str] = None
    asset_id: int
    warranty_provider: str
    warranty_type_code: str
    start_date: date
    end_date: date
    warranty_terms: Optional[str] = None
    coverage_details: Optional[str] = None
    exclusions: Optional[str] = None
    claim_contact: Optional[str] = None
    claim_phone: Optional[str] = None
    claim_email: Optional[str] = None
    warranty_document_url: Optional[str] = None
    warranty_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamWarrantiesUpdate(BaseModel):
    warranty_id: Optional[int] = None
    warranty_number: Optional[str] = None
    warranty_name: Optional[str] = None
    description: Optional[str] = None
    asset_id: Optional[int] = None
    warranty_provider: Optional[str] = None
    warranty_type_code: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    warranty_terms: Optional[str] = None
    coverage_details: Optional[str] = None
    exclusions: Optional[str] = None
    claim_contact: Optional[str] = None
    claim_phone: Optional[str] = None
    claim_email: Optional[str] = None
    warranty_document_url: Optional[str] = None
    warranty_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamWarrantiesOut(BaseModel):
    warranty_id: int
    warranty_number: str
    warranty_name: str
    description: Optional[str] = None
    asset_id: int
    warranty_provider: str
    warranty_type_code: str
    start_date: date
    end_date: date
    warranty_terms: Optional[str] = None
    coverage_details: Optional[str] = None
    exclusions: Optional[str] = None
    claim_contact: Optional[str] = None
    claim_phone: Optional[str] = None
    claim_email: Optional[str] = None
    warranty_document_url: Optional[str] = None
    warranty_status_code: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamWarrantyClaimsCreate(BaseModel):
    claim_id: int
    warranty_id: int
    work_order_id: Optional[int] = None
    claim_number: str
    claim_date: date
    description: Optional[str] = None
    claim_amount: Optional[float] = None
    currency_code: Optional[str] = None
    approved_amount: Optional[float] = None
    claim_status_code: Optional[str] = None
    submitted_by: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[date] = None
    rejection_reason: Optional[str] = None
    payment_date: Optional[date] = None
    payment_reference: Optional[str] = None
    claim_attachments: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamWarrantyClaimsUpdate(BaseModel):
    claim_id: Optional[int] = None
    warranty_id: Optional[int] = None
    work_order_id: Optional[int] = None
    claim_number: Optional[str] = None
    claim_date: Optional[date] = None
    description: Optional[str] = None
    claim_amount: Optional[float] = None
    currency_code: Optional[str] = None
    approved_amount: Optional[float] = None
    claim_status_code: Optional[str] = None
    submitted_by: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[date] = None
    rejection_reason: Optional[str] = None
    payment_date: Optional[date] = None
    payment_reference: Optional[str] = None
    claim_attachments: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamWarrantyClaimsOut(BaseModel):
    claim_id: int
    warranty_id: int
    work_order_id: Optional[int] = None
    claim_number: str
    claim_date: date
    description: Optional[str] = None
    claim_amount: Optional[float] = None
    currency_code: Optional[str] = None
    approved_amount: Optional[float] = None
    claim_status_code: Optional[str] = None
    submitted_by: Optional[str] = None
    approved_by: Optional[str] = None
    approval_date: Optional[date] = None
    rejection_reason: Optional[str] = None
    payment_date: Optional[date] = None
    payment_reference: Optional[str] = None
    claim_attachments: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamWoLaborCreate(BaseModel):
    wo_labor_id: int
    work_order_id: int
    wo_task_id: Optional[int] = None
    technician_id: Optional[int] = None
    craft_code: Optional[str] = None
    hours_estimated: Optional[float] = None
    hours_actual: Optional[float] = None
    hours_overtime: Optional[float] = None
    hours_travel: Optional[float] = None
    hours_wait: Optional[float] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    labor_rate: Optional[float] = None
    overtime_rate: Optional[float] = None
    total_cost: Optional[float] = None
    is_contractor: Optional[bool] = None
    notes: Optional[str] = None
    electronic_signature: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamWoLaborUpdate(BaseModel):
    wo_labor_id: Optional[int] = None
    work_order_id: Optional[int] = None
    wo_task_id: Optional[int] = None
    technician_id: Optional[int] = None
    craft_code: Optional[str] = None
    hours_estimated: Optional[float] = None
    hours_actual: Optional[float] = None
    hours_overtime: Optional[float] = None
    hours_travel: Optional[float] = None
    hours_wait: Optional[float] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    labor_rate: Optional[float] = None
    overtime_rate: Optional[float] = None
    total_cost: Optional[float] = None
    is_contractor: Optional[bool] = None
    notes: Optional[str] = None
    electronic_signature: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamWoLaborOut(BaseModel):
    wo_labor_id: int
    work_order_id: int
    wo_task_id: Optional[int] = None
    technician_id: Optional[int] = None
    craft_code: Optional[str] = None
    hours_estimated: Optional[float] = None
    hours_actual: Optional[float] = None
    hours_overtime: Optional[float] = None
    hours_travel: Optional[float] = None
    hours_wait: Optional[float] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    labor_rate: Optional[float] = None
    overtime_rate: Optional[float] = None
    total_cost: Optional[float] = None
    is_contractor: Optional[bool] = None
    notes: Optional[str] = None
    electronic_signature: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamWoOperationsCreate(BaseModel):
    wo_operation_id: int
    work_order_id: int
    operation_sequence: int
    operation_code: Optional[str] = None
    operation_name: str
    description: Optional[str] = None
    work_center_id: Optional[int] = None
    equipment_id: Optional[int] = None
    estimated_hours: Optional[float] = None
    actual_hours: Optional[float] = None
    operation_status_code: Optional[str] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    completion_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamWoOperationsUpdate(BaseModel):
    wo_operation_id: Optional[int] = None
    work_order_id: Optional[int] = None
    operation_sequence: Optional[int] = None
    operation_code: Optional[str] = None
    operation_name: Optional[str] = None
    description: Optional[str] = None
    work_center_id: Optional[int] = None
    equipment_id: Optional[int] = None
    estimated_hours: Optional[float] = None
    actual_hours: Optional[float] = None
    operation_status_code: Optional[str] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    completion_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamWoOperationsOut(BaseModel):
    wo_operation_id: int
    work_order_id: int
    operation_sequence: int
    operation_code: Optional[str] = None
    operation_name: str
    description: Optional[str] = None
    work_center_id: Optional[int] = None
    equipment_id: Optional[int] = None
    estimated_hours: Optional[float] = None
    actual_hours: Optional[float] = None
    operation_status_code: Optional[str] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    completion_notes: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamWoTasksCreate(BaseModel):
    wo_task_id: int
    work_order_id: int
    task_sequence: int
    task_code: Optional[str] = None
    task_name: str
    description: Optional[str] = None
    instructions: Optional[str] = None
    craft_code: Optional[str] = None
    estimated_hours: Optional[float] = None
    actual_hours: Optional[float] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    is_hold_point: Optional[bool] = None
    requires_quality_check: Optional[bool] = None
    requires_signature: Optional[bool] = None
    task_status_code: Optional[str] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    completion_notes: Optional[str] = None
    created_by_technician: Optional[str] = None
    completed_by_technician: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamWoTasksUpdate(BaseModel):
    wo_task_id: Optional[int] = None
    work_order_id: Optional[int] = None
    task_sequence: Optional[int] = None
    task_code: Optional[str] = None
    task_name: Optional[str] = None
    description: Optional[str] = None
    instructions: Optional[str] = None
    craft_code: Optional[str] = None
    estimated_hours: Optional[float] = None
    actual_hours: Optional[float] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    is_hold_point: Optional[bool] = None
    requires_quality_check: Optional[bool] = None
    requires_signature: Optional[bool] = None
    task_status_code: Optional[str] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    completion_notes: Optional[str] = None
    created_by_technician: Optional[str] = None
    completed_by_technician: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamWoTasksOut(BaseModel):
    wo_task_id: int
    work_order_id: int
    task_sequence: int
    task_code: Optional[str] = None
    task_name: str
    description: Optional[str] = None
    instructions: Optional[str] = None
    craft_code: Optional[str] = None
    estimated_hours: Optional[float] = None
    actual_hours: Optional[float] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    is_hold_point: Optional[bool] = None
    requires_quality_check: Optional[bool] = None
    requires_signature: Optional[bool] = None
    task_status_code: Optional[str] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    completion_notes: Optional[str] = None
    created_by_technician: Optional[str] = None
    completed_by_technician: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamWoToolsCreate(BaseModel):
    wo_tool_id: int
    work_order_id: int
    wo_task_id: Optional[int] = None
    tool_id: int
    quantity_required: Optional[float] = None
    quantity_issued: Optional[float] = None
    quantity_returned: Optional[float] = None
    issued_date: Optional[datetime] = None
    issued_by: Optional[str] = None
    returned_date: Optional[datetime] = None
    returned_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamWoToolsUpdate(BaseModel):
    wo_tool_id: Optional[int] = None
    work_order_id: Optional[int] = None
    wo_task_id: Optional[int] = None
    tool_id: Optional[int] = None
    quantity_required: Optional[float] = None
    quantity_issued: Optional[float] = None
    quantity_returned: Optional[float] = None
    issued_date: Optional[datetime] = None
    issued_by: Optional[str] = None
    returned_date: Optional[datetime] = None
    returned_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None

class EamWoToolsOut(BaseModel):
    wo_tool_id: int
    work_order_id: int
    wo_task_id: Optional[int] = None
    tool_id: int
    quantity_required: Optional[float] = None
    quantity_issued: Optional[float] = None
    quantity_returned: Optional[float] = None
    issued_date: Optional[datetime] = None
    issued_by: Optional[str] = None
    returned_date: Optional[datetime] = None
    returned_by: Optional[str] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    model_config = {"from_attributes": True}

class EamWorkOrderStatusesCreate(BaseModel):
    work_order_status_code: str
    work_order_status_name: str
    description: Optional[str] = None
    is_open: Optional[bool] = None
    is_closed: Optional[bool] = None
    is_cancelled: Optional[bool] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: bool = True

class EamWorkOrderStatusesUpdate(BaseModel):
    work_order_status_code: Optional[str] = None
    work_order_status_name: Optional[str] = None
    description: Optional[str] = None
    is_open: Optional[bool] = None
    is_closed: Optional[bool] = None
    is_cancelled: Optional[bool] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: Optional[bool] = None

class EamWorkOrderStatusesOut(BaseModel):
    work_order_status_code: str
    work_order_status_name: str
    description: Optional[str] = None
    is_open: Optional[bool] = None
    is_closed: Optional[bool] = None
    is_cancelled: Optional[bool] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: bool
    model_config = {"from_attributes": True}

class EamWorkOrderTypesCreate(BaseModel):
    work_order_type_code: str
    work_order_type_name: str
    description: Optional[str] = None
    is_corrective: Optional[bool] = None
    is_preventive: Optional[bool] = None
    is_predictive: Optional[bool] = None
    is_emergency: Optional[bool] = None
    is_inspection: Optional[bool] = None
    is_calibration: Optional[bool] = None
    is_safety: Optional[bool] = None
    is_modification: Optional[bool] = None
    is_project: Optional[bool] = None
    is_breakdown: Optional[bool] = None
    requires_approval: Optional[bool] = None
    requires_planning: Optional[bool] = None
    requires_scheduling: Optional[bool] = None
    requires_permit: Optional[bool] = None
    requires_loto: Optional[bool] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: bool = True

class EamWorkOrderTypesUpdate(BaseModel):
    work_order_type_code: Optional[str] = None
    work_order_type_name: Optional[str] = None
    description: Optional[str] = None
    is_corrective: Optional[bool] = None
    is_preventive: Optional[bool] = None
    is_predictive: Optional[bool] = None
    is_emergency: Optional[bool] = None
    is_inspection: Optional[bool] = None
    is_calibration: Optional[bool] = None
    is_safety: Optional[bool] = None
    is_modification: Optional[bool] = None
    is_project: Optional[bool] = None
    is_breakdown: Optional[bool] = None
    requires_approval: Optional[bool] = None
    requires_planning: Optional[bool] = None
    requires_scheduling: Optional[bool] = None
    requires_permit: Optional[bool] = None
    requires_loto: Optional[bool] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: Optional[bool] = None

class EamWorkOrderTypesOut(BaseModel):
    work_order_type_code: str
    work_order_type_name: str
    description: Optional[str] = None
    is_corrective: Optional[bool] = None
    is_preventive: Optional[bool] = None
    is_predictive: Optional[bool] = None
    is_emergency: Optional[bool] = None
    is_inspection: Optional[bool] = None
    is_calibration: Optional[bool] = None
    is_safety: Optional[bool] = None
    is_modification: Optional[bool] = None
    is_project: Optional[bool] = None
    is_breakdown: Optional[bool] = None
    requires_approval: Optional[bool] = None
    requires_planning: Optional[bool] = None
    requires_scheduling: Optional[bool] = None
    requires_permit: Optional[bool] = None
    requires_loto: Optional[bool] = None
    sort_order: Optional[int] = None
    creation_date: Optional[datetime] = None
    is_active: bool
    model_config = {"from_attributes": True}

class EamWorkOrdersCreate(BaseModel):
    work_order_id: int
    work_order_number: str
    work_order_type_code: str
    work_order_status_code: str
    priority_code: str
    title: str
    description: Optional[str] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    failure_code_id: Optional[int] = None
    failure_cause_code_id: Optional[int] = None
    failure_action_code_id: Optional[int] = None
    requested_by: Optional[str] = None
    requested_date: Optional[datetime] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    planned_by: Optional[str] = None
    planned_date: Optional[datetime] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    due_date: Optional[datetime] = None
    estimated_hours: Optional[float] = None
    actual_hours: Optional[float] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    labor_cost: Optional[float] = None
    parts_cost: Optional[float] = None
    service_cost: Optional[float] = None
    tool_cost: Optional[float] = None
    downtime_required: Optional[bool] = None
    downtime_hours: Optional[float] = None
    downtime_cost: Optional[float] = None
    production_impact: Optional[str] = None
    requires_permit: Optional[bool] = None
    requires_loto: Optional[bool] = None
    permit_id: Optional[int] = None
    loto_id: Optional[int] = None
    pm_schedule_id: Optional[int] = None
    pm_template_id: Optional[int] = None
    inspection_id: Optional[int] = None
    related_work_order_id: Optional[int] = None
    is_recurring: Optional[bool] = None
    recurring_frequency_days: Optional[int] = None
    completion_notes: Optional[str] = None
    completion_report: Optional[str] = None
    quality_check_passed: Optional[bool] = None
    verified_by: Optional[str] = None
    verified_date: Optional[datetime] = None
    closed_by: Optional[str] = None
    closed_date: Optional[datetime] = None
    source_system_code: Optional[str] = None
    source_transaction_id: Optional[str] = None
    ai_generated: Optional[bool] = None
    ai_confidence_score: Optional[float] = None
    ai_recommendation: Optional[str] = None
    custom_attributes: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int = 1
    is_active: bool = True
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamWorkOrdersUpdate(BaseModel):
    work_order_id: Optional[int] = None
    work_order_number: Optional[str] = None
    work_order_type_code: Optional[str] = None
    work_order_status_code: Optional[str] = None
    priority_code: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    failure_code_id: Optional[int] = None
    failure_cause_code_id: Optional[int] = None
    failure_action_code_id: Optional[int] = None
    requested_by: Optional[str] = None
    requested_date: Optional[datetime] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    planned_by: Optional[str] = None
    planned_date: Optional[datetime] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    due_date: Optional[datetime] = None
    estimated_hours: Optional[float] = None
    actual_hours: Optional[float] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    labor_cost: Optional[float] = None
    parts_cost: Optional[float] = None
    service_cost: Optional[float] = None
    tool_cost: Optional[float] = None
    downtime_required: Optional[bool] = None
    downtime_hours: Optional[float] = None
    downtime_cost: Optional[float] = None
    production_impact: Optional[str] = None
    requires_permit: Optional[bool] = None
    requires_loto: Optional[bool] = None
    permit_id: Optional[int] = None
    loto_id: Optional[int] = None
    pm_schedule_id: Optional[int] = None
    pm_template_id: Optional[int] = None
    inspection_id: Optional[int] = None
    related_work_order_id: Optional[int] = None
    is_recurring: Optional[bool] = None
    recurring_frequency_days: Optional[int] = None
    completion_notes: Optional[str] = None
    completion_report: Optional[str] = None
    quality_check_passed: Optional[bool] = None
    verified_by: Optional[str] = None
    verified_date: Optional[datetime] = None
    closed_by: Optional[str] = None
    closed_date: Optional[datetime] = None
    source_system_code: Optional[str] = None
    source_transaction_id: Optional[str] = None
    ai_generated: Optional[bool] = None
    ai_confidence_score: Optional[float] = None
    ai_recommendation: Optional[str] = None
    custom_attributes: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None

class EamWorkOrdersOut(BaseModel):
    work_order_id: int
    work_order_number: str
    work_order_type_code: str
    work_order_status_code: str
    priority_code: str
    title: str
    description: Optional[str] = None
    asset_id: Optional[int] = None
    component_id: Optional[int] = None
    functional_location_id: Optional[int] = None
    failure_code_id: Optional[int] = None
    failure_cause_code_id: Optional[int] = None
    failure_action_code_id: Optional[int] = None
    requested_by: Optional[str] = None
    requested_date: Optional[datetime] = None
    approved_by: Optional[str] = None
    approved_date: Optional[datetime] = None
    planned_by: Optional[str] = None
    planned_date: Optional[datetime] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    due_date: Optional[datetime] = None
    estimated_hours: Optional[float] = None
    actual_hours: Optional[float] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    labor_cost: Optional[float] = None
    parts_cost: Optional[float] = None
    service_cost: Optional[float] = None
    tool_cost: Optional[float] = None
    downtime_required: Optional[bool] = None
    downtime_hours: Optional[float] = None
    downtime_cost: Optional[float] = None
    production_impact: Optional[str] = None
    requires_permit: Optional[bool] = None
    requires_loto: Optional[bool] = None
    permit_id: Optional[int] = None
    loto_id: Optional[int] = None
    pm_schedule_id: Optional[int] = None
    pm_template_id: Optional[int] = None
    inspection_id: Optional[int] = None
    related_work_order_id: Optional[int] = None
    is_recurring: Optional[bool] = None
    recurring_frequency_days: Optional[int] = None
    completion_notes: Optional[str] = None
    completion_report: Optional[str] = None
    quality_check_passed: Optional[bool] = None
    verified_by: Optional[str] = None
    verified_date: Optional[datetime] = None
    closed_by: Optional[str] = None
    closed_date: Optional[datetime] = None
    source_system_code: Optional[str] = None
    source_transaction_id: Optional[str] = None
    ai_generated: Optional[bool] = None
    ai_confidence_score: Optional[float] = None
    ai_recommendation: Optional[str] = None
    custom_attributes: Optional[dict] = None
    creation_date: Optional[datetime] = None
    created_by: Optional[str] = None
    last_update_date: Optional[datetime] = None
    last_updated_by: Optional[str] = None
    object_version_number: int
    is_active: bool
    tenant_id: Optional[str] = None
    organization_id: Optional[int] = None
    site_id: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}
