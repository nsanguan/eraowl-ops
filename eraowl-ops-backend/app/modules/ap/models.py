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
    __table_args__ = {"schema": "ap"}

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


class AgingSnapshots(SQLModel, table=True):
    __tablename__ = "aging_snapshots"
    __table_args__ = {"schema": "ap"}

    snapshot_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    partner_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

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
    __table_args__ = {"schema": "ap"}

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
    __table_args__ = {"schema": "ap"}

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
    __table_args__ = {"schema": "ap"}

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


class ApInvoiceLines(SQLModel, table=True):
    __tablename__ = "ap_invoice_lines"
    __table_args__ = {"schema": "ap"}

    ap_invoice_line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    ap_invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("ap.ap_invoices.ap_invoice_id"), nullable=False))

    line_number: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    item_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    item_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: str = Field(default=None, sa_column=Column(Text, nullable=False))

    quantity: float = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=False))

    uom_code: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    unit_price: float = Field(default=None, sa_column=Column(Numeric(18, 4), nullable=False))

    discount_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    line_total: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tax_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    tax_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    analytic_distribution: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class ApInvoices(SQLModel, table=True):
    __tablename__ = "ap_invoices"
    __table_args__ = {"schema": "ap"}

    ap_invoice_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    invoice_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    supplier_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("ap.ap_suppliers.supplier_id"), nullable=True))

    supplier_site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("ap.ap_supplier_sites.supplier_site_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    currency_id: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    invoice_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    invoice_status: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    po_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    invoice_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    invoice_due_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    date_received: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    gl_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    payment_term_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    payment_method: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    amount_untaxed: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    amount_tax: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    amount_total: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    amount_paid: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    amount_residual: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    tax_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    account_payable_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    payment_reference: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    partner_ref: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    is_paid: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class ApSupplierLocations(SQLModel, table=True):
    __tablename__ = "ap_supplier_locations"
    __table_args__ = {"schema": "ap"}

    location_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    supplier_site_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("ap.ap_supplier_sites.supplier_site_id"), nullable=False))

    supplier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("ap.ap_suppliers.supplier_id"), nullable=False))

    partner_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.parties.party_id"), nullable=False))

    address_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.addresses.address_id"), nullable=False))

    location_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    purchase_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    payment_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    rfq_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    ship_to_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    bill_to_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class ApSupplierSites(SQLModel, table=True):
    __tablename__ = "ap_supplier_sites"
    __table_args__ = {"schema": "ap"}

    supplier_site_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    supplier_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("ap.ap_suppliers.supplier_id"), nullable=False))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    partner_address_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    partner_location_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    payment_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    payment_priority: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    payment_term_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    invoice_currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    bank_account_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    bank_account_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    bank_name: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    bank_branch: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    bank_identifier_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    bank_routing_number: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    email_address: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    phone: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    pay_site_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    purchasing_site_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    receiving_site_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    tax_reporting_site_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    remit_to_supplier_site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    hold_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    hold_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    pay_on_receipt: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    delivery_lead_time_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    supplier_site_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    partner_site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.party_sites.party_site_id"), nullable=True))

    ship_to_warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    bill_to_warehouse_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    lead_time_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    taxable_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    freight_terms: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    min_order_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    max_order_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    ship_via: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    fob_point: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    site_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))


class ApSuppliers(SQLModel, table=True):
    __tablename__ = "ap_suppliers"
    __table_args__ = {"schema": "ap"}

    partner_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    supplier_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    supplier_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    supplier_status: str = Field(default=None, sa_column=Column(String(20), nullable=False))

    payment_term_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    payment_method: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    pay_group: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    default_currency: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    tax_registration_number: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    tax_entity_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    default_expense_account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    default_liability_account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    credit_limit: Optional[float] = Field(default=None, sa_column=Column(Numeric(15, 2), nullable=True))

    risk_category: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    hold_flag: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    hold_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    hold_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    hold_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    invoice_matching_required: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    validation_level: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    supplier_grade: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    po_supplier_code: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    min_order_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    max_order_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(18, 2), nullable=True))

    ship_via: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    fob_point: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    quality_rating: Optional[str] = Field(default=None, sa_column=Column(String(10), nullable=True))

    on_time_delivery_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    approval_status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    approved_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    approved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    supplier_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )


