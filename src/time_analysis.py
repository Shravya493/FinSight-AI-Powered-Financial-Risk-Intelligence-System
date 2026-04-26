import pandas as pd

def monthly_risk(df):

    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")

    monthly = df.groupby(["User", "Month", "Type"])["Amount"].sum().unstack().fillna(0)

    # Ensure columns exist
    monthly["Income"] = monthly.get("Income", 0)
    monthly["Expense"] = monthly.get("Expense", 0)

    # Metrics
    monthly["Savings"] = monthly["Income"] - monthly["Expense"]
    monthly["SavingsRate"] = monthly["Savings"] / monthly["Income"].replace(0, 1)
    monthly["OverspendingIndex"] = monthly["Expense"] / monthly["Income"].replace(0, 1)

    # 🔥 ADD THIS (IMPORTANT)
    monthly["RiskScore"] = (
        0.4 * (1 - monthly["SavingsRate"]) +
        0.3 * monthly["OverspendingIndex"]
    )

    return monthly.reset_index()