import uuid
from datetime import date, datetime, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class AccountingEntriesCreate(BaseModel):
    entry_id: uuid.UUID
    doc_type: str
    doc_id: uuid.UUID
    account_id: Optional[uuid.UUID] = None
    debit_amount: Optional[float] = None
    credit_amount: Optional[float] = None
    currency_code: Optional[str] = None
    description: Optional[str] = None
    entry_date: date
    period_name: Optional[str] = None
    posted: Optional[bool] = None
    posted_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AccountingEntriesUpdate(BaseModel):
    entry_id: Optional[uuid.UUID] = None
    doc_type: Optional[str] = None
    doc_id: Optional[uuid.UUID] = None
    account_id: Optional[uuid.UUID] = None
    debit_amount: Optional[float] = None
    credit_amount: Optional[float] = None
    currency_code: Optional[str] = None
    description: Optional[str] = None
    entry_date: Optional[date] = None
    period_name: Optional[str] = None
    posted: Optional[bool] = None
    posted_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AccountingEntriesOut(BaseModel):
    entry_id: uuid.UUID
    doc_type: str
    doc_id: uuid.UUID
    account_id: Optional[uuid.UUID] = None
    debit_amount: Optional[float] = None
    credit_amount: Optional[float] = None
    currency_code: Optional[str] = None
    description: Optional[str] = None
    entry_date: date
    period_name: Optional[str] = None
    posted: Optional[bool] = None
    posted_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class AgingSnapshotsCreate(BaseModel):
    snapshot_id: uuid.UUID
    partner_id: Optional[uuid.UUID] = None
    snapshot_date: date
    current_amount: Optional[float] = None
    aged_1_30: Optional[float] = None
    aged_31_60: Optional[float] = None
    aged_61_90: Optional[float] = None
    aged_90_plus: Optional[float] = None
    total_due: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AgingSnapshotsUpdate(BaseModel):
    snapshot_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    snapshot_date: Optional[date] = None
    current_amount: Optional[float] = None
    aged_1_30: Optional[float] = None
    aged_31_60: Optional[float] = None
    aged_61_90: Optional[float] = None
    aged_90_plus: Optional[float] = None
    total_due: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AgingSnapshotsOut(BaseModel):
    snapshot_id: uuid.UUID
    partner_id: Optional[uuid.UUID] = None
    snapshot_date: date
    current_amount: Optional[float] = None
    aged_1_30: Optional[float] = None
    aged_31_60: Optional[float] = None
    aged_61_90: Optional[float] = None
    aged_90_plus: Optional[float] = None
    total_due: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class AiAgentLogsCreate(BaseModel):
    log_id: uuid.UUID
    state_id: Optional[uuid.UUID] = None
    doc_id: Optional[uuid.UUID] = None
    agent_name: str
    action: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class AiAgentLogsUpdate(BaseModel):
    log_id: Optional[uuid.UUID] = None
    state_id: Optional[uuid.UUID] = None
    doc_id: Optional[uuid.UUID] = None
    agent_name: Optional[str] = None
    action: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class AiAgentLogsOut(BaseModel):
    log_id: uuid.UUID
    state_id: Optional[uuid.UUID] = None
    doc_id: Optional[uuid.UUID] = None
    agent_name: str
    action: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    duration_ms: Optional[int] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class AiDecisionsCreate(BaseModel):
    decision_id: uuid.UUID
    doc_id: Optional[uuid.UUID] = None
    log_id: Optional[uuid.UUID] = None
    decision_type: str
    decision_data: Optional[dict] = None
    reasoning: Optional[str] = None
    confidence_score: Optional[float] = None
    accepted: Optional[bool] = None
    accepted_by: Optional[uuid.UUID] = None
    accepted_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class AiDecisionsUpdate(BaseModel):
    decision_id: Optional[uuid.UUID] = None
    doc_id: Optional[uuid.UUID] = None
    log_id: Optional[uuid.UUID] = None
    decision_type: Optional[str] = None
    decision_data: Optional[dict] = None
    reasoning: Optional[str] = None
    confidence_score: Optional[float] = None
    accepted: Optional[bool] = None
    accepted_by: Optional[uuid.UUID] = None
    accepted_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class AiDecisionsOut(BaseModel):
    decision_id: uuid.UUID
    doc_id: Optional[uuid.UUID] = None
    log_id: Optional[uuid.UUID] = None
    decision_type: str
    decision_data: Optional[dict] = None
    reasoning: Optional[str] = None
    confidence_score: Optional[float] = None
    accepted: Optional[bool] = None
    accepted_by: Optional[uuid.UUID] = None
    accepted_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class AiWorkflowStateCreate(BaseModel):
    state_id: uuid.UUID
    doc_type: str
    doc_id: uuid.UUID
    workflow_def_id: Optional[uuid.UUID] = None
    thread_id: Optional[str] = None
    state_data: dict
    status: Optional[str] = None
    checkpoint: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class AiWorkflowStateUpdate(BaseModel):
    state_id: Optional[uuid.UUID] = None
    doc_type: Optional[str] = None
    doc_id: Optional[uuid.UUID] = None
    workflow_def_id: Optional[uuid.UUID] = None
    thread_id: Optional[str] = None
    state_data: Optional[dict] = None
    status: Optional[str] = None
    checkpoint: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class AiWorkflowStateOut(BaseModel):
    state_id: uuid.UUID
    doc_type: str
    doc_id: uuid.UUID
    workflow_def_id: Optional[uuid.UUID] = None
    thread_id: Optional[str] = None
    state_data: dict
    status: Optional[str] = None
    checkpoint: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ApInvoiceLinesCreate(BaseModel):
    ap_invoice_line_id: uuid.UUID
    ap_invoice_id: uuid.UUID
    line_number: Optional[int] = None
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    description: str
    quantity: float
    uom_code: Optional[str] = None
    unit_price: float
    discount_pct: Optional[float] = None
    line_total: Optional[float] = None
    account_id: Optional[uuid.UUID] = None
    tax_id: Optional[uuid.UUID] = None
    tax_amount: Optional[float] = None
    analytic_distribution: Optional[dict] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ApInvoiceLinesUpdate(BaseModel):
    ap_invoice_line_id: Optional[uuid.UUID] = None
    ap_invoice_id: Optional[uuid.UUID] = None
    line_number: Optional[int] = None
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[float] = None
    uom_code: Optional[str] = None
    unit_price: Optional[float] = None
    discount_pct: Optional[float] = None
    line_total: Optional[float] = None
    account_id: Optional[uuid.UUID] = None
    tax_id: Optional[uuid.UUID] = None
    tax_amount: Optional[float] = None
    analytic_distribution: Optional[dict] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ApInvoiceLinesOut(BaseModel):
    ap_invoice_line_id: uuid.UUID
    ap_invoice_id: uuid.UUID
    line_number: Optional[int] = None
    item_id: Optional[uuid.UUID] = None
    item_code: Optional[str] = None
    description: str
    quantity: float
    uom_code: Optional[str] = None
    unit_price: float
    discount_pct: Optional[float] = None
    line_total: Optional[float] = None
    account_id: Optional[uuid.UUID] = None
    tax_id: Optional[uuid.UUID] = None
    tax_amount: Optional[float] = None
    analytic_distribution: Optional[dict] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ApInvoicesCreate(BaseModel):
    ap_invoice_id: uuid.UUID
    invoice_number: str
    supplier_id: Optional[uuid.UUID] = None
    supplier_site_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    currency_id: Optional[str] = None
    invoice_type: str
    invoice_status: str
    po_id: Optional[uuid.UUID] = None
    invoice_date: date
    invoice_due_date: Optional[date] = None
    date_received: Optional[date] = None
    gl_date: Optional[date] = None
    payment_term_days: Optional[int] = None
    payment_method: Optional[str] = None
    description: Optional[str] = None
    amount_untaxed: Optional[float] = None
    amount_tax: Optional[float] = None
    amount_total: Optional[float] = None
    amount_paid: Optional[float] = None
    amount_residual: Optional[float] = None
    tax_id: Optional[uuid.UUID] = None
    account_payable_id: Optional[uuid.UUID] = None
    payment_reference: Optional[str] = None
    partner_ref: Optional[str] = None
    is_paid: Optional[bool] = None
    notes: Optional[str] = None
    is_active: bool = True
    corporate_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ApInvoicesUpdate(BaseModel):
    ap_invoice_id: Optional[uuid.UUID] = None
    invoice_number: Optional[str] = None
    supplier_id: Optional[uuid.UUID] = None
    supplier_site_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    currency_id: Optional[str] = None
    invoice_type: Optional[str] = None
    invoice_status: Optional[str] = None
    po_id: Optional[uuid.UUID] = None
    invoice_date: Optional[date] = None
    invoice_due_date: Optional[date] = None
    date_received: Optional[date] = None
    gl_date: Optional[date] = None
    payment_term_days: Optional[int] = None
    payment_method: Optional[str] = None
    description: Optional[str] = None
    amount_untaxed: Optional[float] = None
    amount_tax: Optional[float] = None
    amount_total: Optional[float] = None
    amount_paid: Optional[float] = None
    amount_residual: Optional[float] = None
    tax_id: Optional[uuid.UUID] = None
    account_payable_id: Optional[uuid.UUID] = None
    payment_reference: Optional[str] = None
    partner_ref: Optional[str] = None
    is_paid: Optional[bool] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    corporate_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ApInvoicesOut(BaseModel):
    ap_invoice_id: uuid.UUID
    invoice_number: str
    supplier_id: Optional[uuid.UUID] = None
    supplier_site_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    currency_id: Optional[str] = None
    invoice_type: str
    invoice_status: str
    po_id: Optional[uuid.UUID] = None
    invoice_date: date
    invoice_due_date: Optional[date] = None
    date_received: Optional[date] = None
    gl_date: Optional[date] = None
    payment_term_days: Optional[int] = None
    payment_method: Optional[str] = None
    description: Optional[str] = None
    amount_untaxed: Optional[float] = None
    amount_tax: Optional[float] = None
    amount_total: Optional[float] = None
    amount_paid: Optional[float] = None
    amount_residual: Optional[float] = None
    tax_id: Optional[uuid.UUID] = None
    account_payable_id: Optional[uuid.UUID] = None
    payment_reference: Optional[str] = None
    partner_ref: Optional[str] = None
    is_paid: Optional[bool] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ApSupplierLocationsCreate(BaseModel):
    location_id: uuid.UUID
    supplier_site_id: uuid.UUID
    supplier_id: uuid.UUID
    partner_id: uuid.UUID
    address_id: uuid.UUID
    location_name: Optional[str] = None
    purchase_flag: Optional[bool] = None
    payment_flag: Optional[bool] = None
    rfq_flag: Optional[bool] = None
    ship_to_flag: Optional[bool] = None
    bill_to_flag: Optional[bool] = None
    is_active: bool = True

