import uuid
from datetime import date, datetime
from typing import Optional
from sqlalchemy import Boolean, Column, Date, DateTime, Numeric, String, Text, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlmodel import Field, SQLModel


class ClaimHeader(SQLModel, table=True):
    __tablename__ = "claim_headers"
    __table_args__ = {"schema": "exp"}

    claim_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    bu_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.business_units.business_unit_id", nullable=True)
    employee_id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    claim_number: str = Field(sa_column=Column(String(50), nullable=False, index=True))
    purpose: str = Field(sa_column=Column(String(255), nullable=False))
    total_amount: float = Field(default=0.0, sa_column=Column(Numeric(15, 2), default=0.0))
    status: str = Field(default="DRAFT", sa_column=Column(String(30), default="DRAFT", index=True))
    approved_by: Optional[uuid.UUID] = Field(default=None, nullable=True)
    approved_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))
    corporate_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.corporates.corporate_id", nullable=True)
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.companies.company_id", nullable=True)
    site_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.sites.site_id", nullable=True)


class ClaimLine(SQLModel, table=True):
    __tablename__ = "claim_lines"
    __table_args__ = {"schema": "exp"}

    claim_line_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    claim_id: uuid.UUID = Field(foreign_key="exp.claim_headers.claim_id", nullable=False)
    category_id: uuid.UUID = Field(foreign_key="exp.exp_categories.category_id", nullable=False)
    expense_date: date = Field(sa_column=Column(Date, nullable=False))
    amount: float = Field(sa_column=Column(Numeric(15, 2), nullable=False))
    tax_rate_id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    tax_amount: float = Field(default=0.0, sa_column=Column(Numeric(15, 2), default=0.0))
    receipt_url: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))
    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))
    corporate_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.corporates.corporate_id", nullable=True)
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.companies.company_id", nullable=True)
    site_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.sites.site_id", nullable=True)


class ExpCategory(SQLModel, table=True):
    __tablename__ = "exp_categories"
    __table_args__ = {"schema": "exp"}

    category_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.companies.company_id", nullable=True)
    category_code: str = Field(sa_column=Column(String(50), nullable=False, index=True))
    category_name: str = Field(sa_column=Column(String(100), nullable=False))
    gl_account_id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))
