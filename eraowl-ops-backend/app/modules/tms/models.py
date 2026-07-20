import uuid
from datetime import date, datetime
from typing import Optional
from sqlalchemy import (
    BigInteger, Boolean, Column, Date, DateTime, Integer,
    String, Text, Numeric, func,
)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, JSONB
from sqlalchemy import ForeignKey
from sqlmodel import Field, SQLModel


class AccessorialCharges(SQLModel, table=True):
    __tablename__ = "accessorial_charges"
    __table_args__ = {"schema": "tms"}

    accessorial_charges_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    charge_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    charge_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    charge_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    default_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    default_basis: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class AccessorialRateLines(SQLModel, table=True):
    __tablename__ = "accessorial_rate_lines"
    __table_args__ = {"schema": "tms"}

    accessorial_rate_lines_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    rate_chart_version_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.rate_chart_versions.rate_chart_versions_id"), nullable=False))

    accessorial_charge_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.accessorial_charges.accessorial_charges_id"), nullable=False))

    amount: float = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=False))

    basis: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    min_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    effective_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class AiAgentLogs(SQLModel, table=True):
    __tablename__ = "ai_agent_logs"
    __table_args__ = {"schema": "tms"}

    ai_agent_logs_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    agent_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    agent_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    session_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    workflow_state_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.ai_workflow_state.ai_workflow_state_id"), nullable=True))

    log_level: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    message: str = Field(default=None, sa_column=Column(Text, nullable=False))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    execution_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    model_id: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    tokens_used: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    cost_estimate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    error_detail: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))


