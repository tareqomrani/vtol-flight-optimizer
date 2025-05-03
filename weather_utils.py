
import requests

def fetch_weather_data(start, end):
    lat, lon = start
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=windspeed_10m,winddirection_10m"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch weather data."}
    except Exception as e:
        return {"error": str(e)}
