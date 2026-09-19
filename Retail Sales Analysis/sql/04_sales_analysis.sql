-- Regional, category, and time sales analysis

SELECT region, SUM(sales) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

SELECT category, SUM(sales) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

SELECT sub_category, SUM(sales) AS total_sales
FROM sales
GROUP BY sub_category
ORDER BY total_sales DESC
LIMIT 10;

SELECT EXTRACT(YEAR FROM order_date) AS year, SUM(sales) AS total_sales
FROM sales
GROUP BY EXTRACT(YEAR FROM order_date)
ORDER BY year;

SELECT EXTRACT(MONTH FROM order_date) AS month_number, SUM(sales) AS total_sales
FROM sales
GROUP BY EXTRACT(MONTH FROM order_date)
ORDER BY month_number;

SELECT EXTRACT(MONTH FROM order_date) AS month_number,
       TO_CHAR(MIN(order_date), 'Month') AS month_name,
       SUM(sales) AS total_sales
FROM sales
GROUP BY EXTRACT(MONTH FROM order_date)
ORDER BY month_number;

SELECT EXTRACT(MONTH FROM order_date) AS month_number,
       TO_CHAR(MIN(order_date), 'Month') AS month_name,
       SUM(sales) AS total_sales
FROM sales
GROUP BY EXTRACT(MONTH FROM order_date)
ORDER BY month_number;
