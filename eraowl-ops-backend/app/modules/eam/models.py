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


class EamAiAgentLogs(SQLModel, table=True):
    __tablename__ = "eam_ai_agent_logs"
    __table_args__ = {"schema": "eam"}

    log_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    thread_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    state_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_ai_workflow_state.state_id"), nullable=True))

    agent_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    agent_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    action: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    reasoning: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    llm_calls: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    tool_calls: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamAiDecisions(SQLModel, table=True):
    __tablename__ = "eam_ai_decisions"
    __table_args__ = {"schema": "eam"}

    decision_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    thread_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    doc_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    decision_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    decision_data: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    reasoning: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    confidence_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    accepted: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    accepted_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    accepted_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamAiWorkflowState(SQLModel, table=True):
    __tablename__ = "eam_ai_workflow_state"
    __table_args__ = {"schema": "eam"}

    state_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    thread_id: str = Field(default=None, sa_column=Column(String(150), nullable=False))

    workflow_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_langgraph_workflows.workflow_id"), nullable=True))

    workflow_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    doc_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    doc_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    checkpoint: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    context: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    results: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    errors: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    parent_state_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_ai_workflow_state.state_id"), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamAlerts(SQLModel, table=True):
    __tablename__ = "eam_alerts"
    __table_args__ = {"schema": "eam"}

    alert_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    alert_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    alert_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    alert_source_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    alert_source_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=True))

    component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_components.component_id"), nullable=True))

    severity_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    title: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    action_required: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    alert_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    acknowledged_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    acknowledged_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    resolved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    resolved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    resolution_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    escalation_level: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    escalation_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))


class EamAssetAttachments(SQLModel, table=True):
    __tablename__ = "eam_asset_attachments"
    __table_args__ = {"schema": "eam"}

    attachment_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    attachment_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    attachment_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    file_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    file_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    file_size_bytes: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    attachment_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    revision_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_primary: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamAssetBom(SQLModel, table=True):
    __tablename__ = "eam_asset_bom"
    __table_args__ = {"schema": "eam"}

    asset_bom_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_components.component_id"), nullable=True))

    item_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    item_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    item_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    quantity_per_asset: float = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=False))

    unit_of_measure: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    usage_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    interchangeability_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    superseded_by_item_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    vendor_item_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    manufacturer_item_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    manufacturer_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    lead_time_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    min_stock_level: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    max_stock_level: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    reorder_point: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    safety_stock: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    storage_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    shelf_life_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    requires_certification: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    hazardous_material: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    critical_spare: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    long_lead_item: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

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

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamAssetCategories(SQLModel, table=True):
    __tablename__ = "eam_asset_categories"
    __table_args__ = {"schema": "eam"}

    category_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    category_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    category_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    parent_category_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_asset_categories.category_id"), nullable=True))

    category_level: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    asset_type_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_asset_types.asset_type_id"), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamAssetCriticality(SQLModel, table=True):
    __tablename__ = "eam_asset_criticality"
    __table_args__ = {"schema": "eam"}

    criticality_code: str = Field(sa_column=Column(String(10), primary_key=True))

    criticality_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    impact_level: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    default_color_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    safety_impact: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    environmental_impact: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    operational_impact: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    financial_impact: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    sort_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))


class EamAssetHierarchy(SQLModel, table=True):
    __tablename__ = "eam_asset_hierarchy"
    __table_args__ = {"schema": "eam"}

    hierarchy_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    parent_asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    child_asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    relationship_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    position_description: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    sort_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    effective_start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_critical_component: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamAssetTypes(SQLModel, table=True):
    __tablename__ = "eam_asset_types"
    __table_args__ = {"schema": "eam"}

    asset_type_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    asset_type_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    parent_asset_type_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_asset_types.asset_type_id"), nullable=True))

    asset_class_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    default_criticality_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    default_condition_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    depreciation_method: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    depreciation_life_months: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    insurance_required: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    regulatory_category: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    has_serial_number: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    has_warranty: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    condition_based_maintenance: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    default_maintenance_strategy: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    custom_attributes_schema: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    sort_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamAssetVendors(SQLModel, table=True):
    __tablename__ = "eam_asset_vendors"
    __table_args__ = {"schema": "eam"}

    vendor_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    vendor_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    vendor_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    vendor_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    contact_person: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    email: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    website: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    address: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    service_capabilities: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    service_area: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    certifications: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    performance_rating: Optional[float] = Field(default=None, sa_column=Column(Numeric(3, 1), nullable=True))

    contract_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    preferred_vendor: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    vendor_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamAssets(SQLModel, table=True):
    __tablename__ = "eam_assets"
    __table_args__ = {"schema": "eam"}

    asset_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    asset_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    asset_type_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_asset_types.asset_type_id"), nullable=False))

    asset_class_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    category_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_asset_categories.category_id"), nullable=True))

    criticality_code: Optional[str] = Field(default=None, sa_column=Column(String(10), ForeignKey("eam.eam_asset_criticality.criticality_code"), nullable=True))

    manufacturer_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    manufacturer_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    model_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    manufacture_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    commission_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    in_service_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    warranty_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    warranty_terms: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    functional_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    physical_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    asset_status_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    condition_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    acquisition_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    replacement_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    book_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    salvage_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(15), nullable=True))

    ownership_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    lease_start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    lease_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    depreciation_method: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    depreciation_start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    useful_life_months: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    insurance_policy_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    insurance_coverage: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    insurance_expiry_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    barcode: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    rfid_tag: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    qr_code: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    asset_image_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    source_system_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    source_asset_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    source_transaction_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    custom_attributes: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamAuditLog(SQLModel, table=True):
    __tablename__ = "eam_audit_log"
    __table_args__ = {"schema": "eam"}

    audit_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    table_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    record_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    action_type: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    old_values: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    new_values: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    changed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    change_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamBudgets(SQLModel, table=True):
    __tablename__ = "eam_budgets"
    __table_args__ = {"schema": "eam"}

    budget_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    budget_year: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    budget_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    budget_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    budget_category_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=True))

    functional_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_functional_locations.functional_location_id"), nullable=True))

    planned_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    actual_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    committed_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    variance_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(15), nullable=True))

    budget_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    fiscal_period: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approval_required: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))


