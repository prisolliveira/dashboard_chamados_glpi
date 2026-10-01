CUSTOM_CSS = """
    <style>
    .block-container {
        padding-top: 3.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
        padding-bottom: 2rem;
        max-width: 1100px;
        overflow: visible;
    }
 
    /* ===== Cabeçalho estilo "eyebrow + título + mini-indicadores" ===== */
    .header-wrap {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 16px;
        background-color: transparent;
        padding: 0px;
        margin-bottom: 1.8rem;
    }
 
    .header-left {
        min-width: 260px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(22, 33, 62, 0.08);
        padding: 14px 24px;
    }
 
    .header-eyebrow {
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        color: #16213e;
        margin-bottom: 4px;
    }
 
    .header-title {
        font-size: 26px;
        font-weight: 800;
        color: #16213e;
        line-height: 1.2;
        margin-bottom: 4px;
    }
 
    .header-sub {
        font-size: 13px;
        color: #6b7280;
    }
 
    .header-right {
        display: flex;
        align-items: center;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(22, 33, 62, 0.08);
        padding: 10px 0px;
    }
 
    .info-item {
        display: flex;
        flex-direction: column;
        padding: 0px 20px;
        min-width: 90px;
    }
 
    .info-label {
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        color: #9aa0ab;
        margin-bottom: 4px;
    }
 
    .info-value {
        font-size: 17px;
        font-weight: 800;
        color: #16213e;
    }
 
    .info-divider {
        width: 1px;
        height: 32px;
        background-color: #e5e7eb;
    }
    /* ===== Fim do cabeçalho customizado ===== */
 
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
