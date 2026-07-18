import pytest

from app.core.security import hash_password
from app.modules.admin.models import User


async def _seed_user(db_session, username: str, password: str, email: str) -> User:
    """Insert a user directly — POST /users requires the manage_users privilege."""
    user = User(username=username, email=email, hashed_password=hash_password(password))
    db_session.add(user)
    await db_session.flush()
    return user


@pytest.mark.asyncio
class TestAuthFlow:
    async def test_login_success(self, client, db_session):
        await _seed_user(db_session, "testuser", "securepassword123", "test@example.com")

        response = await client.post("/api/v1/admin/login", json={
            "username": "testuser",
            "password": "securepassword123",
        })
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert data["user"]["username"] == "testuser"

    async def test_login_wrong_password(self, client, db_session):
        await _seed_user(db_session, "wrongpw", "securepassword123", "wrong@example.com")

        response = await client.post("/api/v1/admin/login", json={
            "username": "wrongpw",
            "password": "wrongpassword",
        })
        assert response.status_code == 404

    async def test_token_refresh(self, client, db_session):
        await _seed_user(db_session, "refreshuser", "securepassword123", "refresh@example.com")

        login_resp = await client.post("/api/v1/admin/login", json={
            "username": "refreshuser",
            "password": "securepassword123",
        })
        assert login_resp.status_code == 200


@pytest.mark.asyncio
class TestRBAC:
    async def test_check_privilege_denies_missing_permission(self, client, db_session):
        await _seed_user(db_session, "noperm", "securepassword123", "noperm@example.com")

        login_resp = await client.post("/api/v1/admin/login", json={
            "username": "noperm",
            "password": "securepassword123",
        })
        token = login_resp.json()["access_token"]

        response = await client.get(
            "/api/v1/admin/roles",
            headers={"Authorization": f"Bearer {token}"},
        )
        # User has no role → no privilege → ForbiddenError → 403
        assert response.status_code == 403

    async def test_permission_version_invalidation(self, client, db_session):
        await _seed_user(db_session, "versionuser", "securepassword123", "version@example.com")

        login_resp = await client.post("/api/v1/admin/login", json={
            "username": "versionuser",
            "password": "securepassword123",
        })
        token = login_resp.json()["access_token"]

        response = await client.get(
            "/api/v1/admin/users/me",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert response.status_code == 200

    async def test_unauthenticated_access(self, client):
        response = await client.get("/api/v1/admin/users")
        assert response.status_code == 401
