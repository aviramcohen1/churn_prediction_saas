from src.data_loader import load_data
from src.feature_engineering import preprocess
from src.model import train_model
from src.recommender import recommend_actions

if __name__ == '__main__':
    df = load_data("data/saas_data.csv")
    df_prep, _, _ = preprocess(df)
    model = train_model(df_prep)
    recs = recommend_actions(df_prep, model)
    print("\nSample Recommendations:")
    print(recs.head())

