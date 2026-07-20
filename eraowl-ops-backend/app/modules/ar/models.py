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


class AccountingEntries(SQLModel, table=True):
    __tablename__ = "accounting_entries"
    __table_args__ = {"schema": "ar"}

    entry_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    doc_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    doc_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    debit_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    credit_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    entry_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    period_name: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    posted: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    posted_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class Adjustments(SQLModel, table=True):
    __tablename__ = "adjustments"
    __table_args__ = {"schema": "ar"}

    adjustment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    adjustment_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    approved_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    approved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class AgingSnapshots(SQLModel, table=True):
    __tablename__ = "aging_snapshots"
    __table_args__ = {"schema": "ar"}

    snapshot_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    customer_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    snapshot_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    current_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    aged_1_30: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    aged_31_60: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    aged_61_90: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    aged_90_plus: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    total_due: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class AiAgentLogs(SQLModel, table=True):
    __tablename__ = "ai_agent_logs"
    __table_args__ = {"schema": "ar"}

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
    __table_args__ = {"schema": "ar"}

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
    __table_args__ = {"schema": "ar"}

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


class ArCustomerLocations(SQLModel, table=True):
    __tablename__ = "ar_customer_locations"
    __table_args__ = {"schema": "ar"}

    location_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    cust_acct_site_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    location_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    address_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    location_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    contact_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    contact_phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    contact_email: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    is_default: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    shipping_instructions: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ArCustomerSites(SQLModel, table=True):
    __tablename__ = "ar_customer_sites"
    __table_args__ = {"schema": "ar"}

    cust_acct_site_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    cust_account_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("ar.ar_customers.cust_account_id"), nullable=False))

    partner_site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    contact_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    contact_email: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    contact_phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    default_warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    default_delivery_method: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    shipping_instructions: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    payment_term_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    tax_registration_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    address_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    site_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    bill_to_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    ship_to_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    ship_partial_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    ship_complete_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    contact_job_title: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    freight_term: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    fob_point: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    taxable_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    tax_code_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    min_order_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(15, 2), nullable=True))

    max_order_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(15, 2), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ArCustomers(SQLModel, table=True):
    __tablename__ = "ar_customers"
    __table_args__ = {"schema": "ar"}

    cust_account_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    partner_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    account_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    account_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    account_status: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    credit_limit: Optional[float] = Field(default=None, sa_column=Column(Numeric(15, 2), nullable=True))

    credit_rating: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    credit_hold_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    credit_hold_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    payment_term_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    payment_method: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    default_currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    price_list_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tax_registration_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    tax_entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    default_receivable_account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    default_revenue_account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    primary_salesperson_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    statement_cycle: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    statement_frequency: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    dunning_level: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    dunning_grace_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    collector_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    risk_category: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    customer_grade: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    customer_since: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    last_sale_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    last_activity_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    industry_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    business_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    hold_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    hold_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    hold_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    hold_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    invoice_matching_required: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    validation_level: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    min_order_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(15, 2), nullable=True))

    max_order_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(15, 2), nullable=True))

    on_time_delivery_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    approved_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    approved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ArInvoiceLines(SQLModel, table=True):
    __tablename__ = "ar_invoice_lines"
    __table_args__ = {"schema": "ar"}

    ar_invoice_line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    ar_invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("ar.ar_invoices.ar_invoice_id"), nullable=False))

    line_number: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    line_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    qty: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    unit_price: float = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=False))

    unit_list_price: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=True))

    discount_percent: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    discount_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    line_total: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    net_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    tax_code_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tax_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    tax_exempt_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    tax_exempt_reason: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    tax_exempt_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    so_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    source_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    source_line_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    revenue_account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    receivable_account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    attribute_category: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute1: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute2: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute3: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute4: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute5: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute6: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute7: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute8: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute9: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute10: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute11: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute12: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute13: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute14: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute15: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class ArInvoices(SQLModel, table=True):
    __tablename__ = "ar_invoices"
    __table_args__ = {"schema": "ar"}

    ar_invoice_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    customer_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    customer_site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    bill_to_site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    ship_to_site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    so_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    invoice_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    invoice_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    invoice_status: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    invoice_class: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    invoice_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    gl_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    terms_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    exchange_rate_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    exchange_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 8), nullable=True))

    exchange_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    currency_code: str = Field(default=None, sa_column=Column(String(3), nullable=False))

    total_lines_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    total_tax_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    total_freight_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    total_charges_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    total_discount_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    total_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    amount_due: float = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=False))

    amount_applied: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    amount_credited: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    amount_adjusted: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    salesperson_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    collector_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    comments: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    reference_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    batch_source_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_paid: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    paid_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    payment_method: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    attribute_category: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute1: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute2: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute3: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute4: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute5: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute6: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute7: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute8: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute9: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute10: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute11: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute12: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute13: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute14: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    attribute15: Optional[str] = Field(default=None, sa_column=Column(String(150), nullable=True))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class BankAccounts(SQLModel, table=True):
    __tablename__ = "bank_accounts"
    __table_args__ = {"schema": "ar"}

    bank_account_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    account_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    account_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    bank_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    account_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    swift_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CashReceipts(SQLModel, table=True):
    __tablename__ = "cash_receipts"
    __table_args__ = {"schema": "ar"}

    receipt_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    receipt_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    customer_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    receipt_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    exchange_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 6), nullable=True))

    receipt_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    method_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    reference: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    bank_account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    reversed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    reversal_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class CollectionTasks(SQLModel, table=True):
    __tablename__ = "collection_tasks"
    __table_args__ = {"schema": "ar"}

    task_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    customer_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    invoice_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    collector_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    task_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    priority: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class CreditHolds(SQLModel, table=True):
    __tablename__ = "credit_holds"
    __table_args__ = {"schema": "ar"}

    hold_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    customer_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    invoice_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    hold_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    hold_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    released_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    released_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    release_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class CreditProfiles(SQLModel, table=True):
    __tablename__ = "credit_profiles"
    __table_args__ = {"schema": "ar"}

    profile_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    customer_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    credit_limit: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    credit_used: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    credit_available: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    credit_score: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    risk_rating: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    review_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    review_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class CustSiteUses(SQLModel, table=True):
    __tablename__ = "cust_site_uses"
    __table_args__ = {"schema": "ar"}

    site_use_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    cust_acct_site_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("ar.ar_customer_sites.cust_acct_site_id"), nullable=False))

    site_use_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    site_use_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class CustomerDeposits(SQLModel, table=True):
    __tablename__ = "customer_deposits"
    __table_args__ = {"schema": "ar"}

    deposit_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    deposit_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    customer_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    deposit_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    remaining_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    receipt_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

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