class ApSupplierLocationsUpdate(BaseModel):
    location_id: Optional[uuid.UUID] = None
    supplier_site_id: Optional[uuid.UUID] = None
    supplier_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    address_id: Optional[uuid.UUID] = None
    location_name: Optional[str] = None
    purchase_flag: Optional[bool] = None
    payment_flag: Optional[bool] = None
    rfq_flag: Optional[bool] = None
    ship_to_flag: Optional[bool] = None
    bill_to_flag: Optional[bool] = None
    is_active: Optional[bool] = None

class ApSupplierLocationsOut(BaseModel):
    location_id: uuid.UUID
    supplier_site_id: uuid.UUID
    supplier_id: uuid.UUID
    partner_id: uuid.UUID
    address_id: uuid.UUID
    location_name: Optional[str] = None
    purchase_flag: Optional[bool] = None
    payment_flag: Optional[bool] = None
    rfq_flag: Optional[bool] = None
    ship_to_flag: Optional[bool] = None
    bill_to_flag: Optional[bool] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ApSupplierSitesCreate(BaseModel):
    supplier_site_id: uuid.UUID
    supplier_id: uuid.UUID
    site_id: Optional[uuid.UUID] = None
    partner_address_id: Optional[uuid.UUID] = None
    partner_location_id: Optional[uuid.UUID] = None
    payment_type: Optional[str] = None
    payment_priority: Optional[int] = None
    payment_term_days: Optional[int] = None
    invoice_currency: Optional[str] = None
    bank_account_name: Optional[str] = None
    bank_account_number: Optional[str] = None
    bank_name: Optional[str] = None
    bank_branch: Optional[str] = None
    bank_identifier_code: Optional[str] = None
    bank_routing_number: Optional[str] = None
    email_address: Optional[str] = None
    phone: Optional[str] = None
    pay_site_flag: Optional[bool] = None
    purchasing_site_flag: Optional[bool] = None
    receiving_site_flag: Optional[bool] = None
    tax_reporting_site_flag: Optional[bool] = None
    remit_to_supplier_site_id: Optional[uuid.UUID] = None
    hold_flag: Optional[bool] = None
    hold_reason: Optional[str] = None
    pay_on_receipt: Optional[bool] = None
    delivery_lead_time_days: Optional[int] = None
    notes: Optional[str] = None
    is_active: bool = True
    supplier_site_code: Optional[str] = None
    partner_site_id: Optional[uuid.UUID] = None
    ship_to_warehouse_id: Optional[uuid.UUID] = None
    bill_to_warehouse_id: Optional[uuid.UUID] = None
    lead_time_days: Optional[int] = None
    taxable_flag: Optional[bool] = None
    freight_terms: Optional[str] = None
    min_order_amount: Optional[float] = None
    max_order_amount: Optional[float] = None
    currency_code: Optional[str] = None
    ship_via: Optional[str] = None
    fob_point: Optional[str] = None
    site_code: Optional[str] = None

