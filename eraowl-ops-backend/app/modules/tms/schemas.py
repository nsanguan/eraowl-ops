import uuid
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class AccessorialChargesCreate(BaseModel):
    accessorial_charges_id: uuid.UUID
    charge_code: str
    charge_name: str
    charge_type: str
    description: Optional[str] = None
    default_amount: Optional[float] = None
    default_basis: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class AccessorialChargesUpdate(BaseModel):
    accessorial_charges_id: Optional[uuid.UUID] = None
    charge_code: Optional[str] = None
    charge_name: Optional[str] = None
    charge_type: Optional[str] = None
    description: Optional[str] = None
    default_amount: Optional[float] = None
    default_basis: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class AccessorialChargesOut(BaseModel):
    accessorial_charges_id: uuid.UUID
    charge_code: str
    charge_name: str
    charge_type: str
    description: Optional[str] = None
    default_amount: Optional[float] = None
    default_basis: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class AccessorialRateLinesCreate(BaseModel):
    accessorial_rate_lines_id: uuid.UUID
    rate_chart_version_id: uuid.UUID
    accessorial_charge_id: uuid.UUID
    amount: float
    basis: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class AccessorialRateLinesUpdate(BaseModel):
    accessorial_rate_lines_id: Optional[uuid.UUID] = None
    rate_chart_version_id: Optional[uuid.UUID] = None
    accessorial_charge_id: Optional[uuid.UUID] = None
    amount: Optional[float] = None
    basis: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class AccessorialRateLinesOut(BaseModel):
    accessorial_rate_lines_id: uuid.UUID
    rate_chart_version_id: uuid.UUID
    accessorial_charge_id: uuid.UUID
    amount: float
    basis: Optional[str] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class AiAgentLogsCreate(BaseModel):
    ai_agent_logs_id: uuid.UUID
    agent_name: str
    agent_type: str
    session_id: Optional[uuid.UUID] = None
    workflow_state_id: Optional[uuid.UUID] = None
    log_level: Optional[str] = None
    message: str
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    model_id: Optional[str] = None
    tokens_used: Optional[int] = None
    cost_estimate: Optional[float] = None
    status: Optional[str] = None
    error_detail: Optional[str] = None
    tenant_id: Optional[str] = None

class AiAgentLogsUpdate(BaseModel):
    ai_agent_logs_id: Optional[uuid.UUID] = None
    agent_name: Optional[str] = None
    agent_type: Optional[str] = None
    session_id: Optional[uuid.UUID] = None
    workflow_state_id: Optional[uuid.UUID] = None
    log_level: Optional[str] = None
    message: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    model_id: Optional[str] = None
    tokens_used: Optional[int] = None
    cost_estimate: Optional[float] = None
    status: Optional[str] = None
    error_detail: Optional[str] = None
    tenant_id: Optional[str] = None

class AiAgentLogsOut(BaseModel):
    ai_agent_logs_id: uuid.UUID
    agent_name: str
    agent_type: str
    session_id: Optional[uuid.UUID] = None
    workflow_state_id: Optional[uuid.UUID] = None
    log_level: Optional[str] = None
    message: str
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    execution_time_ms: Optional[int] = None
    model_id: Optional[str] = None
    tokens_used: Optional[int] = None
    cost_estimate: Optional[float] = None
    status: Optional[str] = None
    error_detail: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    model_config = {"from_attributes": True}

