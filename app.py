import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Wine Clustering App", layout="centered")

st.title(" Wine Cluster Prediction")

# Load models
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("pca.pkl", "rb") as f:
    pca = pickle.load(f)

with open("kmeans.pkl", "rb") as f:
    kmeans = pickle.load(f)

# User Input
st.subheader("Enter Wine Properties")

feature_names = [
    "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium",
    "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins",
    "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"
]

default_values = {
    "Alcohol": 13.0,
    "Malic acid": 2.3,
    "Ash": 2.4,
    "Alcalinity of ash": 19.5,
    "Magnesium": 100.0,
    "Total phenols": 2.3,
    "Flavanoids": 2.0,
    "Nonflavanoid phenols": 0.3,
    "Proanthocyanins": 1.5,
    "Color intensity": 5.0,
    "Hue": 1.0,
    "OD280/OD315 of diluted wines": 3.0,
    "Proline": 750.0
}

user_input = {}
for feature in feature_names:
    user_input[feature] = st.number_input(
        feature,
        value=default_values[feature],
        step=0.1,
        format="%.2f"
    )


if st.button("Predict Cluster"):
    input_array = np.array(list(user_input.values())).reshape(1, -1)
    scaled_input = scaler.transform(input_array)
    reduced_input = pca.transform(scaled_input)
    cluster = kmeans.predict(reduced_input)[0]
    
    st.success(f" This wine belongs to **Cluster {cluster}**")

st.markdown("---")

