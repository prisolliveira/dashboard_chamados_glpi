import streamlit as st
import pandas as pd
import plotly.express as px
from style import CUSTOM_CSS

df = pd.read_csv("../dados/chamados_glpi_tratados.csv", sep=";")

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# CABEÇALHO

st.title("Painel de Chamados de Monitoramento")
st.caption("Prefeitura de Goianira · Dados extraídos em 10/09/2026")

# KPI CARDS

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

# GRÁFICOS
# gráfico de chamados por equipamento

eq_possiveis = ["CAMERA", "DVR", "NVR", "SPEED", "ALARME"]
contagem_final = {}

for eq in eq_possiveis:
    contagem_final[eq] = df["Equipamento"].str.contains(eq, na=False).sum()

contagem_equipamento = pd.DataFrame(list(contagem_final.items()), columns=["Equipamento", "Quantidade"])

grafico = px.bar(
    contagem_equipamento.sort_values("Quantidade", ascending=True),
    x="Quantidade",
    y="Equipamento",
    orientation="h",
    title="Chamados por Equipamento",
    text="Quantidade"
)

grafico.update_traces(textposition="outside")
grafico.update_layout(
    xaxis=dict(range=[0, 200])
)

st.plotly_chart(grafico)