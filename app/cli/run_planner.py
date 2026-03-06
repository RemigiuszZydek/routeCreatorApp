import json

from app.models.vehicle import Vehicle
from app.models.order import Order
from app.services.planner_service import PlannerService
from app.solver.vrp_solver import VRPSovler
from app.solver.data_model import DataModel

def load_vehicles():
    with open("data/vehicles.json") as f:
        data = json.load(f)

    return [Vehicle(**v) for v in data]

def load_orders():
    with open("data/orders.json") as f:
        data = json.load(f)

    return [Order(**o) for o in data]


def main():
    vehicles_data = [
    {"id": "v1", "registration": "KR10001", "capacity_m3": 5},
    {"id": "v2", "registration": "KR10002", "capacity_m3": 5},
]
    orders_data = [
    {"id": "o1",  "address": "Katowice 1",  "bags": 10, "bag_volume_m3": 0.3, "lat":50.259, "lon":19.025},
    {"id": "o2",  "address": "Katowice 2",  "bags": 8,  "bag_volume_m3": 0.25,"lat":50.261, "lon":19.030},
    {"id": "o3",  "address": "Katowice 3",  "bags": 12, "bag_volume_m3": 0.2, "lat":50.263, "lon":19.028},
    {"id": "o4",  "address": "Katowice 4",  "bags": 6,  "bag_volume_m3": 0.4, "lat":50.264, "lon":19.020},
    {"id": "o5", "address": "Katowice 5", "bags": 15, "bag_volume_m3": 0.1, "lat":50.262, "lon":19.018}, 
   
]
    
    vehicles = [Vehicle(**v) for v in vehicles_data]
    orders = [Order(**o) for o in orders_data]

    data_model = DataModel(vehicles,orders)

    data = data_model.build()
    
    solver = VRPSovler()

    routes = solver.solve(data)

    print(routes)
  


if __name__ == "__main__":
    main()