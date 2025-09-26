import streamlit as st
import requests

st.title("Bank Churn Prediction")
st.write("Check if you are likely to leave the bank or stay.")
credit_score = st.number_input("Credit Score", 0, 1000, 650)
age = st.number_input("Age", 18, 100, 40)
geo = st.selectbox("Country", ["France", "Spain", "Germany"])
tenure = st.number_input("Tenure (years with the bank)", 0, 10, 3)
balance = st.number_input("Account Balance", 0.0, 1e7, 50000.0)
num = st.number_input("Number of Products", 1, 10, 1)
has_card = st.selectbox("Do you have a credit card?", [0, 1])
active = st.selectbox("Are you an active member?", [0, 1])
salary = st.number_input("Estimated Salary", 0.0, 1e7, 60000.0)

if st.button("Predict"):
    payload = {
        "CreditScore": credit_score,
        "Geography": geo,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num,
        "HasCrCard": has_card,
        "IsActiveMember": active,
        "EstimatedSalary": salary
    }
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    result = response.json()
    if result.get("prediction") == "Leave":
        st.warning("We are sorry to see you go.")
    else:
        st.success("Congratulations! You are likely to stay with the bank.")