from __future__ import annotations
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_ticket_success() -> None:
    # creamos un ticket
    r = client.post("/tickets/", json={"title": "Titulo X", "description": None, "priority": "low"})
    assert r.status_code == 201
    tid = r.json()["id"]

    # lo pedimos por id (rama "found")
    r2 = client.get(f"/tickets/{tid}")
    assert r2.status_code == 200
    assert r2.json()["id"] == tid
