from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_ticket_after_close() -> None:
    r = client.post(
        "/tickets/",
        json={
            "title": "Titulo Z",
            "description": None,
            "priority": "medium",
        },
    )
    assert r.status_code == 201
    tid = r.json()["id"]

    r_close = client.post(f"/tickets/{tid}/close")
    assert r_close.status_code == 200
    assert r_close.json()["status"] == "closed"

    # GET por id debe seguir funcionando (path feliz cubierto)
    r_get = client.get(f"/tickets/{tid}")
    assert r_get.status_code == 200
    assert r_get.json()["id"] == tid