class AiDecisionsCreate(BaseModel):
    ai_decisions_id: uuid.UUID
    decision_type: str
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    input_features: Optional[dict] = None
    prediction: Optional[dict] = None
    explanation: Optional[str] = None
    confidence: Optional[float] = None
    model_version: Optional[str] = None
    is_overridden: Optional[bool] = None
    overridden_by: Optional[uuid.UUID] = None
    overridden_at: Optional[datetime] = None
    override_reason: Optional[str] = None
    feedback_type: Optional[str] = None
    feedback: Optional[str] = None
    status: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class AiDecisionsUpdate(BaseModel):
    ai_decisions_id: Optional[uuid.UUID] = None
    decision_type: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    input_features: Optional[dict] = None
    prediction: Optional[dict] = None
    explanation: Optional[str] = None
    confidence: Optional[float] = None
    model_version: Optional[str] = None
    is_overridden: Optional[bool] = None
    overridden_by: Optional[uuid.UUID] = None
    overridden_at: Optional[datetime] = None
    override_reason: Optional[str] = None
    feedback_type: Optional[str] = None
    feedback: Optional[str] = None
    status: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class AiDecisionsOut(BaseModel):
    ai_decisions_id: uuid.UUID
    decision_type: str
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    input_features: Optional[dict] = None
    prediction: Optional[dict] = None
    explanation: Optional[str] = None
    confidence: Optional[float] = None
    model_version: Optional[str] = None
    is_overridden: Optional[bool] = None
    overridden_by: Optional[uuid.UUID] = None
    overridden_at: Optional[datetime] = None
    override_reason: Optional[str] = None
    feedback_type: Optional[str] = None
    feedback: Optional[str] = None
    status: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class AiWorkflowStateCreate(BaseModel):
    ai_workflow_state_id: uuid.UUID
    workflow_name: str
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    state_type: str
    state_data: Optional[dict] = None
    context_data: Optional[dict] = None
    confidence_score: Optional[float] = None
    status: Optional[str] = None
    completed_at: Optional[datetime] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class AiWorkflowStateUpdate(BaseModel):
    ai_workflow_state_id: Optional[uuid.UUID] = None
    workflow_name: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    state_type: Optional[str] = None
    state_data: Optional[dict] = None
    context_data: Optional[dict] = None
    confidence_score: Optional[float] = None
    status: Optional[str] = None
    completed_at: Optional[datetime] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class AiWorkflowStateOut(BaseModel):
    ai_workflow_state_id: uuid.UUID
    workflow_name: str
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    state_type: str
    state_data: Optional[dict] = None
    context_data: Optional[dict] = None
    confidence_score: Optional[float] = None
    status: Optional[str] = None
    completed_at: Optional[datetime] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CarrierAddressesCreate(BaseModel):
    carrier_addresses_id: uuid.UUID
    carrier_id: uuid.UUID
    address_type: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    is_primary: Optional[bool] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class CarrierAddressesUpdate(BaseModel):
    carrier_addresses_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    address_type: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    is_primary: Optional[bool] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class CarrierAddressesOut(BaseModel):
    carrier_addresses_id: uuid.UUID
    carrier_id: uuid.UUID
    address_type: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    is_primary: Optional[bool] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CarrierCertificationsCreate(BaseModel):
    carrier_certifications_id: uuid.UUID
    carrier_id: uuid.UUID
    certification_type: str
    certification_number: Optional[str] = None
    issuing_authority: Optional[str] = None
    issue_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class CarrierCertificationsUpdate(BaseModel):
    carrier_certifications_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    certification_type: Optional[str] = None
    certification_number: Optional[str] = None
    issuing_authority: Optional[str] = None
    issue_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class CarrierCertificationsOut(BaseModel):
    carrier_certifications_id: uuid.UUID
    carrier_id: uuid.UUID
    certification_type: str
    certification_number: Optional[str] = None
    issuing_authority: Optional[str] = None
    issue_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CarrierContactsCreate(BaseModel):
    carrier_contacts_id: uuid.UUID
    carrier_id: uuid.UUID
    contact_type: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    title: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    mobile_phone: Optional[str] = None
    fax: Optional[str] = None
    is_primary: Optional[bool] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class CarrierContactsUpdate(BaseModel):
    carrier_contacts_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    contact_type: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    title: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    mobile_phone: Optional[str] = None
    fax: Optional[str] = None
    is_primary: Optional[bool] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class CarrierContactsOut(BaseModel):
    carrier_contacts_id: uuid.UUID
    carrier_id: uuid.UUID
    contact_type: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    title: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    mobile_phone: Optional[str] = None
    fax: Optional[str] = None
    is_primary: Optional[bool] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CarrierContractsCreate(BaseModel):
    carrier_contracts_id: uuid.UUID
    carrier_id: uuid.UUID
    contract_number: str
    contract_name: Optional[str] = None
    contract_type: Optional[str] = None
    effective_date: date
    expiration_date: Optional[date] = None
    terms: Optional[str] = None
    status: Optional[str] = None
    auto_renew: Optional[bool] = None
    pdf_url: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class CarrierContractsUpdate(BaseModel):
    carrier_contracts_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    contract_number: Optional[str] = None
    contract_name: Optional[str] = None
    contract_type: Optional[str] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    terms: Optional[str] = None
    status: Optional[str] = None
    auto_renew: Optional[bool] = None
    pdf_url: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class CarrierContractsOut(BaseModel):
    carrier_contracts_id: uuid.UUID
    carrier_id: uuid.UUID
    contract_number: str
    contract_name: Optional[str] = None
    contract_type: Optional[str] = None
    effective_date: date
    expiration_date: Optional[date] = None
    terms: Optional[str] = None
    status: Optional[str] = None
    auto_renew: Optional[bool] = None
    pdf_url: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CarrierEdiCapabilitiesCreate(BaseModel):
    carrier_edi_capabilities_id: uuid.UUID
    carrier_id: uuid.UUID
    edi_type: str
    edi_version: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class CarrierEdiCapabilitiesUpdate(BaseModel):
    carrier_edi_capabilities_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    edi_type: Optional[str] = None
    edi_version: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class CarrierEdiCapabilitiesOut(BaseModel):
    carrier_edi_capabilities_id: uuid.UUID
    carrier_id: uuid.UUID
    edi_type: str
    edi_version: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CarrierEquipmentCreate(BaseModel):
    carrier_equipment_id: uuid.UUID
    carrier_id: uuid.UUID
    equipment_type_id: Optional[uuid.UUID] = None
    unit_number: str
    vin: Optional[str] = None
    license_plate: Optional[str] = None
    license_state: Optional[str] = None
    year: Optional[int] = None
    make: Optional[str] = None
    model: Optional[str] = None
    owned_leased: Optional[str] = None
    purchase_date: Optional[date] = None
    lease_expiration: Optional[date] = None
    status: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class CarrierEquipmentUpdate(BaseModel):
    carrier_equipment_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    equipment_type_id: Optional[uuid.UUID] = None
    unit_number: Optional[str] = None
    vin: Optional[str] = None
    license_plate: Optional[str] = None
    license_state: Optional[str] = None
    year: Optional[int] = None
    make: Optional[str] = None
    model: Optional[str] = None
    owned_leased: Optional[str] = None
    purchase_date: Optional[date] = None
    lease_expiration: Optional[date] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class CarrierEquipmentOut(BaseModel):
    carrier_equipment_id: uuid.UUID
    carrier_id: uuid.UUID
    equipment_type_id: Optional[uuid.UUID] = None
    unit_number: str
    vin: Optional[str] = None
    license_plate: Optional[str] = None
    license_state: Optional[str] = None
    year: Optional[int] = None
    make: Optional[str] = None
    model: Optional[str] = None
    owned_leased: Optional[str] = None
    purchase_date: Optional[date] = None
    lease_expiration: Optional[date] = None
    status: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CarrierEquipmentTypesCreate(BaseModel):
    carrier_equipment_types_id: uuid.UUID
    carrier_id: uuid.UUID
    equipment_type_code: str
    equipment_type_name: str
    description: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class CarrierEquipmentTypesUpdate(BaseModel):
    carrier_equipment_types_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    equipment_type_code: Optional[str] = None
    equipment_type_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class CarrierEquipmentTypesOut(BaseModel):
    carrier_equipment_types_id: uuid.UUID
    carrier_id: uuid.UUID
    equipment_type_code: str
    equipment_type_name: str
    description: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CarrierInsuranceCreate(BaseModel):
    carrier_insurance_id: uuid.UUID
    carrier_id: uuid.UUID
    insurance_type: str
    policy_number: Optional[str] = None
    provider: Optional[str] = None
    coverage_amount: Optional[float] = None
    deductible_amount: Optional[float] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class CarrierInsuranceUpdate(BaseModel):
    carrier_insurance_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    insurance_type: Optional[str] = None
    policy_number: Optional[str] = None
    provider: Optional[str] = None
    coverage_amount: Optional[float] = None
    deductible_amount: Optional[float] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class CarrierInsuranceOut(BaseModel):
    carrier_insurance_id: uuid.UUID
    carrier_id: uuid.UUID
    insurance_type: str
    policy_number: Optional[str] = None
    provider: Optional[str] = None
    coverage_amount: Optional[float] = None
    deductible_amount: Optional[float] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CarrierPerformanceCreate(BaseModel):
    carrier_performance_id: uuid.UUID
    carrier_id: uuid.UUID
    period_start: date
    period_end: date
    on_time_delivery_pct: Optional[float] = None
    on_time_pickup_pct: Optional[float] = None
    service_failure_count: Optional[int] = None
    damage_claim_count: Optional[int] = None
    total_shipments: Optional[int] = None
    avg_transit_days: Optional[float] = None
    tender_acceptance_pct: Optional[float] = None
    score: Optional[float] = None
    score_category: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class CarrierPerformanceUpdate(BaseModel):
    carrier_performance_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    period_start: Optional[date] = None
    period_end: Optional[date] = None
    on_time_delivery_pct: Optional[float] = None
    on_time_pickup_pct: Optional[float] = None
    service_failure_count: Optional[int] = None
    damage_claim_count: Optional[int] = None
    total_shipments: Optional[int] = None
    avg_transit_days: Optional[float] = None
    tender_acceptance_pct: Optional[float] = None
    score: Optional[float] = None
    score_category: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class CarrierPerformanceOut(BaseModel):
    carrier_performance_id: uuid.UUID
    carrier_id: uuid.UUID
    period_start: date
    period_end: date
    on_time_delivery_pct: Optional[float] = None
    on_time_pickup_pct: Optional[float] = None
    service_failure_count: Optional[int] = None
    damage_claim_count: Optional[int] = None
    total_shipments: Optional[int] = None
    avg_transit_days: Optional[float] = None
    tender_acceptance_pct: Optional[float] = None
    score: Optional[float] = None
    score_category: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CarrierServiceLevelsCreate(BaseModel):
    carrier_service_levels_id: uuid.UUID
    carrier_service_id: uuid.UUID
    level_code: str
    level_name: str
    transit_days_min: Optional[int] = None
    transit_days_max: Optional[int] = None
    weight_min: Optional[float] = None
    weight_max: Optional[float] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class CarrierServiceLevelsUpdate(BaseModel):
    carrier_service_levels_id: Optional[uuid.UUID] = None
    carrier_service_id: Optional[uuid.UUID] = None
    level_code: Optional[str] = None
    level_name: Optional[str] = None
    transit_days_min: Optional[int] = None
    transit_days_max: Optional[int] = None
    weight_min: Optional[float] = None
    weight_max: Optional[float] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class CarrierServiceLevelsOut(BaseModel):
    carrier_service_levels_id: uuid.UUID
    carrier_service_id: uuid.UUID
    level_code: str
    level_name: str
    transit_days_min: Optional[int] = None
    transit_days_max: Optional[int] = None
    weight_min: Optional[float] = None
    weight_max: Optional[float] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CarrierServicesCreate(BaseModel):
    carrier_services_id: uuid.UUID
    carrier_id: uuid.UUID
    service_code: str
    service_name: str
    description: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class CarrierServicesUpdate(BaseModel):
    carrier_services_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    service_code: Optional[str] = None
    service_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class CarrierServicesOut(BaseModel):
    carrier_services_id: uuid.UUID
    carrier_id: uuid.UUID
    service_code: str
    service_name: str
    description: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CarriersCreate(BaseModel):
    carriers_id: uuid.UUID
    carrier_code: str
    carrier_name: str
    carrier_type: Optional[str] = None
    mc_number: Optional[str] = None
    dot_number: Optional[str] = None
    scac: Optional[str] = None
    tax_id: Optional[str] = None
    website: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class CarriersUpdate(BaseModel):
    carriers_id: Optional[uuid.UUID] = None
    carrier_code: Optional[str] = None
    carrier_name: Optional[str] = None
    carrier_type: Optional[str] = None
    mc_number: Optional[str] = None
    dot_number: Optional[str] = None
    scac: Optional[str] = None
    tax_id: Optional[str] = None
    website: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class CarriersOut(BaseModel):
    carriers_id: uuid.UUID
    carrier_code: str
    carrier_name: str
    carrier_type: Optional[str] = None
    mc_number: Optional[str] = None
    dot_number: Optional[str] = None
    scac: Optional[str] = None
    tax_id: Optional[str] = None
    website: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CertificatesOfOriginCreate(BaseModel):
    certificates_of_origin_id: uuid.UUID
    certificate_number: str
    shipment_id: Optional[uuid.UUID] = None
    customs_declaration_id: Optional[uuid.UUID] = None
    exporter_name: str
    exporter_address: Optional[str] = None
    consignee_name: str
    consignee_address: Optional[str] = None
    country_of_origin: str
    country_of_destination: str
    issue_date: date
    expiration_date: Optional[date] = None
    certifying_authority: Optional[str] = None
    authorized_signatory: Optional[str] = None
    status: Optional[str] = None
    document_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class CertificatesOfOriginUpdate(BaseModel):
    certificates_of_origin_id: Optional[uuid.UUID] = None
    certificate_number: Optional[str] = None
    shipment_id: Optional[uuid.UUID] = None
    customs_declaration_id: Optional[uuid.UUID] = None
    exporter_name: Optional[str] = None
    exporter_address: Optional[str] = None
    consignee_name: Optional[str] = None
    consignee_address: Optional[str] = None
    country_of_origin: Optional[str] = None
    country_of_destination: Optional[str] = None
    issue_date: Optional[date] = None
    expiration_date: Optional[date] = None
    certifying_authority: Optional[str] = None
    authorized_signatory: Optional[str] = None
    status: Optional[str] = None
    document_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class CertificatesOfOriginOut(BaseModel):
    certificates_of_origin_id: uuid.UUID
    certificate_number: str
    shipment_id: Optional[uuid.UUID] = None
    customs_declaration_id: Optional[uuid.UUID] = None
    exporter_name: str
    exporter_address: Optional[str] = None
    consignee_name: str
    consignee_address: Optional[str] = None
    country_of_origin: str
    country_of_destination: str
    issue_date: date
    expiration_date: Optional[date] = None
    certifying_authority: Optional[str] = None
    authorized_signatory: Optional[str] = None
    status: Optional[str] = None
    document_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ClaimEvidenceCreate(BaseModel):
    claim_evidence_id: uuid.UUID
    claim_id: uuid.UUID
    evidence_type: str
    description: Optional[str] = None
    document_id: Optional[uuid.UUID] = None
    file_url: Optional[str] = None
    provided_by: Optional[str] = None
    provided_date: Optional[date] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class ClaimEvidenceUpdate(BaseModel):
    claim_evidence_id: Optional[uuid.UUID] = None
    claim_id: Optional[uuid.UUID] = None
    evidence_type: Optional[str] = None
    description: Optional[str] = None
    document_id: Optional[uuid.UUID] = None
    file_url: Optional[str] = None
    provided_by: Optional[str] = None
    provided_date: Optional[date] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class ClaimEvidenceOut(BaseModel):
    claim_evidence_id: uuid.UUID
    claim_id: uuid.UUID
    evidence_type: str
    description: Optional[str] = None
    document_id: Optional[uuid.UUID] = None
    file_url: Optional[str] = None
    provided_by: Optional[str] = None
    provided_date: Optional[date] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ClaimLinesCreate(BaseModel):
    claim_lines_id: uuid.UUID
    claim_id: uuid.UUID
    line_number: int
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity_ordered: Optional[float] = None
    quantity_damaged: Optional[float] = None
    quantity_short: Optional[float] = None
    quantity_unit: Optional[str] = None
    unit_value: Optional[float] = None
    amount_claimed: float
    amount_settled: Optional[float] = None
    damage_type: Optional[str] = None
    damage_cause: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ClaimLinesUpdate(BaseModel):
    claim_lines_id: Optional[uuid.UUID] = None
    claim_id: Optional[uuid.UUID] = None
    line_number: Optional[int] = None
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity_ordered: Optional[float] = None
    quantity_damaged: Optional[float] = None
    quantity_short: Optional[float] = None
    quantity_unit: Optional[str] = None
    unit_value: Optional[float] = None
    amount_claimed: Optional[float] = None
    amount_settled: Optional[float] = None
    damage_type: Optional[str] = None
    damage_cause: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ClaimLinesOut(BaseModel):
    claim_lines_id: uuid.UUID
    claim_id: uuid.UUID
    line_number: int
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity_ordered: Optional[float] = None
    quantity_damaged: Optional[float] = None
    quantity_short: Optional[float] = None
    quantity_unit: Optional[str] = None
    unit_value: Optional[float] = None
    amount_claimed: float
    amount_settled: Optional[float] = None
    damage_type: Optional[str] = None
    damage_cause: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ClaimsCreate(BaseModel):
    claims_id: uuid.UUID
    claim_number: str
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    delivery_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    claim_type: str
    claim_date: date
    reported_by: Optional[str] = None
    description: str
    amount_claimed: float
    amount_settled: Optional[float] = None
    amount_paid: Optional[float] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    resolution_notes: Optional[str] = None
    closed_date: Optional[date] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ClaimsUpdate(BaseModel):
    claims_id: Optional[uuid.UUID] = None
    claim_number: Optional[str] = None
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    delivery_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    claim_type: Optional[str] = None
    claim_date: Optional[date] = None
    reported_by: Optional[str] = None
    description: Optional[str] = None
    amount_claimed: Optional[float] = None
    amount_settled: Optional[float] = None
    amount_paid: Optional[float] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    resolution_notes: Optional[str] = None
    closed_date: Optional[date] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ClaimsOut(BaseModel):
    claims_id: uuid.UUID
    claim_number: str
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    delivery_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    claim_type: str
    claim_date: date
    reported_by: Optional[str] = None
    description: str
    amount_claimed: float
    amount_settled: Optional[float] = None
    amount_paid: Optional[float] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    resolution_notes: Optional[str] = None
    closed_date: Optional[date] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ComplianceAccidentsCreate(BaseModel):
    compliance_accidents_id: uuid.UUID
    accident_number: str
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    accident_date: datetime
    accident_type: str
    location_description: Optional[str] = None
    description: str
    injuries_count: Optional[int] = None
    fatalities_count: Optional[int] = None
    vehicles_involved: Optional[int] = None
    property_damage_estimate: Optional[float] = None
    police_report_filed: Optional[bool] = None
    police_report_number: Optional[str] = None
    police_department: Optional[str] = None
    was_ticketed: Optional[bool] = None
    ticket_number: Optional[str] = None
    is_preventable: Optional[bool] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class ComplianceAccidentsUpdate(BaseModel):
    compliance_accidents_id: Optional[uuid.UUID] = None
    accident_number: Optional[str] = None
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    accident_date: Optional[datetime] = None
    accident_type: Optional[str] = None
    location_description: Optional[str] = None
    description: Optional[str] = None
    injuries_count: Optional[int] = None
    fatalities_count: Optional[int] = None
    vehicles_involved: Optional[int] = None
    property_damage_estimate: Optional[float] = None
    police_report_filed: Optional[bool] = None
    police_report_number: Optional[str] = None
    police_department: Optional[str] = None
    was_ticketed: Optional[bool] = None
    ticket_number: Optional[str] = None
    is_preventable: Optional[bool] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class ComplianceAccidentsOut(BaseModel):
    compliance_accidents_id: uuid.UUID
    accident_number: str
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    accident_date: datetime
    accident_type: str
    location_description: Optional[str] = None
    description: str
    injuries_count: Optional[int] = None
    fatalities_count: Optional[int] = None
    vehicles_involved: Optional[int] = None
    property_damage_estimate: Optional[float] = None
    police_report_filed: Optional[bool] = None
    police_report_number: Optional[str] = None
    police_department: Optional[str] = None
    was_ticketed: Optional[bool] = None
    ticket_number: Optional[str] = None
    is_preventable: Optional[bool] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ComplianceDvirCreate(BaseModel):
    compliance_dvir_id: uuid.UUID
    dvir_number: str
    vehicle_id: uuid.UUID
    driver_id: uuid.UUID
    inspection_type: str
    inspection_date: date
    odometer_reading: Optional[int] = None
    engine_hours: Optional[float] = None
    trailer_equipment_id: Optional[uuid.UUID] = None
    results: Optional[str] = None
    is_defect_found: Optional[bool] = None
    defect_description: Optional[str] = None
    corrective_action: Optional[str] = None
    is_driver_ready: Optional[bool] = None
    is_roadworthy: Optional[bool] = None
    mechanic_name: Optional[str] = None
    mechanic_approved_at: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ComplianceDvirUpdate(BaseModel):
    compliance_dvir_id: Optional[uuid.UUID] = None
    dvir_number: Optional[str] = None
    vehicle_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    inspection_type: Optional[str] = None
    inspection_date: Optional[date] = None
    odometer_reading: Optional[int] = None
    engine_hours: Optional[float] = None
    trailer_equipment_id: Optional[uuid.UUID] = None
    results: Optional[str] = None
    is_defect_found: Optional[bool] = None
    defect_description: Optional[str] = None
    corrective_action: Optional[str] = None
    is_driver_ready: Optional[bool] = None
    is_roadworthy: Optional[bool] = None
    mechanic_name: Optional[str] = None
    mechanic_approved_at: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ComplianceDvirOut(BaseModel):
    compliance_dvir_id: uuid.UUID
    dvir_number: str
    vehicle_id: uuid.UUID
    driver_id: uuid.UUID
    inspection_type: str
    inspection_date: date
    odometer_reading: Optional[int] = None
    engine_hours: Optional[float] = None
    trailer_equipment_id: Optional[uuid.UUID] = None
    results: Optional[str] = None
    is_defect_found: Optional[bool] = None
    defect_description: Optional[str] = None
    corrective_action: Optional[str] = None
    is_driver_ready: Optional[bool] = None
    is_roadworthy: Optional[bool] = None
    mechanic_name: Optional[str] = None
    mechanic_approved_at: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ComplianceEldCreate(BaseModel):
    compliance_eld_id: uuid.UUID
    driver_id: uuid.UUID
    vehicle_id: Optional[uuid.UUID] = None
    eld_device_id: Optional[uuid.UUID] = None
    log_date: date
    start_time: datetime
    end_time: Optional[datetime] = None
    driving_time_minutes: Optional[int] = None
    on_duty_time_minutes: Optional[int] = None
    off_duty_time_minutes: Optional[int] = None
    sleeper_berth_time_minutes: Optional[int] = None
    total_miles: Optional[float] = None
    certified: Optional[bool] = None
    certified_at: Optional[datetime] = None
    certified_by: Optional[uuid.UUID] = None
    data_diagnostic_indicator: Optional[bool] = None
    malfunction_indicator: Optional[bool] = None
    source: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ComplianceEldUpdate(BaseModel):
    compliance_eld_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    eld_device_id: Optional[uuid.UUID] = None
    log_date: Optional[date] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    driving_time_minutes: Optional[int] = None
    on_duty_time_minutes: Optional[int] = None
    off_duty_time_minutes: Optional[int] = None
    sleeper_berth_time_minutes: Optional[int] = None
    total_miles: Optional[float] = None
    certified: Optional[bool] = None
    certified_at: Optional[datetime] = None
    certified_by: Optional[uuid.UUID] = None
    data_diagnostic_indicator: Optional[bool] = None
    malfunction_indicator: Optional[bool] = None
    source: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ComplianceEldOut(BaseModel):
    compliance_eld_id: uuid.UUID
    driver_id: uuid.UUID
    vehicle_id: Optional[uuid.UUID] = None
    eld_device_id: Optional[uuid.UUID] = None
    log_date: date
    start_time: datetime
    end_time: Optional[datetime] = None
    driving_time_minutes: Optional[int] = None
    on_duty_time_minutes: Optional[int] = None
    off_duty_time_minutes: Optional[int] = None
    sleeper_berth_time_minutes: Optional[int] = None
    total_miles: Optional[float] = None
    certified: Optional[bool] = None
    certified_at: Optional[datetime] = None
    certified_by: Optional[uuid.UUID] = None
    data_diagnostic_indicator: Optional[bool] = None
    malfunction_indicator: Optional[bool] = None
    source: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ComplianceIftaCreate(BaseModel):
    compliance_ifta_id: uuid.UUID
    license_plate: str
    license_state: str
    vehicle_id: Optional[uuid.UUID] = None
    report_quarter: str
    report_year: int
    total_miles: float
    total_gallons: float
    jurisdiction: Optional[str] = None
    jurisdiction_miles: Optional[float] = None
    jurisdiction_gallons: Optional[float] = None
    tax_due: Optional[float] = None
    tax_paid: Optional[float] = None
    net_tax: Optional[float] = None
    status: Optional[str] = None
    filing_date: Optional[date] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class ComplianceIftaUpdate(BaseModel):
    compliance_ifta_id: Optional[uuid.UUID] = None
    license_plate: Optional[str] = None
    license_state: Optional[str] = None
    vehicle_id: Optional[uuid.UUID] = None
    report_quarter: Optional[str] = None
    report_year: Optional[int] = None
    total_miles: Optional[float] = None
    total_gallons: Optional[float] = None
    jurisdiction: Optional[str] = None
    jurisdiction_miles: Optional[float] = None
    jurisdiction_gallons: Optional[float] = None
    tax_due: Optional[float] = None
    tax_paid: Optional[float] = None
    net_tax: Optional[float] = None
    status: Optional[str] = None
    filing_date: Optional[date] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class ComplianceIftaOut(BaseModel):
    compliance_ifta_id: uuid.UUID
    license_plate: str
    license_state: str
    vehicle_id: Optional[uuid.UUID] = None
    report_quarter: str
    report_year: int
    total_miles: float
    total_gallons: float
    jurisdiction: Optional[str] = None
    jurisdiction_miles: Optional[float] = None
    jurisdiction_gallons: Optional[float] = None
    tax_due: Optional[float] = None
    tax_paid: Optional[float] = None
    net_tax: Optional[float] = None
    status: Optional[str] = None
    filing_date: Optional[date] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ComplianceViolationsCreate(BaseModel):
    compliance_violations_id: uuid.UUID
    violation_number: str
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    violation_date: date
    violation_type: str
    violation_code: Optional[str] = None
    description: str
    location: Optional[str] = None
    issuing_authority: Optional[str] = None
    fine_amount: Optional[float] = None
    currency: Optional[str] = None
    points: Optional[int] = None
    is_preventable: Optional[bool] = None
    status: Optional[str] = None
    resolution_notes: Optional[str] = None
    resolved_date: Optional[date] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class ComplianceViolationsUpdate(BaseModel):
    compliance_violations_id: Optional[uuid.UUID] = None
    violation_number: Optional[str] = None
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    violation_date: Optional[date] = None
    violation_type: Optional[str] = None
    violation_code: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    issuing_authority: Optional[str] = None
    fine_amount: Optional[float] = None
    currency: Optional[str] = None
    points: Optional[int] = None
    is_preventable: Optional[bool] = None
    status: Optional[str] = None
    resolution_notes: Optional[str] = None
    resolved_date: Optional[date] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class ComplianceViolationsOut(BaseModel):
    compliance_violations_id: uuid.UUID
    violation_number: str
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    violation_date: date
    violation_type: str
    violation_code: Optional[str] = None
    description: str
    location: Optional[str] = None
    issuing_authority: Optional[str] = None
    fine_amount: Optional[float] = None
    currency: Optional[str] = None
    points: Optional[int] = None
    is_preventable: Optional[bool] = None
    status: Optional[str] = None
    resolution_notes: Optional[str] = None
    resolved_date: Optional[date] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ContainerSealsCreate(BaseModel):
    container_seals_id: uuid.UUID
    container_id: uuid.UUID
    seal_number: str
    seal_type: Optional[str] = None
    affixed_by: Optional[str] = None
    affixed_date: Optional[datetime] = None
    removed_date: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class ContainerSealsUpdate(BaseModel):
    container_seals_id: Optional[uuid.UUID] = None
    container_id: Optional[uuid.UUID] = None
    seal_number: Optional[str] = None
    seal_type: Optional[str] = None
    affixed_by: Optional[str] = None
    affixed_date: Optional[datetime] = None
    removed_date: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class ContainerSealsOut(BaseModel):
    container_seals_id: uuid.UUID
    container_id: uuid.UUID
    seal_number: str
    seal_type: Optional[str] = None
    affixed_by: Optional[str] = None
    affixed_date: Optional[datetime] = None
    removed_date: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ContainersCreate(BaseModel):
    containers_id: uuid.UUID
    container_number: str
    container_type: Optional[str] = None
    size_code: Optional[str] = None
    iso_code: Optional[str] = None
    owner: Optional[str] = None
    operator: Optional[str] = None
    tare_weight: Optional[float] = None
    max_gross_weight: Optional[float] = None
    max_payload: Optional[float] = None
    status: Optional[str] = None
    last_inspection_date: Optional[date] = None
    next_inspection_date: Optional[date] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class ContainersUpdate(BaseModel):
    containers_id: Optional[uuid.UUID] = None
    container_number: Optional[str] = None
    container_type: Optional[str] = None
    size_code: Optional[str] = None
    iso_code: Optional[str] = None
    owner: Optional[str] = None
    operator: Optional[str] = None
    tare_weight: Optional[float] = None
    max_gross_weight: Optional[float] = None
    max_payload: Optional[float] = None
    status: Optional[str] = None
    last_inspection_date: Optional[date] = None
    next_inspection_date: Optional[date] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class ContainersOut(BaseModel):
    containers_id: uuid.UUID
    container_number: str
    container_type: Optional[str] = None
    size_code: Optional[str] = None
    iso_code: Optional[str] = None
    owner: Optional[str] = None
    operator: Optional[str] = None
    tare_weight: Optional[float] = None
    max_gross_weight: Optional[float] = None
    max_payload: Optional[float] = None
    status: Optional[str] = None
    last_inspection_date: Optional[date] = None
    next_inspection_date: Optional[date] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CustomsDeclarationLinesCreate(BaseModel):
    customs_declaration_lines_id: uuid.UUID
    customs_declaration_id: uuid.UUID
    line_number: int
    hs_code_id: Optional[uuid.UUID] = None
    item_description: str
    quantity: float
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    value: Optional[float] = None
    currency: Optional[str] = None
    country_of_origin: Optional[str] = None
    tariff_rate: Optional[float] = None
    duty_amount: Optional[float] = None
    preference_code: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class CustomsDeclarationLinesUpdate(BaseModel):
    customs_declaration_lines_id: Optional[uuid.UUID] = None
    customs_declaration_id: Optional[uuid.UUID] = None
    line_number: Optional[int] = None
    hs_code_id: Optional[uuid.UUID] = None
    item_description: Optional[str] = None
    quantity: Optional[float] = None
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    value: Optional[float] = None
    currency: Optional[str] = None
    country_of_origin: Optional[str] = None
    tariff_rate: Optional[float] = None
    duty_amount: Optional[float] = None
    preference_code: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class CustomsDeclarationLinesOut(BaseModel):
    customs_declaration_lines_id: uuid.UUID
    customs_declaration_id: uuid.UUID
    line_number: int
    hs_code_id: Optional[uuid.UUID] = None
    item_description: str
    quantity: float
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    value: Optional[float] = None
    currency: Optional[str] = None
    country_of_origin: Optional[str] = None
    tariff_rate: Optional[float] = None
    duty_amount: Optional[float] = None
    preference_code: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class CustomsDeclarationsCreate(BaseModel):
    customs_declarations_id: uuid.UUID
    declaration_number: str
    shipment_id: Optional[uuid.UUID] = None
    declaration_type: str
    customs_broker: Optional[str] = None
    broker_reference: Optional[str] = None
    entry_number: Optional[str] = None
    port_of_entry: Optional[str] = None
    port_of_exit: Optional[str] = None
    country_of_origin: Optional[str] = None
    country_of_destination: Optional[str] = None
    incoterm_id: Optional[uuid.UUID] = None
    total_value: Optional[float] = None
    currency: Optional[str] = None
    total_weight: Optional[float] = None
    weight_unit: Optional[str] = None
    total_lines: Optional[int] = None
    declaration_date: Optional[date] = None
    clearance_date: Optional[date] = None
    status: Optional[str] = None
    broker_notes: Optional[str] = None
    officer_notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class CustomsDeclarationsUpdate(BaseModel):
    customs_declarations_id: Optional[uuid.UUID] = None
    declaration_number: Optional[str] = None
    shipment_id: Optional[uuid.UUID] = None
    declaration_type: Optional[str] = None
    customs_broker: Optional[str] = None
    broker_reference: Optional[str] = None
    entry_number: Optional[str] = None
    port_of_entry: Optional[str] = None
    port_of_exit: Optional[str] = None
    country_of_origin: Optional[str] = None
    country_of_destination: Optional[str] = None
    incoterm_id: Optional[uuid.UUID] = None
    total_value: Optional[float] = None
    currency: Optional[str] = None
    total_weight: Optional[float] = None
    weight_unit: Optional[str] = None
    total_lines: Optional[int] = None
    declaration_date: Optional[date] = None
    clearance_date: Optional[date] = None
    status: Optional[str] = None
    broker_notes: Optional[str] = None
    officer_notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class CustomsDeclarationsOut(BaseModel):
    customs_declarations_id: uuid.UUID
    declaration_number: str
    shipment_id: Optional[uuid.UUID] = None
    declaration_type: str
    customs_broker: Optional[str] = None
    broker_reference: Optional[str] = None
    entry_number: Optional[str] = None
    port_of_entry: Optional[str] = None
    port_of_exit: Optional[str] = None
    country_of_origin: Optional[str] = None
    country_of_destination: Optional[str] = None
    incoterm_id: Optional[uuid.UUID] = None
    total_value: Optional[float] = None
    currency: Optional[str] = None
    total_weight: Optional[float] = None
    weight_unit: Optional[str] = None
    total_lines: Optional[int] = None
    declaration_date: Optional[date] = None
    clearance_date: Optional[date] = None
    status: Optional[str] = None
    broker_notes: Optional[str] = None
    officer_notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class DeliveriesCreate(BaseModel):
    deliveries_id: uuid.UUID
    delivery_number: str
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    delivery_date: date
    delivery_type: Optional[str] = None
    status: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    signed_by: Optional[str] = None
    signed_at: Optional[datetime] = None
    recipient_name: Optional[str] = None
    total_packages: Optional[int] = None
    total_weight: Optional[float] = None
    total_pallets: Optional[int] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DeliveriesUpdate(BaseModel):
    deliveries_id: Optional[uuid.UUID] = None
    delivery_number: Optional[str] = None
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    delivery_date: Optional[date] = None
    delivery_type: Optional[str] = None
    status: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    signed_by: Optional[str] = None
    signed_at: Optional[datetime] = None
    recipient_name: Optional[str] = None
    total_packages: Optional[int] = None
    total_weight: Optional[float] = None
    total_pallets: Optional[int] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DeliveriesOut(BaseModel):
    deliveries_id: uuid.UUID
    delivery_number: str
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    delivery_date: date
    delivery_type: Optional[str] = None
    status: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    signed_by: Optional[str] = None
    signed_at: Optional[datetime] = None
    recipient_name: Optional[str] = None
    total_packages: Optional[int] = None
    total_weight: Optional[float] = None
    total_pallets: Optional[int] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class DeliveryLinesCreate(BaseModel):
    delivery_lines_id: uuid.UUID
    delivery_id: uuid.UUID
    shipment_line_id: Optional[uuid.UUID] = None
    line_number: int
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity_ordered: Optional[float] = None
    quantity_delivered: float
    quantity_damaged: Optional[float] = None
    quantity_short: Optional[float] = None
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    condition: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DeliveryLinesUpdate(BaseModel):
    delivery_lines_id: Optional[uuid.UUID] = None
    delivery_id: Optional[uuid.UUID] = None
    shipment_line_id: Optional[uuid.UUID] = None
    line_number: Optional[int] = None
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity_ordered: Optional[float] = None
    quantity_delivered: Optional[float] = None
    quantity_damaged: Optional[float] = None
    quantity_short: Optional[float] = None
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    condition: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DeliveryLinesOut(BaseModel):
    delivery_lines_id: uuid.UUID
    delivery_id: uuid.UUID
    shipment_line_id: Optional[uuid.UUID] = None
    line_number: int
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity_ordered: Optional[float] = None
    quantity_delivered: float
    quantity_damaged: Optional[float] = None
    quantity_short: Optional[float] = None
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    condition: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class DispatchesCreate(BaseModel):
    dispatches_id: uuid.UUID
    dispatch_number: str
    load_id: Optional[uuid.UUID] = None
    trip_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    dispatch_type: Optional[str] = None
    status: Optional[str] = None
    dispatched_at: Optional[datetime] = None
    acknowledged_at: Optional[datetime] = None
    arrived_at_origin: Optional[datetime] = None
    departed_origin: Optional[datetime] = None
    arrived_at_destination: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    instructions: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DispatchesUpdate(BaseModel):
    dispatches_id: Optional[uuid.UUID] = None
    dispatch_number: Optional[str] = None
    load_id: Optional[uuid.UUID] = None
    trip_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    dispatch_type: Optional[str] = None
    status: Optional[str] = None
    dispatched_at: Optional[datetime] = None
    acknowledged_at: Optional[datetime] = None
    arrived_at_origin: Optional[datetime] = None
    departed_origin: Optional[datetime] = None
    arrived_at_destination: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    instructions: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DispatchesOut(BaseModel):
    dispatches_id: uuid.UUID
    dispatch_number: str
    load_id: Optional[uuid.UUID] = None
    trip_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    dispatch_type: Optional[str] = None
    status: Optional[str] = None
    dispatched_at: Optional[datetime] = None
    acknowledged_at: Optional[datetime] = None
    arrived_at_origin: Optional[datetime] = None
    departed_origin: Optional[datetime] = None
    arrived_at_destination: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    instructions: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class DockAppointmentsCreate(BaseModel):
    dock_appointments_id: uuid.UUID
    dock_door_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    appointment_type: str
    scheduled_start: datetime
    scheduled_end: datetime
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DockAppointmentsUpdate(BaseModel):
    dock_appointments_id: Optional[uuid.UUID] = None
    dock_door_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    appointment_type: Optional[str] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DockAppointmentsOut(BaseModel):
    dock_appointments_id: uuid.UUID
    dock_door_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    appointment_type: str
    scheduled_start: datetime
    scheduled_end: datetime
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class DockDoorsCreate(BaseModel):
    dock_doors_id: uuid.UUID
    door_code: str
    door_name: Optional[str] = None
    facility_name: Optional[str] = None
    facility_id: Optional[str] = None
    door_type: Optional[str] = None
    location: Optional[str] = None
    capacity: Optional[int] = None
    current_occupancy: Optional[int] = None
    status: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class DockDoorsUpdate(BaseModel):
    dock_doors_id: Optional[uuid.UUID] = None
    door_code: Optional[str] = None
    door_name: Optional[str] = None
    facility_name: Optional[str] = None
    facility_id: Optional[str] = None
    door_type: Optional[str] = None
    location: Optional[str] = None
    capacity: Optional[int] = None
    current_occupancy: Optional[int] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class DockDoorsOut(BaseModel):
    dock_doors_id: uuid.UUID
    door_code: str
    door_name: Optional[str] = None
    facility_name: Optional[str] = None
    facility_id: Optional[str] = None
    door_type: Optional[str] = None
    location: Optional[str] = None
    capacity: Optional[int] = None
    current_occupancy: Optional[int] = None
    status: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class DocumentDistributionCreate(BaseModel):
    document_distribution_id: uuid.UUID
    document_id: uuid.UUID
    distribution_type: str
    recipient_email: Optional[str] = None
    recipient_name: Optional[str] = None
    sent_at: Optional[datetime] = None
    status: Optional[str] = None
    delivery_method: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class DocumentDistributionUpdate(BaseModel):
    document_distribution_id: Optional[uuid.UUID] = None
    document_id: Optional[uuid.UUID] = None
    distribution_type: Optional[str] = None
    recipient_email: Optional[str] = None
    recipient_name: Optional[str] = None
    sent_at: Optional[datetime] = None
    status: Optional[str] = None
    delivery_method: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class DocumentDistributionOut(BaseModel):
    document_distribution_id: uuid.UUID
    document_id: uuid.UUID
    distribution_type: str
    recipient_email: Optional[str] = None
    recipient_name: Optional[str] = None
    sent_at: Optional[datetime] = None
    status: Optional[str] = None
    delivery_method: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class DocumentTypesCreate(BaseModel):
    document_types_id: uuid.UUID
    document_type_code: str
    document_type_name: str
    description: Optional[str] = None
    retention_days: Optional[int] = None
    is_required: Optional[bool] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class DocumentTypesUpdate(BaseModel):
    document_types_id: Optional[uuid.UUID] = None
    document_type_code: Optional[str] = None
    document_type_name: Optional[str] = None
    description: Optional[str] = None
    retention_days: Optional[int] = None
    is_required: Optional[bool] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class DocumentTypesOut(BaseModel):
    document_types_id: uuid.UUID
    document_type_code: str
    document_type_name: str
    description: Optional[str] = None
    retention_days: Optional[int] = None
    is_required: Optional[bool] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class DocumentsCreate(BaseModel):
    documents_id: uuid.UUID
    document_type_id: uuid.UUID
    document_number: Optional[str] = None
    document_title: Optional[str] = None
    file_name: str
    file_path: Optional[str] = None
    file_url: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    checksum: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    expiration_date: Optional[date] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class DocumentsUpdate(BaseModel):
    documents_id: Optional[uuid.UUID] = None
    document_type_id: Optional[uuid.UUID] = None
    document_number: Optional[str] = None
    document_title: Optional[str] = None
    file_name: Optional[str] = None
    file_path: Optional[str] = None
    file_url: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    checksum: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    expiration_date: Optional[date] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class DocumentsOut(BaseModel):
    documents_id: uuid.UUID
    document_type_id: uuid.UUID
    document_number: Optional[str] = None
    document_title: Optional[str] = None
    file_name: str
    file_path: Optional[str] = None
    file_url: Optional[str] = None
    file_size_bytes: Optional[int] = None
    mime_type: Optional[str] = None
    checksum: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    expiration_date: Optional[date] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class DriverCertificationsCreate(BaseModel):
    driver_certifications_id: uuid.UUID
    driver_id: uuid.UUID
    certification_type: str
    certification_number: Optional[str] = None
    issuing_authority: Optional[str] = None
    issue_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class DriverCertificationsUpdate(BaseModel):
    driver_certifications_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    certification_type: Optional[str] = None
    certification_number: Optional[str] = None
    issuing_authority: Optional[str] = None
    issue_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class DriverCertificationsOut(BaseModel):
    driver_certifications_id: uuid.UUID
    driver_id: uuid.UUID
    certification_type: str
    certification_number: Optional[str] = None
    issuing_authority: Optional[str] = None
    issue_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class DriverHosCreate(BaseModel):
    driver_hos_id: uuid.UUID
    driver_id: uuid.UUID
    log_date: date
    duty_status: str
    status_start_time: datetime
    status_end_time: Optional[datetime] = None
    driving_minutes: Optional[int] = None
    on_duty_minutes: Optional[int] = None
    off_duty_minutes: Optional[int] = None
    sleeper_berth_minutes: Optional[int] = None
    total_miles_driven: Optional[float] = None
    eld_log_id: Optional[str] = None
    source: Optional[str] = None
    is_violation: Optional[bool] = None
    violation_description: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DriverHosUpdate(BaseModel):
    driver_hos_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    log_date: Optional[date] = None
    duty_status: Optional[str] = None
    status_start_time: Optional[datetime] = None
    status_end_time: Optional[datetime] = None
    driving_minutes: Optional[int] = None
    on_duty_minutes: Optional[int] = None
    off_duty_minutes: Optional[int] = None
    sleeper_berth_minutes: Optional[int] = None
    total_miles_driven: Optional[float] = None
    eld_log_id: Optional[str] = None
    source: Optional[str] = None
    is_violation: Optional[bool] = None
    violation_description: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DriverHosOut(BaseModel):
    driver_hos_id: uuid.UUID
    driver_id: uuid.UUID
    log_date: date
    duty_status: str
    status_start_time: datetime
    status_end_time: Optional[datetime] = None
    driving_minutes: Optional[int] = None
    on_duty_minutes: Optional[int] = None
    off_duty_minutes: Optional[int] = None
    sleeper_berth_minutes: Optional[int] = None
    total_miles_driven: Optional[float] = None
    eld_log_id: Optional[str] = None
    source: Optional[str] = None
    is_violation: Optional[bool] = None
    violation_description: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class DriverPayrollCreate(BaseModel):
    driver_payroll_id: uuid.UUID
    driver_id: uuid.UUID
    pay_period_start: date
    pay_period_end: date
    pay_type: str
    pay_rate: Optional[float] = None
    regular_hours: Optional[float] = None
    overtime_hours: Optional[float] = None
    miles_driven: Optional[float] = None
    stops_completed: Optional[int] = None
    loads_completed: Optional[int] = None
    gross_pay: Optional[float] = None
    deductions: Optional[float] = None
    net_pay: Optional[float] = None
    adjustment_amount: Optional[float] = None
    adjustment_reason: Optional[str] = None
    status: Optional[str] = None
    processed_date: Optional[datetime] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DriverPayrollUpdate(BaseModel):
    driver_payroll_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    pay_period_start: Optional[date] = None
    pay_period_end: Optional[date] = None
    pay_type: Optional[str] = None
    pay_rate: Optional[float] = None
    regular_hours: Optional[float] = None
    overtime_hours: Optional[float] = None
    miles_driven: Optional[float] = None
    stops_completed: Optional[int] = None
    loads_completed: Optional[int] = None
    gross_pay: Optional[float] = None
    deductions: Optional[float] = None
    net_pay: Optional[float] = None
    adjustment_amount: Optional[float] = None
    adjustment_reason: Optional[str] = None
    status: Optional[str] = None
    processed_date: Optional[datetime] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DriverPayrollOut(BaseModel):
    driver_payroll_id: uuid.UUID
    driver_id: uuid.UUID
    pay_period_start: date
    pay_period_end: date
    pay_type: str
    pay_rate: Optional[float] = None
    regular_hours: Optional[float] = None
    overtime_hours: Optional[float] = None
    miles_driven: Optional[float] = None
    stops_completed: Optional[int] = None
    loads_completed: Optional[int] = None
    gross_pay: Optional[float] = None
    deductions: Optional[float] = None
    net_pay: Optional[float] = None
    adjustment_amount: Optional[float] = None
    adjustment_reason: Optional[str] = None
    status: Optional[str] = None
    processed_date: Optional[datetime] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class DriverTrainingCreate(BaseModel):
    driver_training_id: uuid.UUID
    driver_id: uuid.UUID
    training_type: str
    training_name: Optional[str] = None
    provider: Optional[str] = None
    completion_date: date
    expiration_date: Optional[date] = None
    score: Optional[float] = None
    certificate_number: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class DriverTrainingUpdate(BaseModel):
    driver_training_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    training_type: Optional[str] = None
    training_name: Optional[str] = None
    provider: Optional[str] = None
    completion_date: Optional[date] = None
    expiration_date: Optional[date] = None
    score: Optional[float] = None
    certificate_number: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class DriverTrainingOut(BaseModel):
    driver_training_id: uuid.UUID
    driver_id: uuid.UUID
    training_type: str
    training_name: Optional[str] = None
    provider: Optional[str] = None
    completion_date: date
    expiration_date: Optional[date] = None
    score: Optional[float] = None
    certificate_number: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class DriversCreate(BaseModel):
    drivers_id: uuid.UUID
    driver_code: str
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    ssn_last_four: Optional[str] = None
    employee_number: Optional[str] = None
    license_number: Optional[str] = None
    license_state: Optional[str] = None
    license_class: Optional[str] = None
    license_endorsements: Optional[str] = None
    license_expiration: Optional[date] = None
    medical_cert_expiration: Optional[date] = None
    hire_date: Optional[date] = None
    termination_date: Optional[date] = None
    status: Optional[str] = None
    driver_type: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    mobile_phone: Optional[str] = None
    home_terminal: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class DriversUpdate(BaseModel):
    drivers_id: Optional[uuid.UUID] = None
    driver_code: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    ssn_last_four: Optional[str] = None
    employee_number: Optional[str] = None
    license_number: Optional[str] = None
    license_state: Optional[str] = None
    license_class: Optional[str] = None
    license_endorsements: Optional[str] = None
    license_expiration: Optional[date] = None
    medical_cert_expiration: Optional[date] = None
    hire_date: Optional[date] = None
    termination_date: Optional[date] = None
    status: Optional[str] = None
    driver_type: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    mobile_phone: Optional[str] = None
    home_terminal: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class DriversOut(BaseModel):
    drivers_id: uuid.UUID
    driver_code: str
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    ssn_last_four: Optional[str] = None
    employee_number: Optional[str] = None
    license_number: Optional[str] = None
    license_state: Optional[str] = None
    license_class: Optional[str] = None
    license_endorsements: Optional[str] = None
    license_expiration: Optional[date] = None
    medical_cert_expiration: Optional[date] = None
    hire_date: Optional[date] = None
    termination_date: Optional[date] = None
    status: Optional[str] = None
    driver_type: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    mobile_phone: Optional[str] = None
    home_terminal: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class EquipmentCreate(BaseModel):
    equipment_id: uuid.UUID
    equipment_type_id: uuid.UUID
    asset_number: str
    vin: Optional[str] = None
    license_plate: Optional[str] = None
    license_state: Optional[str] = None
    year: Optional[int] = None
    make: Optional[str] = None
    model: Optional[str] = None
    owned_leased: Optional[str] = None
    purchase_date: Optional[date] = None
    lease_expiration: Optional[date] = None
    status: Optional[str] = None
    current_odometer: Optional[int] = None
    last_inspection_date: Optional[date] = None
    next_inspection_date: Optional[date] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class EquipmentUpdate(BaseModel):
    equipment_id: Optional[uuid.UUID] = None
    equipment_type_id: Optional[uuid.UUID] = None
    asset_number: Optional[str] = None
    vin: Optional[str] = None
    license_plate: Optional[str] = None
    license_state: Optional[str] = None
    year: Optional[int] = None
    make: Optional[str] = None
    model: Optional[str] = None
    owned_leased: Optional[str] = None
    purchase_date: Optional[date] = None
    lease_expiration: Optional[date] = None
    status: Optional[str] = None
    current_odometer: Optional[int] = None
    last_inspection_date: Optional[date] = None
    next_inspection_date: Optional[date] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class EquipmentOut(BaseModel):
    equipment_id: uuid.UUID
    equipment_type_id: uuid.UUID
    asset_number: str
    vin: Optional[str] = None
    license_plate: Optional[str] = None
    license_state: Optional[str] = None
    year: Optional[int] = None
    make: Optional[str] = None
    model: Optional[str] = None
    owned_leased: Optional[str] = None
    purchase_date: Optional[date] = None
    lease_expiration: Optional[date] = None
    status: Optional[str] = None
    current_odometer: Optional[int] = None
    last_inspection_date: Optional[date] = None
    next_inspection_date: Optional[date] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class EquipmentAssignmentsCreate(BaseModel):
    equipment_assignments_id: uuid.UUID
    equipment_id: uuid.UUID
    assignment_type: str
    assigned_to_id: Optional[uuid.UUID] = None
    assigned_to_type: Optional[str] = None
    start_date: datetime
    end_date: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class EquipmentAssignmentsUpdate(BaseModel):
    equipment_assignments_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    assignment_type: Optional[str] = None
    assigned_to_id: Optional[uuid.UUID] = None
    assigned_to_type: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class EquipmentAssignmentsOut(BaseModel):
    equipment_assignments_id: uuid.UUID
    equipment_id: uuid.UUID
    assignment_type: str
    assigned_to_id: Optional[uuid.UUID] = None
    assigned_to_type: Optional[str] = None
    start_date: datetime
    end_date: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class EquipmentTrackingDevicesCreate(BaseModel):
    equipment_tracking_devices_id: uuid.UUID
    equipment_id: uuid.UUID
    device_type: str
    device_serial: str
    device_identifier: Optional[str] = None
    provider: Optional[str] = None
    install_date: Optional[date] = None
    last_communication: Optional[datetime] = None
    battery_level: Optional[float] = None
    status: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class EquipmentTrackingDevicesUpdate(BaseModel):
    equipment_tracking_devices_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    device_type: Optional[str] = None
    device_serial: Optional[str] = None
    device_identifier: Optional[str] = None
    provider: Optional[str] = None
    install_date: Optional[date] = None
    last_communication: Optional[datetime] = None
    battery_level: Optional[float] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class EquipmentTrackingDevicesOut(BaseModel):
    equipment_tracking_devices_id: uuid.UUID
    equipment_id: uuid.UUID
    device_type: str
    device_serial: str
    device_identifier: Optional[str] = None
    provider: Optional[str] = None
    install_date: Optional[date] = None
    last_communication: Optional[datetime] = None
    battery_level: Optional[float] = None
    status: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class EquipmentTypesCreate(BaseModel):
    equipment_types_id: uuid.UUID
    equipment_type_code: str
    equipment_type_name: str
    equipment_category: Optional[str] = None
    description: Optional[str] = None
    max_gross_weight: Optional[float] = None
    max_payload_weight: Optional[float] = None
    max_capacity_cu_ft: Optional[float] = None
    length_inches: Optional[float] = None
    width_inches: Optional[float] = None
    height_inches: Optional[float] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class EquipmentTypesUpdate(BaseModel):
    equipment_types_id: Optional[uuid.UUID] = None
    equipment_type_code: Optional[str] = None
    equipment_type_name: Optional[str] = None
    equipment_category: Optional[str] = None
    description: Optional[str] = None
    max_gross_weight: Optional[float] = None
    max_payload_weight: Optional[float] = None
    max_capacity_cu_ft: Optional[float] = None
    length_inches: Optional[float] = None
    width_inches: Optional[float] = None
    height_inches: Optional[float] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class EquipmentTypesOut(BaseModel):
    equipment_types_id: uuid.UUID
    equipment_type_code: str
    equipment_type_name: str
    equipment_category: Optional[str] = None
    description: Optional[str] = None
    max_gross_weight: Optional[float] = None
    max_payload_weight: Optional[float] = None
    max_capacity_cu_ft: Optional[float] = None
    length_inches: Optional[float] = None
    width_inches: Optional[float] = None
    height_inches: Optional[float] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class FreightAuditCreate(BaseModel):
    freight_audit_id: uuid.UUID
    freight_invoice_id: uuid.UUID
    audit_date: datetime
    auditor_id: Optional[uuid.UUID] = None
    audit_type: str
    result: str
    original_amount: Optional[float] = None
    audited_amount: Optional[float] = None
    difference_amount: Optional[float] = None
    discrepancy_reason: Optional[str] = None
    resolution_notes: Optional[str] = None
    is_auto_audited: Optional[bool] = None
    auto_audit_score: Optional[float] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class FreightAuditUpdate(BaseModel):
    freight_audit_id: Optional[uuid.UUID] = None
    freight_invoice_id: Optional[uuid.UUID] = None
    audit_date: Optional[datetime] = None
    auditor_id: Optional[uuid.UUID] = None
    audit_type: Optional[str] = None
    result: Optional[str] = None
    original_amount: Optional[float] = None
    audited_amount: Optional[float] = None
    difference_amount: Optional[float] = None
    discrepancy_reason: Optional[str] = None
    resolution_notes: Optional[str] = None
    is_auto_audited: Optional[bool] = None
    auto_audit_score: Optional[float] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class FreightAuditOut(BaseModel):
    freight_audit_id: uuid.UUID
    freight_invoice_id: uuid.UUID
    audit_date: datetime
    auditor_id: Optional[uuid.UUID] = None
    audit_type: str
    result: str
    original_amount: Optional[float] = None
    audited_amount: Optional[float] = None
    difference_amount: Optional[float] = None
    discrepancy_reason: Optional[str] = None
    resolution_notes: Optional[str] = None
    is_auto_audited: Optional[bool] = None
    auto_audit_score: Optional[float] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class FreightCostAllocationsCreate(BaseModel):
    freight_cost_allocations_id: uuid.UUID
    freight_cost_line_id: Optional[uuid.UUID] = None
    shipment_line_id: Optional[uuid.UUID] = None
    load_line_id: Optional[uuid.UUID] = None
    allocation_percent: Optional[float] = None
    allocated_amount: float
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class FreightCostAllocationsUpdate(BaseModel):
    freight_cost_allocations_id: Optional[uuid.UUID] = None
    freight_cost_line_id: Optional[uuid.UUID] = None
    shipment_line_id: Optional[uuid.UUID] = None
    load_line_id: Optional[uuid.UUID] = None
    allocation_percent: Optional[float] = None
    allocated_amount: Optional[float] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class FreightCostAllocationsOut(BaseModel):
    freight_cost_allocations_id: uuid.UUID
    freight_cost_line_id: Optional[uuid.UUID] = None
    shipment_line_id: Optional[uuid.UUID] = None
    load_line_id: Optional[uuid.UUID] = None
    allocation_percent: Optional[float] = None
    allocated_amount: float
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class FreightCostLinesCreate(BaseModel):
    freight_cost_lines_id: uuid.UUID
    freight_cost_id: uuid.UUID
    line_number: int
    charge_code: Optional[str] = None
    charge_description: Optional[str] = None
    quantity: Optional[float] = None
    rate: Optional[float] = None
    amount: float
    basis: Optional[str] = None
    currency: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class FreightCostLinesUpdate(BaseModel):
    freight_cost_lines_id: Optional[uuid.UUID] = None
    freight_cost_id: Optional[uuid.UUID] = None
    line_number: Optional[int] = None
    charge_code: Optional[str] = None
    charge_description: Optional[str] = None
    quantity: Optional[float] = None
    rate: Optional[float] = None
    amount: Optional[float] = None
    basis: Optional[str] = None
    currency: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class FreightCostLinesOut(BaseModel):
    freight_cost_lines_id: uuid.UUID
    freight_cost_id: uuid.UUID
    line_number: int
    charge_code: Optional[str] = None
    charge_description: Optional[str] = None
    quantity: Optional[float] = None
    rate: Optional[float] = None
    amount: float
    basis: Optional[str] = None
    currency: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class FreightCostsCreate(BaseModel):
    freight_costs_id: uuid.UUID
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    cost_category: str
    cost_type: str
    description: Optional[str] = None
    amount: float
    currency: Optional[str] = None
    cost_date: date
    vendor: Optional[str] = None
    reference_number: Optional[str] = None
    billable_flag: Optional[bool] = None
    paid_flag: Optional[bool] = None
    paid_date: Optional[date] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class FreightCostsUpdate(BaseModel):
    freight_costs_id: Optional[uuid.UUID] = None
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    cost_category: Optional[str] = None
    cost_type: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[str] = None
    cost_date: Optional[date] = None
    vendor: Optional[str] = None
    reference_number: Optional[str] = None
    billable_flag: Optional[bool] = None
    paid_flag: Optional[bool] = None
    paid_date: Optional[date] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class FreightCostsOut(BaseModel):
    freight_costs_id: uuid.UUID
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    cost_category: str
    cost_type: str
    description: Optional[str] = None
    amount: float
    currency: Optional[str] = None
    cost_date: date
    vendor: Optional[str] = None
    reference_number: Optional[str] = None
    billable_flag: Optional[bool] = None
    paid_flag: Optional[bool] = None
    paid_date: Optional[date] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class FreightInvoiceLinesCreate(BaseModel):
    freight_invoice_lines_id: uuid.UUID
    freight_invoice_id: uuid.UUID
    line_number: int
    charge_type: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[float] = None
    rate: Optional[float] = None
    amount: float
    reference: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class FreightInvoiceLinesUpdate(BaseModel):
    freight_invoice_lines_id: Optional[uuid.UUID] = None
    freight_invoice_id: Optional[uuid.UUID] = None
    line_number: Optional[int] = None
    charge_type: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[float] = None
    rate: Optional[float] = None
    amount: Optional[float] = None
    reference: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class FreightInvoiceLinesOut(BaseModel):
    freight_invoice_lines_id: uuid.UUID
    freight_invoice_id: uuid.UUID
    line_number: int
    charge_type: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[float] = None
    rate: Optional[float] = None
    amount: float
    reference: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class FreightInvoicesCreate(BaseModel):
    freight_invoices_id: uuid.UUID
    invoice_number: str
    carrier_id: Optional[uuid.UUID] = None
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    invoice_date: date
    due_date: Optional[date] = None
    total_amount: float
    total_paid: Optional[float] = None
    balance_due: Optional[float] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    invoice_received_date: Optional[date] = None
    invoice_image_url: Optional[str] = None
    reference_number: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class FreightInvoicesUpdate(BaseModel):
    freight_invoices_id: Optional[uuid.UUID] = None
    invoice_number: Optional[str] = None
    carrier_id: Optional[uuid.UUID] = None
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    invoice_date: Optional[date] = None
    due_date: Optional[date] = None
    total_amount: Optional[float] = None
    total_paid: Optional[float] = None
    balance_due: Optional[float] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    invoice_received_date: Optional[date] = None
    invoice_image_url: Optional[str] = None
    reference_number: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class FreightInvoicesOut(BaseModel):
    freight_invoices_id: uuid.UUID
    invoice_number: str
    carrier_id: Optional[uuid.UUID] = None
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    invoice_date: date
    due_date: Optional[date] = None
    total_amount: float
    total_paid: Optional[float] = None
    balance_due: Optional[float] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    invoice_received_date: Optional[date] = None
    invoice_image_url: Optional[str] = None
    reference_number: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class FuelConsumptionCreate(BaseModel):
    fuel_consumption_id: uuid.UUID
    vehicle_id: uuid.UUID
    trip_id: Optional[uuid.UUID] = None
    period_start: datetime
    period_end: datetime
    gallons_consumed: float
    miles_driven: float
    mpg: Optional[float] = None
    idle_time_minutes: Optional[int] = None
    engine_hours: Optional[float] = None
    cost_total: Optional[float] = None
    cost_per_mile: Optional[float] = None
    fuel_type: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class FuelConsumptionUpdate(BaseModel):
    fuel_consumption_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    trip_id: Optional[uuid.UUID] = None
    period_start: Optional[datetime] = None
    period_end: Optional[datetime] = None
    gallons_consumed: Optional[float] = None
    miles_driven: Optional[float] = None
    mpg: Optional[float] = None
    idle_time_minutes: Optional[int] = None
    engine_hours: Optional[float] = None
    cost_total: Optional[float] = None
    cost_per_mile: Optional[float] = None
    fuel_type: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class FuelConsumptionOut(BaseModel):
    fuel_consumption_id: uuid.UUID
    vehicle_id: uuid.UUID
    trip_id: Optional[uuid.UUID] = None
    period_start: datetime
    period_end: datetime
    gallons_consumed: float
    miles_driven: float
    mpg: Optional[float] = None
    idle_time_minutes: Optional[int] = None
    engine_hours: Optional[float] = None
    cost_total: Optional[float] = None
    cost_per_mile: Optional[float] = None
    fuel_type: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class FuelSurchargeLinesCreate(BaseModel):
    fuel_surcharge_lines_id: uuid.UUID
    fuel_surcharge_table_id: uuid.UUID
    fuel_price_min: float
    fuel_price_max: Optional[float] = None
    surcharge_amount: float
    surcharge_percent: Optional[float] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class FuelSurchargeLinesUpdate(BaseModel):
    fuel_surcharge_lines_id: Optional[uuid.UUID] = None
    fuel_surcharge_table_id: Optional[uuid.UUID] = None
    fuel_price_min: Optional[float] = None
    fuel_price_max: Optional[float] = None
    surcharge_amount: Optional[float] = None
    surcharge_percent: Optional[float] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class FuelSurchargeLinesOut(BaseModel):
    fuel_surcharge_lines_id: uuid.UUID
    fuel_surcharge_table_id: uuid.UUID
    fuel_price_min: float
    fuel_price_max: Optional[float] = None
    surcharge_amount: float
    surcharge_percent: Optional[float] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class FuelSurchargeTablesCreate(BaseModel):
    fuel_surcharge_tables_id: uuid.UUID
    table_code: str
    table_name: str
    carrier_id: Optional[uuid.UUID] = None
    base_fuel_price: float
    trigger_increment: float
    surcharge_basis: Optional[str] = None
    effective_date: date
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class FuelSurchargeTablesUpdate(BaseModel):
    fuel_surcharge_tables_id: Optional[uuid.UUID] = None
    table_code: Optional[str] = None
    table_name: Optional[str] = None
    carrier_id: Optional[uuid.UUID] = None
    base_fuel_price: Optional[float] = None
    trigger_increment: Optional[float] = None
    surcharge_basis: Optional[str] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class FuelSurchargeTablesOut(BaseModel):
    fuel_surcharge_tables_id: uuid.UUID
    table_code: str
    table_name: str
    carrier_id: Optional[uuid.UUID] = None
    base_fuel_price: float
    trigger_increment: float
    surcharge_basis: Optional[str] = None
    effective_date: date
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class FuelTransactionsCreate(BaseModel):
    fuel_transactions_id: uuid.UUID
    transaction_number: str
    vehicle_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    fuel_type: str
    fuel_date: datetime
    location_name: Optional[str] = None
    gallons: float
    price_per_gallon: float
    total_amount: float
    currency: Optional[str] = None
    odometer_reading: Optional[int] = None
    vendor: Optional[str] = None
    receipt_number: Optional[str] = None
    payment_method: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class FuelTransactionsUpdate(BaseModel):
    fuel_transactions_id: Optional[uuid.UUID] = None
    transaction_number: Optional[str] = None
    vehicle_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    fuel_type: Optional[str] = None
    fuel_date: Optional[datetime] = None
    location_name: Optional[str] = None
    gallons: Optional[float] = None
    price_per_gallon: Optional[float] = None
    total_amount: Optional[float] = None
    currency: Optional[str] = None
    odometer_reading: Optional[int] = None
    vendor: Optional[str] = None
    receipt_number: Optional[str] = None
    payment_method: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class FuelTransactionsOut(BaseModel):
    fuel_transactions_id: uuid.UUID
    transaction_number: str
    vehicle_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    fuel_type: str
    fuel_date: datetime
    location_name: Optional[str] = None
    gallons: float
    price_per_gallon: float
    total_amount: float
    currency: Optional[str] = None
    odometer_reading: Optional[int] = None
    vendor: Optional[str] = None
    receipt_number: Optional[str] = None
    payment_method: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class GeofenceEventsCreate(BaseModel):
    geofence_events_id: uuid.UUID
    tracking_event_id: Optional[uuid.UUID] = None
    geofence_name: Optional[str] = None
    geofence_type: Optional[str] = None
    facility_name: Optional[str] = None
    facility_id: Optional[str] = None
    event_type: str
    event_timestamp: datetime
    source: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None

