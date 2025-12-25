## Global Weather Analytics Pipeline

This project involves building an automated weather data pipeline that collects hourly data from a public API, transforms and cleans it to ensure reliability, and stores it in a PostgreSQL database for efficient querying. The pipeline will be orchestrated using Apache Airflow, incorporating robust data quality checks, comprehensive logging, and error handling to maintain reliability and traceability. The entire project will be version-controlled with Git and GitHub, with CI/CD workflows in place to enable smooth, automated deployment and updates.

## Data source

    - Open-Meteo API

## Pipeline Features

    - Hourly extraction of weather data from Open-Meteo API

    - Transformation: clean, enrich, create derived columns (heat_index,    comfort_level, is_raining)

    - Loading into PostgreSQL with dimension & fact tables.

    - Automated Airflow DAG for orchestration

    - Logging and retry mechanisms for reliability

    - Data quality checks (validate temperature, humidity, timestamps)

    - Version control with Git/GitHub

    - CI/CD for testing and linting

## Folder Structure

    - weather-data-engineering/
        ├── dags/
        ├── utils/
        ├── sql/
        ├── scripts/
        ├── data/
        ├── docker/
        ├── README.md
        └── requirements.txt

## How to Run

## Further Enhancements.
