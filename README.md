# 🌾 AgroVision - AI-Powered Crop Recommendation System

AgroVision is a smart crop prediction system powered by Machine Learning and AI. It helps farmers and agricultural analysts identify the **most suitable crop** based on **soil nutrients, environmental conditions**, and even **real-time weather data** using OpenWeatherMap API.

![AgroVision Screenshot](https://user-images.githubusercontent.com/your-screenshot.png)

---

## 🚀 Features

- ✅ Predicts the best crop to grow using ML models (Random Forest & XGBoost)
- ✅ Uses real-time temperature and humidity from any city (OpenWeatherMap)
- ✅ Simple, user-friendly interface powered by Streamlit
- ✅ Visual dashboard (coming soon!) for data insights
- ✅ Ready for deployment via Streamlit Cloud or Heroku

---

## 📊 Input Parameters

- Nitrogen (N)
- Phosphorous (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- pH Level
- Rainfall (mm)
- [Optional] City for live weather input

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Models**: XGBoost, Random Forest (trained in Google Colab)
- **APIs**: OpenWeatherMap (live weather)

---

## 🧪 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/phemlata/AgroVision.git
   cd AgroVision
