from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from utils.extract import extract_weather
from utils.transform import transform_weather
from utils.load import load_weather
from utils.logger import get_logger
from utils.db import get_connection
from utils.data_quality import validate_weather

logger = get_logger("airflow")

# name, number of retries and time delay before retries
default_args = {
    "owner": "weather_pipeline",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

def extract_task(**context):
    df = extract_weather()
    context["ti"].xcom_push(key="weather_df", value=df)     # extract_task and context to help pass data between tasks.

def transform_task(**context):
    df = context["ti"].xcom_pull(key="weather_df")
    df = transform_weather(df)
    context["ti"].xcom_push(key="weather_df", value=df)     # transform_task and context to help pass data between tasks.

def validate_task(**context):
    df = context["ti"].xcom_pull(key="weather_df")
    validate_weather(df)                                    # validate_task and context to help pass data between tasks.

def load_task(**context):
    df = context["ti"].xcom_pull(key="weather_df")
    conn = get_connection()
    load_weather(df, conn)
    conn.close()                                        # load_task and context to help pass data between tasks.

with DAG(
    dag_id="weather_etl_pipeline",
    start_date=datetime(2026, 2, 10),
    schedule_interval="@hourly",
    catchup=False,
    default_args=default_args,
    tags=["weather", "etl"],
) as dag:

    extract = PythonOperator(
        task_id="extract_weather",
        python_callable=extract_task,
        provide_context=True,
    )

    transform = PythonOperator(
        task_id="transform_weather",
        python_callable=transform_task,
        provide_context=True,
    )

    validate = PythonOperator(
        task_id="validate_weather",
        python_callable=validate_task,
        provide_context=True,
    )

    load = PythonOperator(
        task_id="load_weather",
        python_callable=load_task,
        provide_context=True,
    )

    # extract >> transform >> validate >> load