class ApSupplierSitesUpdate(BaseModel):
    supplier_site_id: Optional[uuid.UUID] = None
    supplier_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    partner_address_id: Optional[uuid.UUID] = None
    partner_location_id: Optional[uuid.UUID] = None
    payment_type: Optional[str] = None
    payment_priority: Optional[int] = None
    payment_term_days: Optional[int] = None
    invoice_currency: Optional[str] = None
    bank_account_name: Optional[str] = None
    bank_account_number: Optional[str] = None
    bank_name: Optional[str] = None
    bank_branch: Optional[str] = None
    bank_identifier_code: Optional[str] = None
    bank_routing_number: Optional[str] = None
    email_address: Optional[str] = None
    phone: Optional[str] = None
    pay_site_flag: Optional[bool] = None
    purchasing_site_flag: Optional[bool] = None
    receiving_site_flag: Optional[bool] = None
    tax_reporting_site_flag: Optional[bool] = None
    remit_to_supplier_site_id: Optional[uuid.UUID] = None
    hold_flag: Optional[bool] = None
    hold_reason: Optional[str] = None
    pay_on_receipt: Optional[bool] = None
    delivery_lead_time_days: Optional[int] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    supplier_site_code: Optional[str] = None
    partner_site_id: Optional[uuid.UUID] = None
    ship_to_warehouse_id: Optional[uuid.UUID] = None
    bill_to_warehouse_id: Optional[uuid.UUID] = None
    lead_time_days: Optional[int] = None
    taxable_flag: Optional[bool] = None
    freight_terms: Optional[str] = None
    min_order_amount: Optional[float] = None
    max_order_amount: Optional[float] = None
    currency_code: Optional[str] = None
    ship_via: Optional[str] = None
    fob_point: Optional[str] = None
    site_code: Optional[str] = None

