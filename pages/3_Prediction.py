import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

st.title("🤖 Car Price Prediction")

# Load Data
df = pd.read_csv("USA_cars_datasets.csv")

# Cleaning
df['condition_days'] = (
    df['condition']
    .str.extract('(\\d+)')
    .astype(float)
)

df.drop(
    columns=['Unnamed: 0', 'vin', 'lot', 'country', 'condition'],
    inplace=True
)

# Features & Target
X = df.drop(columns=['price'])
y = df['price']

# Columns
categorical_cols = X.select_dtypes(include='object').columns
numeric_cols = X.select_dtypes(exclude='object').columns

# Preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        (
            'cat',
            OneHotEncoder(handle_unknown='ignore'),
            categorical_cols
        ),
        (
            'num',
            'passthrough',
            numeric_cols
        )
    ]
)

# Model
model = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor())
])

# Train
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model.fit(X_train, y_train)

# Inputs
brand = st.selectbox(
    "Brand",
    sorted(df['brand'].unique())
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

# Predict
if st.button("Predict Price"):

    input_df = pd.DataFrame({
        'brand': [brand],
        'year': [year],
        'mileage': [mileage],
        'condition_days': [condition]
    })

    prediction = model.predict(input_df)

    st.success(
        f"Estimated Price: ${prediction[0]:,.2f}"
    )
