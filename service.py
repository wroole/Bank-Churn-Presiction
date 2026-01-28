from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("bank_churn.joblib")
class Client(BaseModel):
    CreditScore: int
    Geography: str
    Age: int
    Tenure:int
    Balance:float
    NumOfProducts:int
    HasCrCard:int
    IsActiveMember:int
    EstimatedSalary:float
    SatisfactionScore:float
    CardType:str
    PointEarned:int

@app.post("/predict")
def predict(data: Client):
    features_df = pd.DataFrame([data.dict()])
    churn = int(model.predict(features_df)[0])
    return {
        'prediction': "Leave" if churn == 1 else "Stay"
    }