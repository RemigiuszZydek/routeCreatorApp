from pydantic import BaseModel

class Order(BaseModel):
    id: str
    address: str
    bags: int
    bag_volume_m3: float

    lat: float
    lon: float

    @property
    def total_volume(self):
        return self.bags * self.bag_volume_m3
    
    @property
    def location(self):
        return(self.lat, self.lon)