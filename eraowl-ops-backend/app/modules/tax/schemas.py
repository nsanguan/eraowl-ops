import uuid
from datetime import date, datetime, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class PartnerTaxProfilesCreate(BaseModel):
    partner_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    tax_registration_number: Optional[str] = None
    tax_entity_type: Optional[str] = None
    is_tax_exempt: Optional[bool] = None
    tax_exempt_certificate: Optional[str] = None
    tax_exempt_reason: Optional[str] = None
    tax_authority: Optional[str] = None
    withholding_tax_rate_pct: Optional[float] = None
    default_wht_code: Optional[str] = None
    is_active: bool = True

class PartnerTaxProfilesUpdate(BaseModel):
    partner_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_registration_number: Optional[str] = None
    tax_entity_type: Optional[str] = None
    is_tax_exempt: Optional[bool] = None
    tax_exempt_certificate: Optional[str] = None
    tax_exempt_reason: Optional[str] = None
    tax_authority: Optional[str] = None
    withholding_tax_rate_pct: Optional[float] = None
    default_wht_code: Optional[str] = None
    is_active: Optional[bool] = None

class PartnerTaxProfilesOut(BaseModel):
    partner_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    tax_registration_number: Optional[str] = None
    tax_entity_type: Optional[str] = None
    is_tax_exempt: Optional[bool] = None
    tax_exempt_certificate: Optional[str] = None
    tax_exempt_reason: Optional[str] = None
    tax_authority: Optional[str] = None
    withholding_tax_rate_pct: Optional[float] = None
    default_wht_code: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAccountsCreate(BaseModel):
    tax_account_id: uuid.UUID
    account_code: str
    account_name: str
    account_type: str
    tax_regime_id: Optional[uuid.UUID] = None
    tax_type_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    gl_account_id: Optional[uuid.UUID] = None
    is_default: Optional[bool] = None
    is_active: bool = True

class TaxAccountsUpdate(BaseModel):
    tax_account_id: Optional[uuid.UUID] = None
    account_code: Optional[str] = None
    account_name: Optional[str] = None
    account_type: Optional[str] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_type_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    gl_account_id: Optional[uuid.UUID] = None
    is_default: Optional[bool] = None
    is_active: Optional[bool] = None

class TaxAccountsOut(BaseModel):
    tax_account_id: uuid.UUID
    account_code: str
    account_name: str
    account_type: str
    tax_regime_id: Optional[uuid.UUID] = None
    tax_type_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    gl_account_id: Optional[uuid.UUID] = None
    is_default: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAgentDefinitionsCreate(BaseModel):
    agent_id: uuid.UUID
    agent_name: str
    agent_type: str
    system_prompt: Optional[str] = None
    llm_config_id: Optional[uuid.UUID] = None
    tools: Optional[dict] = None
    memory_config: Optional[dict] = None
    is_active: bool = True

class TaxAgentDefinitionsUpdate(BaseModel):
    agent_id: Optional[uuid.UUID] = None
    agent_name: Optional[str] = None
    agent_type: Optional[str] = None
    system_prompt: Optional[str] = None
    llm_config_id: Optional[uuid.UUID] = None
    tools: Optional[dict] = None
    memory_config: Optional[dict] = None
    is_active: Optional[bool] = None

class TaxAgentDefinitionsOut(BaseModel):
    agent_id: uuid.UUID
    agent_name: str
    agent_type: str
    system_prompt: Optional[str] = None
    llm_config_id: Optional[uuid.UUID] = None
    tools: Optional[dict] = None
    memory_config: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAiAgentLogsCreate(BaseModel):
    log_id: uuid.UUID
    agent_name: str
    execution_id: Optional[uuid.UUID] = None
    input_summary: Optional[str] = None
    output_summary: Optional[str] = None
    llm_calls: Optional[int] = None
    total_tokens: Optional[int] = None
    total_cost_usd: Optional[float] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool = True

class TaxAiAgentLogsUpdate(BaseModel):
    log_id: Optional[uuid.UUID] = None
    agent_name: Optional[str] = None
    execution_id: Optional[uuid.UUID] = None
    input_summary: Optional[str] = None
    output_summary: Optional[str] = None
    llm_calls: Optional[int] = None
    total_tokens: Optional[int] = None
    total_cost_usd: Optional[float] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: Optional[bool] = None

class TaxAiAgentLogsOut(BaseModel):
    log_id: uuid.UUID
    agent_name: str
    execution_id: Optional[uuid.UUID] = None
    input_summary: Optional[str] = None
    output_summary: Optional[str] = None
    llm_calls: Optional[int] = None
    total_tokens: Optional[int] = None
    total_cost_usd: Optional[float] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAiDecisionsCreate(BaseModel):
    decision_id: uuid.UUID
    decision_type: str
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    confidence: Optional[float] = None
    model_used: Optional[str] = None
    human_reviewed: Optional[bool] = None
    human_decision: Optional[dict] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxAiDecisionsUpdate(BaseModel):
    decision_id: Optional[uuid.UUID] = None
    decision_type: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    confidence: Optional[float] = None
    model_used: Optional[str] = None
    human_reviewed: Optional[bool] = None
    human_decision: Optional[dict] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxAiDecisionsOut(BaseModel):
    decision_id: uuid.UUID
    decision_type: str
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    confidence: Optional[float] = None
    model_used: Optional[str] = None
    human_reviewed: Optional[bool] = None
    human_decision: Optional[dict] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAiModelRegistryCreate(BaseModel):
    registry_id: uuid.UUID
    model_name: str
    model_type: str
    framework: Optional[str] = None
    version: str
    model_artifact_url: Optional[str] = None
    metrics: Optional[dict] = None
    deployment_status: Optional[str] = None
    deployed_at: Optional[datetime] = None
    is_active: bool = True

class TaxAiModelRegistryUpdate(BaseModel):
    registry_id: Optional[uuid.UUID] = None
    model_name: Optional[str] = None
    model_type: Optional[str] = None
    framework: Optional[str] = None
    version: Optional[str] = None
    model_artifact_url: Optional[str] = None
    metrics: Optional[dict] = None
    deployment_status: Optional[str] = None
    deployed_at: Optional[datetime] = None
    is_active: Optional[bool] = None

class TaxAiModelRegistryOut(BaseModel):
    registry_id: uuid.UUID
    model_name: str
    model_type: str
    framework: Optional[str] = None
    version: str
    model_artifact_url: Optional[str] = None
    metrics: Optional[dict] = None
    deployment_status: Optional[str] = None
    deployed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAiWorkflowStateCreate(BaseModel):
    state_id: uuid.UUID
    workflow_name: str
    execution_id: Optional[uuid.UUID] = None
    current_node: Optional[str] = None
    state_data: Optional[dict] = None
    checkpoint_data: Optional[dict] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxAiWorkflowStateUpdate(BaseModel):
    state_id: Optional[uuid.UUID] = None
    workflow_name: Optional[str] = None
    execution_id: Optional[uuid.UUID] = None
    current_node: Optional[str] = None
    state_data: Optional[dict] = None
    checkpoint_data: Optional[dict] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxAiWorkflowStateOut(BaseModel):
    state_id: uuid.UUID
    workflow_name: str
    execution_id: Optional[uuid.UUID] = None
    current_node: Optional[str] = None
    state_data: Optional[dict] = None
    checkpoint_data: Optional[dict] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAlgorithmsCreate(BaseModel):
    algorithm_id: uuid.UUID
    algorithm_type: str
    algorithm_name: str
    description: Optional[str] = None
    inputs: Optional[dict] = None
    outputs: Optional[dict] = None
    config: Optional[dict] = None
    version: Optional[str] = None
    is_active: bool = True

class TaxAlgorithmsUpdate(BaseModel):
    algorithm_id: Optional[uuid.UUID] = None
    algorithm_type: Optional[str] = None
    algorithm_name: Optional[str] = None
    description: Optional[str] = None
    inputs: Optional[dict] = None
    outputs: Optional[dict] = None
    config: Optional[dict] = None
    version: Optional[str] = None
    is_active: Optional[bool] = None

class TaxAlgorithmsOut(BaseModel):
    algorithm_id: uuid.UUID
    algorithm_type: str
    algorithm_name: str
    description: Optional[str] = None
    inputs: Optional[dict] = None
    outputs: Optional[dict] = None
    config: Optional[dict] = None
    version: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxArchiveContainersCreate(BaseModel):
    container_id: uuid.UUID
    container_type: str
    container_code: str
    length_cm: float
    width_cm: float
    height_cm: float
    weight_capacity_kg: Optional[float] = None
    location: Optional[str] = None
    is_active: bool = True

class TaxArchiveContainersUpdate(BaseModel):
    container_id: Optional[uuid.UUID] = None
    container_type: Optional[str] = None
    container_code: Optional[str] = None
    length_cm: Optional[float] = None
    width_cm: Optional[float] = None
    height_cm: Optional[float] = None
    weight_capacity_kg: Optional[float] = None
    location: Optional[str] = None
    is_active: Optional[bool] = None

class TaxArchiveContainersOut(BaseModel):
    container_id: uuid.UUID
    container_type: str
    container_code: str
    length_cm: float
    width_cm: float
    height_cm: float
    weight_capacity_kg: Optional[float] = None
    location: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAssessmentDisputesCreate(BaseModel):
    dispute_id: uuid.UUID
    assessment_id: uuid.UUID
    dispute_date: date
    dispute_reason: str
    dispute_amount: Optional[float] = None
    supporting_docs: Optional[dict] = None
    status: Optional[str] = None
    resolution_date: Optional[date] = None
    resolved_amount: Optional[float] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxAssessmentDisputesUpdate(BaseModel):
    dispute_id: Optional[uuid.UUID] = None
    assessment_id: Optional[uuid.UUID] = None
    dispute_date: Optional[date] = None
    dispute_reason: Optional[str] = None
    dispute_amount: Optional[float] = None
    supporting_docs: Optional[dict] = None
    status: Optional[str] = None
    resolution_date: Optional[date] = None
    resolved_amount: Optional[float] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxAssessmentDisputesOut(BaseModel):
    dispute_id: uuid.UUID
    assessment_id: uuid.UUID
    dispute_date: date
    dispute_reason: str
    dispute_amount: Optional[float] = None
    supporting_docs: Optional[dict] = None
    status: Optional[str] = None
    resolution_date: Optional[date] = None
    resolved_amount: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAssessmentsCreate(BaseModel):
    assessment_id: uuid.UUID
    assessment_type: str
    tax_authority_id: Optional[uuid.UUID] = None
    audit_id: Optional[uuid.UUID] = None
    assessment_number: str
    assessment_date: date
    due_date: date
    total_amount: float
    tax_amount: Optional[float] = None
    penalty_amount: Optional[float] = None
    interest_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxAssessmentsUpdate(BaseModel):
    assessment_id: Optional[uuid.UUID] = None
    assessment_type: Optional[str] = None
    tax_authority_id: Optional[uuid.UUID] = None
    audit_id: Optional[uuid.UUID] = None
    assessment_number: Optional[str] = None
    assessment_date: Optional[date] = None
    due_date: Optional[date] = None
    total_amount: Optional[float] = None
    tax_amount: Optional[float] = None
    penalty_amount: Optional[float] = None
    interest_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxAssessmentsOut(BaseModel):
    assessment_id: uuid.UUID
    assessment_type: str
    tax_authority_id: Optional[uuid.UUID] = None
    audit_id: Optional[uuid.UUID] = None
    assessment_number: str
    assessment_date: date
    due_date: date
    total_amount: float
    tax_amount: Optional[float] = None
    penalty_amount: Optional[float] = None
    interest_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAuditFindingsCreate(BaseModel):
    finding_id: uuid.UUID
    audit_id: uuid.UUID
    finding_number: str
    description: str
    tax_amount_impact: Optional[float] = None
    penalty_amount: Optional[float] = None
    risk_rating: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxAuditFindingsUpdate(BaseModel):
    finding_id: Optional[uuid.UUID] = None
    audit_id: Optional[uuid.UUID] = None
    finding_number: Optional[str] = None
    description: Optional[str] = None
    tax_amount_impact: Optional[float] = None
    penalty_amount: Optional[float] = None
    risk_rating: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxAuditFindingsOut(BaseModel):
    finding_id: uuid.UUID
    audit_id: uuid.UUID
    finding_number: str
    description: str
    tax_amount_impact: Optional[float] = None
    penalty_amount: Optional[float] = None
    risk_rating: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAuditResponsesCreate(BaseModel):
    response_id: uuid.UUID
    audit_id: uuid.UUID
    response_type: Optional[str] = None
    response_date: date
    response_content: Optional[str] = None
    attachments: Optional[dict] = None
    submitted_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxAuditResponsesUpdate(BaseModel):
    response_id: Optional[uuid.UUID] = None
    audit_id: Optional[uuid.UUID] = None
    response_type: Optional[str] = None
    response_date: Optional[date] = None
    response_content: Optional[str] = None
    attachments: Optional[dict] = None
    submitted_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxAuditResponsesOut(BaseModel):
    response_id: uuid.UUID
    audit_id: uuid.UUID
    response_type: Optional[str] = None
    response_date: date
    response_content: Optional[str] = None
    attachments: Optional[dict] = None
    submitted_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAuditRouteLocationsCreate(BaseModel):
    location_id: uuid.UUID
    location_name: str
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    audit_duration_hours: Optional[float] = None
    priority: Optional[int] = None
    is_active: bool = True

