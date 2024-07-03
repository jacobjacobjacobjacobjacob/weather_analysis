# Weather Data Analysis

This repository contains scripts for fetching, cleaning, and analyzing historical weather data. The data is retrieved from the OpenMeteo API and processed to provide insightful statistics regarding temperature, rainfall, snowfall, and daylight duration. Below is a summary of the main functionalities of the provided scripts.

## Files

### `weather_data.py`
This script fetches historical weather data from the OpenMeteo API and processes it into clean, structured data suitable for analysis.

#### Main Functions:
1. **`get_weather_data(start_date, end_date)`**: 
   - Fetches weather data for the specified coordinates and time period.
   - Parameters: `start_date` (YYYY-MM-DD), `end_date` (YYYY-MM-DD).
   - Returns: JSON response with weather data.

2. **`create_weather_dataframes(df)`**:
   - Separates daily and hourly weather data.
   - Parameters: `df` (JSON response from `get_weather_data`).
   - Returns: Two pandas DataFrames (`daily_df`, `hourly_df`).

3. **`change_weather_descriptions(df)`**:
   - Converts weather codes to descriptive weather conditions.
   - Parameters: `df` (DataFrame containing weather data).
   - Returns: DataFrame with weather descriptions.

4. **`clean_weather_data(df)`**:
   - Cleans and formats the weather data, including renaming columns and converting date formats.
   - Parameters: `df` (DataFrame containing weather data).
   - Returns: Cleaned DataFrame.

### `weather_analysis.py`
This script contains functions to analyze the cleaned weather data, providing monthly statistics for various weather parameters.

#### Main Functions:
1. **`temperature_by_month(df)`**:
   - Calculates monthly statistics for temperature.
   - Parameters: `df` (DataFrame containing daily weather data).
   - Returns: DataFrame with monthly temperature statistics.

2. **`rain_by_month(df)`**:
   - Calculates monthly statistics for rainfall.
   - Parameters: `df` (DataFrame containing daily weather data).
   - Returns: DataFrame with monthly rainfall statistics.

3. **`snow_by_month(df)`**:
   - Calculates monthly statistics for snowfall.
   - Parameters: `df` (DataFrame containing daily weather data).
   - Returns: DataFrame with monthly snowfall statistics.

4. **`daylight_by_month(df)`**:
   - Calculates monthly statistics for daylight duration.
   - Parameters: `df` (DataFrame containing daily weather data).
   - Returns: DataFrame with monthly daylight statistics.

5. **`merge_monthly_stats(df)`**:
   - Merges all monthly statistics into a single DataFrame.
   - Parameters: `df` (DataFrame containing daily weather data).
   - Returns: DataFrame with merged monthly statistics.

6. **`get_all_monthly_stats(df)`**:
   - Returns separate DataFrames for each weather parameter and a merged DataFrame with all statistics.
   - Parameters: `df` (DataFrame containing daily weather data).
   - Returns: Four DataFrames (`temp_df`, `rain_df`, `snow_df`, `merged_df`).

## Usage

1. **Fetch and Clean Data**:
   - Run `weather_data.py` to fetch and clean weather data. The script will output two CSV files: `weather_day.csv` and `weather_hour.csv`.

2. **Analyze Data**:
   - Run `weather_analysis.py` to analyze the cleaned weather data. The script will provide monthly statistics for temperature, rainfall, snowfall, and daylight duration.

## Example

```python
# Fetching and cleaning data
start_date = "2023-01-01"
end_date = "2024-06-21"
weather_data = get_weather_data(start_date, end_date)
weather_day, weather_hour = create_weather_dataframes(weather_data)

weather_day = change_weather_descriptions(weather_day)
weather_day = clean_weather_data(weather_day)
weather_day.to_csv("datasets/weather_day.csv", index=False)

weather_hour = change_weather_descriptions(weather_hour)
weather_hour = clean_weather_data(weather_hour)
weather_hour.to_csv("datasets/weather_hour.csv", index=False)

# Analyzing data
daily_df = pd.read_csv("datasets/weather_day.csv")
temp_df, rain_df, snow_df, merged_df = get_all_monthly_stats(daily_df)

print(temp_df.head())
print(rain_df.head())
print(snow_df.head())
print(merged_df.head())
