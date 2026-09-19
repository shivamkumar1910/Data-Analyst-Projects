# Power BI Data Model

## Dataset Structure

This project can use a simple single-table model. The cleaned dataset contains one row per sales transaction, with product, customer, order, and regional details stored together.

## Important Columns

- `row_id`
- `order_id`
- `order_date`
- `ship_date`
- `ship_mode`
- `customer_id`
- `customer_name`
- `segment`
- `country`
- `city`
- `state`
- `region`
- `product_id`
- `category`
- `sub_category`
- `product_name`
- `sales`
- `quantity`
- `discount`
- `profit`
- `year`
- `month`
- `month_number`
- `quarter`

## Data Types

Recommended Power BI data types:

- `order_date`, `ship_date` -> Date
- `sales`, `profit` -> Decimal Number
- `quantity` -> Whole Number
- `discount` -> Decimal Number
- `postal_code` -> Whole Number
- `customer_id`, `order_id`, `product_id` -> Text
- `segment`, `region`, `category`, `sub_category` -> Text

## Relationships

For a beginner project, a single table is enough. There is no need to create separate dimension tables unless you want to expand the model later.

Recommended model:

- One fact table: `superstore_cleaned`
- One date table (optional for time intelligence)

If you add a date table, create a relationship between the date table and `order_date`.

## Measures

Use the cleaned table to create the following measures:

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Average Order Value
- Profit Margin
- Average Discount
- Total Quantity

## Recommended Data Model

Keep the model simple:

- Import the cleaned CSV
- Use one table only
- Mark `order_date` as a date field
- Create a small date table if needed for monthly trend analysis
- Build visuals from the same table with slicers and KPIs

This is a clean and realistic beginner-level model that is easy to explain in an interview.