class ApSupplierSitesOut(BaseModel):
    supplier_site_id: uuid.UUID
    supplier_id: uuid.UUID
    site_id: Optional[uuid.UUID] = None
    partner_address_id: Optional[uuid.UUID] = None
    partner_location_id: Optional[uuid.UUID] = None
    payment_type: Optional[str] = None
    payment_priority: Optional[int] = None
    payment_term_days: Optional[int] = None
    invoice_currency: Optional[str] = None
    bank_account_name: Optional[str] = None
    bank_account_number: Optional[str] = None
    bank_name: Optional[str] = None
    bank_branch: Optional[str] = None
    bank_identifier_code: Optional[str] = None
    bank_routing_number: Optional[str] = None
    email_address: Optional[str] = None
    phone: Optional[str] = None
    pay_site_flag: Optional[bool] = None
    purchasing_site_flag: Optional[bool] = None
    receiving_site_flag: Optional[bool] = None
    tax_reporting_site_flag: Optional[bool] = None
    remit_to_supplier_site_id: Optional[uuid.UUID] = None
    hold_flag: Optional[bool] = None
    hold_reason: Optional[str] = None
    pay_on_receipt: Optional[bool] = None
    delivery_lead_time_days: Optional[int] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    supplier_site_code: Optional[str] = None
    partner_site_id: Optional[uuid.UUID] = None
    ship_to_warehouse_id: Optional[uuid.UUID] = None
    bill_to_warehouse_id: Optional[uuid.UUID] = None
    lead_time_days: Optional[int] = None
    taxable_flag: Optional[bool] = None
    freight_terms: Optional[str] = None
    min_order_amount: Optional[float] = None
    max_order_amount: Optional[float] = None
    currency_code: Optional[str] = None
    ship_via: Optional[str] = None
    fob_point: Optional[str] = None
    site_code: Optional[str] = None
    model_config = {"from_attributes": True}

class ApSuppliersCreate(BaseModel):
    partner_id: uuid.UUID
    supplier_number: str
    supplier_type: str
    supplier_status: str
    payment_term_days: Optional[int] = None
    payment_method: Optional[str] = None
    pay_group: Optional[str] = None
    default_currency: Optional[str] = None
    tax_registration_number: Optional[str] = None
    tax_entity_type: Optional[str] = None
    default_expense_account_id: Optional[uuid.UUID] = None
    default_liability_account_id: Optional[uuid.UUID] = None
    credit_limit: Optional[float] = None
    risk_category: Optional[str] = None
    hold_flag: Optional[bool] = None
    hold_reason: Optional[str] = None
    hold_date: Optional[date] = None
    hold_by: Optional[uuid.UUID] = None
    invoice_matching_required: Optional[str] = None
    validation_level: Optional[str] = None
    supplier_grade: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    po_supplier_code: Optional[str] = None
    min_order_amount: Optional[float] = None
    max_order_amount: Optional[float] = None
    ship_via: Optional[str] = None
    fob_point: Optional[str] = None
    quality_rating: Optional[str] = None
    on_time_delivery_rate: Optional[float] = None
    approval_status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    supplier_id: uuid.UUID

class ApSuppliersUpdate(BaseModel):
    partner_id: Optional[uuid.UUID] = None
    supplier_number: Optional[str] = None
    supplier_type: Optional[str] = None
    supplier_status: Optional[str] = None
    payment_term_days: Optional[int] = None
    payment_method: Optional[str] = None
    pay_group: Optional[str] = None
    default_currency: Optional[str] = None
    tax_registration_number: Optional[str] = None
    tax_entity_type: Optional[str] = None
    default_expense_account_id: Optional[uuid.UUID] = None
    default_liability_account_id: Optional[uuid.UUID] = None
    credit_limit: Optional[float] = None
    risk_category: Optional[str] = None
    hold_flag: Optional[bool] = None
    hold_reason: Optional[str] = None
    hold_date: Optional[date] = None
    hold_by: Optional[uuid.UUID] = None
    invoice_matching_required: Optional[str] = None
    validation_level: Optional[str] = None
    supplier_grade: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    po_supplier_code: Optional[str] = None
    min_order_amount: Optional[float] = None
    max_order_amount: Optional[float] = None
    ship_via: Optional[str] = None
    fob_point: Optional[str] = None
    quality_rating: Optional[str] = None
    on_time_delivery_rate: Optional[float] = None
    approval_status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    supplier_id: Optional[uuid.UUID] = None

class ApSuppliersOut(BaseModel):
    partner_id: uuid.UUID
    supplier_number: str
    supplier_type: str
    supplier_status: str
    payment_term_days: Optional[int] = None
    payment_method: Optional[str] = None
    pay_group: Optional[str] = None
    default_currency: Optional[str] = None
    tax_registration_number: Optional[str] = None
    tax_entity_type: Optional[str] = None
    default_expense_account_id: Optional[uuid.UUID] = None
    default_liability_account_id: Optional[uuid.UUID] = None
    credit_limit: Optional[float] = None
    risk_category: Optional[str] = None
    hold_flag: Optional[bool] = None
    hold_reason: Optional[str] = None
    hold_date: Optional[date] = None
    hold_by: Optional[uuid.UUID] = None
    invoice_matching_required: Optional[str] = None
    validation_level: Optional[str] = None
    supplier_grade: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    po_supplier_code: Optional[str] = None
    min_order_amount: Optional[float] = None
    max_order_amount: Optional[float] = None
    ship_via: Optional[str] = None
    fob_point: Optional[str] = None
    quality_rating: Optional[str] = None
    on_time_delivery_rate: Optional[float] = None
    approval_status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    supplier_id: uuid.UUID
    model_config = {"from_attributes": True}

