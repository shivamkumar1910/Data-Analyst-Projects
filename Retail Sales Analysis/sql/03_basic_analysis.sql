-- Basic KPI questions

SELECT COUNT(DISTINCT order_id) AS total_orders
FROM sales;

SELECT SUM(sales) AS total_sales
FROM sales;

SELECT SUM(profit) AS total_profit
FROM sales;

SELECT COUNT(DISTINCT customer_id) AS unique_customers
FROM sales;

SELECT AVG(order_value) AS avg_order_value
FROM (
    SELECT order_id, SUM(sales) AS order_value
    FROM sales
    GROUP BY order_id
) t;

SELECT AVG(quantity) AS avg_quantity_per_order
FROM sales;
