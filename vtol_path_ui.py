
from vtol_path_optimizer import optimize_path

# Example start and end coordinates
start_coords = (28.5383, -81.3792)  # Orlando, FL
end_coords = (25.7617, -80.1918)    # Miami, FL

# Define cruise altitude in meters
cruise_altitude = 500

# Optimize the flight path
try:
    optimized_route = optimize_path(start_coords, end_coords, cruise_altitude)
    print("Optimized Route:")
    print(f"Distance: {optimized_route['distance_m']:.2f} meters")
    print(f"Cruise Altitude: {optimized_route['cruise_altitude']} meters")
    print("Path Coordinates:")
    for coord in optimized_route["path"]:
        print(coord)
except Exception as e:
    print("An error occurred while optimizing the flight path.")
    print(f"Error: {e}")
