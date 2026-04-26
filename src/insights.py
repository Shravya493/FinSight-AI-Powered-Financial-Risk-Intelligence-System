def generate_insights(df):

    insights = {}

    # 🔹 Top risky user
    insights["TopRiskUser"] = int(df.loc[df["RiskScore"].idxmax(), "User"])

    # 🔹 Safest user
    insights["SafestUser"] = int(df.loc[df["RiskScore"].idxmin(), "User"])

    # 🔹 Average risk
    insights["AverageRisk"] = float(df["RiskScore"].mean())

    # 🔹 Risk distribution
    insights["HighRiskCount"] = int((df["RiskLevel"] == "High").sum())

    # 🔹 Most common risk level
    insights["MostCommonRiskLevel"] = df["RiskLevel"].mode()[0]

    # 🔹 Average savings rate
    insights["AvgSavingsRate"] = float(df["SavingsRate"].mean())

    # 🔥 ADVANCED BUSINESS INSIGHTS

    # Users overspending
    insights["UsersOverspending"] = int((df["OverspendingIndex"] > 1).sum())

    # Users with negative savings
    insights["NegativeSavingsUsers"] = int((df["Savings"] < 0).sum())

    # % high risk users
    insights["HighRiskPercentage"] = float(
        (df["RiskLevel"] == "High").sum() / len(df) * 100
    )

    return insights