class EamCalibrationRequirements(SQLModel, table=True):
    __tablename__ = "eam_calibration_requirements"
    __table_args__ = {"schema": "eam"}

    cal_req_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=True))

    tool_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_tools.tool_id"), nullable=True))

    calibration_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    calibration_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    calibration_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    frequency_days: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    tolerance_range: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    accuracy_requirement: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    standard_reference: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    calibration_procedure: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    requires_certificate: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_traceability: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    assigned_to_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamCalibrationResults(SQLModel, table=True):
    __tablename__ = "eam_calibration_results"
    __table_args__ = {"schema": "eam"}

    cal_result_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    cal_req_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_calibration_requirements.cal_req_id"), nullable=False))

    work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=True))

    tool_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_tools.tool_id"), nullable=True))

    calibration_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    calibrated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    calibration_lab: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    certificate_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    certificate_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    as_found_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    as_left_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    result_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    result_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    adjustment_made: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    next_due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    traceability_info: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))


class EamComplianceRecords(SQLModel, table=True):
    __tablename__ = "eam_compliance_records"
    __table_args__ = {"schema": "eam"}

    compliance_record_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    compliance_req_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_compliance_requirements.compliance_req_id"), nullable=False))

    asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=True))

    work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    inspection_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_inspections.inspection_id"), nullable=True))

    due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    completed_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    result_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    result_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    corrective_action: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    verified_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    verified_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    attachment_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))


class EamComplianceRequirements(SQLModel, table=True):
    __tablename__ = "eam_compliance_requirements"
    __table_args__ = {"schema": "eam"}

    compliance_req_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    requirement_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    requirement_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    regulatory_body: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    regulation_reference: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    asset_type_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_asset_types.asset_type_id"), nullable=True))

    applicability: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    frequency_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    requires_inspection: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_certification: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_training: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    penalty_for_non_compliance: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamComponents(SQLModel, table=True):
    __tablename__ = "eam_components"
    __table_args__ = {"schema": "eam"}

    component_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    component_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    component_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    component_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    parent_component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_components.component_id"), nullable=True))

    manufacturer_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    manufacturer_part_no: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    model_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    criticality_code: Optional[str] = Field(default=None, sa_column=Column(String(10), ForeignKey("eam.eam_asset_criticality.criticality_code"), nullable=True))

    position_description: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    quantity_per_asset: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    unit_of_measure: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    expected_life_months: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    replacement_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    warranty_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    remaining_useful_life: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rul_prediction_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    condition_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    last_replacement_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    last_inspection_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    installation_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    component_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    custom_attributes: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamConditionMonitoringPrograms(SQLModel, table=True):
    __tablename__ = "eam_condition_monitoring_programs"
    __table_args__ = {"schema": "eam"}

    cm_program_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    program_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    program_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    technology_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_components.component_id"), nullable=True))

    frequency_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    route_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    baseline_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    thresholds: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    program_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamConditionReadings(SQLModel, table=True):
    __tablename__ = "eam_condition_readings"
    __table_args__ = {"schema": "eam"}

    reading_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    cm_program_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_condition_monitoring_programs.cm_program_id"), nullable=False))

    meter_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_meters.meter_id"), nullable=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    reading_time: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    reading_value: float = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=False))

    baseline_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    deviation_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    severity_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    trend_direction: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    spectrum_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    thermogram_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamContractAssets(SQLModel, table=True):
    __tablename__ = "eam_contract_assets"
    __table_args__ = {"schema": "eam"}

    contract_asset_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    contract_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_service_contracts.contract_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    coverage_start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    coverage_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    coverage_details: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamCrafts(SQLModel, table=True):
    __tablename__ = "eam_crafts"
    __table_args__ = {"schema": "eam"}

    craft_code: str = Field(sa_column=Column(String(50), primary_key=True))

    craft_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    trade_group_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    hourly_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    overtime_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    travel_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    requires_certification: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    sort_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))


class EamDecommissionPlans(SQLModel, table=True):
    __tablename__ = "eam_decommission_plans"
    __table_args__ = {"schema": "eam"}

    decommission_plan_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    plan_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    plan_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    planned_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    actual_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    decommission_method: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    steps_required: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    approvals_required: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    environmental_considerations: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    safety_considerations: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    estimated_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    actual_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    disposal_proceeds: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    net_proceeds: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    plan_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    certificate_of_disposal_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))


