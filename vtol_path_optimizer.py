
from shapely.geometry import LineString, Point
import numpy as np

def haversine(coord1, coord2):
    """
    Calculate the great-circle distance between two coordinates on Earth.
    """
    from math import radians, sin, cos, sqrt, atan2

    lat1, lon1 = coord1
    lat2, lon2 = coord2

    R = 6371e3  # Radius of Earth in meters
    phi1 = radians(lat1)
    phi2 = radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)

    a = sin(delta_phi/2)**2 + cos(phi1)*cos(phi2)*sin(delta_lambda/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c  # in meters

def generate_straight_line(start_coords, end_coords, num_points=50):
    """
    Generate a straight line path between two coordinates with `num_points` granularity.
    """
    lats = np.linspace(start_coords[0], end_coords[0], num_points)
    lons = np.linspace(start_coords[1], end_coords[1], num_points)
    return list(zip(lats, lons))

def optimize_path(start_coords, end_coords, cruise_altitude):
    """
    Optimizes a straight line path between start and end coordinates.
    Cruise altitude is currently not used in logic but can be integrated later.
    """
    path = generate_straight_line(start_coords, end_coords)
    distance = haversine(start_coords, end_coords)
    return {
        "path": path,
        "distance_m": distance,
        "cruise_altitude": cruise_altitude
    }
