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
    __table_args__ = {"schema": "fa"}

    agent_log_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    agent_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_agent_definitions.agent_id"), nullable=False))

    execution_id: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    action_type: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    tool_calls: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    llm_calls: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    reasoning_trace: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    execution_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    token_usage: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    cost_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    cost_currency: Optional[str] = Field(default=None, sa_column=Column(String(15), nullable=True))

    status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    correlation_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class AiDecisions(SQLModel, table=True):
    __tablename__ = "ai_decisions"
    __table_args__ = {"schema": "fa"}

    decision_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    decision_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    entity_type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    entity_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    decision_data: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    confidence_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    explanation: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    decision_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    reviewed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    review_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    review_comments: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_applied: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    applied_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    applied_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    rejection_reason: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    correlation_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class AiModelRegistry(SQLModel, table=True):
    __tablename__ = "ai_model_registry"
    __table_args__ = {"schema": "fa"}

    registry_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    model_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    model_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    model_framework: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    model_version: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    model_artifact_uri: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    model_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    model_parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    model_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    training_dataset: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    validation_dataset: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    test_dataset: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    feature_list: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    input_schema: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_schema: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    registered_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    registration_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    deployment_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    deprecation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class AiWorkflowState(SQLModel, table=True):
    __tablename__ = "ai_workflow_state"
    __table_args__ = {"schema": "fa"}

    state_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    workflow_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    correlation_id: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    state_data: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    state_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    parent_state_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.ai_workflow_state.state_id"), nullable=True))

    is_completed: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    error_details: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaAdditions(SQLModel, table=True):
    __tablename__ = "fa_additions"
    __table_args__ = {"schema": "fa"}

    addition_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    transaction_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_transactions.transaction_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    addition_source_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    acquisition_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    in_service_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    purchase_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    po_line_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    invoice_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    supplier_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    supplier_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    purchase_price: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    freight_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    installation_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    testing_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    other_costs: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(15), nullable=True))

    project_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaAdjustments(SQLModel, table=True):
    __tablename__ = "fa_adjustments"
    __table_args__ = {"schema": "fa"}

    adjustment_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    transaction_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_transactions.transaction_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    book_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    adjustment_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    adjustment_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    adjustment_reason: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    old_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    new_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    old_salvage_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    new_salvage_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    old_useful_life: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    new_useful_life: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    old_deprn_method_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    new_deprn_method_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    effective_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaAgentDefinitions(SQLModel, table=True):
    __tablename__ = "fa_agent_definitions"
    __table_args__ = {"schema": "fa"}

    agent_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    agent_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    agent_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    agent_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    llm_config_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_llm_configs.llm_config_id"), nullable=True))

    system_prompt: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tools: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    memory_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    max_iterations: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    agent_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    agent_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaAlgorithms(SQLModel, table=True):
    __tablename__ = "fa_algorithms"
    __table_args__ = {"schema": "fa"}

    algorithm_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    algorithm_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    algorithm_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    algorithm_inputs: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    algorithm_outputs: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    algorithm_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    performance_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    algorithm_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    documentation_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaAssetAttachments(SQLModel, table=True):
    __tablename__ = "fa_asset_attachments"
    __table_args__ = {"schema": "fa"}

    attachment_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    attachment_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    file_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    file_path: str = Field(default=None, sa_column=Column(String(500), nullable=False))

    file_size_bytes: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    mime_type: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    is_encrypted: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaAssetBookAssignments(SQLModel, table=True):
    __tablename__ = "fa_asset_book_assignments"
    __table_args__ = {"schema": "fa"}

    assignment_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    book_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_deprn_books.book_id"), nullable=False))

    deprn_method_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_deprn_methods.deprn_method_id"), nullable=False))

    deprn_convention_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_deprn_conventions.deprn_convention_id"), nullable=True))

    useful_life_months: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    salvage_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    salvage_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    deprn_start_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    deprn_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    deprn_remaining_months: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    original_cost: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    current_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    accumulated_deprn: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    net_book_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    prior_ytd_deprn: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    prior_ltd_deprn: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    deprn_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    enable_bonus_deprn: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    bonus_deprn_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    enable_section_179: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    section_179_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    deprn_catchup_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    last_deprn_period_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    last_deprn_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    prorate_factor: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaAssetCategories(SQLModel, table=True):
    __tablename__ = "fa_asset_categories"
    __table_args__ = {"schema": "fa"}

    asset_category_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    category_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    category_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    parent_category_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_asset_categories.asset_category_id"), nullable=True))

    category_level: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    category_path: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    asset_type_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_asset_types.asset_type_id"), nullable=False))

    default_deprn_method_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    default_useful_life: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    default_useful_life_uom: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    default_salvage_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    capitalization_threshold: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    asset_account_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    deprn_account_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    deprn_expense_account_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    cip_account_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    insurance_category_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    tax_category_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    effective_start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaAssetCategoryHierarchy(SQLModel, table=True):
    __tablename__ = "fa_asset_category_hierarchy"
    __table_args__ = {"schema": "fa"}

    hierarchy_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    parent_category_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_asset_categories.asset_category_id"), nullable=False))

    child_category_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_asset_categories.asset_category_id"), nullable=False))

    hierarchy_level: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaAssetComponents(SQLModel, table=True):
    __tablename__ = "fa_asset_components"
    __table_args__ = {"schema": "fa"}

    component_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    parent_asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    component_asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=True))

    component_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    component_description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    component_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    useful_life_months: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    install_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    removal_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_critical: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaAssetCustomAttributes(SQLModel, table=True):
    __tablename__ = "fa_asset_custom_attributes"
    __table_args__ = {"schema": "fa"}

    attribute_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    attribute_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    attribute_value: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    attribute_type_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    attribute_group: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_required: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    display_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaAssetPhotos(SQLModel, table=True):
    __tablename__ = "fa_asset_photos"
    __table_args__ = {"schema": "fa"}

    photo_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    photo_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    photo_timestamp: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    gps_location: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    latitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    longitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    storage_path: str = Field(default=None, sa_column=Column(String(500), nullable=False))

    thumbnail_path: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    file_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    file_size_bytes: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    mime_type: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    photographer_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    photographer_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    annotations: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_primary: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaAssetStorage(SQLModel, table=True):
    __tablename__ = "fa_asset_storage"
    __table_args__ = {"schema": "fa"}

    result_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    problem_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_optimization_problems.problem_id"), nullable=False))

    container_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    container_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    container_dimensions: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    stored_assets: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    utilization_percentage: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    num_assets_stored: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    avg_accessibility_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    weight_capacity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    security_requirements: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    environmental_controls: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    retrieval_sequence: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    visualization_3d_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaAssetTags(SQLModel, table=True):
    __tablename__ = "fa_asset_tags"
    __table_args__ = {"schema": "fa"}

    tag_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    tag_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    tag_value: str = Field(default=None, sa_column=Column(String(500), nullable=False))

    tag_format: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    issued_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    issued_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tag_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    printer_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    print_job_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    replaced_by_tag_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_asset_tags.tag_id"), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaAssetTypes(SQLModel, table=True):
    __tablename__ = "fa_asset_types"
    __table_args__ = {"schema": "fa"}

    asset_type_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    asset_type_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    asset_class_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    default_deprn_method_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    default_useful_life: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    default_useful_life_uom: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    default_salvage_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    capitalization_threshold: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    insurance_category_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    tax_category_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    min_useful_life: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    max_useful_life: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_depreciable: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_leaseable: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_cip_enabled: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaAssets(SQLModel, table=True):
    __tablename__ = "fa_assets"
    __table_args__ = {"schema": "fa"}

    asset_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    asset_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    asset_type_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_asset_types.asset_type_id"), nullable=False))

    asset_category_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_asset_categories.asset_category_id"), nullable=False))

    manufacturer_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    manufacturer_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    model_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    manufacture_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    acquisition_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    in_service_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    original_cost: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    current_cost: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    salvage_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    accumulated_depreciation: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    net_book_value: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    fair_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: str = Field(default=None, sa_column=Column(String(15), nullable=False))

    gps_location: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_locations.location_id"), nullable=True))

    custodian_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_custodians.custodian_id"), nullable=True))

    asset_status_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    condition_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    criticality_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    barcode: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    qr_code: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    rfid_tag: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    source_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    purchase_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    supplier_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    project_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    lease_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    parent_asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=True))

    warranty_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    insurance_policy_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    source_system_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    source_asset_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    source_transaction_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    book_type_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaBonusDepreciation(SQLModel, table=True):
    __tablename__ = "fa_bonus_depreciation"
    __table_args__ = {"schema": "fa"}

    bonus_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    book_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_deprn_books.book_id"), nullable=True))

    bonus_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    bonus_year: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    bonus_percentage: float = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=False))

    bonus_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    eligible_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_elected: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    election_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    carryforward_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    carryforward_year: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaBookTypes(SQLModel, table=True):
    __tablename__ = "fa_book_types"
    __table_args__ = {"schema": "fa"}

    book_type_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    book_type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    book_type_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    is_primary: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_tax_book: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_reporting_book: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaCipCosts(SQLModel, table=True):
    __tablename__ = "fa_cip_costs"
    __table_args__ = {"schema": "fa"}

    cip_cost_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    cip_project_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_cip_projects.cip_project_id"), nullable=False))

    cost_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    cost_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    cost_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    reference_doc_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    reference_doc_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    reference_doc_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    supplier_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    po_line_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    invoice_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    is_capitalizable: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaCipProjects(SQLModel, table=True):
    __tablename__ = "fa_cip_projects"
    __table_args__ = {"schema": "fa"}

    cip_project_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    project_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    project_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    asset_type_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    asset_category_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    start_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    expected_completion_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    actual_completion_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    capitalization_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    cip_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    progress_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    total_budget: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_costs: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    capitalized_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    remaining_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    material_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    labor_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    overhead_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    interest_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    other_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    purchase_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    project_manager: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    target_asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaCountLines(SQLModel, table=True):
    __tablename__ = "fa_count_lines"
    __table_args__ = {"schema": "fa"}

    count_line_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    sheet_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_count_sheets.sheet_id"), nullable=False))

    count_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_physical_counts.count_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    asset_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    asset_description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    expected_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_locations.location_id"), nullable=True))

    actual_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_locations.location_id"), nullable=True))

    expected_custodian_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    actual_custodian_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    barcode_expected: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    barcode_scanned: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    scan_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_mobile_scans.scan_id"), nullable=True))

    scan_timestamp: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    scanned_by: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    gps_latitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    gps_longitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    gps_accuracy: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_scanned: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    line_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    variance_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    variance_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    photo_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    signature_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaCountRoutes(SQLModel, table=True):
    __tablename__ = "fa_count_routes"
    __table_args__ = {"schema": "fa"}

    result_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    problem_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_optimization_problems.problem_id"), nullable=False))

    route_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    counter_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    counter_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    team_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    route_sequence: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    total_distance: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_duration: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_travel_time: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_count_time: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    num_assets: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    counter_skills: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    shift_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    shift_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    high_value_assets_first: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    critical_assets_first: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    route_map_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaCountSheets(SQLModel, table=True):
    __tablename__ = "fa_count_sheets"
    __table_args__ = {"schema": "fa"}

    sheet_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    count_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_physical_counts.count_id"), nullable=False))

    sheet_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    counter_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_custodians.custodian_id"), nullable=True))

    counter_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    team_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    expected_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    scanned_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    sheet_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    assigned_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    started_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    completed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    synced_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaCountVariances(SQLModel, table=True):
    __tablename__ = "fa_count_variances"
    __table_args__ = {"schema": "fa"}

    variance_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    count_line_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_count_lines.count_line_id"), nullable=False))

    count_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_physical_counts.count_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    variance_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    variance_severity_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    expected_value: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    actual_value: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    variance_reason_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    variance_reason: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    investigator_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    investigation_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    resolution_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    resolved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    adjustment_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    requires_adjustment: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    adjustment_pending: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaCustodians(SQLModel, table=True):
    __tablename__ = "fa_custodians"
    __table_args__ = {"schema": "fa"}

    custodian_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    custodian_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    custodian_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    custodian_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    employee_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    department_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    email: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    default_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_locations.location_id"), nullable=True))

    is_acknowledgment_req: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaDeprnBookPeriods(SQLModel, table=True):
    __tablename__ = "fa_deprn_book_periods"
    __table_args__ = {"schema": "fa"}

    period_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    book_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_deprn_books.book_id"), nullable=False))

    period_name: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    fiscal_year: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    period_num: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    period_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    start_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    end_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    deprn_run_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    deprn_posted_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    is_deprn_calculated: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_deprn_posted: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaDeprnBooks(SQLModel, table=True):
    __tablename__ = "fa_deprn_books"
    __table_args__ = {"schema": "fa"}

    book_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    book_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    book_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    book_type_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_book_types.book_type_id"), nullable=False))

    currency_code: str = Field(default=None, sa_column=Column(String(15), nullable=False))

    fiscal_year_start_month: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    default_deprn_method_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    default_useful_life: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    capitalization_threshold: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    enable_bonus_deprn: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    enable_section_179: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    deprn_calendar_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    book_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    last_deprn_run_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_deprn_period_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    asset_account_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    deprn_account_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    deprn_expense_account_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    pnl_account_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    reporting_currency_code: Optional[str] = Field(default=None, sa_column=Column(String(15), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaDeprnCalculation(SQLModel, table=True):
    __tablename__ = "fa_deprn_calculation"
    __table_args__ = {"schema": "fa"}

    deprn_calc_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    book_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_deprn_books.book_id"), nullable=False))

    period_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_deprn_book_periods.period_id"), nullable=False))

    deprn_run_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    beginning_nbv: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    deprn_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    ending_nbv: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    ytd_deprn: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    ltd_deprn: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    bonus_deprn_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    section_179_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    deprn_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    deprn_posting_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    gl_journal_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaDeprnConventions(SQLModel, table=True):
    __tablename__ = "fa_deprn_conventions"
    __table_args__ = {"schema": "fa"}

    deprn_convention_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    convention_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    convention_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    convention_rule: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    first_year_factor: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    last_year_factor: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    is_prorate: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_mid_month: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_mid_quarter: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_half_year: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_full_year: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaDeprnMethods(SQLModel, table=True):
    __tablename__ = "fa_deprn_methods"
    __table_args__ = {"schema": "fa"}

    deprn_method_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    method_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    method_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    method_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    deprn_formula: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    deprn_parameter_1: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    deprn_parameter_2: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    switch_to_sl: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    switch_over_method_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_deprn_methods.deprn_method_id"), nullable=True))

    is_accelerated: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_macrs: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    effective_start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaGroupAssetMembers(SQLModel, table=True):
    __tablename__ = "fa_group_asset_members"
    __table_args__ = {"schema": "fa"}

    member_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    group_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_group_assets.group_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    inclusion_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    removal_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    member_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    member_weight_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaGroupAssets(SQLModel, table=True):
    __tablename__ = "fa_group_assets"
    __table_args__ = {"schema": "fa"}

    group_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    group_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    group_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    group_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_accumulated_deprn: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_nbv: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    average_useful_life: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    deprn_method_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    member_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    group_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaImpairments(SQLModel, table=True):
    __tablename__ = "fa_impairments"
    __table_args__ = {"schema": "fa"}

    impairment_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    transaction_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_transactions.transaction_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    book_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_deprn_books.book_id"), nullable=True))

    impairment_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    impairment_indicator_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    old_carrying_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    recoverable_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    impairment_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    new_carrying_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    fair_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    cost_to_sell: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    value_in_use: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    impairment_reason: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    impairment_test_method: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    impairment_report_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaInsuranceClaims(SQLModel, table=True):
    __tablename__ = "fa_insurance_claims"
    __table_args__ = {"schema": "fa"}

    claim_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    policy_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_insurance_policies.policy_id"), nullable=False))

    asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=True))

    claim_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    claim_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    claim_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    claim_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    approved_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    paid_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    deductible_applied: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    claim_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    incident_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    incident_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    incident_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    adjuster_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    adjuster_phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    settlement_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    claim_document_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    rejection_reason: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaInsurancePolicies(SQLModel, table=True):
    __tablename__ = "fa_insurance_policies"
    __table_args__ = {"schema": "fa"}

    policy_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    policy_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    policy_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    insurance_company: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    coverage_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    coverage_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    deductible_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    premium_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    premium_frequency: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    effective_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    expiration_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    auto_renewal: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    policy_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    policy_document_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    broker_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    broker_contact: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    terms_conditions: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaIntegrationConnections(SQLModel, table=True):
    __tablename__ = "fa_integration_connections"
    __table_args__ = {"schema": "fa"}

    connection_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    connection_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    system_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    integration_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    endpoint_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    api_key_encrypted: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    authentication_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    connection_properties: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    last_test_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_test_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    error_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaIntegrationLogs(SQLModel, table=True):
    __tablename__ = "fa_integration_logs"
    __table_args__ = {"schema": "fa"}

    log_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    connection_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_integration_connections.connection_id"), nullable=False))

    integration_direction: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    transaction_type: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    request_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    response_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    retry_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    execution_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    correlation_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    source_transaction_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    processed_timestamp: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaLanggraphExecutions(SQLModel, table=True):
    __tablename__ = "fa_langgraph_executions"
    __table_args__ = {"schema": "fa"}

    execution_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    workflow_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_langgraph_workflows.workflow_id"), nullable=False))

    execution_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    current_state: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    execution_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    current_node: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    error_details: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    retry_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    max_retries: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    checkpoint_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    result_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    execution_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaLanggraphStates(SQLModel, table=True):
    __tablename__ = "fa_langgraph_states"
    __table_args__ = {"schema": "fa"}

    state_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    execution_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_langgraph_executions.execution_id"), nullable=False))

    node_id: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    node_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    state_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    node_input: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    node_output: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    node_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    retry_attempt: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    tool_calls: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    llm_calls: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    human_input: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    execution_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaLanggraphWorkflows(SQLModel, table=True):
    __tablename__ = "fa_langgraph_workflows"
    __table_args__ = {"schema": "fa"}

    workflow_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    workflow_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    workflow_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    dag_definition: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    state_schema: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    checkpoint_enabled: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    hitl_nodes: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    workflow_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    workflow_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaLeaseAssets(SQLModel, table=True):
    __tablename__ = "fa_lease_assets"
    __table_args__ = {"schema": "fa"}

    lease_asset_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    lease_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_leases.lease_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    is_primary_asset: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    allocated_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaLeaseSchedules(SQLModel, table=True):
    __tablename__ = "fa_lease_schedules"
    __table_args__ = {"schema": "fa"}

    schedule_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    lease_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_leases.lease_id"), nullable=False))

    payment_num: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    payment_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    payment_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    interest_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    principal_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    outstanding_liability: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rou_amortization: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rou_balance: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    payment_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    actual_payment_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    actual_payment_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaLeases(SQLModel, table=True):
    __tablename__ = "fa_leases"
    __table_args__ = {"schema": "fa"}

    lease_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    lease_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    lease_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    lease_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    lease_class_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    lease_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    lessor_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    lessor_reference: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    commencement_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    termination_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    lease_term_months: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    lease_end_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    renewal_options: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    purchase_options: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    termination_options: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    fixed_payment_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    variable_payment_desc: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    variable_payment_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    residual_value_guarantee: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    initial_direct_costs: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    prepayments: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    lease_incentives: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    discount_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    incremental_borrowing_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    lease_liability: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rou_asset_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rou_asset_accumulated_deprn: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rou_asset_nbv: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(15), nullable=True))

    payment_frequency: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    modification_details: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    disclosure_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaLlmConfigs(SQLModel, table=True):
    __tablename__ = "fa_llm_configs"
    __table_args__ = {"schema": "fa"}

    llm_config_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    config_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    provider_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    model_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    api_key_encrypted: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    api_endpoint: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    max_tokens: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    temperature: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    timeout_seconds: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    cost_per_1k_input: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    cost_per_1k_output: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    config_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaLocations(SQLModel, table=True):
    __tablename__ = "fa_locations"
    __table_args__ = {"schema": "fa"}

    location_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    location_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    location_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    location_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    parent_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_locations.location_id"), nullable=True))

    address_line1: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    address_line2: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    postal_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    country_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    gps_location: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    latitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    longitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    supervisor_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    security_level_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    environmental_controls: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_indoor: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    floor_plan_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaMlModels(SQLModel, table=True):
    __tablename__ = "fa_ml_models"
    __table_args__ = {"schema": "fa"}

    model_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    model_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    model_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    model_framework: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    model_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    training_data_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    training_parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    training_results: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    validation_results: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    model_artifact_path: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    model_endpoint_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    model_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    deployment_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    retraining_frequency: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    last_trained_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    accuracy_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    feature_importance: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    monitoring_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaMobileDevices(SQLModel, table=True):
    __tablename__ = "fa_mobile_devices"
    __table_args__ = {"schema": "fa"}

    device_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    device_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    device_type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    device_os: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    device_model: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    device_serial: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    imei_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    mac_address: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    device_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    assigned_to: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    last_sync_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_location: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    app_version: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    battery_level: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    storage_available: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    push_token: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaMobileScans(SQLModel, table=True):
    __tablename__ = "fa_mobile_scans"
    __table_args__ = {"schema": "fa"}

    scan_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    count_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_physical_counts.count_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    asset_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    barcode_scanned: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    scan_type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    scan_timestamp: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    gps_location: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    gps_latitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    gps_longitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    gps_accuracy: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    expected_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    actual_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    scan_status_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    variance_reason_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    variance_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    counter_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_custodians.custodian_id"), nullable=False))

    counter_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    device_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_mobile_devices.device_id"), nullable=True))

    device_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    note_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    sync_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    sync_timestamp: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    sync_error: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    batch_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    source_system_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    source_scan_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaMobileSyncBatches(SQLModel, table=True):
    __tablename__ = "fa_mobile_sync_batches"
    __table_args__ = {"schema": "fa"}

    batch_id: str = Field(sa_column=Column(String(100), primary_key=True))

    mobile_user_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    device_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    batch_timestamp: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    batch_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    record_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    photo_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    signature_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    success_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    error_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    conflict_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    error_details: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    conflict_details: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    processed_timestamp: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaMobileUsers(SQLModel, table=True):
    __tablename__ = "fa_mobile_users"
    __table_args__ = {"schema": "fa"}

    mobile_user_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    custodian_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_custodians.custodian_id"), nullable=False))

    username: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    role_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    permissions: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    assigned_devices: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    last_login: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    is_online: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaOptimizationProblems(SQLModel, table=True):
    __tablename__ = "fa_optimization_problems"
    __table_args__ = {"schema": "fa"}

    problem_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    problem_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    problem_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    problem_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    objective_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    objective_function: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    constraints: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    variables: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    data_sources: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solver_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    solver_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    problem_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    solution_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    solution_results: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaOrtoolsProblems(SQLModel, table=True):
    __tablename__ = "fa_ortools_problems"
    __table_args__ = {"schema": "fa"}

    ortools_problem_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    problem_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    ortools_problem_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    problem_definition: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    problem_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solver_parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solution_results: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solution_quality_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    solve_time_seconds: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_optimal: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    gap_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    execution_log: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaPhotos(SQLModel, table=True):
    __tablename__ = "fa_photos"
    __table_args__ = {"schema": "fa"}

    photo_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    entity_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    entity_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    photo_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    file_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    storage_path: str = Field(default=None, sa_column=Column(String(500), nullable=False))

    thumbnail_path: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    file_size_bytes: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    mime_type: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    gps_location: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    latitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    longitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    taken_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    taken_timestamp: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    device_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    annotations: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_synced: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaPhysicalCounts(SQLModel, table=True):
    __tablename__ = "fa_physical_counts"
    __table_args__ = {"schema": "fa"}

    count_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    count_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    count_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    count_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    count_start_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    count_end_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    planned_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    scope_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    expected_asset_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    scanned_asset_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    missing_asset_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    excess_asset_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    wrong_location_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    variance_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    asset_category_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    custodian_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    supervisor_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    count_team_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_mobile_enabled: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    sync_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaPredictionActuals(SQLModel, table=True):
    __tablename__ = "fa_prediction_actuals"
    __table_args__ = {"schema": "fa"}

    actual_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    prediction_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_predictions.prediction_id"), nullable=False))

    entity_type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    entity_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    actual_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    actual_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    actual_label: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    actual_details: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    prediction_error: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    error_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaPredictions(SQLModel, table=True):
    __tablename__ = "fa_predictions"
    __table_args__ = {"schema": "fa"}

    prediction_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    model_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_ml_models.model_id"), nullable=False))

    prediction_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    entity_type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    entity_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    prediction_date: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    prediction_horizon: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    prediction_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    prediction_probability: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    prediction_label: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    prediction_features: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    prediction_explanation: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    confidence_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    scenario_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    actual_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    actual_outcome_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    prediction_error: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_validated: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaPromptTemplates(SQLModel, table=True):
    __tablename__ = "fa_prompt_templates"
    __table_args__ = {"schema": "fa"}

    prompt_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    template_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    template_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    template_text: str = Field(default=None, sa_column=Column(Text, nullable=False))

    template_variables: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    template_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    llm_config_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_llm_configs.llm_config_id"), nullable=True))

    output_schema: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    example_outputs: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    performance_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaReinstatements(SQLModel, table=True):
    __tablename__ = "fa_reinstatements"
    __table_args__ = {"schema": "fa"}

    reinstatement_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    transaction_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_transactions.transaction_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    retirement_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_retirements.retirement_id"), nullable=False))

    reinstatement_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    reinstatement_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    reinstatement_reason: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaReportSchedules(SQLModel, table=True):
    __tablename__ = "fa_report_schedules"
    __table_args__ = {"schema": "fa"}

    schedule_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    report_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_reports.report_id"), nullable=False))

    schedule_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    frequency_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    cron_expression: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    recipients: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_format: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    distribution_list: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    last_run_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    next_run_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    schedule_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaReports(SQLModel, table=True):
    __tablename__ = "fa_reports"
    __table_args__ = {"schema": "fa"}

    report_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    report_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    report_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    report_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    report_parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_format: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    report_template: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_scheduled: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    schedule_cron: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_generated_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_generated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaRetirements(SQLModel, table=True):
    __tablename__ = "fa_retirements"
    __table_args__ = {"schema": "fa"}

    retirement_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    transaction_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_transactions.transaction_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    retirement_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    retirement_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    original_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    accumulated_deprn: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    net_book_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    proceeds_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    gain_loss_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    buyer_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    buyer_reference: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    retirement_reason: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    is_partial: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaRevaluations(SQLModel, table=True):
    __tablename__ = "fa_revaluations"
    __table_args__ = {"schema": "fa"}

    revaluation_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    transaction_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_transactions.transaction_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    book_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_deprn_books.book_id"), nullable=True))

    revaluation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    old_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    new_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    old_accumulated_deprn: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    new_accumulated_deprn: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    old_nbv: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    new_nbv: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    revaluation_surplus: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    revaluation_deficit: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    revaluation_reason_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    appraiser_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    appraiser_company: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    appraisal_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    appraisal_report_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaScenarios(SQLModel, table=True):
    __tablename__ = "fa_scenarios"
    __table_args__ = {"schema": "fa"}

    scenario_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    scenario_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    scenario_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    assumptions: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    constraints: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    objectives: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    base_scenario_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_scenarios.scenario_id"), nullable=True))

    results: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    comparison_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_approved: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaScipyAnalyses(SQLModel, table=True):
    __tablename__ = "fa_scipy_analyses"
    __table_args__ = {"schema": "fa"}

    analysis_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    analysis_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    analysis_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    analysis_parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    results: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    statistical_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    execution_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    execution_log: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaSignatures(SQLModel, table=True):
    __tablename__ = "fa_signatures"
    __table_args__ = {"schema": "fa"}

    signature_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    entity_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    entity_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    signature_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    signer_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    signer_role: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    signature_timestamp: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    signature_data: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    storage_path: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    gps_location: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    latitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    longitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    device_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    ip_address: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    certificate_ref: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    is_verified: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    verified_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    verification_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    is_synced: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaSolverConfigs(SQLModel, table=True):
    __tablename__ = "fa_solver_configs"
    __table_args__ = {"schema": "fa"}

    solver_config_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    solver_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    solver_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    solver_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    solver_parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    supported_algorithms: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    max_solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    enable_parallel: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    max_threads: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    enable_warm_start: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    performance_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaTaxPayments(SQLModel, table=True):
    __tablename__ = "fa_tax_payments"
    __table_args__ = {"schema": "fa"}

    tax_payment_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    tax_record_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_tax_records.tax_record_id"), nullable=False))

    payment_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    payment_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    payment_reference: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    payment_method: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    paid_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaTaxRecords(SQLModel, table=True):
    __tablename__ = "fa_tax_records"
    __table_args__ = {"schema": "fa"}

    tax_record_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    tax_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    tax_jurisdiction: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    tax_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    assessed_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    tax_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    tax_year: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    assessment_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    payment_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    tax_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    exemption_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    exemption_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    filing_reference: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaTransactions(SQLModel, table=True):
    __tablename__ = "fa_transactions"
    __table_args__ = {"schema": "fa"}

    transaction_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    book_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_deprn_books.book_id"), nullable=True))

    transaction_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    transaction_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    transaction_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    posting_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    asset_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    asset_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    asset_type_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    asset_category_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    custodian_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    from_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    to_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    from_custodian_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    to_custodian_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    cost_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    deprn_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    nbv_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    proceeds_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    gain_loss_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    revaluation_surplus: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    impairment_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(15), nullable=True))

    reference_doc_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    reference_doc_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    reference_doc_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    reason_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    reversal_transaction_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_transactions.transaction_id"), nullable=True))

    is_reversed: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    source_system_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    source_transaction_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    transaction_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaTransfers(SQLModel, table=True):
    __tablename__ = "fa_transfers"
    __table_args__ = {"schema": "fa"}

    transfer_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    transaction_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_transactions.transaction_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    transfer_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    transfer_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    from_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_locations.location_id"), nullable=True))

    to_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_locations.location_id"), nullable=True))

    from_custodian_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_custodians.custodian_id"), nullable=True))

    to_custodian_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_custodians.custodian_id"), nullable=True))

    from_organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    to_organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    from_entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    to_entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    transfer_reason: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    is_custodian_acknowledged: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    custodian_acknowledged_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    entity_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaVectorDocuments(SQLModel, table=True):
    __tablename__ = "fa_vector_documents"
    __table_args__ = {"schema": "fa"}

    document_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    document_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    document_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    content: str = Field(default=None, sa_column=Column(Text, nullable=False))

    content_chunks: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    embeddings: Optional[str] = Field(default=None, sa_column=Column(String, nullable=True))

    meta_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    source_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    document_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    chunk_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_indexed: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    indexed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class FaWarranties(SQLModel, table=True):
    __tablename__ = "fa_warranties"
    __table_args__ = {"schema": "fa"}

    warranty_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    warranty_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    warranty_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    warranty_provider: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    provider_contact: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    start_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    end_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    warranty_term_months: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    coverage_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    coverage_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    exclusions: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    deductible_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    coverage_limit: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_transferable: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    warranty_doc_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    warranty_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class FaWarrantyClaims(SQLModel, table=True):
    __tablename__ = "fa_warranty_claims"
    __table_args__ = {"schema": "fa"}

    claim_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    warranty_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_warranties.warranty_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("fa.fa_assets.asset_id"), nullable=False))

    claim_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    claim_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    claim_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    claim_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    approved_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    claim_status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    issue_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    resolution_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    resolution_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    service_provider: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    claim_doc_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