class GeofenceEventsUpdate(BaseModel):
    geofence_events_id: Optional[uuid.UUID] = None
    tracking_event_id: Optional[uuid.UUID] = None
    geofence_name: Optional[str] = None
    geofence_type: Optional[str] = None
    facility_name: Optional[str] = None
    facility_id: Optional[str] = None
    event_type: Optional[str] = None
    event_timestamp: Optional[datetime] = None
    source: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None

class GeofenceEventsOut(BaseModel):
    geofence_events_id: uuid.UUID
    tracking_event_id: Optional[uuid.UUID] = None
    geofence_name: Optional[str] = None
    geofence_type: Optional[str] = None
    facility_name: Optional[str] = None
    facility_id: Optional[str] = None
    event_type: str
    event_timestamp: datetime
    source: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    model_config = {"from_attributes": True}

class GpsPingsCreate(BaseModel):
    gps_pings_id: uuid.UUID
    equipment_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    device_id: Optional[uuid.UUID] = None
    ping_timestamp: datetime
    latitude: float
    longitude: float
    altitude: Optional[float] = None
    speed: Optional[float] = None
    heading: Optional[float] = None
    accuracy: Optional[float] = None
    odometer: Optional[int] = None
    engine_on: Optional[bool] = None
    ignition_on: Optional[bool] = None
    battery_voltage: Optional[float] = None
    source: Optional[str] = None
    tenant_id: Optional[str] = None

