import uuid
from datetime import date, datetime, time
from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class AccountCombinationsCreate(BaseModel):
    combination_id: uuid.UUID
    segment1: Optional[str] = None
    segment2: Optional[str] = None
    segment3: Optional[str] = None
    segment4: Optional[str] = None
    segment5: Optional[str] = None
    concatenated: Optional[str] = None
    description: Optional[str] = None
    account_type: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class AccountCombinationsUpdate(BaseModel):
    combination_id: Optional[uuid.UUID] = None
    segment1: Optional[str] = None
    segment2: Optional[str] = None
    segment3: Optional[str] = None
    segment4: Optional[str] = None
    segment5: Optional[str] = None
    concatenated: Optional[str] = None
    description: Optional[str] = None
    account_type: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class AccountCombinationsOut(BaseModel):
    combination_id: uuid.UUID
    segment1: Optional[str] = None
    segment2: Optional[str] = None
    segment3: Optional[str] = None
    segment4: Optional[str] = None
    segment5: Optional[str] = None
    concatenated: Optional[str] = None
    description: Optional[str] = None
    account_type: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class AccountingBooksCreate(BaseModel):
    book_id: uuid.UUID
    company_id: Optional[uuid.UUID] = None
    book_code: str
    currency_code: Optional[str] = None

class AccountingBooksUpdate(BaseModel):
    book_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    book_code: Optional[str] = None
    currency_code: Optional[str] = None

class AccountingBooksOut(BaseModel):
    book_id: uuid.UUID
    company_id: Optional[uuid.UUID] = None
    book_code: str
    currency_code: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
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

class AiWorkflowCheckpointsCreate(BaseModel):
    thread_id: str
    checkpoint_ns: str
    checkpoint_id: str
    parent_checkpoint_id: Optional[str] = None
    checkpoint: dict
    meta_data: dict

class AiWorkflowCheckpointsUpdate(BaseModel):
    thread_id: Optional[str] = None
    checkpoint_ns: Optional[str] = None
    checkpoint_id: Optional[str] = None
    parent_checkpoint_id: Optional[str] = None
    checkpoint: Optional[dict] = None
    meta_data: Optional[dict] = None

class AiWorkflowCheckpointsOut(BaseModel):
    thread_id: str
    checkpoint_ns: str
    checkpoint_id: str
    parent_checkpoint_id: Optional[str] = None
    checkpoint: dict
    meta_data: dict
    created_at: Optional[datetime] = None
    model_config = {"from_attributes": True}

class AiWorkflowStateCreate(BaseModel):
    state_id: uuid.UUID
    doc_type: str
    doc_id: uuid.UUID
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

class BalancesCreate(BaseModel):
    balance_id: uuid.UUID
    ledger_id: uuid.UUID
    period_id: uuid.UUID
    combination_id: uuid.UUID
    currency_code: Optional[str] = None
    begin_balance: Optional[float] = None
    period_dr: Optional[float] = None
    period_cr: Optional[float] = None
    end_balance: Optional[float] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class BalancesUpdate(BaseModel):
    balance_id: Optional[uuid.UUID] = None
    ledger_id: Optional[uuid.UUID] = None
    period_id: Optional[uuid.UUID] = None
    combination_id: Optional[uuid.UUID] = None
    currency_code: Optional[str] = None
    begin_balance: Optional[float] = None
    period_dr: Optional[float] = None
    period_cr: Optional[float] = None
    end_balance: Optional[float] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class BalancesOut(BaseModel):
    balance_id: uuid.UUID
    ledger_id: uuid.UUID
    period_id: uuid.UUID
    combination_id: uuid.UUID
    currency_code: Optional[str] = None
    begin_balance: Optional[float] = None
    period_dr: Optional[float] = None
    period_cr: Optional[float] = None
    end_balance: Optional[float] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class BudgetBalancesCreate(BaseModel):
    budget_bal_id: uuid.UUID
    version_id: uuid.UUID
    period_id: uuid.UUID
    combination_id: uuid.UUID
    amount: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class BudgetBalancesUpdate(BaseModel):
    budget_bal_id: Optional[uuid.UUID] = None
    version_id: Optional[uuid.UUID] = None
    period_id: Optional[uuid.UUID] = None
    combination_id: Optional[uuid.UUID] = None
    amount: Optional[float] = None
    currency_code: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class BudgetBalancesOut(BaseModel):
    budget_bal_id: uuid.UUID
    version_id: uuid.UUID
    period_id: uuid.UUID
    combination_id: uuid.UUID
    amount: Optional[float] = None
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

