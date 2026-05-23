from http import HTTPStatus

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app=app)


def test_fastapi_root():
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello from fapi-project!"}


def test_retorno_html():
    response = client.get("/rota_teste")

    assert response.status_code == HTTPStatus.OK

    assert "text/html" in response.headers["content-type"]

    assert "<!DOCTYPE html>" in response.text
    assert "Minha Página" in response.text
    assert "Olá! Esta é uma página HTML retornada pelo Python." in response.text
