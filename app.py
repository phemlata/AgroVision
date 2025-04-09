import streamlit as st
import pickle
import numpy as np
import requests

# 🌤 Fetch weather data
def fetch_weather(city):
    api_key = "da8e1ed2c0ecff1a26c371b81cdd91ed"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()

    # Basic error handling
    if response.get("cod") != 200:
        return None, None

    temp = response["main"]["temp"]
    humidity = response["main"]["humidity"]
    return temp, humidity

# 🔍 Load model & label encoder
model = pickle.load(open("xgboost_model.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

# 🧠 UI Setup
st.set_page_config(page_title="AgroVision", layout="centered")
st.title("🌾 AgroVision - Crop Recommendation")
st.markdown("Predict the best crop to grow based on environmental & soil conditions.")

# 🧾 Weather Integration
st.subheader("🌤 Live Weather (optional)")
city = st.text_input("Enter your city name:")
use_weather = st.checkbox("Use live temperature & humidity from weather")

# 🧾 Input form
with st.form("crop_form"):
    N = st.slider("Nitrogen (N)", 0, 140, 90)
    P = st.slider("Phosphorous (P)", 5, 145, 42)
    K = st.slider("Potassium (K)", 5, 205, 43)

    # Default sliders
    temperature = st.slider("Temperature (°C)", 10.0, 45.0, 25.0)
    humidity = st.slider("Humidity (%)", 10.0, 100.0, 60.0)

    ph = st.slider("pH Level", 3.5, 9.5, 6.5)
    rainfall = st.slider("Rainfall (mm)", 20.0, 300.0, 100.0)

    submit = st.form_submit_button("🌱 Predict Crop")

# 📊 Predict Crop
if submit:
    # Override with live weather if selected
    if use_weather and city:
        live_temp, live_humidity = fetch_weather(city)
        if live_temp is not None:
            temperature = live_temp
            humidity = live_humidity
            st.info(f"✅ Using live weather for {city.title()}: {temperature}°C, {humidity}% humidity")
        else:
            st.warning("⚠️ Could not fetch weather data. Please check city name.")

    # Prepare input & predict
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]
    crop_name = label_encoder.inverse_transform([prediction])[0]

    st.success(f"✅ Recommended Crop: **{crop_name.capitalize()}**")
