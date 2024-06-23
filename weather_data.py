from utils import get_coordinates, address, api_key, weather_code_descriptions
import requests
import pandas as pd

"""
Fetch historical weather data from the OpenMeteo API.
"""


def get_weather_data(start_date, end_date):
    """Returns weather data for the specified coordinates and period"""
    lat, lng = get_coordinates(address, api_key)
    print(f"Coordinates retrieved successfully.\nLat: {lat} Lng: {lng}")
    base_url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lng,
        "start_date": start_date,
        "end_date": end_date,
        "daily": [
            "weather_code",
            "temperature_2m_max",
            "temperature_2m_min",
            "temperature_2m_mean",
            "rain_sum",
            "snowfall_sum",
            "wind_speed_10m_max",
            "daylight_duration",
        ],
        "hourly": [
            "temperature_2m",
            "rain",
            "snowfall",
            "weather_code",
            "wind_speed_10m",
        ],
        "wind_speed_unit": "ms",
        "timezone": "Europe/Berlin",
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        print("API call completed.")
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None


def create_weather_dataframes(df):
    if not isinstance(df, dict) or not df:
        raise ValueError("Weather data is not valid or empty.")

    # Separate daily/hourly data
    daily_data = df.get("daily", {})
    hourly_data = df.get("hourly", {})

    # Create DataFrames
    daily_df = pd.DataFrame(daily_data)
    hourly_df = pd.DataFrame(hourly_data)
    print("DataFrames created.")

    # Drop rows with NaN values
    daily_df = daily_df.dropna(how="any")
    hourly_df = hourly_df.dropna(how="any")
    print("NaN-values removed.")

    return daily_df, hourly_df


def change_weather_descriptions(df):
    """Change weather codes to weather descriptions for clarity"""

    # Change weather codes to weather description for clarity
    if "weather_code" in df.columns:
        df["weather_description"] = df["weather_code"].map(weather_code_descriptions)
        df["weather_description"] = df["weather_description"].str.lower()
        df = df.drop("weather_code", axis=1)
        print("Weather codes transformed successfully.")

    # Simplyfing the descriptions further
    df["weather_description"] = df["weather_description"].apply(
        lambda x: x.split(":", 1)[0].strip()
    )
    mapping = {"Mainly clear": "Clear", "Clear sky": "Clear", "Partly cloudy": "Cloudy"}

    df["weather_description"] = df["weather_description"].replace(mapping)
    df["weather_description"] = df["weather_description"].str.lower()

    return df


def clean_weather_data(df):
    # Convert daylight_duration from seconds to hours
    if "daylight_duration" in df.columns:
        df["daylight_duration"] = round(df["daylight_duration"] / 60 / 60, 1)

    # Rename columns if they exist
    columns_to_rename = {
        "temperature_2m": "temp",
        "temperature_2m_max": "temp_max",
        "temperature_2m_min": "temp_min",
        "temperature_2m_mean": "temp_mean",
        "wind_speed_10m": "wind_speed",
        "wind_speed_10m_max": "wind_max",
        "daylight_duration": "daylight_hours",
        "time": "date",
    }

    columns_to_rename = {k: v for k, v in columns_to_rename.items() if k in df.columns}
    df = df.rename(columns=columns_to_rename)
    print("Columns renamed. ")

    # Convert date to datetime format
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

        # Add columns for day of week, month and time of day
        df["day_of_week"] = df["date"].dt.strftime("%a").str.lower()
        df["month"] = df["date"].dt.strftime("%b").str.lower()
        if "temp" in df.columns:
            df["time_of_day"] = df["date"].dt.strftime("%H:%M")

        # Format date
        df["date"] = df["date"].dt.strftime("%Y-%m-%d")
        print("Dates split and converted.")

    return df


if __name__ == "__main__":
    start_date, end_date = ["2023-01-01", "2024-06-21"]  # YYYY-MM-DD
    weather_data = get_weather_data(start_date, end_date)
    weather_day, weather_hour = create_weather_dataframes(weather_data)

    weather_day = change_weather_descriptions(weather_day)
    weather_day = clean_weather_data(weather_day)
    weather_day.to_csv("datasets/weather_day.csv", index=False)

    weather_hour = change_weather_descriptions(weather_hour)
    weather_hour = clean_weather_data(weather_hour)
    weather_hour.to_csv("datasets/weather_hour.csv", index=False)

    pd.set_option("display.max_columns", None)  # Show all columns
    # pd.set_option('display.max_rows', None)  # Show all rows (optional)

    print(weather_day.head())
