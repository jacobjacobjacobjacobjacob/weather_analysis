import pandas as pd
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

"""
Functions to perform everything to do with analysing the weather data
"""


def temperature_by_month(df):
    """Temperature (C) sorted by month"""
    df["month"] = pd.Categorical(df["month"], categories=months, ordered=True)

    # Group by 'month' and calculate max and mean for 'temp_max' and 'temp_mean'
    monthly_stats = (
        df.groupby("month")
        .agg({"temp_max": "max", "temp_mean": "mean", "temp_min": "min"})
        .reset_index()
    )

    monthly_stats["temp_mean"] = monthly_stats["temp_mean"].round(1)

    return monthly_stats


def rain_by_month(df):
    """Rain (mm) sorted by month"""
    df["month"] = pd.Categorical(df["month"], categories=months, ordered=True)

    monthly_stats = (
        df.groupby("month").agg({"rain_sum": ["max", "mean", "sum"]}).reset_index()
    )

    monthly_stats.columns = ["month", "max_rain", "mean_rain", "sum_rain"]  # Flatten
    monthly_stats["mean_rain"] = monthly_stats["mean_rain"].round(1)

    return monthly_stats


def snow_by_month(df):
    """Snow (mm) sorted by month"""
    df["month"] = pd.Categorical(df["month"], categories=months, ordered=True)

    monthly_stats = (
        df.groupby("month").agg({"snowfall_sum": ["max", "mean", "sum"]}).reset_index()
    )

    monthly_stats.columns = [
        "month",
        "max_snowfall",
        "mean_snowfall",
        "sum_snowfall",
    ]  # Flatten
    monthly_stats["mean_snowfall"] = monthly_stats["mean_snowfall"].round(1)
    return monthly_stats


def daylight_by_month(df):
    """Daylight hours sorted by month"""
    df["month"] = pd.Categorical(df["month"], categories=months, ordered=True)

    monthly_stats = (
        df.groupby("month")
        .agg({"daylight_hours": ["max", "mean", "sum"]})
        .reset_index()
    )

    monthly_stats.columns = [
        "month",
        "max_daylight",
        "mean_daylight",
        "sum_daylight",
    ]  # Flatten
    monthly_stats["mean_daylight"] = monthly_stats["mean_daylight"].round(1)

    return monthly_stats


def merge_monthly_stats(df):
    """Returns a merged dataframe of all the monthly stats"""
    temp_df = temperature_by_month(df)
    rain_df = rain_by_month(df)
    snow_df = snow_by_month(df)
    daylight_df = daylight_by_month(df)

    # Merge the DataFrames on the 'month' column
    merged_df = (
        temp_df.merge(rain_df, on="month")
        .merge(snow_df, on="month")
        .merge(daylight_df, on="month")
    )

    return merged_df


def get_all_monthly_stats(df):
    """Returns dataframes with all the monthly stats"""
    temp_df = temperature_by_month(df)
    rain_df = rain_by_month(df)
    snow_df = snow_by_month(df)
    daylight_df = daylight_by_month(df)

    merged_df = (
        temp_df.merge(rain_df, on="month")
        .merge(snow_df, on="month")
        .merge(daylight_df, on="month")
    )

    return temp_df, rain_df, snow_df, merged_df


if __name__ == "__main__":
    print("weather_analysis.py")

    # Read data
    daily_data_filename = "weather_day.csv"
    hourly_data_filename = "weather_hour.csv"

    daily_df = pd.read_csv(f"datasets/{daily_data_filename}")
    hourly_df = pd.read_csv(f"datasets/{hourly_data_filename}")

    months = [
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec",
    ]

    temp_df, rain_df, snow_df, merged_df = get_all_monthly_stats(daily_df)

    # print(temp_df.head())
    # print(rain_df.head())
    # print(snow_df.head())
    # print(merged_df.head())
