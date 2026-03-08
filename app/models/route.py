from dataclasses import dataclass
from typing import List
from datetime import datetime
from .route_point import Route_Point

@dataclass
class Route:
    id:str
    vehicle_id: str
    start_time: datetime
    end_time: datetime
    distance_km: float
    total_volume_m3: float
    points: List[Route_Point]