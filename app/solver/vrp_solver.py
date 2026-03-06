from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

class VRPSovler:

    def get_routes(self,data, manager, routing, solution):
        
        routes = []

        for vehicle_id in range(data["num_vehicles"]):

            index = routing.Start(vehicle_id)

            route = []

            while not routing.IsEnd(index):

                node = manager.IndexToNode(index)

                route.append(node)

                index = solution.Value(routing.NextVar(index))

            routes.append(route)
        
        return routes

    def solve(self, data):

        manager = pywrapcp.RoutingIndexManager(
            len(data["distance_matrix"]),
            data["num_vehicles"],
            data["depot"]
        )

        routing = pywrapcp.RoutingModel(manager)

        def distnace_callback(from_index, to_index):
            
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)

            return data["distance_matrix"][from_node][to_node]
        
        transit_callback_index = routing.RegisterTransitCallback(distnace_callback)

        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        def demand_callback(from_index):

            from_node = manager.IndexToNode(from_index)
            return int(data["demands"][from_node] * 1000)
        
        demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)

        routing.AddDimensionWithVehicleCapacity(
            demand_callback_index,
            0,
            [int(c * 1000) for c in data["vehicle_capacities"]],
            True,
            "Capacity"
        )

        search_parameters = pywrapcp.DefaultRoutingSearchParameters()

        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
        )

        solution = routing.SolveWithParameters(search_parameters)

        if solution:
            return self.get_routes(data, manager, routing, solution)

        return None
    
    