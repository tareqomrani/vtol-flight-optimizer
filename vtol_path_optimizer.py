
import pandas as pd

def optimize_path(start_coords, end_coords, altitude):
    # Mock function: return two-point DataFrame
    return pd.DataFrame({
        'lat': [start_coords[0], end_coords[0]],
        'lon': [start_coords[1], end_coords[1]]
    })
