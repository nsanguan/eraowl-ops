"""UI Personalization Service — deep merge, load, save, audit trail."""

import uuid
from copy import deepcopy
from datetime import datetime, timezone

from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.admin.models import (
    UiStandardTemplate,
    UserUiPersonalization,
    UiTheme,
    UserRole,
    AuditLog,
)


def _is_id_list(val) -> bool:
    """True when val is a list of dicts each carrying an 'id' key
    (the layout-tree node convention)."""
    return (
        isinstance(val, list)
        and val
        and all(isinstance(v, dict) and "id" in v for v in val)
    )


def _merge_id_lists(base_list: list, override_list: list) -> list:
    """Merge two layout node lists by node id.

    Base nodes absent from the override are kept; override nodes are merged
    onto their base counterpart recursively; override-only nodes are
    appended.  This is what lets a *partial* delta (containing only the
    changed component) apply without dropping its siblings.
    """
    by_id = {node.get("id"): node for node in base_list}
    result = [deepcopy(n) for n in base_list]
    for node in override_list:
        nid = node.get("id")
        if nid in by_id:
            idx = next(i for i, n in enumerate(result) if n.get("id") == nid)
            result[idx] = _deep_merge(result[idx], node)
        else:
            result.append(deepcopy(node))
    return result


def _deep_merge(base: dict, override: dict) -> dict:
    """Recursively merge override dict into base dict.

    - Nested dicts are merged recursively.
    - Lists of layout nodes (dicts with an 'id') are merged *by id* so a
      partial override does not drop sibling nodes.
    - Other lists (e.g. plain string arrays) are replaced entirely.
    - Scalar values in override win over base.
    """
    merged = deepcopy(base)
    for key, val in override.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(val, dict):
            merged[key] = _deep_merge(merged[key], val)
        elif (
            key in merged
            and _is_id_list(merged[key])
            and _is_id_list(val)
        ):
            merged[key] = _merge_id_lists(merged[key], val)
        else:
            merged[key] = deepcopy(val)
    return merged


def _compute_delta(base: dict, current: dict) -> dict:
    """Compute the personalisation delta between a base layout and the
    current (edited) layout.

    Only component nodes whose ``styles`` differ from the base are kept.
    Structural geometry (``componentType`` / ``children``) is pruned so the
    stored override stays a pure style delta, matching the Oracle EBS
    "Personalization = differences only" model.  If ``current`` carries no
    ``children`` (e.g. it was sent as an already-flat override) it is
    returned untouched so callers that send a full tree still work.
    """
    if not base or "children" not in current:
        return deepcopy(current)

    base_by_id: dict = {}

    def _index(node: dict) -> None:
        if not node or not isinstance(node, dict):
            return
        if node.get("id") is not None:
            base_by_id[node["id"]] = {
                "styles": node.get("styles") or {},
                "meta": node.get("meta") or {},
            }
        for child in node.get("children") or []:
            _index(child)

    _index(base)

    def _diff(node: dict) -> dict | None:
        if not node or not isinstance(node, dict):
            return None
        node_id = node.get("id")
        base_entry = base_by_id.get(node_id, {"styles": {}, "meta": {}})
        base_styles = base_entry.get("styles", {})
        base_meta = base_entry.get("meta", {})
        cur_styles = node.get("styles") or {}
        cur_meta = node.get("meta") or {}
        diff_styles = {
            k: v for k, v in cur_styles.items() if not _equal(base_styles.get(k), v)
        }
        diff_meta = {
            k: v for k, v in cur_meta.items() if not _equal(base_meta.get(k), v)
        }
        kept_children = []
        for child in node.get("children") or []:
            d = _diff(child)
            if d is not None:
                kept_children.append(d)
        if not diff_styles and not diff_meta and not kept_children:
            return None
        result: dict = {"id": node_id}
        if diff_styles:
            result["styles"] = diff_styles
        if diff_meta:
            result["meta"] = diff_meta
        if kept_children:
            result["children"] = kept_children
        return result

    return {"children": [c for c in (_diff(n) for n in current["children"]) if c is not None]}


def _equal(a, b) -> bool:
    if isinstance(a, dict) and isinstance(b, dict):
        return a == b
    return a == b


