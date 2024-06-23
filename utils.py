import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()
api_key = os.getenv("MAPS_API_KEY")
address = os.getenv("ADDRESS")


def get_coordinates(address, api_key):
    """Fetch lat/lng coordinates for a specific address using Google Maps API"""
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": api_key}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            location = results[0]["geometry"]["location"]
            return location["lat"], location["lng"]
        else:
            print("Failed to fetch coordinates.")
    else:
        print("Error:", response.status_code, response.text)


# Dictionary of weather codes and descriptions
weather_code_descriptions = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Drizzle: Light",
    53: "Drizzle: Moderate",
    55: "Drizzle: Dense",
    56: "Freezing Drizzle: Light",
    57: "Freezing Drizzle: Dense",
    61: "Rain: Slight",
    63: "Rain: Moderate",
    65: "Rain: Heavy",
    66: "Freezing Rain: Light",
    67: "Freezing Rain: Heavy",
    71: "Snow: Slight",
    73: "Snow: Moderate",
    75: "Snow: Heavy",
    77: "Snow Grains",
    80: "Showers: Slight",
    81: "Showers: Moderate",
    82: "Showers: Violent",
    85: "Snow Showers: Slight",
    86: "Snow Showers: Heavy",
    95: "Thunderstorm: Slight or Moderate",
    96: "Thunderstorm with Hail: Slight",
    99: "Thunderstorm with Hail: Heavy",
}


def validate_date_format(date_str):
    """Validate date format DD-MM-YYYY."""
    try:
        return pd.to_datetime(date_str, format="%d-%m-%Y")
    except ValueError:
        raise ValueError(f"Date {date_str} is not in the correct format DD-MM-YYYY.")
