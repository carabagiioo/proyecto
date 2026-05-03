import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

st.header("Análisis de Vehículos en Venta")

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón original para el odómetro
hist_button = st.button('Construir histograma de Odómetro')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.divider()
st.header("Exploración Adicional de Datos")

# Usaremos checkboxes (casillas de verificación) para que sea más fácil ver varios gráficos a la vez
build_year_hist = st.checkbox('Mostrar Distribución del Año de los Coches')
if build_year_hist:
    st.write('Distribución de vehículos según el año del modelo:')
    fig = go.Figure(data=[go.Histogram(x=car_data['model_year'].dropna())])
    fig.update_layout(title_text='Distribución del Año de los Coches',
                      xaxis_title='Año', yaxis_title='Frecuencia')
    st.plotly_chart(fig, use_container_width=True)

build_price_hist = st.checkbox('Mostrar Distribución de Precio')
if build_price_hist:
    st.write('Distribución de vehículos según su precio:')
    fig = go.Figure(data=[go.Histogram(x=car_data['price'].dropna())])
    fig.update_layout(title_text='Distribución de Precio',
                      xaxis_title='Precio', yaxis_title='Frecuencia')
    st.plotly_chart(fig, use_container_width=True)

build_trans_hist = st.checkbox('Mostrar Distribución de Transmisión')
if build_trans_hist:
    st.write('Tipos de transmisión de los vehículos:')
    fig = go.Figure(data=[go.Histogram(x=car_data['transmission'].dropna())])
    fig.update_layout(title_text='Distribución de la Transmisión',
                      xaxis_title='Transmisión', yaxis_title='Cantidad')
    st.plotly_chart(fig, use_container_width=True)

build_4wd_hist = st.checkbox('Mostrar Distribución de Tracción 4WD')
if build_4wd_hist:
    st.write('Vehículos con y sin tracción 4WD (1.0 = Sí, 0.0 = No):')
    car_data['is_4wd'] = car_data['is_4wd'].fillna(0)
    fig = go.Figure(data=[go.Histogram(x=car_data['is_4wd'].astype(str))])
    fig.update_layout(title_text='Distribución de Vehículos con Tracción 4WD',
                      xaxis_title='Es 4WD', yaxis_title='Cantidad')
    st.plotly_chart(fig, use_container_width=True)

build_condition_hist = st.checkbox('Mostrar Distribución de la Condición')
if build_condition_hist:
    st.write('Condición de los vehículos en venta:')
    fig = go.Figure(data=[go.Histogram(x=car_data['condition'].dropna())])
    fig.update_layout(title_text='Distribución de la Condición de los Vehículos',
                      xaxis_title='Condición', yaxis_title='Cantidad')
    st.plotly_chart(fig, use_container_width=True)

build_box_plot = st.checkbox('Relación entre Condición y Año del Coche')
if build_box_plot:
    st.write('Distribución de los años del modelo según la condición del vehículo:')
    fig = go.Figure()
    conditions = car_data['condition'].dropna().unique()
    for condition in conditions:
        fig.add_trace(go.Box(
            y=car_data[car_data['condition'] ==
                       condition]['model_year'].dropna(),
            name=condition
        ))
    fig.update_layout(title_text='Relación entre Condición y Año de los Coches',
                      yaxis_title='Año del Modelo', xaxis_title='Condición')
    st.plotly_chart(fig, use_container_width=True)
