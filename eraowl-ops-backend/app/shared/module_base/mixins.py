"""
SQLModel Mixins — Global Module Design
=======================================

Shared columns that every entity uses.
Models can inherit from these mixins to avoid duplicating audit columns.

Usage:
    class User(UUIDPKMixin, AuditMixin, SoftDeleteMixin, table=True):
        __tablename__ = "users"
        __table_args__ = {"schema": "admin"}
        username: str = ...
"""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlmodel import Field, SQLModel


class UUIDPKMixin(SQLModel):
    """Standard UUID primary key with uuidv7 default (server-side)."""

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )


class AuditMixin(SQLModel):
    """Created/updated timestamps for every entity."""

    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )
    update_by: Optional[str] = Field(default=None, sa_column=Column(String(100), nullable=True))


class SoftDeleteMixin(SQLModel):
    """Soft-delete support + active flag."""

    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))


class ObjectVersionMixin(SQLModel):
    """Optimistic locking version counter."""

    object_version_number: int = Field(default=1, sa_column=Column(Integer, default=1, nullable=False))
