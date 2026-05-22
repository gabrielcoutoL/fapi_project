from fastapi.testclient import TestClient

from main import app


def teste_fastapi():
    client = TestClient(app=app)

    response = client.get("/")

    assert response.json() == "Hello from fapi-project!"
