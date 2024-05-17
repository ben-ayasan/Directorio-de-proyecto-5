import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button(
    'Haz click aqui para construir histograma')  # crear un botón

st.header('Informacion Importante')
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button(
    'Haz click aqui para construir grafica de dispersión')
st.header('Informacion con grafico de dispersión ')
if hist_button:  # al hacer clic en el botón

    st.write('Creación de grafico de dispersión para el conjunto de datos de anuncios de venta de coches')

# crear un gráfico de dispersión
fig = px.scatter(car_data, x="odometer", y="price")
fig.show()  # crear gráfico de dispersión
st.plotly_chart(fig, use_container_width=True)
