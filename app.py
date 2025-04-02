
import pandas as pd
import streamlit as st
import plotly_express as px

# Crear el encabezado de la aplicación
st.header('Aplicación basada en Streamlit')

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Casillas de verificación para mostrar gráficos
show_hist = st.checkbox('Construir histograma')
show_scatter = st.checkbox('Construir gráfico de dispersión')

if show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if show_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)



