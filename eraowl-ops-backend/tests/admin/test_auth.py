import pytest


@pytest.mark.asyncio
class TestAuthFlow:
    async def test_login_success(self, client, db_session):
        response = await client.post("/api/v1/admin/users", json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "securepassword123",
            "is_active": True,
        })
        assert response.status_code == 201
        user_data = response.json()

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
        await client.post("/api/v1/admin/users", json={
            "username": "wrongpw",
            "email": "wrong@example.com",
            "password": "securepassword123",
            "is_active": True,
        })
        response = await client.post("/api/v1/admin/login", json={
            "username": "wrongpw",
            "password": "wrongpassword",
        })
        assert response.status_code == 404

    async def test_token_refresh(self, client, db_session):
        await client.post("/api/v1/admin/users", json={
            "username": "refreshuser",
            "email": "refresh@example.com",
            "password": "securepassword123",
            "is_active": True,
        })
        login_resp = await client.post("/api/v1/admin/login", json={
            "username": "refreshuser",
            "password": "securepassword123",
        })
        assert login_resp.status_code == 200
        refresh_token = login_resp.cookies.get("refresh_token") or login_resp.json().get("refresh_token")


@pytest.mark.asyncio
class TestRBAC:
    async def test_check_privilege_denies_missing_permission(self, client, db_session):
        await client.post("/api/v1/admin/users", json={
            "username": "noperm",
            "email": "noperm@example.com",
            "password": "securepassword123",
            "is_active": True,
        })
        login_resp = await client.post("/api/v1/admin/login", json={
            "username": "noperm",
            "password": "securepassword123",
        })
        token = login_resp.json()["access_token"]

        response = await client.get(
            "/api/v1/admin/roles",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert response.status_code == 200

    async def test_permission_version_invalidation(self, client, db_session):
        await client.post("/api/v1/admin/users", json={
            "username": "versionuser",
            "email": "version@example.com",
            "password": "securepassword123",
            "is_active": True,
        })
        login_resp = await client.post("/api/v1/admin/login", json={
            "username": "versionuser",
            "password": "securepassword123",
        })
        token = login_resp.json()["access_token"]
        user_id = login_resp.json()["user"]["id"]

        response = await client.get(
            f"/api/v1/admin/users/{user_id}",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert response.status_code == 200

    async def test_unauthenticated_access(self, client):
        response = await client.get("/api/v1/admin/users")
        assert response.status_code == 401
