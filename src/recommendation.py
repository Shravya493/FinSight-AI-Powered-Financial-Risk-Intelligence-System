def recommend(df):

    recommendations = []

    for _, row in df.iterrows():

        if row["OverspendingIndex"] > 1.5:
            recommendations.append("High spending - reduce discretionary expenses")

        elif row["SavingsRate"] < 0:
            recommendations.append("Negative savings - increase income or cut costs")

        elif row["RiskLevel"] == "High":
            recommendations.append("High financial risk - review budget immediately")

        else:
            recommendations.append("Financially stable")

    df["Recommendation"] = recommendations

    return df