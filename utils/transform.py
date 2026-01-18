# utils/transform.py
import pandas as pd
from logger import get_logger 

logger = get_logger("transform")  #call logger function for logging


def transform_weather(df: pd.DataFrame) -> pd.DataFrame:     # transform function
    logger.info("Starting transformation process")

    
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)    # Converting timestamp

    # Drop rows with invalid timestamps
    before = len(df)
    df = df.dropna(subset=["timestamp"])
    logger.info(f"Dropped {before - len(df)} rows with invalid timestamps")

    # Filter unrealistic values
    df = df[
        (df["temperature"].between(-60, 60)) &
        (df["humidity"].between(0, 100)) &
        (df["windspeed"] >= 0) &
        (df["precipitation"] >= 0)
    ]

    logger.info(f"Records after cleaning: {len(df)}")

    
    df["is_raining"] = df["precipitation"] > 0          #is raining field when precipation > 0

    df["comfort_level"] = df["temperature"].apply(
        lambda x: "Cold" if x < 15 else "Hot" if x > 30 else "Comfortable"      #defining comfort level
    )

    df["heat_index"] = df["temperature"] + (df["humidity"] * 0.05)              # defining heat index

    logger.info("Transformation and enrichment completed")                      # logging results

    return df
