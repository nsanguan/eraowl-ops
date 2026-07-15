import hashlib
import uuid
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings as app_settings
from app.core.database import get_db
from app.core.dependencies import check_privilege, get_current_user
from app.core.security import create_access_token, create_refresh_token
from app.modules.admin import schemas
from app.modules.admin.models import UserBusinessUnit
from app.modules.admin.services import AdminService, AdminGenericService
from app.shared.pagination import PaginatedResponse

router = APIRouter()


async def get_service(db: AsyncSession = Depends(get_db)) -> AdminService:
    return AdminService(db)


# ---------------------------------------------------------------------------
# User management
# ---------------------------------------------------------------------------

@router.get("/users")
async def list_users(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    search: Optional[str] = Query(None),
    bu_id: Optional[uuid.UUID] = Query(None),
    role_id: Optional[uuid.UUID] = Query(None),
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_users"),
):
    return await svc.list_users(page=page, page_size=page_size, search=search, bu_id=bu_id, role_id=role_id)


@router.get("/users/me")
async def get_me(
    user=Depends(get_current_user),
    svc: AdminService = Depends(get_service),
):
    roles = await svc.get_user_roles(user.user_id)
    privileges = await svc.get_user_privileges(user.user_id)
    return {
        "user_id": str(user.user_id),
        "username": user.username,
        "email": user.email,
        "is_active": user.is_active,
        "is_deleted": user.is_deleted,
        "permission_version": user.permission_version,
        "last_login_at": user.last_login_at.isoformat() if user.last_login_at else None,
        "created_at": user.created_at.isoformat(),
        "updated_at": user.updated_at.isoformat(),
        "roles": [{"role_id": str(r.role_id), "role_name": r.role_name} for r in roles],
        "privileges": privileges,
    }


@router.get("/users/me/privileges")
async def get_my_privileges(
    user=Depends(get_current_user),
    svc: AdminService = Depends(get_service),
):
    return await svc.get_user_privileges(user.user_id)


@router.get("/users/{user_id}", response_model=schemas.UserOut)
async def get_user(
    user_id: uuid.UUID,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_users"),
):
    return await svc.get_user(user_id)


@router.post("/users", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(
    data: schemas.UserCreate,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_users"),
):
    return await svc.create_user(data)


@router.put("/users/{user_id}", response_model=schemas.UserOut)
async def update_user(
    user_id: uuid.UUID,
    data: schemas.UserUpdate,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_users"),
):
    return await svc.update_user(user_id, data)


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: uuid.UUID,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_users"),
):
    await svc.delete_user(user_id)


@router.put("/users/{user_id}/deactivate", response_model=schemas.UserOut)
async def deactivate_user(
    user_id: uuid.UUID,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_users"),
):
    return await svc.deactivate_user(user_id)


# ---------------------------------------------------------------------------
# User roles
# ---------------------------------------------------------------------------

@router.get("/users/{user_id}/roles", response_model=list[schemas.RoleOut])
async def get_user_roles(
    user_id: uuid.UUID,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_users"),
):
    return await svc.get_user_roles(user_id)


@router.put("/users/{user_id}/roles", status_code=status.HTTP_204_NO_CONTENT)
async def assign_user_roles(
    user_id: uuid.UUID,
    data: schemas.UserAssignRoles,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_users"),
):
    await svc.assign_roles(user_id, data.role_ids)


# ---------------------------------------------------------------------------
# User business units
# ---------------------------------------------------------------------------

@router.get("/users/{user_id}/business-units")
async def get_user_business_units(
    user_id: uuid.UUID,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_users"),
):
    result = await svc.db.execute(
        select(UserBusinessUnit.business_unit_id).where(UserBusinessUnit.user_id == user_id)
    )
    return [row[0] for row in result.all()]


@router.put("/users/{user_id}/business-units", status_code=status.HTTP_204_NO_CONTENT)
async def assign_user_business_units(
    user_id: uuid.UUID,
    data: schemas.UserAssignBusinessUnits,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_users"),
):
    await svc.assign_business_units(user_id, data.bu_ids)


# ---------------------------------------------------------------------------
# User password
# ---------------------------------------------------------------------------

@router.put("/users/{user_id}/change-password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(
    user_id: uuid.UUID,
    data: schemas.UserChangePassword,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_users"),
):
    await svc.change_password(user_id, data.old_password, data.new_password)


# ---------------------------------------------------------------------------
# Role management
# ---------------------------------------------------------------------------

@router.get("/roles", response_model=PaginatedResponse[schemas.RoleOut])
async def list_roles(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_roles"),
):
    return await svc.list_roles(page=page, page_size=page_size)


@router.get("/roles/{role_id}", response_model=schemas.RoleOut)
async def get_role(
    role_id: uuid.UUID,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_roles"),
):
    return await svc.get_role(role_id)


@router.post("/roles", response_model=schemas.RoleOut, status_code=status.HTTP_201_CREATED)
async def create_role(
    data: schemas.RoleCreate,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_roles"),
):
    return await svc.create_role(data)


@router.put("/roles/{role_id}", response_model=schemas.RoleOut)
async def update_role(
    role_id: uuid.UUID,
    data: schemas.RoleUpdate,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_roles"),
):
    return await svc.update_role(role_id, data)


@router.delete("/roles/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_role(
    role_id: uuid.UUID,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "manage_roles"),
):
    await svc.delete_role(role_id)


# ---------------------------------------------------------------------------
# Role permissions
# ---------------------------------------------------------------------------