class AiDecisions(SQLModel, table=True):
    __tablename__ = "ai_decisions"
    __table_args__ = {"schema": "tms"}

    ai_decisions_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    decision_type: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    input_features: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    prediction: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    explanation: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    confidence: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    model_version: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_overridden: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    overridden_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    overridden_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    override_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    feedback_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    feedback: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class AiWorkflowState(SQLModel, table=True):
    __tablename__ = "ai_workflow_state"
    __table_args__ = {"schema": "tms"}

    ai_workflow_state_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    state_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    state_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    context_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    confidence_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CarrierAddresses(SQLModel, table=True):
    __tablename__ = "carrier_addresses"
    __table_args__ = {"schema": "tms"}

    carrier_addresses_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=False))

    address_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    address_line1: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    address_line2: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    postal_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    country: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_primary: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CarrierCertifications(SQLModel, table=True):
    __tablename__ = "carrier_certifications"
    __table_args__ = {"schema": "tms"}

    carrier_certifications_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=False))

    certification_type: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    certification_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    issuing_authority: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    issue_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CarrierContacts(SQLModel, table=True):
    __tablename__ = "carrier_contacts"
    __table_args__ = {"schema": "tms"}

    carrier_contacts_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=False))

    contact_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    first_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    title: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    email: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    mobile_phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    fax: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_primary: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CarrierContracts(SQLModel, table=True):
    __tablename__ = "carrier_contracts"
    __table_args__ = {"schema": "tms"}

    carrier_contracts_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=False))

    contract_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    contract_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    contract_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    effective_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    terms: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    auto_renew: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    pdf_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CarrierEdiCapabilities(SQLModel, table=True):
    __tablename__ = "carrier_edi_capabilities"
    __table_args__ = {"schema": "tms"}

    carrier_edi_capabilities_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=False))

    edi_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    edi_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CarrierEquipment(SQLModel, table=True):
    __tablename__ = "carrier_equipment"
    __table_args__ = {"schema": "tms"}

    carrier_equipment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=False))

    equipment_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carrier_equipment_types.carrier_equipment_types_id"), nullable=True))

    unit_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    vin: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    license_plate: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    license_state: Optional[str] = Field(default=None, sa_column=Column(String(2), nullable=True))

    year: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    make: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    model: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    owned_leased: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    purchase_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    lease_expiration: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CarrierEquipmentTypes(SQLModel, table=True):
    __tablename__ = "carrier_equipment_types"
    __table_args__ = {"schema": "tms"}

    carrier_equipment_types_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=False))

    equipment_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    equipment_type_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CarrierInsurance(SQLModel, table=True):
    __tablename__ = "carrier_insurance"
    __table_args__ = {"schema": "tms"}

    carrier_insurance_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=False))

    insurance_type: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    policy_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    provider: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    coverage_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    deductible_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    effective_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CarrierPerformance(SQLModel, table=True):
    __tablename__ = "carrier_performance"
    __table_args__ = {"schema": "tms"}

    carrier_performance_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=False))

    period_start: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_end: date = Field(default=None, sa_column=Column(Date, nullable=False))

    on_time_delivery_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    on_time_pickup_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    service_failure_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    damage_claim_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_shipments: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    avg_transit_days: Optional[float] = Field(default=None, sa_column=Column(Numeric(8, 2), nullable=True))

    tender_acceptance_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    score_category: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CarrierServiceLevels(SQLModel, table=True):
    __tablename__ = "carrier_service_levels"
    __table_args__ = {"schema": "tms"}

    carrier_service_levels_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_service_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carrier_services.carrier_services_id"), nullable=False))

    level_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    level_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    transit_days_min: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    transit_days_max: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    weight_min: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    weight_max: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CarrierServices(SQLModel, table=True):
    __tablename__ = "carrier_services"
    __table_args__ = {"schema": "tms"}

    carrier_services_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=False))

    service_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    service_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Carriers(SQLModel, table=True):
    __tablename__ = "carriers"
    __table_args__ = {"schema": "tms"}

    carriers_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    carrier_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    carrier_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    carrier_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    mc_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    dot_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    scac: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    tax_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    website: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CertificatesOfOrigin(SQLModel, table=True):
    __tablename__ = "certificates_of_origin"
    __table_args__ = {"schema": "tms"}

    certificates_of_origin_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    certificate_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    shipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=True))

    customs_declaration_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.customs_declarations.customs_declarations_id"), nullable=True))

    exporter_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    exporter_address: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    consignee_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    consignee_address: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    country_of_origin: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    country_of_destination: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    issue_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    certifying_authority: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    authorized_signatory: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    document_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.documents.documents_id"), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ClaimEvidence(SQLModel, table=True):
    __tablename__ = "claim_evidence"
    __table_args__ = {"schema": "tms"}

    claim_evidence_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    claim_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.claims.claims_id"), nullable=False))

    evidence_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    document_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.documents.documents_id"), nullable=True))

    file_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    provided_by: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    provided_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ClaimLines(SQLModel, table=True):
    __tablename__ = "claim_lines"
    __table_args__ = {"schema": "tms"}

    claim_lines_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    claim_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.claims.claims_id"), nullable=False))

    line_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    item_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    item_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    quantity_ordered: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    quantity_damaged: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    quantity_short: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    quantity_unit: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    unit_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    amount_claimed: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    amount_settled: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    damage_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    damage_cause: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class Claims(SQLModel, table=True):
    __tablename__ = "claims"
    __table_args__ = {"schema": "tms"}

    claims_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    claim_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    shipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    delivery_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.deliveries.deliveries_id"), nullable=True))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    claim_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    claim_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    reported_by: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    amount_claimed: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    amount_settled: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    amount_paid: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    priority: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    assigned_to: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    resolution_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    closed_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class ComplianceAccidents(SQLModel, table=True):
    __tablename__ = "compliance_accidents"
    __table_args__ = {"schema": "tms"}

    compliance_accidents_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    accident_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    driver_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=True))

    vehicle_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=True))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    accident_date: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    accident_type: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    location_description: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    injuries_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    fatalities_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    vehicles_involved: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    property_damage_estimate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    police_report_filed: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    police_report_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    police_department: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    was_ticketed: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    ticket_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_preventable: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ComplianceDvir(SQLModel, table=True):
    __tablename__ = "compliance_dvir"
    __table_args__ = {"schema": "tms"}

    compliance_dvir_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    dvir_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    vehicle_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=False))

    driver_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=False))

    inspection_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    inspection_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    odometer_reading: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    engine_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    trailer_equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment.equipment_id"), nullable=True))

    results: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_defect_found: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    defect_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    corrective_action: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_driver_ready: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_roadworthy: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    mechanic_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    mechanic_approved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class ComplianceEld(SQLModel, table=True):
    __tablename__ = "compliance_eld"
    __table_args__ = {"schema": "tms"}

    compliance_eld_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    driver_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=False))

    vehicle_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=True))

    eld_device_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment_tracking_devices.equipment_tracking_devices_id"), nullable=True))

    log_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    start_time: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    end_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    driving_time_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    on_duty_time_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    off_duty_time_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    sleeper_berth_time_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_miles: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    certified: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    certified_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    certified_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    data_diagnostic_indicator: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    malfunction_indicator: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    source: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class ComplianceIfta(SQLModel, table=True):
    __tablename__ = "compliance_ifta"
    __table_args__ = {"schema": "tms"}

    compliance_ifta_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    license_plate: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    license_state: str = Field(default=None, sa_column=Column(String(2), nullable=False))

    vehicle_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=True))

    report_quarter: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    report_year: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    total_miles: float = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=False))

    total_gallons: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    jurisdiction: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    jurisdiction_miles: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    jurisdiction_gallons: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    tax_due: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    tax_paid: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    net_tax: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    filing_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ComplianceViolations(SQLModel, table=True):
    __tablename__ = "compliance_violations"
    __table_args__ = {"schema": "tms"}

    compliance_violations_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    violation_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    driver_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=True))

    vehicle_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=True))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    violation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    violation_type: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    violation_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    location: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    issuing_authority: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    fine_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    points: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_preventable: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    resolution_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    resolved_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ContainerSeals(SQLModel, table=True):
    __tablename__ = "container_seals"
    __table_args__ = {"schema": "tms"}

    container_seals_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    container_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.containers.containers_id"), nullable=False))

    seal_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    seal_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    affixed_by: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    affixed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    removed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Containers(SQLModel, table=True):
    __tablename__ = "containers"
    __table_args__ = {"schema": "tms"}

    containers_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    container_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    container_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    size_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    iso_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    owner: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    operator: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    tare_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_gross_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_payload: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    last_inspection_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    next_inspection_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CustomsDeclarationLines(SQLModel, table=True):
    __tablename__ = "customs_declaration_lines"
    __table_args__ = {"schema": "tms"}

    customs_declaration_lines_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    customs_declaration_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.customs_declarations.customs_declarations_id"), nullable=False))

    line_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    hs_code_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    quantity_unit: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    weight_unit: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    country_of_origin: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tariff_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    duty_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    preference_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class CustomsDeclarations(SQLModel, table=True):
    __tablename__ = "customs_declarations"
    __table_args__ = {"schema": "tms"}

    customs_declarations_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    declaration_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    shipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=True))

    declaration_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    customs_broker: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    broker_reference: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    entry_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    port_of_entry: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    port_of_exit: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    country_of_origin: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    country_of_destination: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    incoterm_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.incoterms.incoterms_id"), nullable=True))

    total_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    total_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    weight_unit: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    total_lines: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    declaration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    clearance_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    broker_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    officer_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class Deliveries(SQLModel, table=True):
    __tablename__ = "deliveries"
    __table_args__ = {"schema": "tms"}

    deliveries_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    delivery_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    shipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    delivery_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    delivery_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    location_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    address_line1: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    postal_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    country: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    signed_by: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    signed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    recipient_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    total_packages: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_pallets: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class DeliveryLines(SQLModel, table=True):
    __tablename__ = "delivery_lines"
    __table_args__ = {"schema": "tms"}

    delivery_lines_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    delivery_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.deliveries.deliveries_id"), nullable=False))

    shipment_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipment_lines.shipment_lines_id"), nullable=True))

    line_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    item_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    item_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    quantity_ordered: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    quantity_delivered: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    quantity_damaged: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    quantity_short: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    quantity_unit: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    weight_unit: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    condition: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class Dispatches(SQLModel, table=True):
    __tablename__ = "dispatches"
    __table_args__ = {"schema": "tms"}

    dispatches_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    dispatch_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    trip_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.trips.trips_id"), nullable=True))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    driver_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=True))

    vehicle_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=True))

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment.equipment_id"), nullable=True))

    dispatch_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    dispatched_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    acknowledged_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    arrived_at_origin: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    departed_origin: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    arrived_at_destination: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    instructions: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class DockAppointments(SQLModel, table=True):
    __tablename__ = "dock_appointments"
    __table_args__ = {"schema": "tms"}

    dock_appointments_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    dock_door_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.dock_doors.dock_doors_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    appointment_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    scheduled_start: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    scheduled_end: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    actual_arrival: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_departure: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class DockDoors(SQLModel, table=True):
    __tablename__ = "dock_doors"
    __table_args__ = {"schema": "tms"}

    dock_doors_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    door_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    door_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    facility_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    facility_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    door_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    location: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    capacity: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    current_occupancy: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class DocumentDistribution(SQLModel, table=True):
    __tablename__ = "document_distribution"
    __table_args__ = {"schema": "tms"}

    document_distribution_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    document_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.documents.documents_id"), nullable=False))

    distribution_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    recipient_email: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    recipient_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    sent_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    delivery_method: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class DocumentTypes(SQLModel, table=True):
    __tablename__ = "document_types"
    __table_args__ = {"schema": "tms"}

    document_types_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    document_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    document_type_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    retention_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_required: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Documents(SQLModel, table=True):
    __tablename__ = "documents"
    __table_args__ = {"schema": "tms"}

    documents_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    document_type_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.document_types.document_types_id"), nullable=False))

    document_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    document_title: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    file_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    file_path: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    file_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    file_size_bytes: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    mime_type: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    checksum: Optional[str] = Field(default=None, sa_column=Column(String(64), nullable=True))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class DriverCertifications(SQLModel, table=True):
    __tablename__ = "driver_certifications"
    __table_args__ = {"schema": "tms"}

    driver_certifications_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    driver_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=False))

    certification_type: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    certification_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    issuing_authority: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    issue_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class DriverHos(SQLModel, table=True):
    __tablename__ = "driver_hos"
    __table_args__ = {"schema": "tms"}

    driver_hos_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    driver_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=False))

    log_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    duty_status: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    status_start_time: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    status_end_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    driving_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    on_duty_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    off_duty_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    sleeper_berth_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_miles_driven: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    eld_log_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    source: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_violation: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    violation_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class DriverPayroll(SQLModel, table=True):
    __tablename__ = "driver_payroll"
    __table_args__ = {"schema": "tms"}

    driver_payroll_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    driver_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=False))

    pay_period_start: date = Field(default=None, sa_column=Column(Date, nullable=False))

    pay_period_end: date = Field(default=None, sa_column=Column(Date, nullable=False))

    pay_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    pay_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    regular_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    overtime_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    miles_driven: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    stops_completed: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    loads_completed: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    gross_pay: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    deductions: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    net_pay: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    adjustment_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    adjustment_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    processed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class DriverTraining(SQLModel, table=True):
    __tablename__ = "driver_training"
    __table_args__ = {"schema": "tms"}

    driver_training_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    driver_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=False))

    training_type: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    training_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    provider: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    completion_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    certificate_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Drivers(SQLModel, table=True):
    __tablename__ = "drivers"
    __table_args__ = {"schema": "tms"}

    drivers_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    driver_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    first_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    last_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    middle_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    date_of_birth: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    ssn_last_four: Optional[str] = Field(default=None, sa_column=Column(String(4), nullable=True))

    employee_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    license_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    license_state: Optional[str] = Field(default=None, sa_column=Column(String(2), nullable=True))

    license_class: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    license_endorsements: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    license_expiration: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    medical_cert_expiration: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    hire_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    termination_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    driver_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    email: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    mobile_phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    home_terminal: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Equipment(SQLModel, table=True):
    __tablename__ = "equipment"
    __table_args__ = {"schema": "tms"}

    equipment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_type_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment_types.equipment_types_id"), nullable=False))

    asset_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    vin: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    license_plate: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    license_state: Optional[str] = Field(default=None, sa_column=Column(String(2), nullable=True))

    year: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    make: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    model: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    owned_leased: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    purchase_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    lease_expiration: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    current_odometer: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    last_inspection_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    next_inspection_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class EquipmentAssignments(SQLModel, table=True):
    __tablename__ = "equipment_assignments"
    __table_args__ = {"schema": "tms"}

    equipment_assignments_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment.equipment_id"), nullable=False))

    assignment_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    assigned_to_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    assigned_to_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    start_date: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    end_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class EquipmentTrackingDevices(SQLModel, table=True):
    __tablename__ = "equipment_tracking_devices"
    __table_args__ = {"schema": "tms"}

    equipment_tracking_devices_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment.equipment_id"), nullable=False))

    device_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    device_serial: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    device_identifier: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    provider: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    install_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    last_communication: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    battery_level: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class EquipmentTypes(SQLModel, table=True):
    __tablename__ = "equipment_types"
    __table_args__ = {"schema": "tms"}

    equipment_types_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    equipment_type_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    equipment_category: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    max_gross_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_payload_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_capacity_cu_ft: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    length_inches: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    width_inches: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    height_inches: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class FreightAudit(SQLModel, table=True):
    __tablename__ = "freight_audit"
    __table_args__ = {"schema": "tms"}

    freight_audit_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    freight_invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.freight_invoices.freight_invoices_id"), nullable=False))

    audit_date: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    auditor_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    audit_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    result: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    original_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    audited_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    difference_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    discrepancy_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    resolution_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_auto_audited: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    auto_audit_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class FreightCostAllocations(SQLModel, table=True):
    __tablename__ = "freight_cost_allocations"
    __table_args__ = {"schema": "tms"}

    freight_cost_allocations_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    freight_cost_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.freight_cost_lines.freight_cost_lines_id"), nullable=True))

    shipment_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipment_lines.shipment_lines_id"), nullable=True))

    load_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.load_lines.load_lines_id"), nullable=True))

    allocation_percent: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    allocated_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class FreightCostLines(SQLModel, table=True):
    __tablename__ = "freight_cost_lines"
    __table_args__ = {"schema": "tms"}

    freight_cost_lines_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    freight_cost_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.freight_costs.freight_costs_id"), nullable=False))

    line_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    charge_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    charge_description: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    basis: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class FreightCosts(SQLModel, table=True):
    __tablename__ = "freight_costs"
    __table_args__ = {"schema": "tms"}

    freight_costs_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    shipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    cost_category: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    cost_type: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    cost_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    vendor: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    reference_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    billable_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    paid_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    paid_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class FreightInvoiceLines(SQLModel, table=True):
    __tablename__ = "freight_invoice_lines"
    __table_args__ = {"schema": "tms"}

    freight_invoice_lines_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    freight_invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.freight_invoices.freight_invoices_id"), nullable=False))

    line_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    charge_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    reference: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class FreightInvoices(SQLModel, table=True):
    __tablename__ = "freight_invoices"
    __table_args__ = {"schema": "tms"}

    freight_invoices_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    invoice_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    shipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    invoice_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    total_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    total_paid: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    balance_due: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    invoice_received_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    invoice_image_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    reference_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class FuelConsumption(SQLModel, table=True):
    __tablename__ = "fuel_consumption"
    __table_args__ = {"schema": "tms"}

    fuel_consumption_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    vehicle_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=False))

    trip_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.trips.trips_id"), nullable=True))

    period_start: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    period_end: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    gallons_consumed: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    miles_driven: float = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=False))

    mpg: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 4), nullable=True))

    idle_time_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    engine_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    cost_total: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    cost_per_mile: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    fuel_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class FuelSurchargeLines(SQLModel, table=True):
    __tablename__ = "fuel_surcharge_lines"
    __table_args__ = {"schema": "tms"}

    fuel_surcharge_lines_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    fuel_surcharge_table_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.fuel_surcharge_tables.fuel_surcharge_tables_id"), nullable=False))

    fuel_price_min: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    fuel_price_max: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    surcharge_amount: float = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=False))

    surcharge_percent: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class FuelSurchargeTables(SQLModel, table=True):
    __tablename__ = "fuel_surcharge_tables"
    __table_args__ = {"schema": "tms"}

    fuel_surcharge_tables_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    table_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    table_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    base_fuel_price: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    trigger_increment: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    surcharge_basis: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    effective_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class FuelTransactions(SQLModel, table=True):
    __tablename__ = "fuel_transactions"
    __table_args__ = {"schema": "tms"}

    fuel_transactions_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    transaction_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    vehicle_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=True))

    driver_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    fuel_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    fuel_date: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    location_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    gallons: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    price_per_gallon: float = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=False))

    total_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    odometer_reading: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    vendor: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    receipt_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    payment_method: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class GeofenceEvents(SQLModel, table=True):
    __tablename__ = "geofence_events"
    __table_args__ = {"schema": "tms"}

    geofence_events_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tracking_event_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.tracking_events.tracking_events_id"), nullable=True))

    geofence_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    geofence_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    facility_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    facility_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    event_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    event_timestamp: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    source: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))


