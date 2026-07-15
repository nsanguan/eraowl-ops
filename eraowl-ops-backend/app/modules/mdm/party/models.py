import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel


class Address(SQLModel, table=True):
    __tablename__ = "addresses"
    __table_args__ = {"schema": "mdm"}

    address_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    country: str = Field(max_length=100)
    address_line1: str = Field(max_length=255)
    address_line2: Optional[str] = Field(default=None, max_length=255)
    city: str = Field(max_length=100)
    state: Optional[str] = Field(default=None, max_length=100)
    postal_code: Optional[str] = Field(default=None, max_length=20)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    party_sites: list["PartySite"] = Relationship(back_populates="address")


class Party(SQLModel, table=True):
    __tablename__ = "parties"
    __table_args__ = {"schema": "mdm"}

    party_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    party_number: str = Field(max_length=50, unique=True, index=True)
    party_code: Optional[str] = Field(default=None, max_length=50)
    party_name: str = Field(max_length=255)
    party_type: str = Field(default="ORGANIZATION", sa_column=Column(String(20), default="ORGANIZATION", nullable=False))
    tax_reference: Optional[str] = Field(default=None, max_length=50)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    party_sites: list["PartySite"] = Relationship(back_populates="party")
    party_roles: list["PartyRole"] = Relationship(back_populates="party")
    supplier: Optional["Supplier"] = Relationship(back_populates="party")
    customer: Optional["Customer"] = Relationship(back_populates="party")


class PartySite(SQLModel, table=True):
    __tablename__ = "party_sites"
    __table_args__ = {"schema": "mdm"}

    party_site_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    party_id: uuid.UUID = Field(foreign_key="mdm.parties.party_id", nullable=False)
    address_id: uuid.UUID = Field(foreign_key="mdm.addresses.address_id", nullable=False)
    party_site_number: str = Field(max_length=50, unique=True, index=True)
    site_name: Optional[str] = Field(default=None, max_length=255)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    party: Party = Relationship(back_populates="party_sites")
    address: Address = Relationship(back_populates="party_sites")
    party_site_uses: list["PartySiteUse"] = Relationship(back_populates="party_site")


class PartySiteUse(SQLModel, table=True):
    __tablename__ = "party_site_uses"
    __table_args__ = {"schema": "mdm"}

    site_use_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    party_site_id: uuid.UUID = Field(foreign_key="mdm.party_sites.party_site_id", nullable=False)
    site_use_type: str = Field(max_length=20)
    is_primary: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    party_site: PartySite = Relationship(back_populates="party_site_uses")


class PartyRole(SQLModel, table=True):
    __tablename__ = "party_roles"
    __table_args__ = (
        UniqueConstraint("party_id", "role_type", name="uq_party_roles_party_role"),
        {"schema": "mdm"},
    )

    party_role_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    party_id: uuid.UUID = Field(foreign_key="mdm.parties.party_id", nullable=False)
    role_type: str = Field(max_length=30)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    party: Party = Relationship(back_populates="party_roles")


class Supplier(SQLModel, table=True):
    __tablename__ = "suppliers"
    __table_args__ = {"schema": "mdm"}

    supplier_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    party_id: uuid.UUID = Field(foreign_key="mdm.parties.party_id", unique=True)
    party_role_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.party_roles.party_role_id", nullable=True)
    supplier_code: Optional[str] = Field(default=None, max_length=50)
    currency_code: Optional[str] = Field(default=None, max_length=10)
    vendor_type_lookup_code: Optional[str] = Field(default=None, max_length=30)
    payment_method_code: Optional[str] = Field(default=None, max_length=30)
    payment_term_days: int = Field(default=30, sa_column=Column(Integer, default=30, nullable=False))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    party: Party = Relationship(back_populates="supplier")
    supplier_sites: list["SupplierSite"] = Relationship(back_populates="supplier")


class SupplierSite(SQLModel, table=True):
    __tablename__ = "supplier_sites"
    __table_args__ = {"schema": "mdm"}

    supplier_site_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    supplier_id: uuid.UUID = Field(foreign_key="mdm.suppliers.supplier_id", nullable=False)
    address_id: uuid.UUID = Field(foreign_key="mdm.addresses.address_id", nullable=False)
    site_name: Optional[str] = Field(default=None, max_length=255)
    site_number: Optional[str] = Field(default=None, max_length=50)
    is_primary: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    supplier: Supplier = Relationship(back_populates="supplier_sites")
    address: Address = Relationship()


class Customer(SQLModel, table=True):
    __tablename__ = "customers"
    __table_args__ = {"schema": "mdm"}

    customer_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    party_id: uuid.UUID = Field(foreign_key="mdm.parties.party_id", unique=True)
    party_role_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.party_roles.party_role_id", nullable=True)
    customer_code: Optional[str] = Field(default=None, max_length=50)
    customer_class_code: Optional[str] = Field(default=None, max_length=30)
    credit_limit: Optional[float] = Field(default=None, sa_column=Column(Float, nullable=True))
    payment_term_days: int = Field(default=30, sa_column=Column(Integer, default=30, nullable=False))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    party: Party = Relationship(back_populates="customer")
    customer_sites: list["CustomerSite"] = Relationship(back_populates="customer")


class CustomerSite(SQLModel, table=True):
    __tablename__ = "customer_sites"
    __table_args__ = {"schema": "mdm"}

    customer_site_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    customer_id: uuid.UUID = Field(foreign_key="mdm.customers.customer_id", nullable=False)
    address_id: uuid.UUID = Field(foreign_key="mdm.addresses.address_id", nullable=False)
    site_name: Optional[str] = Field(default=None, max_length=255)
    site_number: Optional[str] = Field(default=None, max_length=50)
    is_primary: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    customer: Customer = Relationship(back_populates="customer_sites")
    address: Address = Relationship()
