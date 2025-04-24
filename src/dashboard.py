import streamlit as st
import pandas as pd
import joblib
from feature_engineering import preprocess, scatter_plot_risk
from recommender import recommend_actions
from data_loader import load_data


# UI
st.title("📉 SaaS Customer Churn Prediction")
file = st.file_uploader("Upload Customer Data CSV", type=["csv"])

if file:
    df = load_data(file)
    df_prep, _, _ = preprocess(df)
    model = joblib.load("../model.pkl")
    results = recommend_actions(df_prep, model)

    # הוספת העמודה avg_monthly_charge מתוך df_prep
    results['avg_monthly_charge'] = df_prep['avg_monthly_charge']

    st.subheader("📋 Churn Risk Recommendations:")
    st.write(results)
    csv = results.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Recommendations as CSV",
        data=csv,
        file_name='recommendations.csv',
        mime='text/csv',
    )

    st.subheader("📊 Visualizing Risk vs. Monthly Charge")
    fig = scatter_plot_risk(results)
    st.plotly_chart(fig, use_container_width=True)

