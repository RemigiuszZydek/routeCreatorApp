import json

from app.models.vehicle import Vehicle
from app.models.order import Order

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

    print("VEHICLES")
    print(vehicles)

    print()
    print("ORDERS")
    print(orders)


if __name__ == "__main__":
    main()