class EamDocumentAssignments(SQLModel, table=True):
    __tablename__ = "eam_document_assignments"
    __table_args__ = {"schema": "eam"}

    document_assignment_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    document_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_documents.document_id"), nullable=False))

    assignment_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    assignment_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamDocuments(SQLModel, table=True):
    __tablename__ = "eam_documents"
    __table_args__ = {"schema": "eam"}

    document_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    document_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    document_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    document_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    revision_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    revision_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    author: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    owner: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    file_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    file_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    file_size_bytes: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    keywords: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    document_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    superseded_by_document_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_documents.document_id"), nullable=True))

    approval_required: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    effective_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamFailureCodes(SQLModel, table=True):
    __tablename__ = "eam_failure_codes"
    __table_args__ = {"schema": "eam"}

    failure_code_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    failure_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    failure_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    failure_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    parent_failure_code_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_failure_codes.failure_code_id"), nullable=True))

    asset_type_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_asset_types.asset_type_id"), nullable=True))

    component_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_safety_related: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_environmental: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    default_severity: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    sort_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamFailureHistory(SQLModel, table=True):
    __tablename__ = "eam_failure_history"
    __table_args__ = {"schema": "eam"}

    failure_history_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_components.component_id"), nullable=True))

    work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    failure_code_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_failure_codes.failure_code_id"), nullable=True))

    failure_date: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    detection_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    repair_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    downtime_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    repair_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    repair_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    production_loss_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    failure_severity: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    failure_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    root_cause: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    corrective_action: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_recurring: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    related_failure_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_failure_history.failure_history_id"), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))


class EamFmeaItems(SQLModel, table=True):
    __tablename__ = "eam_fmea_items"
    __table_args__ = {"schema": "eam"}

    fmea_item_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    fmea_study_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_fmea_studies.fmea_study_id"), nullable=False))

    item_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    function_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    potential_failure_mode: str = Field(default=None, sa_column=Column(Text, nullable=False))

    potential_effect: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    severity_rating: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    potential_cause: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    occurrence_rating: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    current_controls: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    detection_rating: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    rpn: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    recommended_action: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    action_assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    action_due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    action_completed_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    action_taken: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

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

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamFmeaStudies(SQLModel, table=True):
    __tablename__ = "eam_fmea_studies"
    __table_args__ = {"schema": "eam"}

    fmea_study_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    study_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    study_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_components.component_id"), nullable=True))

    system_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    fmea_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    study_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    fmea_facilitator: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    fmea_team_members: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    study_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    revision_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    approval_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamFunctionalLocations(SQLModel, table=True):
    __tablename__ = "eam_functional_locations"
    __table_args__ = {"schema": "eam"}

    functional_location_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    location_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    location_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    location_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    parent_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_functional_locations.functional_location_id"), nullable=True))

    location_path: Optional[str] = Field(default=None, sa_column=Column(String, nullable=True))

    gps_latitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 8), nullable=True))

    gps_longitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 8), nullable=True))

    address_line1: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    address_line2: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state_province: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    postal_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    country_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    site_id_ref: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    supervisor_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    safety_zone_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    environmental_zone_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    has_confined_space: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    has_hazardous_materials: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    permits_required: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    location_drawing_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    p_and_id_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    location_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    sort_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamInspections(SQLModel, table=True):
    __tablename__ = "eam_inspections"
    __table_args__ = {"schema": "eam"}

    inspection_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    inspection_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    inspection_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    inspection_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=True))

    component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_components.component_id"), nullable=True))

    functional_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_functional_locations.functional_location_id"), nullable=True))

    work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    checklist_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    frequency_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    last_inspection_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    next_inspection_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    inspector_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    inspector_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    inspection_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    result_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    result_summary: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    deficiencies_found: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    corrective_action_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    certificate_issued: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    certificate_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    certificate_expiry: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    regulatory_body: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    inspection_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    inspection_document_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))


class EamIntegrationConnections(SQLModel, table=True):
    __tablename__ = "eam_integration_connections"
    __table_args__ = {"schema": "eam"}

    connection_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    connection_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    connection_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    connection_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    protocol_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    endpoint_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    authentication_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    credentials_encrypted: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    schedule_cron: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    connection_status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    last_sync_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    sync_frequency_min: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    retry_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    timeout_seconds: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamIntegrationLogs(SQLModel, table=True):
    __tablename__ = "eam_integration_logs"
    __table_args__ = {"schema": "eam"}

    log_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    connection_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_integration_connections.connection_id"), nullable=False))

    log_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    direction: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    status_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    payload_sent: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    payload_received: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    records_processed: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    records_failed: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    start_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    end_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamJsa(SQLModel, table=True):
    __tablename__ = "eam_jsa"
    __table_args__ = {"schema": "eam"}

    jsa_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    jsa_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    title: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    jsa_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    prepared_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    reviewed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    jsa_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamJsaSteps(SQLModel, table=True):
    __tablename__ = "eam_jsa_steps"
    __table_args__ = {"schema": "eam"}

    jsa_step_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    jsa_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_jsa.jsa_id"), nullable=False))

    step_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    step_description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    hazards: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    controls: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    responsible_party: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamKitContents(SQLModel, table=True):
    __tablename__ = "eam_kit_contents"
    __table_args__ = {"schema": "eam"}

    kit_content_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    kit_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_kits.kit_id"), nullable=False))

    item_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    item_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    quantity: float = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=False))

    unit_of_measure: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    sort_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamKits(SQLModel, table=True):
    __tablename__ = "eam_kits"
    __table_args__ = {"schema": "eam"}

    kit_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    kit_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    kit_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    pm_template_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_pm_templates.pm_template_id"), nullable=True))

    kit_location: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    kit_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    kit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    last_restock_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    kit_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamKpiDefinitions(SQLModel, table=True):
    __tablename__ = "eam_kpi_definitions"
    __table_args__ = {"schema": "eam"}

    kpi_code: str = Field(sa_column=Column(String(100), primary_key=True))

    kpi_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    formula: str = Field(default=None, sa_column=Column(String(500), nullable=False))

    unit_of_measure: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    higher_is_better: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    benchmark_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    warning_threshold: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    critical_threshold: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    kpi_category: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    calculation_frequency: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    sort_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))


