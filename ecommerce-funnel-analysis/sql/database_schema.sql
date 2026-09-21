-- PostgreSQL version
-- Create a table for the synthetic e-commerce event data
-- This table stores one row per customer event

CREATE TABLE IF NOT EXISTS ecommerce_events (
    event_id BIGSERIAL PRIMARY KEY,
    user_id INTEGER,
    session_id VARCHAR(255),
    event_date TIMESTAMP,
    event_type VARCHAR(50),
    product_id VARCHAR(50),
    device_type VARCHAR(50),
    traffic_source VARCHAR(100),
    country VARCHAR(100)
);

-- Import the CSV into PostgreSQL.
-- Run this from psql or pgAdmin after confirming the file path is correct.
\copy ecommerce_events (
    user_id,
    session_id,
    event_date,
    event_type,
    product_id,
    device_type,
    traffic_source,
    country
)
FROM 'C:/Users/Dell/Documents/Github/Data Analyst Projects/ecommerce-funnel-analysis/data/ecommerce_events.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ','
);

-- Optional check to confirm the table structure
SELECT *
FROM ecommerce_events
LIMIT 10;

SELECT COUNT(*) FROM ecommerce_events;
SELECT COUNT(DISTINCT user_id) FROM ecommerce_events;
SELECT event_type, COUNT(*) FROM ecommerce_events GROUP BY event_type;

