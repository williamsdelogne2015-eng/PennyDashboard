import streamlit as st
import pandas as pd
from modules import screener, simulator, journal, alerts, sentiment, backtest, scoring, news_verification, rank_tickers

st.set_page_config(page_title="Penny Dashboard Pro", layout="wide")
st.title("📈 Penny Stocks Dashboard — Multi-Marchés & Anti-Manipulation")

# === Sélection du marché ===
market = st.selectbox("🌍 Marché", ["US", "Canada", "Europe"])
tickers_data = screener.get_valid_tickers(market)

# === Vérification croisée des news ===
for t in tickers_data:
    api_news = news_verification.get_api_news(t["ticker"])
    ir_news = news_verification.get_ir_news(t["ir_url"])
    validated, unconfirmed = news_verification.cross_validate_news(api_news, ir_news)
    t["validated_news"] = validated
    t["unconfirmed_news"] = unconfirmed
    t["source_score"] = 95 if validated else 60

# === Scoring complet
for t in tickers_data:
    t.update(scoring.compute_scores(t))

# === Classement des tickers
ranked = rank_tickers.rank_tickers(tickers_data)
st.subheader("🏆 Classement des tickers du jour")
st.dataframe(pd.DataFrame(ranked))

# === Simulation rendement composé
st.subheader("💰 Simulation de croissance du capital")
initial = st.number_input("Capital initial (€)", value=1000)
days = st.slider("Nombre de jours", 10, 60, 30)
df_growth = simulator.simulate_growth(initial, days, 0.8, 0.1, 0.1)
st.dataframe(df_growth)

# === Journal de performance
st.subheader("📓 Enregistrer un trade")
ticker = st.text_input("Ticker")
entry = st.number_input("Prix d’achat")
exit = st.number_input("Prix de vente")
result = st.selectbox("Résultat", ["gain", "exit", "loss"])
notes = st.text_area("Notes")
if st.button("💾 Enregistrer"):
    journal.save_trade(ticker, entry, exit, result, notes)
    alerts.send_telegram_alert(f"📢 Nouveau trade : {ticker} → {result}")
    st.success("Trade enregistré et alerte envoyée")

st.subheader("📊 Journal complet")
st.dataframe(journal.load_journal())
