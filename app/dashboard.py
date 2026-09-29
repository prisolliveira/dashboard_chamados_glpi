import streamlit as st
import pandas as pd
import plotly.express as px
from style import CUSTOM_CSS

df = pd.read_csv("../dados/chamados_glpi_tratados.csv", sep=";")

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
st.set_page_config(layout="wide")

# CABEÇALHO

st.title("Painel de Chamados de Monitoramento")
st.caption("Prefeitura de Goianira · Dados extraídos em 10/09/2026")
st.caption("Período de análise: últimos 6 meses (março a setembro de 2026)")

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

card1, card2, card3, card4 = st.columns(4, gap="small")

card1.metric(label="Total", value=total_chamados)
card2.metric(label="Solucionados", value=f"{total_solucionados:.1f}%")
card3.metric(label="Tempo médio", value=f"{dias}d {horas}h")
card4.metric(label="Em andamento", value=total_andamento)

# GRÁFICOS
# 1) gráfico de chamados por equipamento

st.subheader("Chamados por Equipamento")

eq_possiveis = ["CAMERA", "DVR", "NVR", "SPEED", "ALARME"]
eq_contagem = {}

for eq in eq_possiveis:
    eq_contagem[eq] = df["Equipamento"].str.contains(eq, na=False).sum()

eq_confere = df["Equipamento"].str.contains("|".join(eq_possiveis), na=False)
eq_contagem["OUTROS"] = (~eq_confere).sum() # ~ Inversao de valor lógico

contagem_equipamento = pd.DataFrame(list(eq_contagem.items()), columns=["Equipamento", "Quantidade"])

equipamentos = contagem_equipamento[contagem_equipamento["Equipamento"] != "OUTROS"].sort_values("Quantidade", ascending=True)
outros_eq = contagem_equipamento[contagem_equipamento["Equipamento"] == "OUTROS"]

eq_contagem_ordenada = pd.concat([outros_eq, equipamentos])

grafico_equipamento = px.bar(
    eq_contagem_ordenada, # atribui os dados
    x="Quantidade",
    y="Equipamento",
    orientation="h",
    text="Quantidade" # texto das barras
)

grafico_equipamento.update_traces(textposition="outside") # define o texto para fora das barras
grafico_equipamento.update_layout( # retira o nome dos eixos
    xaxis_title="",
    yaxis_title="",
    xaxis=dict(showticklabels=False) # retira números do eixo X
)

st.plotly_chart(grafico_equipamento)

# 2) gráfico de chamados por unidade/setor

st.subheader("Chamados por Localização")
opcao = st.radio( # seletor que alterna
    "Visualizar por:",
    options = ["Unidade", "Setor"],
    horizontal = True
)

loc_contagem = df[opcao].value_counts().reset_index()
loc_contagem.columns = [opcao, "Quantidade"]

locais = loc_contagem[loc_contagem[opcao] != "NAO IDENTIFICADO"].sort_values("Quantidade", ascending=True)
nao_identificado_loc = loc_contagem[loc_contagem[opcao] == "NAO IDENTIFICADO"]

loc_contagem_ordenada = pd.concat([nao_identificado_loc, locais])

grafico_local = px.bar(
    loc_contagem_ordenada,
    x="Quantidade",
    y=opcao,
    orientation="h",
    title=f"Chamados por {opcao}",
    text="Quantidade"
)

grafico_local.update_traces(textposition="outside") 
grafico_local.update_layout(
    xaxis_title="",
    yaxis_title="",
    xaxis=dict(showticklabels=False)
)

st.plotly_chart(grafico_local)