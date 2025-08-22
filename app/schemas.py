from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class TicketCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)
    description: str | None = Field(None, max_length=20000)
    priority: Literal["low", "medium", "high"] = "medium"


class Ticket(TicketCreate):
    id: int
    status: Literal["open", "closed"] = "open"
