import streamlit as st
import pandas as pd
import joblib

st.title("🤖 Car Price Prediction")

#model = joblib.load("model.pkl")

df = pd.read_csv("USA_cars_datasets.csv")

# Inputs
brand = st.selectbox(
    "Select Brand",
    df['brand'].unique()
)

year = st.slider(
    "Year",
    int(df['year'].min()),
    int(df['year'].max()),
    2018
)

mileage = st.number_input(
    "Mileage",
    min_value=0,
    value=10000
)

condition = st.slider(
    "Condition Days",
    1,
    50,
    10
)

# Prediction
if st.button("Predict Price"):

    input_df = pd.DataFrame({
        'brand': [brand],
        'year': [year],
        'mileage': [mileage],
        'condition_days': [condition]
    })

    prediction = model.predict(input_df)

    st.success(f"Estimated Car Price: ${prediction[0]:,.2f}")
