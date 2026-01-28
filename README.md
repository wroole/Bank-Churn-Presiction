# Bank Churn Prediction

This project focuses on predicting customer churn in a banking system using machine learning.  
The goal is to identify customers who are likely to leave the bank based on their profile and activity data.

## 📌 Project Overview

Customer churn prediction is a common business problem in the banking sector.  
In this project, a supervised machine learning model is trained on a structured dataset to predict whether a customer will churn.

The project includes:
- Data preprocessing and feature engineering
- Model training and evaluation
- Model serialization
- REST API for predictions
- Simple UI for interaction

## 🧠 Technologies Used

- **Python**
- **Pandas, NumPy** — data manipulation
- **Scikit-learn** — preprocessing and evaluation
- **XGBoost** — machine learning model
- **Joblib** — model saving/loading
- **FastAPI** — backend API
- **Pydantic** — request validation
- **Streamlit** — frontend interface
- **Matplotlib, Seaborn** — data visualization

## 📊 Model Description

- The model is trained using XGBoost
- Dataset preprocessing was improved to ensure better performance
- The same solution approach was kept, but implemented correctly
- The updated model shows improved prediction results

## 📈 Input Features

- *The model uses the following features:*

CreditScore
Geography
Age
Tenure
Balance
NumOfProducts
HasCrCard
IsActiveMember
EstimatedSalary
Satisfaction Score
Card Type
Point Earned

## ✅ Output

- 0 — Customer stays
- 1 — Customer churns