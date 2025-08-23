from __future__ import annotations
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_ticket_404() -> None:
    r = client.get("/tickets/9999")
    assert r.status_code == 404
    assert r.json()["detail"] == "Ticket not found"

def test_close_ticket_404() -> None:
    r = client.post("/tickets/9999/close")
    assert r.status_code == 404
    assert r.json()["detail"] == "Ticket not found"
