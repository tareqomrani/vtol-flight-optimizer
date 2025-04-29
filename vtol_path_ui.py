import streamlit as st
import folium
from streamlit_folium import st_folium
from shapely.geometry import Point, Polygon

st.set_page_config(page_title="VTOL Flight Path Optimizer", layout="wide")
st.title("VTOL Flight Path Optimizer (Urban Routing)")

CITY_BOUNDS = [[37.75, -122.45], [37.85, -122.35]]  # SF example bounds
NO_FLY_ZONES = [
    Polygon([(-122.42, 37.77), (-122.41, 37.77), (-122.41, 37.78), (-122.42, 37.78)]),
    Polygon([(-122.39, 37.79), (-122.38, 37.79), (-122.38, 37.80), (-122.39, 37.80)])
]

m = folium.Map(location=[37.78, -122.41], zoom_start=14)
for zone in NO_FLY_ZONES:
    folium.Polygon(locations=[(lat, lon) for lon, lat in zone.exterior.coords], color='red').add_to(m)

st.markdown("**Click two points on the map to simulate a VTOL route.**")
map_data = st_folium(m, height=500, returned_objects=["last_clicked"])

if "start" not in st.session_state:
    st.session_state.start = None

if map_data["last_clicked"]:
    point = map_data["last_clicked"]
    latlng = (point["lat"], point["lng"])
    if not st.session_state.start:
        st.session_state.start = latlng
        st.success(f"Start point set at {latlng}")
    else:
        end = latlng
        start = st.session_state.start
        st.session_state.start = None

        # Route check
        path = [start, end]
        path_line = Polygon([start, end])
        blocked = any(zone.intersects(path_line) for zone in NO_FLY_ZONES)

        m = folium.Map(location=start, zoom_start=14)
        for zone in NO_FLY_ZONES:
            folium.Polygon(locations=[(lat, lon) for lon, lat in zone.exterior.coords], color='red').add_to(m)
        folium.Marker(start, tooltip="Start").add_to(m)
        folium.Marker(end, tooltip="End").add_to(m)
        folium.PolyLine(locations=[start, end], color='green' if not blocked else 'orange').add_to(m)

        st.subheader("Flight Path Result")
        st_folium(m, height=500)
        st.info("Path intersects a no-fly zone!" if blocked else "Path is clear.")