CREATE TABLE dim_location (
    location_id INT PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    longitude DOUBLE PRECISION NOT NULL,
    latitude DOUBLE PRECISION NOT NULL
);

CREATE TABLE fact_weather (
    id INT PRIMARY KEY,
    location_id INT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    temperature DOUBLE PRECISION,
    humidity DOUBLE PRECISION,
    windspeed DOUBLE PRECISION,
    CONSTRAINT fk_location
        FOREIGN KEY (location_id)
        REFERENCES dim_location(location_id)
);
