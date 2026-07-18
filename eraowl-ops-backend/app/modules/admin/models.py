import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, DateTime, String, Text, Integer, ForeignKey, func, text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = {"schema": "admin"}

    user_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    username: str = Field(sa_column=Column(String(255), unique=True, index=True, nullable=False))
    email: str = Field(sa_column=Column(String(255), unique=True, index=True, nullable=False))
    hashed_password: str = Field(sa_column=Column(String(255), nullable=False))
    permission_version: int = Field(default=0, sa_column=Column(Integer, default=0, nullable=False))
    is_active: bool = Field(default=True, sa_column=Column(Boolean, default=True, nullable=False))
    last_login_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))
    is_deleted: bool = Field(default=False, sa_column=Column(Boolean, default=False, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    user_roles: list["UserRole"] = Relationship(back_populates="user", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    user_business_units: list["UserBusinessUnit"] = Relationship(back_populates="user", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    refresh_tokens: list["RefreshToken"] = Relationship(back_populates="user", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    audit_logs: list["AuditLog"] = Relationship(back_populates="user")


class Role(SQLModel, table=True):
    __tablename__ = "roles"
    __table_args__ = {"schema": "admin"}

    role_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    role_name: str = Field(sa_column=Column(String(100), unique=True, nullable=False))
    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))

    user_roles: list["UserRole"] = Relationship(back_populates="role", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    role_privileges: list["RolePrivilege"] = Relationship(back_populates="role", sa_relationship_kwargs={"cascade": "all, delete-orphan"})


class Privilege(SQLModel, table=True):
    __tablename__ = "privileges"
    __table_args__ = {"schema": "admin"}

    privilege_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    module: str = Field(sa_column=Column(String(100), nullable=False))
    action: str = Field(sa_column=Column(String(100), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=Column(Text, nullable=True))

    role_privileges: list["RolePrivilege"] = Relationship(back_populates="privilege", sa_relationship_kwargs={"cascade": "all, delete-orphan"})


class UserRole(SQLModel, table=True):
    __tablename__ = "user_roles"
    __table_args__ = {"schema": "admin"}

    user_id: uuid.UUID = Field(foreign_key="admin.users.user_id", primary_key=True)
    role_id: uuid.UUID = Field(foreign_key="admin.roles.role_id", primary_key=True)

    user: "User" = Relationship(back_populates="user_roles")
    role: "Role" = Relationship(back_populates="user_roles")


class RolePrivilege(SQLModel, table=True):
    __tablename__ = "role_privileges"
    __table_args__ = {"schema": "admin"}

    role_id: uuid.UUID = Field(foreign_key="admin.roles.role_id", primary_key=True)
    privilege_id: uuid.UUID = Field(foreign_key="admin.privileges.privilege_id", primary_key=True)

    role: "Role" = Relationship(back_populates="role_privileges")
    privilege: "Privilege" = Relationship(back_populates="role_privileges")


class UserBusinessUnit(SQLModel, table=True):
    __tablename__ = "user_business_units"
    __table_args__ = {"schema": "admin"}

    user_id: uuid.UUID = Field(foreign_key="admin.users.user_id", primary_key=True)
    business_unit_id: uuid.UUID = Field(foreign_key="mdm.business_units.business_unit_id", primary_key=True)

    user: "User" = Relationship(back_populates="user_business_units")


class AuditLog(SQLModel, table=True):
    __tablename__ = "audit_logs"
    __table_args__ = {"schema": "admin"}

    audit_log_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    user_id: Optional[uuid.UUID] = Field(default=None, foreign_key="admin.users.user_id", nullable=True)
    action: str = Field(sa_column=Column(String(255), nullable=False))
    target_entity: str = Field(sa_column=Column(String(100), nullable=False))
    target_id: Optional[uuid.UUID] = Field(default=None, nullable=True)
    old_value: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))
    new_value: Optional[dict] = Field(default=None, sa_column=Column(JSONB, nullable=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    user: Optional["User"] = Relationship(back_populates="audit_logs")


class RefreshToken(SQLModel, table=True):
    __tablename__ = "refresh_tokens"
    __table_args__ = {"schema": "admin"}

    refresh_token_id: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    user_id: uuid.UUID = Field(foreign_key="admin.users.user_id", nullable=False)
    token_hash: str = Field(sa_column=Column(String(512), nullable=False))
    expires_at: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False))
    revoked_at: Optional[datetime] = Field(default=None, sa_column=Column(DateTime(timezone=True), nullable=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))

    user: "User" = Relationship(back_populates="refresh_tokens")


class UiStandardTemplate(SQLModel, table=True):
    """Immutable base UI layout template for pages (site-level).

    Read-only for normal users; populated via seed data or admin tooling.
    """

    __tablename__ = "ui_standard_templates"
    __table_args__ = {"schema": "admin"}

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    page_key: str = Field(
        sa_column=Column(String(255), unique=True, nullable=False, index=True)
    )
    schema_version: str = Field(sa_column=Column(String(50), nullable=False))
    base_layout_json: dict = Field(
        default_factory=dict, sa_column=Column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))
    )
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )


class UserUiPersonalization(SQLModel, table=True):
    """Per-user or per-role UI personalisation overrides (delta on top of template).

    user_id and role_id are both nullable but at least one must be set.
    User-specific overrides take precedence over role-level overrides.
    """

    __tablename__ = "user_ui_personalizations"
    __table_args__ = {"schema": "admin"}

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    )
    page_key: str = Field(sa_column=Column(String(255), nullable=False, index=True))
    user_id: Optional[uuid.UUID] = Field(
        default=None,
        sa_column=Column(UUID(as_uuid=True), ForeignKey("admin.users.user_id", ondelete="CASCADE"), nullable=True),
    )
    role_id: Optional[uuid.UUID] = Field(
        default=None,
        sa_column=Column(UUID(as_uuid=True), ForeignKey("admin.roles.role_id", ondelete="CASCADE"), nullable=True),
    )
    override_json: dict = Field(
        default_factory=dict, sa_column=Column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))
    )
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    )