class TaxAuditRouteLocationsUpdate(BaseModel):
    location_id: Optional[uuid.UUID] = None
    location_name: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    audit_duration_hours: Optional[float] = None
    priority: Optional[int] = None
    is_active: Optional[bool] = None

class TaxAuditRouteLocationsOut(BaseModel):
    location_id: uuid.UUID
    location_name: str
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    audit_duration_hours: Optional[float] = None
    priority: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAuditRoutesCreate(BaseModel):
    route_id: uuid.UUID
    problem_id: Optional[uuid.UUID] = None
    route_name: str
    auditor_name: Optional[str] = None
    total_distance_km: Optional[float] = None
    total_duration_hours: Optional[float] = None
    total_travel_hours: Optional[float] = None
    total_audit_hours: Optional[float] = None
    site_count: Optional[int] = None
    route_sequence: dict
    high_risk_first: Optional[bool] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxAuditRoutesUpdate(BaseModel):
    route_id: Optional[uuid.UUID] = None
    problem_id: Optional[uuid.UUID] = None
    route_name: Optional[str] = None
    auditor_name: Optional[str] = None
    total_distance_km: Optional[float] = None
    total_duration_hours: Optional[float] = None
    total_travel_hours: Optional[float] = None
    total_audit_hours: Optional[float] = None
    site_count: Optional[int] = None
    route_sequence: Optional[dict] = None
    high_risk_first: Optional[bool] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxAuditRoutesOut(BaseModel):
    route_id: uuid.UUID
    problem_id: Optional[uuid.UUID] = None
    route_name: str
    auditor_name: Optional[str] = None
    total_distance_km: Optional[float] = None
    total_duration_hours: Optional[float] = None
    total_travel_hours: Optional[float] = None
    total_audit_hours: Optional[float] = None
    site_count: Optional[int] = None
    route_sequence: dict
    high_risk_first: Optional[bool] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAuditsCreate(BaseModel):
    audit_id: uuid.UUID
    audit_type: str
    tax_authority_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    audit_reference: str
    audit_scope: Optional[str] = None
    audit_period_from: Optional[date] = None
    audit_period_to: Optional[date] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[str] = None
    findings_summary: Optional[str] = None
    assessment_amount: Optional[float] = None
    penalty_amount: Optional[float] = None
    interest_amount: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxAuditsUpdate(BaseModel):
    audit_id: Optional[uuid.UUID] = None
    audit_type: Optional[str] = None
    tax_authority_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    audit_reference: Optional[str] = None
    audit_scope: Optional[str] = None
    audit_period_from: Optional[date] = None
    audit_period_to: Optional[date] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[str] = None
    findings_summary: Optional[str] = None
    assessment_amount: Optional[float] = None
    penalty_amount: Optional[float] = None
    interest_amount: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxAuditsOut(BaseModel):
    audit_id: uuid.UUID
    audit_type: str
    tax_authority_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    audit_reference: str
    audit_scope: Optional[str] = None
    audit_period_from: Optional[date] = None
    audit_period_to: Optional[date] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[str] = None
    findings_summary: Optional[str] = None
    assessment_amount: Optional[float] = None
    penalty_amount: Optional[float] = None
    interest_amount: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAuthoritiesCreate(BaseModel):
    tax_authority_id: uuid.UUID
    authority_code: str
    authority_name: str
    country_code: str
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    website_url: Optional[str] = None
    portal_url: Optional[str] = None
    api_endpoint: Optional[str] = None
    auth_method: Optional[str] = None
    filing_requirements: Optional[str] = None
    payment_methods: Optional[dict] = None
    is_active: bool = True

class TaxAuthoritiesUpdate(BaseModel):
    tax_authority_id: Optional[uuid.UUID] = None
    authority_code: Optional[str] = None
    authority_name: Optional[str] = None
    country_code: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    website_url: Optional[str] = None
    portal_url: Optional[str] = None
    api_endpoint: Optional[str] = None
    auth_method: Optional[str] = None
    filing_requirements: Optional[str] = None
    payment_methods: Optional[dict] = None
    is_active: Optional[bool] = None

class TaxAuthoritiesOut(BaseModel):
    tax_authority_id: uuid.UUID
    authority_code: str
    authority_name: str
    country_code: str
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    website_url: Optional[str] = None
    portal_url: Optional[str] = None
    api_endpoint: Optional[str] = None
    auth_method: Optional[str] = None
    filing_requirements: Optional[str] = None
    payment_methods: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxAuthorityContactsCreate(BaseModel):
    contact_id: uuid.UUID
    tax_authority_id: uuid.UUID
    contact_name: str
    contact_role: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    is_active: bool = True

class TaxAuthorityContactsUpdate(BaseModel):
    contact_id: Optional[uuid.UUID] = None
    tax_authority_id: Optional[uuid.UUID] = None
    contact_name: Optional[str] = None
    contact_role: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None

class TaxAuthorityContactsOut(BaseModel):
    contact_id: uuid.UUID
    tax_authority_id: uuid.UUID
    contact_name: str
    contact_role: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxCertificateJurisdictionsCreate(BaseModel):
    mapping_id: uuid.UUID
    certificate_id: uuid.UUID
    tax_jurisdiction_id: uuid.UUID
    is_active: bool = True

class TaxCertificateJurisdictionsUpdate(BaseModel):
    mapping_id: Optional[uuid.UUID] = None
    certificate_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None

class TaxCertificateJurisdictionsOut(BaseModel):
    mapping_id: uuid.UUID
    certificate_id: uuid.UUID
    tax_jurisdiction_id: uuid.UUID
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxCertificatesCreate(BaseModel):
    certificate_id: uuid.UUID
    certificate_type: str
    certificate_number: str
    issuer_id: Optional[uuid.UUID] = None
    partner_id: uuid.UUID
    certificate_name: str
    effective_from: date
    expiration_date: date
    status: Optional[str] = None
    verification_status: Optional[str] = None
    document_url: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True

class TaxCertificatesUpdate(BaseModel):
    certificate_id: Optional[uuid.UUID] = None
    certificate_type: Optional[str] = None
    certificate_number: Optional[str] = None
    issuer_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    certificate_name: Optional[str] = None
    effective_from: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    verification_status: Optional[str] = None
    document_url: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None

class TaxCertificatesOut(BaseModel):
    certificate_id: uuid.UUID
    certificate_type: str
    certificate_number: str
    issuer_id: Optional[uuid.UUID] = None
    partner_id: uuid.UUID
    certificate_name: str
    effective_from: date
    expiration_date: date
    status: Optional[str] = None
    verification_status: Optional[str] = None
    document_url: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxClassificationRulesCreate(BaseModel):
    rule_id: uuid.UUID
    rule_code: str
    classification_type: str
    conditions: dict
    tax_code_id: Optional[uuid.UUID] = None
    priority: Optional[int] = None
    is_active: bool = True

class TaxClassificationRulesUpdate(BaseModel):
    rule_id: Optional[uuid.UUID] = None
    rule_code: Optional[str] = None
    classification_type: Optional[str] = None
    conditions: Optional[dict] = None
    tax_code_id: Optional[uuid.UUID] = None
    priority: Optional[int] = None
    is_active: Optional[bool] = None

class TaxClassificationRulesOut(BaseModel):
    rule_id: uuid.UUID
    rule_code: str
    classification_type: str
    conditions: dict
    tax_code_id: Optional[uuid.UUID] = None
    priority: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxClassificationsCreate(BaseModel):
    classification_id: uuid.UUID
    classification_type: str
    entity_id: uuid.UUID
    tax_code_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    effective_from: date
    effective_to: Optional[date] = None
    is_active: bool = True

class TaxClassificationsUpdate(BaseModel):
    classification_id: Optional[uuid.UUID] = None
    classification_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    tax_code_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: Optional[bool] = None

class TaxClassificationsOut(BaseModel):
    classification_id: uuid.UUID
    classification_type: str
    entity_id: uuid.UUID
    tax_code_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    effective_from: date
    effective_to: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxCodesCreate(BaseModel):
    tax_code_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    tax_type_id: Optional[uuid.UUID] = None
    tax_rate_id: Optional[uuid.UUID] = None
    tax_code: str
    tax_code_name: str
    description: Optional[str] = None
    effective_from: date
    effective_to: Optional[date] = None
    default_account_id: Optional[uuid.UUID] = None
    is_active: bool = True

class TaxCodesUpdate(BaseModel):
    tax_code_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_type_id: Optional[uuid.UUID] = None
    tax_rate_id: Optional[uuid.UUID] = None
    tax_code: Optional[str] = None
    tax_code_name: Optional[str] = None
    description: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    default_account_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None

class TaxCodesOut(BaseModel):
    tax_code_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    tax_type_id: Optional[uuid.UUID] = None
    tax_rate_id: Optional[uuid.UUID] = None
    tax_code: str
    tax_code_name: str
    description: Optional[str] = None
    effective_from: date
    effective_to: Optional[date] = None
    default_account_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxComplianceCalendarsCreate(BaseModel):
    calendar_id: uuid.UUID
    obligation_id: uuid.UUID
    due_date: date
    period_name: Optional[str] = None
    status: Optional[str] = None
    submitted_date: Optional[date] = None
    reminder_sent_at: Optional[datetime] = None
    is_active: bool = True

class TaxComplianceCalendarsUpdate(BaseModel):
    calendar_id: Optional[uuid.UUID] = None
    obligation_id: Optional[uuid.UUID] = None
    due_date: Optional[date] = None
    period_name: Optional[str] = None
    status: Optional[str] = None
    submitted_date: Optional[date] = None
    reminder_sent_at: Optional[datetime] = None
    is_active: Optional[bool] = None

