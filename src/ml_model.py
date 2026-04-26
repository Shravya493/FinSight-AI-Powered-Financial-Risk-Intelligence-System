from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import r2_score, accuracy_score


# =========================================================
# 🔹 REGRESSION MODELS (for learning relationship)
# =========================================================
def train_regression_models(df):

    X = df[["Income", "Expense", "SavingsRate", "OverspendingIndex"]]
    y = df["RiskScore"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    results = {}

    # 🔹 Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr_pred = lr.predict(X_test)
    results["LinearRegression"] = r2_score(y_test, lr_pred)

    # 🔹 Decision Tree
    dt = DecisionTreeRegressor(random_state=42)
    dt.fit(X_train, y_train)
    dt_pred = dt.predict(X_test)
    results["DecisionTree"] = r2_score(y_test, dt_pred)

    # 🔹 Random Forest
    rf = RandomForestRegressor(random_state=42)
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)
    results["RandomForest"] = r2_score(y_test, rf_pred)

    return results


# =========================================================
# 🔥 CLASSIFICATION MODEL (REALISTIC & IMPORTANT)
# =========================================================
def train_classification_model(df):

    X = df[["Income", "Expense", "SavingsRate", "OverspendingIndex"]]
    y = df["RiskLevel"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    return model, acc

def feature_importance(model):

    import pandas as pd

    features = ["Income", "Expense", "SavingsRate", "OverspendingIndex"]

    importance = model.feature_importances_

    return pd.DataFrame({
        "Feature": features,
        "Importance": importance
    }).sort_values(by="Importance", ascending=False)