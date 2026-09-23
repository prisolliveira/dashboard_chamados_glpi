import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("../dados/chamados_glpi_tratados.csv", sep=";")

st.title("Dashboard de Chamados - Monitoramento")
st.write(df.head())