-- PostgreSQL e-commerce funnel analysis
-- Goal: understand how users move from signup to purchase

-- 1. How many unique users entered the funnel?
SELECT COUNT(DISTINCT user_id) AS total_users
FROM ecommerce_events
WHERE event_type = 'signup';

-- 2. How many users reached each funnel stage?
SELECT event_type,
       COUNT(DISTINCT user_id) AS users_at_stage
FROM ecommerce_events
GROUP BY event_type
ORDER BY CASE event_type
    WHEN 'signup' THEN 1
    WHEN 'product_view' THEN 2
    WHEN 'add_to_cart' THEN 3
    WHEN 'checkout' THEN 4
    WHEN 'purchase' THEN 5
END;

-- 3. Stage conversion rate
WITH funnel_users AS (
    SELECT
        COUNT(DISTINCT CASE WHEN event_type = 'signup' THEN user_id END) AS signup_users,
        COUNT(DISTINCT CASE WHEN event_type = 'product_view' THEN user_id END) AS product_view_users,
        COUNT(DISTINCT CASE WHEN event_type = 'add_to_cart' THEN user_id END) AS add_to_cart_users,
        COUNT(DISTINCT CASE WHEN event_type = 'checkout' THEN user_id END) AS checkout_users,
        COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) AS purchase_users
    FROM ecommerce_events
)
SELECT
    signup_users,
    product_view_users,
    add_to_cart_users,
    checkout_users,
    purchase_users,
    ROUND(product_view_users / signup_users * 100, 2) AS signup_to_product_view_pct,
    ROUND(add_to_cart_users / product_view_users * 100, 2) AS product_view_to_cart_pct,
    ROUND(checkout_users / add_to_cart_users * 100, 2) AS add_to_cart_to_checkout_pct,
    ROUND(purchase_users / checkout_users * 100, 2) AS checkout_to_purchase_pct
FROM funnel_users;

-- 4. Overall purchase conversion rate
SELECT
    COUNT(DISTINCT CASE WHEN event_type = 'signup' THEN user_id END) AS total_signups,
    COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) AS total_purchases,
    ROUND(
        COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) /
        COUNT(DISTINCT CASE WHEN event_type = 'signup' THEN user_id END) * 100,
        2
    ) AS overall_conversion_rate_pct
FROM ecommerce_events;

-- 5. Biggest drop-off between stages
WITH funnel AS (
    SELECT
        COUNT(DISTINCT CASE WHEN event_type = 'signup' THEN user_id END) AS signup_users,
        COUNT(DISTINCT CASE WHEN event_type = 'product_view' THEN user_id END) AS product_view_users,
        COUNT(DISTINCT CASE WHEN event_type = 'add_to_cart' THEN user_id END) AS add_to_cart_users,
        COUNT(DISTINCT CASE WHEN event_type = 'checkout' THEN user_id END) AS checkout_users,
        COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) AS purchase_users
    FROM ecommerce_events
),
conversion AS (
    SELECT
        signup_users,
        product_view_users,
        add_to_cart_users,
        checkout_users,
        purchase_users,
        signup_users - product_view_users AS signup_to_view_dropoff,
        product_view_users - add_to_cart_users AS view_to_cart_dropoff,
        add_to_cart_users - checkout_users AS cart_to_checkout_dropoff,
        checkout_users - purchase_users AS checkout_to_purchase_dropoff
    FROM funnel
)
SELECT *
FROM conversion;

-- 6. Conversion by device type
SELECT
    device_type,
    COUNT(DISTINCT CASE WHEN event_type = 'signup' THEN user_id END) AS total_signups,
    COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) AS total_purchases,
    ROUND(
        COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) /
        COUNT(DISTINCT CASE WHEN event_type = 'signup' THEN user_id END) * 100,
        2
    ) AS purchase_conversion_rate_pct
FROM ecommerce_events
GROUP BY device_type
ORDER BY purchase_conversion_rate_pct DESC;

-- 7. Conversion by traffic source
SELECT
    traffic_source,
    COUNT(DISTINCT CASE WHEN event_type = 'signup' THEN user_id END) AS total_signups,
    COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) AS total_purchases,
    ROUND(
        COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) /
        COUNT(DISTINCT CASE WHEN event_type = 'signup' THEN user_id END) * 100,
        2
    ) AS purchase_conversion_rate_pct
FROM ecommerce_events
GROUP BY traffic_source
ORDER BY purchase_conversion_rate_pct DESC;

-- 8. Daily conversion trend
SELECT
    DATE(event_date) AS event_day,
    COUNT(DISTINCT CASE WHEN event_type = 'signup' THEN user_id END) AS signups,
    COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) AS purchases,
    ROUND(
        COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) /
        COUNT(DISTINCT CASE WHEN event_type = 'signup' THEN user_id END) * 100,
        2
    ) AS conversion_rate_pct
FROM ecommerce_events
GROUP BY DATE(event_date)
ORDER BY event_day;

-- 9. By date and device type
SELECT
    DATE(event_date) AS event_day,
    device_type,
    COUNT(DISTINCT CASE WHEN event_type = 'signup' THEN user_id END) AS signups,
    COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) AS purchases,
    ROUND(
        COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) /
        COUNT(DISTINCT CASE WHEN event_type = 'signup' THEN user_id END) * 100,
        2
    ) AS conversion_rate_pct
FROM ecommerce_events
GROUP BY DATE(event_date), device_type
ORDER BY event_day, device_type;
