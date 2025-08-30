import yfinance as yf
import pandas as pd

def get_data(ticker, start, end):
    # Télécharge les données historiques du ticker entre deux dates
    df = yf.download(ticker, start=start, end=end)
    # Garde uniquement les colonnes utiles
    return df[["Open", "High", "Low", "Close", "Volume"]]