class BankAccounts(SQLModel, table=True):
    __tablename__ = "bank_accounts"
    __table_args__ = {"schema": "ap"}

    bank_account_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    account_name: str = Field(default=None, sa_column=Column(String(200), nullable=False))

    account_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    bank_name: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    bank_branch: Optional[str] = Field(default=None, sa_column=Column(String(200), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    account_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    routing_number: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    swift_code: Optional[str] = Field(default=None, sa_column=Column(String(20), nullable=True))

    iban: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class BankStatementLines(SQLModel, table=True):
    __tablename__ = "bank_statement_lines"
    __table_args__ = {"schema": "ap"}

    line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    statement_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    transaction_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    reference: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    debit_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    credit_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    reconciled: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    payment_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class BankStatements(SQLModel, table=True):
    __tablename__ = "bank_statements"
    __table_args__ = {"schema": "ap"}

    statement_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    bank_account_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    statement_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    ending_balance: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class DiscountTracking(SQLModel, table=True):
    __tablename__ = "discount_tracking"
    __table_args__ = {"schema": "ap"}

    discount_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    discount_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    discount_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    taken: Optional[bool] = Field(default=None, sa_column=Column(Boolean, nullable=True))

    taken_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class ExpenseReportLines(SQLModel, table=True):
    __tablename__ = "expense_report_lines"
    __table_args__ = {"schema": "ap"}

    line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    report_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    expense_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    category: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    tax_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    receipt_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class ExpenseReports(SQLModel, table=True):
    __tablename__ = "expense_reports"
    __table_args__ = {"schema": "ap"}

    report_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    report_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    employee_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    total_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

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


class GlMappingRules(SQLModel, table=True):
    __tablename__ = "gl_mapping_rules"
    __table_args__ = {"schema": "ap"}

    rule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    rule_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    rule_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    source_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    source_value: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class ImportErrorLog(SQLModel, table=True):
    __tablename__ = "import_error_log"
    __table_args__ = {"schema": "ap"}

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
    __table_args__ = {"schema": "ap"}

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


class InvoiceAttachments(SQLModel, table=True):
    __tablename__ = "invoice_attachments"
    __table_args__ = {"schema": "ap"}

    attachment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    file_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))

    file_type: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    file_data: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    file_url: Optional[str] = Field(default=None, sa_column=Column(String(500), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class InvoiceDistributions(SQLModel, table=True):
    __tablename__ = "invoice_distributions"
    __table_args__ = {"schema": "ap"}

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


class InvoiceHolds(SQLModel, table=True):
    __tablename__ = "invoice_holds"
    __table_args__ = {"schema": "ap"}

    hold_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    hold_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

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


class MatchExceptions(SQLModel, table=True):
    __tablename__ = "match_exceptions"
    __table_args__ = {"schema": "ap"}

    exception_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    invoice_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    po_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    receipt_line_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    match_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    exception_code: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    qty_diff: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))

    price_diff: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    amount_diff: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    resolved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class MatchingRules(SQLModel, table=True):
    __tablename__ = "matching_rules"
    __table_args__ = {"schema": "ap"}

    rule_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    rule_code: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    rule_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    match_type: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    quantity_tol_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    price_tol_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    amount_tol: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class PaymentBatches(SQLModel, table=True):
    __tablename__ = "payment_batches"
    __table_args__ = {"schema": "ap"}

    batch_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    batch_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    batch_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    method_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    bank_account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    total_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    payment_count: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

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


class PaymentInstructions(SQLModel, table=True):
    __tablename__ = "payment_instructions"
    __table_args__ = {"schema": "ap"}

    payment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    batch_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    partner_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    payment_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    payment_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

    method_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    bank_account_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    reference: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    status: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    void_reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    voided_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))

    notes: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))

    corporate_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.corporates.corporate_id"), nullable=True))

    company_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.companies.company_id"), nullable=True))

    site_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), ForeignKey("mdm.sites.site_id"), nullable=True))


class PaymentMethods(SQLModel, table=True):
    __tablename__ = "payment_methods"
    __table_args__ = {"schema": "ap"}

    method_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    method_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    method_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class PaymentTerms(SQLModel, table=True):
    __tablename__ = "payment_terms"
    __table_args__ = {"schema": "ap"}

    term_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    term_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    term_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    due_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    discount_days: Optional[int] = Field(default=None, sa_column=Column(Integer, nullable=True))

    discount_pct: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class PeriodStatus(SQLModel, table=True):
    __tablename__ = "period_status"
    __table_args__ = {"schema": "ap"}

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


class PrepaymentApplications(SQLModel, table=True):
    __tablename__ = "prepayment_applications"
    __table_args__ = {"schema": "ap"}

    application_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    prepayment_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    applied_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    applied_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

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


class Prepayments(SQLModel, table=True):
    __tablename__ = "prepayments"
    __table_args__ = {"schema": "ap"}

    prepayment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    invoice_id: uuid.UUID = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=False))

    prepayment_number: str = Field(default=None, sa_column=Column(String(50), nullable=False))

    prepayment_date: date = Field(default=None, sa_column=Column(Date, nullable=False))

    amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    remaining_amount: float = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=False))

    currency_code: Optional[str] = Field(default=None, sa_column=Column(String(3), nullable=True))

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


class TaxCodes(SQLModel, table=True):
    __tablename__ = "tax_codes"
    __table_args__ = {"schema": "ap"}

    tax_code_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    tax_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    tax_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    tax_rate_pct: float = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=False))

    tax_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    recovery_rate: Optional[float] = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class WithholdingTax(SQLModel, table=True):
    __tablename__ = "withholding_tax"
    __table_args__ = {"schema": "ap"}

    wht_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )

    wht_code: str = Field(default=None, sa_column=Column(String(30), nullable=False))

    wht_name: str = Field(default=None, sa_column=Column(String(100), nullable=False))

    wht_rate_pct: float = Field(default=None, sa_column=Column(Numeric(5, 2), nullable=False))

    min_amount: Optional[float] = Field(default=None, sa_column=Column(Numeric(19, 4), nullable=True))

    tax_type: Optional[str] = Field(default=None, sa_column=Column(String(30), nullable=True))

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))

    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))


class WorkflowDefinitions(SQLModel, table=True):
    __tablename__ = "workflow_definitions"
    __table_args__ = {"schema": "ap"}

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
    __table_args__ = {"schema": "ap"}

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