class EamKpiValues(SQLModel, table=True):
    __tablename__ = "eam_kpi_values"
    __table_args__ = {"schema": "eam"}

    kpi_value_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    kpi_code: str = Field(default=None, sa_column=Column(String(100), ForeignKey("eam.eam_kpi_definitions.kpi_code"), nullable=False))

    asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=True))

    functional_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_functional_locations.functional_location_id"), nullable=True))

    calculation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    period_start_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_end_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    actual_value: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    benchmark_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    variance_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    status_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    calculation_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamLanggraphWorkflows(SQLModel, table=True):
    __tablename__ = "eam_langgraph_workflows"
    __table_args__ = {"schema": "eam"}

    workflow_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    workflow_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    workflow_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    workflow_domain: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

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

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamLlmConfigs(SQLModel, table=True):
    __tablename__ = "eam_llm_configs"
    __table_args__ = {"schema": "eam"}

    llm_config_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    config_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    provider: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    model_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    api_endpoint: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    api_key_encrypted: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    max_retries: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    timeout_seconds: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    cost_per_1k_tokens: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 6), nullable=True))

    config_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamLoto(SQLModel, table=True):
    __tablename__ = "eam_loto"
    __table_args__ = {"schema": "eam"}

    loto_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    loto_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    equipment_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=True))

    description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    energy_sources: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    isolation_points: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    lock_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    number_of_locks: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    applied_by: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    applied_date: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    removed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    removed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    verification_method: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    verified_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    verified_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    loto_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    loto_diagram_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamMaintenanceCosts(SQLModel, table=True):
    __tablename__ = "eam_maintenance_costs"
    __table_args__ = {"schema": "eam"}

    cost_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_components.component_id"), nullable=True))

    cost_category_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    cost_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    cost_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(15), nullable=True))

    cost_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    reference_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    reference_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    posted_to_gl: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    gl_posting_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    gl_account_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamMeterAssignments(SQLModel, table=True):
    __tablename__ = "eam_meter_assignments"
    __table_args__ = {"schema": "eam"}

    meter_assignment_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    meter_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_meters.meter_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_components.component_id"), nullable=True))

    installation_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    removal_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    initial_reading: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    last_reading: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    last_reading_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    cumulative_reading: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    assignment_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamMeterReadings(SQLModel, table=True):
    __tablename__ = "eam_meter_readings"
    __table_args__ = {"schema": "eam"}

    time: datetime = Field(sa_column=Column(DateTime(timezone=True), primary_key=True))

    meter_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    reading_value: float = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=False))

    reading_value_text: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    unit_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    reading_method_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    operator_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    quality_flag: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    alarm_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    source_system_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    source_reading_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamMeters(SQLModel, table=True):
    __tablename__ = "eam_meters"
    __table_args__ = {"schema": "eam"}

    meter_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    meter_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    meter_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    meter_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    unit_of_measure: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    data_type_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    possible_values: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    reading_source_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    reading_frequency: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    warning_threshold_high: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    warning_threshold_low: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    critical_threshold_high: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    critical_threshold_low: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    decimal_precision: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    meter_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamMlModels(SQLModel, table=True):
    __tablename__ = "eam_ml_models"
    __table_args__ = {"schema": "eam"}

    model_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    model_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    model_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    model_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    model_framework: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    model_version: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    model_parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    training_data_source: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    training_parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    training_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    training_duration_sec: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    training_accuracy: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    training_loss: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    validation_accuracy: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    validation_loss: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 8), nullable=True))

    test_accuracy: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    feature_importance: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    model_artifacts_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    deployment_status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    deployment_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    inference_endpoint_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    monitoring_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    retraining_schedule: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_retrained_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    parent_model_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_ml_models.model_id"), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamNotifications(SQLModel, table=True):
    __tablename__ = "eam_notifications"
    __table_args__ = {"schema": "eam"}

    notification_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    alert_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_alerts.alert_id"), nullable=True))

    notification_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    recipient_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    recipient_address: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    subject: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    sent_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    read_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    delivery_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    failure_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamOptimizationProblems(SQLModel, table=True):
    __tablename__ = "eam_optimization_problems"
    __table_args__ = {"schema": "eam"}

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

    solution_quality: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamOptimizationSolutions(SQLModel, table=True):
    __tablename__ = "eam_optimization_solutions"
    __table_args__ = {"schema": "eam"}

    solution_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    problem_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_optimization_problems.problem_id"), nullable=False))

    solution_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    solution_data: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    solution_quality: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    solver_log: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    solution_version: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_best: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_feasible: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    constraint_violations: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamOrtoolsProblems(SQLModel, table=True):
    __tablename__ = "eam_ortools_problems"
    __table_args__ = {"schema": "eam"}

    ortools_problem_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    problem_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_optimization_problems.problem_id"), nullable=True))

    problem_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    solver_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    problem_data: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    solver_parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solution_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    solution_quality: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    solver_log: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamPermits(SQLModel, table=True):
    __tablename__ = "eam_permits"
    __table_args__ = {"schema": "eam"}

    permit_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    permit_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    permit_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    functional_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_functional_locations.functional_location_id"), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    issuer_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    issuer_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    recipient_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    recipient_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    issued_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    effective_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    effective_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    extended_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    permit_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    conditions: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    special_requirements: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    cancellation_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    permit_document_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamPhysicalLocations(SQLModel, table=True):
    __tablename__ = "eam_physical_locations"
    __table_args__ = {"schema": "eam"}

    physical_location_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    location_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    location_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    location_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    parent_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_physical_locations.physical_location_id"), nullable=True))

    location_path: Optional[str] = Field(default=None, sa_column=Column(String, nullable=True))

    functional_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_functional_locations.functional_location_id"), nullable=True))

    gps_latitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 8), nullable=True))

    gps_longitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 8), nullable=True))

    address_line1: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    address_line2: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    city: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state_province: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    postal_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    country_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    floor_area_sqm: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    max_weight_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    max_height_m: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    climate_controlled: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    hazmat_capable: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    location_map_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    location_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    sort_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamPmAssignments(SQLModel, table=True):
    __tablename__ = "eam_pm_assignments"
    __table_args__ = {"schema": "eam"}

    pm_assignment_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    pm_template_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_pm_templates.pm_template_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    effective_start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    assignment_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    custom_frequency_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    custom_frequency_uom: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    last_performed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    next_due_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    meter_trigger_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    meter_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamPmScheduleOptimized(SQLModel, table=True):
    __tablename__ = "eam_pm_schedule_optimized"
    __table_args__ = {"schema": "eam"}

    pm_sched_opt_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    pm_sched_problem_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_pm_scheduling_problems.pm_sched_problem_id"), nullable=False))

    pm_schedule_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_pm_schedules.pm_schedule_id"), nullable=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    pm_template_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_pm_templates.pm_template_id"), nullable=True))

    scheduled_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    scheduled_time_slot: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    technician_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_technicians.technician_id"), nullable=True))

    estimated_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    priority_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    sequence_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    constraint_satisfied: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamPmSchedules(SQLModel, table=True):
    __tablename__ = "eam_pm_schedules"
    __table_args__ = {"schema": "eam"}

    pm_schedule_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    pm_assignment_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_pm_assignments.pm_assignment_id"), nullable=False))

    pm_template_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_pm_templates.pm_template_id"), nullable=False))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    due_date: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    earliest_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    latest_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    scheduled_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    completed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    schedule_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    generation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    frequency_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    frequency_uom: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    meter_reading_at_gen: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamPmSchedulingProblems(SQLModel, table=True):
    __tablename__ = "eam_pm_scheduling_problems"
    __table_args__ = {"schema": "eam"}

    pm_sched_problem_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    problem_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_optimization_problems.problem_id"), nullable=False))

    planning_horizon_days: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    schedule_start_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    schedule_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    objective_weight_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    objective_weight_downtime: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    objective_weight_workload: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    technician_availability: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    production_schedule: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    asset_availability: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    resource_limits: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamPmTemplates(SQLModel, table=True):
    __tablename__ = "eam_pm_templates"
    __table_args__ = {"schema": "eam"}

    pm_template_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    template_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    template_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    asset_type_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_asset_types.asset_type_id"), nullable=True))

    work_order_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), ForeignKey("eam.eam_work_order_types.work_order_type_code"), nullable=True))

    frequency_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    frequency_value: float = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=False))

    frequency_uom: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    tolerance_before_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    tolerance_after_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    estimated_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    estimated_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    requires_downtime: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_permit: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_loto: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_inspection: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_measurements: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    craft_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    priority_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    safety_requirements: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    procedure_text: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    checklist_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    template_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    template_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    effective_start_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_end_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    approval_required: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamPredictions(SQLModel, table=True):
    __tablename__ = "eam_predictions"
    __table_args__ = {"schema": "eam"}

    prediction_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    model_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_ml_models.model_id"), nullable=False))

    prediction_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=True))

    component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_components.component_id"), nullable=True))

    prediction_date: datetime = Field(default=None, sa_column=Column(DateTime, nullable=False))

    prediction_horizon_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    predicted_value: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    predicted_value_min: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    predicted_value_max: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    prediction_probability: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    confidence_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    features_used: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    feature_values: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    actual_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    prediction_error: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    prediction_accuracy: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    is_validated: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    scenario_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamPredictiveMaintenance(SQLModel, table=True):
    __tablename__ = "eam_predictive_maintenance"
    __table_args__ = {"schema": "eam"}

    pdm_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_components.component_id"), nullable=True))

    model_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_ml_models.model_id"), nullable=True))

    prediction_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_predictions.prediction_id"), nullable=True))

    health_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    rul_days: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    rul_confidence: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    failure_probability: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    predicted_failure_mode: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    recommended_action: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    priority_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    alert_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_alerts.alert_id"), nullable=True))

    pdm_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    evaluation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    actual_failure_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    prediction_accuracy: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    model_retrained: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamPromptTemplates(SQLModel, table=True):
    __tablename__ = "eam_prompt_templates"
    __table_args__ = {"schema": "eam"}

    prompt_template_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    template_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    template_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    template_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    llm_config_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_llm_configs.llm_config_id"), nullable=True))

    system_prompt: str = Field(default=None, sa_column=Column(Text, nullable=False))

    user_prompt_template: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    variables_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_schema: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    template_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    template_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    usage_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    avg_response_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    avg_cost_per_call: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 6), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamRcaActions(SQLModel, table=True):
    __tablename__ = "eam_rca_actions"
    __table_args__ = {"schema": "eam"}

    rca_action_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    rca_study_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_rca_studies.rca_study_id"), nullable=False))

    rca_cause_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_rca_causes.rca_cause_id"), nullable=True))

    action_description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    action_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    completed_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    action_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    effectiveness_review: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    effectiveness_rating: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamRcaCauses(SQLModel, table=True):
    __tablename__ = "eam_rca_causes"
    __table_args__ = {"schema": "eam"}

    rca_cause_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    rca_study_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_rca_studies.rca_study_id"), nullable=False))

    parent_cause_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_rca_causes.rca_cause_id"), nullable=True))

    cause_level: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    cause_description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    cause_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    evidence: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    category_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    sort_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamRcaStudies(SQLModel, table=True):
    __tablename__ = "eam_rca_studies"
    __table_args__ = {"schema": "eam"}

    rca_study_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    study_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    study_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=True))

    failure_history_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_failure_history.failure_history_id"), nullable=True))

    rca_method_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    study_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    problem_statement: str = Field(default=None, sa_column=Column(Text, nullable=False))

    rca_facilitator: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    rca_participants: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    study_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    conclusion: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    recommendation: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    revision_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    approval_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    ai_generated: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    ai_confidence_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamRcmAnalyses(SQLModel, table=True):
    __tablename__ = "eam_rcm_analyses"
    __table_args__ = {"schema": "eam"}

    rcm_analysis_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    rcm_study_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_rcm_studies.rcm_study_id"), nullable=False))

    function_description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    functional_failure: str = Field(default=None, sa_column=Column(Text, nullable=False))

    failure_mode: str = Field(default=None, sa_column=Column(Text, nullable=False))

    failure_effect: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    failure_consequence: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    severity_rating: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    occurrence_rating: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    detection_rating: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    rpn: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_hidden_failure: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    task_type_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    recommended_task: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    task_interval: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    task_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    responsible_group: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    analysis_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamRcmStudies(SQLModel, table=True):
    __tablename__ = "eam_rcm_studies"
    __table_args__ = {"schema": "eam"}

    rcm_study_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    study_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    study_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    system_boundary: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    study_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    rcm_facilitator: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    rcm_team_members: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    study_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    revision_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    approval_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamSafetyPlans(SQLModel, table=True):
    __tablename__ = "eam_safety_plans"
    __table_args__ = {"schema": "eam"}

    safety_plan_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    plan_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    plan_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    plan_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    plan_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    hazards_identified: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    ppe_required: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    safety_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamScenarios(SQLModel, table=True):
    __tablename__ = "eam_scenarios"
    __table_args__ = {"schema": "eam"}

    scenario_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    scenario_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    scenario_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    scenario_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    problem_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_optimization_problems.problem_id"), nullable=True))

    assumptions: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    constraints: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    objectives: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    results: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    scenario_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    execution_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    execution_duration_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamScipyAnalyses(SQLModel, table=True):
    __tablename__ = "eam_scipy_analyses"
    __table_args__ = {"schema": "eam"}

    scipy_analysis_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    analysis_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    analysis_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=True))

    component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_components.component_id"), nullable=True))

    input_data: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    results: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    quality_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    analysis_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    execution_time_ms: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamServiceContracts(SQLModel, table=True):
    __tablename__ = "eam_service_contracts"
    __table_args__ = {"schema": "eam"}

    contract_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    contract_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    contract_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    contract_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    vendor_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    vendor_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    start_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    end_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    renewal_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    contract_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(15), nullable=True))

    payment_terms: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    sla_response_time_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    sla_resolution_time_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    penalty_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    coverage_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    exclusions: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    contract_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    auto_renew: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    approval_required: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    contract_document_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamSparePartsConsumption(SQLModel, table=True):
    __tablename__ = "eam_spare_parts_consumption"
    __table_args__ = {"schema": "eam"}

    consumption_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    work_order_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=False))

    asset_bom_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_asset_bom.asset_bom_id"), nullable=True))

    item_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    item_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    quantity_required: float = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=False))

    quantity_issued: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    quantity_consumed: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    quantity_returned: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    warehouse_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    bin_location: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    issued_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    issued_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    returned_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    returned_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamSparePartsStorage(SQLModel, table=True):
    __tablename__ = "eam_spare_parts_storage"
    __table_args__ = {"schema": "eam"}

    result_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    storage_opt_problem_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_storage_optimization_problems.storage_opt_problem_id"), nullable=False))

    container_id: int = Field(default=None, sa_column=Column(BigInteger, nullable=False))

    container_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    container_dimensions: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    packed_parts: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    utilization_percentage: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    num_parts_packed: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    avg_accessibility_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    weight_capacity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    compatibility_rules: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    fifo_required: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    retrieval_sequence: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    visualization_3d_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamStorageLocations(SQLModel, table=True):
    __tablename__ = "eam_storage_locations"
    __table_args__ = {"schema": "eam"}

    storage_location_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    location_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    location_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    location_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    parent_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_storage_locations.storage_location_id"), nullable=True))

    physical_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_physical_locations.physical_location_id"), nullable=True))

    width_cm: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    depth_cm: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    height_cm: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    max_weight_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    climate_controlled: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    hazmat_capable: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    fifo_required: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    picking_zone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    location_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamStorageOptimizationProblems(SQLModel, table=True):
    __tablename__ = "eam_storage_optimization_problems"
    __table_args__ = {"schema": "eam"}

    storage_opt_problem_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    problem_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_optimization_problems.problem_id"), nullable=False))

    storage_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_storage_locations.storage_location_id"), nullable=True))

    objective_weight_space: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    objective_weight_access: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    objective_weight_fifo: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    constraints: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamTechnicianCertifications(SQLModel, table=True):
    __tablename__ = "eam_technician_certifications"
    __table_args__ = {"schema": "eam"}

    certification_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    technician_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_technicians.technician_id"), nullable=False))

    certification_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    certification_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    issuing_body: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    certification_level: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    date_obtained: date = Field(default=None, sa_column=Column(Date, nullable=False))

    expiry_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    renewal_required: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    renewal_interval_months: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    attachment_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    verification_status: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    verified_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    verified_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamTechnicianRoutes(SQLModel, table=True):
    __tablename__ = "eam_technician_routes"
    __table_args__ = {"schema": "eam"}

    result_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    routing_problem_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_technician_routing_problems.routing_problem_id"), nullable=False))

    route_id: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    technician_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_technicians.technician_id"), nullable=True))

    technician_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    vehicle_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    route_sequence: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    total_distance: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_duration: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_travel_time: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_work_time: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    num_work_orders: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    technician_skills: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    tools_carried: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    parts_available: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    shift_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    shift_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    route_map_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamTechnicianRoutingProblems(SQLModel, table=True):
    __tablename__ = "eam_technician_routing_problems"
    __table_args__ = {"schema": "eam"}

    routing_problem_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    problem_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_optimization_problems.problem_id"), nullable=False))

    routing_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    depot_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    depot_latitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 8), nullable=True))

    depot_longitude: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 8), nullable=True))

    max_work_orders_per_tech: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    max_travel_time_min: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    objective_weight_travel: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    objective_weight_priority: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    objective_weight_balance: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamTechnicianSkills(SQLModel, table=True):
    __tablename__ = "eam_technician_skills"
    __table_args__ = {"schema": "eam"}

    skill_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    technician_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_technicians.technician_id"), nullable=False))

    skill_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    skill_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    skill_level: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    years_experience: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    certification_name: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    certification_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    certification_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    certification_expiry: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    certified_by: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    is_mandatory: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamTechnicians(SQLModel, table=True):
    __tablename__ = "eam_technicians"
    __table_args__ = {"schema": "eam"}

    technician_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    technician_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    first_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    last_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    email: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    primary_craft_code: Optional[str] = Field(default=None, sa_column=Column(String(50), ForeignKey("eam.eam_crafts.craft_code"), nullable=True))

    location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    location_description: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    supervisor_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_technicians.technician_id"), nullable=True))

    hire_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    hourly_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    overtime_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_contractor: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    contractor_company: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    employee_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    shift_preference: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    max_travel_distance_km: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    technician_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamTools(SQLModel, table=True):
    __tablename__ = "eam_tools"
    __table_args__ = {"schema": "eam"}

    tool_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    tool_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    tool_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    tool_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    manufacturer_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    model_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    specifications: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    location_description: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    tool_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    calibration_required: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    calibration_frequency_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    last_calibration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    next_calibration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    calibration_standard: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    tool_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    replacement_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    rfid_tag: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    barcode: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    tool_image_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamVectorDocuments(SQLModel, table=True):
    __tablename__ = "eam_vector_documents"
    __table_args__ = {"schema": "eam"}

    vector_doc_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    document_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_documents.document_id"), nullable=True))

    chunk_id: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    chunk_text: str = Field(default=None, sa_column=Column(Text, nullable=False))

    chunk_sequence: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    embedding: Optional[str] = Field(default=None, sa_column=Column(String, nullable=True))

    meta_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))