class TaxComplianceCalendarsOut(BaseModel):
    calendar_id: uuid.UUID
    obligation_id: uuid.UUID
    due_date: date
    period_name: Optional[str] = None
    status: Optional[str] = None
    submitted_date: Optional[date] = None
    reminder_sent_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxComplianceObligationsCreate(BaseModel):
    obligation_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    obligation_code: str
    obligation_name: str
    frequency: str
    due_day_of_period: Optional[int] = None
    is_active: bool = True

class TaxComplianceObligationsUpdate(BaseModel):
    obligation_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    obligation_code: Optional[str] = None
    obligation_name: Optional[str] = None
    frequency: Optional[str] = None
    due_day_of_period: Optional[int] = None
    is_active: Optional[bool] = None

class TaxComplianceObligationsOut(BaseModel):
    obligation_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    obligation_code: str
    obligation_name: str
    frequency: str
    due_day_of_period: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxCreditsCreate(BaseModel):
    credit_id: uuid.UUID
    credit_type: str
    source_transaction_id: Optional[uuid.UUID] = None
    tax_type_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    credit_amount: float
    utilized_amount: Optional[float] = None
    remaining_amount: Optional[float] = None
    currency_code: Optional[str] = None
    origin_period: Optional[str] = None
    expiry_period: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxCreditsUpdate(BaseModel):
    credit_id: Optional[uuid.UUID] = None
    credit_type: Optional[str] = None
    source_transaction_id: Optional[uuid.UUID] = None
    tax_type_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    credit_amount: Optional[float] = None
    utilized_amount: Optional[float] = None
    remaining_amount: Optional[float] = None
    currency_code: Optional[str] = None
    origin_period: Optional[str] = None
    expiry_period: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxCreditsOut(BaseModel):
    credit_id: uuid.UUID
    credit_type: str
    source_transaction_id: Optional[uuid.UUID] = None
    tax_type_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    credit_amount: float
    utilized_amount: Optional[float] = None
    remaining_amount: Optional[float] = None
    currency_code: Optional[str] = None
    origin_period: Optional[str] = None
    expiry_period: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxCustomsBondsCreate(BaseModel):
    bond_id: uuid.UUID
    bond_number: str
    bond_type: str
    surety_company: Optional[str] = None
    bond_amount: float
    effective_from: date
    expiration_date: date
    status: Optional[str] = None
    is_active: bool = True

class TaxCustomsBondsUpdate(BaseModel):
    bond_id: Optional[uuid.UUID] = None
    bond_number: Optional[str] = None
    bond_type: Optional[str] = None
    surety_company: Optional[str] = None
    bond_amount: Optional[float] = None
    effective_from: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxCustomsBondsOut(BaseModel):
    bond_id: uuid.UUID
    bond_number: str
    bond_type: str
    surety_company: Optional[str] = None
    bond_amount: float
    effective_from: date
    expiration_date: date
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxCustomsDeclarationsCreate(BaseModel):
    declaration_id: uuid.UUID
    declaration_number: str
    declaration_type: str
    customs_broker_id: Optional[uuid.UUID] = None
    hs_code_id: Optional[uuid.UUID] = None
    declarant_name: Optional[str] = None
    entry_port: Optional[str] = None
    declaration_date: date
    goods_description: Optional[str] = None
    goods_value: float
    duty_amount: Optional[float] = None
    tax_amount: Optional[float] = None
    total_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxCustomsDeclarationsUpdate(BaseModel):
    declaration_id: Optional[uuid.UUID] = None
    declaration_number: Optional[str] = None
    declaration_type: Optional[str] = None
    customs_broker_id: Optional[uuid.UUID] = None
    hs_code_id: Optional[uuid.UUID] = None
    declarant_name: Optional[str] = None
    entry_port: Optional[str] = None
    declaration_date: Optional[date] = None
    goods_description: Optional[str] = None
    goods_value: Optional[float] = None
    duty_amount: Optional[float] = None
    tax_amount: Optional[float] = None
    total_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxCustomsDeclarationsOut(BaseModel):
    declaration_id: uuid.UUID
    declaration_number: str
    declaration_type: str
    customs_broker_id: Optional[uuid.UUID] = None
    hs_code_id: Optional[uuid.UUID] = None
    declarant_name: Optional[str] = None
    entry_port: Optional[str] = None
    declaration_date: date
    goods_description: Optional[str] = None
    goods_value: float
    duty_amount: Optional[float] = None
    tax_amount: Optional[float] = None
    total_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxDocumentArchivesCreate(BaseModel):
    archive_id: uuid.UUID
    problem_id: Optional[uuid.UUID] = None
    container_id: uuid.UUID
    document_type: str
    document_reference: str
    length_cm: float
    width_cm: float
    height_cm: float
    weight_kg: Optional[float] = None
    retention_years: int
    jurisdiction_code: Optional[str] = None
    access_frequency: Optional[str] = None
    position_x: Optional[float] = None
    position_y: Optional[float] = None
    position_z: Optional[float] = None
    retrieval_sequence: Optional[int] = None
    is_active: bool = True

class TaxDocumentArchivesUpdate(BaseModel):
    archive_id: Optional[uuid.UUID] = None
    problem_id: Optional[uuid.UUID] = None
    container_id: Optional[uuid.UUID] = None
    document_type: Optional[str] = None
    document_reference: Optional[str] = None
    length_cm: Optional[float] = None
    width_cm: Optional[float] = None
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    retention_years: Optional[int] = None
    jurisdiction_code: Optional[str] = None
    access_frequency: Optional[str] = None
    position_x: Optional[float] = None
    position_y: Optional[float] = None
    position_z: Optional[float] = None
    retrieval_sequence: Optional[int] = None
    is_active: Optional[bool] = None

class TaxDocumentArchivesOut(BaseModel):
    archive_id: uuid.UUID
    problem_id: Optional[uuid.UUID] = None
    container_id: uuid.UUID
    document_type: str
    document_reference: str
    length_cm: float
    width_cm: float
    height_cm: float
    weight_kg: Optional[float] = None
    retention_years: int
    jurisdiction_code: Optional[str] = None
    access_frequency: Optional[str] = None
    position_x: Optional[float] = None
    position_y: Optional[float] = None
    position_z: Optional[float] = None
    retrieval_sequence: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxEinvoiceConfigsCreate(BaseModel):
    config_id: uuid.UUID
    country_code: str
    standard: str
    api_endpoint: Optional[str] = None
    api_key_hash: Optional[str] = None
    digital_signature_cert: Optional[str] = None
    is_active: bool = True

class TaxEinvoiceConfigsUpdate(BaseModel):
    config_id: Optional[uuid.UUID] = None
    country_code: Optional[str] = None
    standard: Optional[str] = None
    api_endpoint: Optional[str] = None
    api_key_hash: Optional[str] = None
    digital_signature_cert: Optional[str] = None
    is_active: Optional[bool] = None

class TaxEinvoiceConfigsOut(BaseModel):
    config_id: uuid.UUID
    country_code: str
    standard: str
    api_endpoint: Optional[str] = None
    api_key_hash: Optional[str] = None
    digital_signature_cert: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxEinvoiceResponsesCreate(BaseModel):
    response_id: uuid.UUID
    einvoice_id: uuid.UUID
    response_code: Optional[str] = None
    response_message: Optional[str] = None
    response_data: Optional[dict] = None
    received_at: Optional[datetime] = None
    is_active: bool = True

class TaxEinvoiceResponsesUpdate(BaseModel):
    response_id: Optional[uuid.UUID] = None
    einvoice_id: Optional[uuid.UUID] = None
    response_code: Optional[str] = None
    response_message: Optional[str] = None
    response_data: Optional[dict] = None
    received_at: Optional[datetime] = None
    is_active: Optional[bool] = None

class TaxEinvoiceResponsesOut(BaseModel):
    response_id: uuid.UUID
    einvoice_id: uuid.UUID
    response_code: Optional[str] = None
    response_message: Optional[str] = None
    response_data: Optional[dict] = None
    received_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxEinvoicesCreate(BaseModel):
    einvoice_id: uuid.UUID
    source_module: str
    source_doc_id: uuid.UUID
    invoice_number: str
    invoice_uuid: Optional[uuid.UUID] = None
    standard: str
    xml_content: Optional[str] = None
    qr_code: Optional[str] = None
    digital_signature: Optional[str] = None
    submitted_at: Optional[datetime] = None
    status: Optional[str] = None
    authority_response: Optional[dict] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxEinvoicesUpdate(BaseModel):
    einvoice_id: Optional[uuid.UUID] = None
    source_module: Optional[str] = None
    source_doc_id: Optional[uuid.UUID] = None
    invoice_number: Optional[str] = None
    invoice_uuid: Optional[uuid.UUID] = None
    standard: Optional[str] = None
    xml_content: Optional[str] = None
    qr_code: Optional[str] = None
    digital_signature: Optional[str] = None
    submitted_at: Optional[datetime] = None
    status: Optional[str] = None
    authority_response: Optional[dict] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxEinvoicesOut(BaseModel):
    einvoice_id: uuid.UUID
    source_module: str
    source_doc_id: uuid.UUID
    invoice_number: str
    invoice_uuid: Optional[uuid.UUID] = None
    standard: str
    xml_content: Optional[str] = None
    qr_code: Optional[str] = None
    digital_signature: Optional[str] = None
    submitted_at: Optional[datetime] = None
    status: Optional[str] = None
    authority_response: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxEntityRelationshipsCreate(BaseModel):
    relationship_id: uuid.UUID
    parent_entity_id: uuid.UUID
    child_entity_id: uuid.UUID
    relationship_type: Optional[str] = None
    ownership_pct: Optional[float] = None
    is_active: bool = True

class TaxEntityRelationshipsUpdate(BaseModel):
    relationship_id: Optional[uuid.UUID] = None
    parent_entity_id: Optional[uuid.UUID] = None
    child_entity_id: Optional[uuid.UUID] = None
    relationship_type: Optional[str] = None
    ownership_pct: Optional[float] = None
    is_active: Optional[bool] = None

class TaxEntityRelationshipsOut(BaseModel):
    relationship_id: uuid.UUID
    parent_entity_id: uuid.UUID
    child_entity_id: uuid.UUID
    relationship_type: Optional[str] = None
    ownership_pct: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxEntityStructuresCreate(BaseModel):
    entity_id: uuid.UUID
    entity_name: str
    jurisdiction: str
    tax_rate: Optional[float] = None
    entity_type: Optional[str] = None
    activities: Optional[dict] = None
    is_active: bool = True

class TaxEntityStructuresUpdate(BaseModel):
    entity_id: Optional[uuid.UUID] = None
    entity_name: Optional[str] = None
    jurisdiction: Optional[str] = None
    tax_rate: Optional[float] = None
    entity_type: Optional[str] = None
    activities: Optional[dict] = None
    is_active: Optional[bool] = None

class TaxEntityStructuresOut(BaseModel):
    entity_id: uuid.UUID
    entity_name: str
    jurisdiction: str
    tax_rate: Optional[float] = None
    entity_type: Optional[str] = None
    activities: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxExemptionJurisdictionsCreate(BaseModel):
    mapping_id: uuid.UUID
    exemption_id: uuid.UUID
    tax_jurisdiction_id: uuid.UUID
    is_active: bool = True

