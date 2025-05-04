
import streamlit as st
from vtol_path_optimizer import optimize_path

st.title("VTOL Flight Path Optimizer")

# User input for coordinates and cruise altitude
start_coords_input = st.text_input("Start Coordinates (lat, lon)", "28.5383, -81.3792")
end_coords_input = st.text_input("End Coordinates (lat, lon)", "25.7617, -80.1918")
cruise_altitude = st.number_input("Cruise Altitude (meters)", value=500)

if st.button("Optimize Flight Path"):
    try:
        # Convert string inputs to tuples of floats
        start_coords = tuple(map(float, start_coords_input.split(',')))
        end_coords = tuple(map(float, end_coords_input.split(',')))
        
        # Call optimization function
        result = optimize_path(start_coords, end_coords, cruise_altitude)
        
        # Display results
        st.success(f"Distance: {result['distance_m']:.2f} meters")
        st.write(f"Cruise Altitude: {result['cruise_altitude']} meters")
        
        # Show path as map
        st.map({
            "lat": [coord[0] for coord in result["path"]],
            "lon": [coord[1] for coord in result["path"]]
        })

    except Exception as e:
        st.error(f"An error occurred: {e}")
