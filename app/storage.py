from __future__ import annotations

from .schemas import Ticket, TicketCreate


class InMemoryTicketStore:
    def __init__(self) -> None:
        self._data: dict[int, Ticket] = {}
        self._seq = 0

    # Convierte los datos en diccionario con model_dump() y los vuelve argumentos con **
    def create(self, payload: TicketCreate) -> Ticket:
        self._seq += 1
        t = Ticket(id=self._seq, **payload.model_dump())
        self._data[t.id] = t
        return t

    def list(self) -> list[Ticket]:
        return list(self._data.values())

    def get(self, ticket_id: int) -> Ticket | None:
        return self._data.get(ticket_id)

    def close(self, ticket_id: int) -> Ticket | None:
        t = self._data.get(ticket_id)
        if t:
            t.status = "closed"
        return t


store = InMemoryTicketStore()
