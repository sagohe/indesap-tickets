from __future__ import annotations
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_close_ticket_twice() -> None:
    # Crear
    r = client.post("/tickets/", json={"title": "Titulo Y", "description": None, "priority": "low"})
    assert r.status_code == 201
    tid = r.json()["id"]

    # Cerrar 1ra vez (debe pasar)
    r1 = client.post(f"/tickets/{tid}/close")
    assert r1.status_code == 200
    assert r1.json()["status"] == "closed"

    # Cerrar 2da vez (sigue devolviendo el ticket; nuestra store lo permite)
    r2 = client.post(f"/tickets/{tid}/close")
    assert r2.status_code == 200
    assert r2.json()["status"] == "closed"
