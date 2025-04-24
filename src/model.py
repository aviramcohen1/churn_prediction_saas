from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report
import joblib

def train_model(df):
    X = df.drop(columns=['churn', 'customer_id'])  # הסר גם את customer_id
    y = df['churn']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = GradientBoostingClassifier()
    model.fit(X_train, y_train)

    print("\nEvaluation Report:")
    print(classification_report(y_test, model.predict(X_test)))

    joblib.dump(model, 'model.pkl')
    return model