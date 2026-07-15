import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel


class Address(SQLModel, table=True):
    __tablename__ = "addresses"
    __table_args__ = {"schema": "mdm"}

    address_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    address_line1: str = Field(max_length=255)
    address_line2: Optional[str] = Field(default=None, max_length=255)
    city: str = Field(max_length=100)
    state_province: str = Field(max_length=100)
    postal_code: str = Field(max_length=20)
    country_code: str = Field(max_length=5)
    latitude: Optional[float] = Field(default=None, sa_column=Column(Float, nullable=True))
    longitude: Optional[float] = Field(default=None, sa_column=Column(Float, nullable=True))
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
    party_type: str = Field(max_length=20)
    party_name: str = Field(max_length=255)
    tax_id: Optional[str] = Field(default=None, max_length=50)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    party_sites: list["PartySite"] = Relationship(back_populates="mdm")
    party_roles: list["PartyRole"] = Relationship(back_populates="mdm")
    supplier: Optional["Supplier"] = Relationship(back_populates="mdm")
    customer: Optional["Customer"] = Relationship(back_populates="mdm")


class PartySite(SQLModel, table=True):
    __tablename__ = "party_sites"
    __table_args__ = {"schema": "mdm"}

    party_site_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    party_id: uuid.UUID = Field(foreign_key="mdm.parties.party_id")
    address_id: uuid.UUID = Field(foreign_key="mdm.addresses.address_id")
    site_name: Optional[str] = Field(default=None, max_length=255)
    is_primary: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
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

    party_site_use_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    party_site_id: uuid.UUID = Field(foreign_key="mdm.party_sites.party_site_id")
    use_type: str = Field(max_length=20)
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
    party_id: uuid.UUID = Field(foreign_key="mdm.parties.party_id")
    role_type: str = Field(max_length=20)
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
    supplier_code: str = Field(max_length=50, unique=True, index=True)
    payment_term_days: int = Field(default=30, sa_column=Column(Integer, default=30, nullable=False))
    currency: str = Field(max_length=10)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    party: Party = Relationship(back_populates="supplier")


class Customer(SQLModel, table=True):
    __tablename__ = "customers"
    __table_args__ = {"schema": "mdm"}

    customer_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    party_id: uuid.UUID = Field(foreign_key="mdm.parties.party_id", unique=True)
    customer_code: str = Field(max_length=50, unique=True, index=True)
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