class GpsPingsUpdate(BaseModel):
    gps_pings_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    device_id: Optional[uuid.UUID] = None
    ping_timestamp: Optional[datetime] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None
    speed: Optional[float] = None
    heading: Optional[float] = None
    accuracy: Optional[float] = None
    odometer: Optional[int] = None
    engine_on: Optional[bool] = None
    ignition_on: Optional[bool] = None
    battery_voltage: Optional[float] = None
    source: Optional[str] = None
    tenant_id: Optional[str] = None

class GpsPingsOut(BaseModel):
    gps_pings_id: uuid.UUID
    equipment_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    device_id: Optional[uuid.UUID] = None
    ping_timestamp: datetime
    latitude: float
    longitude: float
    altitude: Optional[float] = None
    speed: Optional[float] = None
    heading: Optional[float] = None
    accuracy: Optional[float] = None
    odometer: Optional[int] = None
    engine_on: Optional[bool] = None
    ignition_on: Optional[bool] = None
    battery_voltage: Optional[float] = None
    source: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    model_config = {"from_attributes": True}

class HazmatClassificationsCreate(BaseModel):
    hazmat_classifications_id: uuid.UUID
    class_code: str
    class_name: str
    hazard_class: str
    division: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class HazmatClassificationsUpdate(BaseModel):
    hazmat_classifications_id: Optional[uuid.UUID] = None
    class_code: Optional[str] = None
    class_name: Optional[str] = None
    hazard_class: Optional[str] = None
    division: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class HazmatClassificationsOut(BaseModel):
    hazmat_classifications_id: uuid.UUID
    class_code: str
    class_name: str
    hazard_class: str
    division: Optional[str] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class HazmatIncidentsCreate(BaseModel):
    hazmat_incidents_id: uuid.UUID
    incident_number: str
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    hazmat_classification_id: Optional[uuid.UUID] = None
    un_number: Optional[str] = None
    incident_date: datetime
    incident_type: str
    description: str
    immediate_cause: Optional[str] = None
    corrective_action: Optional[str] = None
    injuries_count: Optional[int] = None
    fatalities_count: Optional[int] = None
    property_damage_estimate: Optional[float] = None
    environmental_damage: Optional[bool] = None
    evacuation_required: Optional[bool] = None
    reported_to_authorities: Optional[bool] = None
    authority_report_number: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class HazmatIncidentsUpdate(BaseModel):
    hazmat_incidents_id: Optional[uuid.UUID] = None
    incident_number: Optional[str] = None
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    hazmat_classification_id: Optional[uuid.UUID] = None
    un_number: Optional[str] = None
    incident_date: Optional[datetime] = None
    incident_type: Optional[str] = None
    description: Optional[str] = None
    immediate_cause: Optional[str] = None
    corrective_action: Optional[str] = None
    injuries_count: Optional[int] = None
    fatalities_count: Optional[int] = None
    property_damage_estimate: Optional[float] = None
    environmental_damage: Optional[bool] = None
    evacuation_required: Optional[bool] = None
    reported_to_authorities: Optional[bool] = None
    authority_report_number: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class HazmatIncidentsOut(BaseModel):
    hazmat_incidents_id: uuid.UUID
    incident_number: str
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    hazmat_classification_id: Optional[uuid.UUID] = None
    un_number: Optional[str] = None
    incident_date: datetime
    incident_type: str
    description: str
    immediate_cause: Optional[str] = None
    corrective_action: Optional[str] = None
    injuries_count: Optional[int] = None
    fatalities_count: Optional[int] = None
    property_damage_estimate: Optional[float] = None
    environmental_damage: Optional[bool] = None
    evacuation_required: Optional[bool] = None
    reported_to_authorities: Optional[bool] = None
    authority_report_number: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class HazmatPackagingCreate(BaseModel):
    hazmat_packaging_id: uuid.UUID
    hazmat_classification_id: uuid.UUID
    un_number: str
    proper_shipping_name: str
    technical_name: Optional[str] = None
    hazard_class: str
    packing_group: Optional[str] = None
    labeling_required: Optional[str] = None
    placarding_required: Optional[str] = None
    packaging_instructions: Optional[str] = None
    quantity_limit_transport: Optional[float] = None
    quantity_limit_unit: Optional[str] = None
    emergency_response_guide: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1

