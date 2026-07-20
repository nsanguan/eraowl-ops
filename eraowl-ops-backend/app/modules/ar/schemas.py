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

class AdjustmentsCreate(BaseModel):
    adjustment_id: uuid.UUID
    invoice_id: uuid.UUID
    adjustment_type: str
    amount: float
    currency_code: Optional[str] = None
    reason: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AdjustmentsUpdate(BaseModel):
    adjustment_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    adjustment_type: Optional[str] = None
    amount: Optional[float] = None
    currency_code: Optional[str] = None
    reason: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class AdjustmentsOut(BaseModel):
    adjustment_id: uuid.UUID
    invoice_id: uuid.UUID
    adjustment_type: str
    amount: float
    currency_code: Optional[str] = None
    reason: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
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

class AgingSnapshotsCreate(BaseModel):
    snapshot_id: uuid.UUID
    customer_id: Optional[uuid.UUID] = None
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
    customer_id: Optional[uuid.UUID] = None
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
    customer_id: Optional[uuid.UUID] = None
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

class ArCustomerLocationsCreate(BaseModel):
    location_id: uuid.UUID
    cust_acct_site_id: uuid.UUID
    location_type: str
    address_id: Optional[uuid.UUID] = None
    location_code: Optional[str] = None
    location_name: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    is_default: Optional[bool] = None
    shipping_instructions: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class ArCustomerLocationsUpdate(BaseModel):
    location_id: Optional[uuid.UUID] = None
    cust_acct_site_id: Optional[uuid.UUID] = None
    location_type: Optional[str] = None
    address_id: Optional[uuid.UUID] = None
    location_code: Optional[str] = None
    location_name: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    is_default: Optional[bool] = None
    shipping_instructions: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class ArCustomerLocationsOut(BaseModel):
    location_id: uuid.UUID
    cust_acct_site_id: uuid.UUID
    location_type: str
    address_id: Optional[uuid.UUID] = None
    location_code: Optional[str] = None
    location_name: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    is_default: Optional[bool] = None
    shipping_instructions: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ArCustomerSitesCreate(BaseModel):
    cust_acct_site_id: uuid.UUID
    cust_account_id: uuid.UUID
    partner_site_id: Optional[uuid.UUID] = None
    site_name: Optional[str] = None
    contact_name: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    default_warehouse_id: Optional[uuid.UUID] = None
    default_delivery_method: Optional[str] = None
    shipping_instructions: Optional[str] = None
    payment_term_days: Optional[int] = None
    tax_registration_number: Optional[str] = None
    is_active: bool = True
    address_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    site_code: Optional[str] = None
    bill_to_flag: Optional[bool] = None
    ship_to_flag: Optional[bool] = None
    ship_partial_flag: Optional[bool] = None
    ship_complete_flag: Optional[bool] = None
    contact_job_title: Optional[str] = None
    freight_term: Optional[str] = None
    fob_point: Optional[str] = None
    taxable_flag: Optional[bool] = None
    tax_code_id: Optional[uuid.UUID] = None
    currency_code: Optional[str] = None
    min_order_amount: Optional[float] = None
    max_order_amount: Optional[float] = None
    object_version_number: int = 1

class ArCustomerSitesUpdate(BaseModel):
    cust_acct_site_id: Optional[uuid.UUID] = None
    cust_account_id: Optional[uuid.UUID] = None
    partner_site_id: Optional[uuid.UUID] = None
    site_name: Optional[str] = None
    contact_name: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    default_warehouse_id: Optional[uuid.UUID] = None
    default_delivery_method: Optional[str] = None
    shipping_instructions: Optional[str] = None
    payment_term_days: Optional[int] = None
    tax_registration_number: Optional[str] = None
    is_active: Optional[bool] = None
    address_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    site_code: Optional[str] = None
    bill_to_flag: Optional[bool] = None
    ship_to_flag: Optional[bool] = None
    ship_partial_flag: Optional[bool] = None
    ship_complete_flag: Optional[bool] = None
    contact_job_title: Optional[str] = None
    freight_term: Optional[str] = None
    fob_point: Optional[str] = None
    taxable_flag: Optional[bool] = None
    tax_code_id: Optional[uuid.UUID] = None
    currency_code: Optional[str] = None
    min_order_amount: Optional[float] = None
    max_order_amount: Optional[float] = None
    object_version_number: Optional[int] = None

