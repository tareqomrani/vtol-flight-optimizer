import geopandas as gpd
import streamlit as st
import folium
from streamlit_folium import st_folium

# Load FAA airspace shapefile
@st.cache_data
def load_airspace_data():
    return gpd.read_file("data/class_airspace.shp")

def main():
    st.title("Regulatory-Aware VTOL Flight Path Planning")

    st.markdown("This app displays FAA Class B, C, and D airspace boundaries.")

    # Load data
    airspace = load_airspace_data()

    # Convert to lat/lon and simplify for performance
    airspace = airspace.to_crs(epsg=4326)

    # Create map
    m = folium.Map(location=[39.8283, -98.5795], zoom_start=5)  # Center on USA

    # Plot airspace polygons
    folium.GeoJson(airspace).add_to(m)

    # Display map in Streamlit
    st_data = st_folium(m, width=700)

if __name__ == "__main__":
    main()