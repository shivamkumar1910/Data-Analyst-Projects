# E-commerce Funnel Analysis

## Project Overview

This project is a beginner-friendly e-commerce funnel analysis built using a synthetic dataset. The goal is to show how a data analyst can study customer behavior from signup through purchase and identify where users are dropping off in the funnel.

The project is intentionally simple and realistic for a student or junior analyst. It focuses on practical questions such as:

- How many users start the funnel?
- How many reach each stage?
- Where do users drop off?
- Does conversion differ by device or traffic source?
- Which dates perform better?

This is not a production-level analytics project. It is designed to be easy to understand, explain in an interview, and build using basic SQL and Tableau.

## Business Problem

Many online businesses struggle to understand why visitors do not convert into customers. A funnel analysis helps answer this by showing how users move through each important stage of the customer journey.

In this project, the funnel is:

Signup → Product View → Add to Cart → Checkout → Purchase

The main business problem is to find where users leave the journey and which segments are performing better or worse.

## Dataset Description

The dataset is synthetic and contains approximately 35,000 rows across 8,500 users. It is designed to simulate realistic ecommerce behavior while keeping the data easy to analyze.

Columns:

- user_id
- session_id
- event_date
- event_type
- product_id
- device_type
- traffic_source
- country

Funnel events used:

- signup
- product_view
- add_to_cart
- checkout
- purchase

The dataset includes realistic drop-off patterns where not every user continues to the next stage.

## Tools Used

- MySQL
- SQL
- Tableau
- CSV dataset
- Python (used only to generate the synthetic dataset)

## Key Questions

The analysis answers questions such as:

- How many unique users entered the funnel?
- How many users reached each stage?
- What percentage moved from one stage to the next?
- What is the overall conversion rate?
- Where is the biggest drop-off?
- Is conversion different by device type?
- Is conversion different by traffic source?
- Which dates perform better or worse?

## SQL Analysis

The SQL scripts in the `sql/` folder are designed to answer the business questions in a clear and beginner-friendly way. They use basic SQL concepts such as:

- SELECT
- WHERE
- GROUP BY
- COUNT
- COUNT DISTINCT
- CASE
- JOIN
- CTEs

The queries show the number of users at each stage and calculate stage-to-stage conversion rates.

## Tableau Dashboard

The dashboard is designed to be clean and simple for an entry-level analyst.

### KPI cards
- Total Users
- Add-to-Cart Rate
- Checkout Rate
- Purchase Conversion Rate

### Visuals
- Funnel chart
- Conversion and drop-off chart
- Conversion by device type
- Conversion by traffic source
- Daily/weekly conversion trend

### Filters
- Date
- Device Type
- Traffic Source
- Country

## Key Insights

Key business insights should be based on the actual analysis of the synthetic data. The figures can be updated after the SQL queries are run.

Examples of findings the project is designed to reveal:

- A large share of users drop off before reaching add-to-cart
- Mobile conversion may be lower than desktop conversion
- Some traffic sources may drive stronger conversion than others
- Purchase conversion can vary by day or week

## Recommendations

Recommendations are based on the actual analysis of the dataset and should be framed carefully.

Examples:

- Review the product page experience where users are likely dropping off
- Improve mobile checkout performance
- Focus more on traffic sources with stronger conversion rates
- Simplify checkout to reduce abandonment

## How to Run the Project

1. Open the project folder.
2. Make sure the dataset is stored in `data/ecommerce_events.csv`.
3. Import the CSV into MySQL.
4. If MySQL blocks the CSV import with the secure-file-priv error, move the CSV into the folder indicated by `SHOW VARIABLES LIKE 'secure_file_priv';` and use that exact path in the import statement.
5. Run the SQL scripts in order from the `sql/` folder.
6. Open Tableau.
7. Connect to the MySQL table.
8. Build the dashboard using the design described in the Tableau README.
9. Use the analysis results to write your insights and recommendations.

## MySQL Import Note

If you see this error:

`The MySQL server is running with the --secure-file-priv option so it cannot execute this statement`

then MySQL is only allowing imports from a specific server directory. The fix is simple:

- run `SHOW VARIABLES LIKE 'secure_file_priv';`
- copy the CSV file into the folder returned by MySQL
- update the import path in the SQL script to match that directory
- or import the CSV using the MySQL Workbench import wizard

This is a common beginner issue and not a problem with the project itself.

## Notes

- The dataset is synthetic and created for learning purposes.
- This project is intentionally simple and beginner-friendly.
- The aim is to demonstrate core analyst thinking rather than advanced production analytics.