class ArCustomerSitesOut(BaseModel):
    cust_acct_site_id: uuid.UUID
    cust_account_id: uuid.UUID
    partner_site_id: Optional[uuid.UUID] = None
    site_name: Optional[str] = None
    contact_name: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    default_warehouse_id: Optional[uuid.UUID] = None
    default_delivery_method: Optional[str] = None
    shipping_instructions: Optional[str] = None
    payment_term_days: Optional[int] = None
    tax_registration_number: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    address_id: Optional[uuid.UUID] = None
    location_id: Optional[uuid.UUID] = None
    site_code: Optional[str] = None
    bill_to_flag: Optional[bool] = None
    ship_to_flag: Optional[bool] = None
    ship_partial_flag: Optional[bool] = None
    ship_complete_flag: Optional[bool] = None
    contact_job_title: Optional[str] = None
    freight_term: Optional[str] = None
    fob_point: Optional[str] = None
    taxable_flag: Optional[bool] = None
    tax_code_id: Optional[uuid.UUID] = None
    currency_code: Optional[str] = None
    min_order_amount: Optional[float] = None
    max_order_amount: Optional[float] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ArCustomersCreate(BaseModel):
    cust_account_id: uuid.UUID
    partner_id: uuid.UUID
    account_number: str
    account_type: str
    account_status: str
    credit_limit: Optional[float] = None
    credit_rating: Optional[str] = None
    credit_hold_flag: Optional[bool] = None
    credit_hold_reason: Optional[str] = None
    payment_term_days: Optional[int] = None
    payment_method: Optional[str] = None
    default_currency: Optional[str] = None
    price_list_id: Optional[uuid.UUID] = None
    tax_registration_number: Optional[str] = None
    tax_entity_type: Optional[str] = None
    default_receivable_account_id: Optional[uuid.UUID] = None
    default_revenue_account_id: Optional[uuid.UUID] = None
    primary_salesperson_id: Optional[uuid.UUID] = None
    statement_cycle: Optional[str] = None
    statement_frequency: Optional[str] = None
    dunning_level: Optional[str] = None
    dunning_grace_days: Optional[int] = None
    collector_id: Optional[uuid.UUID] = None
    risk_category: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    customer_grade: Optional[str] = None
    customer_since: Optional[date] = None
    last_sale_date: Optional[date] = None
    last_activity_date: Optional[date] = None
    industry_code: Optional[str] = None
    business_type: Optional[str] = None
    hold_flag: Optional[bool] = None
    hold_reason: Optional[str] = None
    hold_date: Optional[date] = None
    hold_by: Optional[uuid.UUID] = None
    invoice_matching_required: Optional[str] = None
    validation_level: Optional[str] = None
    min_order_amount: Optional[float] = None
    max_order_amount: Optional[float] = None
    on_time_delivery_rate: Optional[float] = None
    approval_status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    object_version_number: int = 1

class ArCustomersUpdate(BaseModel):
    cust_account_id: Optional[uuid.UUID] = None
    partner_id: Optional[uuid.UUID] = None
    account_number: Optional[str] = None
    account_type: Optional[str] = None
    account_status: Optional[str] = None
    credit_limit: Optional[float] = None
    credit_rating: Optional[str] = None
    credit_hold_flag: Optional[bool] = None
    credit_hold_reason: Optional[str] = None
    payment_term_days: Optional[int] = None
    payment_method: Optional[str] = None
    default_currency: Optional[str] = None
    price_list_id: Optional[uuid.UUID] = None
    tax_registration_number: Optional[str] = None
    tax_entity_type: Optional[str] = None
    default_receivable_account_id: Optional[uuid.UUID] = None
    default_revenue_account_id: Optional[uuid.UUID] = None
    primary_salesperson_id: Optional[uuid.UUID] = None
    statement_cycle: Optional[str] = None
    statement_frequency: Optional[str] = None
    dunning_level: Optional[str] = None
    dunning_grace_days: Optional[int] = None
    collector_id: Optional[uuid.UUID] = None
    risk_category: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    customer_grade: Optional[str] = None
    customer_since: Optional[date] = None
    last_sale_date: Optional[date] = None
    last_activity_date: Optional[date] = None
    industry_code: Optional[str] = None
    business_type: Optional[str] = None
    hold_flag: Optional[bool] = None
    hold_reason: Optional[str] = None
    hold_date: Optional[date] = None
    hold_by: Optional[uuid.UUID] = None
    invoice_matching_required: Optional[str] = None
    validation_level: Optional[str] = None
    min_order_amount: Optional[float] = None
    max_order_amount: Optional[float] = None
    on_time_delivery_rate: Optional[float] = None
    approval_status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    object_version_number: Optional[int] = None

