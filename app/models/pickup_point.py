from sqlalchemy import Column, Integer, Float, String
from .base import Base


class PickupPoint(Base):
    __tablename__ = "pickup_points"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    address = Column(String, nullable=False)
    volume_m3 = Column(Float, nullable=False)
    status = Column(String,nullable=False)
    