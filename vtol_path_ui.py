import streamlit as st
import folium
from streamlit_folium import st_folium
from shapely.geometry import LineString, Polygon
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

st.set_page_config(page_title="VTOL Flight Path Optimizer", layout="wide")
st.title("VTOL Flight Path Optimizer (Address Entry)")

geolocator = Nominatim(user_agent="vtol_planner")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

NO_FLY_ZONES = [
    Polygon([(-122.42, 37.77), (-122.41, 37.77), (-122.41, 37.78), (-122.42, 37.78)]),
    Polygon([(-122.39, 37.79), (-122.38, 37.79), (-122.38, 37.80), (-122.39, 37.80)])
]

with st.form("address_form"):
    st.subheader("Enter Start and End Addresses")
    start_addr = st.text_input("Start Address", "1600 Amphitheatre Parkway, Mountain View, CA")
    end_addr   = st.text_input("End Address", "1 Infinite Loop, Cupertino, CA")
    submitted  = st.form_submit_button("Plan Route")

if submitted:
    loc1 = geocode(start_addr)
    loc2 = geocode(end_addr)
    if not loc1 or not loc2:
        st.error("Could not geocode one or both addresses. Please refine them.")
    else:
        start = (loc1.latitude, loc1.longitude)
        end   = (loc2.latitude, loc2.longitude)

        path = LineString([start, end])
        blocked = any(zone.intersects(path) for zone in NO_FLY_ZONES)

        m = folium.Map(location=start, zoom_start=12)
        for zone in NO_FLY_ZONES:
            folium.Polygon(
                locations=[(lat, lon) for lon, lat in zone.exterior.coords],
                color="red", fill=True, fill_opacity=0.3
            ).add_to(m)

        folium.Marker(start, tooltip="Start", icon=folium.Icon(color="green")).add_to(m)
        folium.Marker(end, tooltip="End", icon=folium.Icon(color="blue")).add_to(m)
        folium.PolyLine(locations=[start, end],
                        color="green" if not blocked else "orange",
                        weight=4, opacity=0.8).add_to(m)

        st.subheader("Route Result")
        st_folium(m, height=500)
        st.info("⚠️ Path intersects a no-fly zone!" if blocked else "✅ Path is clear.")