"""
Tests for UI personalization (PersonalizeService + deep merge) and the
token blacklist wiring (logout/refresh revocation, remaining-TTL helper).
"""

import uuid

import pytest
from sqlalchemy import func, select

from app.core.config import settings
from app.core.security import create_access_token, token_remaining_seconds
from app.modules.admin.models import (
    AuditLog,
    Role,
    UiStandardTemplate,
    User,
    UserUiPersonalization,
)
from app.modules.admin.services.personalize import (
    PersonalizeService,
    _compute_delta,
    _deep_merge,
)


# ---------------------------------------------------------------------------
# _deep_merge (pure function)
# ---------------------------------------------------------------------------


class TestDeepMerge:
    def test_nested_dicts_merge_recursively(self):
        base = {"grid": {"columns": ["a", "b"], "height": 400}, "title": "X"}
        override = {"grid": {"height": 600}}
        merged = _deep_merge(base, override)
        assert merged["grid"]["height"] == 600
        assert merged["grid"]["columns"] == ["a", "b"]
        assert merged["title"] == "X"

    def test_lists_are_replaced_not_merged(self):
        base = {"columns": ["a", "b", "c"]}
        override = {"columns": ["a"]}
        assert _deep_merge(base, override)["columns"] == ["a"]

    def test_scalar_override_wins_and_new_keys_added(self):
        base = {"a": 1}
        override = {"a": 2, "b": 3}
        merged = _deep_merge(base, override)
        assert merged == {"a": 2, "b": 3}

    def test_inputs_are_not_mutated(self):
        base = {"grid": {"height": 400}}
        override = {"grid": {"height": 600}}
        _deep_merge(base, override)
        assert base == {"grid": {"height": 400}}
        assert override == {"grid": {"height": 600}}


# ---------------------------------------------------------------------------
# PersonalizeService (DB-backed)
# ---------------------------------------------------------------------------


async def _make_user(db, username: str) -> User:
    user = User(username=username, email=f"{username}@example.com", hashed_password="x")
    db.add(user)
    await db.flush()
    return user


async def _make_role(db, name: str) -> Role:
    role = Role(role_name=name)
    db.add(role)
    await db.flush()
    return role


async def _make_template(db, page_key: str, layout: dict) -> UiStandardTemplate:
    template = UiStandardTemplate(page_key=page_key, schema_version="1", base_layout_json=layout)
    db.add(template)
    await db.flush()
    return template


@pytest.mark.asyncio
class TestPersonalizeServiceLoad:
    async def test_returns_default_when_no_template(self, db_session):
        svc = PersonalizeService(db_session)
        result = await svc.load_personalization("missing.page", uuid.uuid4(), [])
        assert result == {
            "page_key": "missing.page",
            "schema_version": "0",
            "layout": {},
            "source": "template",
        }

    async def test_template_only(self, db_session):
        await _make_template(db_session, "p1", {"a": 1, "nested": {"x": 1}})
        svc = PersonalizeService(db_session)
        result = await svc.load_personalization("p1", uuid.uuid4(), [])
        assert result["layout"] == {"a": 1, "nested": {"x": 1}}
        assert result["schema_version"] == "1"
        assert result["source"] == "template"

    async def test_role_override_merges_on_template(self, db_session):
        await _make_template(db_session, "p2", {"a": 1, "nested": {"x": 1}})
        role = await _make_role(db_session, "role-p2")
        db_session.add(
            UserUiPersonalization(
                page_key="p2",
                role_id=role.role_id,
                user_id=None,
                override_json={"nested": {"y": 2}},
            )
        )
        await db_session.flush()

        svc = PersonalizeService(db_session)
        result = await svc.load_personalization("p2", uuid.uuid4(), [role.role_id])
        assert result["layout"] == {"a": 1, "nested": {"x": 1, "y": 2}}
        assert result["source"] == "role"

    async def test_user_override_wins_over_role(self, db_session):
        await _make_template(db_session, "p3", {"theme": "light", "grid": {"h": 400}})
        role = await _make_role(db_session, "role-p3")
        user = await _make_user(db_session, "user-p3")
        db_session.add_all([
            UserUiPersonalization(
                page_key="p3", role_id=role.role_id, user_id=None,
                override_json={"theme": "dark", "grid": {"h": 500}},
            ),
            UserUiPersonalization(
                page_key="p3", user_id=user.user_id, role_id=None,
                override_json={"theme": "blue"},
            ),
        ])
        await db_session.flush()

        svc = PersonalizeService(db_session)
        result = await svc.load_personalization("p3", user.user_id, [role.role_id])
        # user override wins on "theme"; role-level "grid.h" still applies
        assert result["layout"] == {"theme": "blue", "grid": {"h": 500}}
        assert result["source"] == "user"


