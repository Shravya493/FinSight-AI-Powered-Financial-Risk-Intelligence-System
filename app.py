import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="FinSight Dashboard",
    layout="wide"
)

# ---------------- TITLE ---------------- #
st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>
    💰 FinSight: AI-Powered Financial Risk Intelligence System
    </h1>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------- LOAD DATA ---------------- #
df = pd.read_csv("output/user_risk.csv")

# ---------------- KPI SECTION ---------------- #
st.subheader("📊 Key Financial Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Total Users", len(df))
col2.metric("⚠️ High Risk Users", (df["RiskLevel"] == "High").sum())
col3.metric("📉 Avg Risk Score", round(df["RiskScore"].mean(), 2))
col4.metric("💰 Avg Savings Rate", round(df["SavingsRate"].mean(), 2))

st.markdown("---")

# ---------------- TOP USERS ---------------- #
st.subheader("🔥 Top Risk Users")

top_users = df.sort_values(by="RiskScore", ascending=False).head(10)

st.dataframe(
    top_users,
    use_container_width=True,
    height=400
)

# ---------------- CHARTS ---------------- #
st.subheader("📈 Risk Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Risk Distribution")
    st.bar_chart(df["RiskLevel"].value_counts())

with col2:
    st.markdown("### Risk Score by User")
    st.bar_chart(df.set_index("User")["RiskScore"])

st.markdown("---")

# ---------------- CATEGORY ANALYSIS ---------------- #
try:
    category_df = pd.read_csv("output/top_categories.csv")

    st.subheader("🛒 Category Risk Contribution")
    st.bar_chart(category_df.set_index("Category"))

except:
    st.warning("Category data not available")

# ---------------- FEATURE IMPORTANCE ---------------- #
try:
    importance = pd.read_csv("output/feature_importance.csv")

    st.subheader("🧠 Feature Importance (ML Insights)")
    st.bar_chart(importance.set_index("Feature"))

except:
    st.warning("Feature importance not available")

# ---------------- FOOTER ---------------- #
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: grey;'>
    Built using AI, Machine Learning & Data Analytics 🚀
    </p>
    """,
    unsafe_allow_html=True
)