class EamWarranties(SQLModel, table=True):
    __tablename__ = "eam_warranties"
    __table_args__ = {"schema": "eam"}

    warranty_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    warranty_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    warranty_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    asset_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=False))

    warranty_provider: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    warranty_type_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    start_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    end_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    warranty_terms: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    coverage_details: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    exclusions: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    claim_contact: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    claim_phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    claim_email: Optional[str] = Field(default=None, sa_column=Column(String(360), nullable=True))

    warranty_document_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    warranty_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamWarrantyClaims(SQLModel, table=True):
    __tablename__ = "eam_warranty_claims"
    __table_args__ = {"schema": "eam"}

    claim_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    warranty_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_warranties.warranty_id"), nullable=False))

    work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    claim_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    claim_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    claim_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(15), nullable=True))

    approved_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    claim_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    submitted_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approval_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    rejection_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    payment_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    payment_reference: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    claim_attachments: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamWoLabor(SQLModel, table=True):
    __tablename__ = "eam_wo_labor"
    __table_args__ = {"schema": "eam"}

    wo_labor_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    work_order_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=False))

    wo_task_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_wo_tasks.wo_task_id"), nullable=True))

    technician_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_technicians.technician_id"), nullable=True))

    craft_code: Optional[str] = Field(default=None, sa_column=Column(String(50), ForeignKey("eam.eam_crafts.craft_code"), nullable=True))

    hours_estimated: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    hours_actual: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    hours_overtime: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    hours_travel: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    hours_wait: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    start_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    end_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    labor_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    overtime_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_contractor: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    electronic_signature: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamWoOperations(SQLModel, table=True):
    __tablename__ = "eam_wo_operations"
    __table_args__ = {"schema": "eam"}

    wo_operation_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    work_order_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=False))

    operation_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    operation_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    operation_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    work_center_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    equipment_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    estimated_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    actual_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    operation_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    actual_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    actual_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    completion_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamWoTasks(SQLModel, table=True):
    __tablename__ = "eam_wo_tasks"
    __table_args__ = {"schema": "eam"}

    wo_task_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    work_order_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=False))

    task_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    task_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    task_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    instructions: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    craft_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    estimated_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    actual_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    estimated_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    actual_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_hold_point: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_quality_check: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_signature: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    task_status_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    actual_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    actual_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    completion_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    created_by_technician: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    completed_by_technician: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamWoTools(SQLModel, table=True):
    __tablename__ = "eam_wo_tools"
    __table_args__ = {"schema": "eam"}

    wo_tool_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    work_order_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=False))

    wo_task_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_wo_tasks.wo_task_id"), nullable=True))

    tool_id: int = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_tools.tool_id"), nullable=False))

    quantity_required: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    quantity_issued: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    quantity_returned: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    issued_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    issued_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    returned_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    returned_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))


