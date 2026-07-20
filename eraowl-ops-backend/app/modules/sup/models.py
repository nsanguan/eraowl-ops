import uuid
from datetime import date, datetime
from typing import Optional
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, Numeric, String, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlmodel import Field, SQLModel


class PortalUser(SQLModel, table=True):
    __tablename__ = "portal_users"
    __table_args__ = {"schema": "sup"}

    portal_user_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    partner_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.parties.party_id", nullable=True)
    email: str = Field(sa_column=Column(String(100), nullable=False, index=True))
    password_hash: str = Field(sa_column=Column(String(255), nullable=False))
    full_name: str = Field(sa_column=Column(String(100), nullable=False))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    last_login_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))


class RfqResponse(SQLModel, table=True):
    __tablename__ = "rfq_responses"
    __table_args__ = {"schema": "sup"}

    response_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    partner_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.parties.party_id", nullable=True)
    item_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.items.item_id", nullable=True)
    quoted_price: float = Field(sa_column=Column(Numeric(18, 4), nullable=False))
    lead_time_days: int = Field(sa_column=Column(Integer, nullable=False))
    valid_until: date = Field(sa_column=Column(Date, nullable=False))
    status: str = Field(default="SUBMITTED", sa_column=Column(String(20), default="SUBMITTED", index=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))
    corporate_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.corporates.corporate_id", nullable=True)
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.companies.company_id", nullable=True)
    site_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.sites.site_id", nullable=True)


class ShipmentAdvice(SQLModel, table=True):
    __tablename__ = "shipment_advices"
    __table_args__ = {"schema": "sup"}

    asn_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    partner_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.parties.party_id", nullable=True)
    po_id: Optional[uuid.UUID] = Field(default=None, foreign_key="po.po_headers.po_id", nullable=True)
    asn_number: str = Field(sa_column=Column(String(50), nullable=False, index=True))
    ship_date: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False))
    expected_arrival: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False))
    status: str = Field(default="SHIPPED", sa_column=Column(String(20), default="SHIPPED", index=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))
    corporate_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.corporates.corporate_id", nullable=True)
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.companies.company_id", nullable=True)
    site_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.sites.site_id", nullable=True)
