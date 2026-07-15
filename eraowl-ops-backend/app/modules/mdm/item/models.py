import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, DateTime, String, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlmodel import Field, Relationship, SQLModel


class Uom(SQLModel, table=True):
    __tablename__ = "uoms"
    __table_args__ = {"schema": "mdm"}

    uom_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    uom_code: str = Field(max_length=50, unique=True, index=True)
    uom_name: str = Field(max_length=255)
    uom_type: str = Field(max_length=20)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    from_conversions: list["UomConversion"] = Relationship(
        back_populates="from_uom",
        sa_relationship_kwargs={"foreign_keys": "UomConversion.from_uom_id"},
    )
    to_conversions: list["UomConversion"] = Relationship(
        back_populates="to_uom",
        sa_relationship_kwargs={"foreign_keys": "UomConversion.to_uom_id"},
    )
    primary_items: list["Item"] = Relationship(back_populates="primary_uom")


class UomConversion(SQLModel, table=True):
    __tablename__ = "uom_conversions"
    __table_args__ = {"schema": "mdm"}

    uom_conversion_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    from_uom_id: uuid.UUID = Field(foreign_key="mdm.uoms.uom_id")
    to_uom_id: uuid.UUID = Field(foreign_key="mdm.uoms.uom_id")
    item_id: uuid.UUID | None = Field(default=None, foreign_key="mdm.items.item_id")
    conversion_factor: float = Field(default=1.0)
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    from_uom: Uom = Relationship(
        back_populates="from_conversions",
        sa_relationship_kwargs={"foreign_keys": "[UomConversion.from_uom_id]"},
    )
    to_uom: Uom = Relationship(
        back_populates="to_conversions",
        sa_relationship_kwargs={"foreign_keys": "[UomConversion.to_uom_id]"},
    )
    item: Optional["Item"] = Relationship(back_populates="uom_conversions")


class ItemCategory(SQLModel, table=True):
    __tablename__ = "item_categories"
    __table_args__ = {"schema": "mdm"}

    item_category_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    category_set: str = Field(max_length=20)
    category_code: str = Field(max_length=50)
    category_name: str = Field(max_length=255)
    parent_category_id: uuid.UUID | None = Field(default=None, foreign_key="mdm.item_categories.item_category_id")
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    parent: Optional["ItemCategory"] = Relationship(
        back_populates="children",
        sa_relationship_kwargs={"remote_side": "ItemCategory.item_category_id"},
    )
    children: list["ItemCategory"] = Relationship(back_populates="parent")
    category_assignments: list["ItemCategoryAssignment"] = Relationship(back_populates="category")


class Item(SQLModel, table=True):
    __tablename__ = "items"
    __table_args__ = {"schema": "mdm"}

    item_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    item_code: str = Field(max_length=50, unique=True, index=True)
    item_name: str = Field(max_length=255)
    item_type: str = Field(max_length=20)
    primary_uom_id: uuid.UUID = Field(foreign_key="mdm.uoms.uom_id")
    status: str = Field(max_length=20)
    description: str | None = Field(default=None, sa_column=Column(Text, nullable=True))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    primary_uom: Uom = Relationship(back_populates="primary_items")
    category_assignments: list["ItemCategoryAssignment"] = Relationship(back_populates="item")
    uom_conversions: list["UomConversion"] = Relationship(back_populates="item")
    organizations: list["ItemOrganization"] = Relationship(back_populates="item")
    supplier_xrefs: list["ItemSupplierXref"] = Relationship(back_populates="item")


class ItemCategoryAssignment(SQLModel, table=True):
    __tablename__ = "item_category_assignments"
    __table_args__ = (
        UniqueConstraint("item_id", "item_category_id", name="uq_item_category_assignment"),
        {"schema": "mdm"},
    )

    item_category_assignment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    item_id: uuid.UUID = Field(foreign_key="mdm.items.item_id")
    item_category_id: uuid.UUID = Field(foreign_key="mdm.item_categories.item_category_id")
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    item: Item = Relationship(back_populates="category_assignments")
    category: ItemCategory = Relationship(back_populates="category_assignments")


class ItemOrganization(SQLModel, table=True):
    __tablename__ = "item_organizations"
    __table_args__ = {"schema": "mdm"}

    item_organization_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    item_id: uuid.UUID = Field(foreign_key="mdm.items.item_id")
    warehouse_id: uuid.UUID = Field(foreign_key="mdm.warehouses.warehouse_id")
    min_qty: float = Field(default=0.0)
    max_qty: float | None = Field(default=None)
    lead_time_days: int = Field(default=0)
    costing_method: str = Field(max_length=20)
    standard_cost: float | None = Field(default=None)
    is_enabled: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    item: Item = Relationship(back_populates="organizations")


class ItemSupplierXref(SQLModel, table=True):
    __tablename__ = "item_supplier_xref"
    __table_args__ = {"schema": "mdm"}

    item_supplier_xref_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    item_id: uuid.UUID = Field(foreign_key="mdm.items.item_id")
    supplier_id: uuid.UUID = Field(foreign_key="mdm.suppliers.supplier_id")
    supplier_item_code: str = Field(max_length=100)
    is_preferred: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    item: Item = Relationship(back_populates="supplier_xrefs")
