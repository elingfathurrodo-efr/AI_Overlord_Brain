import json
import random
import time

DB_FILE="knowledge_miner/knowledge_db.json"


def load_db():

    with open(DB_FILE,"r") as f:
        return json.load(f)


def save_db(data):

    with open(DB_FILE,"w") as f:
        json.dump(data,f,indent=2)


def mine_knowledge():

    db=load_db()

    # simulasi penemuan ide strategi baru
    ideas=[
        "RSI divergence strategy",
        "EMA breakout system",
        "MACD trend confirmation",
        "Bollinger mean reversion",
        "ATR volatility breakout"
    ]

    new_idea=random.choice(ideas)

    entry={
        "time":time.time(),
        "idea":new_idea
    }

    db["knowledge"].append(entry)

    save_db(db)

    print("AI discovered new idea:",new_idea)