class BankAccountsCreate(BaseModel):
    bank_account_id: uuid.UUID
    account_name: str
    account_number: str
    bank_name: Optional[str] = None
    bank_branch: Optional[str] = None
    currency_code: Optional[str] = None
    account_type: Optional[str] = None
    routing_number: Optional[str] = None
    swift_code: Optional[str] = None
    iban: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class BankAccountsUpdate(BaseModel):
    bank_account_id: Optional[uuid.UUID] = None
    account_name: Optional[str] = None
    account_number: Optional[str] = None
    bank_name: Optional[str] = None
    bank_branch: Optional[str] = None
    currency_code: Optional[str] = None
    account_type: Optional[str] = None
    routing_number: Optional[str] = None
    swift_code: Optional[str] = None
    iban: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class BankAccountsOut(BaseModel):
    bank_account_id: uuid.UUID
    account_name: str
    account_number: str
    bank_name: Optional[str] = None
    bank_branch: Optional[str] = None
    currency_code: Optional[str] = None
    account_type: Optional[str] = None
    routing_number: Optional[str] = None
    swift_code: Optional[str] = None
    iban: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class BankStatementLinesCreate(BaseModel):
    line_id: uuid.UUID
    statement_id: uuid.UUID
    transaction_date: date
    description: Optional[str] = None
    reference: Optional[str] = None
    debit_amount: Optional[float] = None
    credit_amount: Optional[float] = None
    reconciled: Optional[bool] = None
    payment_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class BankStatementLinesUpdate(BaseModel):
    line_id: Optional[uuid.UUID] = None
    statement_id: Optional[uuid.UUID] = None
    transaction_date: Optional[date] = None
    description: Optional[str] = None
    reference: Optional[str] = None
    debit_amount: Optional[float] = None
    credit_amount: Optional[float] = None
    reconciled: Optional[bool] = None
    payment_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class BankStatementLinesOut(BaseModel):
    line_id: uuid.UUID
    statement_id: uuid.UUID
    transaction_date: date
    description: Optional[str] = None
    reference: Optional[str] = None
    debit_amount: Optional[float] = None
    credit_amount: Optional[float] = None
    reconciled: Optional[bool] = None
    payment_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class BankStatementsCreate(BaseModel):
    statement_id: uuid.UUID
    bank_account_id: uuid.UUID
    statement_date: date
    ending_balance: float
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class BankStatementsUpdate(BaseModel):
    statement_id: Optional[uuid.UUID] = None
    bank_account_id: Optional[uuid.UUID] = None
    statement_date: Optional[date] = None
    ending_balance: Optional[float] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class BankStatementsOut(BaseModel):
    statement_id: uuid.UUID
    bank_account_id: uuid.UUID
    statement_date: date
    ending_balance: float
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class DiscountTrackingCreate(BaseModel):
    discount_id: uuid.UUID
    invoice_id: uuid.UUID
    discount_date: Optional[date] = None
    discount_amount: Optional[float] = None
    taken: Optional[bool] = None
    taken_date: Optional[date] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DiscountTrackingUpdate(BaseModel):
    discount_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    discount_date: Optional[date] = None
    discount_amount: Optional[float] = None
    taken: Optional[bool] = None
    taken_date: Optional[date] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DiscountTrackingOut(BaseModel):
    discount_id: uuid.UUID
    invoice_id: uuid.UUID
    discount_date: Optional[date] = None
    discount_amount: Optional[float] = None
    taken: Optional[bool] = None
    taken_date: Optional[date] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ExpenseReportLinesCreate(BaseModel):
    line_id: uuid.UUID
    report_id: uuid.UUID
    expense_date: date
    category: Optional[str] = None
    description: Optional[str] = None
    amount: float
    tax_amount: Optional[float] = None
    receipt_url: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ExpenseReportLinesUpdate(BaseModel):
    line_id: Optional[uuid.UUID] = None
    report_id: Optional[uuid.UUID] = None
    expense_date: Optional[date] = None
    category: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    tax_amount: Optional[float] = None
    receipt_url: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ExpenseReportLinesOut(BaseModel):
    line_id: uuid.UUID
    report_id: uuid.UUID
    expense_date: date
    category: Optional[str] = None
    description: Optional[str] = None
    amount: float
    tax_amount: Optional[float] = None
    receipt_url: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ExpenseReportsCreate(BaseModel):
    report_id: uuid.UUID
    report_number: str
    employee_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    total_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ExpenseReportsUpdate(BaseModel):
    report_id: Optional[uuid.UUID] = None
    report_number: Optional[str] = None
    employee_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    total_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ExpenseReportsOut(BaseModel):
    report_id: uuid.UUID
    report_number: str
    employee_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    total_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class GlMappingRulesCreate(BaseModel):
    rule_id: uuid.UUID
    rule_code: str
    rule_name: str
    source_type: str
    source_value: Optional[str] = None
    account_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1

