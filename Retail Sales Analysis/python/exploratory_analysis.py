from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def load_cleaned_data(project_root):
    file_path = project_root / "data" / "cleaned" / "superstore_cleaned.csv"
    if not file_path.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found at {file_path}. Run data_cleaning.py first."
        )
    return pd.read_csv(file_path)


def save_chart(fig, file_name, output_folder):
    output_folder.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(output_folder / file_name, dpi=300)
    plt.close(fig)


def sales_summary(df):
    print("\n=== Sales Summary ===")
    print(f"Total sales: ${df['sales'].sum():,.2f}")
    print(f"Average sales: ${df['sales'].mean():,.2f}")
    print(f"Total orders: {df['order_id'].nunique()}")
    print(f"Unique customers: {df['customer_id'].nunique()}")


def profit_summary(df):
    print("\n=== Profit Summary ===")
    print(f"Total profit: ${df['profit'].sum():,.2f}")
    print(f"Average profit: ${df['profit'].mean():,.2f}")


def order_analysis(df):
    print("\n=== Order Analysis ===")
    avg_order_value = df.groupby("order_id")["sales"].sum().mean()
    avg_quantity_per_order = df.groupby("order_id")["quantity"].sum().mean()
    print(f"Average order value: ${avg_order_value:,.2f}")
    print(f"Average quantity per order: {avg_quantity_per_order:,.2f}")


def create_basic_charts(df, charts_folder):
    # Monthly sales trend
    monthly_sales = df.groupby("month_number")["sales"].sum().sort_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    monthly_sales.plot(kind="line", marker="o", ax=ax, color="steelblue")
    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Month Number")
    ax.set_ylabel("Sales")
    save_chart(fig, "monthly_sales_trend.png", charts_folder)

    # Monthly profit trend
    monthly_profit = df.groupby("month_number")["profit"].sum().sort_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    monthly_profit.plot(kind="line", marker="o", ax=ax, color="darkgreen")
    ax.set_title("Monthly Profit Trend")
    ax.set_xlabel("Month Number")
    ax.set_ylabel("Profit")
    save_chart(fig, "monthly_profit_trend.png", charts_folder)

    # Sales by region
    region_sales = df.groupby("region")["sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    region_sales.plot(kind="bar", ax=ax, color="royalblue")
    ax.set_title("Sales by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Sales")
    save_chart(fig, "sales_by_region.png", charts_folder)

    # Profit by region
    region_profit = df.groupby("region")["profit"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    region_profit.plot(kind="bar", ax=ax, color="seagreen")
    ax.set_title("Profit by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Profit")
    save_chart(fig, "profit_by_region.png", charts_folder)

    # Sales by category
    category_sales = df.groupby("category")["sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    category_sales.plot(kind="bar", ax=ax, color="tomato")
    ax.set_title("Sales by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Sales")
    save_chart(fig, "sales_by_category.png", charts_folder)

    # Profit by category
    category_profit = df.groupby("category")["profit"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    category_profit.plot(kind="bar", ax=ax, color="purple")
    ax.set_title("Profit by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Profit")
    save_chart(fig, "profit_by_category.png", charts_folder)

    # Discount vs profit
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df["discount"], df["profit"], alpha=0.5, color="darkorange")
    ax.set_title("Discount vs Profit")
    ax.set_xlabel("Discount")
    ax.set_ylabel("Profit")
    save_chart(fig, "discount_vs_profit.png", charts_folder)


def create_product_and_customer_charts(df, charts_folder):
    top_products_sales = df.groupby("product_name")["sales"].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    top_products_sales.plot(kind="bar", ax=ax, color="cadetblue")
    ax.set_title("Top 10 Products by Sales")
    ax.set_xlabel("Product")
    ax.set_ylabel("Sales")
    plt.xticks(rotation=45, ha="right")
    save_chart(fig, "top_10_products_by_sales.png", charts_folder)

    top_products_profit = df.groupby("product_name")["profit"].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    top_products_profit.plot(kind="bar", ax=ax, color="mediumseagreen")
    ax.set_title("Top 10 Products by Profit")
    ax.set_xlabel("Product")
    ax.set_ylabel("Profit")
    plt.xticks(rotation=45, ha="right")
    save_chart(fig, "top_10_products_by_profit.png", charts_folder)

    bottom_products_profit = df.groupby("product_name")["profit"].sum().sort_values(ascending=True).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    bottom_products_profit.plot(kind="bar", ax=ax, color="indianred")
    ax.set_title("Bottom 10 Products by Profit")
    ax.set_xlabel("Product")
    ax.set_ylabel("Profit")
    plt.xticks(rotation=45, ha="right")
    save_chart(fig, "bottom_10_products_by_profit.png", charts_folder)

    top_customers_sales = df.groupby("customer_name")["sales"].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    top_customers_sales.plot(kind="bar", ax=ax, color="darkslategray")
    ax.set_title("Top Customers by Sales")
    ax.set_xlabel("Customer")
    ax.set_ylabel("Sales")
    plt.xticks(rotation=45, ha="right")
    save_chart(fig, "top_customers_by_sales.png", charts_folder)

    top_customers_profit = df.groupby("customer_name")["profit"].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    top_customers_profit.plot(kind="bar", ax=ax, color="slateblue")
    ax.set_title("Top Customers by Profit")
    ax.set_xlabel("Customer")
    ax.set_ylabel("Profit")
    plt.xticks(rotation=45, ha="right")
    save_chart(fig, "top_customers_by_profit.png", charts_folder)


def main():
    project_root = Path(__file__).resolve().parents[1]
    charts_folder = project_root / "reports" / "charts"

    try:
        df = load_cleaned_data(project_root)
        sales_summary(df)
        profit_summary(df)
        order_analysis(df)

        print("\n=== Top Products by Sales ===")
        print(df.groupby("product_name")["sales"].sum().sort_values(ascending=False).head(10))

        print("\n=== Top Products by Profit ===")
        print(df.groupby("product_name")["profit"].sum().sort_values(ascending=False).head(10))

        print("\n=== Bottom Products by Profit ===")
        print(df.groupby("product_name")["profit"].sum().sort_values(ascending=True).head(10))

        print("\n=== Top Customers by Sales ===")
        print(df.groupby("customer_name")["sales"].sum().sort_values(ascending=False).head(10))

        print("\n=== Top Customers by Profit ===")
        print(df.groupby("customer_name")["profit"].sum().sort_values(ascending=False).head(10))

        create_basic_charts(df, charts_folder)
        create_product_and_customer_charts(df, charts_folder)

        print(f"\nCharts saved to: {charts_folder}")

    except FileNotFoundError as error:
        print(f"\n{error}")
        print("Place the cleaned dataset here before running the analysis:")
        print(project_root / "data" / "cleaned" / "superstore_cleaned.csv")
    except Exception as error:
        print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()
