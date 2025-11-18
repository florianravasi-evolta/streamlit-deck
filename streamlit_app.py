# streamlit_app.py
import streamlit as st
import pandas as pd
from plots import make_price_vs_dispatch_figure

st.set_page_config(
    page_title="Evolta – Battery Trading Showcase",
    layout="wide",
)

# ---- Branding header ----
col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image("assets/evolta_logo.png", use_container_width=True)
with col_title:
    st.markdown("### Battery Trading Forecast Showcase")
    st.markdown(
        "Interactive examples of how our forecasts drive dispatch decisions."
    )

# ---- Controls: choose scenario ----
examples = {
    "High price spike day": "data/example_high_spike.parquet",
    "Calm day": "data/example_calm.parquet",
    "Choppy intraday volatility": "data/example_choppy.parquet",
}
choice = st.selectbox("Choose an example day", list(examples.keys()))

df = pd.read_parquet(examples[choice])
df_prices = df[["datetime", "price"]]
df_dispatch = df[["datetime", "discharge_mw"]]

# ---- Plots ----
fig = make_price_vs_dispatch_figure(df_prices, df_dispatch, title=choice)
st.plotly_chart(fig, use_container_width=True)

# You can add more sections:
# - Probability of spikes vs realized prices
# - P&L comparison "with vs without battery strategy"