class HazmatPackagingUpdate(BaseModel):
    hazmat_packaging_id: Optional[uuid.UUID] = None
    hazmat_classification_id: Optional[uuid.UUID] = None
    un_number: Optional[str] = None
    proper_shipping_name: Optional[str] = None
    technical_name: Optional[str] = None
    hazard_class: Optional[str] = None
    packing_group: Optional[str] = None
    labeling_required: Optional[str] = None
    placarding_required: Optional[str] = None
    packaging_instructions: Optional[str] = None
    quantity_limit_transport: Optional[float] = None
    quantity_limit_unit: Optional[str] = None
    emergency_response_guide: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class HazmatPackagingOut(BaseModel):
    hazmat_packaging_id: uuid.UUID
    hazmat_classification_id: uuid.UUID
    un_number: str
    proper_shipping_name: str
    technical_name: Optional[str] = None
    hazard_class: str
    packing_group: Optional[str] = None
    labeling_required: Optional[str] = None
    placarding_required: Optional[str] = None
    packaging_instructions: Optional[str] = None
    quantity_limit_transport: Optional[float] = None
    quantity_limit_unit: Optional[str] = None
    emergency_response_guide: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class HazmatSegregationCreate(BaseModel):
    hazmat_segregation_id: uuid.UUID
    class_a: str
    class_b: str
    segregation_rule: str
    description: Optional[str] = None
    is_segregated: Optional[bool] = None
    notes: Optional[str] = None
    object_version_number: int = 1

class HazmatSegregationUpdate(BaseModel):
    hazmat_segregation_id: Optional[uuid.UUID] = None
    class_a: Optional[str] = None
    class_b: Optional[str] = None
    segregation_rule: Optional[str] = None
    description: Optional[str] = None
    is_segregated: Optional[bool] = None
    notes: Optional[str] = None
    object_version_number: Optional[int] = None

