import streamlit as st
import pickle
import numpy as np

# Load model

model = pickle.load(open("model.pkl", "rb"))

# Title

st.title("📊 Economic Growth Predictor")

st.write("Enter the values below:")

# Inputs

inflation = st.number_input("Inflation (%)", value=5.0)
unemployment = st.number_input("Unemployment (%)", value=6.0)
life_exp = st.number_input("Life Expectancy", value=70.0)
education = st.number_input("Education (%)", value=50.0)

# Button

if st.button("Predict GDP Growth"):
    input_data = np.array([[inflation, unemployment, life_exp, education]])
    prediction = model.predict(input_data)
    st.success(f"Predicted GDP Growth: {prediction[0]:.2f}%")
