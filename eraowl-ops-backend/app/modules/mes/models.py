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


class JobOrders(SQLModel, table=True):
    __tablename__ = "job_orders"
    __table_args__ = {"schema": "mes"}

    job_order_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    wo_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    operation_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    work_center_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.work_centers.work_center_id"), nullable=False))

    job_status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    qty_produced: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    qty_scrap: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class MachineTelemetry(SQLModel, table=True):
    __tablename__ = "machine_telemetry"
    __table_args__ = {"schema": "mes"}

    telemetry_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    work_center_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.work_centers.work_center_id"), nullable=False))

    job_order_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.job_orders.job_order_id"), nullable=True))

    metric_name: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    metric_value: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    metric_text: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    recorded_at: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class MesAiAgentLogs(SQLModel, table=True):
    __tablename__ = "mes_ai_agent_logs"
    __table_args__ = {"schema": "mes"}

    log_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    agent_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    agent_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    reasoning: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    tool_calls: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    llm_calls: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    logged_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesAiFeatureStore(SQLModel, table=True):
    __tablename__ = "mes_ai_feature_store"
    __table_args__ = {"schema": "mes"}

    feature_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    feature_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    feature_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    feature_timestamp: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesAiModelRegistry(SQLModel, table=True):
    __tablename__ = "mes_ai_model_registry"
    __table_args__ = {"schema": "mes"}

    registry_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    model_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    model_version: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    model_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    framework: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    artifact_path: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    registered_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    registered_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesAiWorkflowStates(SQLModel, table=True):
    __tablename__ = "mes_ai_workflow_states"
    __table_args__ = {"schema": "mes"}

    state_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    state_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesAlerts(SQLModel, table=True):
    __tablename__ = "mes_alerts"
    __table_args__ = {"schema": "mes"}

    alert_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    alert_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    severity: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    source_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    source_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    title: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    assigned_to: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    assigned_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    acknowledged_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    resolved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    resolution: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    escalation_level: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    alert_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesAlgorithms(SQLModel, table=True):
    __tablename__ = "mes_algorithms"
    __table_args__ = {"schema": "mes"}

    algorithm_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    algorithm_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    algorithm_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    inputs_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    outputs_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    config_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    language: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    source_code: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    documentation: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesAndonBoards(SQLModel, table=True):
    __tablename__ = "mes_andon_boards"
    __table_args__ = {"schema": "mes"}

    board_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    board_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    board_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    location: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    display_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesAndonTriggers(SQLModel, table=True):
    __tablename__ = "mes_andon_triggers"
    __table_args__ = {"schema": "mes"}

    trigger_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    board_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_andon_boards.board_id"), nullable=True))

    alert_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_alerts.alert_id"), nullable=True))

    triggered_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    display_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    audio_played: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    cleared_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesBatchRecordMaterials(SQLModel, table=True):
    __tablename__ = "mes_batch_record_materials"
    __table_args__ = {"schema": "mes"}

    material_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    batch_record_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_batch_records.batch_record_id"), nullable=False))

    item_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    item_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    planned_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    actual_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    added_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    added_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesBatchRecordSteps(SQLModel, table=True):
    __tablename__ = "mes_batch_record_steps"
    __table_args__ = {"schema": "mes"}

    step_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    batch_record_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_batch_records.batch_record_id"), nullable=False))

    step_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    step_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    step_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    target_value: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    actual_value: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    result: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    start_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    end_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    operator_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesBatchRecords(SQLModel, table=True):
    __tablename__ = "mes_batch_records"
    __table_args__ = {"schema": "mes"}

    batch_record_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_order_execution.execution_id"), nullable=True))

    batch_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    product_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    product_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    batch_size: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    batch_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    batch_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    recipe_revision: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    reviewed_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    reviewed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    approved_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    approved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesCrewAssignments(SQLModel, table=True):
    __tablename__ = "mes_crew_assignments"
    __table_args__ = {"schema": "mes"}

    assignment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    crew_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_crews.crew_id"), nullable=False))

    operator_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operators.operator_id"), nullable=False))

    role: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesCrews(SQLModel, table=True):
    __tablename__ = "mes_crews"
    __table_args__ = {"schema": "mes"}

    crew_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    crew_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    crew_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    supervisor_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesCribCompartments(SQLModel, table=True):
    __tablename__ = "mes_crib_compartments"
    __table_args__ = {"schema": "mes"}

    compartment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    crib_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_tool_cribs.crib_id"), nullable=False))

    compartment_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    width_cm: Optional[float] = Field(default=None, sa_column=Column(Numeric(8, 2), nullable=True))

    depth_cm: Optional[float] = Field(default=None, sa_column=Column(Numeric(8, 2), nullable=True))

    height_cm: Optional[float] = Field(default=None, sa_column=Column(Numeric(8, 2), nullable=True))

    max_weight_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(8, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesCribPackingResults(SQLModel, table=True):
    __tablename__ = "mes_crib_packing_results"
    __table_args__ = {"schema": "mes"}

    packing_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    crib_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_tool_cribs.crib_id"), nullable=False))

    tool_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_tooling_master.tool_id"), nullable=False))

    compartment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_crib_compartments.compartment_id"), nullable=True))

    position_x: Optional[float] = Field(default=None, sa_column=Column(Numeric(8, 2), nullable=True))

    position_y: Optional[float] = Field(default=None, sa_column=Column(Numeric(8, 2), nullable=True))

    position_z: Optional[float] = Field(default=None, sa_column=Column(Numeric(8, 2), nullable=True))

    rotation: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    packed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    optimized: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesDeliveryRequests(SQLModel, table=True):
    __tablename__ = "mes_delivery_requests"
    __table_args__ = {"schema": "mes"}

    request_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_order_execution.execution_id"), nullable=True))

    request_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    from_location: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    to_location: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    qty_required: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    requested_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    required_by_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    priority: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    vehicle_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    assigned_route_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    delivered_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesDeliveryRoutes(SQLModel, table=True):
    __tablename__ = "mes_delivery_routes"
    __table_args__ = {"schema": "mes"}

    route_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    route_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    vehicle_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    stops_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    total_distance: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    total_duration_min: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    distance_uom: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    optimized: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    optimization_result_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    route_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesDigitalTwinModels(SQLModel, table=True):
    __tablename__ = "mes_digital_twin_models"
    __table_args__ = {"schema": "mes"}

    twin_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    twin_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    config_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    data_sources_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    simulation_results: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    last_sync: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesDocumentInstances(SQLModel, table=True):
    __tablename__ = "mes_document_instances"
    __table_args__ = {"schema": "mes"}

    instance_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    document_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_documents.document_id"), nullable=False))

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_order_execution.execution_id"), nullable=True))

    instance_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    generated_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    printed: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    printed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    signed_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    signed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesDocuments(SQLModel, table=True):
    __tablename__ = "mes_documents"
    __table_args__ = {"schema": "mes"}

    document_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    document_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    document_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    document_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    template_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    content: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    file_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    version: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesDowntimeEvents(SQLModel, table=True):
    __tablename__ = "mes_downtime_events"
    __table_args__ = {"schema": "mes"}

    downtime_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    work_center_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_centers.work_center_id"), nullable=True))

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_order_execution.execution_id"), nullable=True))

    operation_exec_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operation_execution.operation_exec_id"), nullable=True))

    downtime_category: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    downtime_reason_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_downtime_reasons.reason_id"), nullable=True))

    start_time: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    end_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    duration_minutes: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    affected_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    responsible: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    corrective_action: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesDowntimeReasons(SQLModel, table=True):
    __tablename__ = "mes_downtime_reasons"
    __table_args__ = {"schema": "mes"}

    reason_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    category: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    reason_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    reason_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    sub_reason: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_planned: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    requires_action: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesEnergyMeters(SQLModel, table=True):
    __tablename__ = "mes_energy_meters"
    __table_args__ = {"schema": "mes"}

    meter_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    meter_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    meter_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    meter_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    conversion_factor: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 6), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesEnergyReadings(SQLModel, table=True):
    __tablename__ = "mes_energy_readings"
    __table_args__ = {"schema": "mes"}

    reading_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    meter_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_energy_meters.meter_id"), nullable=False))

    reading_value: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    reading_time: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    cost_per_unit: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 2), nullable=True))

    carbon_footprint_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesEquipment(SQLModel, table=True):
    __tablename__ = "mes_equipment"
    __table_args__ = {"schema": "mes"}

    equipment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    equipment_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    equipment_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_equipment_types.equipment_type_id"), nullable=True))

    equipment_class_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_equipment_classes.equipment_class_id"), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_equipment_locations.location_id"), nullable=True))

    status_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_equipment_statuses.status_id"), nullable=True))

    manufacturer: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    model: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    install_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    warranty_expiry: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    capacity_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    capacity_uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    power_rating: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    power_uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    asset_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesEquipmentAssignments(SQLModel, table=True):
    __tablename__ = "mes_equipment_assignments"
    __table_args__ = {"schema": "mes"}

    assignment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_equipment.equipment_id"), nullable=False))

    work_center_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    production_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    assigned_from: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    assigned_until: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesEquipmentCapabilities(SQLModel, table=True):
    __tablename__ = "mes_equipment_capabilities"
    __table_args__ = {"schema": "mes"}

    capability_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_equipment.equipment_id"), nullable=False))

    operation_type: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    min_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    max_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesEquipmentCertifications(SQLModel, table=True):
    __tablename__ = "mes_equipment_certifications"
    __table_args__ = {"schema": "mes"}

    certification_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_equipment.equipment_id"), nullable=False))

    cert_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    cert_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    issue_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    expiry_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    cert_body: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesEquipmentClasses(SQLModel, table=True):
    __tablename__ = "mes_equipment_classes"
    __table_args__ = {"schema": "mes"}

    equipment_class_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    class_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    class_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesEquipmentConnections(SQLModel, table=True):
    __tablename__ = "mes_equipment_connections"
    __table_args__ = {"schema": "mes"}

    connection_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_equipment.equipment_id"), nullable=False))

    protocol: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    endpoint: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    port: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    topic: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesEquipmentDataPoints(SQLModel, table=True):
    __tablename__ = "mes_equipment_data_points"
    __table_args__ = {"schema": "mes"}

    point_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_equipment.equipment_id"), nullable=False))

    point_code: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    point_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    data_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    sampling_rate: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    scaling_factor: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 6), nullable=True))

    offset_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesEquipmentLocations(SQLModel, table=True):
    __tablename__ = "mes_equipment_locations"
    __table_args__ = {"schema": "mes"}

    location_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    location_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    location_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    area: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    line: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    cell: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    station: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesEquipmentStatuses(SQLModel, table=True):
    __tablename__ = "mes_equipment_statuses"
    __table_args__ = {"schema": "mes"}

    status_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    status_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    status_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    is_running: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_idle: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_down: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    color: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesEquipmentTypes(SQLModel, table=True):
    __tablename__ = "mes_equipment_types"
    __table_args__ = {"schema": "mes"}

    equipment_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesGenealogy(SQLModel, table=True):
    __tablename__ = "mes_genealogy"
    __table_args__ = {"schema": "mes"}

    genealogy_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    parent_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    parent_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    parent_lot: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    parent_serial: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    child_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    child_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    child_lot: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    child_serial: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    operation_exec_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operation_execution.operation_exec_id"), nullable=True))

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_order_execution.execution_id"), nullable=True))

    genealogy_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    direction: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesGenealogySnapshots(SQLModel, table=True):
    __tablename__ = "mes_genealogy_snapshots"
    __table_args__ = {"schema": "mes"}

    snapshot_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    snapshot_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    snapshot_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    reason: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesInstructionAcknowledgments(SQLModel, table=True):
    __tablename__ = "mes_instruction_acknowledgments"
    __table_args__ = {"schema": "mes"}

    ack_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    instruction_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_instructions.instruction_id"), nullable=False))

    operator_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operators.operator_id"), nullable=False))

    acknowledged_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    understood: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesInstructionVersions(SQLModel, table=True):
    __tablename__ = "mes_instruction_versions"
    __table_args__ = {"schema": "mes"}

    version_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    instruction_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_instructions.instruction_id"), nullable=False))

    version_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    content: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    change_notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    effective_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    reviewed_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    approved_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    approved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesInstructions(SQLModel, table=True):
    __tablename__ = "mes_instructions"
    __table_args__ = {"schema": "mes"}

    instruction_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    instruction_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    instruction_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    instruction_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    current_version: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    content: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    duration_seconds: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    safety_warnings: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    quality_checks: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    department: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    category: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_controlled: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesIntegrationConnections(SQLModel, table=True):
    __tablename__ = "mes_integration_connections"
    __table_args__ = {"schema": "mes"}

    connection_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    connection_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    connection_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    integration_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    endpoint_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    auth_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    auth_credentials: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    config_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    schedule: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    last_sync: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesIntegrationLogs(SQLModel, table=True):
    __tablename__ = "mes_integration_logs"
    __table_args__ = {"schema": "mes"}

    log_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    connection_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_integration_connections.connection_id"), nullable=False))

    direction: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    request_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    response_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    logged_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesKpiActuals(SQLModel, table=True):
    __tablename__ = "mes_kpi_actuals"
    __table_args__ = {"schema": "mes"}

    actual_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    kpi_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_kpi_definitions.kpi_id"), nullable=False))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    actual_value: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    variance: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    period_start: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    period_end: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    recorded_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesKpiDefinitions(SQLModel, table=True):
    __tablename__ = "mes_kpi_definitions"
    __table_args__ = {"schema": "mes"}

    kpi_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    kpi_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    kpi_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    kpi_category: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    formula: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    higher_is_better: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    warning_threshold: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    critical_threshold: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesLaborAssignments(SQLModel, table=True):
    __tablename__ = "mes_labor_assignments"
    __table_args__ = {"schema": "mes"}

    labor_assignment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    operator_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operators.operator_id"), nullable=False))

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_order_execution.execution_id"), nullable=True))

    operation_exec_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operation_execution.operation_exec_id"), nullable=True))

    labor_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    start_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    end_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    duration_minutes: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    skill_applied: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    cert_used: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesLaborTimeCollection(SQLModel, table=True):
    __tablename__ = "mes_labor_time_collection"
    __table_args__ = {"schema": "mes"}

    time_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    operator_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operators.operator_id"), nullable=False))

    clock_in: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    clock_out: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    duration_minutes: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    work_center_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_centers.work_center_id"), nullable=True))

    shift_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_shifts.shift_id"), nullable=True))

    is_overtime: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_break: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    absence_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    recorded_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesLineBalancing(SQLModel, table=True):
    __tablename__ = "mes_line_balancing"
    __table_args__ = {"schema": "mes"}

    balance_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    production_line_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_production_lines.production_line_id"), nullable=False))

    product_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    takt_time_seconds: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    cycle_time_seconds: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    station_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    balance_efficiency: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    as_of_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesLlmConfigs(SQLModel, table=True):
    __tablename__ = "mes_llm_configs"
    __table_args__ = {"schema": "mes"}

    config_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    config_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    provider: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    model_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    api_key_encrypted: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_default: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesMachineAlarms(SQLModel, table=True):
    __tablename__ = "mes_machine_alarms"
    __table_args__ = {"schema": "mes"}

    alarm_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    alarm_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    alarm_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    severity: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    alarm_start: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    alarm_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    acknowledged: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    acknowledged_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    acknowledged_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    cleared_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    cleared_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesMachineDataValues(SQLModel, table=True):
    __tablename__ = "mes_machine_data_values"
    __table_args__ = {"schema": "mes"}

    value_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    point_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    value_numeric: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    value_text: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    quality_flag: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    recorded_at: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesMachineEvents(SQLModel, table=True):
    __tablename__ = "mes_machine_events"
    __table_args__ = {"schema": "mes"}

    event_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    event_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    event_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    event_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    severity: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    event_time: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    acknowledged: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    acknowledged_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    acknowledged_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesMachinePrograms(SQLModel, table=True):
    __tablename__ = "mes_machine_programs"
    __table_args__ = {"schema": "mes"}

    program_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    program_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    program_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    program_version: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    program_data: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    loaded_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    loaded_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesMaintenanceHistory(SQLModel, table=True):
    __tablename__ = "mes_maintenance_history"
    __table_args__ = {"schema": "mes"}

    history_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    mwo_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_maintenance_work_orders.mwo_id"), nullable=False))

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    maintenance_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    parts_used: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    findings: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    recommendations: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    downtime_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    cost_total: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesMaintenanceParts(SQLModel, table=True):
    __tablename__ = "mes_maintenance_parts"
    __table_args__ = {"schema": "mes"}

    part_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    mwo_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_maintenance_work_orders.mwo_id"), nullable=False))

    item_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    item_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    qty_used: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 2), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesMaintenanceSchedules(SQLModel, table=True):
    __tablename__ = "mes_maintenance_schedules"
    __table_args__ = {"schema": "mes"}

    schedule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    maintenance_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    frequency_value: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    frequency_uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    last_performed: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    next_due: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    estimated_duration_min: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesMaintenanceWorkOrders(SQLModel, table=True):
    __tablename__ = "mes_maintenance_work_orders"
    __table_args__ = {"schema": "mes"}

    mwo_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    schedule_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    maintenance_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    title: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    priority: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    requested_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    scheduled_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    completed_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    downtime_minutes: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    cost_estimated: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 2), nullable=True))

    cost_actual: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 2), nullable=True))

    technician_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesMaterialConsumption(SQLModel, table=True):
    __tablename__ = "mes_material_consumption"
    __table_args__ = {"schema": "mes"}

    consumption_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    execution_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_order_execution.execution_id"), nullable=False))

    operation_exec_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operation_execution.operation_exec_id"), nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    item_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    planned_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    actual_qty: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    variance_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    supplier_lot: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    expiry_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    consumption_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    consumed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    consumed_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesMaterialIssues(SQLModel, table=True):
    __tablename__ = "mes_material_issues"
    __table_args__ = {"schema": "mes"}

    issue_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    execution_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_order_execution.execution_id"), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    qty_issued: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    from_location: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    to_location: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    issued_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    issued_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesMaterialReturns(SQLModel, table=True):
    __tablename__ = "mes_material_returns"
    __table_args__ = {"schema": "mes"}

    return_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    execution_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_order_execution.execution_id"), nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    qty_returned: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    return_reason: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    returned_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    returned_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesMlModelVersions(SQLModel, table=True):
    __tablename__ = "mes_ml_model_versions"
    __table_args__ = {"schema": "mes"}

    version_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    model_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_ml_models.model_id"), nullable=False))

    version_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    model_artifact: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    training_data_info: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    accuracy: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    precision: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    recall: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    f1_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    trained_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    trained_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_production: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesMlModels(SQLModel, table=True):
    __tablename__ = "mes_ml_models"
    __table_args__ = {"schema": "mes"}

    model_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    model_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    model_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    framework: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    training_params: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    training_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    validation_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    feature_importance: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    deployment_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    endpoint_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    monitoring_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    retraining_schedule: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesNotifications(SQLModel, table=True):
    __tablename__ = "mes_notifications"
    __table_args__ = {"schema": "mes"}

    notification_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    notification_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    recipient_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    recipient_email: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    recipient_phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    subject: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    channel: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    sent_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    delivered_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    read_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesOeeCalculations(SQLModel, table=True):
    __tablename__ = "mes_oee_calculations"
    __table_args__ = {"schema": "mes"}

    oee_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    work_center_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_centers.work_center_id"), nullable=True))

    production_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_production_lines.production_line_id"), nullable=True))

    shift_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_shifts.shift_id"), nullable=True))

    calculation_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_type: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    available_time_min: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    operating_time_min: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    downtime_min: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    ideal_cycle_time: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    total_parts: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    good_parts: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    defect_parts: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    availability_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    performance_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    quality_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    oee_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesOeeLosses(SQLModel, table=True):
    __tablename__ = "mes_oee_losses"
    __table_args__ = {"schema": "mes"}

    loss_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    oee_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_oee_calculations.oee_id"), nullable=False))

    loss_category: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    loss_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    loss_minutes: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    loss_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesOeeTargets(SQLModel, table=True):
    __tablename__ = "mes_oee_targets"
    __table_args__ = {"schema": "mes"}

    target_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    work_center_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_centers.work_center_id"), nullable=True))

    oee_target: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    availability_target: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    performance_target: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    quality_target: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    effective_from: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_until: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesOperationExecution(SQLModel, table=True):
    __tablename__ = "mes_operation_execution"
    __table_args__ = {"schema": "mes"}

    operation_exec_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    execution_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_order_execution.execution_id"), nullable=False))

    operation_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    operation_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    operation_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    work_center_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_centers.work_center_id"), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    planned_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    completed_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    scrapped_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    rework_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    setup_time_minutes: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    run_time_minutes: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    wait_time_minutes: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    move_time_minutes: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    queue_time_minutes: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    standard_cycle_time: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    actual_cycle_time: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    efficiency_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    yield_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    scrap_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    rework_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    scheduled_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    scheduled_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    operator_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    instructions: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesOperationSteps(SQLModel, table=True):
    __tablename__ = "mes_operation_steps"
    __table_args__ = {"schema": "mes"}

    step_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    operation_exec_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operation_execution.operation_exec_id"), nullable=False))

    step_sequence: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    step_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    instruction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    target_value: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    actual_value: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    pass_fail: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    result: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    step_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    step_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    signed_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    signed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesOperatorAssignments(SQLModel, table=True):
    __tablename__ = "mes_operator_assignments"
    __table_args__ = {"schema": "mes"}

    assignment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    operator_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operators.operator_id"), nullable=False))

    work_center_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_centers.work_center_id"), nullable=True))

    station_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_stations.station_id"), nullable=True))

    assigned_from: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    assigned_until: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    role: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesOperatorCertifications(SQLModel, table=True):
    __tablename__ = "mes_operator_certifications"
    __table_args__ = {"schema": "mes"}

    cert_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    operator_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operators.operator_id"), nullable=False))

    cert_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    cert_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    issue_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    expiry_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesOperatorPerformance(SQLModel, table=True):
    __tablename__ = "mes_operator_performance"
    __table_args__ = {"schema": "mes"}

    performance_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    operator_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operators.operator_id"), nullable=False))

    evaluation_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    productivity_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    quality_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    efficiency_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    error_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    safety_incidents: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesOperatorSchedules(SQLModel, table=True):
    __tablename__ = "mes_operator_schedules"
    __table_args__ = {"schema": "mes"}

    schedule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    operator_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operators.operator_id"), nullable=False))

    shift_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    schedule_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    start_time: Optional[str] = Field(default=None, sa_column=Column(Time, nullable=True))

    end_time: Optional[str] = Field(default=None, sa_column=Column(Time, nullable=True))

    is_overtime: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesOperatorSkills(SQLModel, table=True):
    __tablename__ = "mes_operator_skills"
    __table_args__ = {"schema": "mes"}

    skill_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    operator_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operators.operator_id"), nullable=False))

    skill_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    skill_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    proficiency_level: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    certified: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    certified_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    expiry_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesOperatorTraining(SQLModel, table=True):
    __tablename__ = "mes_operator_training"
    __table_args__ = {"schema": "mes"}

    training_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    operator_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operators.operator_id"), nullable=False))

    training_course: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    training_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    expiry_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    trainer: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    passed: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesOperators(SQLModel, table=True):
    __tablename__ = "mes_operators"
    __table_args__ = {"schema": "mes"}

    operator_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    employee_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    first_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    last_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    email: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    hire_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    badge_rfid: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    department: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    job_title: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesOptimizationProblems(SQLModel, table=True):
    __tablename__ = "mes_optimization_problems"
    __table_args__ = {"schema": "mes"}

    problem_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    problem_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    objective: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    constraints_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    algorithm_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    solver_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    submitted_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    solved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesOptimizationResults(SQLModel, table=True):
    __tablename__ = "mes_optimization_results"
    __table_args__ = {"schema": "mes"}

    result_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_optimization_problems.problem_id"), nullable=False))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    solution_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    gap_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    is_optimal: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    iterations: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    solver_log: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesOrtoolsProblems(SQLModel, table=True):
    __tablename__ = "mes_ortools_problems"
    __table_args__ = {"schema": "mes"}

    problem_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    problem_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    problem_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solver_config: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    solution_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_optimal: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    solver_log: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    solved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesPerformanceActuals(SQLModel, table=True):
    __tablename__ = "mes_performance_actuals"
    __table_args__ = {"schema": "mes"}

    actual_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    metric_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_performance_metrics.metric_id"), nullable=False))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    actual_value: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    target_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    variance: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    period_start: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    period_end: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    recorded_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesPerformanceMetrics(SQLModel, table=True):
    __tablename__ = "mes_performance_metrics"
    __table_args__ = {"schema": "mes"}

    metric_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    metric_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    metric_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    metric_category: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    calculation_method: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    higher_is_better: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesPredictions(SQLModel, table=True):
    __tablename__ = "mes_predictions"
    __table_args__ = {"schema": "mes"}

    prediction_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    model_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_ml_models.model_id"), nullable=True))

    prediction_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    predicted_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    probability: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    confidence_lower: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    confidence_upper: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    features_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    actual_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    prediction_error: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    horizon: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    predicted_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    scenario_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesProductionCells(SQLModel, table=True):
    __tablename__ = "mes_production_cells"
    __table_args__ = {"schema": "mes"}

    cell_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    cell_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    cell_name: str = Field(default=None, sa_column=Column(String(150), nullable=False))

    production_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_production_lines.production_line_id"), nullable=True))

    cell_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesProductionLines(SQLModel, table=True):
    __tablename__ = "mes_production_lines"
    __table_args__ = {"schema": "mes"}

    production_line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    line_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    line_name: str = Field(default=None, sa_column=Column(String(150), nullable=False))

    line_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    supervisor_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    takt_time_seconds: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    cycle_time_seconds: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesPromptTemplates(SQLModel, table=True):
    __tablename__ = "mes_prompt_templates"
    __table_args__ = {"schema": "mes"}

    template_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    template_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    template_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    template_text: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    variables_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    version: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    llm_config_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesQualityHolds(SQLModel, table=True):
    __tablename__ = "mes_quality_holds"
    __table_args__ = {"schema": "mes"}

    hold_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    entity_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    hold_reason: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    hold_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    hold_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    released_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    held_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    released_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    disposition: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesQualityInspections(SQLModel, table=True):
    __tablename__ = "mes_quality_inspections"
    __table_args__ = {"schema": "mes"}

    inspection_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    operation_exec_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operation_execution.operation_exec_id"), nullable=False))

    inspection_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    inspector_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    inspection_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    result: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    measured_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    spec_min: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    spec_max: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    defect_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesQualitySpcData(SQLModel, table=True):
    __tablename__ = "mes_quality_spc_data"
    __table_args__ = {"schema": "mes"}

    spc_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    inspection_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_quality_inspections.inspection_id"), nullable=True))

    operation_exec_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operation_execution.operation_exec_id"), nullable=False))

    sample_size: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    mean_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    std_dev: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    cp: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 4), nullable=True))

    cpk: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 4), nullable=True))

    usl: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    lsl: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    out_of_control: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    sample_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesResourceAvailability(SQLModel, table=True):
    __tablename__ = "mes_resource_availability"
    __table_args__ = {"schema": "mes"}

    availability_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    resource_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_resources.resource_id"), nullable=False))

    available_from: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    available_until: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    available_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesResourceCosts(SQLModel, table=True):
    __tablename__ = "mes_resource_costs"
    __table_args__ = {"schema": "mes"}

    cost_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    resource_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_resources.resource_id"), nullable=False))

    cost_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    cost_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    cost_uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    effective_from: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_until: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesResourceTypes(SQLModel, table=True):
    __tablename__ = "mes_resource_types"
    __table_args__ = {"schema": "mes"}

    resource_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesResources(SQLModel, table=True):
    __tablename__ = "mes_resources"
    __table_args__ = {"schema": "mes"}

    resource_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    resource_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    resource_name: str = Field(default=None, sa_column=Column(String(150), nullable=False))

    resource_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_resource_types.resource_type_id"), nullable=True))

    resource_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesScenarios(SQLModel, table=True):
    __tablename__ = "mes_scenarios"
    __table_args__ = {"schema": "mes"}

    scenario_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    scenario_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    scenario_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    assumptions_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    constraints_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    objectives_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    results_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    comparison_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    recommendations: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    created_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_baseline: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesScheduleResults(SQLModel, table=True):
    __tablename__ = "mes_schedule_results"
    __table_args__ = {"schema": "mes"}

    result_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    problem_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_scheduling_problems.problem_id"), nullable=False))

    schedule_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    makespan: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    total_tardiness: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    machine_utilization: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    objective_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    solve_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_optimal: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    reschedule_trigger: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_applied: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    applied_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesSchedulingProblems(SQLModel, table=True):
    __tablename__ = "mes_scheduling_problems"
    __table_args__ = {"schema": "mes"}

    problem_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    schedule_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    problem_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    jobs_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    machines_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    processing_times: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    setup_times: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    due_dates: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    priorities: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    constraints_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    objective: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    horizon_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    horizon_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesScipyAnalyses(SQLModel, table=True):
    __tablename__ = "mes_scipy_analyses"
    __table_args__ = {"schema": "mes"}

    analysis_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    analysis_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    analysis_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    method: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    result_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    execution_time_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    performed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesSensorCalibrations(SQLModel, table=True):
    __tablename__ = "mes_sensor_calibrations"
    __table_args__ = {"schema": "mes"}

    calibration_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    sensor_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_sensors.sensor_id"), nullable=False))

    calibration_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    calibrated_by: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    result: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    as_found: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    as_left: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    certificate_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    next_calibration_due: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesSensors(SQLModel, table=True):
    __tablename__ = "mes_sensors"
    __table_args__ = {"schema": "mes"}

    sensor_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    sensor_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    sensor_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    sensor_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    model: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    range_min: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    range_max: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    accuracy: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    resolution: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    location_on_equipment: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    last_calibrated: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    calibration_due: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesShiftHandovers(SQLModel, table=True):
    __tablename__ = "mes_shift_handovers"
    __table_args__ = {"schema": "mes"}

    handover_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    work_center_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_centers.work_center_id"), nullable=False))

    from_shift_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    to_shift_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    handover_time: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    issues_reported: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    pending_tasks: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    handed_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    received_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesShiftSchedules(SQLModel, table=True):
    __tablename__ = "mes_shift_schedules"
    __table_args__ = {"schema": "mes"}

    schedule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    work_center_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_centers.work_center_id"), nullable=False))

    shift_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_shifts.shift_id"), nullable=False))

    schedule_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    crew_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_crews.crew_id"), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesShifts(SQLModel, table=True):
    __tablename__ = "mes_shifts"
    __table_args__ = {"schema": "mes"}

    shift_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    shift_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    shift_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    start_time: str = Field(default=None, sa_column=Column(Time, nullable=False))

    end_time: str = Field(default=None, sa_column=Column(Time, nullable=False))

    duration_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(4, 2), nullable=True))

    is_night_shift: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesSolverConfigs(SQLModel, table=True):
    __tablename__ = "mes_solver_configs"
    __table_args__ = {"schema": "mes"}

    solver_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    solver_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    solver_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    version: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    parameters: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_default: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesStationAssignments(SQLModel, table=True):
    __tablename__ = "mes_station_assignments"
    __table_args__ = {"schema": "mes"}

    assignment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    station_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_stations.station_id"), nullable=False))

    work_center_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_centers.work_center_id"), nullable=True))

    assigned_from: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    assigned_until: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesStationTypes(SQLModel, table=True):
    __tablename__ = "mes_station_types"
    __table_args__ = {"schema": "mes"}

    station_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesStations(SQLModel, table=True):
    __tablename__ = "mes_stations"
    __table_args__ = {"schema": "mes"}

    station_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    station_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    station_name: str = Field(default=None, sa_column=Column(String(150), nullable=False))

    station_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_station_types.station_type_id"), nullable=True))

    work_center_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_centers.work_center_id"), nullable=True))

    location: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    has_hmi: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    has_scanner: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    has_printer: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesToolCribs(SQLModel, table=True):
    __tablename__ = "mes_tool_cribs"
    __table_args__ = {"schema": "mes"}

    crib_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    crib_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    crib_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    location: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    dimensions: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    total_capacity: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesToolingAssignments(SQLModel, table=True):
    __tablename__ = "mes_tooling_assignments"
    __table_args__ = {"schema": "mes"}

    assignment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tool_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_tooling_master.tool_id"), nullable=False))

    operation_exec_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_operation_execution.operation_exec_id"), nullable=True))

    equipment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    assigned_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    returned_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    usage_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    assigned_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesToolingLifeTracking(SQLModel, table=True):
    __tablename__ = "mes_tooling_life_tracking"
    __table_args__ = {"schema": "mes"}

    tracking_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tool_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_tooling_master.tool_id"), nullable=False))

    usage_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    max_usage_life: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    total_runtime_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    max_runtime_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    wear_percentage: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    last_maintenance: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    next_maintenance_due: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesToolingMaster(SQLModel, table=True):
    __tablename__ = "mes_tooling_master"
    __table_args__ = {"schema": "mes"}

    tool_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tool_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    tool_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    tool_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_tooling_types.tool_type_id"), nullable=True))

    manufacturer: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    model: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    location: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    shelf_life_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    shelf_life_uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    dimensions: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    weight_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))

    rfid_tag: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    barcode: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesToolingTypes(SQLModel, table=True):
    __tablename__ = "mes_tooling_types"
    __table_args__ = {"schema": "mes"}

    tool_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesVectorStoreConfigs(SQLModel, table=True):
    __tablename__ = "mes_vector_store_configs"
    __table_args__ = {"schema": "mes"}

    config_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    config_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    store_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    connection_string: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    embedding_model: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    collection_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesVectorStoreDocuments(SQLModel, table=True):
    __tablename__ = "mes_vector_store_documents"
    __table_args__ = {"schema": "mes"}

    doc_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    config_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_vector_store_configs.config_id"), nullable=False))

    title: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    content: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    meta_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    embedding_id: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    chunk_index: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesWorkCenterCalendars(SQLModel, table=True):
    __tablename__ = "mes_work_center_calendars"
    __table_args__ = {"schema": "mes"}

    calendar_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    work_center_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_centers.work_center_id"), nullable=False))

    calendar_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    shift_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    available_hours: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    is_working_day: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesWorkCenterCapacities(SQLModel, table=True):
    __tablename__ = "mes_work_center_capacities"
    __table_args__ = {"schema": "mes"}

    capacity_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    work_center_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_centers.work_center_id"), nullable=False))

    capacity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    capacity_value: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    uom: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    effective_from: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    effective_until: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesWorkCenterConstraints(SQLModel, table=True):
    __tablename__ = "mes_work_center_constraints"
    __table_args__ = {"schema": "mes"}

    constraint_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    work_center_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_centers.work_center_id"), nullable=False))

    constraint_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    constraint_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    max_capacity: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    is_bottleneck: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesWorkCenterTypes(SQLModel, table=True):
    __tablename__ = "mes_work_center_types"
    __table_args__ = {"schema": "mes"}

    work_center_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    is_automated: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesWorkCenters(SQLModel, table=True):
    __tablename__ = "mes_work_centers"
    __table_args__ = {"schema": "mes"}

    work_center_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    center_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    center_name: str = Field(default=None, sa_column=Column(String(150), nullable=False))

    center_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    work_center_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_center_types.work_center_type_id"), nullable=True))

    capacity_per_shift: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    efficiency_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    iot_gateway_topic: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesWorkOrderExecution(SQLModel, table=True):
    __tablename__ = "mes_work_order_execution"
    __table_args__ = {"schema": "mes"}

    execution_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    work_order_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    work_order_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    priority: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    product_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    product_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    product_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    planned_qty: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    started_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    completed_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    scrapped_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    rework_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    bom_revision: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    routing_revision: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    scheduled_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    scheduled_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_start: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    actual_end: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    project_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    project_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MesWorkOrderHolds(SQLModel, table=True):
    __tablename__ = "mes_work_order_holds"
    __table_args__ = {"schema": "mes"}

    hold_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    execution_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_order_execution.execution_id"), nullable=False))

    hold_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    hold_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    hold_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    released_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    held_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    released_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesWorkOrderSignatures(SQLModel, table=True):
    __tablename__ = "mes_work_order_signatures"
    __table_args__ = {"schema": "mes"}

    signature_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    execution_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_work_order_execution.execution_id"), nullable=False))

    signature_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    signed_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    signed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    signature_data: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    remarks: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesWorkflowDefinitions(SQLModel, table=True):
    __tablename__ = "mes_workflow_definitions"
    __table_args__ = {"schema": "mes"}

    workflow_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    workflow_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    nodes_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    edges_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    config_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    version: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MesWorkflowExecutions(SQLModel, table=True):
    __tablename__ = "mes_workflow_executions"
    __table_args__ = {"schema": "mes"}

    execution_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mes.mes_workflow_definitions.workflow_id"), nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    state_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    checkpoint_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    inputs_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    outputs_json: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    execution_metrics: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class WorkCenters(SQLModel, table=True):
    __tablename__ = "work_centers"
    __table_args__ = {"schema": "mes"}

    work_center_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    center_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    center_name: str = Field(default=None, sa_column=Column(String(150), nullable=False))

    center_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    iot_gateway_topic: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

