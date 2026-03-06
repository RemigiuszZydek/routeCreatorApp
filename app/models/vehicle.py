from pydantic import BaseModel

class Vehicle(BaseModel):
    id: str
    registration: str
    capacity_m3: float
    