class ArCustomersOut(BaseModel):
    cust_account_id: uuid.UUID
    partner_id: uuid.UUID
    account_number: str
    account_type: str
    account_status: str
    credit_limit: Optional[float] = None
    credit_rating: Optional[str] = None
    credit_hold_flag: Optional[bool] = None
    credit_hold_reason: Optional[str] = None
    payment_term_days: Optional[int] = None
    payment_method: Optional[str] = None
    default_currency: Optional[str] = None
    price_list_id: Optional[uuid.UUID] = None
    tax_registration_number: Optional[str] = None
    tax_entity_type: Optional[str] = None
    default_receivable_account_id: Optional[uuid.UUID] = None
    default_revenue_account_id: Optional[uuid.UUID] = None
    primary_salesperson_id: Optional[uuid.UUID] = None
    statement_cycle: Optional[str] = None
    statement_frequency: Optional[str] = None
    dunning_level: Optional[str] = None
    dunning_grace_days: Optional[int] = None
    collector_id: Optional[uuid.UUID] = None
    risk_category: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    customer_grade: Optional[str] = None
    customer_since: Optional[date] = None
    last_sale_date: Optional[date] = None
    last_activity_date: Optional[date] = None
    industry_code: Optional[str] = None
    business_type: Optional[str] = None
    hold_flag: Optional[bool] = None
    hold_reason: Optional[str] = None
    hold_date: Optional[date] = None
    hold_by: Optional[uuid.UUID] = None
    invoice_matching_required: Optional[str] = None
    validation_level: Optional[str] = None
    min_order_amount: Optional[float] = None
    max_order_amount: Optional[float] = None
    on_time_delivery_rate: Optional[float] = None
    approval_status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ArInvoiceLinesCreate(BaseModel):
    ar_invoice_line_id: uuid.UUID
    ar_invoice_id: uuid.UUID
    line_number: int
    line_type: str
    item_id: Optional[uuid.UUID] = None
    item_description: Optional[str] = None
    uom_code: Optional[str] = None
    qty: float
    unit_price: float
    unit_list_price: Optional[float] = None
    discount_percent: Optional[float] = None
    discount_amount: Optional[float] = None
    line_total: Optional[float] = None
    net_amount: Optional[float] = None
    tax_code_id: Optional[uuid.UUID] = None
    tax_amount: Optional[float] = None
    tax_exempt_flag: Optional[bool] = None
    tax_exempt_reason: Optional[str] = None
    tax_exempt_number: Optional[str] = None
    so_line_id: Optional[uuid.UUID] = None
    source_line_id: Optional[uuid.UUID] = None
    source_line_type: Optional[str] = None
    revenue_account_id: Optional[uuid.UUID] = None
    receivable_account_id: Optional[uuid.UUID] = None
    attribute_category: Optional[str] = None
    attribute1: Optional[str] = None
    attribute2: Optional[str] = None
    attribute3: Optional[str] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    attribute6: Optional[str] = None
    attribute7: Optional[str] = None
    attribute8: Optional[str] = None
    attribute9: Optional[str] = None
    attribute10: Optional[str] = None
    attribute11: Optional[str] = None
    attribute12: Optional[str] = None
    attribute13: Optional[str] = None
    attribute14: Optional[str] = None
    attribute15: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ArInvoiceLinesUpdate(BaseModel):
    ar_invoice_line_id: Optional[uuid.UUID] = None
    ar_invoice_id: Optional[uuid.UUID] = None
    line_number: Optional[int] = None
    line_type: Optional[str] = None
    item_id: Optional[uuid.UUID] = None
    item_description: Optional[str] = None
    uom_code: Optional[str] = None
    qty: Optional[float] = None
    unit_price: Optional[float] = None
    unit_list_price: Optional[float] = None
    discount_percent: Optional[float] = None
    discount_amount: Optional[float] = None
    line_total: Optional[float] = None
    net_amount: Optional[float] = None
    tax_code_id: Optional[uuid.UUID] = None
    tax_amount: Optional[float] = None
    tax_exempt_flag: Optional[bool] = None
    tax_exempt_reason: Optional[str] = None
    tax_exempt_number: Optional[str] = None
    so_line_id: Optional[uuid.UUID] = None
    source_line_id: Optional[uuid.UUID] = None
    source_line_type: Optional[str] = None
    revenue_account_id: Optional[uuid.UUID] = None
    receivable_account_id: Optional[uuid.UUID] = None
    attribute_category: Optional[str] = None
    attribute1: Optional[str] = None
    attribute2: Optional[str] = None
    attribute3: Optional[str] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    attribute6: Optional[str] = None
    attribute7: Optional[str] = None
    attribute8: Optional[str] = None
    attribute9: Optional[str] = None
    attribute10: Optional[str] = None
    attribute11: Optional[str] = None
    attribute12: Optional[str] = None
    attribute13: Optional[str] = None
    attribute14: Optional[str] = None
    attribute15: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ArInvoiceLinesOut(BaseModel):
    ar_invoice_line_id: uuid.UUID
    ar_invoice_id: uuid.UUID
    line_number: int
    line_type: str
    item_id: Optional[uuid.UUID] = None
    item_description: Optional[str] = None
    uom_code: Optional[str] = None
    qty: float
    unit_price: float
    unit_list_price: Optional[float] = None
    discount_percent: Optional[float] = None
    discount_amount: Optional[float] = None
    line_total: Optional[float] = None
    net_amount: Optional[float] = None
    tax_code_id: Optional[uuid.UUID] = None
    tax_amount: Optional[float] = None
    tax_exempt_flag: Optional[bool] = None
    tax_exempt_reason: Optional[str] = None
    tax_exempt_number: Optional[str] = None
    so_line_id: Optional[uuid.UUID] = None
    source_line_id: Optional[uuid.UUID] = None
    source_line_type: Optional[str] = None
    revenue_account_id: Optional[uuid.UUID] = None
    receivable_account_id: Optional[uuid.UUID] = None
    attribute_category: Optional[str] = None
    attribute1: Optional[str] = None
    attribute2: Optional[str] = None
    attribute3: Optional[str] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    attribute6: Optional[str] = None
    attribute7: Optional[str] = None
    attribute8: Optional[str] = None
    attribute9: Optional[str] = None
    attribute10: Optional[str] = None
    attribute11: Optional[str] = None
    attribute12: Optional[str] = None
    attribute13: Optional[str] = None
    attribute14: Optional[str] = None
    attribute15: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ArInvoicesCreate(BaseModel):
    ar_invoice_id: uuid.UUID
    company_id: Optional[uuid.UUID] = None
    customer_id: uuid.UUID
    customer_site_id: Optional[uuid.UUID] = None
    bill_to_site_id: Optional[uuid.UUID] = None
    ship_to_site_id: Optional[uuid.UUID] = None
    so_id: Optional[uuid.UUID] = None
    invoice_number: str
    invoice_type: str
    invoice_status: str
    invoice_class: Optional[str] = None
    invoice_date: date
    gl_date: Optional[date] = None
    due_date: Optional[date] = None
    terms_id: Optional[uuid.UUID] = None
    exchange_rate_type: Optional[str] = None
    exchange_rate: Optional[float] = None
    exchange_date: Optional[date] = None
    currency_code: str
    total_lines_amount: Optional[float] = None
    total_tax_amount: Optional[float] = None
    total_freight_amount: Optional[float] = None
    total_charges_amount: Optional[float] = None
    total_discount_amount: Optional[float] = None
    total_amount: Optional[float] = None
    amount_due: float
    amount_applied: Optional[float] = None
    amount_credited: Optional[float] = None
    amount_adjusted: Optional[float] = None
    salesperson_id: Optional[uuid.UUID] = None
    collector_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    comments: Optional[str] = None
    reference_number: Optional[str] = None
    batch_source_id: Optional[uuid.UUID] = None
    is_paid: Optional[bool] = None
    paid_date: Optional[date] = None
    payment_method: Optional[str] = None
    attribute_category: Optional[str] = None
    attribute1: Optional[str] = None
    attribute2: Optional[str] = None
    attribute3: Optional[str] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    attribute6: Optional[str] = None
    attribute7: Optional[str] = None
    attribute8: Optional[str] = None
    attribute9: Optional[str] = None
    attribute10: Optional[str] = None
    attribute11: Optional[str] = None
    attribute12: Optional[str] = None
    attribute13: Optional[str] = None
    attribute14: Optional[str] = None
    attribute15: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ArInvoicesUpdate(BaseModel):
    ar_invoice_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    customer_id: Optional[uuid.UUID] = None
    customer_site_id: Optional[uuid.UUID] = None
    bill_to_site_id: Optional[uuid.UUID] = None
    ship_to_site_id: Optional[uuid.UUID] = None
    so_id: Optional[uuid.UUID] = None
    invoice_number: Optional[str] = None
    invoice_type: Optional[str] = None
    invoice_status: Optional[str] = None
    invoice_class: Optional[str] = None
    invoice_date: Optional[date] = None
    gl_date: Optional[date] = None
    due_date: Optional[date] = None
    terms_id: Optional[uuid.UUID] = None
    exchange_rate_type: Optional[str] = None
    exchange_rate: Optional[float] = None
    exchange_date: Optional[date] = None
    currency_code: Optional[str] = None
    total_lines_amount: Optional[float] = None
    total_tax_amount: Optional[float] = None
    total_freight_amount: Optional[float] = None
    total_charges_amount: Optional[float] = None
    total_discount_amount: Optional[float] = None
    total_amount: Optional[float] = None
    amount_due: Optional[float] = None
    amount_applied: Optional[float] = None
    amount_credited: Optional[float] = None
    amount_adjusted: Optional[float] = None
    salesperson_id: Optional[uuid.UUID] = None
    collector_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    comments: Optional[str] = None
    reference_number: Optional[str] = None
    batch_source_id: Optional[uuid.UUID] = None
    is_paid: Optional[bool] = None
    paid_date: Optional[date] = None
    payment_method: Optional[str] = None
    attribute_category: Optional[str] = None
    attribute1: Optional[str] = None
    attribute2: Optional[str] = None
    attribute3: Optional[str] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    attribute6: Optional[str] = None
    attribute7: Optional[str] = None
    attribute8: Optional[str] = None
    attribute9: Optional[str] = None
    attribute10: Optional[str] = None
    attribute11: Optional[str] = None
    attribute12: Optional[str] = None
    attribute13: Optional[str] = None
    attribute14: Optional[str] = None
    attribute15: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ArInvoicesOut(BaseModel):
    ar_invoice_id: uuid.UUID
    company_id: Optional[uuid.UUID] = None
    customer_id: uuid.UUID
    customer_site_id: Optional[uuid.UUID] = None
    bill_to_site_id: Optional[uuid.UUID] = None
    ship_to_site_id: Optional[uuid.UUID] = None
    so_id: Optional[uuid.UUID] = None
    invoice_number: str
    invoice_type: str
    invoice_status: str
    invoice_class: Optional[str] = None
    invoice_date: date
    gl_date: Optional[date] = None
    due_date: Optional[date] = None
    terms_id: Optional[uuid.UUID] = None
    exchange_rate_type: Optional[str] = None
    exchange_rate: Optional[float] = None
    exchange_date: Optional[date] = None
    currency_code: str
    total_lines_amount: Optional[float] = None
    total_tax_amount: Optional[float] = None
    total_freight_amount: Optional[float] = None
    total_charges_amount: Optional[float] = None
    total_discount_amount: Optional[float] = None
    total_amount: Optional[float] = None
    amount_due: float
    amount_applied: Optional[float] = None
    amount_credited: Optional[float] = None
    amount_adjusted: Optional[float] = None
    salesperson_id: Optional[uuid.UUID] = None
    collector_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    comments: Optional[str] = None
    reference_number: Optional[str] = None
    batch_source_id: Optional[uuid.UUID] = None
    is_paid: Optional[bool] = None
    paid_date: Optional[date] = None
    payment_method: Optional[str] = None
    attribute_category: Optional[str] = None
    attribute1: Optional[str] = None
    attribute2: Optional[str] = None
    attribute3: Optional[str] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    attribute6: Optional[str] = None
    attribute7: Optional[str] = None
    attribute8: Optional[str] = None
    attribute9: Optional[str] = None
    attribute10: Optional[str] = None
    attribute11: Optional[str] = None
    attribute12: Optional[str] = None
    attribute13: Optional[str] = None
    attribute14: Optional[str] = None
    attribute15: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class BankAccountsCreate(BaseModel):
    bank_account_id: uuid.UUID
    account_name: str
    account_number: str
    bank_name: Optional[str] = None
    currency_code: Optional[str] = None
    account_type: Optional[str] = None
    swift_code: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class BankAccountsUpdate(BaseModel):
    bank_account_id: Optional[uuid.UUID] = None
    account_name: Optional[str] = None
    account_number: Optional[str] = None
    bank_name: Optional[str] = None
    currency_code: Optional[str] = None
    account_type: Optional[str] = None
    swift_code: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class BankAccountsOut(BaseModel):
    bank_account_id: uuid.UUID
    account_name: str
    account_number: str
    bank_name: Optional[str] = None
    currency_code: Optional[str] = None
    account_type: Optional[str] = None
    swift_code: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CashReceiptsCreate(BaseModel):
    receipt_id: uuid.UUID
    receipt_number: str
    customer_id: Optional[uuid.UUID] = None
    receipt_date: date
    amount: float
    currency_code: Optional[str] = None
    exchange_rate: Optional[float] = None
    receipt_type: Optional[str] = None
    method_id: Optional[uuid.UUID] = None
    reference: Optional[str] = None
    bank_account_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    reversed_at: Optional[datetime] = None
    reversal_reason: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class CashReceiptsUpdate(BaseModel):
    receipt_id: Optional[uuid.UUID] = None
    receipt_number: Optional[str] = None
    customer_id: Optional[uuid.UUID] = None
    receipt_date: Optional[date] = None
    amount: Optional[float] = None
    currency_code: Optional[str] = None
    exchange_rate: Optional[float] = None
    receipt_type: Optional[str] = None
    method_id: Optional[uuid.UUID] = None
    reference: Optional[str] = None
    bank_account_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    reversed_at: Optional[datetime] = None
    reversal_reason: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class CashReceiptsOut(BaseModel):
    receipt_id: uuid.UUID
    receipt_number: str
    customer_id: Optional[uuid.UUID] = None
    receipt_date: date
    amount: float
    currency_code: Optional[str] = None
    exchange_rate: Optional[float] = None
    receipt_type: Optional[str] = None
    method_id: Optional[uuid.UUID] = None
    reference: Optional[str] = None
    bank_account_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    reversed_at: Optional[datetime] = None
    reversal_reason: Optional[str] = None
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

