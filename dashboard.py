import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="AgroVision Dashboard", layout="wide")
st.title("📊 AgroVision Crop Data Dashboard")

# Load dataset
df = pd.read_csv("../Crop_recommendation.csv")

# Crop frequency
st.subheader("🌱 Crop Frequency")
st.bar_chart(df["label"].value_counts())

# Correlation heatmap
st.subheader("📊 Correlation Heatmap")
st.pyplot(sns.heatmap(df.drop("label", axis=1).corr(), annot=True, cmap="coolwarm").figure)

# pH distribution
st.subheader("🌿 Soil pH Distribution")
st.pyplot(sns.histplot(df["ph"], kde=True, color="green").figure)