class TaxExemptionJurisdictionsUpdate(BaseModel):
    mapping_id: Optional[uuid.UUID] = None
    exemption_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None

class TaxExemptionJurisdictionsOut(BaseModel):
    mapping_id: uuid.UUID
    exemption_id: uuid.UUID
    tax_jurisdiction_id: uuid.UUID
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxExemptionsCreate(BaseModel):
    exemption_id: uuid.UUID
    exemption_code: str
    exemption_name: str
    exemption_type: str
    description: Optional[str] = None
    conditions: Optional[dict] = None
    documentation_required: Optional[str] = None
    effective_from: date
    effective_to: Optional[date] = None
    is_active: bool = True

class TaxExemptionsUpdate(BaseModel):
    exemption_id: Optional[uuid.UUID] = None
    exemption_code: Optional[str] = None
    exemption_name: Optional[str] = None
    exemption_type: Optional[str] = None
    description: Optional[str] = None
    conditions: Optional[dict] = None
    documentation_required: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: Optional[bool] = None

class TaxExemptionsOut(BaseModel):
    exemption_id: uuid.UUID
    exemption_code: str
    exemption_name: str
    exemption_type: str
    description: Optional[str] = None
    conditions: Optional[dict] = None
    documentation_required: Optional[str] = None
    effective_from: date
    effective_to: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxFilingsCreate(BaseModel):
    filing_id: uuid.UUID
    tax_return_id: uuid.UUID
    filing_type: Optional[str] = None
    submission_method: Optional[str] = None
    submitted_by: Optional[uuid.UUID] = None
    submitted_at: Optional[datetime] = None
    confirmation_code: Optional[str] = None
    authority_response: Optional[dict] = None
    status: Optional[str] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxFilingsUpdate(BaseModel):
    filing_id: Optional[uuid.UUID] = None
    tax_return_id: Optional[uuid.UUID] = None
    filing_type: Optional[str] = None
    submission_method: Optional[str] = None
    submitted_by: Optional[uuid.UUID] = None
    submitted_at: Optional[datetime] = None
    confirmation_code: Optional[str] = None
    authority_response: Optional[dict] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxFilingsOut(BaseModel):
    filing_id: uuid.UUID
    tax_return_id: uuid.UUID
    filing_type: Optional[str] = None
    submission_method: Optional[str] = None
    submitted_by: Optional[uuid.UUID] = None
    submitted_at: Optional[datetime] = None
    confirmation_code: Optional[str] = None
    authority_response: Optional[dict] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxHsCodeDutyRatesCreate(BaseModel):
    duty_rate_id: uuid.UUID
    hs_code_id: uuid.UUID
    country_code: str
    duty_rate_pct: float
    duty_type: Optional[str] = None
    fixed_duty_amount: Optional[float] = None
    preferential_rate_pct: Optional[float] = None
    quota_restrictions: Optional[str] = None
    effective_from: date
    effective_to: Optional[date] = None
    is_active: bool = True

class TaxHsCodeDutyRatesUpdate(BaseModel):
    duty_rate_id: Optional[uuid.UUID] = None
    hs_code_id: Optional[uuid.UUID] = None
    country_code: Optional[str] = None
    duty_rate_pct: Optional[float] = None
    duty_type: Optional[str] = None
    fixed_duty_amount: Optional[float] = None
    preferential_rate_pct: Optional[float] = None
    quota_restrictions: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: Optional[bool] = None

class TaxHsCodeDutyRatesOut(BaseModel):
    duty_rate_id: uuid.UUID
    hs_code_id: uuid.UUID
    country_code: str
    duty_rate_pct: float
    duty_type: Optional[str] = None
    fixed_duty_amount: Optional[float] = None
    preferential_rate_pct: Optional[float] = None
    quota_restrictions: Optional[str] = None
    effective_from: date
    effective_to: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxHsCodesCreate(BaseModel):
    hs_code_id: uuid.UUID
    hs_code: str
    hs_chapter: str
    hs_heading: str
    hs_subheading: Optional[str] = None
    hs_national: Optional[str] = None
    description: str
    unit_of_measure: Optional[str] = None
    parent_hs_code_id: Optional[uuid.UUID] = None
    effective_from: date
    effective_to: Optional[date] = None
    is_active: bool = True

class TaxHsCodesUpdate(BaseModel):
    hs_code_id: Optional[uuid.UUID] = None
    hs_code: Optional[str] = None
    hs_chapter: Optional[str] = None
    hs_heading: Optional[str] = None
    hs_subheading: Optional[str] = None
    hs_national: Optional[str] = None
    description: Optional[str] = None
    unit_of_measure: Optional[str] = None
    parent_hs_code_id: Optional[uuid.UUID] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: Optional[bool] = None

class TaxHsCodesOut(BaseModel):
    hs_code_id: uuid.UUID
    hs_code: str
    hs_chapter: str
    hs_heading: str
    hs_subheading: Optional[str] = None
    hs_national: Optional[str] = None
    description: str
    unit_of_measure: Optional[str] = None
    parent_hs_code_id: Optional[uuid.UUID] = None
    effective_from: date
    effective_to: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxIntegrationConnectionsCreate(BaseModel):
    connection_id: uuid.UUID
    connection_name: str
    integration_type: str
    target_system: str
    endpoint_url: Optional[str] = None
    auth_config: Optional[dict] = None
    schedule_cron: Optional[str] = None
    is_active: bool = True

class TaxIntegrationConnectionsUpdate(BaseModel):
    connection_id: Optional[uuid.UUID] = None
    connection_name: Optional[str] = None
    integration_type: Optional[str] = None
    target_system: Optional[str] = None
    endpoint_url: Optional[str] = None
    auth_config: Optional[dict] = None
    schedule_cron: Optional[str] = None
    is_active: Optional[bool] = None

class TaxIntegrationConnectionsOut(BaseModel):
    connection_id: uuid.UUID
    connection_name: str
    integration_type: str
    target_system: str
    endpoint_url: Optional[str] = None
    auth_config: Optional[dict] = None
    schedule_cron: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxIntegrationLogsCreate(BaseModel):
    log_id: uuid.UUID
    connection_id: Optional[uuid.UUID] = None
    direction: Optional[str] = None
    payload: Optional[dict] = None
    response: Optional[dict] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    executed_at: Optional[datetime] = None
    duration_ms: Optional[int] = None
    is_active: bool = True

class TaxIntegrationLogsUpdate(BaseModel):
    log_id: Optional[uuid.UUID] = None
    connection_id: Optional[uuid.UUID] = None
    direction: Optional[str] = None
    payload: Optional[dict] = None
    response: Optional[dict] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    executed_at: Optional[datetime] = None
    duration_ms: Optional[int] = None
    is_active: Optional[bool] = None

class TaxIntegrationLogsOut(BaseModel):
    log_id: uuid.UUID
    connection_id: Optional[uuid.UUID] = None
    direction: Optional[str] = None
    payload: Optional[dict] = None
    response: Optional[dict] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    executed_at: Optional[datetime] = None
    duration_ms: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxJurisdictionAddressesCreate(BaseModel):
    address_id: uuid.UUID
    tax_jurisdiction_id: uuid.UUID
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    is_active: bool = True

class TaxJurisdictionAddressesUpdate(BaseModel):
    address_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    is_active: Optional[bool] = None

class TaxJurisdictionAddressesOut(BaseModel):
    address_id: uuid.UUID
    tax_jurisdiction_id: uuid.UUID
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxJurisdictionAgreementsCreate(BaseModel):
    agreement_id: uuid.UUID
    jurisdiction_id_a: uuid.UUID
    jurisdiction_id_b: uuid.UUID
    agreement_type: str
    effective_from: date
    effective_to: Optional[date] = None
    description: Optional[str] = None
    is_active: bool = True

class TaxJurisdictionAgreementsUpdate(BaseModel):
    agreement_id: Optional[uuid.UUID] = None
    jurisdiction_id_a: Optional[uuid.UUID] = None
    jurisdiction_id_b: Optional[uuid.UUID] = None
    agreement_type: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class TaxJurisdictionAgreementsOut(BaseModel):
    agreement_id: uuid.UUID
    jurisdiction_id_a: uuid.UUID
    jurisdiction_id_b: uuid.UUID
    agreement_type: str
    effective_from: date
    effective_to: Optional[date] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxJurisdictionsCreate(BaseModel):
    tax_jurisdiction_id: uuid.UUID
    country_code: str
    jurisdiction_code: str
    jurisdiction_name: str
    jurisdiction_type: str
    parent_jurisdiction_id: Optional[uuid.UUID] = None
    is_active: bool = True

class TaxJurisdictionsUpdate(BaseModel):
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    country_code: Optional[str] = None
    jurisdiction_code: Optional[str] = None
    jurisdiction_name: Optional[str] = None
    jurisdiction_type: Optional[str] = None
    parent_jurisdiction_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None

class TaxJurisdictionsOut(BaseModel):
    tax_jurisdiction_id: uuid.UUID
    country_code: str
    jurisdiction_code: str
    jurisdiction_name: str
    jurisdiction_type: str
    parent_jurisdiction_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxLanggraphExecutionsCreate(BaseModel):
    execution_id: uuid.UUID
    workflow_id: uuid.UUID
    execution_name: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    current_state: Optional[str] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    is_active: bool = True

class TaxLanggraphExecutionsUpdate(BaseModel):
    execution_id: Optional[uuid.UUID] = None
    workflow_id: Optional[uuid.UUID] = None
    execution_name: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    current_state: Optional[str] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    is_active: Optional[bool] = None

class TaxLanggraphExecutionsOut(BaseModel):
    execution_id: uuid.UUID
    workflow_id: uuid.UUID
    execution_name: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    current_state: Optional[str] = None
    status: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxLanggraphStatesCreate(BaseModel):
    state_id: uuid.UUID
    execution_id: uuid.UUID
    node_id: str
    node_type: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool = True

class TaxLanggraphStatesUpdate(BaseModel):
    state_id: Optional[uuid.UUID] = None
    execution_id: Optional[uuid.UUID] = None
    node_id: Optional[str] = None
    node_type: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: Optional[bool] = None

