import numpy as np

def calculate_risk(df, market_score):

    df["RiskScore"] = (
        0.4 * (1 - df["SavingsRate"]) +
        0.3 * df["OverspendingIndex"] +
        0.3 * (1 - market_score)
    )
    
    df["RiskScore"] = df["RiskScore"] + np.random.normal(0, 0.2, len(df))

    # 🔥 Risk classification
    df["RiskLevel"] = df["RiskScore"].apply(
        lambda x: "High" if x > 1 else ("Medium" if x > 0.5 else "Low")
    )

    return df