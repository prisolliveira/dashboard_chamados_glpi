CUSTOM_CSS = """
    <style>
    /* KPI Cards - estilo minimalista */
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
"""

# Paleta de cores usada nos gráficos de equipamento
CORES_EQUIPAMENTO = {
    "CAMERA": "#408BDB",
    "DVR": "#7BB3E8",
    "NVR": "#A8D0F0",
    "SPEED": "#D4E8F7",
    "ALARME": "#E63946",
}