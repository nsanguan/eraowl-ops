import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional
from sqlalchemy import Boolean, Column, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import Field, Relationship, SQLModel


class OrgCorporate(SQLModel, table=True):
    __tablename__ = "corporates"
    __table_args__ = {"schema": "mdm"}

    corporate_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    corp_name: str = Field(max_length=255)
    corp_code: str = Field(max_length=50, unique=True, index=True)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    companies: list["OrgCompany"] = Relationship(back_populates="corporate")


class OrgCompany(SQLModel, table=True):
    __tablename__ = "companies"
    __table_args__ = {"schema": "mdm"}

    company_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    corporate_id: uuid.UUID = Field(foreign_key="mdm.corporates.corporate_id")
    legal_name: str = Field(max_length=255)
    tax_id: str = Field(max_length=50)
    company_code: str = Field(max_length=50, unique=True, index=True)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    corporate: OrgCorporate = Relationship(back_populates="companies")
    business_units: list["OrgBusinessUnit"] = Relationship(back_populates="company")


class OrgBusinessUnit(SQLModel, table=True):
    __tablename__ = "business_units"
    __table_args__ = {"schema": "mdm"}

    business_unit_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    company_id: uuid.UUID = Field(foreign_key="mdm.companies.company_id")
    bu_name: str = Field(max_length=255)
    bu_code: str = Field(max_length=50, unique=True, index=True)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    company: OrgCompany = Relationship(back_populates="business_units")
    sites: list["OrgSite"] = Relationship(back_populates="business_unit")


class OrgSite(SQLModel, table=True):
    __tablename__ = "sites"
    __table_args__ = {"schema": "mdm"}

    site_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    business_unit_id: uuid.UUID = Field(foreign_key="mdm.business_units.business_unit_id")
    site_name: str = Field(max_length=255)
    site_code: str = Field(max_length=50)
    address_id: uuid.UUID | None = Field(default=None, foreign_key="mdm.addresses.address_id")
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    business_unit: OrgBusinessUnit = Relationship(back_populates="sites")
    warehouses: list["OrgWarehouse"] = Relationship(back_populates="site")


class OrgWarehouse(SQLModel, table=True):
    __tablename__ = "warehouses"
    __table_args__ = {"schema": "mdm"}

    warehouse_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    site_id: uuid.UUID = Field(foreign_key="mdm.sites.site_id")
    warehouse_name: str = Field(max_length=255)
    warehouse_code: str = Field(max_length=50)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    site: OrgSite = Relationship(back_populates="warehouses")
    locators: list["OrgWarehouseLocator"] = Relationship(back_populates="warehouse")


class OrgWarehouseLocator(SQLModel, table=True):
    __tablename__ = "warehouse_locators"
    __table_args__ = {"schema": "mdm"}

    warehouse_locator_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    warehouse_id: uuid.UUID = Field(foreign_key="mdm.warehouses.warehouse_id")
    zone: str = Field(max_length=50)
    aisle: str = Field(max_length=50)
    rack: str = Field(max_length=50)
    bin: str = Field(max_length=50)
    locator_code: str = Field(max_length=100)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    warehouse: OrgWarehouse = Relationship(back_populates="locators")
