import csv
import os

file = "trade_history.csv"

def log_trade(data):

    header = [
        "time",
        "symbol",
        "strategy",
        "entry",
        "exit",
        "profit",
        "market_regime"
    ]

    file_exists = os.path.isfile(file)

    with open(file,"a",newline="") as f:

        writer = csv.DictWriter(f,fieldnames=header)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)
