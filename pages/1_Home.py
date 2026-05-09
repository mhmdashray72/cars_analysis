import streamlit as st
import pandas as pd

st.title("🏠 Home Page")

df = pd.read_csv("USA_cars_datasets.csv")

st.image(
    "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7",
    use_container_width=True
)

st.markdown("## 📌 Project Overview")

st.write("""
This project analyzes the USA Cars Dataset.

### Objectives:
- Clean the data
- Extract insights
- Build ML models
- Predict car prices
""")

st.markdown("## 📊 Dataset Information")

col1, col2, col3 = st.columns(3)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Brands", df['brand'].nunique())

st.markdown("## 🔍 Sample Data")

st.dataframe(df.head())
