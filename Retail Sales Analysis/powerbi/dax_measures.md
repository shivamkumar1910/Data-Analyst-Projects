# Power BI DAX Measures

These beginner-friendly DAX measures help build the dashboard. They are written for a table called `superstore_cleaned`.

## Total Sales

Total Sales =
SUM(superstore_cleaned[Sales])

This measure adds all sales values in the dataset.

## Total Profit

Total Profit =
SUM(superstore_cleaned[Profit])

This measure shows total profit after costs and discounts.

## Total Orders

Total Orders =
DISTINCTCOUNT(superstore_cleaned[Order ID])

This counts the number of unique orders in the dataset.

## Total Customers

Total Customers =
DISTINCTCOUNT(superstore_cleaned[Customer ID])

This counts unique customers who placed orders.

## Average Order Value

Average Order Value =
DIVIDE([Total Sales], [Total Orders])

This calculates the average revenue per order.

## Profit Margin

Profit Margin =
DIVIDE([Total Profit], [Total Sales])

This shows how much profit is earned for each dollar of sales.

## Average Discount

Average Discount =
AVERAGE(superstore_cleaned[Discount])

This helps measure whether discounting is heavy or moderate.

## Total Quantity

Total Quantity =
SUM(superstore_cleaned[Quantity])

This measures the number of units sold.

## Optional Date Measures

Year =
YEAR(MAX(superstore_cleaned[Order Date]))

This can be useful if you want a year-level selector.

Month Name =
FORMAT(MAX(superstore_cleaned[Order Date]), "MMMM")

This helps create monthly trend labels in the dashboard.

## Notes

Keep the DAX simple and easy to explain. In a beginner portfolio project, clarity and business understanding are more important than advanced modeling.
