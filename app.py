
import pandas as pd
import streamlit as st
import plotly_express as px

# Crear el encabezado de la aplicación
st.header('Aplicación basada en Streamlit')

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear botones para generar gráficos
hist_button = st.button('Construir histograma')
scat_button = st.button('Construir gráfico de dispersión')

# Si se presiona el botón del histograma
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Si se presiona el botón del gráfico de dispersión
if scat_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)


