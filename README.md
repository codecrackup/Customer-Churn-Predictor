# 📡 Telco Customer Churn Predictor

🚀 **[Live Demo →](https://customer-churn-predictor-08.streamlit.app/)**

A basic **Machine Learning classification project** that predicts whether a telecom customer is likely to churn.

This project was built to practice the complete ML workflow, from preprocessing and model training to evaluation and deployment.

> This is intentionally a simple project and serves as a starting point for practicing end-to-end Machine Learning.

## 🧠 What I Practiced

- EDA
- Feature Engineering
- One-Hot Encoding
- Power Transformation
- ColumnTransformer
- ML Pipelines
- Logistic Regression
- Cross-Validation
- Classification Metrics
- Probability Prediction
- Model Deployment with Streamlit

## 🤖 Model

**Logistic Regression**

Preprocessing:
- One-Hot Encoding for categorical features
- Power Transformation for the numerical feature

## 📊 Performance

| Metric | Score |
|---|---:|
| Accuracy | 80.1% |
| Precision | 65.7% |
| Recall | 53.1% |
| F1 Score | 58.6% |
| ROC-AUC | 85.0% |

## 🛠️ Tech Stack

Python · Pandas · NumPy · Scikit-learn · Streamlit · Joblib

## 🚀 Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
