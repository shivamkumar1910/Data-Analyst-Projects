-- PostgreSQL profit and product analysis

SELECT region, SUM(profit) AS total_profit
FROM sales
GROUP BY region
ORDER BY total_profit DESC;

SELECT category, SUM(profit) AS total_profit
FROM sales
GROUP BY category
ORDER BY total_profit DESC;

SELECT sub_category, SUM(profit) AS total_profit
FROM sales
GROUP BY sub_category
ORDER BY total_profit ASC
LIMIT 10;

SELECT product_name, SUM(sales) AS total_sales
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;

SELECT product_name, SUM(profit) AS total_profit
FROM sales
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 10;

SELECT product_name, SUM(profit) AS total_profit
FROM sales
GROUP BY product_name
ORDER BY total_profit ASC
LIMIT 10;

SELECT EXTRACT(MONTH FROM order_date) AS month_number,
       TO_CHAR(MIN(order_date), 'Month') AS month_name,
       SUM(profit) AS total_profit
FROM sales
GROUP BY EXTRACT(MONTH FROM order_date)
ORDER BY month_number;