class TaxLanggraphStatesOut(BaseModel):
    state_id: uuid.UUID
    execution_id: uuid.UUID
    node_id: str
    node_type: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxLanggraphWorkflowsCreate(BaseModel):
    workflow_id: uuid.UUID
    workflow_name: str
    workflow_description: Optional[str] = None
    dag_definition: dict
    state_schema: Optional[dict] = None
    checkpoint_enabled: Optional[bool] = None
    hitl_nodes: Optional[dict] = None
    workflow_version: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxLanggraphWorkflowsUpdate(BaseModel):
    workflow_id: Optional[uuid.UUID] = None
    workflow_name: Optional[str] = None
    workflow_description: Optional[str] = None
    dag_definition: Optional[dict] = None
    state_schema: Optional[dict] = None
    checkpoint_enabled: Optional[bool] = None
    hitl_nodes: Optional[dict] = None
    workflow_version: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxLanggraphWorkflowsOut(BaseModel):
    workflow_id: uuid.UUID
    workflow_name: str
    workflow_description: Optional[str] = None
    dag_definition: dict
    state_schema: Optional[dict] = None
    checkpoint_enabled: Optional[bool] = None
    hitl_nodes: Optional[dict] = None
    workflow_version: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxLinesCreate(BaseModel):
    tax_line_id: uuid.UUID
    tax_transaction_id: uuid.UUID
    line_sequence: int
    tax_code_id: Optional[uuid.UUID] = None
    tax_rate_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    taxable_amount: float
    tax_amount: float
    non_recoverable_amount: Optional[float] = None
    tax_rate_pct: Optional[float] = None
    exemption_id: Optional[uuid.UUID] = None
    exemption_amount: Optional[float] = None
    place_of_supply_id: Optional[uuid.UUID] = None
    currency_code: Optional[str] = None
    exchange_rate: Optional[float] = None
    rounding_adjustment: Optional[float] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxLinesUpdate(BaseModel):
    tax_line_id: Optional[uuid.UUID] = None
    tax_transaction_id: Optional[uuid.UUID] = None
    line_sequence: Optional[int] = None
    tax_code_id: Optional[uuid.UUID] = None
    tax_rate_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    taxable_amount: Optional[float] = None
    tax_amount: Optional[float] = None
    non_recoverable_amount: Optional[float] = None
    tax_rate_pct: Optional[float] = None
    exemption_id: Optional[uuid.UUID] = None
    exemption_amount: Optional[float] = None
    place_of_supply_id: Optional[uuid.UUID] = None
    currency_code: Optional[str] = None
    exchange_rate: Optional[float] = None
    rounding_adjustment: Optional[float] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxLinesOut(BaseModel):
    tax_line_id: uuid.UUID
    tax_transaction_id: uuid.UUID
    line_sequence: int
    tax_code_id: Optional[uuid.UUID] = None
    tax_rate_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    taxable_amount: float
    tax_amount: float
    non_recoverable_amount: Optional[float] = None
    tax_rate_pct: Optional[float] = None
    exemption_id: Optional[uuid.UUID] = None
    exemption_amount: Optional[float] = None
    place_of_supply_id: Optional[uuid.UUID] = None
    currency_code: Optional[str] = None
    exchange_rate: Optional[float] = None
    rounding_adjustment: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxLlmConfigsCreate(BaseModel):
    llm_config_id: uuid.UUID
    provider: str
    model_name: str
    api_key_hash: Optional[str] = None
    parameters: Optional[dict] = None
    is_active: bool = True

class TaxLlmConfigsUpdate(BaseModel):
    llm_config_id: Optional[uuid.UUID] = None
    provider: Optional[str] = None
    model_name: Optional[str] = None
    api_key_hash: Optional[str] = None
    parameters: Optional[dict] = None
    is_active: Optional[bool] = None

class TaxLlmConfigsOut(BaseModel):
    llm_config_id: uuid.UUID
    provider: str
    model_name: str
    api_key_hash: Optional[str] = None
    parameters: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxMlModelsCreate(BaseModel):
    model_id: uuid.UUID
    model_type: str
    model_name: str
    framework: Optional[str] = None
    model_version: Optional[str] = None
    description: Optional[str] = None
    training_params: Optional[dict] = None
    feature_columns: Optional[dict] = None
    target_column: Optional[str] = None
    accuracy_metric: Optional[float] = None
    is_active: bool = True

class TaxMlModelsUpdate(BaseModel):
    model_id: Optional[uuid.UUID] = None
    model_type: Optional[str] = None
    model_name: Optional[str] = None
    framework: Optional[str] = None
    model_version: Optional[str] = None
    description: Optional[str] = None
    training_params: Optional[dict] = None
    feature_columns: Optional[dict] = None
    target_column: Optional[str] = None
    accuracy_metric: Optional[float] = None
    is_active: Optional[bool] = None

class TaxMlModelsOut(BaseModel):
    model_id: uuid.UUID
    model_type: str
    model_name: str
    framework: Optional[str] = None
    model_version: Optional[str] = None
    description: Optional[str] = None
    training_params: Optional[dict] = None
    feature_columns: Optional[dict] = None
    target_column: Optional[str] = None
    accuracy_metric: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxOptimizationProblemsCreate(BaseModel):
    problem_id: uuid.UUID
    problem_name: str
    problem_type: str
    description: Optional[str] = None
    objective_type: str
    objective_function: Optional[dict] = None
    constraints: Optional[dict] = None
    variables: Optional[dict] = None
    parameters: Optional[dict] = None
    data_sources: Optional[dict] = None
    solver_type: Optional[str] = None
    solver_config: Optional[dict] = None
    status: Optional[str] = None
    solve_time_ms: Optional[int] = None
    objective_value: Optional[float] = None
    tax_savings_amount: Optional[float] = None
    tax_savings_currency: Optional[str] = None
    is_active: bool = True

class TaxOptimizationProblemsUpdate(BaseModel):
    problem_id: Optional[uuid.UUID] = None
    problem_name: Optional[str] = None
    problem_type: Optional[str] = None
    description: Optional[str] = None
    objective_type: Optional[str] = None
    objective_function: Optional[dict] = None
    constraints: Optional[dict] = None
    variables: Optional[dict] = None
    parameters: Optional[dict] = None
    data_sources: Optional[dict] = None
    solver_type: Optional[str] = None
    solver_config: Optional[dict] = None
    status: Optional[str] = None
    solve_time_ms: Optional[int] = None
    objective_value: Optional[float] = None
    tax_savings_amount: Optional[float] = None
    tax_savings_currency: Optional[str] = None
    is_active: Optional[bool] = None

class TaxOptimizationProblemsOut(BaseModel):
    problem_id: uuid.UUID
    problem_name: str
    problem_type: str
    description: Optional[str] = None
    objective_type: str
    objective_function: Optional[dict] = None
    constraints: Optional[dict] = None
    variables: Optional[dict] = None
    parameters: Optional[dict] = None
    data_sources: Optional[dict] = None
    solver_type: Optional[str] = None
    solver_config: Optional[dict] = None
    status: Optional[str] = None
    solve_time_ms: Optional[int] = None
    objective_value: Optional[float] = None
    tax_savings_amount: Optional[float] = None
    tax_savings_currency: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxOptimizationScenariosCreate(BaseModel):
    scenario_id: uuid.UUID
    problem_id: uuid.UUID
    scenario_name: str
    assumptions: Optional[dict] = None
    constraints_override: Optional[dict] = None
    parameters_override: Optional[dict] = None
    result_data: Optional[dict] = None
    objective_value: Optional[float] = None
    tax_savings_amount: Optional[float] = None
    is_active: bool = True

class TaxOptimizationScenariosUpdate(BaseModel):
    scenario_id: Optional[uuid.UUID] = None
    problem_id: Optional[uuid.UUID] = None
    scenario_name: Optional[str] = None
    assumptions: Optional[dict] = None
    constraints_override: Optional[dict] = None
    parameters_override: Optional[dict] = None
    result_data: Optional[dict] = None
    objective_value: Optional[float] = None
    tax_savings_amount: Optional[float] = None
    is_active: Optional[bool] = None

class TaxOptimizationScenariosOut(BaseModel):
    scenario_id: uuid.UUID
    problem_id: uuid.UUID
    scenario_name: str
    assumptions: Optional[dict] = None
    constraints_override: Optional[dict] = None
    parameters_override: Optional[dict] = None
    result_data: Optional[dict] = None
    objective_value: Optional[float] = None
    tax_savings_amount: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxOptimizationSolutionsCreate(BaseModel):
    solution_id: uuid.UUID
    problem_id: uuid.UUID
    solution_version: int
    solution_data: dict
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_optimal: Optional[bool] = None
    is_active: bool = True

class TaxOptimizationSolutionsUpdate(BaseModel):
    solution_id: Optional[uuid.UUID] = None
    problem_id: Optional[uuid.UUID] = None
    solution_version: Optional[int] = None
    solution_data: Optional[dict] = None
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_optimal: Optional[bool] = None
    is_active: Optional[bool] = None

class TaxOptimizationSolutionsOut(BaseModel):
    solution_id: uuid.UUID
    problem_id: uuid.UUID
    solution_version: int
    solution_data: dict
    objective_value: Optional[float] = None
    solve_time_ms: Optional[int] = None
    is_optimal: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxOrtoolsProblemsCreate(BaseModel):
    ortools_id: uuid.UUID
    problem_type: str
    problem_name: str
    problem_definition: dict
    problem_data: Optional[dict] = None
    solution_result: Optional[dict] = None
    solution_quality: Optional[str] = None
    solve_time_ms: Optional[int] = None
    solver_config_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxOrtoolsProblemsUpdate(BaseModel):
    ortools_id: Optional[uuid.UUID] = None
    problem_type: Optional[str] = None
    problem_name: Optional[str] = None
    problem_definition: Optional[dict] = None
    problem_data: Optional[dict] = None
    solution_result: Optional[dict] = None
    solution_quality: Optional[str] = None
    solve_time_ms: Optional[int] = None
    solver_config_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxOrtoolsProblemsOut(BaseModel):
    ortools_id: uuid.UUID
    problem_type: str
    problem_name: str
    problem_definition: dict
    problem_data: Optional[dict] = None
    solution_result: Optional[dict] = None
    solution_quality: Optional[str] = None
    solve_time_ms: Optional[int] = None
    solver_config_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxPenaltiesCreate(BaseModel):
    penalty_id: uuid.UUID
    penalty_type: str
    assessment_id: Optional[uuid.UUID] = None
    penalty_amount: float
    calculated_at: date
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxPenaltiesUpdate(BaseModel):
    penalty_id: Optional[uuid.UUID] = None
    penalty_type: Optional[str] = None
    assessment_id: Optional[uuid.UUID] = None
    penalty_amount: Optional[float] = None
    calculated_at: Optional[date] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxPenaltiesOut(BaseModel):
    penalty_id: uuid.UUID
    penalty_type: str
    assessment_id: Optional[uuid.UUID] = None
    penalty_amount: float
    calculated_at: date
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxPenaltyWaiversCreate(BaseModel):
    waiver_id: uuid.UUID
    penalty_id: uuid.UUID
    waiver_date: date
    waiver_reason: str
    waived_amount: float
    approved_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxPenaltyWaiversUpdate(BaseModel):
    waiver_id: Optional[uuid.UUID] = None
    penalty_id: Optional[uuid.UUID] = None
    waiver_date: Optional[date] = None
    waiver_reason: Optional[str] = None
    waived_amount: Optional[float] = None
    approved_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxPenaltyWaiversOut(BaseModel):
    waiver_id: uuid.UUID
    penalty_id: uuid.UUID
    waiver_date: date
    waiver_reason: str
    waived_amount: float
    approved_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxPeriodsCreate(BaseModel):
    tax_period_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    period_type: str
    period_name: str
    period_code: str
    start_date: date
    end_date: date
    due_date: date
    status: Optional[str] = None
    is_active: bool = True

class TaxPeriodsUpdate(BaseModel):
    tax_period_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    period_type: Optional[str] = None
    period_name: Optional[str] = None
    period_code: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    due_date: Optional[date] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxPeriodsOut(BaseModel):
    tax_period_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    period_type: str
    period_name: str
    period_code: str
    start_date: date
    end_date: date
    due_date: date
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxPredictionActualsCreate(BaseModel):
    actual_id: uuid.UUID
    prediction_id: uuid.UUID
    actual_value: float
    error_absolute: Optional[float] = None
    error_pct: Optional[float] = None
    observation_date: date
    is_active: bool = True

class TaxPredictionActualsUpdate(BaseModel):
    actual_id: Optional[uuid.UUID] = None
    prediction_id: Optional[uuid.UUID] = None
    actual_value: Optional[float] = None
    error_absolute: Optional[float] = None
    error_pct: Optional[float] = None
    observation_date: Optional[date] = None
    is_active: Optional[bool] = None

