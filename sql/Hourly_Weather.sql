

-- create database
CREATE DATABASE Hourly_Weather;

-- Create dimension table: Cities
CREATE TABLE IF NOT EXISTS location (
    city VARCHAR(100) PRIMARY KEY
);

-- Create fact table: Hourly weather
CREATE TABLE IF NOT EXISTS weather_hourly (
    city VARCHAR(100) REFERENCES location(city),
    timestamp TIMESTAMPTZ NOT NULL,
    temperature REAL,
    humidity REAL,
    windspeed REAL,
    precipitation REAL,
    is_raining BOOLEAN,
    comfort_level VARCHAR(20),
    heat_index REAL,
    PRIMARY KEY (city, timestamp)
);



