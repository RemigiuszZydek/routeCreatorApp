import json

from app.models.vehicle import Vehicle
from app.models.order import Order
from app.services.planner_service import PlannerService

def load_vehicles():
    with open("data/vehicles.json") as f:
        data = json.load(f)

    return [Vehicle(**v) for v in data]

def load_orders():
    with open("data/orders.json") as f:
        data = json.load(f)

    return [Order(**o) for o in data]


def main():
    vehicles = load_vehicles()
    orders = load_orders()

    planner = PlannerService()

    routes = planner.plan(vehicles,orders)

    for route in routes:

        print()
        print("Vehicle:", route.vehicle_id)

        for i, trip in enumerate(route.trips):

            print(f"  Trip {i+1}")

            for stop in trip.stops:
                print("     Stop:", stop.address)

            print("     Volume:", trip.total_volume)


if __name__ == "__main__":
    main()