class TaxPredictionActualsOut(BaseModel):
    actual_id: uuid.UUID
    prediction_id: uuid.UUID
    actual_value: float
    error_absolute: Optional[float] = None
    error_pct: Optional[float] = None
    observation_date: date
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxPredictionsCreate(BaseModel):
    prediction_id: uuid.UUID
    model_id: Optional[uuid.UUID] = None
    prediction_type: str
    entity_id: Optional[uuid.UUID] = None
    jurisdiction: Optional[str] = None
    tax_type_id: Optional[uuid.UUID] = None
    prediction_date: date
    prediction_value: Optional[float] = None
    prediction_lower: Optional[float] = None
    prediction_upper: Optional[float] = None
    confidence_level: Optional[float] = None
    features_used: Optional[dict] = None
    scenario_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxPredictionsUpdate(BaseModel):
    prediction_id: Optional[uuid.UUID] = None
    model_id: Optional[uuid.UUID] = None
    prediction_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    jurisdiction: Optional[str] = None
    tax_type_id: Optional[uuid.UUID] = None
    prediction_date: Optional[date] = None
    prediction_value: Optional[float] = None
    prediction_lower: Optional[float] = None
    prediction_upper: Optional[float] = None
    confidence_level: Optional[float] = None
    features_used: Optional[dict] = None
    scenario_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxPredictionsOut(BaseModel):
    prediction_id: uuid.UUID
    model_id: Optional[uuid.UUID] = None
    prediction_type: str
    entity_id: Optional[uuid.UUID] = None
    jurisdiction: Optional[str] = None
    tax_type_id: Optional[uuid.UUID] = None
    prediction_date: date
    prediction_value: Optional[float] = None
    prediction_lower: Optional[float] = None
    prediction_upper: Optional[float] = None
    confidence_level: Optional[float] = None
    features_used: Optional[dict] = None
    scenario_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxPromptTemplatesCreate(BaseModel):
    prompt_id: uuid.UUID
    prompt_type: str
    prompt_name: str
    template_text: str
    input_variables: Optional[dict] = None
    output_schema: Optional[dict] = None
    llm_config_id: Optional[uuid.UUID] = None
    version: Optional[str] = None
    is_active: bool = True

class TaxPromptTemplatesUpdate(BaseModel):
    prompt_id: Optional[uuid.UUID] = None
    prompt_type: Optional[str] = None
    prompt_name: Optional[str] = None
    template_text: Optional[str] = None
    input_variables: Optional[dict] = None
    output_schema: Optional[dict] = None
    llm_config_id: Optional[uuid.UUID] = None
    version: Optional[str] = None
    is_active: Optional[bool] = None

class TaxPromptTemplatesOut(BaseModel):
    prompt_id: uuid.UUID
    prompt_type: str
    prompt_name: str
    template_text: str
    input_variables: Optional[dict] = None
    output_schema: Optional[dict] = None
    llm_config_id: Optional[uuid.UUID] = None
    version: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxRateTiersCreate(BaseModel):
    tier_id: uuid.UUID
    tax_rate_id: uuid.UUID
    tier_sequence: int
    from_amount: float
    to_amount: Optional[float] = None
    tier_rate_pct: float
    tier_fixed_amount: Optional[float] = None
    is_active: bool = True

class TaxRateTiersUpdate(BaseModel):
    tier_id: Optional[uuid.UUID] = None
    tax_rate_id: Optional[uuid.UUID] = None
    tier_sequence: Optional[int] = None
    from_amount: Optional[float] = None
    to_amount: Optional[float] = None
    tier_rate_pct: Optional[float] = None
    tier_fixed_amount: Optional[float] = None
    is_active: Optional[bool] = None

class TaxRateTiersOut(BaseModel):
    tier_id: uuid.UUID
    tax_rate_id: uuid.UUID
    tier_sequence: int
    from_amount: float
    to_amount: Optional[float] = None
    tier_rate_pct: float
    tier_fixed_amount: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxRatesCreate(BaseModel):
    tax_rate_id: uuid.UUID
    tax_type_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    tax_status_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    tax_code: str
    tax_rate_pct: float
    recovery_rate_pct: Optional[float] = None
    effective_from: date
    effective_to: Optional[date] = None
    gl_account_id: Optional[uuid.UUID] = None
    round_rule: Optional[str] = None
    minimum_amount: Optional[float] = None
    maximum_amount: Optional[float] = None
    description: Optional[str] = None
    is_active: bool = True
    rate_type: Optional[str] = None
    fixed_amount: Optional[float] = None
    priority: Optional[int] = None

class TaxRatesUpdate(BaseModel):
    tax_rate_id: Optional[uuid.UUID] = None
    tax_type_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_status_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    tax_code: Optional[str] = None
    tax_rate_pct: Optional[float] = None
    recovery_rate_pct: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    gl_account_id: Optional[uuid.UUID] = None
    round_rule: Optional[str] = None
    minimum_amount: Optional[float] = None
    maximum_amount: Optional[float] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    rate_type: Optional[str] = None
    fixed_amount: Optional[float] = None
    priority: Optional[int] = None

class TaxRatesOut(BaseModel):
    tax_rate_id: uuid.UUID
    tax_type_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    tax_status_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    tax_code: str
    tax_rate_pct: float
    recovery_rate_pct: Optional[float] = None
    effective_from: date
    effective_to: Optional[date] = None
    gl_account_id: Optional[uuid.UUID] = None
    round_rule: Optional[str] = None
    minimum_amount: Optional[float] = None
    maximum_amount: Optional[float] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    rate_type: Optional[str] = None
    fixed_amount: Optional[float] = None
    priority: Optional[int] = None
    model_config = {"from_attributes": True}

class TaxReconciliationsCreate(BaseModel):
    reconciliation_id: uuid.UUID
    reconciliation_type: str
    tax_regime_id: Optional[uuid.UUID] = None
    tax_period_id: Optional[uuid.UUID] = None
    gl_tax_balance: Optional[float] = None
    return_tax_amount: Optional[float] = None
    variance_amount: Optional[float] = None
    variance_reason: Optional[str] = None
    adjustment_amount: Optional[float] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxReconciliationsUpdate(BaseModel):
    reconciliation_id: Optional[uuid.UUID] = None
    reconciliation_type: Optional[str] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_period_id: Optional[uuid.UUID] = None
    gl_tax_balance: Optional[float] = None
    return_tax_amount: Optional[float] = None
    variance_amount: Optional[float] = None
    variance_reason: Optional[str] = None
    adjustment_amount: Optional[float] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxReconciliationsOut(BaseModel):
    reconciliation_id: uuid.UUID
    reconciliation_type: str
    tax_regime_id: Optional[uuid.UUID] = None
    tax_period_id: Optional[uuid.UUID] = None
    gl_tax_balance: Optional[float] = None
    return_tax_amount: Optional[float] = None
    variance_amount: Optional[float] = None
    variance_reason: Optional[str] = None
    adjustment_amount: Optional[float] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxRefundsCreate(BaseModel):
    refund_id: uuid.UUID
    refund_type: str
    tax_authority_id: Optional[uuid.UUID] = None
    tax_period_id: Optional[uuid.UUID] = None
    claim_number: str
    claim_date: date
    claimed_amount: float
    approved_amount: Optional[float] = None
    paid_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    paid_date: Optional[date] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxRefundsUpdate(BaseModel):
    refund_id: Optional[uuid.UUID] = None
    refund_type: Optional[str] = None
    tax_authority_id: Optional[uuid.UUID] = None
    tax_period_id: Optional[uuid.UUID] = None
    claim_number: Optional[str] = None
    claim_date: Optional[date] = None
    claimed_amount: Optional[float] = None
    approved_amount: Optional[float] = None
    paid_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    paid_date: Optional[date] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxRefundsOut(BaseModel):
    refund_id: uuid.UUID
    refund_type: str
    tax_authority_id: Optional[uuid.UUID] = None
    tax_period_id: Optional[uuid.UUID] = None
    claim_number: str
    claim_date: date
    claimed_amount: float
    approved_amount: Optional[float] = None
    paid_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    paid_date: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxRegimeAttachmentsCreate(BaseModel):
    attachment_id: uuid.UUID
    tax_regime_id: uuid.UUID
    attachment_type: str
    file_name: str
    file_url: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True

class TaxRegimeAttachmentsUpdate(BaseModel):
    attachment_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    attachment_type: Optional[str] = None
    file_name: Optional[str] = None
    file_url: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class TaxRegimeAttachmentsOut(BaseModel):
    attachment_id: uuid.UUID
    tax_regime_id: uuid.UUID
    attachment_type: str
    file_name: str
    file_url: Optional[str] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxRegimeRulesCreate(BaseModel):
    regime_rule_id: uuid.UUID
    tax_regime_id: uuid.UUID
    rule_code: str
    rule_name: str
    rule_type: str
    rule_conditions: Optional[dict] = None
    rule_action: Optional[dict] = None
    effective_from: date
    effective_to: Optional[date] = None
    priority: Optional[int] = None
    is_active: bool = True

class TaxRegimeRulesUpdate(BaseModel):
    regime_rule_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    rule_code: Optional[str] = None
    rule_name: Optional[str] = None
    rule_type: Optional[str] = None
    rule_conditions: Optional[dict] = None
    rule_action: Optional[dict] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    priority: Optional[int] = None
    is_active: Optional[bool] = None

class TaxRegimeRulesOut(BaseModel):
    regime_rule_id: uuid.UUID
    tax_regime_id: uuid.UUID
    rule_code: str
    rule_name: str
    rule_type: str
    rule_conditions: Optional[dict] = None
    rule_action: Optional[dict] = None
    effective_from: date
    effective_to: Optional[date] = None
    priority: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxRegimesCreate(BaseModel):
    tax_regime_id: uuid.UUID
    country_code: str
    tax_regime_code: str
    tax_regime_name: str
    tax_type: str
    description: Optional[str] = None
    is_active: bool = True
    regime_type: Optional[str] = None
    accounting_method: Optional[str] = None
    reporting_frequency: Optional[str] = None
    is_tax_inclusive: Optional[bool] = None
    rounding_rule: Optional[str] = None
    registration_threshold: Optional[float] = None
    filing_threshold: Optional[float] = None

class TaxRegimesUpdate(BaseModel):
    tax_regime_id: Optional[uuid.UUID] = None
    country_code: Optional[str] = None
    tax_regime_code: Optional[str] = None
    tax_regime_name: Optional[str] = None
    tax_type: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    regime_type: Optional[str] = None
    accounting_method: Optional[str] = None
    reporting_frequency: Optional[str] = None
    is_tax_inclusive: Optional[bool] = None
    rounding_rule: Optional[str] = None
    registration_threshold: Optional[float] = None
    filing_threshold: Optional[float] = None

class TaxRegimesOut(BaseModel):
    tax_regime_id: uuid.UUID
    country_code: str
    tax_regime_code: str
    tax_regime_name: str
    tax_type: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    regime_type: Optional[str] = None
    accounting_method: Optional[str] = None
    reporting_frequency: Optional[str] = None
    is_tax_inclusive: Optional[bool] = None
    rounding_rule: Optional[str] = None
    registration_threshold: Optional[float] = None
    filing_threshold: Optional[float] = None
    model_config = {"from_attributes": True}

