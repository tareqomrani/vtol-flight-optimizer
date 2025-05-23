![VTOL Optimizer Banner](vtol_banner.png)

# VTOL Flight Path Optimizer

The VTOL Flight Path Optimizer is a Streamlit-based web app that allows users to simulate and plan low-altitude urban air routes. Designed with mobile users in mind, the app currently uses latitude and longitude input, but will soon support drag-and-drop route planning and address entry.

## Features

- Latitude and longitude-based route planning (address input and drag-and-drop coming soon)
- Cruise altitude selection
- Real-time path visualization
- Mobile-friendly interface
- Regulatory-aware routing (coming soon)

## How to Use

1. Open the app in your browser or mobile device.
2. Enter your start and end coordinates in decimal degrees (e.g., 28.538336, -81.379234).
3. Select your desired cruise altitude.
4. Click "Optimize Route" to view the suggested path.

## Tech Stack

- Python
- Streamlit
- Folium (Leaflet.js)
- Shapely & GeoPandas
- FAA dataset integration (in progress)

## FAA Dataset Integration

We are integrating FAA regulatory data to help users avoid **no-fly zones and restricted airspace**.

**Access the FAA shapefiles here:**

- [FAA Special Use Airspace Dataset (ArcGIS)](https://hub.arcgis.com/datasets/faa::special-use-airspace/about)
- [FAA National Security UAS Flight Restrictions](https://udds-faa.opendata.arcgis.com/datasets/faa::national-security-uas-flight-restrictions-1/about)

## License

MIT