class HazmatSegregationOut(BaseModel):
    hazmat_segregation_id: uuid.UUID
    class_a: str
    class_b: str
    segregation_rule: str
    description: Optional[str] = None
    is_segregated: Optional[bool] = None
    notes: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class HsCodesCreate(BaseModel):
    hs_codes_id: uuid.UUID
    hs_code: str
    description: str
    chapter: Optional[str] = None
    heading: Optional[str] = None
    subheading: Optional[str] = None
    duty_rate: Optional[float] = None
    unit_of_measure: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class HsCodesUpdate(BaseModel):
    hs_codes_id: Optional[uuid.UUID] = None
    hs_code: Optional[str] = None
    description: Optional[str] = None
    chapter: Optional[str] = None
    heading: Optional[str] = None
    subheading: Optional[str] = None
    duty_rate: Optional[float] = None
    unit_of_measure: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class HsCodesOut(BaseModel):
    hs_codes_id: uuid.UUID
    hs_code: str
    description: str
    chapter: Optional[str] = None
    heading: Optional[str] = None
    subheading: Optional[str] = None
    duty_rate: Optional[float] = None
    unit_of_measure: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class IncotermsCreate(BaseModel):
    incoterms_id: uuid.UUID
    incoterm_code: str
    incoterm_name: str
    description: Optional[str] = None
    risk_transfer_point: Optional[str] = None
    cost_allocation: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class IncotermsUpdate(BaseModel):
    incoterms_id: Optional[uuid.UUID] = None
    incoterm_code: Optional[str] = None
    incoterm_name: Optional[str] = None
    description: Optional[str] = None
    risk_transfer_point: Optional[str] = None
    cost_allocation: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class IncotermsOut(BaseModel):
    incoterms_id: uuid.UUID
    incoterm_code: str
    incoterm_name: str
    description: Optional[str] = None
    risk_transfer_point: Optional[str] = None
    cost_allocation: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class InsurancePoliciesCreate(BaseModel):
    insurance_policies_id: uuid.UUID
    policy_number: str
    carrier_id: Optional[uuid.UUID] = None
    provider: str
    policy_type: str
    coverage_type: Optional[str] = None
    coverage_limit: Optional[float] = None
    deductible: Optional[float] = None
    premium_amount: Optional[float] = None
    effective_date: date
    expiration_date: date
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class InsurancePoliciesUpdate(BaseModel):
    insurance_policies_id: Optional[uuid.UUID] = None
    policy_number: Optional[str] = None
    carrier_id: Optional[uuid.UUID] = None
    provider: Optional[str] = None
    policy_type: Optional[str] = None
    coverage_type: Optional[str] = None
    coverage_limit: Optional[float] = None
    deductible: Optional[float] = None
    premium_amount: Optional[float] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class InsurancePoliciesOut(BaseModel):
    insurance_policies_id: uuid.UUID
    policy_number: str
    carrier_id: Optional[uuid.UUID] = None
    provider: str
    policy_type: str
    coverage_type: Optional[str] = None
    coverage_limit: Optional[float] = None
    deductible: Optional[float] = None
    premium_amount: Optional[float] = None
    effective_date: date
    expiration_date: date
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class InterfaceErrorLogCreate(BaseModel):
    interface_error_log_id: uuid.UUID
    source_system: str
    interface_type: str
    error_code: Optional[str] = None
    error_message: str
    error_detail: Optional[str] = None
    severity: Optional[str] = None
    endpoint: Optional[str] = None
    request_payload: Optional[str] = None
    response_payload: Optional[str] = None
    http_status: Optional[int] = None
    resolved: Optional[bool] = None
    resolved_at: Optional[datetime] = None
    resolved_by: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class InterfaceErrorLogUpdate(BaseModel):
    interface_error_log_id: Optional[uuid.UUID] = None
    source_system: Optional[str] = None
    interface_type: Optional[str] = None
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    error_detail: Optional[str] = None
    severity: Optional[str] = None
    endpoint: Optional[str] = None
    request_payload: Optional[str] = None
    response_payload: Optional[str] = None
    http_status: Optional[int] = None
    resolved: Optional[bool] = None
    resolved_at: Optional[datetime] = None
    resolved_by: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class InterfaceErrorLogOut(BaseModel):
    interface_error_log_id: uuid.UUID
    source_system: str
    interface_type: str
    error_code: Optional[str] = None
    error_message: str
    error_detail: Optional[str] = None
    severity: Optional[str] = None
    endpoint: Optional[str] = None
    request_payload: Optional[str] = None
    response_payload: Optional[str] = None
    http_status: Optional[int] = None
    resolved: Optional[bool] = None
    resolved_at: Optional[datetime] = None
    resolved_by: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class InterfaceShipmentImportCreate(BaseModel):
    interface_shipment_import_id: uuid.UUID
    batch_id: str
    source_system: str
    source_type: Optional[str] = None
    payload: Optional[dict] = None
    status: Optional[str] = None
    validation_result: Optional[str] = None
    error_message: Optional[str] = None
    shipment_id: Optional[uuid.UUID] = None
    processed_at: Optional[datetime] = None
    processed_by: Optional[str] = None
    retry_count: Optional[int] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class InterfaceShipmentImportUpdate(BaseModel):
    interface_shipment_import_id: Optional[uuid.UUID] = None
    batch_id: Optional[str] = None
    source_system: Optional[str] = None
    source_type: Optional[str] = None
    payload: Optional[dict] = None
    status: Optional[str] = None
    validation_result: Optional[str] = None
    error_message: Optional[str] = None
    shipment_id: Optional[uuid.UUID] = None
    processed_at: Optional[datetime] = None
    processed_by: Optional[str] = None
    retry_count: Optional[int] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class InterfaceShipmentImportOut(BaseModel):
    interface_shipment_import_id: uuid.UUID
    batch_id: str
    source_system: str
    source_type: Optional[str] = None
    payload: Optional[dict] = None
    status: Optional[str] = None
    validation_result: Optional[str] = None
    error_message: Optional[str] = None
    shipment_id: Optional[uuid.UUID] = None
    processed_at: Optional[datetime] = None
    processed_by: Optional[str] = None
    retry_count: Optional[int] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class KpiDefinitionsCreate(BaseModel):
    kpi_definitions_id: uuid.UUID
    kpi_code: str
    kpi_name: str
    kpi_category: Optional[str] = None
    description: Optional[str] = None
    formula: Optional[str] = None
    unit: Optional[str] = None
    higher_is_better: Optional[bool] = None
    target_value: Optional[float] = None
    warning_threshold: Optional[float] = None
    critical_threshold: Optional[float] = None
    frequency: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class KpiDefinitionsUpdate(BaseModel):
    kpi_definitions_id: Optional[uuid.UUID] = None
    kpi_code: Optional[str] = None
    kpi_name: Optional[str] = None
    kpi_category: Optional[str] = None
    description: Optional[str] = None
    formula: Optional[str] = None
    unit: Optional[str] = None
    higher_is_better: Optional[bool] = None
    target_value: Optional[float] = None
    warning_threshold: Optional[float] = None
    critical_threshold: Optional[float] = None
    frequency: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class KpiDefinitionsOut(BaseModel):
    kpi_definitions_id: uuid.UUID
    kpi_code: str
    kpi_name: str
    kpi_category: Optional[str] = None
    description: Optional[str] = None
    formula: Optional[str] = None
    unit: Optional[str] = None
    higher_is_better: Optional[bool] = None
    target_value: Optional[float] = None
    warning_threshold: Optional[float] = None
    critical_threshold: Optional[float] = None
    frequency: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class KpiValuesCreate(BaseModel):
    kpi_values_id: uuid.UUID
    kpi_definition_id: uuid.UUID
    carrier_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    period_start: date
    period_end: date
    actual_value: Optional[float] = None
    target_value: Optional[float] = None
    variance: Optional[float] = None
    variance_percent: Optional[float] = None
    is_target_achieved: Optional[bool] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class KpiValuesUpdate(BaseModel):
    kpi_values_id: Optional[uuid.UUID] = None
    kpi_definition_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    period_start: Optional[date] = None
    period_end: Optional[date] = None
    actual_value: Optional[float] = None
    target_value: Optional[float] = None
    variance: Optional[float] = None
    variance_percent: Optional[float] = None
    is_target_achieved: Optional[bool] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class KpiValuesOut(BaseModel):
    kpi_values_id: uuid.UUID
    kpi_definition_id: uuid.UUID
    carrier_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    period_start: date
    period_end: date
    actual_value: Optional[float] = None
    target_value: Optional[float] = None
    variance: Optional[float] = None
    variance_percent: Optional[float] = None
    is_target_achieved: Optional[bool] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class LaneCarriersCreate(BaseModel):
    lane_carriers_id: uuid.UUID
    lane_id: uuid.UUID
    carrier_id: uuid.UUID
    carrier_service_id: Optional[uuid.UUID] = None
    is_preferred: Optional[bool] = None
    is_contracted: Optional[bool] = None
    contract_rate: Optional[float] = None
    transit_days_min: Optional[int] = None
    transit_days_max: Optional[int] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class LaneCarriersUpdate(BaseModel):
    lane_carriers_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    carrier_service_id: Optional[uuid.UUID] = None
    is_preferred: Optional[bool] = None
    is_contracted: Optional[bool] = None
    contract_rate: Optional[float] = None
    transit_days_min: Optional[int] = None
    transit_days_max: Optional[int] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class LaneCarriersOut(BaseModel):
    lane_carriers_id: uuid.UUID
    lane_id: uuid.UUID
    carrier_id: uuid.UUID
    carrier_service_id: Optional[uuid.UUID] = None
    is_preferred: Optional[bool] = None
    is_contracted: Optional[bool] = None
    contract_rate: Optional[float] = None
    transit_days_min: Optional[int] = None
    transit_days_max: Optional[int] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class LanePerformanceCreate(BaseModel):
    lane_performance_id: uuid.UUID
    lane_id: uuid.UUID
    carrier_id: Optional[uuid.UUID] = None
    period_start: date
    period_end: date
    total_shipments: Optional[int] = None
    on_time_deliveries: Optional[int] = None
    on_time_pickups: Optional[int] = None
    avg_transit_days: Optional[float] = None
    min_transit_days: Optional[int] = None
    max_transit_days: Optional[int] = None
    damage_claims: Optional[int] = None
    avg_cost_per_mile: Optional[float] = None
    avg_cost_per_load: Optional[float] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class LanePerformanceUpdate(BaseModel):
    lane_performance_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    period_start: Optional[date] = None
    period_end: Optional[date] = None
    total_shipments: Optional[int] = None
    on_time_deliveries: Optional[int] = None
    on_time_pickups: Optional[int] = None
    avg_transit_days: Optional[float] = None
    min_transit_days: Optional[int] = None
    max_transit_days: Optional[int] = None
    damage_claims: Optional[int] = None
    avg_cost_per_mile: Optional[float] = None
    avg_cost_per_load: Optional[float] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class LanePerformanceOut(BaseModel):
    lane_performance_id: uuid.UUID
    lane_id: uuid.UUID
    carrier_id: Optional[uuid.UUID] = None
    period_start: date
    period_end: date
    total_shipments: Optional[int] = None
    on_time_deliveries: Optional[int] = None
    on_time_pickups: Optional[int] = None
    avg_transit_days: Optional[float] = None
    min_transit_days: Optional[int] = None
    max_transit_days: Optional[int] = None
    damage_claims: Optional[int] = None
    avg_cost_per_mile: Optional[float] = None
    avg_cost_per_load: Optional[float] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class LanesCreate(BaseModel):
    lanes_id: uuid.UUID
    lane_code: str
    lane_name: str
    origin_city: Optional[str] = None
    origin_state: Optional[str] = None
    origin_zip: Optional[str] = None
    origin_country: Optional[str] = None
    destination_city: Optional[str] = None
    destination_state: Optional[str] = None
    destination_zip: Optional[str] = None
    destination_country: Optional[str] = None
    distance_miles: Optional[float] = None
    distance_km: Optional[float] = None
    transit_days_min: Optional[int] = None
    transit_days_max: Optional[int] = None
    lane_type: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class LanesUpdate(BaseModel):
    lanes_id: Optional[uuid.UUID] = None
    lane_code: Optional[str] = None
    lane_name: Optional[str] = None
    origin_city: Optional[str] = None
    origin_state: Optional[str] = None
    origin_zip: Optional[str] = None
    origin_country: Optional[str] = None
    destination_city: Optional[str] = None
    destination_state: Optional[str] = None
    destination_zip: Optional[str] = None
    destination_country: Optional[str] = None
    distance_miles: Optional[float] = None
    distance_km: Optional[float] = None
    transit_days_min: Optional[int] = None
    transit_days_max: Optional[int] = None
    lane_type: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class LanesOut(BaseModel):
    lanes_id: uuid.UUID
    lane_code: str
    lane_name: str
    origin_city: Optional[str] = None
    origin_state: Optional[str] = None
    origin_zip: Optional[str] = None
    origin_country: Optional[str] = None
    destination_city: Optional[str] = None
    destination_state: Optional[str] = None
    destination_zip: Optional[str] = None
    destination_country: Optional[str] = None
    distance_miles: Optional[float] = None
    distance_km: Optional[float] = None
    transit_days_min: Optional[int] = None
    transit_days_max: Optional[int] = None
    lane_type: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class LoadCostsCreate(BaseModel):
    load_costs_id: uuid.UUID
    load_id: uuid.UUID
    cost_type: str
    description: Optional[str] = None
    vendor: Optional[str] = None
    amount: float
    billable: Optional[bool] = None
    billable_amount: Optional[float] = None
    currency: Optional[str] = None
    reference_number: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class LoadCostsUpdate(BaseModel):
    load_costs_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    cost_type: Optional[str] = None
    description: Optional[str] = None
    vendor: Optional[str] = None
    amount: Optional[float] = None
    billable: Optional[bool] = None
    billable_amount: Optional[float] = None
    currency: Optional[str] = None
    reference_number: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class LoadCostsOut(BaseModel):
    load_costs_id: uuid.UUID
    load_id: uuid.UUID
    cost_type: str
    description: Optional[str] = None
    vendor: Optional[str] = None
    amount: float
    billable: Optional[bool] = None
    billable_amount: Optional[float] = None
    currency: Optional[str] = None
    reference_number: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class LoadLegsCreate(BaseModel):
    load_legs_id: uuid.UUID
    load_id: uuid.UUID
    leg_sequence: int
    from_stop_id: Optional[uuid.UUID] = None
    to_stop_id: Optional[uuid.UUID] = None
    mode: Optional[str] = None
    carrier_id: Optional[uuid.UUID] = None
    distance_miles: Optional[float] = None
    estimated_duration_minutes: Optional[int] = None
    actual_duration_minutes: Optional[int] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class LoadLegsUpdate(BaseModel):
    load_legs_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    leg_sequence: Optional[int] = None
    from_stop_id: Optional[uuid.UUID] = None
    to_stop_id: Optional[uuid.UUID] = None
    mode: Optional[str] = None
    carrier_id: Optional[uuid.UUID] = None
    distance_miles: Optional[float] = None
    estimated_duration_minutes: Optional[int] = None
    actual_duration_minutes: Optional[int] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class LoadLegsOut(BaseModel):
    load_legs_id: uuid.UUID
    load_id: uuid.UUID
    leg_sequence: int
    from_stop_id: Optional[uuid.UUID] = None
    to_stop_id: Optional[uuid.UUID] = None
    mode: Optional[str] = None
    carrier_id: Optional[uuid.UUID] = None
    distance_miles: Optional[float] = None
    estimated_duration_minutes: Optional[int] = None
    actual_duration_minutes: Optional[int] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class LoadLinesCreate(BaseModel):
    load_lines_id: uuid.UUID
    load_id: uuid.UUID
    shipment_line_id: Optional[uuid.UUID] = None
    line_number: int
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity: float
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    volume: Optional[float] = None
    volume_unit: Optional[str] = None
    pallets_count: Optional[int] = None
    pieces_count: Optional[int] = None
    freight_class: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class LoadLinesUpdate(BaseModel):
    load_lines_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    shipment_line_id: Optional[uuid.UUID] = None
    line_number: Optional[int] = None
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity: Optional[float] = None
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    volume: Optional[float] = None
    volume_unit: Optional[str] = None
    pallets_count: Optional[int] = None
    pieces_count: Optional[int] = None
    freight_class: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class LoadLinesOut(BaseModel):
    load_lines_id: uuid.UUID
    load_id: uuid.UUID
    shipment_line_id: Optional[uuid.UUID] = None
    line_number: int
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity: float
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    volume: Optional[float] = None
    volume_unit: Optional[str] = None
    pallets_count: Optional[int] = None
    pieces_count: Optional[int] = None
    freight_class: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class LoadStopsCreate(BaseModel):
    load_stops_id: uuid.UUID
    load_id: uuid.UUID
    stop_sequence: int
    stop_type: str
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    appointment_id: Optional[uuid.UUID] = None
    planned_arrival: Optional[datetime] = None
    planned_departure: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    arrived_miles: Optional[float] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class LoadStopsUpdate(BaseModel):
    load_stops_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    stop_sequence: Optional[int] = None
    stop_type: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    appointment_id: Optional[uuid.UUID] = None
    planned_arrival: Optional[datetime] = None
    planned_departure: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    arrived_miles: Optional[float] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class LoadStopsOut(BaseModel):
    load_stops_id: uuid.UUID
    load_id: uuid.UUID
    stop_sequence: int
    stop_type: str
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    appointment_id: Optional[uuid.UUID] = None
    planned_arrival: Optional[datetime] = None
    planned_departure: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    arrived_miles: Optional[float] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class LoadsCreate(BaseModel):
    loads_id: uuid.UUID
    load_number: str
    shipment_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    route_id: Optional[uuid.UUID] = None
    load_type: Optional[str] = None
    status: Optional[str] = None
    origin_location: Optional[str] = None
    destination_location: Optional[str] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    total_weight: Optional[float] = None
    total_pieces: Optional[int] = None
    total_pallets: Optional[int] = None
    total_miles: Optional[float] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    carrier_cost: Optional[float] = None
    revenue: Optional[float] = None
    currency: Optional[str] = None
    bol_number: Optional[str] = None
    po_number: Optional[str] = None
    is_hazmat: Optional[bool] = None
    is_temp_controlled: Optional[bool] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class LoadsUpdate(BaseModel):
    loads_id: Optional[uuid.UUID] = None
    load_number: Optional[str] = None
    shipment_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    route_id: Optional[uuid.UUID] = None
    load_type: Optional[str] = None
    status: Optional[str] = None
    origin_location: Optional[str] = None
    destination_location: Optional[str] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    total_weight: Optional[float] = None
    total_pieces: Optional[int] = None
    total_pallets: Optional[int] = None
    total_miles: Optional[float] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    carrier_cost: Optional[float] = None
    revenue: Optional[float] = None
    currency: Optional[str] = None
    bol_number: Optional[str] = None
    po_number: Optional[str] = None
    is_hazmat: Optional[bool] = None
    is_temp_controlled: Optional[bool] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class LoadsOut(BaseModel):
    loads_id: uuid.UUID
    load_number: str
    shipment_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    route_id: Optional[uuid.UUID] = None
    load_type: Optional[str] = None
    status: Optional[str] = None
    origin_location: Optional[str] = None
    destination_location: Optional[str] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    total_weight: Optional[float] = None
    total_pieces: Optional[int] = None
    total_pallets: Optional[int] = None
    total_miles: Optional[float] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    carrier_cost: Optional[float] = None
    revenue: Optional[float] = None
    currency: Optional[str] = None
    bol_number: Optional[str] = None
    po_number: Optional[str] = None
    is_hazmat: Optional[bool] = None
    is_temp_controlled: Optional[bool] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MilestoneAchievementsCreate(BaseModel):
    milestone_achievements_id: uuid.UUID
    milestone_id: uuid.UUID
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    tracking_event_id: Optional[uuid.UUID] = None
    planned_time: Optional[datetime] = None
    achieved_time: Optional[datetime] = None
    variance_minutes: Optional[int] = None
    is_on_time: Optional[bool] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class MilestoneAchievementsUpdate(BaseModel):
    milestone_achievements_id: Optional[uuid.UUID] = None
    milestone_id: Optional[uuid.UUID] = None
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    tracking_event_id: Optional[uuid.UUID] = None
    planned_time: Optional[datetime] = None
    achieved_time: Optional[datetime] = None
    variance_minutes: Optional[int] = None
    is_on_time: Optional[bool] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class MilestoneAchievementsOut(BaseModel):
    milestone_achievements_id: uuid.UUID
    milestone_id: uuid.UUID
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    tracking_event_id: Optional[uuid.UUID] = None
    planned_time: Optional[datetime] = None
    achieved_time: Optional[datetime] = None
    variance_minutes: Optional[int] = None
    is_on_time: Optional[bool] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class MilestonesCreate(BaseModel):
    milestones_id: uuid.UUID
    milestone_code: str
    milestone_name: str
    milestone_category: Optional[str] = None
    description: Optional[str] = None
    is_required: Optional[bool] = None
    is_customer_visible: Optional[bool] = None
    display_order: Optional[int] = None
    sla_minutes: Optional[int] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class MilestonesUpdate(BaseModel):
    milestones_id: Optional[uuid.UUID] = None
    milestone_code: Optional[str] = None
    milestone_name: Optional[str] = None
    milestone_category: Optional[str] = None
    description: Optional[str] = None
    is_required: Optional[bool] = None
    is_customer_visible: Optional[bool] = None
    display_order: Optional[int] = None
    sla_minutes: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class MilestonesOut(BaseModel):
    milestones_id: uuid.UUID
    milestone_code: str
    milestone_name: str
    milestone_category: Optional[str] = None
    description: Optional[str] = None
    is_required: Optional[bool] = None
    is_customer_visible: Optional[bool] = None
    display_order: Optional[int] = None
    sla_minutes: Optional[int] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class PickupLinesCreate(BaseModel):
    pickup_lines_id: uuid.UUID
    pickup_id: uuid.UUID
    shipment_line_id: Optional[uuid.UUID] = None
    line_number: int
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity_expected: Optional[float] = None
    quantity_picked_up: float
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    condition: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class PickupLinesUpdate(BaseModel):
    pickup_lines_id: Optional[uuid.UUID] = None
    pickup_id: Optional[uuid.UUID] = None
    shipment_line_id: Optional[uuid.UUID] = None
    line_number: Optional[int] = None
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity_expected: Optional[float] = None
    quantity_picked_up: Optional[float] = None
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    condition: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class PickupLinesOut(BaseModel):
    pickup_lines_id: uuid.UUID
    pickup_id: uuid.UUID
    shipment_line_id: Optional[uuid.UUID] = None
    line_number: int
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity_expected: Optional[float] = None
    quantity_picked_up: float
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    condition: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class PickupsCreate(BaseModel):
    pickups_id: uuid.UUID
    pickup_number: str
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    pickup_date: date
    status: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    pickup_appointment_id: Optional[uuid.UUID] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    total_packages: Optional[int] = None
    total_weight: Optional[float] = None
    total_pallets: Optional[int] = None
    signed_by: Optional[str] = None
    signed_at: Optional[datetime] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class PickupsUpdate(BaseModel):
    pickups_id: Optional[uuid.UUID] = None
    pickup_number: Optional[str] = None
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    pickup_date: Optional[date] = None
    status: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    pickup_appointment_id: Optional[uuid.UUID] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    total_packages: Optional[int] = None
    total_weight: Optional[float] = None
    total_pallets: Optional[int] = None
    signed_by: Optional[str] = None
    signed_at: Optional[datetime] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class PickupsOut(BaseModel):
    pickups_id: uuid.UUID
    pickup_number: str
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    pickup_date: date
    status: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    pickup_appointment_id: Optional[uuid.UUID] = None
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    total_packages: Optional[int] = None
    total_weight: Optional[float] = None
    total_pallets: Optional[int] = None
    signed_by: Optional[str] = None
    signed_at: Optional[datetime] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class PodCreate(BaseModel):
    pod_id: uuid.UUID
    delivery_id: uuid.UUID
    pod_number: str
    signed_by: Optional[str] = None
    signed_at: Optional[datetime] = None
    signature_image_url: Optional[str] = None
    delivered_at: Optional[datetime] = None
    condition_notes: Optional[str] = None
    exceptions: Optional[str] = None
    is_physical_pod: Optional[bool] = None
    physical_pod_location: Optional[str] = None
    document_url: Optional[str] = None
    status: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class PodUpdate(BaseModel):
    pod_id: Optional[uuid.UUID] = None
    delivery_id: Optional[uuid.UUID] = None
    pod_number: Optional[str] = None
    signed_by: Optional[str] = None
    signed_at: Optional[datetime] = None
    signature_image_url: Optional[str] = None
    delivered_at: Optional[datetime] = None
    condition_notes: Optional[str] = None
    exceptions: Optional[str] = None
    is_physical_pod: Optional[bool] = None
    physical_pod_location: Optional[str] = None
    document_url: Optional[str] = None
    status: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class PodOut(BaseModel):
    pod_id: uuid.UUID
    delivery_id: uuid.UUID
    pod_number: str
    signed_by: Optional[str] = None
    signed_at: Optional[datetime] = None
    signature_image_url: Optional[str] = None
    delivered_at: Optional[datetime] = None
    condition_notes: Optional[str] = None
    exceptions: Optional[str] = None
    is_physical_pod: Optional[bool] = None
    physical_pod_location: Optional[str] = None
    document_url: Optional[str] = None
    status: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class RateChartVersionsCreate(BaseModel):
    rate_chart_versions_id: uuid.UUID
    rate_chart_id: uuid.UUID
    version_number: int
    version_name: Optional[str] = None
    effective_date: date
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    change_summary: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_date: Optional[datetime] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class RateChartVersionsUpdate(BaseModel):
    rate_chart_versions_id: Optional[uuid.UUID] = None
    rate_chart_id: Optional[uuid.UUID] = None
    version_number: Optional[int] = None
    version_name: Optional[str] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    change_summary: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_date: Optional[datetime] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class RateChartVersionsOut(BaseModel):
    rate_chart_versions_id: uuid.UUID
    rate_chart_id: uuid.UUID
    version_number: int
    version_name: Optional[str] = None
    effective_date: date
    expiration_date: Optional[date] = None
    status: Optional[str] = None
    change_summary: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_date: Optional[datetime] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class RateChartsCreate(BaseModel):
    rate_charts_id: uuid.UUID
    rate_chart_code: str
    rate_chart_name: str
    carrier_id: Optional[uuid.UUID] = None
    contract_id: Optional[uuid.UUID] = None
    rate_chart_type: str
    effective_date: date
    expiration_date: Optional[date] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class RateChartsUpdate(BaseModel):
    rate_charts_id: Optional[uuid.UUID] = None
    rate_chart_code: Optional[str] = None
    rate_chart_name: Optional[str] = None
    carrier_id: Optional[uuid.UUID] = None
    contract_id: Optional[uuid.UUID] = None
    rate_chart_type: Optional[str] = None
    effective_date: Optional[date] = None
    expiration_date: Optional[date] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class RateChartsOut(BaseModel):
    rate_charts_id: uuid.UUID
    rate_chart_code: str
    rate_chart_name: str
    carrier_id: Optional[uuid.UUID] = None
    contract_id: Optional[uuid.UUID] = None
    rate_chart_type: str
    effective_date: date
    expiration_date: Optional[date] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class RateLinesCreate(BaseModel):
    rate_lines_id: uuid.UUID
    rate_chart_version_id: uuid.UUID
    origin_zone_id: Optional[uuid.UUID] = None
    destination_zone_id: Optional[uuid.UUID] = None
    equipment_type_id: Optional[uuid.UUID] = None
    commodity_class: Optional[str] = None
    weight_break_min: Optional[float] = None
    weight_break_max: Optional[float] = None
    rate: float
    rate_basis: str
    minimum_charge: Optional[float] = None
    maximum_charge: Optional[float] = None
    currency: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class RateLinesUpdate(BaseModel):
    rate_lines_id: Optional[uuid.UUID] = None
    rate_chart_version_id: Optional[uuid.UUID] = None
    origin_zone_id: Optional[uuid.UUID] = None
    destination_zone_id: Optional[uuid.UUID] = None
    equipment_type_id: Optional[uuid.UUID] = None
    commodity_class: Optional[str] = None
    weight_break_min: Optional[float] = None
    weight_break_max: Optional[float] = None
    rate: Optional[float] = None
    rate_basis: Optional[str] = None
    minimum_charge: Optional[float] = None
    maximum_charge: Optional[float] = None
    currency: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class RateLinesOut(BaseModel):
    rate_lines_id: uuid.UUID
    rate_chart_version_id: uuid.UUID
    origin_zone_id: Optional[uuid.UUID] = None
    destination_zone_id: Optional[uuid.UUID] = None
    equipment_type_id: Optional[uuid.UUID] = None
    commodity_class: Optional[str] = None
    weight_break_min: Optional[float] = None
    weight_break_max: Optional[float] = None
    rate: float
    rate_basis: str
    minimum_charge: Optional[float] = None
    maximum_charge: Optional[float] = None
    currency: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class RateZonesCreate(BaseModel):
    rate_zones_id: uuid.UUID
    zone_code: str
    zone_name: str
    zone_type: Optional[str] = None
    postal_code_start: Optional[str] = None
    postal_code_end: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class RateZonesUpdate(BaseModel):
    rate_zones_id: Optional[uuid.UUID] = None
    zone_code: Optional[str] = None
    zone_name: Optional[str] = None
    zone_type: Optional[str] = None
    postal_code_start: Optional[str] = None
    postal_code_end: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class RateZonesOut(BaseModel):
    rate_zones_id: uuid.UUID
    zone_code: str
    zone_name: str
    zone_type: Optional[str] = None
    postal_code_start: Optional[str] = None
    postal_code_end: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class RouteAlternativesCreate(BaseModel):
    route_alternatives_id: uuid.UUID
    route_id: uuid.UUID
    alternative_route_id: uuid.UUID
    priority: Optional[int] = None
    condition_type: Optional[str] = None
    condition_value: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class RouteAlternativesUpdate(BaseModel):
    route_alternatives_id: Optional[uuid.UUID] = None
    route_id: Optional[uuid.UUID] = None
    alternative_route_id: Optional[uuid.UUID] = None
    priority: Optional[int] = None
    condition_type: Optional[str] = None
    condition_value: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class RouteAlternativesOut(BaseModel):
    route_alternatives_id: uuid.UUID
    route_id: uuid.UUID
    alternative_route_id: uuid.UUID
    priority: Optional[int] = None
    condition_type: Optional[str] = None
    condition_value: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class RouteStopsCreate(BaseModel):
    route_stops_id: uuid.UUID
    route_id: uuid.UUID
    stop_sequence: int
    stop_type: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    planned_arrival: Optional[datetime] = None
    planned_departure: Optional[datetime] = None
    distance_from_prev_miles: Optional[float] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class RouteStopsUpdate(BaseModel):
    route_stops_id: Optional[uuid.UUID] = None
    route_id: Optional[uuid.UUID] = None
    stop_sequence: Optional[int] = None
    stop_type: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    planned_arrival: Optional[datetime] = None
    planned_departure: Optional[datetime] = None
    distance_from_prev_miles: Optional[float] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class RouteStopsOut(BaseModel):
    route_stops_id: uuid.UUID
    route_id: uuid.UUID
    stop_sequence: int
    stop_type: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    planned_arrival: Optional[datetime] = None
    planned_departure: Optional[datetime] = None
    distance_from_prev_miles: Optional[float] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class RoutesCreate(BaseModel):
    routes_id: uuid.UUID
    route_code: str
    route_name: str
    lane_id: Optional[uuid.UUID] = None
    origin_location: Optional[str] = None
    destination_location: Optional[str] = None
    total_distance_miles: Optional[float] = None
    total_distance_km: Optional[float] = None
    estimated_hours: Optional[float] = None
    route_type: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class RoutesUpdate(BaseModel):
    routes_id: Optional[uuid.UUID] = None
    route_code: Optional[str] = None
    route_name: Optional[str] = None
    lane_id: Optional[uuid.UUID] = None
    origin_location: Optional[str] = None
    destination_location: Optional[str] = None
    total_distance_miles: Optional[float] = None
    total_distance_km: Optional[float] = None
    estimated_hours: Optional[float] = None
    route_type: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class RoutesOut(BaseModel):
    routes_id: uuid.UUID
    route_code: str
    route_name: str
    lane_id: Optional[uuid.UUID] = None
    origin_location: Optional[str] = None
    destination_location: Optional[str] = None
    total_distance_miles: Optional[float] = None
    total_distance_km: Optional[float] = None
    estimated_hours: Optional[float] = None
    route_type: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ShipmentAppointmentsCreate(BaseModel):
    shipment_appointments_id: uuid.UUID
    shipment_id: uuid.UUID
    appointment_type: str
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    requested_start: Optional[datetime] = None
    requested_end: Optional[datetime] = None
    confirmed_start: Optional[datetime] = None
    confirmed_end: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    dock_door: Optional[str] = None
    reference_number: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class ShipmentAppointmentsUpdate(BaseModel):
    shipment_appointments_id: Optional[uuid.UUID] = None
    shipment_id: Optional[uuid.UUID] = None
    appointment_type: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    requested_start: Optional[datetime] = None
    requested_end: Optional[datetime] = None
    confirmed_start: Optional[datetime] = None
    confirmed_end: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    dock_door: Optional[str] = None
    reference_number: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class ShipmentAppointmentsOut(BaseModel):
    shipment_appointments_id: uuid.UUID
    shipment_id: uuid.UUID
    appointment_type: str
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    requested_start: Optional[datetime] = None
    requested_end: Optional[datetime] = None
    confirmed_start: Optional[datetime] = None
    confirmed_end: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    dock_door: Optional[str] = None
    reference_number: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ShipmentLinesCreate(BaseModel):
    shipment_lines_id: uuid.UUID
    shipment_id: uuid.UUID
    line_number: int
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity: float
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    volume: Optional[float] = None
    volume_unit: Optional[str] = None
    pallets_count: Optional[int] = None
    pieces_count: Optional[int] = None
    freight_class: Optional[str] = None
    nmfc_code: Optional[str] = None
    hazmat_class_id: Optional[uuid.UUID] = None
    declared_value: Optional[float] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ShipmentLinesUpdate(BaseModel):
    shipment_lines_id: Optional[uuid.UUID] = None
    shipment_id: Optional[uuid.UUID] = None
    line_number: Optional[int] = None
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity: Optional[float] = None
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    volume: Optional[float] = None
    volume_unit: Optional[str] = None
    pallets_count: Optional[int] = None
    pieces_count: Optional[int] = None
    freight_class: Optional[str] = None
    nmfc_code: Optional[str] = None
    hazmat_class_id: Optional[uuid.UUID] = None
    declared_value: Optional[float] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ShipmentLinesOut(BaseModel):
    shipment_lines_id: uuid.UUID
    shipment_id: uuid.UUID
    line_number: int
    item_code: Optional[str] = None
    item_description: Optional[str] = None
    quantity: float
    quantity_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    volume: Optional[float] = None
    volume_unit: Optional[str] = None
    pallets_count: Optional[int] = None
    pieces_count: Optional[int] = None
    freight_class: Optional[str] = None
    nmfc_code: Optional[str] = None
    hazmat_class_id: Optional[uuid.UUID] = None
    declared_value: Optional[float] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ShipmentNotesCreate(BaseModel):
    shipment_notes_id: uuid.UUID
    shipment_id: uuid.UUID
    note_type: Optional[str] = None
    subject: Optional[str] = None
    note_text: str
    author_id: Optional[uuid.UUID] = None
    is_internal: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class ShipmentNotesUpdate(BaseModel):
    shipment_notes_id: Optional[uuid.UUID] = None
    shipment_id: Optional[uuid.UUID] = None
    note_type: Optional[str] = None
    subject: Optional[str] = None
    note_text: Optional[str] = None
    author_id: Optional[uuid.UUID] = None
    is_internal: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class ShipmentNotesOut(BaseModel):
    shipment_notes_id: uuid.UUID
    shipment_id: uuid.UUID
    note_type: Optional[str] = None
    subject: Optional[str] = None
    note_text: str
    author_id: Optional[uuid.UUID] = None
    is_internal: Optional[bool] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ShipmentStatusesCreate(BaseModel):
    shipment_statuses_id: uuid.UUID
    status_code: str
    status_name: str
    status_category: Optional[str] = None
    description: Optional[str] = None
    is_terminal: Optional[bool] = None
    display_order: Optional[int] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class ShipmentStatusesUpdate(BaseModel):
    shipment_statuses_id: Optional[uuid.UUID] = None
    status_code: Optional[str] = None
    status_name: Optional[str] = None
    status_category: Optional[str] = None
    description: Optional[str] = None
    is_terminal: Optional[bool] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class ShipmentStatusesOut(BaseModel):
    shipment_statuses_id: uuid.UUID
    status_code: str
    status_name: str
    status_category: Optional[str] = None
    description: Optional[str] = None
    is_terminal: Optional[bool] = None
    display_order: Optional[int] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ShipmentTypesCreate(BaseModel):
    shipment_types_id: uuid.UUID
    shipment_type_code: str
    shipment_type_name: str
    description: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class ShipmentTypesUpdate(BaseModel):
    shipment_types_id: Optional[uuid.UUID] = None
    shipment_type_code: Optional[str] = None
    shipment_type_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class ShipmentTypesOut(BaseModel):
    shipment_types_id: uuid.UUID
    shipment_type_code: str
    shipment_type_name: str
    description: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ShipmentsCreate(BaseModel):
    shipments_id: uuid.UUID
    shipment_number: str
    shipment_type_id: Optional[uuid.UUID] = None
    status_id: Optional[uuid.UUID] = None
    customer_id: Optional[str] = None
    customer_name: Optional[str] = None
    customer_reference: Optional[str] = None
    carrier_id: Optional[uuid.UUID] = None
    carrier_service_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    route_id: Optional[uuid.UUID] = None
    origin_city: Optional[str] = None
    origin_state: Optional[str] = None
    origin_zip: Optional[str] = None
    origin_country: Optional[str] = None
    destination_city: Optional[str] = None
    destination_state: Optional[str] = None
    destination_zip: Optional[str] = None
    destination_country: Optional[str] = None
    requested_pickup_date: Optional[datetime] = None
    requested_delivery_date: Optional[datetime] = None
    scheduled_pickup_date: Optional[datetime] = None
    scheduled_delivery_date: Optional[datetime] = None
    actual_pickup_date: Optional[datetime] = None
    actual_delivery_date: Optional[datetime] = None
    total_weight: Optional[float] = None
    weight_unit: Optional[str] = None
    total_pieces: Optional[int] = None
    total_pallets: Optional[int] = None
    total_volume: Optional[float] = None
    volume_unit: Optional[str] = None
    freight_class: Optional[str] = None
    commodity_description: Optional[str] = None
    declared_value: Optional[float] = None
    is_hazmat: Optional[bool] = None
    is_temp_controlled: Optional[bool] = None
    min_temp: Optional[float] = None
    max_temp: Optional[float] = None
    temperature_unit: Optional[str] = None
    estimated_miles: Optional[float] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    currency: Optional[str] = None
    bol_number: Optional[str] = None
    po_number: Optional[str] = None
    so_number: Optional[str] = None
    freight_terms: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class ShipmentsUpdate(BaseModel):
    shipments_id: Optional[uuid.UUID] = None
    shipment_number: Optional[str] = None
    shipment_type_id: Optional[uuid.UUID] = None
    status_id: Optional[uuid.UUID] = None
    customer_id: Optional[str] = None
    customer_name: Optional[str] = None
    customer_reference: Optional[str] = None
    carrier_id: Optional[uuid.UUID] = None
    carrier_service_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    route_id: Optional[uuid.UUID] = None
    origin_city: Optional[str] = None
    origin_state: Optional[str] = None
    origin_zip: Optional[str] = None
    origin_country: Optional[str] = None
    destination_city: Optional[str] = None
    destination_state: Optional[str] = None
    destination_zip: Optional[str] = None
    destination_country: Optional[str] = None
    requested_pickup_date: Optional[datetime] = None
    requested_delivery_date: Optional[datetime] = None
    scheduled_pickup_date: Optional[datetime] = None
    scheduled_delivery_date: Optional[datetime] = None
    actual_pickup_date: Optional[datetime] = None
    actual_delivery_date: Optional[datetime] = None
    total_weight: Optional[float] = None
    weight_unit: Optional[str] = None
    total_pieces: Optional[int] = None
    total_pallets: Optional[int] = None
    total_volume: Optional[float] = None
    volume_unit: Optional[str] = None
    freight_class: Optional[str] = None
    commodity_description: Optional[str] = None
    declared_value: Optional[float] = None
    is_hazmat: Optional[bool] = None
    is_temp_controlled: Optional[bool] = None
    min_temp: Optional[float] = None
    max_temp: Optional[float] = None
    temperature_unit: Optional[str] = None
    estimated_miles: Optional[float] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    currency: Optional[str] = None
    bol_number: Optional[str] = None
    po_number: Optional[str] = None
    so_number: Optional[str] = None
    freight_terms: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class ShipmentsOut(BaseModel):
    shipments_id: uuid.UUID
    shipment_number: str
    shipment_type_id: Optional[uuid.UUID] = None
    status_id: Optional[uuid.UUID] = None
    customer_id: Optional[str] = None
    customer_name: Optional[str] = None
    customer_reference: Optional[str] = None
    carrier_id: Optional[uuid.UUID] = None
    carrier_service_id: Optional[uuid.UUID] = None
    lane_id: Optional[uuid.UUID] = None
    route_id: Optional[uuid.UUID] = None
    origin_city: Optional[str] = None
    origin_state: Optional[str] = None
    origin_zip: Optional[str] = None
    origin_country: Optional[str] = None
    destination_city: Optional[str] = None
    destination_state: Optional[str] = None
    destination_zip: Optional[str] = None
    destination_country: Optional[str] = None
    requested_pickup_date: Optional[datetime] = None
    requested_delivery_date: Optional[datetime] = None
    scheduled_pickup_date: Optional[datetime] = None
    scheduled_delivery_date: Optional[datetime] = None
    actual_pickup_date: Optional[datetime] = None
    actual_delivery_date: Optional[datetime] = None
    total_weight: Optional[float] = None
    weight_unit: Optional[str] = None
    total_pieces: Optional[int] = None
    total_pallets: Optional[int] = None
    total_volume: Optional[float] = None
    volume_unit: Optional[str] = None
    freight_class: Optional[str] = None
    commodity_description: Optional[str] = None
    declared_value: Optional[float] = None
    is_hazmat: Optional[bool] = None
    is_temp_controlled: Optional[bool] = None
    min_temp: Optional[float] = None
    max_temp: Optional[float] = None
    temperature_unit: Optional[str] = None
    estimated_miles: Optional[float] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    currency: Optional[str] = None
    bol_number: Optional[str] = None
    po_number: Optional[str] = None
    so_number: Optional[str] = None
    freight_terms: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class TemperatureEventsCreate(BaseModel):
    temperature_events_id: uuid.UUID
    tracking_event_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    device_id: Optional[uuid.UUID] = None
    sensor_id: Optional[str] = None
    temperature: float
    temperature_unit: Optional[str] = None
    set_point: Optional[float] = None
    ambient_temperature: Optional[float] = None
    is_alert: Optional[bool] = None
    alert_type: Optional[str] = None
    event_timestamp: datetime
    notes: Optional[str] = None
    tenant_id: Optional[str] = None

