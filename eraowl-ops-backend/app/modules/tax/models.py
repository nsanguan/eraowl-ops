import uuid
from datetime import date, datetime, time
from typing import Optional, List, Dict, Any
from sqlalchemy import (
    BigInteger, Boolean, Column, Date, DateTime, Float, Integer,
    SmallInteger, String, Text, Time, Interval, LargeBinary,
    Numeric, ARRAY, func,
)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, JSONB, JSON
from sqlalchemy import ForeignKey
from sqlmodel import Field, SQLModel


class PartnerTaxProfiles(SQLModel, table=True):
    __tablename__ = "partner_tax_profiles"
    __table_args__ = {"schema": "tax"}

    partner_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tax_registration_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    tax_entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_tax_exempt: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    tax_exempt_certificate: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tax_exempt_reason: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    tax_authority: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    withholding_tax_rate_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    default_wht_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxAccounts(SQLModel, table=True):
    __tablename__ = "tax_accounts"
    __table_args__ = {"schema": "tax"}

    tax_account_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    account_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    account_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    account_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=True))

    tax_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_types.tax_type_id"), nullable=True))

    tax_jurisdiction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_jurisdictions.tax_jurisdiction_id"), nullable=True))

    gl_account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_default: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxAgentDefinitions(SQLModel, table=True):
    __tablename__ = "tax_agent_definitions"
    __table_args__ = {"schema": "tax"}

    agent_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    agent_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    agent_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    system_prompt: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    llm_config_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_llm_configs.llm_config_id"), nullable=True))

    tools: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    memory_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxAiAgentLogs(SQLModel, table=True):
    __tablename__ = "tax_ai_agent_logs"
    __table_args__ = {"schema": "tax"}

    log_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    agent_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    input_summary: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    output_summary: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    llm_calls: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_tokens: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_cost_usd: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 6), nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxAiDecisions(SQLModel, table=True):
    __tablename__ = "tax_ai_decisions"
    __table_args__ = {"schema": "tax"}

    decision_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    decision_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    confidence: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    model_used: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    human_reviewed: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    human_decision: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxAiModelRegistry(SQLModel, table=True):
    __tablename__ = "tax_ai_model_registry"
    __table_args__ = {"schema": "tax"}

    registry_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    model_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    model_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    framework: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    version: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    model_artifact_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    deployment_status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    deployed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxAiWorkflowState(SQLModel, table=True):
    __tablename__ = "tax_ai_workflow_state"
    __table_args__ = {"schema": "tax"}

    state_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    current_node: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    checkpoint_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxAlgorithms(SQLModel, table=True):
    __tablename__ = "tax_algorithms"
    __table_args__ = {"schema": "tax"}

    algorithm_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    algorithm_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    algorithm_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    inputs: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    outputs: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxArchiveContainers(SQLModel, table=True):
    __tablename__ = "tax_archive_containers"
    __table_args__ = {"schema": "tax"}

    container_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    container_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    container_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    length_cm: float = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=False))

    width_cm: float = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=False))

    height_cm: float = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=False))

    weight_capacity_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    location: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxAssessmentDisputes(SQLModel, table=True):
    __tablename__ = "tax_assessment_disputes"
    __table_args__ = {"schema": "tax"}

    dispute_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    assessment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_assessments.assessment_id"), nullable=False))

    dispute_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    dispute_reason: str = Field(default=None, sa_column=Column(Text, nullable=False))

    dispute_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    supporting_docs: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    resolution_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    resolved_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class TaxAssessments(SQLModel, table=True):
    __tablename__ = "tax_assessments"
    __table_args__ = {"schema": "tax"}

    assessment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    assessment_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    tax_authority_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_authorities.tax_authority_id"), nullable=True))

    audit_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_audits.audit_id"), nullable=True))

    assessment_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    assessment_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    due_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    total_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    tax_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    penalty_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    interest_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class TaxAuditFindings(SQLModel, table=True):
    __tablename__ = "tax_audit_findings"
    __table_args__ = {"schema": "tax"}

    finding_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    audit_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_audits.audit_id"), nullable=False))

    finding_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    tax_amount_impact: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    penalty_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    risk_rating: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxAuditResponses(SQLModel, table=True):
    __tablename__ = "tax_audit_responses"
    __table_args__ = {"schema": "tax"}

    response_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    audit_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_audits.audit_id"), nullable=False))

    response_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    response_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    response_content: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    attachments: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    submitted_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxAuditRouteLocations(SQLModel, table=True):
    __tablename__ = "tax_audit_route_locations"
    __table_args__ = {"schema": "tax"}

    location_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    location_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    address: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    latitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 7), nullable=True))

    longitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 7), nullable=True))

    audit_duration_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxAuditRoutes(SQLModel, table=True):
    __tablename__ = "tax_audit_routes"
    __table_args__ = {"schema": "tax"}

    route_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_optimization_problems.problem_id"), nullable=True))

    route_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    auditor_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    total_distance_km: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    total_duration_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    total_travel_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    total_audit_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    site_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    route_sequence: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    high_risk_first: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxAudits(SQLModel, table=True):
    __tablename__ = "tax_audits"
    __table_args__ = {"schema": "tax"}

    audit_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    audit_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    tax_authority_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_authorities.tax_authority_id"), nullable=True))

    tax_jurisdiction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_jurisdictions.tax_jurisdiction_id"), nullable=True))

    audit_reference: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    audit_scope: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    audit_period_from: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    audit_period_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    findings_summary: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    assessment_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    penalty_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    interest_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class TaxAuthorities(SQLModel, table=True):
    __tablename__ = "tax_authorities"
    __table_args__ = {"schema": "tax"}

    tax_authority_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    authority_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    authority_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    country_code: str = Field(default=None, sa_column=Column(String(2), nullable=False))

    address_line1: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    address_line2: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    postal_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    website_url: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    portal_url: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    api_endpoint: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    auth_method: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    filing_requirements: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    payment_methods: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxAuthorityContacts(SQLModel, table=True):
    __tablename__ = "tax_authority_contacts"
    __table_args__ = {"schema": "tax"}

    contact_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_authority_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_authorities.tax_authority_id"), nullable=False))

    contact_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    contact_role: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    email: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxCertificateJurisdictions(SQLModel, table=True):
    __tablename__ = "tax_certificate_jurisdictions"
    __table_args__ = {"schema": "tax"}

    mapping_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    certificate_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_certificates.certificate_id"), nullable=False))

    tax_jurisdiction_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_jurisdictions.tax_jurisdiction_id"), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxCertificates(SQLModel, table=True):
    __tablename__ = "tax_certificates"
    __table_args__ = {"schema": "tax"}

    certificate_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    certificate_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    certificate_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    issuer_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_authorities.tax_authority_id"), nullable=True))

    partner_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    certificate_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    expiration_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    verification_status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    document_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxClassificationRules(SQLModel, table=True):
    __tablename__ = "tax_classification_rules"
    __table_args__ = {"schema": "tax"}

    rule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    rule_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    classification_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    conditions: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    tax_code_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_codes.tax_code_id"), nullable=True))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxClassifications(SQLModel, table=True):
    __tablename__ = "tax_classifications"
    __table_args__ = {"schema": "tax"}

    classification_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    classification_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    entity_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    tax_code_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_codes.tax_code_id"), nullable=True))

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=True))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxCodes(SQLModel, table=True):
    __tablename__ = "tax_codes"
    __table_args__ = {"schema": "tax"}

    tax_code_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=True))

    tax_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_types.tax_type_id"), nullable=True))

    tax_rate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_rates.tax_rate_id"), nullable=True))

    tax_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    tax_code_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    default_account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxComplianceCalendars(SQLModel, table=True):
    __tablename__ = "tax_compliance_calendars"
    __table_args__ = {"schema": "tax"}

    calendar_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    obligation_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_compliance_obligations.obligation_id"), nullable=False))

    due_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_name: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    submitted_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    reminder_sent_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxComplianceObligations(SQLModel, table=True):
    __tablename__ = "tax_compliance_obligations"
    __table_args__ = {"schema": "tax"}

    obligation_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=True))

    tax_jurisdiction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_jurisdictions.tax_jurisdiction_id"), nullable=True))

    obligation_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    obligation_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    frequency: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    due_day_of_period: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxCredits(SQLModel, table=True):
    __tablename__ = "tax_credits"
    __table_args__ = {"schema": "tax"}

    credit_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    credit_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    source_transaction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tax_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_types.tax_type_id"), nullable=True))

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=True))

    credit_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    utilized_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    remaining_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    origin_period: Optional[str] = Field(default=None, sa_column=Column(String(7), nullable=True))

    expiry_period: Optional[str] = Field(default=None, sa_column=Column(String(7), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class TaxCustomsBonds(SQLModel, table=True):
    __tablename__ = "tax_customs_bonds"
    __table_args__ = {"schema": "tax"}

    bond_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    bond_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    bond_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    surety_company: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    bond_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    expiration_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxCustomsDeclarations(SQLModel, table=True):
    __tablename__ = "tax_customs_declarations"
    __table_args__ = {"schema": "tax"}

    declaration_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    declaration_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    declaration_type: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    customs_broker_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    hs_code_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_hs_codes.hs_code_id"), nullable=True))

    declarant_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    entry_port: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    declaration_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    goods_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    goods_value: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    duty_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    tax_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class TaxDocumentArchives(SQLModel, table=True):
    __tablename__ = "tax_document_archives"
    __table_args__ = {"schema": "tax"}

    archive_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_optimization_problems.problem_id"), nullable=True))

    container_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_archive_containers.container_id"), nullable=False))

    document_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    document_reference: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    length_cm: float = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=False))

    width_cm: float = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=False))

    height_cm: float = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=False))

    weight_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    retention_years: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    jurisdiction_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    access_frequency: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    position_x: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    position_y: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    position_z: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    retrieval_sequence: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxEinvoiceConfigs(SQLModel, table=True):
    __tablename__ = "tax_einvoice_configs"
    __table_args__ = {"schema": "tax"}

    config_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    country_code: str = Field(default=None, sa_column=Column(String(2), nullable=False))

    standard: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    api_endpoint: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    api_key_hash: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    digital_signature_cert: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxEinvoiceResponses(SQLModel, table=True):
    __tablename__ = "tax_einvoice_responses"
    __table_args__ = {"schema": "tax"}

    response_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    einvoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_einvoices.einvoice_id"), nullable=False))

    response_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    response_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    response_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    received_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxEinvoices(SQLModel, table=True):
    __tablename__ = "tax_einvoices"
    __table_args__ = {"schema": "tax"}

    einvoice_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    source_module: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    source_doc_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    invoice_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    invoice_uuid: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    standard: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    xml_content: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    qr_code: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    digital_signature: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    submitted_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    authority_response: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class TaxEntityRelationships(SQLModel, table=True):
    __tablename__ = "tax_entity_relationships"
    __table_args__ = {"schema": "tax"}

    relationship_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    parent_entity_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_entity_structures.entity_id"), nullable=False))

    child_entity_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_entity_structures.entity_id"), nullable=False))

    relationship_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    ownership_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxEntityStructures(SQLModel, table=True):
    __tablename__ = "tax_entity_structures"
    __table_args__ = {"schema": "tax"}

    entity_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    entity_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    jurisdiction: str = Field(default=None, sa_column=Column(String(2), nullable=False))

    tax_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    activities: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxExemptionJurisdictions(SQLModel, table=True):
    __tablename__ = "tax_exemption_jurisdictions"
    __table_args__ = {"schema": "tax"}

    mapping_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    exemption_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_exemptions.exemption_id"), nullable=False))

    tax_jurisdiction_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_jurisdictions.tax_jurisdiction_id"), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxExemptions(SQLModel, table=True):
    __tablename__ = "tax_exemptions"
    __table_args__ = {"schema": "tax"}

    exemption_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    exemption_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    exemption_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    exemption_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    conditions: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    documentation_required: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxFilings(SQLModel, table=True):
    __tablename__ = "tax_filings"
    __table_args__ = {"schema": "tax"}

    filing_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_return_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_returns.tax_return_id"), nullable=False))

    filing_type: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    submission_method: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    submitted_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    submitted_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    confirmation_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    authority_response: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class TaxHsCodeDutyRates(SQLModel, table=True):
    __tablename__ = "tax_hs_code_duty_rates"
    __table_args__ = {"schema": "tax"}

    duty_rate_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    hs_code_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_hs_codes.hs_code_id"), nullable=False))

    country_code: str = Field(default=None, sa_column=Column(String(2), nullable=False))

    duty_rate_pct: float = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=False))

    duty_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    fixed_duty_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    preferential_rate_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    quota_restrictions: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxHsCodes(SQLModel, table=True):
    __tablename__ = "tax_hs_codes"
    __table_args__ = {"schema": "tax"}

    hs_code_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    hs_code: str = Field(default=None, sa_column=Column(String(12), nullable=False))

    hs_chapter: str = Field(default=None, sa_column=Column(String(2), nullable=False))

    hs_heading: str = Field(default=None, sa_column=Column(String(4), nullable=False))

    hs_subheading: Optional[str] = Field(default=None, sa_column=Column(String(6), nullable=True))

    hs_national: Optional[str] = Field(default=None, sa_column=Column(String(12), nullable=True))

    description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    unit_of_measure: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    parent_hs_code_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_hs_codes.hs_code_id"), nullable=True))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxIntegrationConnections(SQLModel, table=True):
    __tablename__ = "tax_integration_connections"
    __table_args__ = {"schema": "tax"}

    connection_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    connection_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    integration_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    target_system: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    endpoint_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    auth_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    schedule_cron: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxIntegrationLogs(SQLModel, table=True):
    __tablename__ = "tax_integration_logs"
    __table_args__ = {"schema": "tax"}

    log_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    connection_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_integration_connections.connection_id"), nullable=True))

    direction: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    payload: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    response: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    executed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxJurisdictionAddresses(SQLModel, table=True):
    __tablename__ = "tax_jurisdiction_addresses"
    __table_args__ = {"schema": "tax"}

    address_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_jurisdiction_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_jurisdictions.tax_jurisdiction_id"), nullable=False))

    address_line1: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    address_line2: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    postal_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    country_code: Optional[str] = Field(default=None, sa_column=Column(String(2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxJurisdictionAgreements(SQLModel, table=True):
    __tablename__ = "tax_jurisdiction_agreements"
    __table_args__ = {"schema": "tax"}

    agreement_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    jurisdiction_id_a: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_jurisdictions.tax_jurisdiction_id"), nullable=False))

    jurisdiction_id_b: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_jurisdictions.tax_jurisdiction_id"), nullable=False))

    agreement_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxJurisdictions(SQLModel, table=True):
    __tablename__ = "tax_jurisdictions"
    __table_args__ = {"schema": "tax"}

    tax_jurisdiction_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    country_code: str = Field(default=None, sa_column=Column(String(2), nullable=False))

    jurisdiction_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    jurisdiction_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    jurisdiction_type: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    parent_jurisdiction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxLanggraphExecutions(SQLModel, table=True):
    __tablename__ = "tax_langgraph_executions"
    __table_args__ = {"schema": "tax"}

    execution_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_langgraph_workflows.workflow_id"), nullable=False))

    execution_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    current_state: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxLanggraphStates(SQLModel, table=True):
    __tablename__ = "tax_langgraph_states"
    __table_args__ = {"schema": "tax"}

    state_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    execution_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_langgraph_executions.execution_id"), nullable=False))

    node_id: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    node_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxLanggraphWorkflows(SQLModel, table=True):
    __tablename__ = "tax_langgraph_workflows"
    __table_args__ = {"schema": "tax"}

    workflow_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    workflow_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    dag_definition: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    state_schema: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    checkpoint_enabled: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    hitl_nodes: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    workflow_version: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxLines(SQLModel, table=True):
    __tablename__ = "tax_lines"
    __table_args__ = {"schema": "tax"}

    tax_line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_transaction_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_transactions.tax_transaction_id"), nullable=False))

    line_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    tax_code_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_codes.tax_code_id"), nullable=True))

    tax_rate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_rates.tax_rate_id"), nullable=True))

    tax_jurisdiction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_jurisdictions.tax_jurisdiction_id"), nullable=True))

    taxable_amount: float = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=False))

    tax_amount: float = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=False))

    non_recoverable_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    tax_rate_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    exemption_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    exemption_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    place_of_supply_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    exchange_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    rounding_adjustment: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class TaxLlmConfigs(SQLModel, table=True):
    __tablename__ = "tax_llm_configs"
    __table_args__ = {"schema": "tax"}

    llm_config_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    provider: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    model_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    api_key_hash: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxMlModels(SQLModel, table=True):
    __tablename__ = "tax_ml_models"
    __table_args__ = {"schema": "tax"}

    model_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    model_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    model_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    framework: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    model_version: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    training_params: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    feature_columns: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    target_column: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    accuracy_metric: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxOptimizationProblems(SQLModel, table=True):
    __tablename__ = "tax_optimization_problems"
    __table_args__ = {"schema": "tax"}

    problem_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    problem_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    objective_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    objective_function: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    constraints: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    variables: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    data_sources: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solver_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    solver_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    tax_savings_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    tax_savings_currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxOptimizationScenarios(SQLModel, table=True):
    __tablename__ = "tax_optimization_scenarios"
    __table_args__ = {"schema": "tax"}

    scenario_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_optimization_problems.problem_id"), nullable=False))

    scenario_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    assumptions: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    constraints_override: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    parameters_override: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    result_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    tax_savings_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxOptimizationSolutions(SQLModel, table=True):
    __tablename__ = "tax_optimization_solutions"
    __table_args__ = {"schema": "tax"}

    solution_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_optimization_problems.problem_id"), nullable=False))

    solution_version: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    solution_data: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    is_optimal: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxOrtoolsProblems(SQLModel, table=True):
    __tablename__ = "tax_ortools_problems"
    __table_args__ = {"schema": "tax"}

    ortools_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    problem_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    problem_definition: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    problem_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solution_result: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solution_quality: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    solver_config_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_solver_configs.solver_config_id"), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxPenalties(SQLModel, table=True):
    __tablename__ = "tax_penalties"
    __table_args__ = {"schema": "tax"}

    penalty_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    penalty_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    assessment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_assessments.assessment_id"), nullable=True))

    penalty_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    calculated_at: date = Field(default=None, sa_column=Column(Date, nullable=False))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxPenaltyWaivers(SQLModel, table=True):
    __tablename__ = "tax_penalty_waivers"
    __table_args__ = {"schema": "tax"}

    waiver_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    penalty_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_penalties.penalty_id"), nullable=False))

    waiver_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    waiver_reason: str = Field(default=None, sa_column=Column(Text, nullable=False))

    waived_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    approved_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxPeriods(SQLModel, table=True):
    __tablename__ = "tax_periods"
    __table_args__ = {"schema": "tax"}

    tax_period_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=True))

    period_type: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    period_name: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    period_code: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    start_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    end_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    due_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxPredictionActuals(SQLModel, table=True):
    __tablename__ = "tax_prediction_actuals"
    __table_args__ = {"schema": "tax"}

    actual_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    prediction_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_predictions.prediction_id"), nullable=False))

    actual_value: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    error_absolute: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    error_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    observation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxPredictions(SQLModel, table=True):
    __tablename__ = "tax_predictions"
    __table_args__ = {"schema": "tax"}

    prediction_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    model_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_ml_models.model_id"), nullable=True))

    prediction_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    jurisdiction: Optional[str] = Field(default=None, sa_column=Column(String(2), nullable=True))

    tax_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_types.tax_type_id"), nullable=True))

    prediction_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    prediction_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    prediction_lower: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    prediction_upper: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    confidence_level: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    features_used: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    scenario_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class TaxPromptTemplates(SQLModel, table=True):
    __tablename__ = "tax_prompt_templates"
    __table_args__ = {"schema": "tax"}

    prompt_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    prompt_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    prompt_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    template_text: str = Field(default=None, sa_column=Column(Text, nullable=False))

    input_variables: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_schema: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    llm_config_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_llm_configs.llm_config_id"), nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxRateTiers(SQLModel, table=True):
    __tablename__ = "tax_rate_tiers"
    __table_args__ = {"schema": "tax"}

    tier_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_rate_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_rates.tax_rate_id"), nullable=False))

    tier_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    from_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    to_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    tier_rate_pct: float = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=False))

    tier_fixed_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxRates(SQLModel, table=True):
    __tablename__ = "tax_rates"
    __table_args__ = {"schema": "tax"}

    tax_rate_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_type_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_types.tax_type_id"), nullable=False))

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tax_status_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tax_jurisdiction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tax_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    tax_rate_pct: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    recovery_rate_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    gl_account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    round_rule: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    minimum_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(15, 2), nullable=True))

    maximum_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(15, 2), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    rate_type: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    fixed_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))


