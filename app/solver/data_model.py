from app.solver.distance_matrix import create_distance_matrix

class DataModel:
    def __init__(self, vehicles, orders, depot_index=0):
        self.vehicles = vehicles
        self.orders = orders

        self.depot_index = depot_index

        self.locations = []
        self.demands = []
        self.vehicle_capacities = []

    def build(self):

        self.locations.append((50.2649, 19.0238))

        for order in self.orders:
            self.locations.append(order.location)

        self.demands.append(0)

        for order in self.orders:
            self.demands.append(order.total_volume)

        for vehicle in self.vehicles:
            self.vehicle_capacities.append(vehicle.capacity_m3)

        distance_matrix = create_distance_matrix(self.locations)

        return {
            "locations": self.locations,
            "distance_matrix": distance_matrix,
            "demands": self.demands,
            "vehicle_capacities": self.vehicle_capacities,
            "num_vehicles": len(self.vehicles),
            "depot": self.depot_index
        }