class DepositApplications(SQLModel, table=True):
    __tablename__ = "deposit_applications"
    __table_args__ = {"schema": "ar"}

    application_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    deposit_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    applied_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    applied_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class DunningHistory(SQLModel, table=True):
    __tablename__ = "dunning_history"
    __table_args__ = {"schema": "ar"}

    dunning_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    customer_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    invoice_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    plan_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    level_num: int = Field(default=None, sa_column=Column(Integer, nullable=False))

    letter_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    response: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class DunningPlans(SQLModel, table=True):
    __tablename__ = "dunning_plans"
    __table_args__ = {"schema": "ar"}

    plan_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    plan_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    plan_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    levels: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    days_between: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ImportErrorLog(SQLModel, table=True):
    __tablename__ = "import_error_log"
    __table_args__ = {"schema": "ar"}

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
    __table_args__ = {"schema": "ar"}

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

    invoice_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    processed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class InvoiceDistributions(SQLModel, table=True):
    __tablename__ = "invoice_distributions"
    __table_args__ = {"schema": "ar"}

    distribution_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    invoice_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    debit_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    credit_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    percent: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class PaymentSchedules(SQLModel, table=True):
    __tablename__ = "payment_schedules"
    __table_args__ = {"schema": "ar"}

    schedule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    installment_num: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    due_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    amount_due: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    amount_remaining: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class PeriodStatus(SQLModel, table=True):
    __tablename__ = "period_status"
    __table_args__ = {"schema": "ar"}

    period_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    period_name: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    start_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    end_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    closed_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    closed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ReceiptApplications(SQLModel, table=True):
    __tablename__ = "receipt_applications"
    __table_args__ = {"schema": "ar"}

    application_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    receipt_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    applied_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    applied_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    discount_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class ReceiptBatches(SQLModel, table=True):
    __tablename__ = "receipt_batches"
    __table_args__ = {"schema": "ar"}

    batch_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    batch_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    batch_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    total_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    receipt_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

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


class RevenueSchedules(SQLModel, table=True):
    __tablename__ = "revenue_schedules"
    __table_args__ = {"schema": "ar"}

    schedule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    invoice_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    recognize_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    recognized: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    recognized_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class TaxCodes(SQLModel, table=True):
    __tablename__ = "tax_codes"
    __table_args__ = {"schema": "ar"}

    tax_code_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    tax_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    tax_rate_pct: float = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=False))

    tax_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class TransactionTypes(SQLModel, table=True):
    __tablename__ = "transaction_types"
    __table_args__ = {"schema": "ar"}

    type_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    type_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    type_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    sign: Optional[str] = Field(default=None, sa_column=Column(String(1), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class WorkflowDefinitions(SQLModel, table=True):
    __tablename__ = "workflow_definitions"
    __table_args__ = {"schema": "ar"}

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
    __table_args__ = {"schema": "ar"}

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