class CollectionTasksCreate(BaseModel):
    task_id: uuid.UUID
    customer_id: uuid.UUID
    invoice_id: Optional[uuid.UUID] = None
    collector_id: Optional[uuid.UUID] = None
    task_type: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    due_date: Optional[date] = None
    completed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class CollectionTasksUpdate(BaseModel):
    task_id: Optional[uuid.UUID] = None
    customer_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    collector_id: Optional[uuid.UUID] = None
    task_type: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    due_date: Optional[date] = None
    completed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class CollectionTasksOut(BaseModel):
    task_id: uuid.UUID
    customer_id: uuid.UUID
    invoice_id: Optional[uuid.UUID] = None
    collector_id: Optional[uuid.UUID] = None
    task_type: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    due_date: Optional[date] = None
    completed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class CreditHoldsCreate(BaseModel):
    hold_id: uuid.UUID
    customer_id: uuid.UUID
    invoice_id: Optional[uuid.UUID] = None
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

class CreditHoldsUpdate(BaseModel):
    hold_id: Optional[uuid.UUID] = None
    customer_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
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

class CreditHoldsOut(BaseModel):
    hold_id: uuid.UUID
    customer_id: uuid.UUID
    invoice_id: Optional[uuid.UUID] = None
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

class CreditProfilesCreate(BaseModel):
    profile_id: uuid.UUID
    customer_id: uuid.UUID
    credit_limit: Optional[float] = None
    credit_used: Optional[float] = None
    credit_available: Optional[float] = None
    credit_score: Optional[str] = None
    risk_rating: Optional[str] = None
    review_date: Optional[date] = None
    review_by: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class CreditProfilesUpdate(BaseModel):
    profile_id: Optional[uuid.UUID] = None
    customer_id: Optional[uuid.UUID] = None
    credit_limit: Optional[float] = None
    credit_used: Optional[float] = None
    credit_available: Optional[float] = None
    credit_score: Optional[str] = None
    risk_rating: Optional[str] = None
    review_date: Optional[date] = None
    review_by: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class CreditProfilesOut(BaseModel):
    profile_id: uuid.UUID
    customer_id: uuid.UUID
    credit_limit: Optional[float] = None
    credit_used: Optional[float] = None
    credit_available: Optional[float] = None
    credit_score: Optional[str] = None
    risk_rating: Optional[str] = None
    review_date: Optional[date] = None
    review_by: Optional[uuid.UUID] = None
    notes: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class CustSiteUsesCreate(BaseModel):
    site_use_id: uuid.UUID
    cust_acct_site_id: uuid.UUID
    site_use_code: str
    site_use_name: Optional[str] = None
    is_active: bool = True

