import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess(df):
    df = df.copy()

    # המרת churn ל-0/1
    df['churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # המרת שמות עמודות תואמות
    df.rename(columns={
        'customerID': 'customer_id',
        'tenure': 'account_age_days',
        'MonthlyCharges': 'monthly_usage',
        'Contract': 'customer_segment'
    }, inplace=True)

    le = LabelEncoder()
    df['customer_segment'] = le.fit_transform(df['customer_segment'])

    numerical = ['account_age_days', 'monthly_usage']
    scaler = StandardScaler()
    df[numerical] = scaler.fit_transform(df[numerical])

    return df[['customer_id', 'account_age_days', 'monthly_usage', 'customer_segment', 'churn']], scaler, le