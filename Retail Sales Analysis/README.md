# Retail Sales Analysis Dashboard

## Overview

This project is a beginner-friendly retail analytics portfolio project built around the public Sample Superstore dataset. It demonstrates the full workflow of a junior data analyst: cleaning raw sales data, exploring patterns in sales and profitability, writing SQL queries, and preparing a Power BI dashboard for business reporting.

The goal is to show how data can be transformed into useful business insight. Instead of focusing on advanced modeling, this project emphasizes practical analyst skills such as data validation, KPI calculation, trend analysis, and stakeholder-friendly reporting.

## Business Problem

Retail businesses often need to understand which products, categories, regions, and customer groups perform best. They also need to monitor margins, identify low-profit products, and evaluate the impact of discounting on overall profitability. This project addresses that challenge by turning raw transaction data into a clear sales and profit story that supports business decisions.

## Objectives

- Analyze sales performance
- Analyze profitability
- Identify top and bottom products
- Compare regional performance
- Understand customer behavior
- Analyze discount impact

## Tech Stack

- Python
- Pandas
- Matplotlib
- SQL
- PostgreSQL
- Power BI

## Project Structure

- `data/raw/` - Raw CSV input file from the public Sample Superstore dataset
- `data/cleaned/` - Cleaned dataset created by the Python cleaning script
- `python/` - Python scripts for cleaning and exploratory analysis
- `sql/` - SQL scripts for table creation, import, and business analysis
- `powerbi/` - Data model, DAX measures, and dashboard setup guide
- `reports/` - Charts and insight notes
- `README.md` - Project overview and run instructions
- `requirements.txt` - Required Python libraries

## Data Cleaning

The Python cleaning workflow includes:

1. Loading the raw CSV file
2. Checking the size and structure of the dataset
3. Reviewing column names and data types
4. Identifying missing values and duplicate rows
5. Converting date columns to datetime format
6. Cleaning numeric values and standardizing field names
7. Creating useful date fields such as year, month, month number, and quarter
8. Saving the cleaned dataset to `data/cleaned/superstore_cleaned.csv`

The cleaning script is designed to be beginner-friendly and easy to explain in an interview.

## SQL Analysis

The SQL layer is built in PostgreSQL and focuses on practical business questions such as:

- Total sales and total profit
- Number of orders and unique customers
- Regional comparison
- Category and sub-category analysis
- Monthly sales and profit trends
- Product performance ranking
- Discount and profitability analysis

The SQL scripts are organized by theme and are intentionally written in a readable format for learning and demonstration.

## Power BI Dashboard

The dashboard is planned as a three-page Power BI report:

1. Executive Overview
   - KPI cards
   - Monthly sales trend
   - Sales by region
   - Sales by category
   - Profit by region

2. Product and Category Analysis
   - Category and sub-category performance
   - Top 10 products by sales and profit
   - Bottom 10 products by profit

3. Customer and Regional Analysis
   - Top customers
   - Sales and profit by region
   - Sales and profit by segment
   - Monthly sales trend

## Key Insights

This section is intentionally left ready for actual analysis after the dataset is added and the scripts are run. Because the raw CSV is not currently present in the workspace, no business findings are claimed here without verification.

## Business Recommendations

Recommendations will be added after the actual dataset is analyzed. The project is structured so the recommendations are based on measured results from the sales data rather than assumptions.

## How to Run

1. Download the public Sample Superstore dataset from Tableau's public sample data or a trusted public CSV mirror and save it as `data/raw/superstore.csv`.
   - A common source is the Tableau Sample Superstore data used in public training material and sample workbooks.
   - If using a mirror, make sure the file matches the standard Sample Superstore transaction format with columns such as Order ID, Order Date, Sales, Quantity, Discount, Profit, Category, Region, and Customer Name.
2. Open a terminal in the project folder.
3. Install Python dependencies:
   `pip install -r requirements.txt`
4. Run the data cleaning script:
   `python python/data_cleaning.py`
5. Run the exploratory analysis script:
   `python python/exploratory_analysis.py`
6. Import the cleaned CSV into PostgreSQL.
7. Run the SQL scripts in order from `sql/`.
8. Open Power BI Desktop.
9. Import the cleaned dataset.
10. Build the dashboard using the guide in `powerbi/dashboard_guide.md`.

## Notes

- The dataset is not included in this project folder because it is a public file that must be downloaded into the local project directory.
- The scripts are prepared to handle the dataset once it is placed in the expected location.
- All calculations and recommendations should be based on the actual cleaned data from the source file.
