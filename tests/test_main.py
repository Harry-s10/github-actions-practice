from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok"}


def test_add():
    response = client.get("/add/2/3")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"result": 5}
