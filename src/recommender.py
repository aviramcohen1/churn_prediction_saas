def recommend_actions(df, model):
    df = df.copy()
    df['churn_risk'] = model.predict_proba(df.drop(columns=['churn', 'customer_id']))[:, 1]  # הסר גם את customer_id
    df['recommendation'] = df['churn_risk'].apply(lambda r: 'Call Customer' if r > 0.7 else ('Send Discount Offer' if r > 0.4 else 'No Action'))
    return df[['customer_id', 'churn_risk', 'recommendation']]
