from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load('rent_api/model/house_rent_model.pkl')

# Define the input data model
class RentRequest(BaseModel):
    Size: int
    BHK: int
    Bathroom: int
    Current_Floor: int
    Total_Floors: int
    Area_Type: str
    Furnishing_Status: str
    Tenant_Preferred: str
    City: str


@app.get("/")
def read_root():
    return {"message": "House Rent Prediction API is live!"}

@app.post("/predict_rent")
def predict_rent(data: RentRequest):
    try:
        df = pd.DataFrame([data.dict()])
        rent = model.predict(df)[0]
        return {"Predicted_Rent": round(rent, 2)}
    except Exception as e:
        return {"error": str(e)}

