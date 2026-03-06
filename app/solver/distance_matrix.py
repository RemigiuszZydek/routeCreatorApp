import math

def haversine_distance(a,b):

    lat1, lon1 = a
    lat2, lon2 = b

    R = 6371

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (math.sin(dlat /2) ** 2
         + math.cos(math.radians(lat1))
         * math.cos(math.radians(lat2))
         * math.sin(dlon/2) ** 2)
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def create_distance_matrix(locations):

    matrix = []

    for from_node in locations:

        row = []

        for to_node in locations:

            distance = haversine_distance(from_node, to_node)

            row.append(int(distance))

        matrix.append(row)

    return matrix

