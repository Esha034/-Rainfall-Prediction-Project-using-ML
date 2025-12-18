import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Rainfall Prediction App", layout="centered")

st.title("🌧️ Rainfall Prediction System")

# Load model
with open("model/rainfall_prediction_model.pkl", "rb") as file:
    model_data = pickle.load(file)

model = model_data["model"]
feature_names = model_data["feature_names"]

st.subheader("Enter Weather Details")

pressure = st.number_input("Pressure", value=1015.9)
dewpoint = st.number_input("Dew Point", value=19.9)
humidity = st.number_input("Humidity", value=95.0)
cloud = st.number_input("Cloud", value=81.0)
sunshine = st.number_input("Sunshine", value=0.0)
winddirection = st.number_input("Wind Direction", value=40.0)
windspeed = st.number_input("Wind Speed", value=13.7)

if st.button("Predict Rainfall"):
    input_data = pd.DataFrame([[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]],
                              columns=feature_names)
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("🌧️ Rainfall Expected")
    else:
        st.info("☀️ No Rainfall Expected")
