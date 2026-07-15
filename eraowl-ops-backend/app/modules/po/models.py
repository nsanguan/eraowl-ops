import uuid
from datetime import date, datetime
from typing import Optional
from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, String, Text, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, JSONB
from sqlmodel import Field, Relationship, SQLModel


class PoHeader(SQLModel, table=True):
    __tablename__ = "po_headers"
    __table_args__ = {"schema": "po"}

    po_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    po_number: str = Field(sa_column=Column(String(50), unique=True, nullable=False, index=True))
    status: str = Field(default="DRAFT", sa_column=Column(String(20), nullable=False, default="DRAFT", index=True))
    order_date: date = Field(sa_column=Column(Date, nullable=False))
    supplier_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.suppliers.supplier_id", nullable=True)
    supplier_site_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.party_sites.party_site_id", nullable=True)
    currency_code: str = Field(default="THB", sa_column=Column(String(10), default="THB"))
    exchange_rate: float = Field(default=1.0, sa_column=Column(Float, default=1.0))
    payment_term_days: int = Field(default=30, sa_column=Column(Integer, default=30))
    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))
    total_amount: float = Field(default=0.0, sa_column=Column(Float, default=0.0))
    business_unit_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.business_units.business_unit_id", nullable=True)
    buyer_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    lines: list["PoLine"] = Relationship(back_populates="header")
    shipments: list["PoShipment"] = Relationship(back_populates="header")
    distributions: list["PoDistribution"] = Relationship(back_populates="header")
    releases: list["PoRelease"] = Relationship(back_populates="header")
    amendments: list["PoAmendment"] = Relationship(back_populates="header")
    approvals: list["PoApproval"] = Relationship(back_populates="header")


class PoLine(SQLModel, table=True):
    __tablename__ = "po_lines"
    __table_args__ = (
        UniqueConstraint("po_id", "line_num", name="uq_po_lines_line"),
        {"schema": "po"},
    )

    po_line_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    po_id: uuid.UUID = Field(foreign_key="po.po_headers.po_id", nullable=False)
    line_num: int = Field(sa_column=Column(Integer, nullable=False))
    item_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.items.item_id", nullable=True)
    item_description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))
    uom_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.uoms.uom_id", nullable=True)
    qty_ordered: float = Field(default=0, sa_column=Column(Float, default=0))
    qty_received: float = Field(default=0, sa_column=Column(Float, default=0))
    qty_invoiced: float = Field(default=0, sa_column=Column(Float, default=0))
    unit_price: float = Field(default=0, sa_column=Column(Float, nullable=False, default=0))
    line_amount: float = Field(default=0, sa_column=Column(Float, default=0))
    tax_amount: float = Field(default=0, sa_column=Column(Float, default=0))
    charge_amount: float = Field(default=0, sa_column=Column(Float, default=0))
    need_by_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))
    promise_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))
    line_type: str = Field(default="GOODS", sa_column=Column(String(30), default="GOODS"))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    header: "PoHeader" = Relationship(back_populates="lines")
    shipments: list["PoShipment"] = Relationship(back_populates="line")
    distributions: list["PoDistribution"] = Relationship(back_populates="line")


class PoShipment(SQLModel, table=True):
    __tablename__ = "po_shipments"
    __table_args__ = {"schema": "po"}

    po_shipment_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    po_id: uuid.UUID = Field(foreign_key="po.po_headers.po_id", nullable=False)
    po_line_id: uuid.UUID = Field(foreign_key="po.po_lines.po_line_id", nullable=False)
    shipment_num: int = Field(sa_column=Column(Integer, nullable=False))
    qty_ordered: float = Field(default=0, sa_column=Column(Float, default=0))
    qty_received: float = Field(default=0, sa_column=Column(Float, default=0))
    qty_accepted: float = Field(default=0, sa_column=Column(Float, default=0))
    qty_rejected: float = Field(default=0, sa_column=Column(Float, default=0))
    expected_receipt_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))
    actual_receipt_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))
    warehouse_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.warehouses.warehouse_id", nullable=True)
    locator_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.warehouse_locators.warehouse_locator_id", nullable=True)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    header: "PoHeader" = Relationship(back_populates="shipments")
    line: "PoLine" = Relationship(back_populates="shipments")
    distributions: list["PoDistribution"] = Relationship(back_populates="shipment")


class PoDistribution(SQLModel, table=True):
    __tablename__ = "po_distributions"
    __table_args__ = {"schema": "po"}

    distribution_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    po_id: uuid.UUID = Field(foreign_key="po.po_headers.po_id", nullable=False)
    po_line_id: uuid.UUID = Field(foreign_key="po.po_lines.po_line_id", nullable=False)
    po_shipment_id: Optional[uuid.UUID] = Field(default=None, foreign_key="po.po_shipments.po_shipment_id", nullable=True)
    distribution_num: int = Field(sa_column=Column(Integer, nullable=False))
    account_code: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))
    amount: float = Field(default=0, sa_column=Column(Float, default=0))
    percent: float = Field(default=100, sa_column=Column(Float, default=100))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))

    header: "PoHeader" = Relationship(back_populates="distributions")
    line: "PoLine" = Relationship(back_populates="distributions")
    shipment: Optional["PoShipment"] = Relationship(back_populates="distributions")


class PoRelease(SQLModel, table=True):
    __tablename__ = "po_releases"
    __table_args__ = {"schema": "po"}

    release_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    po_id: uuid.UUID = Field(foreign_key="po.po_headers.po_id", nullable=False)
    release_num: int = Field(sa_column=Column(Integer, nullable=False))
    release_amount: float = Field(default=0, sa_column=Column(Float, default=0))
    release_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))
    expected_delivery_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))
    status: str = Field(default="OPEN", sa_column=Column(String(20), default="OPEN"))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    header: "PoHeader" = Relationship(back_populates="releases")


class PoAmendment(SQLModel, table=True):
    __tablename__ = "po_amendments"
    __table_args__ = {"schema": "po"}

    amendment_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    po_id: uuid.UUID = Field(foreign_key="po.po_headers.po_id", nullable=False)
    amendment_num: int = Field(sa_column=Column(Integer, nullable=False))
    change_type: str = Field(sa_column=Column(String(50), nullable=False))
    change_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))
    reason: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))
    approved_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))
    approved_date: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    header: "PoHeader" = Relationship(back_populates="amendments")


class PoApproval(SQLModel, table=True):
    __tablename__ = "po_approvals"
    __table_args__ = {"schema": "po"}

    approval_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    po_id: uuid.UUID = Field(foreign_key="po.po_headers.po_id", nullable=False)
    approval_level: int = Field(sa_column=Column(Integer, nullable=False))
    approver_id: Optional[uuid.UUID] = Field(default=None, foreign_key="admin.users.user_id", nullable=True)
    approver_name: Optional[str] = Field(default=None, sa_column=Column(String(255), nullable=True))
    status: str = Field(default="PENDING", sa_column=Column(String(20), nullable=False, default="PENDING"))
    comments: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))
    approved_date: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    header: "PoHeader" = Relationship(back_populates="approvals")