class BudgetVersionsCreate(BaseModel):
    version_id: uuid.UUID
    version_code: str
    version_name: str
    budget_type: Optional[str] = None
    fiscal_year: Optional[int] = None
    is_active: bool = True
    object_version_number: int = 1

class BudgetVersionsUpdate(BaseModel):
    version_id: Optional[uuid.UUID] = None
    version_code: Optional[str] = None
    version_name: Optional[str] = None
    budget_type: Optional[str] = None
    fiscal_year: Optional[int] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class BudgetVersionsOut(BaseModel):
    version_id: uuid.UUID
    version_code: str
    version_name: str
    budget_type: Optional[str] = None
    fiscal_year: Optional[int] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class ChartOfAccountsCreate(BaseModel):
    account_id: uuid.UUID
    company_id: Optional[uuid.UUID] = None
    account_code: str
    account_name: str
    account_type: str

class ChartOfAccountsUpdate(BaseModel):
    account_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    account_code: Optional[str] = None
    account_name: Optional[str] = None
    account_type: Optional[str] = None

class ChartOfAccountsOut(BaseModel):
    account_id: uuid.UUID
    company_id: Optional[uuid.UUID] = None
    account_code: str
    account_name: str
    account_type: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class ExchangeRatesCreate(BaseModel):
    rate_id: uuid.UUID
    from_currency: str
    to_currency: str
    rate_type: Optional[str] = None
    rate_date: date
    rate: float
    source: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class ExchangeRatesUpdate(BaseModel):
    rate_id: Optional[uuid.UUID] = None
    from_currency: Optional[str] = None
    to_currency: Optional[str] = None
    rate_type: Optional[str] = None
    rate_date: Optional[date] = None
    rate: Optional[float] = None
    source: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class ExchangeRatesOut(BaseModel):
    rate_id: uuid.UUID
    from_currency: str
    to_currency: str
    rate_type: Optional[str] = None
    rate_date: date
    rate: float
    source: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class FiscalPeriodsCreate(BaseModel):
    period_id: uuid.UUID
    period_name: str
    fiscal_year: int
    period_num: int
    period_type: Optional[str] = None
    start_date: date
    end_date: date
    status: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class FiscalPeriodsUpdate(BaseModel):
    period_id: Optional[uuid.UUID] = None
    period_name: Optional[str] = None
    fiscal_year: Optional[int] = None
    period_num: Optional[int] = None
    period_type: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class FiscalPeriodsOut(BaseModel):
    period_id: uuid.UUID
    period_name: str
    fiscal_year: int
    period_num: int
    period_type: Optional[str] = None
    start_date: date
    end_date: date
    status: Optional[str] = None
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
    processed_at: Optional[datetime] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class JournalCategoriesCreate(BaseModel):
    category_id: uuid.UUID
    category_code: str
    category_name: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class JournalCategoriesUpdate(BaseModel):
    category_id: Optional[uuid.UUID] = None
    category_code: Optional[str] = None
    category_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class JournalCategoriesOut(BaseModel):
    category_id: uuid.UUID
    category_code: str
    category_name: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class JournalHeadersCreate(BaseModel):
    journal_id: uuid.UUID
    book_id: uuid.UUID
    accounting_date: date
    doc_sequence: str
    source_module: str
    ledger_id: Optional[uuid.UUID] = None
    source_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    status: Optional[str] = None
    posted_at: Optional[datetime] = None
    posted_by: Optional[uuid.UUID] = None
    reversal_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class JournalHeadersUpdate(BaseModel):
    journal_id: Optional[uuid.UUID] = None
    book_id: Optional[uuid.UUID] = None
    accounting_date: Optional[date] = None
    doc_sequence: Optional[str] = None
    source_module: Optional[str] = None
    ledger_id: Optional[uuid.UUID] = None
    source_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    status: Optional[str] = None
    posted_at: Optional[datetime] = None
    posted_by: Optional[uuid.UUID] = None
    reversal_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class JournalHeadersOut(BaseModel):
    journal_id: uuid.UUID
    book_id: uuid.UUID
    accounting_date: date
    doc_sequence: str
    source_module: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    ledger_id: Optional[uuid.UUID] = None
    source_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    status: Optional[str] = None
    posted_at: Optional[datetime] = None
    posted_by: Optional[uuid.UUID] = None
    reversal_id: Optional[uuid.UUID] = None
    is_active: bool
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class JournalLinesCreate(BaseModel):
    line_id: uuid.UUID
    journal_id: uuid.UUID
    account_id: uuid.UUID
    debit_amount: Optional[float] = None
    credit_amount: Optional[float] = None
    line_num: Optional[int] = None
    combination_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    currency_code: Optional[str] = None
    exchange_rate: Optional[float] = None
    reference: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class JournalLinesUpdate(BaseModel):
    line_id: Optional[uuid.UUID] = None
    journal_id: Optional[uuid.UUID] = None
    account_id: Optional[uuid.UUID] = None
    debit_amount: Optional[float] = None
    credit_amount: Optional[float] = None
    line_num: Optional[int] = None
    combination_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    currency_code: Optional[str] = None
    exchange_rate: Optional[float] = None
    reference: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

