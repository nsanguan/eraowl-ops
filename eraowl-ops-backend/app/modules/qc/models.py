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


class AiAgentLogs(SQLModel, table=True):
    __tablename__ = "ai_agent_logs"
    __table_args__ = {"schema": "qc"}

    agent_log_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    agent_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    execution_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    llm_config_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    log_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    log_level: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    token_usage_prompt: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    token_usage_completion: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    token_usage_total: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    tool_calls: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    reasoning_trace: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class AiDecisions(SQLModel, table=True):
    __tablename__ = "ai_decisions"
    __table_args__ = {"schema": "qc"}

    decision_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    decision_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    decision_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    decision_source: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    execution_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    model_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    input_summary: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_decision: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    confidence_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    human_review_required: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    human_reviewer: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    human_review_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    human_override: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    decision_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    compliance_tags: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class AiModelRegistry(SQLModel, table=True):
    __tablename__ = "ai_model_registry"
    __table_args__ = {"schema": "qc"}

    registry_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    model_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    model_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    model_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    model_framework_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    model_version: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    model_stage: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    model_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    model_artifact_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    model_card: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    training_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    validation_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    fairness_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    bias_assessment: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    explainability_report: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class AiWorkflowState(SQLModel, table=True):
    __tablename__ = "ai_workflow_state"
    __table_args__ = {"schema": "qc"}

    workflow_state_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    workflow_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    execution_id: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    workflow_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    state_data: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    current_step: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    workflow_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    error_info: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    meta_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class InspectionChecklist(SQLModel, table=True):
    __tablename__ = "inspection_checklist"
    __table_args__ = {"schema": "qc"}

    item_check_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    plan_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("qc.inspection_plans.plan_id"), nullable=False))

    parameter_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    test_method: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    min_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    max_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    expected_text: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class InspectionOrders(SQLModel, table=True):
    __tablename__ = "inspection_orders"
    __table_args__ = {"schema": "qc"}

    inspection_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    plan_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("qc.inspection_plans.plan_id"), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    inspector_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    source_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    source_line_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    total_qty: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    sample_qty: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    disposition: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    decision_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    inspected_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class InspectionPlans(SQLModel, table=True):
    __tablename__ = "inspection_plans"
    __table_args__ = {"schema": "qc"}

    plan_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    category_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    plan_name: str = Field(default=None, sa_column=Column(String(150), nullable=False))

    version: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class InspectionResults(SQLModel, table=True):
    __tablename__ = "inspection_results"
    __table_args__ = {"schema": "qc"}

    result_line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    inspection_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("qc.inspection_orders.inspection_id"), nullable=False))

    item_check_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("qc.inspection_checklist.item_check_id"), nullable=False))

    actual_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    actual_text: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    is_ok: bool = Field(default=None, sa_column=Column(Boolean, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class QcAgentDefinitions(SQLModel, table=True):
    __tablename__ = "qc_agent_definitions"
    __table_args__ = {"schema": "qc"}

    agent_definition_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    agent_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    agent_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    agent_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    agent_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    agent_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    llm_config_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    system_prompt: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tools: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    memory_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    max_iterations: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcAlgorithms(SQLModel, table=True):
    __tablename__ = "qc_algorithms"
    __table_args__ = {"schema": "qc"}

    algorithm_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    algorithm_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    algorithm_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    algorithm_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    algorithm_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    algorithm_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    input_schema: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_schema: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    configuration: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    performance_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    documentation_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcAuditFindings(SQLModel, table=True):
    __tablename__ = "qc_audit_findings"
    __table_args__ = {"schema": "qc"}

    audit_finding_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    audit_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    finding_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    finding_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    finding_severity_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    finding_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: str = Field(default=None, sa_column=Column(String(2000), nullable=False))

    criteria_reference: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    evidence: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    root_cause: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    corrective_action_plan: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    verification_method: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    verification_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    verified_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    closed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcAudits(SQLModel, table=True):
    __tablename__ = "qc_audits"
    __table_args__ = {"schema": "qc"}

    audit_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    audit_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    audit_title: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    audit_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    audit_standard_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    audit_status_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    department_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    scope_description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    criteria_reference: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    lead_auditor_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    lead_auditor_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    audit_team: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    planned_start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    planned_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    actual_start_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    actual_end_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    overall_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    conclusion: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    recommendation: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    finding_count_critical: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    finding_count_major: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    finding_count_minor: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    finding_count_observation: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    signed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    signed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    signature_meaning: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcCapaActions(SQLModel, table=True):
    __tablename__ = "qc_capa_actions"
    __table_args__ = {"schema": "qc"}

    capa_action_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    capa_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    action_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    action_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    action_description: str = Field(default=None, sa_column=Column(String(2000), nullable=False))

    assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    target_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    completed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    action_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    completion_notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    effectiveness_score: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    attachment_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcCapaHeaders(SQLModel, table=True):
    __tablename__ = "qc_capa_headers"
    __table_args__ = {"schema": "qc"}

    capa_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    capa_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    capa_title: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    capa_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    capa_source_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    source_ncr_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_audit_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_complaint_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_document_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_reference: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    capa_priority_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    capa_status_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    department_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    root_cause_analysis_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    root_cause_summary: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    problem_description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    requested_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    requested_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    assigned_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effectiveness_review_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effectiveness_result: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_effective: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    closure_notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    closed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    closed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    signed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    signed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    signature_meaning: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcCharacteristicValueSets(SQLModel, table=True):
    __tablename__ = "qc_characteristic_value_sets"
    __table_args__ = {"schema": "qc"}

    value_set_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    characteristic_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    value_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    value_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    display_sequence: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_default: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    enabled_flag: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcCharacteristics(SQLModel, table=True):
    __tablename__ = "qc_characteristics"
    __table_args__ = {"schema": "qc"}

    characteristic_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    characteristic_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    characteristic_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    characteristic_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    data_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    precision_decimal: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    display_sequence: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    min_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    max_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    regex_pattern: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    default_value: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    help_text: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    is_required: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_calculated: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    formula: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    parent_characteristic_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    conditional_visibility: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    security_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcComplaintInvestigations(SQLModel, table=True):
    __tablename__ = "qc_complaint_investigations"
    __table_args__ = {"schema": "qc"}

    investigation_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    complaint_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    investigation_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    investigator: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    investigation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    findings: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    root_cause_analysis_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    action_taken: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    customer_communication: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    follow_up_required: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    follow_up_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcControlPlanCharacteristics(SQLModel, table=True):
    __tablename__ = "qc_control_plan_characteristics"
    __table_args__ = {"schema": "qc"}

    cp_characteristic_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    control_plan_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    characteristic_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    spec_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    operation_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    process_step_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    characteristic_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    measurement_technique: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    sample_size: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    sampling_frequency: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    control_method: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    reaction_plan: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    responsible_party: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    document_reference: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    sequence_number: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcControlPlans(SQLModel, table=True):
    __tablename__ = "qc_control_plans"
    __table_args__ = {"schema": "qc"}

    control_plan_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    control_plan_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    control_plan_title: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    control_plan_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    control_plan_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    control_plan_status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    department_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    process_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    fmea_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    revision_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    prepared_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    prepared_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcCostOfQuality(SQLModel, table=True):
    __tablename__ = "qc_cost_of_quality"
    __table_args__ = {"schema": "qc"}

    coq_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    coq_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    coq_category_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    coq_item_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    department_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    product_line_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    project_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    transaction_date: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    source_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    source_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    gl_account_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcCustomerComplaints(SQLModel, table=True):
    __tablename__ = "qc_customer_complaints"
    __table_args__ = {"schema": "qc"}

    complaint_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    complaint_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    complaint_title: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    complaint_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    complaint_severity_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    complaint_status_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    customer_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    customer_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    customer_contact: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    order_line_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    quantity_affected: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    complaint_date: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    received_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    response_required_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    investigation_summary: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    root_cause_summary: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    customer_response: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    rma_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    return_quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    ncr_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    capa_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    closed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    closed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    recurrence_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    signed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    signed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    signature_meaning: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcDefectMaster(SQLModel, table=True):
    __tablename__ = "qc_defect_master"
    __table_args__ = {"schema": "qc"}

    defect_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    defect_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    defect_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    defect_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    defect_severity_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    defect_category_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    is_visible_inspector: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    requires_containment: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    default_disposition: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcDefectOccurrences(SQLModel, table=True):
    __tablename__ = "qc_defect_occurrences"
    __table_args__ = {"schema": "qc"}

    defect_occurrence_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    defect_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    inspection_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    test_result_line_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    ncr_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    complaint_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    occurrence_date: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    defect_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    operator_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    shift_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    machine_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    process_step_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcDocuments(SQLModel, table=True):
    __tablename__ = "qc_documents"
    __table_args__ = {"schema": "qc"}

    document_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    document_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    document_title: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    document_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    document_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    document_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    department_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    author_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    author_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    owner_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    owner_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    keywords: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    effective_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    review_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    review_cycle_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    obsolete_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    security_class_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    requires_training: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcEquipmentCalibration(SQLModel, table=True):
    __tablename__ = "qc_equipment_calibration"
    __table_args__ = {"schema": "qc"}

    calibration_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    equipment_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    calibration_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    calibration_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    calibration_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    calibration_date: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    calibrated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    technician_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    calibration_lab: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    calibration_location: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    standard_used_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    standard_traceability: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    as_found_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    as_left_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    uncertainty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    is_in_tolerance: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    certificate_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    certificate_file_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    certificate_expiry_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    next_calibration_due: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    environment_temp: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    environment_humidity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcFailureAnalysis(SQLModel, table=True):
    __tablename__ = "qc_failure_analysis"
    __table_args__ = {"schema": "qc"}

    failure_analysis_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    fa_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    fa_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    fa_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    ncr_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    complaint_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    failure_mode: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    failure_mechanism: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    failure_site: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    findings: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    conclusion: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    recommendation: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    root_cause_analysis_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    analyzed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    analysis_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    evidence_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcFmeaActions(SQLModel, table=True):
    __tablename__ = "qc_fmea_actions"
    __table_args__ = {"schema": "qc"}

    fmea_action_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    fmea_item_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    action_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    action_description: str = Field(default=None, sa_column=Column(String(2000), nullable=False))

    action_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    target_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    completion_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    action_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    results: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    revised_severity: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    revised_occurrence: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    revised_detection: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    revised_rpn: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcFmeaHeaders(SQLModel, table=True):
    __tablename__ = "qc_fmea_headers"
    __table_args__ = {"schema": "qc"}

    fmea_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    fmea_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    fmea_title: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    fmea_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    fmea_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    fmea_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    department_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    process_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    system_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    scope_description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    team_members: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    prepared_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    prepared_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    reviewed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    reviewed_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    revision_notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcFmeaItems(SQLModel, table=True):
    __tablename__ = "qc_fmea_items"
    __table_args__ = {"schema": "qc"}

    fmea_item_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    fmea_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    item_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    function_requirement: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    failure_mode: str = Field(default=None, sa_column=Column(String(2000), nullable=False))

    effect_of_failure: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    severity_rating: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    cause_of_failure: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    occurrence_rating: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    current_control_prevention: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    current_control_detection: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    detection_rating: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    rpn_value: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    recommended_action: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    action_assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    action_target_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    action_completed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    action_result: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    revised_severity: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    revised_occurrence: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    revised_detection: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    revised_rpn: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcHolds(SQLModel, table=True):
    __tablename__ = "qc_holds"
    __table_args__ = {"schema": "qc"}

    hold_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    hold_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    hold_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    hold_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    hold_reason: str = Field(default=None, sa_column=Column(String(2000), nullable=False))

    item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    placed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    placed_date: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    source_inspection_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_ncr_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    release_authority: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    release_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    release_reason: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    release_condition: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcInspectionEquipment(SQLModel, table=True):
    __tablename__ = "qc_inspection_equipment"
    __table_args__ = {"schema": "qc"}

    inspection_equip_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    inspection_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    equipment_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    usage_start_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    usage_end_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    calibration_verified: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcInspectionLots(SQLModel, table=True):
    __tablename__ = "qc_inspection_lots"
    __table_args__ = {"schema": "qc"}

    inspection_lot_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    inspection_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    lot_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    lot_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    supplier_lot_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    receipt_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    expiry_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcInspectionRoutes(SQLModel, table=True):
    __tablename__ = "qc_inspection_routes"
    __table_args__ = {"schema": "qc"}

    inspection_route_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    problem_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    route_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    route_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    inspector_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    inspector_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    route_sequence: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    total_distance: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_duration: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    num_inspections: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    inspector_skills: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    shift_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    shift_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    route_map_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    created_by_algorithm_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcInspections(SQLModel, table=True):
    __tablename__ = "qc_inspections"
    __table_args__ = {"schema": "qc"}

    inspection_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    inspection_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    inspection_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    source_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    source_document_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_document_line_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_transaction_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    batch_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    supplier_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    customer_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    quality_plan_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    sampling_plan_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    inspection_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    inspection_location: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    inspector_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    inspector_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    inspection_quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    sample_quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    accepted_quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rejected_quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rework_quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    scrapped_quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    inspection_status_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    disposition_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    overall_result_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    planned_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    started_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    completed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    signed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    signed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    signature_meaning: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    ncr_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    hold_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    environment_temp: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    environment_humidity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcIntegrationConnections(SQLModel, table=True):
    __tablename__ = "qc_integration_connections"
    __table_args__ = {"schema": "qc"}

    connection_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    connection_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    connection_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    integration_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    target_system_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    endpoint_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    auth_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    credentials_encrypted: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    connection_properties: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    connection_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    heartbeat_interval_sec: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    last_heartbeat: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcIntegrationLogs(SQLModel, table=True):
    __tablename__ = "qc_integration_logs"
    __table_args__ = {"schema": "qc"}

    integration_log_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    connection_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    log_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    log_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    direction_code: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    request_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    response_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    execution_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    execution_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    retry_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    source_transaction_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    payload_size_bytes: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcKpiActuals(SQLModel, table=True):
    __tablename__ = "qc_kpi_actuals"
    __table_args__ = {"schema": "qc"}

    kpi_actual_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    kpi_definition_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    actual_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    variance: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    variance_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    evaluation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    period_start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    period_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    entity_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcKpiDefinitions(SQLModel, table=True):
    __tablename__ = "qc_kpi_definitions"
    __table_args__ = {"schema": "qc"}

    kpi_definition_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    kpi_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    kpi_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    kpi_category_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    kpi_subcategory_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    formula: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    unit_of_measure: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    data_source: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    frequency_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    direction_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    threshold_green_from: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    threshold_green_to: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    threshold_yellow_from: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    threshold_yellow_to: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    threshold_red_from: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    threshold_red_to: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    owner_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    owner_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    is_calculated: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    calculation_sql: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcLanggraphExecutions(SQLModel, table=True):
    __tablename__ = "qc_langgraph_executions"
    __table_args__ = {"schema": "qc"}

    execution_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    workflow_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    execution_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    execution_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    current_node: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    execution_state: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    checkpoints: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    retry_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    llm_calls_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    tool_calls_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    triggered_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    source_inspection_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_ncr_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_complaint_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcLanggraphStates(SQLModel, table=True):
    __tablename__ = "qc_langgraph_states"
    __table_args__ = {"schema": "qc"}

    state_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    execution_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    node_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    state_data: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    is_checkpoint: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcLanggraphWorkflows(SQLModel, table=True):
    __tablename__ = "qc_langgraph_workflows"
    __table_args__ = {"schema": "qc"}

    workflow_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    workflow_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    workflow_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    workflow_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    workflow_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    workflow_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    dag_definition: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    state_schema: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    checkpoint_enabled: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    hitl_nodes: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    timeout_seconds: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    max_retries: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcLlmConfigs(SQLModel, table=True):
    __tablename__ = "qc_llm_configs"
    __table_args__ = {"schema": "qc"}

    llm_config_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    config_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    config_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    provider_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    model_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    api_endpoint: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    api_key_encrypted: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    temperature: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    max_tokens: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    top_p: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    frequency_penalty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    presence_penalty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    timeout_seconds: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    max_retries: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    config_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcLotDispositions(SQLModel, table=True):
    __tablename__ = "qc_lot_dispositions"
    __table_args__ = {"schema": "qc"}

    lot_disposition_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    disposition_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    inspection_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    ncr_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    disposition_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    disposition_reason: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    disposition_date: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    disposition_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    rework_instructions: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    scrap_instructions: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    return_instructions: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    sort_instructions: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    condition_use_as_is: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    cost_impact: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    signed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    signed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    signature_meaning: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcMlModels(SQLModel, table=True):
    __tablename__ = "qc_ml_models"
    __table_args__ = {"schema": "qc"}

    ml_model_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    model_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    model_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    model_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    model_framework_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    model_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    model_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    problem_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    training_parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    model_architecture: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    feature_columns: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    target_column: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    training_data_query: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    training_results: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    validation_results: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    deployment_endpoint: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    deployment_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    monitoring_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    retraining_frequency: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    last_trained_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    accuracy_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    precision_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    recall_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    f1_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    trained_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcMsaMeasurements(SQLModel, table=True):
    __tablename__ = "qc_msa_measurements"
    __table_args__ = {"schema": "qc"}

    msa_measurement_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    msa_study_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    operator_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    operator_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    part_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    part_sequence: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    trial_number: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    measured_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    reference_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    bias: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    measurement_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    measurement_timestamp: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcMsaStudies(SQLModel, table=True):
    __tablename__ = "qc_msa_studies"
    __table_args__ = {"schema": "qc"}

    msa_study_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    msa_study_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    msa_study_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    msa_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    msa_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    equipment_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    characteristic_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    part_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    number_of_operators: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    number_of_parts: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    number_of_trials: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    tolerance: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    process_variation: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    ndc_value: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    acceptance_criteria: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    conclusion: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    study_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    performed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcNcrAttachments(SQLModel, table=True):
    __tablename__ = "qc_ncr_attachments"
    __table_args__ = {"schema": "qc"}

    ncr_attachment_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    ncr_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    attachment_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    file_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    file_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    file_size_bytes: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    mime_type: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcNcrContainment(SQLModel, table=True):
    __tablename__ = "qc_ncr_containment"
    __table_args__ = {"schema": "qc"}

    containment_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    ncr_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    containment_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    description: str = Field(default=None, sa_column=Column(String(2000), nullable=False))

    assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    target_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    completed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    containment_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    effectiveness_review: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcNcrHeaders(SQLModel, table=True):
    __tablename__ = "qc_ncr_headers"
    __table_args__ = {"schema": "qc"}

    ncr_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    ncr_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    ncr_title: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    ncr_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    ncr_severity_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    ncr_status_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    discovery_source_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    source_inspection_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_complaint_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_audit_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_document_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_document_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    supplier_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    customer_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    quantity_affected: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    cost_affected: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    defect_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    defect_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    disposition_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    containment_required: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    root_cause_analysis_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    capa_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    reported_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    reported_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    assigned_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    investigation_summary: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    root_cause_summary: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    corrective_action_summary: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    closed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    closed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    recurrence_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    signed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    signed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    signature_meaning: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcNotifications(SQLModel, table=True):
    __tablename__ = "qc_notifications"
    __table_args__ = {"schema": "qc"}

    notification_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    notification_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    notification_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    notification_severity: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notification_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    title: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    message_body: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    recipient_list: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    source_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    source_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    action_required: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    due_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    escalation_level: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    acknowledged_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    acknowledged_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    actioned_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    actioned_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    closed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcOptimizationProblems(SQLModel, table=True):
    __tablename__ = "qc_optimization_problems"
    __table_args__ = {"schema": "qc"}

    problem_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    problem_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    problem_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    problem_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    problem_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    objective_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    objective_function: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    constraints: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    variables: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    data_sources: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solver_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    solver_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcOrtoolsProblems(SQLModel, table=True):
    __tablename__ = "qc_ortools_problems"
    __table_args__ = {"schema": "qc"}

    ortools_problem_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    problem_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    problem_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    problem_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    problem_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    solver_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    algorithm_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    problem_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solution_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    is_optimal: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    gap_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    logs: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    execution_timestamp: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcPlanAttachments(SQLModel, table=True):
    __tablename__ = "qc_plan_attachments"
    __table_args__ = {"schema": "qc"}

    plan_attachment_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    plan_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    attachment_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    file_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    file_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    file_size_bytes: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    mime_type: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcPlanElements(SQLModel, table=True):
    __tablename__ = "qc_plan_elements"
    __table_args__ = {"schema": "qc"}

    plan_element_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    plan_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    element_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    characteristic_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    spec_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    test_method_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    sampling_plan_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    element_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_mandatory: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_control_characteristic: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    sample_size: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    frequency_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    instruction_text: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcPlanTriggers(SQLModel, table=True):
    __tablename__ = "qc_plan_triggers"
    __table_args__ = {"schema": "qc"}

    plan_trigger_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    plan_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    trigger_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    trigger_event_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    trigger_source_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    source_document_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    enabled_flag: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    effective_start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcPlans(SQLModel, table=True):
    __tablename__ = "qc_plans"
    __table_args__ = {"schema": "qc"}

    plan_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    plan_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    plan_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    plan_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    plan_category_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    plan_priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    plan_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    plan_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    plan_frequency_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    plan_source_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_mandatory: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    supplier_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    customer_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    department_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    effective_start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    sampling_plan_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    spec_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    action_on_pass: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    action_on_fail: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    action_on_hold: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcPpapSubmissions(SQLModel, table=True):
    __tablename__ = "qc_ppap_submissions"
    __table_args__ = {"schema": "qc"}

    ppap_submission_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    ppap_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    ppap_level: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    ppap_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    item_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    supplier_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    customer_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    customer_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    submission_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    approval_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    engineering_change_level: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    design_record_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    dfmea_ref: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    pfmea_ref: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    control_plan_ref: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    msa_ref: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    dimensional_results: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    material_test_results: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    process_flow_diagram: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    capability_studies: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    qualified_lab_doc: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    appearance_approval: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    sample_parts_ref: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    master_sample_ref: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    checking_aids_ref: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    customer_specific_reqs: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcPredictions(SQLModel, table=True):
    __tablename__ = "qc_predictions"
    __table_args__ = {"schema": "qc"}

    prediction_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    prediction_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    prediction_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    ml_model_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    prediction_horizon: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    predicted_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    predicted_probability: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    confidence_level: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    prediction_features: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    prediction_timestamp: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    actual_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    prediction_error: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    accuracy_metric: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    scenario_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcPromptTemplates(SQLModel, table=True):
    __tablename__ = "qc_prompt_templates"
    __table_args__ = {"schema": "qc"}

    prompt_template_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    template_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    template_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    template_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    template_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    prompt_text: str = Field(default=None, sa_column=Column(Text, nullable=False))

    input_variables: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_parser: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    example_inputs: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    llm_config_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    template_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcRootCauseAnalysis(SQLModel, table=True):
    __tablename__ = "qc_root_cause_analysis"
    __table_args__ = {"schema": "qc"}

    root_cause_analysis_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    rca_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    rca_method_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    rca_title: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    rca_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    source_ncr_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_capa_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_complaint_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    facilitator: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    participants: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    problem_statement: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    analysis_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    conclusion: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    recommendation: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    rca_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    completed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    attachment_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcRootCauseCauses(SQLModel, table=True):
    __tablename__ = "qc_root_cause_causes"
    __table_args__ = {"schema": "qc"}

    root_cause_cause_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    root_cause_analysis_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    cause_level: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    cause_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    cause_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    cause_description: str = Field(default=None, sa_column=Column(String(2000), nullable=False))

    parent_cause_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    is_root_cause: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    evidence: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcSampleContainers(SQLModel, table=True):
    __tablename__ = "qc_sample_containers"
    __table_args__ = {"schema": "qc"}

    container_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    container_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    container_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    container_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    length_cm: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    width_cm: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    height_cm: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_weight_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    temperature_zone_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    capacity: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    location_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcSamplePackingResults(SQLModel, table=True):
    __tablename__ = "qc_sample_packing_results"
    __table_args__ = {"schema": "qc"}

    packing_result_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    problem_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    container_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    container_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    container_dimensions: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    packed_samples: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    utilization_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    num_samples_packed: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    temperature_zones: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    compatibility_rules: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    retrieval_sequence: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    visualization_3d_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcSamplingPlanLines(SQLModel, table=True):
    __tablename__ = "qc_sampling_plan_lines"
    __table_args__ = {"schema": "qc"}

    sampling_plan_line_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    sampling_plan_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    lot_size_from: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    lot_size_to: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    sample_size: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    accept_number: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    reject_number: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    additional_requirements: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcSamplingPlans(SQLModel, table=True):
    __tablename__ = "qc_sampling_plans"
    __table_args__ = {"schema": "qc"}

    sampling_plan_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    plan_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    plan_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    sampling_standard_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    sampling_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    sampling_level_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    aql_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    ltpd_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    lot_size_from: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    lot_size_to: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    sample_size: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    accept_number: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    reject_number: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    switching_rule_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    skip_lot_rule_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_restrictive: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcScenarios(SQLModel, table=True):
    __tablename__ = "qc_scenarios"
    __table_args__ = {"schema": "qc"}

    scenario_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    scenario_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    scenario_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    scenario_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    scenario_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    assumptions: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    constraints: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    objectives: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    input_parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    results: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    comparison_notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    recommendation: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    created_by_algorithm_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    execution_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcScipyAnalyses(SQLModel, table=True):
    __tablename__ = "qc_scipy_analyses"
    __table_args__ = {"schema": "qc"}

    scipy_analysis_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    analysis_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    analysis_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    analysis_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    analysis_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    result_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    statistic_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    p_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    degrees_of_freedom: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    confidence_interval_lower: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    confidence_interval_upper: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    effect_size: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    conclusion: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    execution_timestamp: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    execution_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcSolverConfigs(SQLModel, table=True):
    __tablename__ = "qc_solver_configs"
    __table_args__ = {"schema": "qc"}

    solver_config_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    solver_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    solver_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    solver_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    algorithm_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    max_solve_time_seconds: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    max_iterations: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    tolerance: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    parallel_execution: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcSpcAlerts(SQLModel, table=True):
    __tablename__ = "qc_spc_alerts"
    __table_args__ = {"schema": "qc"}

    spc_alert_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    spc_chart_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    spc_data_point_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    alert_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    alert_severity_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    alert_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    rule_violated: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    acknowledged_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    resolved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    resolution_notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcSpcCharts(SQLModel, table=True):
    __tablename__ = "qc_spc_charts"
    __table_args__ = {"schema": "qc"}

    spc_chart_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    chart_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    chart_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    chart_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    characteristic_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    subgroup_size: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    sampling_frequency_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    chart_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    chart_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    upper_spec_limit: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    lower_spec_limit: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    upper_control_limit: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    lower_control_limit: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    center_line: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    sigma_estimate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    cp_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    cpk_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    pp_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    ppk_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    out_of_control_rules: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcSpcDataPoints(SQLModel, table=True):
    __tablename__ = "qc_spc_data_points"
    __table_args__ = {"schema": "qc"}

    spc_data_point_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    spc_chart_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    subgroup_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    sample_timestamp: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    measurements: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    sample_mean: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    sample_range: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    sample_std_dev: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    sample_min: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    sample_max: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    ucl: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    lcl: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    center_line: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    usl: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    lsl: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    is_out_of_control: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    out_of_control_rules: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    pattern_detected: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    operator_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    operator_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    equipment_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcSpecLimits(SQLModel, table=True):
    __tablename__ = "qc_spec_limits"
    __table_args__ = {"schema": "qc"}

    spec_limit_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    spec_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    characteristic_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    limit_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    upper_limit: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    lower_limit: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    nominal_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    tolerance_plus: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    tolerance_minus: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    sequence_number: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcSpecs(SQLModel, table=True):
    __tablename__ = "qc_specs"
    __table_args__ = {"schema": "qc"}

    spec_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    spec_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    spec_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    spec_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    spec_class_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    spec_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    spec_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    customer_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    supplier_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    regulatory_standard: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    acceptance_criteria: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    aql_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    ltpd_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    test_method_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    sampling_plan_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    effective_start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcSupplierProfiles(SQLModel, table=True):
    __tablename__ = "qc_supplier_profiles"
    __table_args__ = {"schema": "qc"}

    supplier_profile_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    supplier_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    supplier_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    supplier_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    quality_rating: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    quality_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    risk_level_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    approval_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    approval_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    last_audit_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    next_audit_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    certification_list: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcSupplierScorecards(SQLModel, table=True):
    __tablename__ = "qc_supplier_scorecards"
    __table_args__ = {"schema": "qc"}

    scorecard_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    supplier_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    scorecard_period: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    scorecard_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    quality_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    delivery_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    cost_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    service_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    overall_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    ppm_defective: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    defect_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    first_pass_yield: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    lot_rejection_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    incoming_inspection_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    ncr_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    capa_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    on_time_delivery_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    total_shipments: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    scorecard_grade: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcTestEquipment(SQLModel, table=True):
    __tablename__ = "qc_test_equipment"
    __table_args__ = {"schema": "qc"}

    equipment_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    equipment_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    equipment_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    equipment_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    manufacturer: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    model_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    asset_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    location_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    department_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    range_min: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    range_max: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    accuracy: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    resolution: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    equipment_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    calibration_required: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    calibration_frequency_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    last_calibration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    next_calibration_due: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    certified_flag: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    certification_ref: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcTestMethods(SQLModel, table=True):
    __tablename__ = "qc_test_methods"
    __table_args__ = {"schema": "qc"}

    test_method_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    method_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    method_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    method_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    method_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    method_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    procedure_steps: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    sample_preparation: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    acceptance_criteria: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    equipment_requirements: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    training_requirements: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    certification_required: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    safety_requirements: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    reference_standard: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    reference_source: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    turnaround_time_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcTestResultLines(SQLModel, table=True):
    __tablename__ = "qc_test_result_lines"
    __table_args__ = {"schema": "qc"}

    test_result_line_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    test_result_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    characteristic_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    spec_limit_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    measured_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    measured_text: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    measured_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    deviation_from_target: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    deviation_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    result_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_out_of_spec: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_warning: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    defect_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    defect_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    operator_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    equipment_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    test_timestamp: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    sequence_number: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcTestResults(SQLModel, table=True):
    __tablename__ = "qc_test_results"
    __table_args__ = {"schema": "qc"}

    test_result_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    inspection_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    test_result_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    test_result_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    overall_result_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    operator_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    operator_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    test_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    test_method_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    equipment_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    test_duration_minutes: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    calculation_mean: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    calculation_std_dev: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    calculation_range: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    calculation_cpk: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    calculation_ppk: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    is_retest: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    original_result_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    signed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    signed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    signature_meaning: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcTrainingAttendees(SQLModel, table=True):
    __tablename__ = "qc_training_attendees"
    __table_args__ = {"schema": "qc"}

    training_attendee_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    training_course_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    employee_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    employee_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    training_date: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    completion_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    trainer_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    trainer_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    attendance_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    assessment_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    assessment_result_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    certificate_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    certificate_issue_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    certificate_expiry_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effectiveness_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    feedback_rating: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcTrainingCourses(SQLModel, table=True):
    __tablename__ = "qc_training_courses"
    __table_args__ = {"schema": "qc"}

    training_course_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    course_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    course_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    course_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    course_category_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    course_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    course_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    duration_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    delivery_method_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    certification_required: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    certification_validity_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    assessment_required: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    passing_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    trainer_qualification: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    cost_per_trainee: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class QcVectorDocuments(SQLModel, table=True):
    __tablename__ = "qc_vector_documents"
    __table_args__ = {"schema": "qc"}

    vector_document_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    document_external_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    collection_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    content: str = Field(default=None, sa_column=Column(Text, nullable=False))

    meta_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    embedding_model: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    chunk_sequence: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    token_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    source_document_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