class CustSiteUsesUpdate(BaseModel):
    site_use_id: Optional[uuid.UUID] = None
    cust_acct_site_id: Optional[uuid.UUID] = None
    site_use_code: Optional[str] = None
    site_use_name: Optional[str] = None
    is_active: Optional[bool] = None

class CustSiteUsesOut(BaseModel):
    site_use_id: uuid.UUID
    cust_acct_site_id: uuid.UUID
    site_use_code: str
    site_use_name: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class CustomerDepositsCreate(BaseModel):
    deposit_id: uuid.UUID
    deposit_number: str
    customer_id: uuid.UUID
    deposit_date: date
    amount: float
    remaining_amount: float
    currency_code: Optional[str] = None
    receipt_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class CustomerDepositsUpdate(BaseModel):
    deposit_id: Optional[uuid.UUID] = None
    deposit_number: Optional[str] = None
    customer_id: Optional[uuid.UUID] = None
    deposit_date: Optional[date] = None
    amount: Optional[float] = None
    remaining_amount: Optional[float] = None
    currency_code: Optional[str] = None
    receipt_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class CustomerDepositsOut(BaseModel):
    deposit_id: uuid.UUID
    deposit_number: str
    customer_id: uuid.UUID
    deposit_date: date
    amount: float
    remaining_amount: float
    currency_code: Optional[str] = None
    receipt_id: Optional[uuid.UUID] = None
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

