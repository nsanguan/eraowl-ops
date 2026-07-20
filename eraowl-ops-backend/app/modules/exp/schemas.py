import uuid
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class ClaimHeaderCreate(BaseModel):
    bu_id: Optional[uuid.UUID] = None
    employee_id: Optional[uuid.UUID] = None
    claim_number: str
    purpose: str
    total_amount: float = 0.0
    status: str = "DRAFT"
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class ClaimHeaderUpdate(BaseModel):
    bu_id: Optional[uuid.UUID] = None
    employee_id: Optional[uuid.UUID] = None
    claim_number: Optional[str] = None
    purpose: Optional[str] = None
    total_amount: Optional[float] = None
    status: Optional[str] = None
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class ClaimHeaderOut(BaseModel):
    claim_id: uuid.UUID
    bu_id: Optional[uuid.UUID] = None
    employee_id: Optional[uuid.UUID] = None
    claim_number: str
    purpose: str
    total_amount: float
    status: str
    approved_by: Optional[uuid.UUID] = None
    approved_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

    model_config = {"from_attributes": True}


class ClaimLineCreate(BaseModel):
    claim_id: uuid.UUID
    category_id: uuid.UUID
    expense_date: date
    amount: float
    tax_rate_id: Optional[uuid.UUID] = None
    tax_amount: float = 0.0
    receipt_url: Optional[str] = None
    description: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class ClaimLineUpdate(BaseModel):
    claim_id: Optional[uuid.UUID] = None
    category_id: Optional[uuid.UUID] = None
    expense_date: Optional[date] = None
    amount: Optional[float] = None
    tax_rate_id: Optional[uuid.UUID] = None
    tax_amount: Optional[float] = None
    receipt_url: Optional[str] = None
    description: Optional[str] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None


class ClaimLineOut(BaseModel):
    claim_line_id: uuid.UUID
    claim_id: uuid.UUID
    category_id: uuid.UUID
    expense_date: date
    amount: float
    tax_rate_id: Optional[uuid.UUID] = None
    tax_amount: float
    receipt_url: Optional[str] = None
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    update_by: Optional[uuid.UUID] = None
    corporate_id: Optional[uuid.UUID] = None
    company_id: Optional[uuid.UUID] = None
    site_id: Optional[uuid.UUID] = None

    model_config = {"from_attributes": True}


class ExpCategoryCreate(BaseModel):
    company_id: Optional[uuid.UUID] = None
    category_code: str
    category_name: str
    gl_account_id: Optional[uuid.UUID] = None
    is_active: bool = True


class ExpCategoryUpdate(BaseModel):
    company_id: Optional[uuid.UUID] = None
    category_code: Optional[str] = None
    category_name: Optional[str] = None
    gl_account_id: Optional[uuid.UUID] = None
    is_active: Optional[bool] = None


class ExpCategoryOut(BaseModel):
    category_id: uuid.UUID
    company_id: Optional[uuid.UUID] = None
    category_code: str
    category_name: str
    gl_account_id: Optional[uuid.UUID] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime
    update_by: Optional[uuid.UUID] = None

    model_config = {"from_attributes": True}
