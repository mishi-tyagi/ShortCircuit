from pydantic import BaseModel
from typing import List, Tuple

class Emergency(BaseModel):
    id: str
    type: str
    severity: int
    location: Tuple[int, int]
    time_active: int

class Unit(BaseModel):
    id: str
    type: str
    location: Tuple[int, int]
    available: bool

class DispatchAction(BaseModel):
    action: str
    unit_id: str
    emergency_id: str