class DepositApplicationsCreate(BaseModel):
    application_id: uuid.UUID
    deposit_id: uuid.UUID
    invoice_id: uuid.UUID
    applied_date: date
    applied_amount: float
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DepositApplicationsUpdate(BaseModel):
    application_id: Optional[uuid.UUID] = None
    deposit_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    applied_date: Optional[date] = None
    applied_amount: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DepositApplicationsOut(BaseModel):
    application_id: uuid.UUID
    deposit_id: uuid.UUID
    invoice_id: uuid.UUID
    applied_date: date
    applied_amount: float
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class DunningHistoryCreate(BaseModel):
    dunning_id: uuid.UUID
    customer_id: uuid.UUID
    invoice_id: Optional[uuid.UUID] = None
    plan_id: Optional[uuid.UUID] = None
    level_num: int
    letter_date: Optional[date] = None
    status: Optional[str] = None
    response: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DunningHistoryUpdate(BaseModel):
    dunning_id: Optional[uuid.UUID] = None
    customer_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    plan_id: Optional[uuid.UUID] = None
    level_num: Optional[int] = None
    letter_date: Optional[date] = None
    status: Optional[str] = None
    response: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class DunningHistoryOut(BaseModel):
    dunning_id: uuid.UUID
    customer_id: uuid.UUID
    invoice_id: Optional[uuid.UUID] = None
    plan_id: Optional[uuid.UUID] = None
    level_num: int
    letter_date: Optional[date] = None
    status: Optional[str] = None
    response: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class DunningPlansCreate(BaseModel):
    plan_id: uuid.UUID
    plan_code: str
    plan_name: str
    description: Optional[str] = None
    levels: Optional[int] = None
    days_between: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1

