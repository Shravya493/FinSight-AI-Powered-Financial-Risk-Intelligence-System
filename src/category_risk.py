def top_risk_category(transactions):

    expense_df = transactions[transactions["Type"] == "Expense"]

    category_spending = (
        expense_df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    return category_spending.reset_index()