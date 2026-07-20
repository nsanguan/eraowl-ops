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


class AbcAssignments(SQLModel, table=True):
    __tablename__ = "abc_assignments"
    __table_args__ = {"schema": "inv"}

    assignment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    class_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    compile_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    annual_usage_value: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class AbcClasses(SQLModel, table=True):
    __tablename__ = "abc_classes"
    __table_args__ = {"schema": "inv"}

    class_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    class_code: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    class_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    min_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    max_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class AiAgentLogs(SQLModel, table=True):
    __tablename__ = "ai_agent_logs"
    __table_args__ = {"schema": "inv"}

    log_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    state_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    doc_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    agent_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    action: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    duration_ms: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class AiDecisions(SQLModel, table=True):
    __tablename__ = "ai_decisions"
    __table_args__ = {"schema": "inv"}

    decision_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    doc_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    log_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    decision_type: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    decision_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    reasoning: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    confidence_score: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    accepted: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    accepted_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    accepted_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class AiWorkflowState(SQLModel, table=True):
    __tablename__ = "ai_workflow_state"
    __table_args__ = {"schema": "inv"}

    state_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    doc_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    doc_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    workflow_def_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    thread_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    state_data: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    checkpoint: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CostTypes(SQLModel, table=True):
    __tablename__ = "cost_types"
    __table_args__ = {"schema": "inv"}

    cost_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    cost_type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    cost_type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    costing_method: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CycleCountSchedules(SQLModel, table=True):
    __tablename__ = "cycle_count_schedules"
    __table_args__ = {"schema": "inv"}

    schedule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    schedule_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    schedule_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    class_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    frequency_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ImportErrorLog(SQLModel, table=True):
    __tablename__ = "import_error_log"
    __table_args__ = {"schema": "inv"}

    error_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    import_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    error_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    error_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    retryable: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    resolved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ImportInterface(SQLModel, table=True):
    __tablename__ = "import_interface"
    __table_args__ = {"schema": "inv"}

    import_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    source_system: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    source_transaction_id: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    payload: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    doc_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    retry_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    processed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class InspectionPlans(SQLModel, table=True):
    __tablename__ = "inspection_plans"
    __table_args__ = {"schema": "inv"}

    plan_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    plan_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    plan_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class InspectionResults(SQLModel, table=True):
    __tablename__ = "inspection_results"
    __table_args__ = {"schema": "inv"}

    result_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    transaction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    plan_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    inspector_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    result: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class InvCycleCounts(SQLModel, table=True):
    __tablename__ = "inv_cycle_counts"
    __table_args__ = {"schema": "inv"}

    cycle_count_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    count_sequence: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    expected_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    actual_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    variance_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    count_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    counted_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class InvOnhandBalances(SQLModel, table=True):
    __tablename__ = "inv_onhand_balances"
    __table_args__ = {"schema": "inv"}

    onhand_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    qty_onhand: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    qty_reserved: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    qty_available: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class InvReservations(SQLModel, table=True):
    __tablename__ = "inv_reservations"
    __table_args__ = {"schema": "inv"}

    reservation_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    qty_reserved: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    source_doc_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    source_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    source_doc_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    demand_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    demand_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    reservation_no: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    reservation_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class InvTransactionTypes(SQLModel, table=True):
    __tablename__ = "inv_transaction_types"
    __table_args__ = {"schema": "inv"}

    transaction_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    transaction_type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    transaction_type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    direction: str = Field(default=None, sa_column=Column(String(10), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ItemAttributes(SQLModel, table=True):
    __tablename__ = "item_attributes"
    __table_args__ = {"schema": "inv"}

    item_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    item_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    abc_class: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    lot_control_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    serial_control_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    shelf_life_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    minimum_quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    maximum_quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    safety_stock: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    reorder_point: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    reorder_quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=True))

    average_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=True))

    last_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=True))

    standard_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=True))

    cost_method: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    cycle_count_enabled: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    cycle_count_frequency: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    default_warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    attribute_category: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute1: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute2: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute3: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute4: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute5: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    category_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ItemCosts(SQLModel, table=True):
    __tablename__ = "item_costs"
    __table_args__ = {"schema": "inv"}

    cost_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    cost_type_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    effective_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class LotGenealogy(SQLModel, table=True):
    __tablename__ = "lot_genealogy"
    __table_args__ = {"schema": "inv"}

    geneology_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    lot_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    parent_lot_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    quantity: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    transaction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    direction: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class LotMaster(SQLModel, table=True):
    __tablename__ = "lot_master"
    __table_args__ = {"schema": "inv"}

    lot_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    lot_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    lot_grade: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    lot_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    manufacturing_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    expiration_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    expiry_alert_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    origin: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    supplier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    supplier_lot_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    received_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class LotOnhand(SQLModel, table=True):
    __tablename__ = "lot_onhand"
    __table_args__ = {"schema": "inv"}

    lot_onhand_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    lot_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    qty_onhand: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    qty_reserved: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    qty_available: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class LpnContents(SQLModel, table=True):
    __tablename__ = "lpn_contents"
    __table_args__ = {"schema": "inv"}

    content_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    lpn_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    lot_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    serial_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    quantity: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class LpnMaster(SQLModel, table=True):
    __tablename__ = "lpn_master"
    __table_args__ = {"schema": "inv"}

    lpn_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    lpn_number: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    lpn_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    parent_lpn_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    lot_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    weight_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    volume_cbm: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class MaterialTransactions(SQLModel, table=True):
    __tablename__ = "material_transactions"
    __table_args__ = {"schema": "inv"}

    transaction_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    transaction_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    transaction_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    transaction_source: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    source_doc_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    source_doc_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    source_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_from_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_to_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    serial_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    qty: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=True))

    total_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    reference_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    transaction_date: datetime = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MoveOrderHeaders(SQLModel, table=True):
    __tablename__ = "move_order_headers"
    __table_args__ = {"schema": "inv"}

    move_order_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    move_order_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    source_warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    dest_warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    move_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MoveOrderLines(SQLModel, table=True):
    __tablename__ = "move_order_lines"
    __table_args__ = {"schema": "inv"}

    move_line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    move_order_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    qty_requested: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    qty_moved: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    from_location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    to_location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class PhysicalInventoryHeaders(SQLModel, table=True):
    __tablename__ = "physical_inventory_headers"
    __table_args__ = {"schema": "inv"}

    inv_header_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    inventory_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class PhysicalInventoryLines(SQLModel, table=True):
    __tablename__ = "physical_inventory_lines"
    __table_args__ = {"schema": "inv"}

    inv_line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    inv_header_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    expected_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    actual_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    variance_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class ReplenishmentRules(SQLModel, table=True):
    __tablename__ = "replenishment_rules"
    __table_args__ = {"schema": "inv"}

    rule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    rule_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    rule_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    rule_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    min_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    max_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    reorder_point: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    safety_stock: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    lead_time_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class Serial(SQLModel, table=True):
    __tablename__ = "serial"
    __table_args__ = {"schema": "inv"}

    serial_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    serial_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    item_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    lot_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    lot_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    current_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    manufacture_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    expiry_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    unit_cost: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class SerialGenealogy(SQLModel, table=True):
    __tablename__ = "serial_genealogy"
    __table_args__ = {"schema": "inv"}

    geneology_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    serial_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    parent_serial_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    transaction_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    direction: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class TransferOrderLines(SQLModel, table=True):
    __tablename__ = "transfer_order_lines"
    __table_args__ = {"schema": "inv"}

    transfer_line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    transfer_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    qty_requested: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    qty_shipped: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    qty_received: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class TransferOrders(SQLModel, table=True):
    __tablename__ = "transfer_orders"
    __table_args__ = {"schema": "inv"}

    transfer_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    transfer_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    source_warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    dest_warehouse_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class WorkflowDefinitions(SQLModel, table=True):
    __tablename__ = "workflow_definitions"
    __table_args__ = {"schema": "inv"}

    workflow_def_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    workflow_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    workflow_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    definition: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    version: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class WorkflowTasks(SQLModel, table=True):
    __tablename__ = "workflow_tasks"
    __table_args__ = {"schema": "inv"}

    task_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    doc_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    doc_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    workflow_def_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    step_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    step_seq: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    input_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    output_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    retry_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    max_retries: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    started_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