@pytest.mark.asyncio
class TestPersonalizeServiceSave:
    async def test_save_creates_then_upserts_same_record(self, db_session):
        svc = PersonalizeService(db_session)
        user = await _make_user(db_session, "saver")

        first = await svc.save_personalization(
            page_key="p4",
            target_user_id=user.user_id,
            target_role_id=None,
            override_json={"v": 1},
            actor_user_id=user.user_id,
        )
        second = await svc.save_personalization(
            page_key="p4",
            target_user_id=user.user_id,
            target_role_id=None,
            override_json={"v": 2},
            actor_user_id=user.user_id,
        )
        assert first["id"] == second["id"]

        rows = await db_session.execute(
            select(func.count()).select_from(UserUiPersonalization).where(
                UserUiPersonalization.page_key == "p4"
            )
        )
        assert rows.scalar_one() == 1

    async def test_save_writes_audit_log(self, db_session):
        svc = PersonalizeService(db_session)
        user = await _make_user(db_session, "audited")

        await svc.save_personalization(
            page_key="p5",
            target_user_id=user.user_id,
            target_role_id=None,
            override_json={"v": 1},
            actor_user_id=user.user_id,
        )
        rows = await db_session.execute(
            select(AuditLog).where(AuditLog.target_entity == "UserUiPersonalization")
        )
        entry = rows.scalar_one()
        assert entry.user_id == user.user_id
        assert entry.new_value == {"v": 1}

    async def test_save_requires_a_target(self, db_session):
        svc = PersonalizeService(db_session)
        with pytest.raises(ValueError, match="target_user_id or target_role_id"):
            await svc.save_personalization(
                page_key="p6",
                target_user_id=None,
                target_role_id=None,
                override_json={},
                actor_user_id=None,
            )


# ---------------------------------------------------------------------------
# Token blacklist helpers + logout wiring
# ---------------------------------------------------------------------------


class TestComputeDelta:
    def test_keeps_only_changed_styles(self):
        base = {
            "children": [
                {"id": "a", "styles": {"color": "black"}},
                {"id": "b", "styles": {"font": 12}},
            ]
        }
        current = {
            "children": [
                {"id": "a", "styles": {"color": "red"}},   # changed
                {"id": "b", "styles": {"font": 12}},        # unchanged -> dropped
            ]
        }
        delta = _compute_delta(base, current)
        assert delta == {"children": [{"id": "a", "styles": {"color": "red"}}]}

    def test_nested_changed_child_is_kept(self):
        base = {"children": [{"id": "root", "children": [{"id": "leaf", "styles": {"w": 1}}]}]}
        current = {"children": [{"id": "root", "children": [{"id": "leaf", "styles": {"w": 9}}]}]}
        delta = _compute_delta(base, current)
        assert delta == {
            "children": [{"id": "root", "children": [{"id": "leaf", "styles": {"w": 9}}]}]
        }

    def test_full_tree_passthrough_when_no_children(self):
        flat = {"a": 1}
        assert _compute_delta({"children": []}, flat) == {"a": 1}


