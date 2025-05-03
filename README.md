# Regulatory-Aware VTOL Flight Path Optimizer

This module demonstrates how to visualize and plan VTOL routes while avoiding restricted FAA airspace using shapefiles for Class B, C, and D airspaces.

## Features
- FAA shapefile loading
- Interactive map display
- Ready for integration into a full optimizer app

## Setup
1. Place the FAA shapefiles in the `data/` directory (create this folder if needed).
2. Run the Streamlit app using:
```bash
streamlit run regulatory_aware_vtol.py
```

## Notes
- You can download FAA shapefiles [here](https://adds-faa.opendata.arcgis.com/datasets/class-airspace).