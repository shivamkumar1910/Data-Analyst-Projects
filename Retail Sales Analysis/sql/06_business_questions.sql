-- Business Questions for Retail Sales Analysis
-- Each section includes the actual business question, SQL, and interpretation notes.

-- Question 1: Which region generates the highest sales?
SELECT region, SUM(sales) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC
LIMIT 1;
-- Business interpretation:
-- This helps the business identify where the strongest revenue is generated and where to focus sales support efforts.

-- Question 2: Which region generates the highest profit?
SELECT region, SUM(profit) AS total_profit
FROM sales
GROUP BY region
ORDER BY total_profit DESC
LIMIT 1;
-- Business interpretation:
-- This helps determine which region contributes most to profitability and where operations are most efficient.

-- Question 3: Which category generates the most sales?
SELECT category, SUM(sales) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC
LIMIT 1;
-- Business interpretation:
-- This highlights the category that drives the most revenue and can guide inventory and marketing priorities.

-- Question 4: Which category generates the most profit?
SELECT category, SUM(profit) AS total_profit
FROM sales
GROUP BY category
ORDER BY total_profit DESC
LIMIT 1;
-- Business interpretation:
-- This shows which category is most valuable in terms of margin and should be prioritized for product investment.

-- Question 5: Which products have the highest sales?
SELECT product_name, SUM(sales) AS total_sales
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;
-- Business interpretation:
-- These products are strong revenue drivers and may warrant promotional support or inventory expansion.

-- Question 6: Which products are generating the lowest profit?
SELECT product_name, SUM(profit) AS total_profit
FROM sales
GROUP BY product_name
ORDER BY total_profit ASC
LIMIT 10;
-- Business interpretation:
-- Low-profit products may require cost review, pricing adjustments, or removal from assortment.

-- Question 7: What are the monthly sales trends?
SELECT TO_CHAR(order_date, 'Month') AS month_name, SUM(sales) AS total_sales
FROM sales
GROUP BY TO_CHAR(order_date, 'Month'), EXTRACT(MONTH FROM order_date)
ORDER BY EXTRACT(MONTH FROM order_date);
-- Business interpretation:
-- This identifies seasonal patterns and helps with forecasting, staffing, and stock planning.

-- Question 8: What are the monthly profit trends?
SELECT TO_CHAR(order_date, 'Month') AS month_name, SUM(profit) AS total_profit
FROM sales
GROUP BY TO_CHAR(order_date, 'Month'), EXTRACT(MONTH FROM order_date)
ORDER BY EXTRACT(MONTH FROM order_date);
-- Business interpretation:
-- This helps identify months when profitability is strongest or weakest and supports strategy adjustments.

-- Question 9: Are higher discounts linked to lower profit?
SELECT category,
       AVG(discount) AS avg_discount,
       SUM(profit) AS total_profit
FROM sales
GROUP BY category
ORDER BY avg_discount DESC;
-- Business interpretation:
-- Comparing discount levels with profit helps evaluate whether pricing strategy is supporting margin goals.

-- Question 10: Who are the top customers by sales?
SELECT customer_name, SUM(sales) AS total_sales
FROM sales
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 10;
-- Business interpretation:
-- High-value customers can be targeted for loyalty programs, repeat sales campaigns, and personalized service.
