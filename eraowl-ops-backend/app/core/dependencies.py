import uuid
from fastapi import Depends, Request
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import decode_token
from app.core.exceptions import UnauthorizedError, ForbiddenError


async def get_current_user(
    request: Request,
    db: AsyncSession = Depends(get_db),
):
    from app.modules.admin.models import User

    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        raise UnauthorizedError(message="Missing or invalid Authorization header")

    token = auth_header[7:]
    payload = decode_token(token)
    if not payload or payload.get("type") != "access":
        raise UnauthorizedError(message="Invalid or expired token")

    user_id = payload.get("sub")
    if not user_id:
        raise UnauthorizedError(message="Invalid token payload")

    result = await db.execute(
        select(User).where(
            and_(User.user_id == uuid.UUID(user_id), User.is_deleted == False, User.is_active == True)
        )
    )
    user_inst = result.scalar_one_or_none()
    if not user_inst:
        raise UnauthorizedError(message="User not found or inactive")

    token_version = payload.get("ver", 0)
    if token_version != user_inst.permission_version:
        raise UnauthorizedError(message="Session expired — permissions changed, please re-login")

    return user_inst


def check_privilege(module: str, action: str):
    from app.modules.admin.models import User, UserRole, Role, RolePrivilege, Privilege

    async def _check(
        request: Request,
        user: User = Depends(get_current_user),
        db: AsyncSession = Depends(get_db),
    ) -> bool:
        rows = await db.execute(
            select(Privilege)
            .select_from(User)
            .join(UserRole, UserRole.user_id == User.user_id)
            .join(Role, Role.role_id == UserRole.role_id)
            .join(RolePrivilege, RolePrivilege.role_id == Role.role_id)
            .join(Privilege, Privilege.privilege_id == RolePrivilege.privilege_id)
            .where(
                and_(
                    User.user_id == user.user_id,
                    Privilege.module == module,
                    Privilege.action == action,
                )
            )
        )
        privilege = rows.scalar_one_or_none()
        if not privilege:
            raise ForbiddenError(
                message=f"Missing privilege: {module}.{action}"
            )
        return True

    return Depends(_check)
