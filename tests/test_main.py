from fastapi.testclient import TestClient
from datetime import timedelta
from main import app

from api.api_v1.endpoints.login import create_access_token


client = TestClient(app)

access_token = create_access_token(
    data={
        "username": "admin",
        "id": "1",
        "user_id": "1",
        "role": 100,
        "is_active": 1,
        "department": "IT",
        "status": "ok",
        "type": "account",
        "currentAuthority": "admin",
    },
    expires_delta=timedelta(600),
)


def test_login_for_access_token():
    response = client.post(
        "/api/login/account",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={"username": "admin", "password": "hocmang"},
    )
    print(response.text)
    assert response.status_code == 200


def test_current_user():
    response = client.get(
        "/api/users/currentUser",
        headers={"Authorization": "Bearer {}".format(access_token)},
    )
    assert response.status_code == 200
    assert response.json() == {
        "username": "admin",
        "user_id": 1,
        "status": "ok",
        "type": "account",
        "currentAuthority": 100,
        "role": 100,
    }


def test_get_users():
    response = client.get(
        "/api/users",
        headers={"Authorization": "Bearer {}".format(access_token)},
    )
    assert response.status_code == 200
    assert type(response.json()["data"]) == list