class TaxReconciliations(SQLModel, table=True):
    __tablename__ = "tax_reconciliations"
    __table_args__ = {"schema": "tax"}

    reconciliation_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    reconciliation_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=True))

    tax_period_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_periods.tax_period_id"), nullable=True))

    gl_tax_balance: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    return_tax_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    variance_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    variance_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    adjustment_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxRefunds(SQLModel, table=True):
    __tablename__ = "tax_refunds"
    __table_args__ = {"schema": "tax"}

    refund_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    refund_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    tax_authority_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_authorities.tax_authority_id"), nullable=True))

    tax_period_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_periods.tax_period_id"), nullable=True))

    claim_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    claim_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    claimed_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    approved_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    paid_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    paid_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class TaxRegimeAttachments(SQLModel, table=True):
    __tablename__ = "tax_regime_attachments"
    __table_args__ = {"schema": "tax"}

    attachment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_regime_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=False))

    attachment_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    file_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    file_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxRegimeRules(SQLModel, table=True):
    __tablename__ = "tax_regime_rules"
    __table_args__ = {"schema": "tax"}

    regime_rule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_regime_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=False))

    rule_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    rule_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    rule_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    rule_conditions: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    rule_action: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxRegimes(SQLModel, table=True):
    __tablename__ = "tax_regimes"
    __table_args__ = {"schema": "tax"}

    tax_regime_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    country_code: str = Field(default=None, sa_column=Column(String(2), nullable=False))

    tax_regime_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    tax_regime_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    tax_type: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    regime_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    accounting_method: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    reporting_frequency: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_tax_inclusive: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    rounding_rule: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    registration_threshold: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    filing_threshold: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))


