import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

st.header("Análisis de Vehículos en Venta")

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón
hist_button = st.button('Construir histograma') # al hacer clic en este botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
