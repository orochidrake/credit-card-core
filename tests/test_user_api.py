import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def authorization_headers():
    return {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRnVsYW5vIiwidXNlcl9lbWFpbCI6ImZ1bGFub0BmdWxhbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHBpcmVzIjoxNjkwOTA0NjQwLjA0MTk1MTJ9.q_Zb03FW8zbxPFqahQ_kjoQVrtoIS4HalbMHPWWeoXI"
    }

@pytest.fixture
def sign_up_info():
    return {
        "fullname": "Test Fulano",
        "email": "fulano@fulan.com",
        "password": "teste123",
        "role": "admin"
    }


# this test will fail is user with the same email as in the test file is already registered
def test_user_creation(sign_up_info):
    response = client.post('/api/v1/signup/', json=sign_up_info)
    assert response.status_code == 201

def test_user_login():
    response = client.post('/api/v1/login/', json={"email": "fulano@fulan.com", "password": "teste123"})
    assert response.status_code == 200
    assert response is not None
    assert "access_token" in response.json()
    assert response.json()["access_token"] != ""


def test_get_users(authorization_headers):
    response = client.get('/api/v1/users/', headers=authorization_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    for element in response.json():
        assert isinstance(element, dict)
        assert all(key in element for key in ["id", "fullname", "email", "role", "date", "time"])