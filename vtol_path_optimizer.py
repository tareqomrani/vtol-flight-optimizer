from shapely.geometry import LineString

def optimize_path(start_coords, end_coords, altitude):
    return LineString([start_coords, end_coords])
