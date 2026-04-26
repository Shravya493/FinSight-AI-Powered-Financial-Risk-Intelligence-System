import pandas as pd

def analyze_behavior(df):

    results = []

    for user in df["User"].unique():
        user_df = df[df["User"] == user]

        income = user_df[user_df["Type"] == "Income"]["Amount"].sum()
        expense = user_df[user_df["Type"] == "Expense"]["Amount"].sum()

        savings = income - expense
        savings_rate = savings / income if income != 0 else 0
        overspending_index = expense / income if income != 0 else 0

        results.append({
            "User": user,
            "Income": income,
            "Expense": expense,
            "Savings": savings,
            "SavingsRate": savings_rate,
            "OverspendingIndex": overspending_index
        })

    return pd.DataFrame(results)