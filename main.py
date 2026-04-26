from src.data_cleaning import clean_transactions, clean_news
from src.data_loader import load_transactions, load_news
from src.behavior import analyze_behavior
from src.sentiment import analyze_sentiment
from src.risk_engine import calculate_risk
from src.time_analysis import monthly_risk
from src.insights import generate_insights
from src.recommendation import recommend
from src.category_risk import top_risk_category
from src.ml_model import train_regression_models, train_classification_model
from src.scenario_analysis import simulate_scenarios
from src.ml_model import feature_importance
import numpy as np
np.random.seed(42)

# ---------------- STEP 1: CLEAN DATA ---------------- #
clean_transactions("data/raw_transactions.csv", "data/transactions.csv")
clean_news("data/raw_news.csv", "data/news.csv")

# ---------------- STEP 2: LOAD DATA ---------------- #
transactions = load_transactions("data/transactions.csv")
news = load_news("data/news.csv")

# ---------------- STEP 3: BEHAVIOR ---------------- #
behavior_df = analyze_behavior(transactions)

# ---------------- STEP 4: SENTIMENT ---------------- #
market_score, _ = analyze_sentiment(news)

# ---------------- STEP 5: RISK ---------------- #
risk_df = calculate_risk(behavior_df, market_score)

# ---------------- STEP 6: RECOMMENDATIONS ---------------- #
risk_df = recommend(risk_df)

# ---------------- STEP 7: TIME ANALYSIS ---------------- #
monthly_df = monthly_risk(transactions)

# ---------------- STEP 8: INSIGHTS ---------------- #
insights = generate_insights(risk_df)

#--------------Category risk---------
category_df = top_risk_category(transactions)
category_df.to_csv("output/top_categories.csv", index=False)

# ---------------- STEP 9: SAVE OUTPUT ---------------- #
risk_df.to_csv("output/user_risk.csv", index=False)
monthly_df.to_csv("output/monthly_risk.csv", index=False)

risk_df.to_csv("output/ml_dataset.csv", index=False)

scenarios = simulate_scenarios(risk_df)

print("\nScenario Analysis:")
print("Positive Market Risk (sample):")
print(scenarios["PositiveMarketRisk"].head())

print("\nNegative Market Risk (sample):")
print(scenarios["NegativeMarketRisk"].head())

print("\n✅ PROJECT COMPLETED SUCCESSFULLY\n")
print("\nTop 5 Users by Risk:\n")
print(risk_df.sort_values(by="RiskScore", ascending=False).head())
print("\nInsights:", insights)

# 🔹 Regression (for understanding relationships)
reg_results = train_regression_models(risk_df)

print("\nRegression Model Performance:")
for model, score in reg_results.items():
    print(f"{model}: {score:.3f}")

# 🔥 Classification (actual ML use-case)
clf_model, accuracy = train_classification_model(risk_df)

print("\nClassification Accuracy:", round(accuracy, 3))

importance_df = feature_importance(clf_model)

print("\nFeature Importance:")
print(importance_df)
importance_df.to_csv("output/feature_importance.csv", index=False)