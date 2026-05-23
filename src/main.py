from http import HTTPStatus
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from src.schemas import Message

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent


@app.get("/", response_model=Message, status_code=HTTPStatus.OK)
def main():
    return {"message": "Hello from fapi-project!"}


@app.get("/rota_teste", response_class=FileResponse)
def home():
    caminho_html = BASE_DIR / "index.html"
    return FileResponse(caminho_html)
