import streamlit as st
from vtol_path_optimizer import optimize_path  # Assuming your logic is in this module

st.set_page_config(page_title="VTOL Flight Path Optimizer", layout="centered")

st.title("VTOL Flight Path Optimizer")

st.markdown("Enter the coordinates below to optimize your VTOL flight path.")

def parse_coords(label):
    coord_input = st.text_input(f"Enter {label} coordinates (format: `latitude,longitude`):")
    if coord_input:
        try:
            lat_str, lon_str = coord_input.strip().split(',')
            return float(lat_str.strip()), float(lon_str.strip())
        except Exception:
            st.error(f"Invalid {label} coordinates. Use the format: `latitude,longitude` (e.g., `34.0522,-118.2437`).")
            st.stop()
    return None

start_coords = parse_coords("start")
end_coords = parse_coords("end")

if start_coords and end_coords:
    if st.button("Optimize Flight Path"):
        with st.spinner("Calculating optimal path..."):
            try:
                optimized_route = optimize_path(start_coords, end_coords)

                st.success("Flight path optimized!")
                st.write("Optimized Route Coordinates:")
                st.code(str(optimized_route))

                # Optionally display on a map if you have lat/lon pairs
                try:
                    st.map(data={"lat": [pt[0] for pt in optimized_route],
                                 "lon": [pt[1] for pt in optimized_route]})
                except Exception:
                    st.warning("Map view skipped: output format may not be suitable for plotting.")
            except Exception as e:
                st.error("An error occurred while optimizing the flight path.")
                st.exception(e)