class GpsPings(SQLModel, table=True):
    __tablename__ = "gps_pings"
    __table_args__ = {"schema": "tms"}

    gps_pings_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment.equipment_id"), nullable=True))

    vehicle_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=True))

    driver_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    device_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment_tracking_devices.equipment_tracking_devices_id"), nullable=True))

    ping_timestamp: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    latitude: float = Field(default=None, sa_column=Column(Numeric(10, 7), nullable=False))

    longitude: float = Field(default=None, sa_column=Column(Numeric(10, 7), nullable=False))

    altitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    speed: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    heading: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    accuracy: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    odometer: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    engine_on: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    ignition_on: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    battery_voltage: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    source: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))


class HazmatClassifications(SQLModel, table=True):
    __tablename__ = "hazmat_classifications"
    __table_args__ = {"schema": "tms"}

    hazmat_classifications_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    class_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    class_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    hazard_class: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    division: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class HazmatIncidents(SQLModel, table=True):
    __tablename__ = "hazmat_incidents"
    __table_args__ = {"schema": "tms"}

    hazmat_incidents_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    incident_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    shipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    hazmat_classification_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.hazmat_classifications.hazmat_classifications_id"), nullable=True))

    un_number: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    incident_date: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    incident_type: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    immediate_cause: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    corrective_action: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    injuries_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    fatalities_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    property_damage_estimate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    environmental_damage: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    evacuation_required: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    reported_to_authorities: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    authority_report_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class HazmatPackaging(SQLModel, table=True):
    __tablename__ = "hazmat_packaging"
    __table_args__ = {"schema": "tms"}

    hazmat_packaging_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    hazmat_classification_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.hazmat_classifications.hazmat_classifications_id"), nullable=False))

    un_number: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    proper_shipping_name: str = Field(default=None, sa_column=Column(Text, nullable=False))

    technical_name: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    hazard_class: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    packing_group: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    labeling_required: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    placarding_required: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    packaging_instructions: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    quantity_limit_transport: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    quantity_limit_unit: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    emergency_response_guide: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class HazmatSegregation(SQLModel, table=True):
    __tablename__ = "hazmat_segregation"
    __table_args__ = {"schema": "tms"}

    hazmat_segregation_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    class_a: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    class_b: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    segregation_rule: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_segregated: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class HsCodes(SQLModel, table=True):
    __tablename__ = "hs_codes"
    __table_args__ = {"schema": "tms"}

    hs_codes_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    hs_code: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    chapter: Optional[str] = Field(default=None, sa_column=Column(String(2), nullable=True))

    heading: Optional[str] = Field(default=None, sa_column=Column(String(4), nullable=True))

    subheading: Optional[str] = Field(default=None, sa_column=Column(String(6), nullable=True))

    duty_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    unit_of_measure: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Incoterms(SQLModel, table=True):
    __tablename__ = "incoterms"
    __table_args__ = {"schema": "tms"}

    incoterms_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    incoterm_code: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    incoterm_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    risk_transfer_point: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    cost_allocation: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class InsurancePolicies(SQLModel, table=True):
    __tablename__ = "insurance_policies"
    __table_args__ = {"schema": "tms"}

    insurance_policies_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    policy_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    provider: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    policy_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    coverage_type: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    coverage_limit: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    deductible: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    premium_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    effective_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    expiration_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class InterfaceErrorLog(SQLModel, table=True):
    __tablename__ = "interface_error_log"
    __table_args__ = {"schema": "tms"}

    interface_error_log_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    source_system: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    interface_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    error_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    error_message: str = Field(default=None, sa_column=Column(Text, nullable=False))

    error_detail: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    severity: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    endpoint: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    request_payload: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    response_payload: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    http_status: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    resolved: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    resolved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    resolved_by: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class InterfaceShipmentImport(SQLModel, table=True):
    __tablename__ = "interface_shipment_import"
    __table_args__ = {"schema": "tms"}

    interface_shipment_import_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    batch_id: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    source_system: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    source_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    payload: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    validation_result: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    shipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=True))

    processed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    processed_by: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    retry_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class KpiDefinitions(SQLModel, table=True):
    __tablename__ = "kpi_definitions"
    __table_args__ = {"schema": "tms"}

    kpi_definitions_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    kpi_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    kpi_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    kpi_category: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    formula: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    unit: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    higher_is_better: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    warning_threshold: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    critical_threshold: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    frequency: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class KpiValues(SQLModel, table=True):
    __tablename__ = "kpi_values"
    __table_args__ = {"schema": "tms"}

    kpi_values_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    kpi_definition_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.kpi_definitions.kpi_definitions_id"), nullable=False))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    lane_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.lanes.lanes_id"), nullable=True))

    driver_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=True))

    period_start: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_end: date = Field(default=None, sa_column=Column(Date, nullable=False))

    actual_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    variance: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    variance_percent: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    is_target_achieved: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class LaneCarriers(SQLModel, table=True):
    __tablename__ = "lane_carriers"
    __table_args__ = {"schema": "tms"}

    lane_carriers_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    lane_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.lanes.lanes_id"), nullable=False))

    carrier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=False))

    carrier_service_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carrier_services.carrier_services_id"), nullable=True))

    is_preferred: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_contracted: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    contract_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    transit_days_min: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    transit_days_max: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    effective_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class LanePerformance(SQLModel, table=True):
    __tablename__ = "lane_performance"
    __table_args__ = {"schema": "tms"}

    lane_performance_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    lane_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.lanes.lanes_id"), nullable=False))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    period_start: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_end: date = Field(default=None, sa_column=Column(Date, nullable=False))

    total_shipments: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    on_time_deliveries: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    on_time_pickups: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    avg_transit_days: Optional[float] = Field(default=None, sa_column=Column(Numeric(8, 2), nullable=True))

    min_transit_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    max_transit_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    damage_claims: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    avg_cost_per_mile: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    avg_cost_per_load: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Lanes(SQLModel, table=True):
    __tablename__ = "lanes"
    __table_args__ = {"schema": "tms"}

    lanes_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    lane_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    lane_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    origin_city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    origin_state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    origin_zip: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    origin_country: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    destination_city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    destination_state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    destination_zip: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    destination_country: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    distance_miles: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    distance_km: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    transit_days_min: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    transit_days_max: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    lane_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class LoadCosts(SQLModel, table=True):
    __tablename__ = "load_costs"
    __table_args__ = {"schema": "tms"}

    load_costs_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    load_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=False))

    cost_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    vendor: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    billable: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    billable_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    reference_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class LoadLegs(SQLModel, table=True):
    __tablename__ = "load_legs"
    __table_args__ = {"schema": "tms"}

    load_legs_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    load_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=False))

    leg_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    from_stop_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.load_stops.load_stops_id"), nullable=True))

    to_stop_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.load_stops.load_stops_id"), nullable=True))

    mode: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    distance_miles: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    estimated_duration_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    actual_duration_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class LoadLines(SQLModel, table=True):
    __tablename__ = "load_lines"
    __table_args__ = {"schema": "tms"}

    load_lines_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    load_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=False))

    shipment_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipment_lines.shipment_lines_id"), nullable=True))

    line_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    item_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    item_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    quantity_unit: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    weight_unit: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    volume: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    volume_unit: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    pallets_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    pieces_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    freight_class: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class LoadStops(SQLModel, table=True):
    __tablename__ = "load_stops"
    __table_args__ = {"schema": "tms"}

    load_stops_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    load_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=False))

    stop_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    stop_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    location_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    address_line1: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    postal_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    country: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    contact_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    contact_phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    appointment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipment_appointments.shipment_appointments_id"), nullable=True))

    planned_arrival: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    planned_departure: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_arrival: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_departure: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    arrived_miles: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Loads(SQLModel, table=True):
    __tablename__ = "loads"
    __table_args__ = {"schema": "tms"}

    loads_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    load_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    shipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=True))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    driver_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=True))

    vehicle_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=True))

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment.equipment_id"), nullable=True))

    route_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.routes.routes_id"), nullable=True))

    load_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    origin_location: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    destination_location: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    scheduled_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    scheduled_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    total_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_pieces: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_pallets: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_miles: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    estimated_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    actual_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    carrier_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    revenue: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    bol_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    po_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_hazmat: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_temp_controlled: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MilestoneAchievements(SQLModel, table=True):
    __tablename__ = "milestone_achievements"
    __table_args__ = {"schema": "tms"}

    milestone_achievements_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    milestone_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.milestones.milestones_id"), nullable=False))

    shipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    tracking_event_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.tracking_events.tracking_events_id"), nullable=True))

    planned_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    achieved_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    variance_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_on_time: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Milestones(SQLModel, table=True):
    __tablename__ = "milestones"
    __table_args__ = {"schema": "tms"}

    milestones_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    milestone_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    milestone_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    milestone_category: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_required: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_customer_visible: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    display_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    sla_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class PickupLines(SQLModel, table=True):
    __tablename__ = "pickup_lines"
    __table_args__ = {"schema": "tms"}

    pickup_lines_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    pickup_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.pickups.pickups_id"), nullable=False))

    shipment_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipment_lines.shipment_lines_id"), nullable=True))

    line_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    item_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    item_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    quantity_expected: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    quantity_picked_up: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    quantity_unit: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    weight_unit: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    condition: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Pickups(SQLModel, table=True):
    __tablename__ = "pickups"
    __table_args__ = {"schema": "tms"}

    pickups_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    pickup_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    shipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    pickup_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    location_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    address_line1: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    postal_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    country: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    contact_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    contact_phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    pickup_appointment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipment_appointments.shipment_appointments_id"), nullable=True))

    scheduled_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    scheduled_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_arrival: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_departure: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    total_packages: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_pallets: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    signed_by: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    signed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Pod(SQLModel, table=True):
    __tablename__ = "pod"
    __table_args__ = {"schema": "tms"}

    pod_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    delivery_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.deliveries.deliveries_id"), nullable=False))

    pod_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    signed_by: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    signed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    signature_image_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    delivered_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    condition_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    exceptions: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_physical_pod: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    physical_pod_location: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    document_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class RateChartVersions(SQLModel, table=True):
    __tablename__ = "rate_chart_versions"
    __table_args__ = {"schema": "tms"}

    rate_chart_versions_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    rate_chart_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.rate_charts.rate_charts_id"), nullable=False))

    version_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    version_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    effective_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    change_summary: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    approved_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    approved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class RateCharts(SQLModel, table=True):
    __tablename__ = "rate_charts"
    __table_args__ = {"schema": "tms"}

    rate_charts_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    rate_chart_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    rate_chart_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    contract_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carrier_contracts.carrier_contracts_id"), nullable=True))

    rate_chart_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    effective_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class RateLines(SQLModel, table=True):
    __tablename__ = "rate_lines"
    __table_args__ = {"schema": "tms"}

    rate_lines_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    rate_chart_version_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.rate_chart_versions.rate_chart_versions_id"), nullable=False))

    origin_zone_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    destination_zone_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    equipment_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment_types.equipment_types_id"), nullable=True))

    commodity_class: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    weight_break_min: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    weight_break_max: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rate: float = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=False))

    rate_basis: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    minimum_charge: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    maximum_charge: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class RateZones(SQLModel, table=True):
    __tablename__ = "rate_zones"
    __table_args__ = {"schema": "tms"}

    rate_zones_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    zone_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    zone_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    zone_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    postal_code_start: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    postal_code_end: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    region: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    country: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class RouteAlternatives(SQLModel, table=True):
    __tablename__ = "route_alternatives"
    __table_args__ = {"schema": "tms"}

    route_alternatives_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    route_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.routes.routes_id"), nullable=False))

    alternative_route_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.routes.routes_id"), nullable=False))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    condition_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    condition_value: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class RouteStops(SQLModel, table=True):
    __tablename__ = "route_stops"
    __table_args__ = {"schema": "tms"}

    route_stops_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    route_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.routes.routes_id"), nullable=False))

    stop_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    stop_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    location_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    address_line1: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    postal_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    country: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    planned_arrival: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    planned_departure: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    distance_from_prev_miles: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Routes(SQLModel, table=True):
    __tablename__ = "routes"
    __table_args__ = {"schema": "tms"}

    routes_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    route_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    route_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    lane_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.lanes.lanes_id"), nullable=True))

    origin_location: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    destination_location: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    total_distance_miles: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    total_distance_km: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    estimated_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    route_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ShipmentAppointments(SQLModel, table=True):
    __tablename__ = "shipment_appointments"
    __table_args__ = {"schema": "tms"}

    shipment_appointments_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    shipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=False))

    appointment_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    location_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    address_line1: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    postal_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    country: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    contact_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    contact_phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    requested_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    requested_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    confirmed_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    confirmed_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_arrival: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_departure: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    dock_door: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    reference_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ShipmentLines(SQLModel, table=True):
    __tablename__ = "shipment_lines"
    __table_args__ = {"schema": "tms"}

    shipment_lines_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    shipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=False))

    line_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    item_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    item_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    quantity_unit: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    weight_unit: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    volume: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    volume_unit: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    pallets_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    pieces_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    freight_class: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    nmfc_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    hazmat_class_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    declared_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class ShipmentNotes(SQLModel, table=True):
    __tablename__ = "shipment_notes"
    __table_args__ = {"schema": "tms"}

    shipment_notes_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    shipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=False))

    note_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    subject: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    note_text: str = Field(default=None, sa_column=Column(Text, nullable=False))

    author_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_internal: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ShipmentStatuses(SQLModel, table=True):
    __tablename__ = "shipment_statuses"
    __table_args__ = {"schema": "tms"}

    shipment_statuses_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    status_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    status_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    status_category: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_terminal: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    display_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ShipmentTypes(SQLModel, table=True):
    __tablename__ = "shipment_types"
    __table_args__ = {"schema": "tms"}

    shipment_types_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    shipment_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    shipment_type_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Shipments(SQLModel, table=True):
    __tablename__ = "shipments"
    __table_args__ = {"schema": "tms"}

    shipments_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    shipment_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    shipment_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipment_types.shipment_types_id"), nullable=True))

    status_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipment_statuses.shipment_statuses_id"), nullable=True))

    customer_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    customer_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    customer_reference: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    carrier_service_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carrier_services.carrier_services_id"), nullable=True))

    lane_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.lanes.lanes_id"), nullable=True))

    route_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.routes.routes_id"), nullable=True))

    origin_city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    origin_state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    origin_zip: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    origin_country: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    destination_city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    destination_state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    destination_zip: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    destination_country: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    requested_pickup_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    requested_delivery_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    scheduled_pickup_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    scheduled_delivery_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_pickup_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_delivery_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    total_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    weight_unit: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    total_pieces: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_pallets: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_volume: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    volume_unit: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    freight_class: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    commodity_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    declared_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_hazmat: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_temp_controlled: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    min_temp: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    max_temp: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    temperature_unit: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    estimated_miles: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    estimated_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    actual_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    bol_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    po_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    so_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    freight_terms: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class TemperatureEvents(SQLModel, table=True):
    __tablename__ = "temperature_events"
    __table_args__ = {"schema": "tms"}

    temperature_events_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tracking_event_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.tracking_events.tracking_events_id"), nullable=True))

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment.equipment_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    device_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment_tracking_devices.equipment_tracking_devices_id"), nullable=True))

    sensor_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    temperature: float = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=False))

    temperature_unit: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    set_point: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    ambient_temperature: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    is_alert: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    alert_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    event_timestamp: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))