class GlMappingRulesUpdate(BaseModel):
    rule_id: Optional[uuid.UUID] = None
    rule_code: Optional[str] = None
    rule_name: Optional[str] = None
    source_type: Optional[str] = None
    source_value: Optional[str] = None
    account_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class GlMappingRulesOut(BaseModel):
    rule_id: uuid.UUID
    rule_code: str
    rule_name: str
    source_type: str
    source_value: Optional[str] = None
    account_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ImportErrorLogCreate(BaseModel):
    error_id: uuid.UUID
    import_id: Optional[uuid.UUID] = None
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    error_data: Optional[dict] = None
    retryable: Optional[bool] = None
    resolved_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class ImportErrorLogUpdate(BaseModel):
    error_id: Optional[uuid.UUID] = None
    import_id: Optional[uuid.UUID] = None
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    error_data: Optional[dict] = None
    retryable: Optional[bool] = None
    resolved_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class ImportErrorLogOut(BaseModel):
    error_id: uuid.UUID
    import_id: Optional[uuid.UUID] = None
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    error_data: Optional[dict] = None
    retryable: Optional[bool] = None
    resolved_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ImportInterfaceCreate(BaseModel):
    import_id: uuid.UUID
    source_system: str
    source_transaction_id: str
    payload: dict
    doc_type: Optional[str] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    invoice_id: Optional[uuid.UUID] = None
    processed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class ImportInterfaceUpdate(BaseModel):
    import_id: Optional[uuid.UUID] = None
    source_system: Optional[str] = None
    source_transaction_id: Optional[str] = None
    payload: Optional[dict] = None
    doc_type: Optional[str] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    invoice_id: Optional[uuid.UUID] = None
    processed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class ImportInterfaceOut(BaseModel):
    import_id: uuid.UUID
    source_system: str
    source_transaction_id: str
    payload: dict
    doc_type: Optional[str] = None
    status: Optional[str] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    invoice_id: Optional[uuid.UUID] = None
    processed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class InvoiceAttachmentsCreate(BaseModel):
    attachment_id: uuid.UUID
    invoice_id: uuid.UUID
    file_name: Optional[str] = None
    file_type: Optional[str] = None
    file_data: Optional[str] = None
    file_url: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class InvoiceAttachmentsUpdate(BaseModel):
    attachment_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    file_name: Optional[str] = None
    file_type: Optional[str] = None
    file_data: Optional[str] = None
    file_url: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class InvoiceAttachmentsOut(BaseModel):
    attachment_id: uuid.UUID
    invoice_id: uuid.UUID
    file_name: Optional[str] = None
    file_type: Optional[str] = None
    file_data: Optional[str] = None
    file_url: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class InvoiceDistributionsCreate(BaseModel):
    distribution_id: uuid.UUID
    invoice_id: uuid.UUID
    invoice_line_id: Optional[uuid.UUID] = None
    account_id: Optional[uuid.UUID] = None
    debit_amount: Optional[float] = None
    credit_amount: Optional[float] = None
    percent: Optional[float] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InvoiceDistributionsUpdate(BaseModel):
    distribution_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    invoice_line_id: Optional[uuid.UUID] = None
    account_id: Optional[uuid.UUID] = None
    debit_amount: Optional[float] = None
    credit_amount: Optional[float] = None
    percent: Optional[float] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InvoiceDistributionsOut(BaseModel):
    distribution_id: uuid.UUID
    invoice_id: uuid.UUID
    invoice_line_id: Optional[uuid.UUID] = None
    account_id: Optional[uuid.UUID] = None
    debit_amount: Optional[float] = None
    credit_amount: Optional[float] = None
    percent: Optional[float] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class InvoiceHoldsCreate(BaseModel):
    hold_id: uuid.UUID
    invoice_id: uuid.UUID
    hold_type: str
    hold_reason: Optional[str] = None
    hold_date: date
    released_by: Optional[uuid.UUID] = None
    released_at: Optional[datetime] = None
    release_reason: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InvoiceHoldsUpdate(BaseModel):
    hold_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    hold_type: Optional[str] = None
    hold_reason: Optional[str] = None
    hold_date: Optional[date] = None
    released_by: Optional[uuid.UUID] = None
    released_at: Optional[datetime] = None
    release_reason: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class InvoiceHoldsOut(BaseModel):
    hold_id: uuid.UUID
    invoice_id: uuid.UUID
    hold_type: str
    hold_reason: Optional[str] = None
    hold_date: date
    released_by: Optional[uuid.UUID] = None
    released_at: Optional[datetime] = None
    release_reason: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MatchExceptionsCreate(BaseModel):
    exception_id: uuid.UUID
    invoice_id: uuid.UUID
    invoice_line_id: Optional[uuid.UUID] = None
    po_line_id: Optional[uuid.UUID] = None
    receipt_line_id: Optional[uuid.UUID] = None
    match_type: str
    exception_code: Optional[str] = None
    description: Optional[str] = None
    qty_diff: Optional[float] = None
    price_diff: Optional[float] = None
    amount_diff: Optional[float] = None
    status: Optional[str] = None
    resolved_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MatchExceptionsUpdate(BaseModel):
    exception_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    invoice_line_id: Optional[uuid.UUID] = None
    po_line_id: Optional[uuid.UUID] = None
    receipt_line_id: Optional[uuid.UUID] = None
    match_type: Optional[str] = None
    exception_code: Optional[str] = None
    description: Optional[str] = None
    qty_diff: Optional[float] = None
    price_diff: Optional[float] = None
    amount_diff: Optional[float] = None
    status: Optional[str] = None
    resolved_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class MatchExceptionsOut(BaseModel):
    exception_id: uuid.UUID
    invoice_id: uuid.UUID
    invoice_line_id: Optional[uuid.UUID] = None
    po_line_id: Optional[uuid.UUID] = None
    receipt_line_id: Optional[uuid.UUID] = None
    match_type: str
    exception_code: Optional[str] = None
    description: Optional[str] = None
    qty_diff: Optional[float] = None
    price_diff: Optional[float] = None
    amount_diff: Optional[float] = None
    status: Optional[str] = None
    resolved_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class MatchingRulesCreate(BaseModel):
    rule_id: uuid.UUID
    rule_code: str
    rule_name: str
    match_type: str
    quantity_tol_pct: Optional[float] = None
    price_tol_pct: Optional[float] = None
    amount_tol: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class MatchingRulesUpdate(BaseModel):
    rule_id: Optional[uuid.UUID] = None
    rule_code: Optional[str] = None
    rule_name: Optional[str] = None
    match_type: Optional[str] = None
    quantity_tol_pct: Optional[float] = None
    price_tol_pct: Optional[float] = None
    amount_tol: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class MatchingRulesOut(BaseModel):
    rule_id: uuid.UUID
    rule_code: str
    rule_name: str
    match_type: str
    quantity_tol_pct: Optional[float] = None
    price_tol_pct: Optional[float] = None
    amount_tol: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class PaymentBatchesCreate(BaseModel):
    batch_id: uuid.UUID
    batch_number: str
    batch_date: date
    method_id: Optional[uuid.UUID] = None
    bank_account_id: Optional[uuid.UUID] = None
    total_amount: Optional[float] = None
    payment_count: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PaymentBatchesUpdate(BaseModel):
    batch_id: Optional[uuid.UUID] = None
    batch_number: Optional[str] = None
    batch_date: Optional[date] = None
    method_id: Optional[uuid.UUID] = None
    bank_account_id: Optional[uuid.UUID] = None
    total_amount: Optional[float] = None
    payment_count: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PaymentBatchesOut(BaseModel):
    batch_id: uuid.UUID
    batch_number: str
    batch_date: date
    method_id: Optional[uuid.UUID] = None
    bank_account_id: Optional[uuid.UUID] = None
    total_amount: Optional[float] = None
    payment_count: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class PaymentInstructionsCreate(BaseModel):
    payment_id: uuid.UUID
    batch_id: Optional[uuid.UUID] = None
    invoice_id: uuid.UUID
    partner_id: Optional[uuid.UUID] = None
    payment_number: str
    payment_date: date
    amount: float
    currency_code: Optional[str] = None
    method_id: Optional[uuid.UUID] = None
    bank_account_id: Optional[uuid.UUID] = None
    reference: Optional[str] = None
    status: Optional[str] = None
    void_reason: Optional[str] = None
    voided_at: Optional[datetime] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PaymentInstructionsUpdate(BaseModel):
    payment_id: Optional[uuid.UUID] = None
    batch_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    payment_number: Optional[str] = None
    payment_date: Optional[date] = None
    amount: Optional[float] = None
    currency_code: Optional[str] = None
    method_id: Optional[uuid.UUID] = None
    bank_account_id: Optional[uuid.UUID] = None
    reference: Optional[str] = None
    status: Optional[str] = None
    void_reason: Optional[str] = None
    voided_at: Optional[datetime] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PaymentInstructionsOut(BaseModel):
    payment_id: uuid.UUID
    batch_id: Optional[uuid.UUID] = None
    invoice_id: uuid.UUID
    partner_id: Optional[uuid.UUID] = None
    payment_number: str
    payment_date: date
    amount: float
    currency_code: Optional[str] = None
    method_id: Optional[uuid.UUID] = None
    bank_account_id: Optional[uuid.UUID] = None
    reference: Optional[str] = None
    status: Optional[str] = None
    void_reason: Optional[str] = None
    voided_at: Optional[datetime] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class PaymentMethodsCreate(BaseModel):
    method_id: uuid.UUID
    method_code: str
    method_name: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class PaymentMethodsUpdate(BaseModel):
    method_id: Optional[uuid.UUID] = None
    method_code: Optional[str] = None
    method_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class PaymentMethodsOut(BaseModel):
    method_id: uuid.UUID
    method_code: str
    method_name: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class PaymentTermsCreate(BaseModel):
    term_id: uuid.UUID
    term_code: str
    term_name: str
    due_days: Optional[int] = None
    discount_days: Optional[int] = None
    discount_pct: Optional[float] = None
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class PaymentTermsUpdate(BaseModel):
    term_id: Optional[uuid.UUID] = None
    term_code: Optional[str] = None
    term_name: Optional[str] = None
    due_days: Optional[int] = None
    discount_days: Optional[int] = None
    discount_pct: Optional[float] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class PaymentTermsOut(BaseModel):
    term_id: uuid.UUID
    term_code: str
    term_name: str
    due_days: Optional[int] = None
    discount_days: Optional[int] = None
    discount_pct: Optional[float] = None
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class PeriodStatusCreate(BaseModel):
    period_id: uuid.UUID
    period_name: str
    start_date: date
    end_date: date
    status: Optional[str] = None
    closed_by: Optional[uuid.UUID] = None
    closed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class PeriodStatusUpdate(BaseModel):
    period_id: Optional[uuid.UUID] = None
    period_name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[str] = None
    closed_by: Optional[uuid.UUID] = None
    closed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class PeriodStatusOut(BaseModel):
    period_id: uuid.UUID
    period_name: str
    start_date: date
    end_date: date
    status: Optional[str] = None
    closed_by: Optional[uuid.UUID] = None
    closed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class PrepaymentApplicationsCreate(BaseModel):
    application_id: uuid.UUID
    prepayment_id: uuid.UUID
    invoice_id: uuid.UUID
    applied_date: date
    applied_amount: float
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PrepaymentApplicationsUpdate(BaseModel):
    application_id: Optional[uuid.UUID] = None
    prepayment_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    applied_date: Optional[date] = None
    applied_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PrepaymentApplicationsOut(BaseModel):
    application_id: uuid.UUID
    prepayment_id: uuid.UUID
    invoice_id: uuid.UUID
    applied_date: date
    applied_amount: float
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class PrepaymentsCreate(BaseModel):
    prepayment_id: uuid.UUID
    invoice_id: uuid.UUID
    prepayment_number: str
    prepayment_date: date
    amount: float
    remaining_amount: float
    currency_code: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PrepaymentsUpdate(BaseModel):
    prepayment_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    prepayment_number: Optional[str] = None
    prepayment_date: Optional[date] = None
    amount: Optional[float] = None
    remaining_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PrepaymentsOut(BaseModel):
    prepayment_id: uuid.UUID
    invoice_id: uuid.UUID
    prepayment_number: str
    prepayment_date: date
    amount: float
    remaining_amount: float
    currency_code: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class TaxCodesCreate(BaseModel):
    tax_code_id: uuid.UUID
    tax_code: str
    tax_name: str
    tax_rate_pct: float
    tax_type: Optional[str] = None
    recovery_rate: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1