class EamWorkOrderStatuses(SQLModel, table=True):
    __tablename__ = "eam_work_order_statuses"
    __table_args__ = {"schema": "eam"}

    work_order_status_code: str = Field(sa_column=Column(String(50), primary_key=True))

    work_order_status_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    is_open: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_closed: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_cancelled: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    sort_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))


class EamWorkOrderTypes(SQLModel, table=True):
    __tablename__ = "eam_work_order_types"
    __table_args__ = {"schema": "eam"}

    work_order_type_code: str = Field(sa_column=Column(String(50), primary_key=True))

    work_order_type_name: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(String(2000), nullable=True))

    is_corrective: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_preventive: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_predictive: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_emergency: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_inspection: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_calibration: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_safety: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_modification: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_project: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_breakdown: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_approval: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_planning: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_scheduling: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_permit: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_loto: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    sort_order: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))


class EamWorkOrders(SQLModel, table=True):
    __tablename__ = "eam_work_orders"
    __table_args__ = {"schema": "eam"}

    work_order_id: int = Field(sa_column=Column(BigInteger, primary_key=True))

    work_order_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    work_order_type_code: str = Field(default=None, sa_column=Column(String(50), ForeignKey("eam.eam_work_order_types.work_order_type_code"), nullable=False))

    work_order_status_code: str = Field(default=None, sa_column=Column(String(50), ForeignKey("eam.eam_work_order_statuses.work_order_status_code"), nullable=False))

    priority_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    title: str = Field(default=None, sa_column=Column(String(360), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    asset_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_assets.asset_id"), nullable=True))

    component_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_components.component_id"), nullable=True))

    functional_location_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_functional_locations.functional_location_id"), nullable=True))

    failure_code_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    failure_cause_code_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    failure_action_code_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    requested_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    requested_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    approved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    planned_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    planned_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    scheduled_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    scheduled_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    actual_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    actual_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    due_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    estimated_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    actual_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    estimated_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    actual_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    labor_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    parts_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    service_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    tool_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    downtime_required: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    downtime_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(12, 4), nullable=True))

    downtime_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    production_impact: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    requires_permit: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_loto: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    permit_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    loto_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    pm_schedule_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    pm_template_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    inspection_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    related_work_order_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, ForeignKey("eam.eam_work_orders.work_order_id"), nullable=True))

    is_recurring: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    recurring_frequency_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    completion_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    completion_report: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    quality_check_passed: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    verified_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    verified_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    closed_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    closed_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    source_system_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    source_transaction_id: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    ai_generated: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    ai_confidence_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 4), nullable=True))

    ai_recommendation: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    custom_attributes: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    creation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    created_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    last_update_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime, nullable=True))

    last_updated_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    tenant_id: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    organization_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    site_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

