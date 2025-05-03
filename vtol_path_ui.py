
import streamlit as st
import pydeck as pdk
from routing import get_optimized_path
from weather_utils import fetch_weather_data

st.set_page_config(page_title="VTOL Flight Optimizer", layout="wide")
st.title("VTOL Flight Path Optimizer")

start = st.text_input("Start (lat, lon)", "28.5383, -81.3792")
end = st.text_input("End (lat, lon)", "28.3852, -81.5639")
altitude = st.slider("Cruise Altitude (meters)", 100, 500, 300)
use_weather = st.checkbox("Optimize using real-time weather data", value=True)

if st.button("Optimize Path"):
    start_coords = tuple(map(float, start.split(',')))
    end_coords = tuple(map(float, end.split(',')))

    path = get_optimized_path(start_coords, end_coords, altitude, use_weather)

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=(start_coords[0] + end_coords[0]) / 2,
            longitude=(start_coords[1] + end_coords[1]) / 2,
            zoom=10,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "PathLayer",
                data=[{"path": path, "name": "VTOL Route"}],
                get_path="path",
                get_color=[0, 0, 255],
                width_scale=20,
                width_min_pixels=2,
                get_width=5,
                pickable=True,
            )
        ],
    ))
