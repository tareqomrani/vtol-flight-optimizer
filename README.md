![VTOL Optimizer Banner](./assets/vtol_banner.png)

# VTOL Flight Path Optimizer

The VTOL Flight Path Optimizer is a Streamlit-based web app that allows users to simulate and plan low-altitude urban air routes. Designed with mobile users in mind, the app allows you to select start and end coordinates via latitude and longitude input. A future update will allow drag-and-drop route planning and address entry on an interactive map.

## Features

- Latitude and longitude-based route input (drag-and-drop and address entry coming soon)
- Cruise altitude selection
- Real-time path visualization
- Mobile-friendly interface
- Regulatory-aware routing (coming soon)

## How to Use

1. Open the app in your browser or mobile device.
2. Enter the start and end coordinates (latitude and longitude).
3. Select your desired cruise altitude.
4. Click Optimize Route to view the suggested path.

## Tech Stack

- Python
- Streamlit
- Leaflet.js (via Streamlit components)
- Shapely & Geopandas
- FAA dataset integration (in progress)

## Future Enhancements

- Drag-and-drop route planning
- Address autocomplete input
- Real-time obstacle and weather integration
- Energy modeling
- Full regulatory dataset overlay
- Exportable flight plans

**Try it live**: [Your Streamlit App Link]  
**License**: MIT

## Notes
- FAA datasets are being integrated from [FAA Data Portal](https://www.faa.gov/data-research).