class JournalLinesOut(BaseModel):
    line_id: uuid.UUID
    journal_id: uuid.UUID
    account_id: uuid.UUID
    debit_amount: Optional[float] = None
    credit_amount: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    line_num: Optional[int] = None
    combination_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    currency_code: Optional[str] = None
    exchange_rate: Optional[float] = None
    reference: Optional[str] = None
    is_active: bool
    object_version_number: int
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None
    model_config = {"from_attributes": True}

class JournalSourcesCreate(BaseModel):
    source_id: uuid.UUID
    source_code: str
    source_name: str
    description: Optional[str] = None
    is_active: bool = True
    object_version_number: int = 1

class JournalSourcesUpdate(BaseModel):
    source_id: Optional[uuid.UUID] = None
    source_code: Optional[str] = None
    source_name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class JournalSourcesOut(BaseModel):
    source_id: uuid.UUID
    source_code: str
    source_name: str
    description: Optional[str] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class LedgersCreate(BaseModel):
    ledger_id: uuid.UUID
    ledger_code: str
    ledger_name: str
    ledger_type: Optional[str] = None
    currency_code: str
    coa_id: Optional[uuid.UUID] = None
    period_set_id: Optional[uuid.UUID] = None
    is_active: bool = True
    object_version_number: int = 1

class LedgersUpdate(BaseModel):
    ledger_id: Optional[uuid.UUID] = None
    ledger_code: Optional[str] = None
    ledger_name: Optional[str] = None
    ledger_type: Optional[str] = None
    currency_code: Optional[str] = None
    coa_id: Optional[uuid.UUID] = None
    period_set_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class LedgersOut(BaseModel):
    ledger_id: uuid.UUID
    ledger_code: str
    ledger_name: str
    ledger_type: Optional[str] = None
    currency_code: str
    coa_id: Optional[uuid.UUID] = None
    period_set_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    update_by: Optional[uuid.UUID] = None
    object_version_number: int
    model_config = {"from_attributes": True}

class PeriodStatusesCreate(BaseModel):
    period_stat_id: uuid.UUID
    ledger_id: uuid.UUID
    period_id: uuid.UUID
    status: Optional[str] = None
    opened_at: Optional[datetime] = None
    closed_by: Optional[uuid.UUID] = None
    closed_at: Optional[datetime] = None
    is_active: bool = True
    object_version_number: int = 1

class PeriodStatusesUpdate(BaseModel):
    period_stat_id: Optional[uuid.UUID] = None
    ledger_id: Optional[uuid.UUID] = None
    period_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    opened_at: Optional[datetime] = None
    closed_by: Optional[uuid.UUID] = None
    closed_at: Optional[datetime] = None
    is_active: Optional[bool] = None
    object_version_number: Optional[int] = None

class PeriodStatusesOut(BaseModel):
    period_stat_id: uuid.UUID
    ledger_id: uuid.UUID
    period_id: uuid.UUID
    status: Optional[str] = None
    opened_at: Optional[datetime] = None
    closed_by: Optional[uuid.UUID] = None
    closed_at: Optional[datetime] = None
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
