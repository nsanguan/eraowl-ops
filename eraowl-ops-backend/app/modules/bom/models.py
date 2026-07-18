import uuid
from datetime import date, datetime

from sqlalchemy import Boolean, Column, Date, DateTime, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlmodel import Field, Relationship, SQLModel


class BomHeader(SQLModel, table=True):
    __tablename__ = "bom_headers"
    __table_args__ = {"schema": "bom"}

    bom_header_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    item_id: uuid.UUID = Field(foreign_key="mdm.items.item_id")
    alternate_bom_code: str | None = Field(default=None, max_length=50)
    revision: str = Field(max_length=50)
    status: str = Field(default="PENDING_APPROVAL", max_length=20)
    effective_date_from: date = Field(sa_column=Column(Date, nullable=False))
    effective_date_to: date | None = Field(default=None, sa_column=Column(Date, nullable=True))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    components: list["BomComponent"] = Relationship(back_populates="bom_header")


class BomComponent(SQLModel, table=True):
    __tablename__ = "bom_components"
    __table_args__ = {"schema": "bom"}

    bom_component_id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    bom_header_id: uuid.UUID = Field(foreign_key="bom.bom_headers.bom_header_id")
    component_item_id: uuid.UUID = Field(foreign_key="mdm.items.item_id")
    quantity_per: float = Field(default=1.0)
    uom_id: uuid.UUID = Field(foreign_key="mdm.uoms.uom_id")
    operation_seq: int | None = Field(default=None)
    effective_date_from: date = Field(sa_column=Column(Date, nullable=False))
    effective_date_to: date | None = Field(default=None, sa_column=Column(Date, nullable=True))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )

    bom_header: BomHeader = Relationship(back_populates="components")
