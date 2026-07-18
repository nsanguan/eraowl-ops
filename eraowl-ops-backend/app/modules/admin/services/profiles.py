"""User Profiles (Oracle EBS Profile Options) service.

Manages profile options and resolves their effective value across the level
hierarchy.  Precedence (most specific wins) follows EBS:

    User (1) > Role (2) > Application (3) > Site (4)

The resolved value is the first level (walking from most to least specific)
that carries a stored value for the option.
"""

import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import select, func, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import NotFoundError, ValidationError
from app.modules.admin.models import (
    ProfileOption,
    ProfileOptionValue,
    ProfileLevel,
)

# Level -> precedence weight (lower = higher priority). Mirrors EBS.
LEVEL_PRECEDENCE = {
    "user": 1,
    "role": 2,
    "application": 3,
    "site": 4,
}


class ProfileService:
    def __init__(self, db: AsyncSession):
        self.db = db

    # ------------------------------------------------------------------
    # Levels
    # ------------------------------------------------------------------

    async def list_levels(self) -> list[ProfileLevel]:
        rows = await self.db.execute(select(ProfileLevel).order_by(ProfileLevel.precedence))
        return list(rows.scalars().all())

    # ------------------------------------------------------------------
    # Profile options (catalogue)
    # ------------------------------------------------------------------

    async def list_options(
        self,
        page: int = 1,
        page_size: int = 50,
        search: Optional[str] = None,
        include_system: bool = True,
    ) -> dict:
        conditions = [ProfileOption.is_deleted == False]
        if not include_system:
            conditions.append(ProfileOption.is_system == False)
        if search:
            like = f"%{search.strip()}%"
            conditions.append(
                (ProfileOption.profile_option_name.ilike(like))
                | (ProfileOption.user_profile_option_name.ilike(like))
            )
        where = and_(*conditions)
        total = (
            await self.db.execute(select(func.count()).select_from(ProfileOption).where(where))
        ).scalar() or 0
        rows = await self.db.execute(
            select(ProfileOption)
            .where(where)
            .order_by(ProfileOption.profile_option_name)
            .offset((page - 1) * page_size)
            .limit(page_size)
        )
        items = list(rows.scalars().all())
        total_pages = max(1, (total + page_size - 1) // page_size)
        return {
            "items": items,
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
        }

    async def get_option(self, profile_option_id: uuid.UUID) -> ProfileOption:
        opt = await self.db.get(ProfileOption, profile_option_id)
        if not opt or opt.is_deleted:
            raise NotFoundError(entity="ProfileOption")
        return opt

    async def create_option(self, data) -> ProfileOption:
        payload = data.model_dump() if hasattr(data, "model_dump") else dict(data)
        self._validate_value_type(payload.get("value_type", "text"))
        option = ProfileOption(**payload)
        self.db.add(option)
        await self.db.commit()
        await self.db.refresh(option)
        return option

    async def update_option(self, profile_option_id: uuid.UUID, data) -> ProfileOption:
        option = await self.get_option(profile_option_id)
        payload = data.model_dump(exclude_unset=True) if hasattr(data, "model_dump") else dict(data)
        if "value_type" in payload and payload["value_type"] is not None:
            self._validate_value_type(payload["value_type"])
        for key, val in payload.items():
            if val is not None and hasattr(option, key):
                setattr(option, key, val)
        option.updated_at = datetime.now(timezone.utc)
        await self.db.commit()
        await self.db.refresh(option)
        return option

    async def delete_option(self, profile_option_id: uuid.UUID) -> None:
        option = await self.get_option(profile_option_id)
        option.is_deleted = True
        option.updated_at = datetime.now(timezone.utc)
        await self.db.commit()

    # ------------------------------------------------------------------
    # Values (set / list across levels)
    # ------------------------------------------------------------------

    async def list_values(self, profile_option_id: uuid.UUID) -> list[ProfileOptionValue]:
        await self.get_option(profile_option_id)  # existence check
        rows = await self.db.execute(
            select(ProfileOptionValue)
            .where(ProfileOptionValue.profile_option_id == profile_option_id)
            .order_by(ProfileOptionValue.level)
        )
        return list(rows.scalars().all())

    async def set_value(
        self, profile_option_id: uuid.UUID, level: str, level_key: Optional[str], value: str
    ) -> ProfileOptionValue:
        option = await self.get_option(profile_option_id)
        level = (level or "").strip().lower()
        if level not in LEVEL_PRECEDENCE:
            raise ValidationError(
                f"Invalid level '{level}'. Must be one of: site, application, role, user"
            )
        enabled_flag = {
            "site": option.site_enabled,
            "application": option.application_enabled,
            "role": option.role_enabled,
            "user": option.user_enabled,
        }[level]
        if not enabled_flag:
            raise ValidationError(
                f"Profile option '{option.profile_option_name}' is not enabled at level '{level}'"
            )

        self._validate_value(option.value_type, value)

        if level == "site":
            level_key = None
        elif not level_key:
            raise ValidationError(f"level_key is required for level '{level}'")

        row = await self.db.execute(
            select(ProfileOptionValue).where(
                and_(
                    ProfileOptionValue.profile_option_id == profile_option_id,
                    ProfileOptionValue.level == level,
                    ProfileOptionValue.level_key == level_key,
                )
            )
        )
        existing = row.scalar_one_or_none()
        if existing:
            existing.profile_option_value = value
            existing.updated_at = datetime.now(timezone.utc)
            entity = existing
        else:
            entity = ProfileOptionValue(
                profile_option_id=profile_option_id,
                level=level,
                level_key=level_key,
                profile_option_value=value,
            )
            self.db.add(entity)
        await self.db.commit()
        await self.db.refresh(entity)
        return entity

    async def delete_value(
        self, profile_option_id: uuid.UUID, level: str, level_key: Optional[str]
    ) -> None:
        await self.get_option(profile_option_id)
        if level == "site":
            level_key = None
        row = await self.db.execute(
            select(ProfileOptionValue).where(
                and_(
                    ProfileOptionValue.profile_option_id == profile_option_id,
                    ProfileOptionValue.level == level,
                    ProfileOptionValue.level_key == level_key,
                )
            )
        )
        entity = row.scalar_one_or_none()
        if entity:
            await self.db.delete(entity)
            await self.db.commit()

    # ------------------------------------------------------------------
    # Effective value resolution (the heart of EBS profiles)
    # ------------------------------------------------------------------

    async def get_effective_value(
        self,
        profile_option_name: str,
        user_id: Optional[uuid.UUID] = None,
        role_ids: Optional[list[uuid.UUID]] = None,
    ) -> dict:
        """Resolve the effective value for an option following precedence.

        For ``user`` level the concrete user_id is used; for ``role`` level the
        first role (lowest role id, for determinism) with a value wins;
        ``application`` and ``site`` use the single stored row at that level.
        """
        opt_row = await self.db.execute(
            select(ProfileOption).where(
                ProfileOption.profile_option_name == profile_option_name,
                ProfileOption.is_deleted == False,
            )
        )
        option = opt_row.scalar_one_or_none()
        if option is None:
            raise NotFoundError(entity="ProfileOption")

        vals_row = await self.db.execute(
            select(ProfileOptionValue).where(
                ProfileOptionValue.profile_option_id == option.profile_option_id
            )
        )
        values = list(vals_row.scalars().all())

        def _find(level: str, key: Optional[str]) -> Optional[ProfileOptionValue]:
            for v in values:
                if v.level == level and (v.level_key or None) == key:
                    return v
            return None

        candidates = []
        if user_id is not None:
            v = _find("user", str(user_id))
            if v:
                candidates.append((LEVEL_PRECEDENCE["user"], v))
        if role_ids:
            best = None
            for rid in role_ids:
                v = _find("role", str(rid))
                if v and (best is None or str(rid) < str(best[0])):
                    best = (rid, v)
            if best:
                candidates.append((LEVEL_PRECEDENCE["role"], best[1]))
        app_v = _find("application", None)
        if app_v:
            candidates.append((LEVEL_PRECEDENCE["application"], app_v))
        site_v = _find("site", None)
        if site_v:
            candidates.append((LEVEL_PRECEDENCE["site"], site_v))

        if not candidates:
            return {
                "profile_option_name": profile_option_name,
                "effective_value": None,
                "resolved_level": None,
                "level_key": None,
                "is_default": False,
            }

        candidates.sort(key=lambda c: c[0])
        chosen = candidates[0][1]
        return {
            "profile_option_name": profile_option_name,
            "effective_value": chosen.profile_option_value,
            "resolved_level": chosen.level,
            "level_key": chosen.level_key,
            "is_default": chosen.level == "site",
        }

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _validate_value_type(value_type: str) -> None:
        allowed = {"text", "number", "date", "checkbox", "url"}
        if value_type not in allowed:
            raise ValidationError(
                f"Invalid value_type '{value_type}'. Must be one of: {', '.join(sorted(allowed))}"
            )

    @staticmethod
    def _validate_value(value_type: str, value: str) -> None:
        if value_type == "checkbox" and value not in ("Y", "N", "true", "false", "1", "0"):
            raise ValidationError("checkbox value must be one of: Y, N, true, false, 1, 0")
        if value_type == "number":
            try:
                float(value)
            except (TypeError, ValueError):
                raise ValidationError("value must be numeric")
        if value_type == "url":
            if not (value.startswith("http://") or value.startswith("https://") or value.startswith("/")):
                raise ValidationError("url value must start with http(s):// or /")
