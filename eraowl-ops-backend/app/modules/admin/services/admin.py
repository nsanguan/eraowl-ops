import hashlib
import importlib
import math
import os
import uuid
from datetime import datetime, timezone

import redis.asyncio as aioredis
from sqlalchemy import and_, delete, func, select, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.config import settings
from app.core.security import hash_password, verify_password
from app.core.exceptions import AppError
from app.shared.pagination import PaginatedResponse
from app.modules.admin.exceptions import (
    UserNotFoundError,
    UserAlreadyExistsError,
    RoleNotFoundError,
    RoleAlreadyExistsError,
)
from app.modules.admin.models import (
    User,
    Role,
    Privilege,
    UserRole,
    RolePrivilege,
    UserBusinessUnit,
    AuditLog,
    RefreshToken,
)


def _hash_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


def _paginated(
    items: list, total: int, page: int, page_size: int
) -> PaginatedResponse:
    return PaginatedResponse(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        total_pages=math.ceil(total / page_size) if total > 0 else 0,
    )


class AdminService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def _write_audit_log(
        self,
        user_id: uuid.UUID | None,
        action: str,
        target_entity: str,
        target_id: uuid.UUID | None = None,
        old_value: dict | None = None,
        new_value: dict | None = None,
    ) -> None:
        entry = AuditLog(
            user_id=user_id,
            action=action,
            target_entity=target_entity,
            target_id=target_id,
            old_value=old_value,
            new_value=new_value,
        )
        self.db.add(entry)
        await self.db.flush()

    async def _increment_permission_version(self, role_id: uuid.UUID) -> None:
        user_ids_result = await self.db.execute(
            select(UserRole.user_id).where(UserRole.role_id == role_id)
        )
        user_ids = [row[0] for row in user_ids_result.all()]
        if not user_ids:
            return

        await self.db.execute(
            text(
                "UPDATE admin.users SET permission_version = permission_version + 1 "
                "WHERE user_id = ANY(:ids)"
            ),
            {"ids": user_ids},
        )

    async def list_users(
        self,
        page: int = 1,
        page_size: int = 20,
        search: str | None = None,
        bu_id: uuid.UUID | None = None,
        role_id: uuid.UUID | None = None,
    ) -> PaginatedResponse:
        conditions = [User.is_deleted == False]

        if search:
            conditions.append(
                (User.username.ilike(f"%{search}%")) | (User.email.ilike(f"%{search}%"))
            )
        if bu_id:
            sub = select(UserBusinessUnit.user_id).where(UserBusinessUnit.business_unit_id == bu_id)
            conditions.append(User.user_id.in_(sub))
        if role_id:
            sub = select(UserRole.user_id).where(UserRole.role_id == role_id)
            conditions.append(User.user_id.in_(sub))

        where = and_(*conditions) if conditions else text("TRUE")

        total_result = await self.db.execute(select(func.count()).select_from(User).where(where))
        total = total_result.scalar()

        offset = (page - 1) * page_size
        result = await self.db.execute(
            select(User)
            .options(selectinload(User.user_roles).selectinload(UserRole.role))
            .where(where)
            .order_by(User.created_at.desc())
            .offset(offset)
            .limit(page_size)
        )
        users = list(result.scalars().all())

        items = []
        for u in users:
            roles = [ur.role for ur in u.user_roles]
            items.append({
                "user_id": str(u.user_id),
                "username": u.username,
                "email": u.email,
                "is_active": u.is_active,
                "is_deleted": u.is_deleted,
                "permission_version": u.permission_version,
                "last_login_at": u.last_login_at.isoformat() if u.last_login_at else None,
                "created_at": u.created_at.isoformat(),
                "updated_at": u.updated_at.isoformat(),
                "roles": [{"role_id": str(r.role_id), "role_name": r.role_name, "name": r.role_name} for r in roles],
            })

        return _paginated(items, total, page, page_size)

    async def get_user(self, user_id: uuid.UUID) -> User:
        result = await self.db.execute(select(User).where(User.user_id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            raise UserNotFoundError()
        return user

    async def create_user(self, data) -> User:
        existing = await self.db.execute(
            select(User).where((User.username == data.username) | (User.email == data.email))
        )
        if existing.scalar_one_or_none():
            raise UserAlreadyExistsError()

        user = User(
            username=data.username,
            email=data.email,
            hashed_password=hash_password(data.password),
            is_active=data.is_active,
        )
        self.db.add(user)
        await self.db.flush()

        await self._write_audit_log(
            user_id=user.user_id,
            action="user_created",
            target_entity="User",
            target_id=user.user_id,
            new_value={"username": data.username, "email": data.email},
        )

        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def update_user(self, user_id: uuid.UUID, data) -> User:
        user = await self.get_user(user_id)
        old_value = {"email": user.email, "is_active": user.is_active, "is_deleted": user.is_deleted}

        if data.email is not None:
            user.email = data.email
        if data.is_active is not None:
            user.is_active = data.is_active
        if data.is_deleted is not None:
            user.is_deleted = data.is_deleted

        await self.db.flush()

        await self._write_audit_log(
            user_id=user_id,
            action="user_updated",
            target_entity="User",
            target_id=user_id,
            old_value=old_value,
            new_value={"email": user.email, "is_active": user.is_active, "is_deleted": user.is_deleted},
        )

        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def delete_user(self, user_id: uuid.UUID) -> None:
        user = await self.get_user(user_id)

        chk_audit = await self.db.execute(
            select(func.count()).select_from(AuditLog).where(AuditLog.user_id == user_id)
        )
        audit_count = chk_audit.scalar_one()

        if audit_count > 0:
            raise AppError(
                status_code=409,
                error_code="FK_CONSTRAINT",
                message=(
                    f"Cannot delete user \"{user.username}\" because they have {audit_count} "
                    f"audit log entr(ies). Please deactivate the user instead."
                ),
            )

        await self._write_audit_log(
            user_id=user_id,
            action="user_deleted",
            target_entity="User",
            target_id=user_id,
        )

        await self.db.delete(user)
        await self.db.flush()
        await self.db.commit()

    async def deactivate_user(self, user_id: uuid.UUID) -> User:
        user = await self.get_user(user_id)
        user.is_active = False
        await self.db.flush()
        await self._write_audit_log(
            user_id=user_id,
            action="user_deactivated",
            target_entity="User",
            target_id=user_id,
            new_value={"is_active": False},
        )
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def assign_roles(self, user_id: uuid.UUID, role_ids: list[uuid.UUID]) -> None:
        await self.get_user(user_id)

        await self.db.execute(delete(UserRole).where(UserRole.user_id == user_id))

        for role_id in role_ids:
            ur = UserRole(user_id=user_id, role_id=role_id)
            self.db.add(ur)

        await self.db.flush()
        await self._write_audit_log(
            user_id=user_id,
            action="roles_assigned",
            target_entity="User",
            target_id=user_id,
            new_value={"role_ids": [str(r) for r in role_ids]},
        )
        await self.db.commit()

    async def get_user_roles(self, user_id: uuid.UUID) -> list[Role]:
        result = await self.db.execute(
            select(Role)
            .join(UserRole, UserRole.role_id == Role.role_id)
            .where(UserRole.user_id == user_id)
        )
        return list(result.scalars().all())

    async def assign_business_units(self, user_id: uuid.UUID, bu_ids: list[uuid.UUID]) -> None:
        await self.get_user(user_id)

        await self.db.execute(delete(UserBusinessUnit).where(UserBusinessUnit.user_id == user_id))

        for bu_id in bu_ids:
            ubu = UserBusinessUnit(user_id=user_id, business_unit_id=bu_id)
            self.db.add(ubu)

        await self.db.flush()
        await self._write_audit_log(
            user_id=user_id,
            action="business_units_assigned",
            target_entity="User",
            target_id=user_id,
            new_value={"bu_ids": [str(b) for b in bu_ids]},
        )
        await self.db.commit()

    async def change_password(
        self, user_id: uuid.UUID, old_password: str, new_password: str
    ) -> None:
        user = await self.get_user(user_id)

        if not verify_password(old_password, user.hashed_password):
            from app.core.exceptions import ValidationError
            raise ValidationError(message="Old password is incorrect")

        user.hashed_password = hash_password(new_password)
        await self.db.flush()

        await self._write_audit_log(
            user_id=user_id,
            action="password_changed",
            target_entity="User",
            target_id=user_id,
        )
        await self.db.commit()

    async def list_roles(self, page: int = 1, page_size: int = 20) -> PaginatedResponse:
        total_result = await self.db.execute(select(func.count()).select_from(Role))
        total = total_result.scalar()

        offset = (page - 1) * page_size
        result = await self.db.execute(
            select(Role).order_by(Role.created_at.desc()).offset(offset).limit(page_size)
        )
        roles = list(result.scalars().all())

        return _paginated(roles, total, page, page_size)

    async def get_role(self, role_id: uuid.UUID) -> Role:
        result = await self.db.execute(select(Role).where(Role.role_id == role_id))
        role = result.scalar_one_or_none()
        if not role:
            raise RoleNotFoundError()
        return role

    async def create_role(self, data) -> Role:
        existing = await self.db.execute(
            select(Role).where(Role.role_name == data.role_name)
        )
        if existing.scalar_one_or_none():
            raise RoleAlreadyExistsError()

        role = Role(role_name=data.role_name, description=data.description)
        self.db.add(role)
        await self.db.flush()

        await self._write_audit_log(
            user_id=None,
            action="role_created",
            target_entity="Role",
            target_id=role.role_id,
            new_value={"role_name": data.role_name, "description": data.description},
        )

        await self.db.commit()
        await self.db.refresh(role)
        return role

    async def update_role(self, role_id: uuid.UUID, data) -> Role:
        role = await self.get_role(role_id)
        old_value = {"role_name": role.role_name, "description": role.description}

        if data.role_name is not None:
            role.role_name = data.role_name
        if data.description is not None:
            role.description = data.description

        await self.db.flush()

        await self._write_audit_log(
            user_id=None,
            action="role_updated",
            target_entity="Role",
            target_id=role_id,
            old_value=old_value,
            new_value={"role_name": role.role_name, "description": role.description},
        )

        await self.db.commit()
        await self.db.refresh(role)
        return role

    async def delete_role(self, role_id: uuid.UUID) -> None:
        role = await self.get_role(role_id)
        await self.db.execute(delete(UserRole).where(UserRole.role_id == role_id))
        await self.db.execute(delete(RolePrivilege).where(RolePrivilege.role_id == role_id))
        await self.db.delete(role)
        await self.db.flush()
        await self.db.commit()

    async def _invalidate_redis_for_role(self, role_id: uuid.UUID) -> None:
        try:
            redis_client = aioredis.from_url(settings.REDIS_URL, decode_responses=True)
            user_ids_result = await self.db.execute(
                select(UserRole.user_id).where(UserRole.role_id == role_id)
            )
            user_ids = [str(row[0]) for row in user_ids_result.all()]
            if user_ids:
                key = f"perm_version:{role_id}"
                await redis_client.set(key, datetime.now(timezone.utc).timestamp())
                await redis_client.expire(key, 900)
            await redis_client.aclose()
        except Exception:
            pass

    async def assign_permissions(
        self, role_id: uuid.UUID, privilege_ids: list[uuid.UUID]
    ) -> None:
        await self.get_role(role_id)

        await self.db.execute(
            delete(RolePrivilege).where(RolePrivilege.role_id == role_id)
        )

        for priv_id in privilege_ids:
            rp = RolePrivilege(role_id=role_id, privilege_id=priv_id)
            self.db.add(rp)

        await self.db.flush()
        await self._increment_permission_version(role_id)

        await self._invalidate_redis_for_role(role_id)

        await self._write_audit_log(
            user_id=None,
            action="permissions_assigned",
            target_entity="Role",
            target_id=role_id,
            new_value={"privilege_ids": [str(p) for p in privilege_ids]},
        )
        await self.db.commit()

    async def get_role_permissions(self, role_id: uuid.UUID) -> list[Privilege]:
        result = await self.db.execute(
            select(Privilege)
            .join(RolePrivilege, RolePrivilege.privilege_id == Privilege.privilege_id)
            .where(RolePrivilege.role_id == role_id)
        )
        return list(result.scalars().all())

    async def list_privileges(self) -> list[Privilege]:
        result = await self.db.execute(select(Privilege).order_by(Privilege.module, Privilege.action))
        return list(result.scalars().all())

    async def seed_privileges(self) -> dict[str, int]:
        modules_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."
        )
        privileges_to_seed = self._collect_privileges(modules_dir)

        created = 0
        skipped = 0

        for priv in privileges_to_seed:
            existing = await self.db.execute(
                select(Privilege).where(
                    and_(
                        Privilege.module == priv["module"],
                        Privilege.action == priv["action"],
                    )
                )
            )
            if existing.scalar_one_or_none() is None:
                p = Privilege(
                    module=priv["module"],
                    action=priv["action"],
                    description=priv["description"],
                )
                self.db.add(p)
                created += 1
            else:
                skipped += 1

        await self.db.flush()
        await self.db.commit()
        return {"created": created, "skipped": skipped}

    def _collect_privileges(self, base_dir: str) -> list[dict]:
        result: list[dict] = []

        for entry in sorted(os.listdir(base_dir)):
            entry_path = os.path.join(base_dir, entry)
            if not os.path.isdir(entry_path):
                continue

            permissions_file = os.path.join(entry_path, "permissions.py")
            if os.path.isfile(permissions_file):
                try:
                    spec = importlib.util.spec_from_file_location(
                        f"_seed_{entry}", permissions_file
                    )
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                    module_name = getattr(mod, "MODULE_NAME", entry)
                    privileges = getattr(mod, "PRIVILEGES", [])
                    for priv in privileges:
                        result.append({
                            "module": module_name,
                            "action": priv["action"],
                            "description": priv.get("description", ""),
                        })
                except Exception:
                    pass
                continue

            result.extend(self._collect_privileges(entry_path))

        return result

    async def list_audit_logs(
        self,
        page: int = 1,
        page_size: int = 20,
        user_id_filter: uuid.UUID | None = None,
    ) -> PaginatedResponse:
        conditions = []
        if user_id_filter:
            conditions.append(AuditLog.user_id == user_id_filter)

        where = and_(*conditions) if conditions else text("TRUE")

        total_result = await self.db.execute(
            select(func.count()).select_from(AuditLog).where(where)
        )
        total = total_result.scalar()

        offset = (page - 1) * page_size
        result = await self.db.execute(
            select(AuditLog)
            .where(where)
            .order_by(AuditLog.created_at.desc())
            .offset(offset)
            .limit(page_size)
        )
        logs = list(result.scalars().all())

        return _paginated(logs, total, page, page_size)

    async def store_refresh_token(
        self,
        user_id: uuid.UUID,
        token: str,
        expires_at: datetime,
    ) -> RefreshToken:
        token_hash = _hash_token(token)
        rt = RefreshToken(
            user_id=user_id,
            token_hash=token_hash,
            expires_at=expires_at,
        )
        self.db.add(rt)
        await self.db.commit()
        return rt

    async def revoke_refresh_token(self, token_hash: str) -> None:
        result = await self.db.execute(
            select(RefreshToken).where(RefreshToken.token_hash == token_hash)
        )
        rt = result.scalar_one_or_none()
        if rt:
            rt.revoked_at = datetime.now(timezone.utc)
            await self.db.flush()
            await self.db.commit()

    async def is_token_valid(self, token_hash: str) -> bool:
        result = await self.db.execute(
            select(RefreshToken).where(
                and_(
                    RefreshToken.token_hash == token_hash,
                    RefreshToken.revoked_at.is_(None),
                    RefreshToken.expires_at > datetime.now(timezone.utc),
                )
            )
        )
        return result.scalar_one_or_none() is not None

    async def authenticate(self, username: str, password: str) -> User:
        result = await self.db.execute(
            select(User).where(
                and_(User.username == username, User.is_deleted == False, User.is_active == True)
            )
        )
        user = result.scalar_one_or_none()
        if not user or not verify_password(password, user.hashed_password):
            raise UserNotFoundError()
        user.last_login_at = datetime.now(timezone.utc)
        return user

    async def get_user_privileges(self, user_id: uuid.UUID) -> list[dict]:
        rows = await self.db.execute(
            select(Privilege)
            .select_from(User)
            .join(UserRole, UserRole.user_id == User.user_id)
            .join(RolePrivilege, RolePrivilege.role_id == UserRole.role_id)
            .join(Privilege, Privilege.privilege_id == RolePrivilege.privilege_id)
            .where(User.user_id == user_id)
        )
        privileges = rows.scalars().all()
        return [{"module": p.module, "action": p.action} for p in privileges]

    async def revoke_all_user_tokens(self, user_id: uuid.UUID) -> None:
        await self.db.execute(
            text(
                "UPDATE admin.refresh_tokens SET revoked_at = :now WHERE user_id = :uid AND revoked_at IS NULL"
            ),
            {"now": datetime.now(timezone.utc), "uid": user_id},
        )
        await self.db.flush()
        await self.db.commit()

    async def get_refresh_token_hash(self, token: str) -> RefreshToken | None:
        result = await self.db.execute(
            select(RefreshToken).where(
                and_(
                    RefreshToken.token_hash == _hash_token(token),
                    RefreshToken.revoked_at.is_(None),
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_permission_matrix(self) -> dict:
        roles_result = await self.db.execute(
            select(Role).order_by(Role.role_name)
        )
        roles = roles_result.scalars().all()

        privileges_result = await self.db.execute(
            select(Privilege).order_by(Privilege.module, Privilege.action)
        )
        privileges = privileges_result.scalars().all()

        rp_rows = (await self.db.execute(select(RolePrivilege))).scalars().all()

        matrix: dict[str, list[str]] = {}
        for rp in rp_rows:
            rid = str(rp.role_id)
            pid = str(rp.privilege_id)
            if rid not in matrix:
                matrix[rid] = []
            matrix[rid].append(pid)

        return {
            "roles": [{"role_id": str(r.role_id), "role_name": r.role_name, "description": r.description} for r in roles],
            "privileges": [{"privilege_id": str(p.privilege_id), "module": p.module, "action": p.action, "description": p.description} for p in privileges],
            "matrix": matrix,
        }

    async def sync_permission_matrix(self, matrix: dict[str, list[str]]) -> None:
        role_ids = [uuid.UUID(rid) for rid in matrix.keys()]

        for role_id in role_ids:
            await self.db.execute(
                delete(RolePrivilege).where(RolePrivilege.role_id == role_id)
            )

            priv_ids = matrix.get(str(role_id), [])
            for pid in priv_ids:
                rp = RolePrivilege(role_id=role_id, privilege_id=uuid.UUID(pid))
                self.db.add(rp)

            user_ids_result = await self.db.execute(
                select(UserRole.user_id).where(UserRole.role_id == role_id)
            )
            user_ids = [row[0] for row in user_ids_result.all()]
            if user_ids:
                await self.db.execute(
                    text(
                        "UPDATE admin.users SET permission_version = permission_version + 1 "
                        "WHERE user_id = ANY(:ids)"
                    ),
                    {"ids": user_ids},
                )

            try:
                import redis.asyncio as aioredis
                from app.core.config import settings
                r = await aioredis.from_url(settings.REDIS_URL, decode_responses=True)
                await r.set(f"perm_version:{role_id}", datetime.now(timezone.utc).timestamp())
                await r.expire(f"perm_version:{role_id}", 900)
                await r.aclose()
            except Exception:
                pass

        await self.db.commit()
