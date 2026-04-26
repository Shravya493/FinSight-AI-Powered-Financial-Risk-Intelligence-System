import pandas as pd
import numpy as np
np.random.seed(42)
# ---------------- TRANSACTIONS ---------------- #
def clean_transactions(input_path, output_path):
    
    # Try both separators
    try:
        df = pd.read_csv(input_path)
        if df.shape[1] == 1:
            df = pd.read_csv(input_path, sep="\t")
    except:
        df = pd.read_csv(input_path, sep="\t")

    # Clean column names
    df.columns = df.columns.str.strip()

    print("Original Columns:", df.columns)

    # Clean string columns
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.strip()

    # Rename
    df = df.rename(columns={
        "Date": "Date",
        "Transaction Description": "Description",
        "Category": "Category",
        "Amount": "Amount",
        "Type": "Type"
    })

    # Convert Date
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")

    # Clean Amount
    df["Amount"] = df["Amount"].astype(str).str.replace(",", "").str.replace("₹", "")
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

    # Normalize Type
    df["Type"] = df["Type"].str.capitalize()

    print("\nBefore drop:")
    print(df[["Date", "Amount", "Type"]].head())

    # Drop bad rows
    df = df.dropna(subset=["Date", "Amount"])

    print("\nRows after cleaning:", len(df))
    print("Unique Types:", df["Type"].unique())

    # 🔥 ADD USER COLUMN HERE (IMPORTANT)
    df["User"] = np.random.randint(1, 201, len(df))

    # Final columns
    df = df[["User", "Date", "Category", "Amount", "Type"]]

    df.to_csv(output_path, index=False)
    return df


# ---------------- NEWS ---------------- #
def clean_news(input_path, output_path):
    df = pd.read_csv(input_path)

    # Clean column names
    df.columns = df.columns.str.strip()

    print("News Columns:", df.columns)

    # Combine headline + description
    if "Description" in df.columns:
        df["News"] = df["Headlines"].astype(str) + " " + df["Description"].astype(str)
    else:
        df["News"] = df["Headlines"].astype(str)

    # Create dummy date
    df["Date"] = pd.to_datetime("2020-01-01")

    df = df[["Date", "News"]]

    print("\nNews sample:")
    print(df.head())

    df.to_csv(output_path, index=False)
    return df