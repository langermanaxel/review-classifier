import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import sys
import os
from io import BytesIO

# ============================
# FIX IMPORT ROOT
# ============================
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

# ============================
# CONFIGURACIÓN UI
# ============================
st.set_page_config(
    page_title="Dashboard de Reseñas del Café",
    layout="wide",
    page_icon="☕",
)


# ============================
# ESTILO CSS PERSONALIZADO (MODO OSCURO PREMIUM)
# ============================
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.block-container {
    padding-top: 2rem;
}
h1, h2, h3, h4, h5, h6, p, label, .stMetric {
    color: #e2e8f0 !important;
}
[data-testid="stMetricValue"] {
    color: #22c55e;
}
.sidebar .sidebar-content {
    background-color: #1e293b;
}
table {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)


# ============================
# CARGA DE DATOS
# ============================
DATA_PATH = os.path.join(ROOT_DIR, "data", "reviews.csv")
df = pd.read_csv(DATA_PATH)

# Si no hay fecha, agregamos una columna ficticia uniforme
if "date" not in df.columns:
    df["date"] = pd.date_range(start="2024-01-01", periods=len(df))

df["date"] = pd.to_datetime(df["date"])


# ============================
# SIDEBAR (Filtros)
# ============================
st.sidebar.header("🔍 Filtros")

sentiment_filter = st.sidebar.multiselect(
    "Sentimientos",
    options=["pos", "neg"],
    default=["pos", "neg"]
)

date_range = st.sidebar.date_input(
    "Rango de fecha",
    value=[df["date"].min(), df["date"].max()]
)

export_btn = st.sidebar.button("📥 Exportar CSV filtrado")


# ============================
# APLICAR FILTROS
# ============================
df_filtered = df[df["label"].isin(sentiment_filter)]
df_filtered = df_filtered[
    (df_filtered["date"] >= pd.to_datetime(date_range[0])) &
    (df_filtered["date"] <= pd.to_datetime(date_range[1]))
]


# ============================
# MÉTRICAS
# ============================
st.title("📈 Dashboard de Reseñas del Café")
st.write("Análisis NLP de reseñas con Machine Learning.")

total_reviews = len(df_filtered)
pos_count = (df_filtered["label"] == "pos").sum()
neg_count = (df_filtered["label"] == "neg").sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total de Reseñas", total_reviews)
col2.metric("Positivas", pos_count, f"{(pos_count/total_reviews*100):.1f}%")
col3.metric("Negativas", neg_count, f"{(neg_count/total_reviews*100):.1f}%")


# ============================
# GRÁFICO: PIE CHART
# ============================
st.subheader("📊 Distribución de Sentimientos")

if total_reviews > 0:
    fig1, ax1 = plt.subplots(figsize=(5, 5))
    ax1.pie(
        [pos_count, neg_count],
        labels=["Positivas", "Negativas"],
        autopct="%1.1f%%",
        colors=["#22c55e", "#ef4444"]
    )
    ax1.set_title("Proporción")
    st.pyplot(fig1)
else:
    st.info("No hay reseñas para mostrar en este rango.")


# ============================
# WORDCLOUD
# ============================
st.subheader("☁ Nube de Palabras")

wc_sentiment = st.selectbox("Seleccionar sentimiento para la nube:", ["pos", "neg"])

text_wc = " ".join(df_filtered[df_filtered["label"] == wc_sentiment]["text"].astype(str))

if text_wc.strip():
    wc = WordCloud(width=900, height=400, background_color="black").generate(text_wc)

    fig_wc, ax_wc = plt.subplots(figsize=(12, 5))
    ax_wc.imshow(wc, interpolation="bilinear")
    ax_wc.axis("off")
    st.pyplot(fig_wc)
else:
    st.warning("No hay palabras para generar la nube.")


# ============================
# TENDENCIA EN EL TIEMPO
# ============================
st.subheader("📅 Tendencia Temporal")

df_grouped = df_filtered.groupby([df_filtered["date"].dt.date, "label"]).size().reset_index(name="count")

fig3, ax3 = plt.subplots(figsize=(15, 5))

for label in ["pos", "neg"]:
    subset = df_grouped[df_grouped["label"] == label]
    ax3.plot(subset["date"], subset["count"], marker="o", label=label)

ax3.legend(["Positivas", "Negativas"])
ax3.set_xlabel("Fecha")
ax3.set_ylabel("Cantidad")
ax3.grid(alpha=0.3)
ax3.set_title("Evolución diaria de reseñas")

st.pyplot(fig3)


# ============================
# EXPORTACIÓN CSV
# ============================
if export_btn:
    to_write = df_filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Descargar CSV filtrado",
        data=to_write,
        file_name="reseñas_filtradas.csv",
        mime="text/csv"
    )


# ============================
# TABLA FINAL
# ============================
st.subheader("📋 Reseñas filtradas")
st.dataframe(df_filtered, use_container_width=True)