class TaxRegistrationsCreate(BaseModel):
    registration_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    tax_authority_id: Optional[uuid.UUID] = None
    registration_number: str
    registration_type: str
    effective_from: date
    effective_to: Optional[date] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxRegistrationsUpdate(BaseModel):
    registration_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    tax_authority_id: Optional[uuid.UUID] = None
    registration_number: Optional[str] = None
    registration_type: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxRegistrationsOut(BaseModel):
    registration_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    tax_authority_id: Optional[uuid.UUID] = None
    registration_number: str
    registration_type: str
    effective_from: date
    effective_to: Optional[date] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxReportTypesCreate(BaseModel):
    report_type_id: uuid.UUID
    report_type_code: str
    report_type_name: str
    description: Optional[str] = None
    default_format: Optional[str] = None
    is_active: bool = True

class TaxReportTypesUpdate(BaseModel):
    report_type_id: Optional[uuid.UUID] = None
    report_type_code: Optional[str] = None
    report_type_name: Optional[str] = None
    description: Optional[str] = None
    default_format: Optional[str] = None
    is_active: Optional[bool] = None

class TaxReportTypesOut(BaseModel):
    report_type_id: uuid.UUID
    report_type_code: str
    report_type_name: str
    description: Optional[str] = None
    default_format: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxReportsCreate(BaseModel):
    report_id: uuid.UUID
    report_type_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_period_id: Optional[uuid.UUID] = None
    report_name: str
    report_format: Optional[str] = None
    parameters: Optional[dict] = None
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    generated_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxReportsUpdate(BaseModel):
    report_id: Optional[uuid.UUID] = None
    report_type_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_period_id: Optional[uuid.UUID] = None
    report_name: Optional[str] = None
    report_format: Optional[str] = None
    parameters: Optional[dict] = None
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    generated_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxReportsOut(BaseModel):
    report_id: uuid.UUID
    report_type_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_period_id: Optional[uuid.UUID] = None
    report_name: str
    report_format: Optional[str] = None
    parameters: Optional[dict] = None
    file_url: Optional[str] = None
    generated_at: Optional[datetime] = None
    generated_by: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxReturnAttachmentsCreate(BaseModel):
    attachment_id: uuid.UUID
    tax_return_id: uuid.UUID
    file_name: str
    file_url: Optional[str] = None
    attachment_type: Optional[str] = None
    is_active: bool = True

class TaxReturnAttachmentsUpdate(BaseModel):
    attachment_id: Optional[uuid.UUID] = None
    tax_return_id: Optional[uuid.UUID] = None
    file_name: Optional[str] = None
    file_url: Optional[str] = None
    attachment_type: Optional[str] = None
    is_active: Optional[bool] = None

class TaxReturnAttachmentsOut(BaseModel):
    attachment_id: uuid.UUID
    tax_return_id: uuid.UUID
    file_name: str
    file_url: Optional[str] = None
    attachment_type: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxReturnsCreate(BaseModel):
    tax_return_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    tax_period_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    tax_authority_id: Optional[uuid.UUID] = None
    return_type: Optional[str] = None
    return_number: str
    period_name: str
    due_date: date
    submitted_date: Optional[date] = None
    accepted_date: Optional[date] = None
    status: Optional[str] = None
    taxable_sales: Optional[float] = None
    taxable_purchases: Optional[float] = None
    output_tax: Optional[float] = None
    input_tax: Optional[float] = None
    net_tax_payable: Optional[float] = None
    net_tax_refundable: Optional[float] = None
    total_adjustments: Optional[float] = None
    currency_code: Optional[str] = None
    filing_confirmation: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True

class TaxReturnsUpdate(BaseModel):
    tax_return_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_period_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    tax_authority_id: Optional[uuid.UUID] = None
    return_type: Optional[str] = None
    return_number: Optional[str] = None
    period_name: Optional[str] = None
    due_date: Optional[date] = None
    submitted_date: Optional[date] = None
    accepted_date: Optional[date] = None
    status: Optional[str] = None
    taxable_sales: Optional[float] = None
    taxable_purchases: Optional[float] = None
    output_tax: Optional[float] = None
    input_tax: Optional[float] = None
    net_tax_payable: Optional[float] = None
    net_tax_refundable: Optional[float] = None
    total_adjustments: Optional[float] = None
    currency_code: Optional[str] = None
    filing_confirmation: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None

class TaxReturnsOut(BaseModel):
    tax_return_id: uuid.UUID
    tax_regime_id: Optional[uuid.UUID] = None
    tax_period_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    tax_authority_id: Optional[uuid.UUID] = None
    return_type: Optional[str] = None
    return_number: str
    period_name: str
    due_date: date
    submitted_date: Optional[date] = None
    accepted_date: Optional[date] = None
    status: Optional[str] = None
    taxable_sales: Optional[float] = None
    taxable_purchases: Optional[float] = None
    output_tax: Optional[float] = None
    input_tax: Optional[float] = None
    net_tax_payable: Optional[float] = None
    net_tax_refundable: Optional[float] = None
    total_adjustments: Optional[float] = None
    currency_code: Optional[str] = None
    filing_confirmation: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxRuleConditionsCreate(BaseModel):
    condition_id: uuid.UUID
    tax_rule_id: uuid.UUID
    condition_sequence: int
    field_name: str
    operator: str
    field_value: str
    is_active: bool = True

class TaxRuleConditionsUpdate(BaseModel):
    condition_id: Optional[uuid.UUID] = None
    tax_rule_id: Optional[uuid.UUID] = None
    condition_sequence: Optional[int] = None
    field_name: Optional[str] = None
    operator: Optional[str] = None
    field_value: Optional[str] = None
    is_active: Optional[bool] = None

class TaxRuleConditionsOut(BaseModel):
    condition_id: uuid.UUID
    tax_rule_id: uuid.UUID
    condition_sequence: int
    field_name: str
    operator: str
    field_value: str
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxRuleTaxCodesCreate(BaseModel):
    assignment_id: uuid.UUID
    tax_rule_id: uuid.UUID
    tax_code_id: uuid.UUID
    is_default: Optional[bool] = None
    is_active: bool = True

class TaxRuleTaxCodesUpdate(BaseModel):
    assignment_id: Optional[uuid.UUID] = None
    tax_rule_id: Optional[uuid.UUID] = None
    tax_code_id: Optional[uuid.UUID] = None
    is_default: Optional[bool] = None
    is_active: Optional[bool] = None

class TaxRuleTaxCodesOut(BaseModel):
    assignment_id: uuid.UUID
    tax_rule_id: uuid.UUID
    tax_code_id: uuid.UUID
    is_default: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxRulesCreate(BaseModel):
    tax_rule_id: uuid.UUID
    rule_code: str
    rule_name: str
    rule_type: str
    description: Optional[str] = None
    priority: Optional[int] = None
    effective_from: date
    effective_to: Optional[date] = None
    condition_operator: Optional[str] = None
    conditions: dict
    actions: dict
    is_active: bool = True

class TaxRulesUpdate(BaseModel):
    tax_rule_id: Optional[uuid.UUID] = None
    rule_code: Optional[str] = None
    rule_name: Optional[str] = None
    rule_type: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    condition_operator: Optional[str] = None
    conditions: Optional[dict] = None
    actions: Optional[dict] = None
    is_active: Optional[bool] = None

class TaxRulesOut(BaseModel):
    tax_rule_id: uuid.UUID
    rule_code: str
    rule_name: str
    rule_type: str
    description: Optional[str] = None
    priority: Optional[int] = None
    effective_from: date
    effective_to: Optional[date] = None
    condition_operator: Optional[str] = None
    conditions: dict
    actions: dict
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxScenariosCreate(BaseModel):
    scenario_id: uuid.UUID
    scenario_name: str
    scenario_type: str
    description: Optional[str] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    objective: Optional[str] = None
    result_summary: Optional[dict] = None
    tax_impact_amount: Optional[float] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxScenariosUpdate(BaseModel):
    scenario_id: Optional[uuid.UUID] = None
    scenario_name: Optional[str] = None
    scenario_type: Optional[str] = None
    description: Optional[str] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    objective: Optional[str] = None
    result_summary: Optional[dict] = None
    tax_impact_amount: Optional[float] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxScenariosOut(BaseModel):
    scenario_id: uuid.UUID
    scenario_name: str
    scenario_type: str
    description: Optional[str] = None
    assumptions: Optional[dict] = None
    constraints: Optional[dict] = None
    objective: Optional[str] = None
    result_summary: Optional[dict] = None
    tax_impact_amount: Optional[float] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxScipyAnalysesCreate(BaseModel):
    analysis_id: uuid.UUID
    analysis_type: str
    analysis_name: str
    input_data: Optional[dict] = None
    analysis_params: Optional[dict] = None
    result_data: Optional[dict] = None
    solver_config_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxScipyAnalysesUpdate(BaseModel):
    analysis_id: Optional[uuid.UUID] = None
    analysis_type: Optional[str] = None
    analysis_name: Optional[str] = None
    input_data: Optional[dict] = None
    analysis_params: Optional[dict] = None
    result_data: Optional[dict] = None
    solver_config_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxScipyAnalysesOut(BaseModel):
    analysis_id: uuid.UUID
    analysis_type: str
    analysis_name: str
    input_data: Optional[dict] = None
    analysis_params: Optional[dict] = None
    result_data: Optional[dict] = None
    solver_config_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxSolverConfigsCreate(BaseModel):
    solver_config_id: uuid.UUID
    solver_type: str
    solver_name: str
    parameters: Optional[dict] = None
    version: Optional[str] = None
    is_active: bool = True

class TaxSolverConfigsUpdate(BaseModel):
    solver_config_id: Optional[uuid.UUID] = None
    solver_type: Optional[str] = None
    solver_name: Optional[str] = None
    parameters: Optional[dict] = None
    version: Optional[str] = None
    is_active: Optional[bool] = None

class TaxSolverConfigsOut(BaseModel):
    solver_config_id: uuid.UUID
    solver_type: str
    solver_name: str
    parameters: Optional[dict] = None
    version: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxStatusesCreate(BaseModel):
    tax_status_id: uuid.UUID
    tax_regime_id: uuid.UUID
    tax_status_code: str
    tax_status_name: str
    is_recoverable: Optional[bool] = None
    recovery_rate_pct: Optional[float] = None
    is_active: bool = True

class TaxStatusesUpdate(BaseModel):
    tax_status_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_status_code: Optional[str] = None
    tax_status_name: Optional[str] = None
    is_recoverable: Optional[bool] = None
    recovery_rate_pct: Optional[float] = None
    is_active: Optional[bool] = None

