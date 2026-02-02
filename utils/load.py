# utils/load.py
from psycopg2.extras import execute_batch
from logger import get_logger
from db import get_connection

logger = get_logger("load")


def load_weather(df):
    logger.info("Starting load process")

    conn = get_connection()             #connection function to database
    cursor = conn.cursor()              # creating cussor to carry out taska

    # Insert locations (dimension table)
    location = df["city"].unique()         # creating unique Cities

    for city in location:                  #   Insert values into DIM table Location
        cursor.execute(
            """
            INSERT INTO dim_location (city)
            VALUES (%s)
            ON CONFLICT (city) DO NOTHING;
            """,
            (city,)
        )

    logger.info("Locations loaded")

   
    records = df.to_records(index=False)         # convert df into a list of tuples

    query = """
        INSERT INTO fact_weather_hourly
        (city, timestamp, temperature, humidity, windspeed, precipitation,
         is_raining, comfort_level, heat_index)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (city, timestamp) DO NOTHING;
    """

    execute_batch(cursor, query, records)               # execute cursor, query, and records

    conn.commit()                                       # save result

    logger.info(f"Loaded {len(df)} weather records")

    cursor.close()
    conn.close()
