
import streamlit as st
from vtol_path_optimizer import optimize_path

st.set_page_config(layout="wide", page_title="VTOL Flight Path Optimizer")
st.title("VTOL Flight Path Optimizer")

st.markdown("Enter start and end coordinates as `lat,lon` (e.g. `37.7749,-122.4194`)")

start = st.text_input("Start Coordinates (lat,lon)", "37.7749,-122.4194")
end = st.text_input("End Coordinates (lat,lon)", "37.8044,-122.2711")
altitude = st.slider("Cruise Altitude (ft)", 200, 1000, 400)

if st.button("Optimize Route"):
    try:
        start_coords = tuple(map(float, start.split(',')))
        end_coords = tuple(map(float, end.split(',')))
        result = optimize_path(start_coords, end_coords, altitude)
        st.map(result)
    except Exception as e:
        st.error(f"Error: {e}")