class TestDeepMergeIdLists:
    def test_partial_children_delta_keeps_siblings(self):
        base = {
            "children": [
                {"id": "a", "styles": {"color": "black"}},
                {"id": "b", "styles": {"width": "50%"}},
            ]
        }
        override = {"children": [{"id": "b", "styles": {"color": "red"}}]}
        merged = _deep_merge(base, override)
        ids = [n["id"] for n in merged["children"]]
        assert ids == ["a", "b"]  # sibling 'a' not dropped
        assert merged["children"][0]["styles"] == {"color": "black"}
        assert merged["children"][1]["styles"] == {"width": "50%", "color": "red"}

    def test_override_only_child_is_appended(self):
        base = {"children": [{"id": "a", "styles": {}}]}
        override = {"children": [{"id": "z", "styles": {"x": 1}}]}
        merged = _deep_merge(base, override)
        assert [n["id"] for n in merged["children"]] == ["a", "z"]


class TestTokenRemainingSeconds:
    def test_fresh_access_token_has_nearly_full_ttl(self):
        token = create_access_token(str(uuid.uuid4()), [], 0)
        remaining = token_remaining_seconds(token)
        full = settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        assert full - 5 < remaining <= full

    def test_invalid_token_returns_zero(self):
        assert token_remaining_seconds("not-a-jwt") == 0

    def test_expired_token_returns_zero(self):
        from datetime import datetime, timedelta, timezone

        from jose import jwt

        expired = jwt.encode(
            {
                "sub": str(uuid.uuid4()),
                "exp": datetime.now(timezone.utc) - timedelta(minutes=1),
                "type": "access",
            },
            settings.JWT_SECRET,
            algorithm=settings.JWT_ALGORITHM,
        )
        assert token_remaining_seconds(expired) == 0


@pytest.mark.asyncio
class TestLogoutBlacklist:
    async def test_logout_revokes_access_token(self, client, db_session, monkeypatch):
        # In-memory stand-ins for Redis so the test needs no Redis server
        blacklisted: set[str] = set()

        async def fake_blacklist(token: str, ttl_seconds: int) -> bool:
            blacklisted.add(token)
            return True

        async def fake_is_blacklisted(token: str) -> bool:
            return token in blacklisted

        monkeypatch.setattr("app.modules.admin.router.blacklist_token", fake_blacklist)
        monkeypatch.setattr("app.core.dependencies.is_token_blacklisted", fake_is_blacklisted)

        from app.core.security import hash_password

        db_session.add(
            User(
                username="logoutuser",
                email="logout@example.com",
                hashed_password=hash_password("securepassword123"),
            )
        )
        await db_session.flush()

        login_resp = await client.post("/api/v1/admin/login", json={
            "username": "logoutuser",
            "password": "securepassword123",
        })
        assert login_resp.status_code == 200
        tokens = login_resp.json()
        access_token = tokens["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}

        # Token works before logout
        before = await client.get("/api/v1/admin/users/me", headers=headers)
        assert before.status_code == 200

        logout_resp = await client.post("/api/v1/admin/logout", json={
            "refresh_token": tokens["refresh_token"],
            "access_token": access_token,
        })
        assert logout_resp.status_code == 204

        # Same token is rejected after logout
        after = await client.get("/api/v1/admin/users/me", headers=headers)
        assert after.status_code == 401

    async def test_logout_without_access_token_still_succeeds(self, client, db_session):
        from app.core.security import hash_password

        db_session.add(
            User(
                username="plainlogout",
                email="plainlogout@example.com",
                hashed_password=hash_password("securepassword123"),
            )
        )
        await db_session.flush()

        login_resp = await client.post("/api/v1/admin/login", json={
            "username": "plainlogout",
            "password": "securepassword123",
        })
        logout_resp = await client.post("/api/v1/admin/logout", json={
            "refresh_token": login_resp.json()["refresh_token"],
        })
        assert logout_resp.status_code == 204
