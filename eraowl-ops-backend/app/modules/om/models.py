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
    __table_args__ = {"schema": "om"}

    log_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    state_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    order_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

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
    __table_args__ = {"schema": "om"}

    decision_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    order_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

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
    __table_args__ = {"schema": "om"}

    state_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    order_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

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


class CustomerAttributes(SQLModel, table=True):
    __tablename__ = "customer_attributes"
    __table_args__ = {"schema": "om"}

    partner_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    credit_limit: Optional[float] = Field(default=None, sa_column=Column(Numeric(15, 2), nullable=True))

    price_list_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    payment_term_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    default_warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ImportErrorLog(SQLModel, table=True):
    __tablename__ = "import_error_log"
    __table_args__ = {"schema": "om"}

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


class LineTypes(SQLModel, table=True):
    __tablename__ = "line_types"
    __table_args__ = {"schema": "om"}

    line_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    line_type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    line_type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class OmHeaders(SQLModel, table=True):
    __tablename__ = "om_headers"
    __table_args__ = {"schema": "om"}

    so_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    bu_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    customer_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    so_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    order_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    status: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    order_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    exchange_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 6), nullable=True))

    payment_term_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    salesperson_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    requested_ship_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    promised_delivery_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    ship_to_address_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    bill_to_address_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    source_system: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    source_transaction_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    ship_from_warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class OmLines(SQLModel, table=True):
    __tablename__ = "om_lines"
    __table_args__ = {"schema": "om"}

    so_line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    so_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("om.om_headers.so_id"), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    qty_ordered: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    unit_price: float = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    line_num: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    line_type_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    line_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    need_by_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    promised_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    tax_rate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    taxable_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    discount_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    discount_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    source_line_id: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class OmShipments(SQLModel, table=True):
    __tablename__ = "om_shipments"
    __table_args__ = {"schema": "om"}

    om_shipment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    so_line_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    so_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    shipment_num: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    ship_from_warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    ship_to_warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    ship_to_address_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    carrier_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    tracking_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    qty_ordered: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    qty_shipped: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    qty_delivered: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    qty_invoiced: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    unit_price: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    requested_ship_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    actual_ship_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    requested_delivery_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    actual_delivery_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class OrderImportInterface(SQLModel, table=True):
    __tablename__ = "order_import_interface"
    __table_args__ = {"schema": "om"}

    import_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    source_system: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    source_transaction_id: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    payload: dict = Field(default=None, sa_column=Column(JSONB, nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    retry_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    order_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    processed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class OrderTypes(SQLModel, table=True):
    __tablename__ = "order_types"
    __table_args__ = {"schema": "om"}

    order_type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    order_type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    order_type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ShipmentTracking(SQLModel, table=True):
    __tablename__ = "shipment_tracking"
    __table_args__ = {"schema": "om"}

    tracking_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    order_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    carrier_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    tracking_number: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    ship_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    estimated_arrival: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    actual_arrival: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    shipment_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class WmsCallbacks(SQLModel, table=True):
    __tablename__ = "wms_callbacks"
    __table_args__ = {"schema": "om"}

    callback_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    queue_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    order_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    callback_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    callback_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    processed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    error_message: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class WmsTaskQueue(SQLModel, table=True):
    __tablename__ = "wms_task_queue"
    __table_args__ = {"schema": "om"}

    queue_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    order_line_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    qty_required: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    qty_picked: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    qty_shipped: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    source_warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    dest_warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    assigned_to: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class WorkflowAssignments(SQLModel, table=True):
    __tablename__ = "workflow_assignments"
    __table_args__ = {"schema": "om"}

    assignment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    task_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    assignee_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    assignee_value: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class WorkflowDefinitions(SQLModel, table=True):
    __tablename__ = "workflow_definitions"
    __table_args__ = {"schema": "om"}

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
    __table_args__ = {"schema": "om"}

    task_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    order_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    workflow_def_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    step_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    step_seq: int = Field(default=None, sa_column=Column(Integer, nullable=False))

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

