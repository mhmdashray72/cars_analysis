import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Insights Dashboard")

df = pd.read_csv("USA_cars_datasets.csv")

# Sidebar Filters
st.sidebar.header("Filters")

selected_brand = st.sidebar.multiselect(
    "Select Brand",
    options=df['brand'].unique(),
    default=df['brand'].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df['year'].min()),
    int(df['year'].max()),
    (
        int(df['year'].min()),
        int(df['year'].max())
    )
)

filtered_df = df[
    (df['brand'].isin(selected_brand)) &
    (df['year'].between(year_range[0], year_range[1]))
]

# KPIs
st.markdown("## 📌 KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Cars", filtered_df.shape[0])
col2.metric("Average Price", f"${filtered_df['price'].mean():,.0f}")
col3.metric("Max Price", f"${filtered_df['price'].max():,.0f}")
col4.metric("Average Mileage", f"{filtered_df['mileage'].mean():,.0f}")

# Charts
st.markdown("## 📈 Price Distribution")

fig1 = px.histogram(
    filtered_df,
    x='price',
    nbins=40,
    title='Price Distribution'
)

st.plotly_chart(fig1, use_container_width=True)

# Brand Count
st.markdown("## 🚘 Top Brands")

brand_count = filtered_df['brand'].value_counts().reset_index()
brand_count.columns = ['Brand', 'Count']

fig2 = px.bar(
    brand_count,
    x='Brand',
    y='Count',
    title='Top Brands'
)

st.plotly_chart(fig2, use_container_width=True)

# Year vs Price
st.markdown("## 📅 Year vs Price")

fig3 = px.scatter(
    filtered_df,
    x='year',
    y='price',
    color='brand',
    title='Year vs Price'
)

st.plotly_chart(fig3, use_container_width=True)

# Mileage vs Price
st.markdown("## 🛣 Mileage vs Price")

fig4 = px.scatter(
    filtered_df,
    x='mileage',
    y='price',
    color='brand',
    title='Mileage vs Price'
)

st.plotly_chart(fig4, use_container_width=True)
