from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_create_and_list_ticket() -> None:
    payload = {
        "title": "Error en producción",
        "description": "500 en /checkout",
        "priority": "high",
    }
    r = client.post("/tickets/", json=payload)
    assert r.status_code == 201
    created = r.json()
    assert created["id"] == 1
    assert created["status"] == "open"

    r2 = client.get("/tickets/")
    assert r2.status_code == 200
    items = r2.json()
    assert len(items) == 1


def test_close_ticket() -> None:
    r = client.post(
        "/tickets/",
        json={"title": "Bug", "description": None, "priority": "low"},
    )
    ticket_id = r.json()["id"]

    r2 = client.post(f"/tickets/{ticket_id}/close")
    assert r2.status_code == 200
    assert r2.json()["status"] == "closed"
