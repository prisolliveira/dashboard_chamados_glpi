CUSTOM_CSS = """
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
        padding-bottom: 2rem;
        max-width: 1100px;
    }
 
    /* Título principal */
    h1 {
        font-weight: 800 !important;
        color: #16213e !important;
        margin-bottom: 0.3rem !important;
        padding-bottom: 0.8rem !important;
        border-bottom: 3px solid #16213e !important;
        font-size: 24px !important;
    }
 
    [data-testid="stCaptionContainer"] {
        color: #6b7280 !important;
        font-size: 12px !important;
    }
 
    /* Espaço extra abaixo do cabeçalho, antes dos KPI cards */
    div[data-testid="stMetric"] {
        margin-top: 1.8rem;
    }
 
    /* KPI Cards - cabeçalho escuro estilo "card com topo navy" */
    div[data-testid="stMetric"] {
        background-color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0px 0px 10px 0px !important;
        box-shadow: 0 2px 8px rgba(22, 33, 62, 0.08) !important;
        overflow: hidden !important;
    }
 
    div[data-testid="stMetric"] label,
    div[data-testid="stMetricLabel"],
    div[data-testid="stMetricLabel"] > div,
    div[data-testid="stMetricLabel"] p {
        font-size: 10px !important;
        font-weight: 700 !important;
        color: #ffffff !important;
        text-transform: uppercase !important;
        letter-spacing: 0.6px !important;
        background-color: #16213e !important;
        padding: 7px 12px !important;
        margin: 0px 0px 8px 0px !important;
        width: 100% !important;
        display: block !important;
    }
 
    div[data-testid="stMetricValue"] {
        font-size: 20px !important;
        font-weight: 800 !important;
        color: #16213e !important;
        padding: 0px 12px !important;
    }
 
    div[data-testid="column"] {
        padding: 0px 7px;
    }
 
    /* Títulos de seção - mais espaço acima para separar bem de cima */
    h3 {
        font-weight: 700 !important;
        color: #ffffff !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.6px !important;
        margin-top: 2.2rem !important;
        margin-bottom: 0px !important;
        padding: 8px 14px !important;
        background-color: #16213e !important;
        border-radius: 8px 8px 0px 0px !important;
        display: block !important;
    }
 
    /* Radio buttons */
    div[data-testid="stRadio"] label {
        font-size: 12px;
        color: #16213e;
        font-weight: 600;
    }
 
    div[data-testid="stRadio"] {
        padding: 10px 14px 2px 14px;
        background-color: #ffffff;
    }
 
    /* Tabela */
    div[data-testid="stDataFrame"] {
        border-radius: 0px 0px 10px 10px;
        overflow: hidden;
        border: none;
        box-shadow: 0 2px 8px rgba(22, 33, 62, 0.08);
        font-size: 12px;
    }
 
    /* "Card" wrapper para envolver gráficos logo após um h3 */
    div[data-testid="stPlotlyChart"] {
        background-color: #ffffff;
        border-radius: 0px 0px 10px 10px;
        padding: 6px;
        box-shadow: 0 2px 8px rgba(22, 33, 62, 0.08);
        margin-bottom: 0.5rem;
    }
    </style>
"""