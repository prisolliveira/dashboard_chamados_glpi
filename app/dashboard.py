import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("../dados/chamados_glpi_tratados.csv", sep=";")

st.markdown("""
    <style>
    div[data-testid="stMetric"] {
        background-color: transparent;
        border: none;
        padding: 10px 0px;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 13px;
        font-weight: 400;
        color: #888888;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }  
    div[data-testid="stMetricValue"] {
        font-size: 28px;
        font-weight: 600;
        color: #1a1a1a;
    }
    div[data-testid="column"] {
        padding: 0px 15px 0px 0px;
    }
    </style>
""", unsafe_allow_html=True)


st.title("Painel de Chamados de Monitoramento")
st.caption("Prefeitura de Goianira · Dados extraídos em 10/09/2026")

total_chamados = len(df)
total_solucionados = (df["Status"] == "Solucionado").mean() * 100

tempo_solucionados = df[df["Tempo para solução"] != "NAO SOLUCIONADO"]
tempo_solucionados["Tempo para solução"] = pd.to_timedelta(tempo_solucionados["Tempo para solução"])
tempo_solucionados["Tempo para solução"] = tempo_solucionados["Tempo para solução"].dt.total_seconds() / 3600

tempo_medio = tempo_solucionados["Tempo para solução"].mean()
dias = int(tempo_medio // 24)
horas = int(tempo_medio % 24)

total_andamento = (df["Status"] == "Em atendimento (atribuído)").sum()

cl1, cl2, cl3, cl4 = st.columns(4, gap="small")

cl1.metric(label="Total", value=total_chamados)
cl2.metric(label="Solucionados", value=f"{total_solucionados:.1f}%")
cl3.metric(label="Tempo médio", value=f"{dias}d {horas}h")
cl4.metric(label="Em andamento", value=total_andamento)

