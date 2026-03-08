from dataclasses import dataclass

@dataclass
class Vehicle:
    id: str
    model: str
    capacity_m3 : float
    max_weight_kg : float
    