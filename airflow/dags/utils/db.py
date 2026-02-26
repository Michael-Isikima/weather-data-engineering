# utils/db.py
import psycopg2                 
import os
from dotenv import load_dotenv
from utils.logger import get_logger

logger = get_logger("db")           #logger function for logging

# Load environment variables
load_dotenv()                       # load env credentials


def get_connection():               # database connector function

        # env credentials for connecting to DB
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )

        logger.info("Database connection established")   # logger information when successful
        return conn

    except Exception as e:
        logger.error(f"Database connection failed: {e}") # logger information when unsuccessful
        raise                                              # Airflow stops programe
