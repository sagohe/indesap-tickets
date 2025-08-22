from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional, Literal

class TicketCreate(BaseModel):
    title: str=Field(...,min_length=3,max_length=200)
    description: Optional[str] = Field(None,max_length=20000)
    priority: Literal["low","medium","high"] = "medium"
    
class Ticket(TicketCreate):
    id : int
    status: Literal["open","closed"] = "open"