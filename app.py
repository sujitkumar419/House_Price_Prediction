import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("full_model.pkl", "rb") as f:
    final_model = pickle.load(f)

# Load column names (saved from Notebook)
with open("columns.pkl", "rb") as f:
    columns = pickle.load(f)

st.title("🏡 House Price Prediction (Full Model)")

# Example inputs
LotArea = st.number_input("Lot Area (sq ft)", min_value=1000, max_value=100000, value=8000)
OverallQual = st.slider("Overall Quality (1-10)", 1, 10, 5)
YearBuilt = st.number_input("Year Built", min_value=1800, max_value=2025, value=2000)
GrLivArea = st.number_input("Living Area (sq ft)", min_value=500, max_value=5000, value=1500)
GarageCars = st.slider("Garage Cars", 0, 4, 2)

# Create input row with all columns (no X here!)
input_data = pd.DataFrame([[0]*len(columns)], columns=columns)

# Overwrite selected features
input_data["LotArea"] = LotArea
input_data["OverallQual"] = OverallQual
input_data["YearBuilt"] = YearBuilt
input_data["GrLivArea"] = GrLivArea
input_data["GarageCars"] = GarageCars

if st.button("Predict Price"):
    price = final_model.predict(input_data)[0]
    st.success(f"Predicted House Price: ${price:,.2f}")
