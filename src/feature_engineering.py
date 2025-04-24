import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import plotly.express as px

def preprocess(df):
    df = df.copy()

    # המרת churn ל-0/1
    df['churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # שינוי שמות עמודות
    df.rename(columns={
        'customerID': 'customer_id',
        'tenure': 'account_age_days',
        'MonthlyCharges': 'monthly_usage',
        'Contract': 'customer_segment'
    }, inplace=True)

    # תכונה חדשה: avg_monthly_charge = TotalCharges / tenure
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['avg_monthly_charge'] = df['TotalCharges'] / df['account_age_days']
    df['avg_monthly_charge'] = df['avg_monthly_charge'].fillna(0)

    # תכונות בינאריות נוספות
    df['is_long_term'] = (df['customer_segment'] == 'Two year').astype(int)
    df['has_tech_support'] = (df['TechSupport'] == 'Yes').astype(int)

    # קידוד ושינוי עמודות מספריות
    le = LabelEncoder()
    df['customer_segment'] = le.fit_transform(df['customer_segment'])

    numerical = ['account_age_days', 'monthly_usage', 'avg_monthly_charge']
    scaler = StandardScaler()
    df[numerical] = scaler.fit_transform(df[numerical])

    return df[[
        'customer_id',
        'account_age_days',
        'monthly_usage',
        'avg_monthly_charge',
        'customer_segment',
        'is_long_term',
        'has_tech_support',
        'churn'
    ]], scaler, le


def scatter_plot_risk(df_with_risk):
    fig = px.scatter(
        df_with_risk,
        x='avg_monthly_charge',
        y='churn_risk',
        color='recommendation',
        hover_data=['customer_id'],
        title='Churn Risk vs. Average Monthly Charge'
    )
    return fig
