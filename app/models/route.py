from pydantic import BaseModel
from typing import List

class Stop(BaseModel):
    order_id: str
    address: str
    volume: float

class Route(BaseModel):
    vehicle_id: str
    stops: List[Stop]
    total_volume: float
    