class TemperatureEventsUpdate(BaseModel):
    temperature_events_id: Optional[uuid.UUID] = None
    tracking_event_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    device_id: Optional[uuid.UUID] = None
    sensor_id: Optional[str] = None
    temperature: Optional[float] = None
    temperature_unit: Optional[str] = None
    set_point: Optional[float] = None
    ambient_temperature: Optional[float] = None
    is_alert: Optional[bool] = None
    alert_type: Optional[str] = None
    event_timestamp: Optional[datetime] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None

class TemperatureEventsOut(BaseModel):
    temperature_events_id: uuid.UUID
    tracking_event_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    device_id: Optional[uuid.UUID] = None
    sensor_id: Optional[str] = None
    temperature: float
    temperature_unit: Optional[str] = None
    set_point: Optional[float] = None
    ambient_temperature: Optional[float] = None
    is_alert: Optional[bool] = None
    alert_type: Optional[str] = None
    event_timestamp: datetime
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    model_config = {"from_attributes": True}

class TenderCascadeCreate(BaseModel):
    tender_cascade_id: uuid.UUID
    tender_id: uuid.UUID
    cascade_level: int
    carrier_id: uuid.UUID
    carrier_group: Optional[str] = None
    sent_at: Optional[datetime] = None
    response_at: Optional[datetime] = None
    response_type: Optional[str] = None
    cascade_delay_minutes: Optional[int] = None
    timeout_minutes: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class TenderCascadeUpdate(BaseModel):
    tender_cascade_id: Optional[uuid.UUID] = None
    tender_id: Optional[uuid.UUID] = None
    cascade_level: Optional[int] = None
    carrier_id: Optional[uuid.UUID] = None
    carrier_group: Optional[str] = None
    sent_at: Optional[datetime] = None
    response_at: Optional[datetime] = None
    response_type: Optional[str] = None
    cascade_delay_minutes: Optional[int] = None
    timeout_minutes: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class TenderCascadeOut(BaseModel):
    tender_cascade_id: uuid.UUID
    tender_id: uuid.UUID
    cascade_level: int
    carrier_id: uuid.UUID
    carrier_group: Optional[str] = None
    sent_at: Optional[datetime] = None
    response_at: Optional[datetime] = None
    response_type: Optional[str] = None
    cascade_delay_minutes: Optional[int] = None
    timeout_minutes: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class TenderResponsesCreate(BaseModel):
    tender_responses_id: uuid.UUID
    tender_id: uuid.UUID
    carrier_id: uuid.UUID
    response_type: str
    response_date: datetime
    responded_rate: Optional[float] = None
    responded_rate_basis: Optional[str] = None
    counter_rate: Optional[float] = None
    counter_rate_basis: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class TenderResponsesUpdate(BaseModel):
    tender_responses_id: Optional[uuid.UUID] = None
    tender_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    response_type: Optional[str] = None
    response_date: Optional[datetime] = None
    responded_rate: Optional[float] = None
    responded_rate_basis: Optional[str] = None
    counter_rate: Optional[float] = None
    counter_rate_basis: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class TenderResponsesOut(BaseModel):
    tender_responses_id: uuid.UUID
    tender_id: uuid.UUID
    carrier_id: uuid.UUID
    response_type: str
    response_date: datetime
    responded_rate: Optional[float] = None
    responded_rate_basis: Optional[str] = None
    counter_rate: Optional[float] = None
    counter_rate_basis: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class TendersCreate(BaseModel):
    tenders_id: uuid.UUID
    tender_number: str
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    tender_type: str
    status: Optional[str] = None
    tender_date: datetime
    response_deadline: Optional[datetime] = None
    offered_rate: Optional[float] = None
    offered_rate_basis: Optional[str] = None
    currency: Optional[str] = None
    origin_location: Optional[str] = None
    destination_location: Optional[str] = None
    pickup_start: Optional[datetime] = None
    pickup_end: Optional[datetime] = None
    delivery_start: Optional[datetime] = None
    delivery_end: Optional[datetime] = None
    total_weight: Optional[float] = None
    equipment_type_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class TendersUpdate(BaseModel):
    tenders_id: Optional[uuid.UUID] = None
    tender_number: Optional[str] = None
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    tender_type: Optional[str] = None
    status: Optional[str] = None
    tender_date: Optional[datetime] = None
    response_deadline: Optional[datetime] = None
    offered_rate: Optional[float] = None
    offered_rate_basis: Optional[str] = None
    currency: Optional[str] = None
    origin_location: Optional[str] = None
    destination_location: Optional[str] = None
    pickup_start: Optional[datetime] = None
    pickup_end: Optional[datetime] = None
    delivery_start: Optional[datetime] = None
    delivery_end: Optional[datetime] = None
    total_weight: Optional[float] = None
    equipment_type_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class TendersOut(BaseModel):
    tenders_id: uuid.UUID
    tender_number: str
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    tender_type: str
    status: Optional[str] = None
    tender_date: datetime
    response_deadline: Optional[datetime] = None
    offered_rate: Optional[float] = None
    offered_rate_basis: Optional[str] = None
    currency: Optional[str] = None
    origin_location: Optional[str] = None
    destination_location: Optional[str] = None
    pickup_start: Optional[datetime] = None
    pickup_end: Optional[datetime] = None
    delivery_start: Optional[datetime] = None
    delivery_end: Optional[datetime] = None
    total_weight: Optional[float] = None
    equipment_type_id: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class TrackingEventsCreate(BaseModel):
    tracking_events_id: uuid.UUID
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    event_type: str
    event_code: Optional[str] = None
    event_name: Optional[str] = None
    event_description: Optional[str] = None
    event_timestamp: datetime
    location_name: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    source: Optional[str] = None
    source_detail: Optional[str] = None
    is_customer_visible: Optional[bool] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class TrackingEventsUpdate(BaseModel):
    tracking_events_id: Optional[uuid.UUID] = None
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    event_type: Optional[str] = None
    event_code: Optional[str] = None
    event_name: Optional[str] = None
    event_description: Optional[str] = None
    event_timestamp: Optional[datetime] = None
    location_name: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    source: Optional[str] = None
    source_detail: Optional[str] = None
    is_customer_visible: Optional[bool] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class TrackingEventsOut(BaseModel):
    tracking_events_id: uuid.UUID
    shipment_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    event_type: str
    event_code: Optional[str] = None
    event_name: Optional[str] = None
    event_description: Optional[str] = None
    event_timestamp: datetime
    location_name: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    source: Optional[str] = None
    source_detail: Optional[str] = None
    is_customer_visible: Optional[bool] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class TripStopsCreate(BaseModel):
    trip_stops_id: uuid.UUID
    trip_id: uuid.UUID
    load_stop_id: Optional[uuid.UUID] = None
    stop_sequence: int
    stop_type: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    planned_arrival: Optional[datetime] = None
    planned_departure: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    odometer_start: Optional[int] = None
    odometer_end: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class TripStopsUpdate(BaseModel):
    trip_stops_id: Optional[uuid.UUID] = None
    trip_id: Optional[uuid.UUID] = None
    load_stop_id: Optional[uuid.UUID] = None
    stop_sequence: Optional[int] = None
    stop_type: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    planned_arrival: Optional[datetime] = None
    planned_departure: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    odometer_start: Optional[int] = None
    odometer_end: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class TripStopsOut(BaseModel):
    trip_stops_id: uuid.UUID
    trip_id: uuid.UUID
    load_stop_id: Optional[uuid.UUID] = None
    stop_sequence: int
    stop_type: Optional[str] = None
    location_name: Optional[str] = None
    address_line1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    planned_arrival: Optional[datetime] = None
    planned_departure: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    odometer_start: Optional[int] = None
    odometer_end: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class TripsCreate(BaseModel):
    trips_id: uuid.UUID
    trip_number: str
    load_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    trip_type: Optional[str] = None
    status: Optional[str] = None
    origin_location: Optional[str] = None
    destination_location: Optional[str] = None
    scheduled_departure: Optional[datetime] = None
    scheduled_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    total_miles: Optional[float] = None
    total_duration_minutes: Optional[int] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class TripsUpdate(BaseModel):
    trips_id: Optional[uuid.UUID] = None
    trip_number: Optional[str] = None
    load_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    trip_type: Optional[str] = None
    status: Optional[str] = None
    origin_location: Optional[str] = None
    destination_location: Optional[str] = None
    scheduled_departure: Optional[datetime] = None
    scheduled_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    total_miles: Optional[float] = None
    total_duration_minutes: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class TripsOut(BaseModel):
    trips_id: uuid.UUID
    trip_number: str
    load_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    trip_type: Optional[str] = None
    status: Optional[str] = None
    origin_location: Optional[str] = None
    destination_location: Optional[str] = None
    scheduled_departure: Optional[datetime] = None
    scheduled_arrival: Optional[datetime] = None
    actual_departure: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None
    total_miles: Optional[float] = None
    total_duration_minutes: Optional[int] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class VehicleAssignmentsCreate(BaseModel):
    vehicle_assignments_id: uuid.UUID
    vehicle_id: uuid.UUID
    driver_id: Optional[uuid.UUID] = None
    assignment_type: str
    start_date: datetime
    end_date: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class VehicleAssignmentsUpdate(BaseModel):
    vehicle_assignments_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    driver_id: Optional[uuid.UUID] = None
    assignment_type: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class VehicleAssignmentsOut(BaseModel):
    vehicle_assignments_id: uuid.UUID
    vehicle_id: uuid.UUID
    driver_id: Optional[uuid.UUID] = None
    assignment_type: str
    start_date: datetime
    end_date: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class VehicleInspectionsCreate(BaseModel):
    vehicle_inspections_id: uuid.UUID
    vehicle_id: uuid.UUID
    inspection_type: str
    inspection_date: date
    inspector_name: Optional[str] = None
    inspector_company: Optional[str] = None
    location: Optional[str] = None
    odometer_at_inspection: Optional[int] = None
    result: Optional[str] = None
    defects_found: Optional[str] = None
    corrective_action: Optional[str] = None
    next_inspection_due: Optional[date] = None
    status: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class VehicleInspectionsUpdate(BaseModel):
    vehicle_inspections_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    inspection_type: Optional[str] = None
    inspection_date: Optional[date] = None
    inspector_name: Optional[str] = None
    inspector_company: Optional[str] = None
    location: Optional[str] = None
    odometer_at_inspection: Optional[int] = None
    result: Optional[str] = None
    defects_found: Optional[str] = None
    corrective_action: Optional[str] = None
    next_inspection_due: Optional[date] = None
    status: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class VehicleInspectionsOut(BaseModel):
    vehicle_inspections_id: uuid.UUID
    vehicle_id: uuid.UUID
    inspection_type: str
    inspection_date: date
    inspector_name: Optional[str] = None
    inspector_company: Optional[str] = None
    location: Optional[str] = None
    odometer_at_inspection: Optional[int] = None
    result: Optional[str] = None
    defects_found: Optional[str] = None
    corrective_action: Optional[str] = None
    next_inspection_due: Optional[date] = None
    status: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class VehicleMaintenanceCreate(BaseModel):
    vehicle_maintenance_id: uuid.UUID
    vehicle_id: uuid.UUID
    maintenance_type: str
    description: Optional[str] = None
    scheduled_date: Optional[date] = None
    completed_date: Optional[date] = None
    odometer_at_service: Optional[int] = None
    cost: Optional[float] = None
    vendor: Optional[str] = None
    work_order_number: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class VehicleMaintenanceUpdate(BaseModel):
    vehicle_maintenance_id: Optional[uuid.UUID] = None
    vehicle_id: Optional[uuid.UUID] = None
    maintenance_type: Optional[str] = None
    description: Optional[str] = None
    scheduled_date: Optional[date] = None
    completed_date: Optional[date] = None
    odometer_at_service: Optional[int] = None
    cost: Optional[float] = None
    vendor: Optional[str] = None
    work_order_number: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class VehicleMaintenanceOut(BaseModel):
    vehicle_maintenance_id: uuid.UUID
    vehicle_id: uuid.UUID
    maintenance_type: str
    description: Optional[str] = None
    scheduled_date: Optional[date] = None
    completed_date: Optional[date] = None
    odometer_at_service: Optional[int] = None
    cost: Optional[float] = None
    vendor: Optional[str] = None
    work_order_number: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class VehicleTypesCreate(BaseModel):
    vehicle_types_id: uuid.UUID
    vehicle_type_code: str
    vehicle_type_name: str
    description: Optional[str] = None
    max_gvw: Optional[float] = None
    max_payload: Optional[float] = None
    fuel_type: Optional[str] = None
    num_axles: Optional[int] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class VehicleTypesUpdate(BaseModel):
    vehicle_types_id: Optional[uuid.UUID] = None
    vehicle_type_code: Optional[str] = None
    vehicle_type_name: Optional[str] = None
    description: Optional[str] = None
    max_gvw: Optional[float] = None
    max_payload: Optional[float] = None
    fuel_type: Optional[str] = None
    num_axles: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class VehicleTypesOut(BaseModel):
    vehicle_types_id: uuid.UUID
    vehicle_type_code: str
    vehicle_type_name: str
    description: Optional[str] = None
    max_gvw: Optional[float] = None
    max_payload: Optional[float] = None
    fuel_type: Optional[str] = None
    num_axles: Optional[int] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class VehiclesCreate(BaseModel):
    vehicles_id: uuid.UUID
    vehicle_type_id: uuid.UUID
    vehicle_number: str
    vin: Optional[str] = None
    license_plate: Optional[str] = None
    license_state: Optional[str] = None
    year: Optional[int] = None
    make: Optional[str] = None
    model: Optional[str] = None
    color: Optional[str] = None
    owned_leased: Optional[str] = None
    purchase_date: Optional[date] = None
    lease_expiration: Optional[date] = None
    status: Optional[str] = None
    current_odometer: Optional[int] = None
    last_maintenance_date: Optional[date] = None
    next_maintenance_due_date: Optional[date] = None
    registration_expiration: Optional[date] = None
    insurance_expiration: Optional[date] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class VehiclesUpdate(BaseModel):
    vehicles_id: Optional[uuid.UUID] = None
    vehicle_type_id: Optional[uuid.UUID] = None
    vehicle_number: Optional[str] = None
    vin: Optional[str] = None
    license_plate: Optional[str] = None
    license_state: Optional[str] = None
    year: Optional[int] = None
    make: Optional[str] = None
    model: Optional[str] = None
    color: Optional[str] = None
    owned_leased: Optional[str] = None
    purchase_date: Optional[date] = None
    lease_expiration: Optional[date] = None
    status: Optional[str] = None
    current_odometer: Optional[int] = None
    last_maintenance_date: Optional[date] = None
    next_maintenance_due_date: Optional[date] = None
    registration_expiration: Optional[date] = None
    insurance_expiration: Optional[date] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class VehiclesOut(BaseModel):
    vehicles_id: uuid.UUID
    vehicle_type_id: uuid.UUID
    vehicle_number: str
    vin: Optional[str] = None
    license_plate: Optional[str] = None
    license_state: Optional[str] = None
    year: Optional[int] = None
    make: Optional[str] = None
    model: Optional[str] = None
    color: Optional[str] = None
    owned_leased: Optional[str] = None
    purchase_date: Optional[date] = None
    lease_expiration: Optional[date] = None
    status: Optional[str] = None
    current_odometer: Optional[int] = None
    last_maintenance_date: Optional[date] = None
    next_maintenance_due_date: Optional[date] = None
    registration_expiration: Optional[date] = None
    insurance_expiration: Optional[date] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class WorkflowApprovalHierarchiesCreate(BaseModel):
    workflow_approval_hierarchies_id: uuid.UUID
    workflow_definition_id: uuid.UUID
    level_number: int
    approver_role: Optional[str] = None
    approver_user_id: Optional[uuid.UUID] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    escalation_minutes: Optional[int] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class WorkflowApprovalHierarchiesUpdate(BaseModel):
    workflow_approval_hierarchies_id: Optional[uuid.UUID] = None
    workflow_definition_id: Optional[uuid.UUID] = None
    level_number: Optional[int] = None
    approver_role: Optional[str] = None
    approver_user_id: Optional[uuid.UUID] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    escalation_minutes: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class WorkflowApprovalHierarchiesOut(BaseModel):
    workflow_approval_hierarchies_id: uuid.UUID
    workflow_definition_id: uuid.UUID
    level_number: int
    approver_role: Optional[str] = None
    approver_user_id: Optional[uuid.UUID] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    escalation_minutes: Optional[int] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class WorkflowApprovalHistoryCreate(BaseModel):
    workflow_approval_history_id: uuid.UUID
    workflow_task_id: uuid.UUID
    approver_id: uuid.UUID
    action: str
    action_date: datetime
    comments: Optional[str] = None
    escalation_reason: Optional[str] = None
    previous_level: Optional[int] = None
    next_level: Optional[int] = None
    tenant_id: Optional[str] = None

