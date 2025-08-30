import pandas as pd
from datetime import datetime

def save_trade(ticker, entry, exit, result, notes):
    # Charger le journal existant
    df = pd.read_csv("journal.csv")
    # Ajouter une nouvelle ligne
    df.loc[len(df)] = [datetime.today().strftime("%Y-%m-%d"), ticker, entry, exit, result, notes]
    # Sauvegarder le journal mis à jour
    df.to_csv("journal.csv", index=False)

def load_journal():
    # Charger et retourner le journal complet
    return pd.read_csv("journal.csv")
