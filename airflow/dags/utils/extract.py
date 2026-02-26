# utils/extract.py
import requests
import time
import pandas as pd
from utils.logger import get_logger

logger = get_logger("extract")

API_URL = "https://api.open-meteo.com/v1/forecast"

LOCATIONS = [
    {"city": "Lagos", "lat": 6.5244, "lon": 3.3792},
    {"city": "London", "lat": 51.5074, "lon": -0.1278},
    {"city": "New York", "lat": 40.7128, "lon": -74.0060},
]

MAX_RETRIES = 3
RETRY_DELAY = 5


def extract_weather():
    all_data = []

    for loc in LOCATIONS:
        city = loc["city"]
        latitude = loc["lat"]
        longitude = loc["lon"]

        logger.info(f"Starting extraction for {city}")

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m,relativehumidity_2m,windspeed_10m,precipitation"
        }

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = requests.get(API_URL, params=params, timeout=10)
                response.raise_for_status()

                data = response.json()

                df = pd.DataFrame({
                    "city": city,
                    "timestamp": data["hourly"]["time"],
                    "temperature": data["hourly"]["temperature_2m"],
                    "humidity": data["hourly"]["relativehumidity_2m"],
                    "windspeed": data["hourly"]["windspeed_10m"],
                    "precipitation": data["hourly"]["precipitation"],
                })

                logger.info(f"{city}: Extracted {len(df)} records")
                all_data.append(df)
                break

            except Exception as e:
                logger.error(f"{city} attempt {attempt} failed: {e}")

                if attempt < MAX_RETRIES:
                    logger.info(f"{city}: Retrying in {RETRY_DELAY} seconds...")
                    time.sleep(RETRY_DELAY)
                else:
                    logger.error(f"{city}: All retries failed")
                    raise

    final_df = pd.concat(all_data, ignore_index=True)
    return final_df
