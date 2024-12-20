import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Analisis de datos de Vehiculos en EU')

grafic_button = st.button("Make a Histogram")

