from sqlalchemy import Column, Integer, Float, String
from .base import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    car_registration = Column(String, nullable=False)
    capacity_m3 = Column(Float, nullable=False)
    max_weight_kg = Column(Float, nullable=True)

    