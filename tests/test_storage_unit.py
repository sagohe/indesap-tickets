from __future__ import annotations
from app.storage import InMemoryTicketStore
from app.schemas import TicketCreate

def test_storage_get_not_found() -> None:
    s = InMemoryTicketStore()
    assert s.get(12345) is None  # rama de None

def test_storage_close_not_found() -> None:
    s = InMemoryTicketStore()
    assert s.close(12345) is None  # rama de None

def test_storage_full_cycle() -> None:
    s = InMemoryTicketStore()
    t = s.create(TicketCreate(title="Alpha", description=None, priority="medium"))
    all_ = s.list()
    assert len(all_) == 1
    closed = s.close(t.id)
    assert closed and closed.status == "closed"