class TaxCodesUpdate(BaseModel):
    tax_code_id: Optional[uuid.UUID] = None
    tax_code: Optional[str] = None
    tax_name: Optional[str] = None
    tax_rate_pct: Optional[float] = None
    tax_type: Optional[str] = None
    recovery_rate: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class TaxCodesOut(BaseModel):
    tax_code_id: uuid.UUID
    tax_code: str
    tax_name: str
    tax_rate_pct: float
    tax_type: Optional[str] = None
    recovery_rate: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class WithholdingTaxCreate(BaseModel):
    wht_id: uuid.UUID
    wht_code: str
    wht_name: str
    wht_rate_pct: float
    min_amount: Optional[float] = None
    tax_type: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class WithholdingTaxUpdate(BaseModel):
    wht_id: Optional[uuid.UUID] = None
    wht_code: Optional[str] = None
    wht_name: Optional[str] = None
    wht_rate_pct: Optional[float] = None
    min_amount: Optional[float] = None
    tax_type: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class WithholdingTaxOut(BaseModel):
    wht_id: uuid.UUID
    wht_code: str
    wht_name: str
    wht_rate_pct: float
    min_amount: Optional[float] = None
    tax_type: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class WorkflowDefinitionsCreate(BaseModel):
    workflow_def_id: uuid.UUID
    workflow_code: str
    workflow_name: str
    description: Optional[str] = None
    definition: dict
    version: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class WorkflowDefinitionsUpdate(BaseModel):
    workflow_def_id: Optional[uuid.UUID] = None
    workflow_code: Optional[str] = None
    workflow_name: Optional[str] = None
    description: Optional[str] = None
    definition: Optional[dict] = None
    version: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class WorkflowDefinitionsOut(BaseModel):
    workflow_def_id: uuid.UUID
    workflow_code: str
    workflow_name: str
    description: Optional[str] = None
    definition: dict
    version: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class WorkflowTasksCreate(BaseModel):
    task_id: uuid.UUID
    doc_type: str
    doc_id: uuid.UUID
    workflow_def_id: Optional[uuid.UUID] = None
    step_name: str
    step_seq: Optional[int] = None
    status: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    max_retries: Optional[int] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    assigned_to: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class WorkflowTasksUpdate(BaseModel):
    task_id: Optional[uuid.UUID] = None
    doc_type: Optional[str] = None
    doc_id: Optional[uuid.UUID] = None
    workflow_def_id: Optional[uuid.UUID] = None
    step_name: Optional[str] = None
    step_seq: Optional[int] = None
    status: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    max_retries: Optional[int] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    assigned_to: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class WorkflowTasksOut(BaseModel):
    task_id: uuid.UUID
    doc_type: str
    doc_id: uuid.UUID
    workflow_def_id: Optional[uuid.UUID] = None
    step_name: str
    step_seq: Optional[int] = None
    status: Optional[str] = None
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = None
    max_retries: Optional[int] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    assigned_to: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}