class TenderCascade(SQLModel, table=True):
    __tablename__ = "tender_cascade"
    __table_args__ = {"schema": "tms"}

    tender_cascade_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tender_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.tenders.tenders_id"), nullable=False))

    cascade_level: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    carrier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=False))

    carrier_group: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    sent_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    response_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    response_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    cascade_delay_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    timeout_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class TenderResponses(SQLModel, table=True):
    __tablename__ = "tender_responses"
    __table_args__ = {"schema": "tms"}

    tender_responses_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tender_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.tenders.tenders_id"), nullable=False))

    carrier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=False))

    response_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    response_date: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    responded_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    responded_rate_basis: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    counter_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    counter_rate_basis: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Tenders(SQLModel, table=True):
    __tablename__ = "tenders"
    __table_args__ = {"schema": "tms"}

    tenders_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tender_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    shipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    tender_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    tender_date: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    response_deadline: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    offered_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    offered_rate_basis: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    origin_location: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    destination_location: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    pickup_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    pickup_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    delivery_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    delivery_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    total_weight: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    equipment_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment_types.equipment_types_id"), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class TrackingEvents(SQLModel, table=True):
    __tablename__ = "tracking_events"
    __table_args__ = {"schema": "tms"}

    tracking_events_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    shipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.shipments.shipments_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    event_type: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    event_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    event_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    event_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    event_timestamp: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    location_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    postal_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    country: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    latitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 7), nullable=True))

    longitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 7), nullable=True))

    source: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    source_detail: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    is_customer_visible: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class TripStops(SQLModel, table=True):
    __tablename__ = "trip_stops"
    __table_args__ = {"schema": "tms"}

    trip_stops_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    trip_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.trips.trips_id"), nullable=False))

    load_stop_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.load_stops.load_stops_id"), nullable=True))

    stop_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    stop_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    location_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    address_line1: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    postal_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    country: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    planned_arrival: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    planned_departure: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_arrival: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_departure: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    odometer_start: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    odometer_end: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Trips(SQLModel, table=True):
    __tablename__ = "trips"
    __table_args__ = {"schema": "tms"}

    trips_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    trip_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    driver_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.drivers.drivers_id"), nullable=True))

    vehicle_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=True))

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment.equipment_id"), nullable=True))

    trip_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    origin_location: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    destination_location: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    scheduled_departure: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    scheduled_arrival: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_departure: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_arrival: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    total_miles: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    total_duration_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class VehicleAssignments(SQLModel, table=True):
    __tablename__ = "vehicle_assignments"
    __table_args__ = {"schema": "tms"}

    vehicle_assignments_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    vehicle_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=False))

    driver_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    assignment_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    start_date: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    end_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class VehicleInspections(SQLModel, table=True):
    __tablename__ = "vehicle_inspections"
    __table_args__ = {"schema": "tms"}

    vehicle_inspections_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    vehicle_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=False))

    inspection_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    inspection_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    inspector_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    inspector_company: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    location: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    odometer_at_inspection: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    result: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    defects_found: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    corrective_action: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    next_inspection_due: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class VehicleMaintenance(SQLModel, table=True):
    __tablename__ = "vehicle_maintenance"
    __table_args__ = {"schema": "tms"}

    vehicle_maintenance_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    vehicle_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicles.vehicles_id"), nullable=False))

    maintenance_type: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    scheduled_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    completed_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    odometer_at_service: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    vendor: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    work_order_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class VehicleTypes(SQLModel, table=True):
    __tablename__ = "vehicle_types"
    __table_args__ = {"schema": "tms"}

    vehicle_types_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    vehicle_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    vehicle_type_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    max_gvw: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_payload: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    fuel_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    num_axles: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Vehicles(SQLModel, table=True):
    __tablename__ = "vehicles"
    __table_args__ = {"schema": "tms"}

    vehicles_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    vehicle_type_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.vehicle_types.vehicle_types_id"), nullable=False))

    vehicle_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    vin: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    license_plate: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    license_state: Optional[str] = Field(default=None, sa_column=Column(String(2), nullable=True))

    year: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    make: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    model: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    color: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    owned_leased: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    purchase_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    lease_expiration: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    current_odometer: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    last_maintenance_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    next_maintenance_due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    registration_expiration: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    insurance_expiration: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class WorkflowApprovalHierarchies(SQLModel, table=True):
    __tablename__ = "workflow_approval_hierarchies"
    __table_args__ = {"schema": "tms"}

    workflow_approval_hierarchies_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_definition_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.workflow_definitions.workflow_definitions_id"), nullable=False))

    level_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    approver_role: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approver_user_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    min_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    escalation_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class WorkflowApprovalHistory(SQLModel, table=True):
    __tablename__ = "workflow_approval_history"
    __table_args__ = {"schema": "tms"}

    workflow_approval_history_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_task_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.workflow_tasks.workflow_tasks_id"), nullable=False))

    approver_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    action: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    action_date: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    comments: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    escalation_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    previous_level: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    next_level: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))


