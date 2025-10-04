import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("crop_model.pkl")

st.set_page_config(page_title="🌱 AgriBot", page_icon="🌾", layout="centered")

st.title("🌱 AgriBot – Crop Suitability Chatbot")
st.write("Enter your field conditions and I’ll predict if it’s suitable for planting.")

# Input fields
rain = st.number_input("🌧️ Average Monthly Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0)
temp = st.number_input("🌡️ Average Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
fert = st.number_input("🌍 Soil Fertility Index (5–30)", min_value=0.0, max_value=50.0, value=20.0)

# Predict button
if st.button("Check Suitability ✅"):
    user_data = np.array([[rain, temp, fert]])
    prediction = model.predict(user_data)[0]

    if prediction == 1:
        st.success("✅ Conditions look GOOD for planting! 🌾")
    else:
        st.error("❌ Conditions may NOT be suitable. Consider waiting.")