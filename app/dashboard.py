import streamlit as st
import pandas as pd
import plotly.express as px
import locale
from style import CUSTOM_CSS

df = pd.read_csv("../dados/chamados_glpi_tratados.csv", sep=";")

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
st.set_page_config(layout="wide", page_title="Chamados GLPI - Monitoramento", page_icon="📊")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

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

st.markdown(f"""
    <div class="header-wrap">
        <div class="header-left">
            <div class="header-eyebrow">Prefeitura de Goianira · GLPI · 2026</div>
            <div class="header-title">Painel de Chamados de Monitoramento</div>
            <div class="header-sub">Dados extraídos em 10/09/2026 · Período: últimos 9 meses</div>
        </div>
        <div class="header-right">
            <div class="info-item">
                <div class="info-label">Total</div>
                <div class="info-value">{total_chamados}</div>
            </div>
            <div class="info-divider"></div>
            <div class="info-item">
                <div class="info-label">Solucionados</div>
                <div class="info-value">{total_solucionados:.1f}%</div>
            </div>
            <div class="info-divider"></div>
            <div class="info-item">
                <div class="info-label">Tempo médio</div>
                <div class="info-value">{dias}d {horas}h</div>
            </div>
            <div class="info-divider"></div>
            <div class="info-item">
                <div class="info-label">Em andamento</div>
                <div class="info-value">{total_andamento}</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# VISUALIZAÇÕES

# 1) gráfico de linhas de rendimento

st.markdown("### VOLUME DE CHAMADOS POR MÊS")

df["Mês"] = pd.to_datetime(df["Data de abertura"], 
    format="%d/%m/%Y %H:%M", 
    errors="coerce",).dt.to_period("M").astype(str)

chamados_por_mes = df.groupby("Mês").size().reset_index(name="Quantidade")

grafico_volume = px.line(
    chamados_por_mes,
    x="Mês",
    y="Quantidade",
    markers=True

)

grafico_volume.update_layout(
    xaxis_title="",
    yaxis_title=""
    
)

st.plotly_chart(grafico_volume, use_container_width=True, config={"displayModeBar": False})


gf_eq, gf_loc = st.columns(2)

with gf_eq:
    # 2) gráfico de chamados por equipamento

    st.markdown("### CHAMADOS POR EQUIPAMENTO")
    
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
    eq_contagem_ordenada["cor_grupo"] = eq_contagem_ordenada["Equipamento"].apply(
        lambda x: "cinza" if x == "OUTROS" else "normal"
    )

    grafico_equipamento = px.bar(
        eq_contagem_ordenada, # atribui os dados
        x="Quantidade",
        y="Equipamento",
        orientation="h",
        text="Quantidade", # texto das barras
        color="cor_grupo",
        color_discrete_map={"normal": "#1f77b4", "cinza": "#B0B7C3"}
    )

    max_valor = eq_contagem_ordenada["Quantidade"].max()

    grafico_equipamento.update_layout( # retira o nome dos eixos
        xaxis_title="",
        yaxis_title="",
        xaxis=dict(showticklabels=False, range=[0, max_valor * 1.15]), # retira números do eixo X
        height=350, 
        bargap=0.3,
        showlegend=False
    )

    grafico_equipamento.update_traces(textposition="outside") # define o texto para fora das barras

    st.plotly_chart(grafico_equipamento, use_container_width=True, config={"displayModeBar": False})


with gf_loc:
    # 3) gráfico de chamados por unidade/setor

    st.markdown("### CHAMADOS POR LOCALIZAÇÃO")
    grafico, filtro = st.columns([3,1])

    with filtro:
        opcao_loc = st.radio( # seletor que alterna
                "Visualizar por:",
                options=["Unidade", "Setor"],
                horizontal=False
            )

    with grafico:
        loc_contagem = df[opcao_loc].value_counts().reset_index()
        loc_contagem.columns = [opcao_loc, "Quantidade"]

        locais = loc_contagem[loc_contagem[opcao_loc] != "NAO IDENTIFICADO"].sort_values("Quantidade", ascending=True)
        nao_identificado_loc = loc_contagem[loc_contagem[opcao_loc] == "NAO IDENTIFICADO"]

        loc_contagem_ordenada = pd.concat([nao_identificado_loc, locais])
        loc_contagem_ordenada["cor_grupo"] = loc_contagem_ordenada[opcao_loc].apply(
            lambda x: "cinza" if x == "NAO IDENTIFICADO" else "normal"
        )

        grafico_local = px.bar(
            loc_contagem_ordenada,
            x="Quantidade",
            y=opcao_loc,
            orientation="h",
            text="Quantidade",
            color="cor_grupo",
            color_discrete_map={"normal": "#1f77b4", "cinza": "#B0B7C3"}
        )

        grafico_local.update_traces(textposition="outside") 
        grafico_local.update_layout(
            xaxis_title="",
            yaxis_title="",
            xaxis=dict(showticklabels=False, range=[0, max_valor * 1.15]),
            height=350, 
            bargap=0.3,
            showlegend=False
        )

        st.plotly_chart(grafico_local, use_container_width=True, config={"displayModeBar": False})

# 4) tabela de chamados novos/em andamento/pendente

st.markdown("### CHAMADOS SEM FINALIZAÇÃO")

data_extracao = pd.to_datetime("2026-09-10", format='mixed')

opcao_tab = st.radio(
    "Visualizar por status:",
    options=["Novo", "Em atendimento (atribuído)", "Pendente"]
)

nao_finalizados = df[df["Status"] == opcao_tab].copy()
nao_finalizados["Última atualização"] = pd.to_datetime(
    nao_finalizados["Última atualização"],
    format="%d/%m/%Y %H:%M",
    errors="coerce",
)

nao_finalizados["Dias sem atualização"] = (data_extracao - nao_finalizados["Última atualização"]).dt.days
nao_finalizados = nao_finalizados[nao_finalizados["Dias sem atualização"] > 0]

tabela_parados = nao_finalizados[["ID", "Status", "Equipamento", "Setor", "Dias sem atualização"]]

st.dataframe(
    tabela_parados.sort_values("Dias sem atualização", ascending=False),
    use_container_width=True,
    hide_index=True
)