@router.get("/roles/{role_id}/permissions", response_model=list[schemas.PrivilegeOut])
async def get_role_permissions(
    role_id: uuid.UUID,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "assign_privileges"),
):
    return await svc.get_role_permissions(role_id)


@router.put("/roles/{role_id}/permissions", status_code=status.HTTP_204_NO_CONTENT)
async def assign_role_permissions(
    role_id: uuid.UUID,
    data: schemas.RoleAssignPermissions,
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "assign_privileges"),
):
    await svc.assign_permissions(role_id, data.privilege_ids)


# ---------------------------------------------------------------------------
# Privileges
# ---------------------------------------------------------------------------

@router.get("/privileges", response_model=list[schemas.PrivilegeOut])
async def list_privileges(
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "view"),
):
    return await svc.list_privileges()


@router.post("/privileges/seed")
async def seed_privileges(
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "assign_privileges"),
):
    return await svc.seed_privileges()


# ---------------------------------------------------------------------------
# Audit logs
# ---------------------------------------------------------------------------

@router.get("/audit-logs", response_model=PaginatedResponse[schemas.AuditLogOut])
async def list_audit_logs(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    user_id: Optional[uuid.UUID] = Query(None),
    svc: AdminService = Depends(get_service),
    _priv=check_privilege("admin", "view_audit_logs"),
):
    return await svc.list_audit_logs(
        page=page, page_size=page_size, user_id_filter=user_id
    )


# ---------------------------------------------------------------------------
# Authentication
# ---------------------------------------------------------------------------


@router.post("/login")
async def login(data: schemas.LoginRequest, svc: AdminService = Depends(get_service)):
    user = await svc.authenticate(data.username, data.password)
    role_ids = [r.role_id for r in await svc.get_user_roles(user.user_id)]
    access_token = create_access_token(
        str(user.user_id), [str(r) for r in role_ids], user.permission_version
    )
    refresh_token, expires_at = create_refresh_token(str(user.user_id))

    user_dict = {
        "user_id": str(user.user_id), "username": user.username, "email": user.email,
        "is_active": user.is_active, "is_deleted": user.is_deleted,
        "permission_version": user.permission_version,
        "last_login_at": user.last_login_at.isoformat() if user.last_login_at else None,
        "created_at": user.created_at.isoformat(),
        "updated_at": user.updated_at.isoformat(),
    }

    await svc.store_refresh_token(user.user_id, refresh_token, expires_at)

    expires_in = app_settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": expires_in,
        "user": user_dict,
    }


@router.post("/refresh")
async def refresh_token(
    data: schemas.RefreshRequest,
    svc: AdminService = Depends(get_service),
):
    payload = decode_token(data.refresh_token)
    if not payload or payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    token_hash = hashlib.sha256(data.refresh_token.encode()).hexdigest()
    valid = await svc.is_token_valid(token_hash)
    if not valid:
        raise HTTPException(status_code=401, detail="Token revoked or expired")

    await svc.revoke_refresh_token(token_hash)

    user_id = uuid.UUID(payload["sub"])
    user = await svc.get_user(user_id)
    role_ids = [r.role_id for r in await svc.get_user_roles(user.user_id)]
    access_token = create_access_token(
        str(user.user_id), [str(r) for r in role_ids], user.permission_version
    )
    new_refresh_token, expires_at = create_refresh_token(str(user.user_id))
    await svc.store_refresh_token(user.user_id, new_refresh_token, expires_at)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "refresh_token": new_refresh_token,
        "expires_in": app_settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    }


@router.post("/logout", status_code=204)
async def logout(data: schemas.LogoutRequest, svc: AdminService = Depends(get_service)):
    token_hash = hashlib.sha256(data.refresh_token.encode()).hexdigest()
    await svc.revoke_refresh_token(token_hash)


# ---------------------------------------------------------------------------
# Generic CRUD — dynamic table access via AdminGenericService
# ---------------------------------------------------------------------------

async def get_generic_service(db: AsyncSession = Depends(get_db)) -> AdminGenericService:
    return AdminGenericService(db)


@router.get("/generic/{table_name}")
async def generic_list(
    table_name: str,
    svc: AdminGenericService = Depends(get_generic_service),
    _user=Depends(get_current_user),
    _priv=check_privilege("admin", "manage_users"),
):
    return await svc.list_all(table_name)


@router.get("/generic/{table_name}/{entity_id}")
async def generic_get(
    table_name: str,
    entity_id: str,
    svc: AdminGenericService = Depends(get_generic_service),
    _user=Depends(get_current_user),
    _priv=check_privilege("admin", "manage_users"),
):
    return await svc.get_one(table_name, entity_id)


@router.post("/generic/{table_name}", status_code=status.HTTP_201_CREATED)
async def generic_create(
    table_name: str,
    data: dict,
    svc: AdminGenericService = Depends(get_generic_service),
    _user=Depends(get_current_user),
    _priv=check_privilege("admin", "manage_users"),
):
    return await svc.create(table_name, data)


@router.put("/generic/{table_name}/{entity_id}")
async def generic_update(
    table_name: str,
    entity_id: str,
    data: dict,
    svc: AdminGenericService = Depends(get_generic_service),
    _user=Depends(get_current_user),
    _priv=check_privilege("admin", "manage_users"),
):
    return await svc.update(table_name, entity_id, data)


@router.delete("/generic/{table_name}/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def generic_delete(
    table_name: str,
    entity_id: str,
    svc: AdminGenericService = Depends(get_generic_service),
    _user=Depends(get_current_user),
    _priv=check_privilege("admin", "manage_users"),
):
    await svc.delete(table_name, entity_id)
