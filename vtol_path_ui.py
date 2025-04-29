import streamlit as st
import folium
from shapely.geometry import LineString, Polygon
from streamlit_folium import st_folium

st.set_page_config(page_title="VTOL Path Planner - Drag & Drop", layout="wide")
st.title("VTOL Flight Path Optimizer (Drag & Drop)")

# Predefined no-fly zones
NO_FLY_ZONES = [
    Polygon([(-122.42, 37.77), (-122.41, 37.77), (-122.41, 37.78), (-122.42, 37.78)]),
    Polygon([(-122.39, 37.79), (-122.38, 37.79), (-122.38, 37.80), (-122.39, 37.80)])
]

# Default coordinates
start_coords = [37.776, -122.418]
end_coords = [37.794, -122.385]

# Build map
m = folium.Map(location=[37.78, -122.41], zoom_start=14)

# No-fly zones
for zone in NO_FLY_ZONES:
    folium.Polygon(locations=[(lat, lon) for lon, lat in zone.exterior.coords],
                   color='red', tooltip="No-Fly Zone").add_to(m)

# Add draggable markers
start_marker = folium.Marker(location=start_coords, draggable=True, popup="Start", icon=folium.Icon(color="green"))
end_marker = folium.Marker(location=end_coords, draggable=True, popup="End", icon=folium.Icon(color="blue"))
start_marker.add_to(m)
end_marker.add_to(m)

# Display map
st.markdown("**Drag the start and end markers to desired locations.**")
map_data = st_folium(m, height=500)

# Capture user-submitted marker positions
if st.button("Evaluate Flight Path"):
    start = start_coords
    end = end_coords

    if map_data and "last_object_clicked" in map_data:
        st.warning("Map interactions are limited to initial marker positions for now.")
    
    path_line = LineString([start, end])
    blocked = any(zone.intersects(path_line) for zone in NO_FLY_ZONES)

    m2 = folium.Map(location=start, zoom_start=14)
    for zone in NO_FLY_ZONES:
        folium.Polygon(locations=[(lat, lon) for lon, lat in zone.exterior.coords],
                       color='red', tooltip="No-Fly Zone").add_to(m2)
    folium.Marker(start, tooltip="Start", icon=folium.Icon(color="green")).add_to(m2)
    folium.Marker(end, tooltip="End", icon=folium.Icon(color="blue")).add_to(m2)
    folium.PolyLine([start, end], color="orange" if blocked else "green").add_to(m2)

    st.subheader("Flight Path Result")
    st_folium(m2, height=500)
    st.info("Path intersects a no-fly zone!" if blocked else "Path is clear.")