class WorkflowApprovalHistoryUpdate(BaseModel):
    workflow_approval_history_id: Optional[uuid.UUID] = None
    workflow_task_id: Optional[uuid.UUID] = None
    approver_id: Optional[uuid.UUID] = None
    action: Optional[str] = None
    action_date: Optional[datetime] = None
    comments: Optional[str] = None
    escalation_reason: Optional[str] = None
    previous_level: Optional[int] = None
    next_level: Optional[int] = None
    tenant_id: Optional[str] = None

class WorkflowApprovalHistoryOut(BaseModel):
    workflow_approval_history_id: uuid.UUID
    workflow_task_id: uuid.UUID
    approver_id: uuid.UUID
    action: str
    action_date: datetime
    comments: Optional[str] = None
    escalation_reason: Optional[str] = None
    previous_level: Optional[int] = None
    next_level: Optional[int] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    model_config = {"from_attributes": True}

class WorkflowDefinitionsCreate(BaseModel):
    workflow_definitions_id: uuid.UUID
    workflow_code: str
    workflow_name: str
    workflow_type: str
    description: Optional[str] = None
    entity_type: Optional[str] = None
    version: Optional[int] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class WorkflowDefinitionsUpdate(BaseModel):
    workflow_definitions_id: Optional[uuid.UUID] = None
    workflow_code: Optional[str] = None
    workflow_name: Optional[str] = None
    workflow_type: Optional[str] = None
    description: Optional[str] = None
    entity_type: Optional[str] = None
    version: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class WorkflowDefinitionsOut(BaseModel):
    workflow_definitions_id: uuid.UUID
    workflow_code: str
    workflow_name: str
    workflow_type: str
    description: Optional[str] = None
    entity_type: Optional[str] = None
    version: Optional[int] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class WorkflowTasksCreate(BaseModel):
    workflow_tasks_id: uuid.UUID
    workflow_definition_id: uuid.UUID
    entity_type: str
    entity_id: uuid.UUID
    task_name: str
    task_type: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    assigned_role: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    completed_by: Optional[uuid.UUID] = None
    result: Optional[str] = None
    comments: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class WorkflowTasksUpdate(BaseModel):
    workflow_tasks_id: Optional[uuid.UUID] = None
    workflow_definition_id: Optional[uuid.UUID] = None
    entity_type: Optional[str] = None
    entity_id: Optional[uuid.UUID] = None
    task_name: Optional[str] = None
    task_type: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    assigned_role: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    completed_by: Optional[uuid.UUID] = None
    result: Optional[str] = None
    comments: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class WorkflowTasksOut(BaseModel):
    workflow_tasks_id: uuid.UUID
    workflow_definition_id: uuid.UUID
    entity_type: str
    entity_id: uuid.UUID
    task_name: str
    task_type: Optional[str] = None
    assigned_to: Optional[uuid.UUID] = None
    assigned_role: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    completed_by: Optional[uuid.UUID] = None
    result: Optional[str] = None
    comments: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class YardGateTransactionsCreate(BaseModel):
    yard_gate_transactions_id: uuid.UUID
    transaction_type: str
    equipment_id: Optional[uuid.UUID] = None
    container_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    driver_name: Optional[str] = None
    driver_license: Optional[str] = None
    vehicle_license: Optional[str] = None
    transaction_time: datetime
    facility_id: Optional[str] = None
    gate_number: Optional[str] = None
    seal_number: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class YardGateTransactionsUpdate(BaseModel):
    yard_gate_transactions_id: Optional[uuid.UUID] = None
    transaction_type: Optional[str] = None
    equipment_id: Optional[uuid.UUID] = None
    container_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    driver_name: Optional[str] = None
    driver_license: Optional[str] = None
    vehicle_license: Optional[str] = None
    transaction_time: Optional[datetime] = None
    facility_id: Optional[str] = None
    gate_number: Optional[str] = None
    seal_number: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class YardGateTransactionsOut(BaseModel):
    yard_gate_transactions_id: uuid.UUID
    transaction_type: str
    equipment_id: Optional[uuid.UUID] = None
    container_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    carrier_id: Optional[uuid.UUID] = None
    driver_name: Optional[str] = None
    driver_license: Optional[str] = None
    vehicle_license: Optional[str] = None
    transaction_time: datetime
    facility_id: Optional[str] = None
    gate_number: Optional[str] = None
    seal_number: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class YardInventoryCreate(BaseModel):
    yard_inventory_id: uuid.UUID
    yard_location_id: uuid.UUID
    equipment_id: Optional[uuid.UUID] = None
    container_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    check_in_time: datetime
    check_out_time: Optional[datetime] = None
    checked_in_by: Optional[str] = None
    checked_out_by: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class YardInventoryUpdate(BaseModel):
    yard_inventory_id: Optional[uuid.UUID] = None
    yard_location_id: Optional[uuid.UUID] = None
    equipment_id: Optional[uuid.UUID] = None
    container_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    check_in_time: Optional[datetime] = None
    check_out_time: Optional[datetime] = None
    checked_in_by: Optional[str] = None
    checked_out_by: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class YardInventoryOut(BaseModel):
    yard_inventory_id: uuid.UUID
    yard_location_id: uuid.UUID
    equipment_id: Optional[uuid.UUID] = None
    container_id: Optional[uuid.UUID] = None
    load_id: Optional[uuid.UUID] = None
    check_in_time: datetime
    check_out_time: Optional[datetime] = None
    checked_in_by: Optional[str] = None
    checked_out_by: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class YardLocationsCreate(BaseModel):
    yard_locations_id: uuid.UUID
    yard_code: str
    yard_name: Optional[str] = None
    facility_id: Optional[str] = None
    location_type: Optional[str] = None
    capacity: Optional[int] = None
    current_occupancy: Optional[int] = None
    is_active: bool = True
    tenant_id: Optional[str] = None
    object_version_number: int = 1

class YardLocationsUpdate(BaseModel):
    yard_locations_id: Optional[uuid.UUID] = None
    yard_code: Optional[str] = None
    yard_name: Optional[str] = None
    facility_id: Optional[str] = None
    location_type: Optional[str] = None
    capacity: Optional[int] = None
    current_occupancy: Optional[int] = None
    is_active: Optional[bool] = None
    tenant_id: Optional[str] = None
    object_version_number: Optional[int] = None

class YardLocationsOut(BaseModel):
    yard_locations_id: uuid.UUID
    yard_code: str
    yard_name: Optional[str] = None
    facility_id: Optional[str] = None
    location_type: Optional[str] = None
    capacity: Optional[int] = None
    current_occupancy: Optional[int] = None
    is_active: bool
    tenant_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}
