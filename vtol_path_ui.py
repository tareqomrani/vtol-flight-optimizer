import streamlit as st
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import folium
from streamlit_folium import st_folium

def geocode_address(address):
    geolocator = Nominatim(user_agent="vtol_app", timeout=10)
    try:
        location = geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
    except GeocoderTimedOut:
        return None
    return None

st.set_page_config(page_title="VTOL Flight Path Optimizer", layout="centered")
st.title("VTOL Flight Path Optimizer")

start_address = st.text_input("Enter start address", "Orlando, FL")
end_address = st.text_input("Enter end address", "Miami, FL")

start_coords = geocode_address(start_address)
end_coords = geocode_address(end_address)

if start_coords and end_coords:
    m = folium.Map(location=start_coords, zoom_start=6)
    folium.Marker(location=start_coords, popup="Start", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker(location=end_coords, popup="End", icon=folium.Icon(color="red")).add_to(m)
    folium.PolyLine(locations=[start_coords, end_coords], color="blue").add_to(m)
    st_folium(m, width=700, height=500)
else:
    st.error("Could not geocode one or both addresses. Please try again with valid US addresses.")