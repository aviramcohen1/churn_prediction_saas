# 📊 SaaS Customer Churn Prediction

This project is a complete, production-ready example of a **Customer Churn Prediction System** for a SaaS company. It includes data preprocessing, model training, churn risk scoring, and personalized action recommendations—all with a clean Streamlit dashboard.

---

## 🚀 Features
- Gradient Boosting model for churn prediction
- Feature engineering with encoding and scaling
- Personalized recommendations based on churn risk:
  - Call Customer
  - Send Discount Offer
  - No Action
- Streamlit dashboard for real-time interaction
- Export recommendations as downloadable CSV
- Modular and readable codebase

---

## 📁 Project Structure
```
churn_prediction_saas/
├── src/
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── recommender.py
│   └── dashboard.py
├── main.py
├── requirements.txt
├── .gitignore
├── dashboard_screenshot.png
└── README.md
```
> 🔹 Place your `saas_data.csv` in a local `data/` folder for training & dashboard.  
> (This file is not included in the repository.)

---

## 📦 Installation
```bash
git clone https://github.com/aviramcohen1/churn_prediction_saas.git
cd churn_prediction_saas
pip install -r requirements.txt
```

---

## 📈 Run Model Training
```bash
python main.py
```

---

## 📊 Launch Dashboard
```bash
streamlit run src/dashboard.py
```

Then open the link (usually http://localhost:8501/) and upload your `saas_data.csv` file.

---

## 🖼 Dashboard Example

Below is a screenshot showing both recommendations and the churn risk visualization:

![Dashboard Screenshot](dashboard_screenshot.png)

---

## 📄 Sample Data Source
- Kaggle: [Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Rename it to `saas_data.csv` and place inside a local `data/` folder (not tracked in Git).

---

Made with ❤️ by Aviram