class TaxRegistrations(SQLModel, table=True):
    __tablename__ = "tax_registrations"
    __table_args__ = {"schema": "tax"}

    registration_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=True))

    tax_jurisdiction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_jurisdictions.tax_jurisdiction_id"), nullable=True))

    tax_authority_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_authorities.tax_authority_id"), nullable=True))

    registration_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    registration_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxReportTypes(SQLModel, table=True):
    __tablename__ = "tax_report_types"
    __table_args__ = {"schema": "tax"}

    report_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    report_type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    report_type_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    default_format: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxReports(SQLModel, table=True):
    __tablename__ = "tax_reports"
    __table_args__ = {"schema": "tax"}

    report_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    report_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_report_types.report_type_id"), nullable=True))

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=True))

    tax_period_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_periods.tax_period_id"), nullable=True))

    report_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    report_format: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    file_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    generated_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    generated_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxReturnAttachments(SQLModel, table=True):
    __tablename__ = "tax_return_attachments"
    __table_args__ = {"schema": "tax"}

    attachment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_return_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_returns.tax_return_id"), nullable=False))

    file_name: str = Field(default=None, sa_column=Column(String(255), nullable=False))

    file_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    attachment_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxReturns(SQLModel, table=True):
    __tablename__ = "tax_returns"
    __table_args__ = {"schema": "tax"}

    tax_return_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=True))

    tax_period_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_periods.tax_period_id"), nullable=True))

    tax_jurisdiction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_jurisdictions.tax_jurisdiction_id"), nullable=True))

    tax_authority_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_authorities.tax_authority_id"), nullable=True))

    return_type: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    return_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    period_name: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    due_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    submitted_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    accepted_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    taxable_sales: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    taxable_purchases: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    output_tax: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    input_tax: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    net_tax_payable: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    net_tax_refundable: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_adjustments: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    filing_confirmation: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxRuleConditions(SQLModel, table=True):
    __tablename__ = "tax_rule_conditions"
    __table_args__ = {"schema": "tax"}

    condition_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_rule_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_rules.tax_rule_id"), nullable=False))

    condition_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    field_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    operator: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    field_value: str = Field(default=None, sa_column=Column(String(500), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxRuleTaxCodes(SQLModel, table=True):
    __tablename__ = "tax_rule_tax_codes"
    __table_args__ = {"schema": "tax"}

    assignment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_rule_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_rules.tax_rule_id"), nullable=False))

    tax_code_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_codes.tax_code_id"), nullable=False))

    is_default: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxRules(SQLModel, table=True):
    __tablename__ = "tax_rules"
    __table_args__ = {"schema": "tax"}

    tax_rule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    rule_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    rule_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    rule_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    condition_operator: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    conditions: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    actions: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxScenarios(SQLModel, table=True):
    __tablename__ = "tax_scenarios"
    __table_args__ = {"schema": "tax"}

    scenario_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    scenario_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    scenario_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    assumptions: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    constraints: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    objective: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    result_summary: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    tax_impact_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxScipyAnalyses(SQLModel, table=True):
    __tablename__ = "tax_scipy_analyses"
    __table_args__ = {"schema": "tax"}

    analysis_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    analysis_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    analysis_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    analysis_params: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    result_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solver_config_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_solver_configs.solver_config_id"), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxSolverConfigs(SQLModel, table=True):
    __tablename__ = "tax_solver_configs"
    __table_args__ = {"schema": "tax"}

    solver_config_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    solver_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    solver_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxStatuses(SQLModel, table=True):
    __tablename__ = "tax_statuses"
    __table_args__ = {"schema": "tax"}

    tax_status_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_regime_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=False))

    tax_status_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    tax_status_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    is_recoverable: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    recovery_rate_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxTrainingRuns(SQLModel, table=True):
    __tablename__ = "tax_training_runs"
    __table_args__ = {"schema": "tax"}

    run_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    model_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_ml_models.model_id"), nullable=False))

    run_version: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    training_data_start: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    training_data_end: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    training_duration_sec: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    accuracy: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    precision: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    recall: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    f1_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    model_artifact_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxTransactions(SQLModel, table=True):
    __tablename__ = "tax_transactions"
    __table_args__ = {"schema": "tax"}

    tax_transaction_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    bu_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    partner_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tax_rate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tax_status_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tax_jurisdiction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    source_module: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    source_doc_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    source_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    doc_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    tax_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    base_amount: float = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=False))

    tax_amount: float = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=False))

    recoverable_tax_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    non_recoverable_tax_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    tax_period: str = Field(default=None, sa_column=Column(String(7), nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    tax_return_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    filing_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    attribute_category: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute1: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute2: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute3: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute4: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute5: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class TaxTransferPricingAdjustments(SQLModel, table=True):
    __tablename__ = "tax_transfer_pricing_adjustments"
    __table_args__ = {"schema": "tax"}

    adjustment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    study_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_transfer_pricing_studies.study_id"), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    adjustment_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    adjustment_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    adjustment_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxTransferPricingPolicies(SQLModel, table=True):
    __tablename__ = "tax_transfer_pricing_policies"
    __table_args__ = {"schema": "tax"}

    policy_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    policy_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    policy_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    method: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxTransferPricingStudies(SQLModel, table=True):
    __tablename__ = "tax_transfer_pricing_studies"
    __table_args__ = {"schema": "tax"}

    study_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    policy_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_transfer_pricing_policies.policy_id"), nullable=True))

    study_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    tax_year: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    jurisdiction: Optional[str] = Field(default=None, sa_column=Column(String(2), nullable=True))

    analysis_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    arm_length_range_min: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    arm_length_range_max: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    selected_margin: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    documentation_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxTypes(SQLModel, table=True):
    __tablename__ = "tax_types"
    __table_args__ = {"schema": "tax"}

    tax_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    country_code: Optional[str] = Field(default=None, sa_column=Column(String(2), nullable=True))

    tax_type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    tax_type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    category: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    accounting_treatment: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_recoverable: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    recovery_rate_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rounding_rule: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))


