from typing import Optional
import uuid
from datetime import datetime
from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    is_active: bool = True


class UserUpdate(BaseModel):
    email: Optional[str] = None
    is_active: Optional[bool] = None
    is_deleted: Optional[bool] = None


class UserOut(BaseModel):
    user_id: uuid.UUID
    username: str
    email: str
    is_active: bool
    last_login_at: Optional[datetime] = None
    permission_version: int
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class UserChangePassword(BaseModel):
    old_password: str
    new_password: str


class UserAssignRoles(BaseModel):
    role_ids: list[uuid.UUID]


class UserAssignBusinessUnits(BaseModel):
    bu_ids: list[uuid.UUID]


class RoleOut(BaseModel):
    role_id: uuid.UUID
    role_name: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class PrivilegeOut(BaseModel):
    privilege_id: uuid.UUID
    module: str
    action: str
    description: Optional[str] = None

    model_config = {"from_attributes": True}


class UserWithRoles(UserOut):
    roles: list[RoleOut] = []
    business_unit_ids: list[uuid.UUID] = []


class RoleCreate(BaseModel):
    role_name: str
    description: Optional[str] = None


class RoleUpdate(BaseModel):
    role_name: Optional[str] = None
    description: Optional[str] = None


class RoleAssignPermissions(BaseModel):
    privilege_ids: list[uuid.UUID]


class RoleWithPermissions(RoleOut):
    privileges: list[PrivilegeOut] = []


class PrivilegeCreate(BaseModel):
    module: str
    action: str
    description: Optional[str] = None


class AuditLogOut(BaseModel):
    audit_log_id: uuid.UUID
    user_id: Optional[uuid.UUID] = None
    action: str
    target_entity: str
    target_id: Optional[uuid.UUID] = None
    old_value: Optional[dict] = None
    new_value: Optional[dict] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user: UserOut


class RefreshRequest(BaseModel):
    refresh_token: str


class LogoutRequest(BaseModel):
    refresh_token: str


class PermissionMatrixResponse(BaseModel):
    roles: list[RoleOut]
    privileges: list[PrivilegeOut]
    matrix: dict[str, list[str]]


class PermissionMatrixSync(BaseModel):
    matrix: dict[str, list[str]]
