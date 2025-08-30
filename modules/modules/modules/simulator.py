import pandas as pd

def simulate_growth(initial, days, win_rate, exit_rate, loss_rate, win=0.15, exit=0.01, loss=-0.05):
    results = ["gain"] * int(days * win_rate) + ["exit"] * int(days * exit_rate) + ["loss"] * int(days * loss_rate)
    capital = initial
    history = []
    for i, r in enumerate(results):
        if r == "gain":
            capital *= (1 + win)
        elif r == "exit":
            capital *= (1 + exit)
        elif r == "loss":
            capital *= (1 + loss)
        history.append({
            "Jour": i + 1,
            "Type": r,
            "Capital (€)": round(capital, 2)
        })
    return pd.DataFrame(history)
