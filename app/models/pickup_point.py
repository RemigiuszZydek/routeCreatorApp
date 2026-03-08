from dataclasses import dataclass

@dataclass
class Pickup_Point:
    id: str
    address: str
    volume_m3: float
    status: str
    