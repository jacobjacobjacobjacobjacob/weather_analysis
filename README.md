Weather Data Analysis
This repository contains scripts for fetching, cleaning, and analyzing historical weather data. The data is retrieved from the OpenMeteo API and processed to provide insightful statistics regarding temperature, rainfall, snowfall, and daylight duration. Below is a summary of the main functionalities of the provided scripts.

Files
weather_data.py
This script fetches historical weather data from the OpenMeteo API and processes it into clean, structured data suitable for analysis.

Main Functions:
get_weather_data(start_date, end_date):

Fetches weather data for the specified coordinates and time period.
Parameters: start_date (YYYY-MM-DD), end_date (YYYY-MM-DD).
Returns: JSON response with weather data.
create_weather_dataframes(df):

Separates daily and hourly weather data.
Parameters: df (JSON response from get_weather_data).
Returns: Two pandas DataFrames (daily_df, hourly_df).
change_weather_descriptions(df):

Converts weather codes to descriptive weather conditions.
Parameters: df (DataFrame containing weather data).
Returns: DataFrame with weather descriptions.
clean_weather_data(df):

Cleans and formats the weather data, including renaming columns and converting date formats.
Parameters: df (DataFrame containing weather data).
Returns: Cleaned DataFrame.
weather_analysis.py
This script contains functions to analyze the cleaned weather data, providing monthly statistics for various weather parameters.

Main Functions:
temperature_by_month(df):

Calculates monthly statistics for temperature.
Parameters: df (DataFrame containing daily weather data).
Returns: DataFrame with monthly temperature statistics.
rain_by_month(df):

Calculates monthly statistics for rainfall.
Parameters: df (DataFrame containing daily weather data).
Returns: DataFrame with monthly rainfall statistics.
snow_by_month(df):

Calculates monthly statistics for snowfall.
Parameters: df (DataFrame containing daily weather data).
Returns: DataFrame with monthly snowfall statistics.
daylight_by_month(df):

Calculates monthly statistics for daylight duration.
Parameters: df (DataFrame containing daily weather data).
Returns: DataFrame with monthly daylight statistics.
merge_monthly_stats(df):

Merges all monthly statistics into a single DataFrame.
Parameters: df (DataFrame containing daily weather data).
Returns: DataFrame with merged monthly statistics.
get_all_monthly_stats(df):

Returns separate DataFrames for each weather parameter and a merged DataFrame with all statistics.
Parameters: df (DataFrame containing daily weather data).
Returns: Four DataFrames (temp_df, rain_df, snow_df, merged_df).