class TaxVectorDocuments(SQLModel, table=True):
    __tablename__ = "tax_vector_documents"
    __table_args__ = {"schema": "tax"}

    vector_doc_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    document_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    title: str = Field(default=None, sa_column=Column(String(500), nullable=False))

    content: str = Field(default=None, sa_column=Column(Text, nullable=False))

    meta_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    embedding_model: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxWithholdingCertificates(SQLModel, table=True):
    __tablename__ = "tax_withholding_certificates"
    __table_args__ = {"schema": "tax"}

    wht_certificate_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    partner_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    wht_config_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_withholding_configs.wht_config_id"), nullable=True))

    certificate_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    certificate_type: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    issue_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    tax_year: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    gross_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    wht_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    document_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxWithholdingConfigs(SQLModel, table=True):
    __tablename__ = "tax_withholding_configs"
    __table_args__ = {"schema": "tax"}

    wht_config_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    wht_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    tax_regime_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_regimes.tax_regime_id"), nullable=True))

    tax_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_types.tax_type_id"), nullable=True))

    wht_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    wht_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    wht_rate_pct: float = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=False))

    threshold_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    minimum_withholding: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    effective_from: date = Field(default=None, sa_column=Column(Date, nullable=False))

    effective_to: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    gl_account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class TaxWithholdingPayments(SQLModel, table=True):
    __tablename__ = "tax_withholding_payments"
    __table_args__ = {"schema": "tax"}

    wht_payment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_authority_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("tax.tax_authorities.tax_authority_id"), nullable=True))

    tax_period: str = Field(default=None, sa_column=Column(String(7), nullable=False))

    payment_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    payment_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    payment_method: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    reference_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