class DunningPlansUpdate(BaseModel):
    plan_id: Optional[uuid.UUID] = None
    plan_code: Optional[str] = None
    plan_name: Optional[str] = None
    description: Optional[str] = None
    levels: Optional[int] = None
    days_between: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class DunningPlansOut(BaseModel):
    plan_id: uuid.UUID
    plan_code: str
    plan_name: str
    description: Optional[str] = None
    levels: Optional[int] = None
    days_between: Optional[int] = None
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

class PaymentSchedulesCreate(BaseModel):
    schedule_id: uuid.UUID
    invoice_id: uuid.UUID
    installment_num: Optional[int] = None
    due_date: date
    amount_due: float
    amount_remaining: float
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PaymentSchedulesUpdate(BaseModel):
    schedule_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    installment_num: Optional[int] = None
    due_date: Optional[date] = None
    amount_due: Optional[float] = None
    amount_remaining: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class PaymentSchedulesOut(BaseModel):
    schedule_id: uuid.UUID
    invoice_id: uuid.UUID
    installment_num: Optional[int] = None
    due_date: date
    amount_due: float
    amount_remaining: float
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

class ReceiptApplicationsCreate(BaseModel):
    application_id: uuid.UUID
    receipt_id: uuid.UUID
    invoice_id: uuid.UUID
    applied_date: date
    applied_amount: float
    discount_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ReceiptApplicationsUpdate(BaseModel):
    application_id: Optional[uuid.UUID] = None
    receipt_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    applied_date: Optional[date] = None
    applied_amount: Optional[float] = None
    discount_amount: Optional[float] = None
    currency_code: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ReceiptApplicationsOut(BaseModel):
    application_id: uuid.UUID
    receipt_id: uuid.UUID
    invoice_id: uuid.UUID
    applied_date: date
    applied_amount: float
    discount_amount: Optional[float] = None
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

