"""Create the sales table and load the cleaned Superstore dataset into PostgreSQL."""

import argparse
import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv


TABLE_SQL = """
CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    row_id INTEGER,
    order_id VARCHAR(50),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_id VARCHAR(50),
    customer_name VARCHAR(200),
    segment VARCHAR(50),
    country VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code INTEGER,
    region VARCHAR(50),
    product_id VARCHAR(50),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name TEXT,
    sales NUMERIC(12, 2),
    quantity INTEGER,
    discount NUMERIC(5, 2),
    profit NUMERIC(12, 2)
);
"""

COLUMNS = """
row_id, order_id, order_date, ship_date, ship_mode, customer_id,
customer_name, segment, country, city, state, postal_code, region,
product_id, category, sub_category, product_name, sales, quantity,
discount, profit
"""


def main():
    parser = argparse.ArgumentParser(description="Load cleaned retail sales data into PostgreSQL.")
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Delete existing sales rows before importing. Use only when you intend to reload the table.",
    )
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parents[1]
    cleaned_path = project_root / "data" / "cleaned" / "superstore_cleaned.csv"
    load_dotenv(project_root / ".env")
    database_url = os.getenv("DATABASE_URL")

    if not cleaned_path.exists():
        raise FileNotFoundError(f"Cleaned dataset not found: {cleaned_path}. Run data_cleaning.py first.")
    if not database_url:
        raise ValueError(
            "DATABASE_URL is not set. Copy .env.example to .env and add your PostgreSQL connection URL."
        )

    with psycopg.connect(database_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(TABLE_SQL)
            cursor.execute("SELECT COUNT(*) FROM sales")
            existing_rows = cursor.fetchone()[0]

            if existing_rows and not args.replace:
                raise ValueError(
                    f"The sales table already contains {existing_rows} rows. "
                    "Run with --replace only if you want to reload it."
                )
            if args.replace:
                cursor.execute("TRUNCATE TABLE sales RESTART IDENTITY")

            with cleaned_path.open("r", encoding="utf-8", newline="") as csv_file:
                with cursor.copy(f"COPY sales ({COLUMNS}) FROM STDIN WITH (FORMAT CSV, HEADER TRUE)") as copy:
                    while chunk := csv_file.read(1024 * 1024):
                        copy.write(chunk)

            cursor.execute("SELECT COUNT(*) FROM sales")
            loaded_rows = cursor.fetchone()[0]

    print(f"Connected to PostgreSQL and loaded {loaded_rows:,} rows into the sales table.")


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, ValueError, psycopg.Error) as error:
        raise SystemExit(f"Database load failed: {error}")
