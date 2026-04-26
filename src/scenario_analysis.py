def simulate_scenarios(df):

    scenarios = {}

    # Positive market (risk decreases)
    scenarios["PositiveMarketRisk"] = df["RiskScore"] * 0.9

    # Negative market (risk increases)
    scenarios["NegativeMarketRisk"] = df["RiskScore"] * 1.2

    return scenarios