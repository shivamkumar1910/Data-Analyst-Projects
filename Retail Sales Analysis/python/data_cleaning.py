import pandas as pd
from pathlib import Path


def load_dataset(raw_path):
    """Load the raw CSV file and raise a clear error if it is missing."""
    if not raw_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at: {raw_path}. Please download the Sample Superstore CSV and save it here."
        )

    df = pd.read_csv(raw_path)
    print(f"Raw dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def show_dataset_overview(df):
    """Print basic dataset information."""
    print("\n=== Dataset Overview ===")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("Column names:")
    print(list(df.columns))
    print("\nData types:")
    print(df.dtypes)


def check_missing_values(df):
    """Display missing values by column."""
    missing = df.isnull().sum()
    print("\n=== Missing Values ===")
    print(missing[missing > 0])
    return int(missing.sum())


def check_duplicates(df):
    """Return and print duplicate row count."""
    duplicate_count = df.duplicated().sum()
    print(f"\nDuplicate rows: {duplicate_count}")
    return duplicate_count


def standardize_columns(df):
    """Clean and standardize column names for easier analysis."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return df


def convert_dates(df):
    """Convert date columns into datetime values."""
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    if "ship_date" in df.columns:
        df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")
    return df


def check_numeric_columns(df):
    """Print numeric columns and convert them when possible."""
    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
    print("\nNumeric columns:")
    print(numeric_columns)
    return numeric_columns


def handle_missing_values(df):
    """Handle missing values using simple, explainable logic."""
    missing_count_before = int(df.isnull().sum().sum())

    text_columns = [
        "customer_name",
        "segment",
        "country",
        "city",
        "state",
        "region",
        "category",
        "sub_category",
        "product_name",
        "product_id",
        "ship_mode",
        "customer_id",
        "order_id",
    ]

    for column in text_columns:
        if column in df.columns:
            df[column] = df[column].fillna("Unknown")

    numeric_columns = [
        "sales",
        "quantity",
        "discount",
        "profit",
        "postal_code",
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")
            if df[column].isnull().any():
                median_value = df[column].median()
                df[column] = df[column].fillna(median_value)

    missing_count_after = int(df.isnull().sum().sum())
    print(f"\nMissing values handled: {missing_count_before - missing_count_after}")
    return missing_count_before - missing_count_after


def check_invalid_values(df):
    """Look for obvious invalid or impossible values."""
    print("\n=== Invalid Values Check ===")
    for column in ["sales", "profit", "quantity", "discount"]:
        if column in df.columns:
            negative_values = (df[column] < 0).sum()
            if negative_values > 0:
                print(f"{column}: {negative_values} negative values found")
            else:
                print(f"{column}: no negative values found")


def create_date_features(df):
    """Create year, month, month number, and quarter columns."""
    if "order_date" in df.columns:
        df["year"] = df["order_date"].dt.year
        df["month"] = df["order_date"].dt.strftime("%b")
        df["month_number"] = df["order_date"].dt.month
        df["quarter"] = df["order_date"].dt.quarter
    return df


def clean_dataset(df):
    """Apply the full cleaning workflow."""
    original_rows = len(df)
    df = standardize_columns(df)
    duplicate_count = df.duplicated().sum()
    df = df.drop_duplicates().copy()
    df = convert_dates(df)
    check_numeric_columns(df)
    handle_missing_values(df)
    check_invalid_values(df)
    df = create_date_features(df)
    final_rows = len(df)

    print("\n=== Cleaning Summary ===")
    print(f"Original rows: {original_rows}")
    print(f"Duplicate rows removed: {duplicate_count}")
    print(f"Missing values handled: {original_rows - final_rows + duplicate_count}")
    print(f"Final rows: {final_rows}")

    return df


def main():
    project_root = Path(__file__).resolve().parents[1]
    raw_path = project_root / "data" / "raw" / "superstore.csv"
    cleaned_path = project_root / "data" / "cleaned" / "superstore_cleaned.csv"

    try:
        df = load_dataset(raw_path)
        show_dataset_overview(df)
        check_missing_values(df)
        check_duplicates(df)
        cleaned_df = clean_dataset(df)
        cleaned_df.to_csv(cleaned_path, index=False)
        print(f"\nCleaned dataset saved to: {cleaned_path}")
    except FileNotFoundError as error:
        print(f"\n{error}")
        print("Place the dataset here before running the script:")
        print(raw_path)
    except Exception as error:
        print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()
