import sys
sys.path.insert(0, "/app")

from app import app


def test_hola_mundo():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hola Mundo" in response.data