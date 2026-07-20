import uuid
from datetime import date, datetime
from typing import Optional
from sqlalchemy import Boolean, Column, Date, DateTime, Numeric, String, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlmodel import Field, SQLModel


class CycleCount(SQLModel, table=True):
    __tablename__ = "cycle_counts"
    __table_args__ = {"schema": "wms"}

    count_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    warehouse_id: uuid.UUID = Field(foreign_key="mdm.warehouses.warehouse_id", nullable=False)
    location_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.warehouse_locators.warehouse_locator_id", nullable=True)
    item_id: uuid.UUID = Field(foreign_key="mdm.items.item_id", nullable=False)
    expected_qty: float = Field(sa_column=Column(Numeric(14, 4), nullable=False))
    actual_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))
    variance_qty: Optional[float] = Field(default=None, sa_column=Column(Numeric(14, 4), nullable=True))
    status: str = Field(default="PENDING", sa_column=Column(String(20), default="PENDING", index=True))
    counted_by: Optional[uuid.UUID] = Field(default=None, nullable=True)
    counted_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))
    corporate_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.corporates.corporate_id", nullable=True)
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.companies.company_id", nullable=True)
    site_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.sites.site_id", nullable=True)


class PackingTask(SQLModel, table=True):
    __tablename__ = "packing_tasks"
    __table_args__ = {"schema": "wms"}

    packing_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    so_id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    picking_id: Optional[uuid.UUID] = Field(default=None, foreign_key="wms.picking_tasks.picking_id", nullable=True)
    package_code: str = Field(sa_column=Column(String(50), nullable=False))
    weight_kg: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=True))
    volume_cbm: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 3), nullable=True))
    status: str = Field(default="PENDING", sa_column=Column(String(20), default="PENDING", index=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))
    corporate_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.corporates.corporate_id", nullable=True)
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.companies.company_id", nullable=True)
    site_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.sites.site_id", nullable=True)


class PickingTask(SQLModel, table=True):
    __tablename__ = "picking_tasks"
    __table_args__ = {"schema": "wms"}

    picking_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    so_line_id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    item_id: uuid.UUID = Field(foreign_key="mdm.items.item_id", nullable=False)
    from_location: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.warehouse_locators.warehouse_locator_id", nullable=True)
    qty_required: float = Field(sa_column=Column(Numeric(14, 4), nullable=False))
    qty_picked: float = Field(default=0, sa_column=Column(Numeric(14, 4), default=0))
    status: str = Field(default="PENDING", sa_column=Column(String(20), default="PENDING", index=True))
    assigned_to: Optional[uuid.UUID] = Field(default=None, nullable=True)
    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))
    corporate_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.corporates.corporate_id", nullable=True)
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.companies.company_id", nullable=True)
    site_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.sites.site_id", nullable=True)


class PutawayTask(SQLModel, table=True):
    __tablename__ = "putaway_tasks"
    __table_args__ = {"schema": "wms"}

    putaway_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    receiving_id: Optional[uuid.UUID] = Field(default=None, foreign_key="wms.receiving_schedules.receiving_id", nullable=True)
    item_id: uuid.UUID = Field(foreign_key="mdm.items.item_id", nullable=False)
    from_location: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.warehouse_locators.warehouse_locator_id", nullable=True)
    to_location: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.warehouse_locators.warehouse_locator_id", nullable=True)
    qty: float = Field(sa_column=Column(Numeric(14, 4), nullable=False))
    status: str = Field(default="PENDING", sa_column=Column(String(20), default="PENDING", index=True))
    assigned_to: Optional[uuid.UUID] = Field(default=None, nullable=True)
    completed_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))
    corporate_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.corporates.corporate_id", nullable=True)
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.companies.company_id", nullable=True)
    site_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.sites.site_id", nullable=True)


class ReceivingSchedule(SQLModel, table=True):
    __tablename__ = "receiving_schedules"
    __table_args__ = {"schema": "wms"}

    receiving_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    warehouse_id: uuid.UUID = Field(foreign_key="mdm.warehouses.warehouse_id", nullable=False)
    po_id: Optional[uuid.UUID] = Field(default=None, foreign_key="po.po_headers.po_id", nullable=True)
    asn_id: Optional[uuid.UUID] = Field(default=None, foreign_key="sup.shipment_advices.asn_id", nullable=True)
    scheduled_date: date = Field(sa_column=Column(Date, nullable=False))
    status: str = Field(default="SCHEDULED", sa_column=Column(String(20), default="SCHEDULED", index=True))
    dock_door: Optional[str] = Field(default=None, sa_column=Column(String(50), nullable=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))
    corporate_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.corporates.corporate_id", nullable=True)
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.companies.company_id", nullable=True)
    site_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.sites.site_id", nullable=True)


class ShipmentHeader(SQLModel, table=True):
    __tablename__ = "shipment_headers"
    __table_args__ = {"schema": "wms"}

    shipment_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    so_id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    packing_id: Optional[uuid.UUID] = Field(default=None, foreign_key="wms.packing_tasks.packing_id", nullable=True)
    trip_id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    shipment_code: str = Field(sa_column=Column(String(50), nullable=False, index=True))
    status: str = Field(default="PENDING", sa_column=Column(String(20), default="PENDING", index=True))
    shipped_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))
    corporate_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.corporates.corporate_id", nullable=True)
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.companies.company_id", nullable=True)
    site_id: Optional[uuid.UUID] = Field(default=None, foreign_key="mdm.sites.site_id", nullable=True)


class WarehouseZone(SQLModel, table=True):
    __tablename__ = "warehouse_zones"
    __table_args__ = {"schema": "wms"}

    zone_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    warehouse_id: uuid.UUID = Field(foreign_key="mdm.warehouses.warehouse_id", nullable=False)
    zone_code: str = Field(sa_column=Column(String(50), nullable=False))
    zone_name: str = Field(sa_column=Column(String(100), nullable=False))
    zone_type: str = Field(sa_column=Column(String(30), nullable=False))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
    update_by: Optional[uuid.UUID] = Field(default=None, sa_column=Column(PG_UUID(as_uuid=True), nullable=True))
