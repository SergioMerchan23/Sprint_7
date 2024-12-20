import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Analisis de datos de Vehiculos en EU')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
     st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')  # escribir un mensaje
            
     # crear un histograma
     fig = px.histogram(car_data, x="odometer")
        
     # mostrar un gráfico Plotly interactivo
     st.plotly_chart(fig, use_container_width=True)

hist_2_button = st.button("Contruir grafica de dispersion")

if hist_2_button:
     
     st.write("Creacion de una grafica de dispersion entre condicion del vehiculo y su precio")

     fig_2 = px.scatter(car_data, x="condition", y="price")

     st.plotly_chart(fig_2, use_container_width=True)