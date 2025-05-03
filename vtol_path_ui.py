
import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
from shapely.geometry import LineString
import geopandas as gpd

st.set_page_config(page_title="VTOL Route Optimizer", layout="wide")

def geocode(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json"}
    response = requests.get(url, params=params)
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return float(data["lat"]), float(data["lon"])
    else:
        return None

st.title("VTOL Flight Path Optimizer")

start_address = st.text_input("Start Address", placeholder="Enter starting location")
end_address = st.text_input("End Address", placeholder="Enter destination")

if start_address and end_address:
    start_coords = geocode(start_address)
    end_coords = geocode(end_address)

    if start_coords and end_coords:
        st.success(f"Start: {start_coords}, End: {end_coords}")

        m = folium.Map(location=start_coords, zoom_start=13)
        folium.Marker(start_coords, tooltip="Start", icon=folium.Icon(color="green")).add_to(m)
        folium.Marker(end_coords, tooltip="End", icon=folium.Icon(color="red")).add_to(m)
        folium.PolyLine([start_coords, end_coords], color="blue", weight=4).add_to(m)

        st_folium(m, width=700, height=500)
    else:
        st.error("Could not find one or both addresses. Please try again.")
