import pandas as pd

REQUIRED_COLUMNS = [
    'customer_id',
    'last_login',
    'support_tickets',
    'account_age_days',
    'monthly_usage',
    'customer_segment',
    'churn'
]

try:
    df = pd.read_csv('data/saas_data.csv')
    print("\n✅ הקובץ נטען בהצלחה!")
    print("\n📋 העמודות שנמצאו בקובץ:")
    print(df.columns.tolist())

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        print("\n❌ העמודות הבאות חסרות בקובץ:")
        print(missing)
    else:
        print("\n🎯 כל העמודות הנדרשות קיימות. אפשר להמשיך!")

    print("\n🔍 הצצה לשורות הראשונות:")
    print(df.head())

except FileNotFoundError:
    print("❌ הקובץ 'data/saas_data.csv' לא נמצא. ודא שהוא קיים בתיקייה הנכונה.")
except Exception as e:
    print(f"⚠️ שגיאה: {e}")
