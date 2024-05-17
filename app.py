import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
# crear un botón

st.header('Informacion de kilometraje de vehiculos')
if hist_button:

    build_histogram = st.checkbox('Construir un histograma')
# al hacer clic en el botón
build_scatter = st.checkbox('Construir un diagrama de dispersión')
# escribir un mensaje
if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
elif build_scatter:
    st.write('Construir un diagrama de dispersión de precios y kilometraje')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig)
