import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

st.header('Informacion Importante')

# crear un histograma
fig = px.histogram(car_data, x="odometer")

# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_disp = st.checkbox('Construir grafico de dispersion')

if build_disp:  # si la casilla de verificación está seleccionada
    st.write('Construir grafico de dispersion para la columna odómetro')


st.header('Informacion con grafico de dispersión ')
if build_disp:  # al hacer clic en el botón

    st.write('Creación de grafico de dispersión para el conjunto de datos de anuncios de venta de coches')

# crear un gráfico de dispersión
fig = px.scatter(car_data, x="odometer", y="price")
fig.show()  # crear gráfico de dispersión
st.plotly_chart(fig, use_container_width=True)
