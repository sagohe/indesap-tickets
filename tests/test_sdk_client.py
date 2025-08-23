from __future__ import annotations
import json
import responses
from sdk.indesap_client import IndesapClient

BASE = "http://example.com"

@responses.activate
def test_sdk_create_and_list_and_close() -> None:
    client = IndesapClient(BASE)

    # Mock create
    responses.add(
        responses.POST, f"{BASE}/tickets/",
        json={"id": 1, "title": "X", "description": None, "priority": "high", "status": "open"},
        status=201,
        content_type="application/json",
    )

    # Mock list
    responses.add(
        responses.GET, f"{BASE}/tickets/",
        json=[{"id": 1, "title": "X", "description": None, "priority": "high", "status": "open"}],
        status=200,
        content_type="application/json",
    )

    # Mock close
    responses.add(
        responses.POST, f"{BASE}/tickets/1/close",
        json={"id": 1, "title": "X", "description": None, "priority": "high", "status": "closed"},
        status=200,
        content_type="application/json",
    )

    t = client.create_ticket("X", None, "high")
    assert t.id == 1 and t.status == "open"

    items = client.list_tickets()
    assert len(items) == 1 and items[0].id == 1

    closed = client.close_ticket(1)
    assert closed.status == "closed"
