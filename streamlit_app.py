import streamlit as st 
import pickle 

#load model
model = pickle.load(open("models/model.pkl", "rb"))

st.title("🏠 House price Predictor")

area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
location = st.number_input("Location (0=suburban, 1=urban)")

if st.button("Predict"):
    result = model.predict([[area, bedrooms, bathrooms, location]])
    st.success(f"Predicted Price: {result[0]:,.0f}")