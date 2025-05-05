import streamlit as st
import folium
from streamlit_folium import st_folium
from vtol_path_optimizer import optimize_path

st.set_page_config(page_title="VTOL Flight Path Optimizer", layout="wide")
st.title("VTOL Flight Path Optimizer")

with st.form("input_form"):
    start = st.text_input("Start Coordinates (lat, lon)", "28.538336, -81.379234")
    end = st.text_input("End Coordinates (lat, lon)", "28.602427, -81.200057")
    altitude = st.slider("Cruise Altitude (ft)", 500, 5000, 1500)
    submitted = st.form_submit_button("Optimize Route")

if submitted:
    try:
        start_coords = tuple(map(float, start.split(',')))
        end_coords = tuple(map(float, end.split(',')))
        path = optimize_path(start_coords, end_coords, altitude)

        m = folium.Map(location=start_coords, zoom_start=12)
        folium.Marker(start_coords, tooltip="Start").add_to(m)
        folium.Marker(end_coords, tooltip="End").add_to(m)
        folium.PolyLine(locations=[(pt[1], pt[0]) for pt in path.coords], color="blue").add_to(m)
        st_folium(m, width=700, height=500)
    except Exception as e:
        st.error(f"Error: {str(e)}")
