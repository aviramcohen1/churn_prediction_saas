import streamlit as st
import pandas as pd
import joblib
from src.feature_engineering import preprocess
from src.recommender import recommend_actions
from src.data_loader import load_data

# UI
st.title("📉 SaaS Customer Churn Prediction")
file = st.file_uploader("Upload Customer Data CSV", type=["csv"])

if file:
    df = load_data(file)
    df_prep, _, _ = preprocess(df)
    model = joblib.load("model.pkl")
    results = recommend_actions(df_prep, model)
    st.write(results)