class PersonalizeService:
    """Read/write UI personalisation overrides.

    The base template (``UiStandardTemplate``) is strictly READ-ONLY from the
    API surface — this service only ever reads it and writes to
    ``UserUiPersonalization``.  There is deliberately no method here that
    mutates a standard template.
    """

    def __init__(self, db: AsyncSession):
        self.db = db

    async def _write_audit_log(
        self,
        actor_user_id: uuid.UUID | None,
        action: str,
        target_entity: str,
        target_id: uuid.UUID | None = None,
        old_value: dict | None = None,
        new_value: dict | None = None,
    ) -> None:
        entry = AuditLog(
            user_id=actor_user_id,
            action=action,
            target_entity=target_entity,
            target_id=target_id,
            old_value=old_value,
            new_value=new_value,
        )
        self.db.add(entry)
        await self.db.flush()

    async def get_user_role_ids(self, user_id: uuid.UUID) -> list[uuid.UUID]:
        """Return all role UUIDs assigned to a user."""
        rows = await self.db.execute(
            select(UserRole.role_id).where(UserRole.user_id == user_id)
        )
        return [row[0] for row in rows.all()]

    async def load_template(self, page_key: str) -> dict | None:
        """Read the immutable base template for a page (read-only source)."""
        row = await self.db.execute(
            select(UiStandardTemplate).where(UiStandardTemplate.page_key == page_key)
        )
        template = row.scalar_one_or_none()
        if template is None:
            return None
        return {
            "page_key": page_key,
            "schema_version": template.schema_version,
            "layout": template.base_layout_json or {},
        }

    async def list_templates(self, search: str | None = None) -> list[dict]:
        """List all standard UI templates (the catalogue of personalizable
        pages).  Optionally filtered by a case-insensitive substring match on
        ``page_key`` or ``schema_version``.  Sorted by ``page_key``.
        """
        stmt = select(
            UiStandardTemplate.page_key,
            UiStandardTemplate.schema_version,
            UiStandardTemplate.base_layout_json,
        )
        if search:
            like = f"%{search.strip()}%"
            stmt = stmt.where(
                UiStandardTemplate.page_key.ilike(like)
                | UiStandardTemplate.schema_version.ilike(like)
            )
        stmt = stmt.order_by(UiStandardTemplate.page_key)
        rows = await self.db.execute(stmt)
        results = []
        for page_key, schema_version, base_layout in rows.all():
            components = _count_components(base_layout or {})
            results.append(
                {
                    "page_key": page_key,
                    "schema_version": schema_version,
                    "component_count": components,
                }
            )
        return results

    async def get_template_detail(self, page_key: str) -> dict | None:
        """Full template record including the base layout component tree."""
        row = await self.db.execute(
            select(UiStandardTemplate).where(UiStandardTemplate.page_key == page_key)
        )
        template = row.scalar_one_or_none()
        if template is None:
            return None
        return {
            "id": str(template.id),
            "page_key": template.page_key,
            "schema_version": template.schema_version,
            "base_layout_json": template.base_layout_json or {},
            "component_count": _count_components(template.base_layout_json or {}),
            "created_at": template.created_at.isoformat() if template.created_at else None,
            "updated_at": template.updated_at.isoformat() if template.updated_at else None,
        }

    async def load_personalization(
        self, page_key: str, user_id: uuid.UUID, role_ids: list[uuid.UUID]
    ) -> dict:
        """Load the merged UI layout for a page key.

        Resolution order:
        1. UiStandardTemplate (base layout)
        2. Role-level override — when the user has multiple roles with
           overrides, the most recently updated one wins (deterministic
           given the data, but arbitrary by design: role-level overrides
           are intended to be maintained for one primary role per page).
        3. User-level override (wins over everything)
        """
        # --- 1. Base template ---
        row = await self.db.execute(
            select(UiStandardTemplate).where(
                UiStandardTemplate.page_key == page_key
            )
        )
        template = row.scalar_one_or_none()
        if template is None:
            return {
                "page_key": page_key,
                "schema_version": "0",
                "layout": {},
                "source": "template",
            }

        base = template.base_layout_json or {}
        schema_version = template.schema_version
        merged = deepcopy(base)
        source = "template"

        # --- 2. Role-level override (first match wins) ---
        if role_ids:
            role_row = await self.db.execute(
                select(UserUiPersonalization).where(
                    and_(
                        UserUiPersonalization.page_key == page_key,
                        UserUiPersonalization.role_id.in_(role_ids),
                        UserUiPersonalization.user_id.is_(None),
                    )
                ).order_by(UserUiPersonalization.updated_at.desc())
            )
            role_personalization = role_row.scalars().first()
            if role_personalization and role_personalization.override_json:
                merged = _deep_merge(merged, role_personalization.override_json)
                source = "role"

        # --- 3. User-level override (highest priority) ---
        user_row = await self.db.execute(
            select(UserUiPersonalization).where(
                and_(
                    UserUiPersonalization.page_key == page_key,
                    UserUiPersonalization.user_id == user_id,
                )
            )
        )
        user_personalization = user_row.scalar_one_or_none()
        if user_personalization and user_personalization.override_json:
            merged = _deep_merge(merged, user_personalization.override_json)
            source = "user"

        return {
            "page_key": page_key,
            "schema_version": schema_version,
            "layout": merged,
            "source": source,
        }

    async def save_personalization(
        self,
        page_key: str,
        target_user_id: uuid.UUID | None,
        target_role_id: uuid.UUID | None,
        override_json: dict,
        actor_user_id: uuid.UUID | None,
        as_delta: bool = False,
    ) -> dict:
        """Upsert a personalisation override and write an audit log.

        ``as_delta=True`` shrinks ``override_json`` to only the style
        differences versus the base template before storing — this is what
        the In-Context Editor's "Save Personalization" uses so each profile
        carries just its own changes (Delta/Override model).  When
        ``as_delta=False`` the payload is stored verbatim (full override).
        """
        if not target_user_id and not target_role_id:
            raise ValueError(
                "At least one of target_user_id or target_role_id must be set"
            )

        if as_delta:
            template = await self.load_template(page_key)
            base = template["layout"] if template else {}
            override_json = _compute_delta(base, override_json)

        # Locate existing record
        conditions = [UserUiPersonalization.page_key == page_key]
        if target_user_id:
            conditions.append(UserUiPersonalization.user_id == target_user_id)
        else:
            conditions.append(UserUiPersonalization.user_id.is_(None))

        if target_role_id:
            conditions.append(UserUiPersonalization.role_id == target_role_id)
        else:
            conditions.append(UserUiPersonalization.role_id.is_(None))

        row = await self.db.execute(
            select(UserUiPersonalization).where(and_(*conditions))
        )
        existing = row.scalar_one_or_none()

        old_value = None
        if existing:
            old_value = existing.override_json
            existing.override_json = override_json
            existing.updated_at = datetime.now(timezone.utc)
            entity_id = existing.id
        else:
            entry = UserUiPersonalization(
                page_key=page_key,
                user_id=target_user_id,
                role_id=target_role_id,
                override_json=override_json,
            )
            self.db.add(entry)
            await self.db.flush()
            entity_id = entry.id

        await self.db.commit()
        await self._write_audit_log(
            actor_user_id=actor_user_id,
            action="upsert" if old_value is not None else "create",
            target_entity="UserUiPersonalization",
            target_id=entity_id,
            old_value=old_value,
            new_value=override_json,
        )

        return {
            "id": str(entity_id),
            "page_key": page_key,
            "user_id": str(target_user_id) if target_user_id else None,
            "role_id": str(target_role_id) if target_role_id else None,
        }

    async def load_theme(self, user_id: uuid.UUID, role_ids: list[uuid.UUID]) -> dict:
        """Resolve global theme tokens: role-level then user-level (user wins)."""
        tokens = {}
        source = "default"
        if role_ids:
            row = await self.db.execute(
                select(UiTheme)
                .where(UiTheme.role_id.in_(role_ids), UiTheme.user_id.is_(None))
                .order_by(UiTheme.updated_at.desc())
            )
            role_theme = row.scalar_one_or_none()
            if role_theme and role_theme.tokens:
                tokens = {**tokens, **role_theme.tokens}
                source = "role"
        if user_id:
            row = await self.db.execute(
                select(UiTheme).where(UiTheme.user_id == user_id)
            )
            user_theme = row.scalar_one_or_none()
            if user_theme and user_theme.tokens:
                tokens = {**tokens, **user_theme.tokens}
                source = "user"
        return {"tokens": tokens, "source": source}

    async def save_theme(
        self,
        target_user_id: uuid.UUID | None,
        target_role_id: uuid.UUID | None,
        tokens: dict | None,
        actor_user_id: uuid.UUID | None,
    ) -> dict:
        if not target_user_id and not target_role_id:
            raise ValueError("At least one of target_user_id or target_role_id must be set")
        conditions = []
        if target_user_id:
            conditions.append(UiTheme.user_id == target_user_id)
        else:
            conditions.append(UiTheme.user_id.is_(None))
        if target_role_id:
            conditions.append(UiTheme.role_id == target_role_id)
        else:
            conditions.append(UiTheme.role_id.is_(None))

        row = await self.db.execute(select(UiTheme).where(and_(*conditions)))
        existing = row.scalar_one_or_none()

        old_value = None
        if existing:
            old_value = existing.tokens
            existing.tokens = tokens or {}
            existing.updated_at = datetime.now(timezone.utc)
            entity_id = existing.id
        else:
            entry = UiTheme(user_id=target_user_id, role_id=target_role_id, tokens=tokens or {})
            self.db.add(entry)
            await self.db.flush()
            entity_id = entry.id

        await self.db.commit()
        await self._write_audit_log(
            actor_user_id=actor_user_id,
            action="upsert" if old_value is not None else "create",
            target_entity="UiTheme",
            target_id=entity_id,
            old_value=old_value,
            new_value=tokens,
        )
        return {"id": str(entity_id), "user_id": str(target_user_id) if target_user_id else None, "role_id": str(target_role_id) if target_role_id else None}


def _count_components(layout: dict) -> int:
    """Count component nodes (those carrying an ``id``) in a layout tree."""
    count = 0

    def walk(node: dict) -> None:
        if not node or not isinstance(node, dict):
            return
        if node.get("id") is not None:
            nonlocal count
            count += 1
        for child in node.get("children") or []:
            walk(child)

    walk(layout)
    return count