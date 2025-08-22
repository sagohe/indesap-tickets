from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import requests

TicketStatus = Literal["open", "closed"]
Priority = Literal["low", "medium", "high"]


@dataclass
class Ticket:
    id: int
    title: str
    description: str | None
    priority: Priority
    status: TicketStatus


class IndesapClient:
    def __init__(self, base_url: str, api_key: str | None = None, timeout: int = 10) -> None:
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "indesap-client/0.1.0"})
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})
        self.timeout = timeout

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def create_ticket(
        self, title: str, description: str | None = None, priority: Priority = "medium"
    ) -> Ticket:
        payload = {"title": title, "description": description, "priority": priority}
        r = self.session.post(self._url("/tickets/"), json=payload, timeout=self.timeout)
        if r.status_code != 201:
            print("ERROR DETALLE:", r.status_code, r.text)  # <-- verás el mensaje de validación
            r.raise_for_status()
        data = r.json()
        return Ticket(**data)

    def list_tickets(self) -> list[Ticket]:
        r = self.session.get(self._url("/tickets/"), timeout=self.timeout)
        r.raise_for_status()
        return [Ticket(**t) for t in r.json()]

    def get_ticket(self, ticket_id: int) -> Ticket:
        r = self.session.get(self._url(f"/tickets/{ticket_id}"), timeout=self.timeout)
        r.raise_for_status()
        return Ticket(**r.json())

    def close_ticket(self, ticket_id: int) -> Ticket:
        r = self.session.post(self._url(f"/tickets/{ticket_id}/close"), timeout=self.timeout)
        r.raise_for_status()
        return Ticket(**r.json())