class TaxStatusesOut(BaseModel):
    tax_status_id: uuid.UUID
    tax_regime_id: uuid.UUID
    tax_status_code: str
    tax_status_name: str
    is_recoverable: Optional[bool] = None
    recovery_rate_pct: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxTrainingRunsCreate(BaseModel):
    run_id: uuid.UUID
    model_id: uuid.UUID
    run_version: str
    training_data_start: Optional[date] = None
    training_data_end: Optional[date] = None
    training_duration_sec: Optional[int] = None
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    model_artifact_url: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxTrainingRunsUpdate(BaseModel):
    run_id: Optional[uuid.UUID] = None
    model_id: Optional[uuid.UUID] = None
    run_version: Optional[str] = None
    training_data_start: Optional[date] = None
    training_data_end: Optional[date] = None
    training_duration_sec: Optional[int] = None
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    model_artifact_url: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxTrainingRunsOut(BaseModel):
    run_id: uuid.UUID
    model_id: uuid.UUID
    run_version: str
    training_data_start: Optional[date] = None
    training_data_end: Optional[date] = None
    training_duration_sec: Optional[int] = None
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    model_artifact_url: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxTransactionsCreate(BaseModel):
    tax_transaction_id: uuid.UUID
    company_id: Optional[uuid.UUID] = None
    bu_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    tax_rate_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_status_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    source_module: str
    source_doc_id: uuid.UUID
    source_line_id: Optional[uuid.UUID] = None
    doc_number: str
    tax_date: date
    base_amount: float
    tax_amount: float
    recoverable_tax_amount: Optional[float] = None
    non_recoverable_tax_amount: Optional[float] = None
    tax_period: str
    status: Optional[str] = None
    tax_return_id: Optional[uuid.UUID] = None
    filing_date: Optional[date] = None
    attribute_category: Optional[str] = None
    attribute1: Optional[str] = None
    attribute2: Optional[str] = None
    attribute3: Optional[str] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxTransactionsUpdate(BaseModel):
    tax_transaction_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    bu_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    tax_rate_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_status_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    source_module: Optional[str] = None
    source_doc_id: Optional[uuid.UUID] = None
    source_line_id: Optional[uuid.UUID] = None
    doc_number: Optional[str] = None
    tax_date: Optional[date] = None
    base_amount: Optional[float] = None
    tax_amount: Optional[float] = None
    recoverable_tax_amount: Optional[float] = None
    non_recoverable_tax_amount: Optional[float] = None
    tax_period: Optional[str] = None
    status: Optional[str] = None
    tax_return_id: Optional[uuid.UUID] = None
    filing_date: Optional[date] = None
    attribute_category: Optional[str] = None
    attribute1: Optional[str] = None
    attribute2: Optional[str] = None
    attribute3: Optional[str] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class TaxTransactionsOut(BaseModel):
    tax_transaction_id: uuid.UUID
    company_id: Optional[uuid.UUID] = None
    bu_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    tax_rate_id: Optional[uuid.UUID] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_status_id: Optional[uuid.UUID] = None
    tax_jurisdiction_id: Optional[uuid.UUID] = None
    source_module: str
    source_doc_id: uuid.UUID
    source_line_id: Optional[uuid.UUID] = None
    doc_number: str
    tax_date: date
    base_amount: float
    tax_amount: float
    recoverable_tax_amount: Optional[float] = None
    non_recoverable_tax_amount: Optional[float] = None
    tax_period: str
    status: Optional[str] = None
    tax_return_id: Optional[uuid.UUID] = None
    filing_date: Optional[date] = None
    attribute_category: Optional[str] = None
    attribute1: Optional[str] = None
    attribute2: Optional[str] = None
    attribute3: Optional[str] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxTransferPricingAdjustmentsCreate(BaseModel):
    adjustment_id: uuid.UUID
    study_id: Optional[uuid.UUID] = None
    entity_id: Optional[uuid.UUID] = None
    adjustment_type: str
    adjustment_amount: float
    currency_code: Optional[str] = None
    adjustment_reason: Optional[str] = None
    is_active: bool = True

class TaxTransferPricingAdjustmentsUpdate(BaseModel):
    adjustment_id: Optional[uuid.UUID] = None
    study_id: Optional[uuid.UUID] = None
    entity_id: Optional[uuid.UUID] = None
    adjustment_type: Optional[str] = None
    adjustment_amount: Optional[float] = None
    currency_code: Optional[str] = None
    adjustment_reason: Optional[str] = None
    is_active: Optional[bool] = None

class TaxTransferPricingAdjustmentsOut(BaseModel):
    adjustment_id: uuid.UUID
    study_id: Optional[uuid.UUID] = None
    entity_id: Optional[uuid.UUID] = None
    adjustment_type: str
    adjustment_amount: float
    currency_code: Optional[str] = None
    adjustment_reason: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxTransferPricingPoliciesCreate(BaseModel):
    policy_id: uuid.UUID
    policy_code: str
    policy_name: str
    method: str
    description: Optional[str] = None
    effective_from: date
    effective_to: Optional[date] = None
    is_active: bool = True

class TaxTransferPricingPoliciesUpdate(BaseModel):
    policy_id: Optional[uuid.UUID] = None
    policy_code: Optional[str] = None
    policy_name: Optional[str] = None
    method: Optional[str] = None
    description: Optional[str] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    is_active: Optional[bool] = None

class TaxTransferPricingPoliciesOut(BaseModel):
    policy_id: uuid.UUID
    policy_code: str
    policy_name: str
    method: str
    description: Optional[str] = None
    effective_from: date
    effective_to: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxTransferPricingStudiesCreate(BaseModel):
    study_id: uuid.UUID
    policy_id: Optional[uuid.UUID] = None
    study_name: str
    tax_year: int
    jurisdiction: Optional[str] = None
    analysis_data: Optional[dict] = None
    arm_length_range_min: Optional[float] = None
    arm_length_range_max: Optional[float] = None
    selected_margin: Optional[float] = None
    documentation_url: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxTransferPricingStudiesUpdate(BaseModel):
    study_id: Optional[uuid.UUID] = None
    policy_id: Optional[uuid.UUID] = None
    study_name: Optional[str] = None
    tax_year: Optional[int] = None
    jurisdiction: Optional[str] = None
    analysis_data: Optional[dict] = None
    arm_length_range_min: Optional[float] = None
    arm_length_range_max: Optional[float] = None
    selected_margin: Optional[float] = None
    documentation_url: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxTransferPricingStudiesOut(BaseModel):
    study_id: uuid.UUID
    policy_id: Optional[uuid.UUID] = None
    study_name: str
    tax_year: int
    jurisdiction: Optional[str] = None
    analysis_data: Optional[dict] = None
    arm_length_range_min: Optional[float] = None
    arm_length_range_max: Optional[float] = None
    selected_margin: Optional[float] = None
    documentation_url: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxTypesCreate(BaseModel):
    tax_type_id: uuid.UUID
    country_code: Optional[str] = None
    tax_type_code: str
    tax_type_name: str
    tax_regime_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    is_active: bool = True
    category: Optional[str] = None
    accounting_treatment: Optional[str] = None
    is_recoverable: Optional[bool] = None
    recovery_rate_pct: Optional[float] = None
    rounding_rule: Optional[str] = None

class TaxTypesUpdate(BaseModel):
    tax_type_id: Optional[uuid.UUID] = None
    country_code: Optional[str] = None
    tax_type_code: Optional[str] = None
    tax_type_name: Optional[str] = None
    tax_regime_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    category: Optional[str] = None
    accounting_treatment: Optional[str] = None
    is_recoverable: Optional[bool] = None
    recovery_rate_pct: Optional[float] = None
    rounding_rule: Optional[str] = None

class TaxTypesOut(BaseModel):
    tax_type_id: uuid.UUID
    country_code: Optional[str] = None
    tax_type_code: str
    tax_type_name: str
    tax_regime_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    is_active: bool
    category: Optional[str] = None
    accounting_treatment: Optional[str] = None
    is_recoverable: Optional[bool] = None
    recovery_rate_pct: Optional[float] = None
    rounding_rule: Optional[str] = None
    model_config = {"from_attributes": True}

class TaxVectorDocumentsCreate(BaseModel):
    vector_doc_id: uuid.UUID
    document_type: str
    title: str
    content: str
    meta_data: Optional[dict] = None
    embedding_model: Optional[str] = None
    is_active: bool = True

class TaxVectorDocumentsUpdate(BaseModel):
    vector_doc_id: Optional[uuid.UUID] = None
    document_type: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    meta_data: Optional[dict] = None
    embedding_model: Optional[str] = None
    is_active: Optional[bool] = None

class TaxVectorDocumentsOut(BaseModel):
    vector_doc_id: uuid.UUID
    document_type: str
    title: str
    content: str
    meta_data: Optional[dict] = None
    embedding_model: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxWithholdingCertificatesCreate(BaseModel):
    wht_certificate_id: uuid.UUID
    partner_id: uuid.UUID
    wht_config_id: Optional[uuid.UUID] = None
    certificate_number: str
    certificate_type: Optional[str] = None
    issue_date: date
    tax_year: int
    gross_amount: float
    wht_amount: float
    currency_code: Optional[str] = None
    status: Optional[str] = None
    document_url: Optional[str] = None
    is_active: bool = True

class TaxWithholdingCertificatesUpdate(BaseModel):
    wht_certificate_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    wht_config_id: Optional[uuid.UUID] = None
    certificate_number: Optional[str] = None
    certificate_type: Optional[str] = None
    issue_date: Optional[date] = None
    tax_year: Optional[int] = None
    gross_amount: Optional[float] = None
    wht_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    document_url: Optional[str] = None
    is_active: Optional[bool] = None

class TaxWithholdingCertificatesOut(BaseModel):
    wht_certificate_id: uuid.UUID
    partner_id: uuid.UUID
    wht_config_id: Optional[uuid.UUID] = None
    certificate_number: str
    certificate_type: Optional[str] = None
    issue_date: date
    tax_year: int
    gross_amount: float
    wht_amount: float
    currency_code: Optional[str] = None
    status: Optional[str] = None
    document_url: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxWithholdingConfigsCreate(BaseModel):
    wht_config_id: uuid.UUID
    wht_type: str
    tax_regime_id: Optional[uuid.UUID] = None
    tax_type_id: Optional[uuid.UUID] = None
    wht_code: str
    wht_name: str
    wht_rate_pct: float
    threshold_amount: Optional[float] = None
    minimum_withholding: Optional[float] = None
    effective_from: date
    effective_to: Optional[date] = None
    gl_account_id: Optional[uuid.UUID] = None
    is_active: bool = True

class TaxWithholdingConfigsUpdate(BaseModel):
    wht_config_id: Optional[uuid.UUID] = None
    wht_type: Optional[str] = None
    tax_regime_id: Optional[uuid.UUID] = None
    tax_type_id: Optional[uuid.UUID] = None
    wht_code: Optional[str] = None
    wht_name: Optional[str] = None
    wht_rate_pct: Optional[float] = None
    threshold_amount: Optional[float] = None
    minimum_withholding: Optional[float] = None
    effective_from: Optional[date] = None
    effective_to: Optional[date] = None
    gl_account_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None

class TaxWithholdingConfigsOut(BaseModel):
    wht_config_id: uuid.UUID
    wht_type: str
    tax_regime_id: Optional[uuid.UUID] = None
    tax_type_id: Optional[uuid.UUID] = None
    wht_code: str
    wht_name: str
    wht_rate_pct: float
    threshold_amount: Optional[float] = None
    minimum_withholding: Optional[float] = None
    effective_from: date
    effective_to: Optional[date] = None
    gl_account_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxWithholdingPaymentsCreate(BaseModel):
    wht_payment_id: uuid.UUID
    tax_authority_id: Optional[uuid.UUID] = None
    tax_period: str
    payment_amount: float
    payment_date: date
    payment_method: Optional[str] = None
    reference_number: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True

class TaxWithholdingPaymentsUpdate(BaseModel):
    wht_payment_id: Optional[uuid.UUID] = None
    tax_authority_id: Optional[uuid.UUID] = None
    tax_period: Optional[str] = None
    payment_amount: Optional[float] = None
    payment_date: Optional[date] = None
    payment_method: Optional[str] = None
    reference_number: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None

class TaxWithholdingPaymentsOut(BaseModel):
    wht_payment_id: uuid.UUID
    tax_authority_id: Optional[uuid.UUID] = None
    tax_period: str
    payment_amount: float
    payment_date: date
    payment_method: Optional[str] = None
    reference_number: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}
