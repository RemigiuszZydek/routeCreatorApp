from app.models.route import Route, Stop, Trip

class PlannerService:
    def plan(self,vehicles, orders):
        routes = {v.id: Route(vehicle_id=v.id, trips=[]) for v in vehicles}
        vehicle_index = 0
        current_trip_stops = []
        current_volume = 0

        vehicle = vehicles[vehicle_index]

        for order in orders:

            order_volume = order.total_volume

            if current_volume + order_volume > vehicle.capacity_m3:

                trip = Trip(
                    stops = current_trip_stops,
                    total_volume=current_volume
                )

                routes[vehicle.id].trips.append(trip)

                vehicle_index = (vehicle_index + 1) %len(vehicles)
                vehicle = vehicle[vehicle_index]

                current_trip_stops = []
                current_volume = 0
            
            stop = Stop(
                order_id=order.id,
                address=order.address,
                volume=order_volume
            )
            
            current_trip_stops.append(stop)
            current_volume += order_volume

        if current_trip_stops:
            trip = Trip(
                stops=current_trip_stops,
                total_volume=current_volume
            )

            routes[vehicle.id].trips.append(trip)

        return list(routes.values())