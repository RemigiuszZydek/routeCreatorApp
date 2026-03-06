from pydantic import BaseModel
from typing import List

class Stop(BaseModel):
    order_id: str
    address: str
    volume: float

class Trip(BaseModel):
    stops: List[Stop]
    total_volume: float
class Route(BaseModel):
    vehicle_id: str
    trips: List[Trip]




    