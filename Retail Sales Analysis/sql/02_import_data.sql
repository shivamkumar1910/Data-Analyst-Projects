-- Load the cleaned CSV into the sales table.
-- Update the file path if needed depending on your PostgreSQL setup.

COPY sales (
    row_id,
    order_id,
    order_date,
    ship_date,
    ship_mode,
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region,
    product_id,
    category,
    sub_category,
    product_name,
    sales,
    quantity,
    discount,
    profit
)
FROM 'C:/Users/Dell/Documents/Github/Data Analyst Projects/Retail-Sales-Analysis/data/cleaned/superstore_cleaned.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ','
);

SELECT COUNT(*) AS total_rows FROM sales;
