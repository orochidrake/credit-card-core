import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def authorization_headers():
    return {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRnVsYW5vIiwidXNlcl9lbWFpbCI6ImZ1bGFub0BmdWxhbi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHBpcmVzIjoxNjkwOTg5MTEwLjQzNzMzOH0.QKn6HMpEe1HVpB9cTBlGUbAHERtLcf8sgLsn4mVO0l4"
    }

def test_create_credit_card_success():
    credit_card = {
        "number": "4111111111111111",
        "exp_date": "12/23",
        "holder": "John Doe",
        "cvv": "123"
    }
    response = client.post("/api/v1/credit-card/", headers=authorization_headers, json=credit_card)
    assert response.status_code == 201
    assert response.json()["holder"] == "John Doe"


def test_create_credit_card_insufficient_privileges():
    credit_card = {
        "number": "4111111111111111",
        "exp_date": "12/23",
        "holder": "John Doe",
        "cvv": "123"
    }
    response = client.post("/api/v1/credit-card/", json=credit_card, headers={"Authorization": "Bearer invalid_token"})
    assert response.status_code == 401


def test_create_credit_card_invalid_number():
    credit_card = {
        "number": "1234567890123456",
        "exp_date": "12/23",
        "holder": "John Doe",
        "cvv": "123"
    }
    response = client.post("/api/v1/credit-card", json=credit_card, headers=authorization_headers)
    assert response.status_code == 400
    assert response.json()["detail"] == "The Credit Card Number is invalid"


def test_create_credit_card_invalid_exp_date():
    credit_card = {
        "number": "4111111111111111",
        "exp_date": "01/20",
        "holder": "John Doe",
        "cvv": "123"
    }
    response = client.post("/api/v1/credit-card/", json=credit_card, headers=authorization_headers)
    assert response.status_code == 400
    assert response.json()["detail"] == "The Expiration date is invalid"


def test_create_credit_card_invalid_holder():
    credit_card = {
        "number": "4111111111111111",
        "exp_date": "12/23",
        "holder": "J",
        "cvv": "123"
    }
    response = client.post("/api/v1/credit-card/", json=credit_card, headers=authorization_headers)
    assert response.status_code == 400
    assert response.json()["detail"] == "The Credit Card Holder is invalid"


def test_create_credit_card_invalid_cvv():
    credit_card = {
        "number": "4111111111111111",
        "exp_date": "12/23",
        "holder": "John Doe",
        "cvv": "12"
    }
    response = client.post("/api/v1/credit-card/", json=credit_card, headers=authorization_headers)
    assert response.status_code == 400
    assert response.json()["detail"] == "The Credit Card CVV is invalid"


def test_create_credit_card_existing_number():
    credit_card = {
        "number": "4111111111111111",
        "exp_date": "12/23",
        "holder": "John Doe",
        "cvv": "123"
    }
    response = client.post("/api/v1/credit-card/", json=credit_card, headers=authorization_headers)
    assert response.status_code == 409
    assert response.json()["detail"] == "Credit card with the number already exists"


def test_create_credit_card_database_error():
    credit_card = {
        "number": "4111111111111111",
        "exp_date": "12/23",
        "holder": "John Doe",
        "cvv": "123"
    }
    response = client.post("/api/v1/credit-card/", json=credit_card, headers=authorization_headers)
    assert response.status_code == 500
    assert response.json()["detail"] == "An error occurred while creating the credit card"