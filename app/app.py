# app.py
import streamlit as st
import pandas as pd
import requests

st.title("🏠 House Rent Prediction")

user_input = {
    "Size": st.number_input("Size (sq ft)", 100, 10000, 1000),
    "BHK": st.slider("BHK", 1, 5, 2),
    "Bathroom": st.slider("Bathroom", 1, 5, 2),
    "Current_Floor": st.number_input("Current Floor", 0, 50, 2),
    "Total_Floors": st.number_input("Total Floors", 1, 50, 10),
    "Area_Type": st.selectbox("Area Type", ["Super Area", "Carpet Area", "Built Area"]),
    "Furnishing_Status": st.selectbox("Furnishing Status", ["Furnished", "Unfurnished", "Semi-Furnished"]),
    "Tenant_Preferred": st.selectbox("Tenant Preferred", ["Bachelors", "Family", "Bachelors/Family"]),
    "City": st.selectbox("City", ["Bangalore", "Mumbai", "Chennai", "Delhi", "Hyderabad"])
}

if st.button("Predict"):
    response = requests.post("https://ai-rent-checker.onrender.com/predict_rent", json=user_input)
    st.success(f"Estimated Rent: ₹ {response.json()['predicted_rent']}")
