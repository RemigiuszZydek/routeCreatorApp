from sqlalchemy import Column, Integer,ForeignKey
from .base import Base


class RoutePoint(Base):
    __tablename__ = "route_points"
    id = Column(Integer, primary_key=True, autoincrement=True)
    route_id = Column(Integer, ForeignKey("routes.id"), nullable=False)
    pickup_point_id = Column(Integer, ForeignKey("pickup_points.id"), nullable=False)
    order = Column(Integer, nullable=False)