from __future__ import annotations
import pytest
import responses
from requests import HTTPError

from sdk.indesap_client import IndesapClient

BASE = "http://example.com"


def test_client_sets_auth_header() -> None:
    c = IndesapClient(BASE, api_key="XYZ")
    assert c.session.headers.get("Authorization") == "Bearer XYZ"


@responses.activate
def test_client_get_ticket_and_list() -> None:
    c = IndesapClient(BASE)

    # get_ticket path feliz
    responses.add(
        responses.GET, f"{BASE}/tickets/1",
        json={"id": 1, "title": "A", "description": None, "priority": "medium", "status": "open"},
        status=200, content_type="application/json",
    )
    t = c.get_ticket(1)
    assert t.id == 1 and t.status == "open"

    # list_tickets con 2 elementos (cubre la compresión)
    responses.add(
        responses.GET, f"{BASE}/tickets/",
        json=[
            {"id": 1, "title": "A", "description": None, "priority": "medium", "status": "open"},
            {"id": 2, "title": "B", "description": "d", "priority": "high", "status": "closed"},
        ],
        status=200, content_type="application/json",
    )
    items = c.list_tickets()
    assert [i.id for i in items] == [1, 2]


@responses.activate
def test_client_create_raises_on_error() -> None:
    c = IndesapClient(BASE)

    # Fuerza un 400/500 para cubrir la rama donde raise_for_status() lanza
    responses.add(
        responses.POST, f"{BASE}/tickets/",
        json={"detail": "bad"}, status=400, content_type="application/json",
    )
    with pytest.raises(HTTPError):
        c.create_ticket("X", None, "high")
