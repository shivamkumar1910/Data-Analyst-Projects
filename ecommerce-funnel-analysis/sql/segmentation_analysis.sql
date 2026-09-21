-- PostgreSQL segment-level funnel analysis
-- This helps show how different customer groups behave

SELECT
    device_type,
    COUNT(DISTINCT user_id) AS users,
    COUNT(DISTINCT CASE WHEN event_type = 'product_view' THEN user_id END) AS product_view_users,
    COUNT(DISTINCT CASE WHEN event_type = 'add_to_cart' THEN user_id END) AS add_to_cart_users,
    COUNT(DISTINCT CASE WHEN event_type = 'checkout' THEN user_id END) AS checkout_users,
    COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) AS purchase_users
FROM ecommerce_events
GROUP BY device_type
ORDER BY device_type;

SELECT
    traffic_source,
    COUNT(DISTINCT user_id) AS users,
    COUNT(DISTINCT CASE WHEN event_type = 'product_view' THEN user_id END) AS product_view_users,
    COUNT(DISTINCT CASE WHEN event_type = 'add_to_cart' THEN user_id END) AS add_to_cart_users,
    COUNT(DISTINCT CASE WHEN event_type = 'checkout' THEN user_id END) AS checkout_users,
    COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) AS purchase_users
FROM ecommerce_events
GROUP BY traffic_source
ORDER BY traffic_source;

SELECT
    country,
    COUNT(DISTINCT user_id) AS users,
    COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) AS purchases,
    ROUND(
        COUNT(DISTINCT CASE WHEN event_type = 'purchase' THEN user_id END) /
        COUNT(DISTINCT user_id) * 100,
        2
    ) AS conversion_rate_pct
FROM ecommerce_events
GROUP BY country
ORDER BY conversion_rate_pct DESC;
