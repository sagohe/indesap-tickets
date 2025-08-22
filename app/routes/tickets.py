from __future__ import annotations

from fastapi import APIRouter, HTTPException

from ..schemas import Ticket, TicketCreate
from ..storage import store

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("/", response_model=Ticket, status_code=201)
def create_ticket(payload: TicketCreate) -> Ticket:
    return store.create(payload)


@router.get("/", response_model=list[Ticket])
def list_ticket() -> list[Ticket]:
    return store.list()


@router.get("/{ticket_id}", response_model=Ticket)
def get_ticket(ticket_id: int) -> Ticket:
    t = store.get(ticket_id)
    if not t:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return t


@router.post("/{ticket_id}/close", response_model=Ticket)
def close_ticket(ticket_id: int) -> Ticket:
    t = store.close(ticket_id)
    if not t:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return t