class ReceiptBatchesCreate(BaseModel):
    batch_id: uuid.UUID
    batch_number: str
    batch_date: date
    total_amount: Optional[float] = None
    receipt_count: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ReceiptBatchesUpdate(BaseModel):
    batch_id: Optional[uuid.UUID] = None
    batch_number: Optional[str] = None
    batch_date: Optional[date] = None
    total_amount: Optional[float] = None
    receipt_count: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class ReceiptBatchesOut(BaseModel):
    batch_id: uuid.UUID
    batch_number: str
    batch_date: date
    total_amount: Optional[float] = None
    receipt_count: Optional[int] = None
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

class RevenueSchedulesCreate(BaseModel):
    schedule_id: uuid.UUID
    invoice_id: uuid.UUID
    invoice_line_id: Optional[uuid.UUID] = None
    recognize_date: date
    amount: float
    recognized: Optional[bool] = None
    recognized_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class RevenueSchedulesUpdate(BaseModel):
    schedule_id: Optional[uuid.UUID] = None
    invoice_id: Optional[uuid.UUID] = None
    invoice_line_id: Optional[uuid.UUID] = None
    recognize_date: Optional[date] = None
    amount: Optional[float] = None
    recognized: Optional[bool] = None
    recognized_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class RevenueSchedulesOut(BaseModel):
    schedule_id: uuid.UUID
    invoice_id: uuid.UUID
    invoice_line_id: Optional[uuid.UUID] = None
    recognize_date: date
    amount: float
    recognized: Optional[bool] = None
    recognized_at: Optional[datetime] = None
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
    is_active: bool = True
    object_version_number: int = 1

class TaxCodesUpdate(BaseModel):
    tax_code_id: Optional[uuid.UUID] = None
    tax_code: Optional[str] = None
    tax_name: Optional[str] = None
    tax_rate_pct: Optional[float] = None
    tax_type: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class TaxCodesOut(BaseModel):
    tax_code_id: uuid.UUID
    tax_code: str
    tax_name: str
    tax_rate_pct: float
    tax_type: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class TransactionTypesCreate(BaseModel):
    type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    sign: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class TransactionTypesUpdate(BaseModel):
    type_id: Optional[uuid.UUID] = None
    type_code: Optional[str] = None
    type_name: Optional[str] = None
    description: Optional[str] = None
    sign: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class TransactionTypesOut(BaseModel):
    type_id: uuid.UUID
    type_code: str
    type_name: str
    description: Optional[str] = None
    sign: Optional[str] = None
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
