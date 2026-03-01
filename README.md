# Bank Churn Prediction

This project focuses on predicting customer churn in a banking system
using machine learning.\
The goal is to identify customers who are likely to leave the bank based
on their profile and activity data.

## 📌 Project Overview

Customer churn prediction is a common business problem in the banking
sector.\
In this project, a supervised machine learning model is trained on a
structured dataset to predict whether a customer will churn.

The project includes: - Data preprocessing and feature engineering -
Model training and evaluation - Model serialization - REST API for
predictions - Simple UI for interaction

## 🧠 Technologies Used

-   Python
-   Pandas, NumPy
-   Scikit-learn
-   XGBoost
-   Joblib
-   FastAPI
-   Pydantic
-   Streamlit
-   Matplotlib, Seaborn
-   Docker & Docker Compose

## 📊 Model Description

-   The model is trained using XGBoost
-   Dataset preprocessing was improved to ensure better performance
-   The updated model shows improved prediction results

## 📈 Input Features

CreditScore\
Geography\
Age\
Tenure\
Balance\
NumOfProducts\
HasCrCard\
IsActiveMember\
EstimatedSalary\
SatisfactionScore\
CardType\
PointEarned

## ✅ Output

-   0 --- Customer stays\
-   1 --- Customer churns

## 🐳 Docker

The entire application runs inside Docker containers.

-   The backend (FastAPI) and frontend (Streamlit) are containerized.
-   Services are orchestrated using a `docker-compose.yml` file.
-   Docker Compose creates a shared network so the frontend can
    communicate with the backend.

### Run with Docker:

    docker compose up --build

### Access:

-   Frontend: http://localhost:8501\
-   Backend docs: http://localhost:8000/docs

To stop the application:

    docker compose down