class WorkflowDefinitions(SQLModel, table=True):
    __tablename__ = "workflow_definitions"
    __table_args__ = {"schema": "tms"}

    workflow_definitions_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    workflow_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    workflow_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    version: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class WorkflowTasks(SQLModel, table=True):
    __tablename__ = "workflow_tasks"
    __table_args__ = {"schema": "tms"}

    workflow_tasks_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_definition_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.workflow_definitions.workflow_definitions_id"), nullable=False))

    entity_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    entity_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    task_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    task_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    assigned_to: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    assigned_role: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    priority: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    due_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    result: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    comments: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class YardGateTransactions(SQLModel, table=True):
    __tablename__ = "yard_gate_transactions"
    __table_args__ = {"schema": "tms"}

    yard_gate_transactions_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    transaction_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment.equipment_id"), nullable=True))

    container_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.containers.containers_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    carrier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.carriers.carriers_id"), nullable=True))

    driver_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    driver_license: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    vehicle_license: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    transaction_time: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    facility_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    gate_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    seal_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class YardInventory(SQLModel, table=True):
    __tablename__ = "yard_inventory"
    __table_args__ = {"schema": "tms"}

    yard_inventory_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    yard_location_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.yard_locations.yard_locations_id"), nullable=False))

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.equipment.equipment_id"), nullable=True))

    container_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.containers.containers_id"), nullable=True))

    load_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tms.loads.loads_id"), nullable=True))

    check_in_time: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    check_out_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    checked_in_by: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    checked_out_by: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class YardLocations(SQLModel, table=True):
    __tablename__ = "yard_locations"
    __table_args__ = {"schema": "tms"}

    yard_locations_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    yard_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    yard_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    facility_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    location_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    capacity: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    current_occupancy: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

