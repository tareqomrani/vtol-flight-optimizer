
import numpy as np

def get_optimized_path(start, end, altitude, use_weather=False):
    # Simple straight-line with altitude
    lat1, lon1 = start
    lat2, lon2 = end

    if use_weather:
        from weather_utils import fetch_weather_data
        wind = fetch_weather_data(start, end)
        print(f"Fetched wind data: {wind}")

    return [
        [lon1, lat1, altitude],
        [lon2, lat2, altitude]
    ]
