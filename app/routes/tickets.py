from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.schemas import Ticket, TicketCreate
from app.storage import store

# Organiza direcciones con sus endpoints

router = APIRouter(prefix="/tickets", tags=["tickets"])

# Endpoints

@router.post("/", response_model=Ticket, status_code=201)
def create_ticket(payload: TicketCreate) -> Ticket:
    return store.create(payload)


@router.get("/", response_model=list[Ticket])
def list_tickets() -> list[Ticket]:
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
