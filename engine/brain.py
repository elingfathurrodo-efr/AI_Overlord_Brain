import json
import os
import pandas as pd
import numpy as np
from datetime import datetime

# ==============================
# PATH CONFIG
# ==============================

DATA_PATH = "data/trade_history.csv"
WEIGHT_PATH = "intelligence/neural_weights.json"
GENOME_PATH = "genomes/genomes_active.json"
RISK_PATH = "risk/risk_protector.json"
BOOST_PATH = "boost/boost_config.json"
LOGIC_PATH = "logic.json"


# ==============================
# LOADERS
# ==============================

def load_json(path, default={}):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default


def load_market_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    return None


# ==============================
# SARAF 1-50
# ==============================

def sensory_layer(df, weights):

    score = 0

    close = df['close']
    last = close.iloc[-1]

    sma200 = close.rolling(200).mean().iloc[-1]
    sma50 = close.rolling(50).mean().iloc[-1]

    if last > sma200:
        score += 15 * weights.get("structure",0.7)

    if sma50 > sma200:
        score += 10 * weights.get("trend",0.7)

    volatility = close.std()

    if volatility > 0.001:
        score += 10 * weights.get("volatility",0.6)

    return score


# ==============================
# SARAF 51-100
# ==============================

def indicator_layer(df, weights):

    score = 0

    price = df['close'].iloc[-1]

    ema20 = df['close'].ewm(span=20).mean().iloc[-1]
    ema50 = df['close'].ewm(span=50).mean().iloc[-1]

    if price > ema20:
        score += 10 * weights.get("ema_fast",0.7)

    if price > ema50:
        score += 10 * weights.get("ema_slow",0.7)

    momentum = df['close'].pct_change().mean()

    if momentum > 0:
        score += 15 * weights.get("momentum",0.7)

    rsi = compute_rsi(df['close'])

    if rsi < 35:
        score += 12 * weights.get("rsi_buy",0.6)

    if rsi > 65:
        score -= 12 * weights.get("rsi_sell",0.6)

    return score


# ==============================
# SARAF 101-140
# ==============================

def genome_layer(genome):

    score = 0

    aggression = genome.get("aggression",0.5)
    patience = genome.get("patience",0.5)
    adaptability = genome.get("adaptability",0.5)

    score += aggression * 10
    score += patience * 8
    score += adaptability * 12

    return score


# ==============================
# SARAF 141-170
# ==============================

def learning_layer(df):

    score = 0

    if 'profit' in df.columns:

        wins = df[df['profit']>0].shape[0]
        total = df.shape[0]

        if total > 0:

            winrate = wins/total

            score += winrate * 20

    return score


# ==============================
# SARAF 171-190
# ==============================

def risk_layer(risk):

    protection = risk.get("protection",0.9)
    equity_guard = risk.get("equity_guard",0.8)

    score = protection * 10 + equity_guard * 10

    return score


# ==============================
# SARAF 191-200
# ==============================

def boost_layer(boost):

    boost_power = boost.get("boost",1.0)

    return boost_power * 5


# ==============================
# RSI
# ==============================

def compute_rsi(series, period=14):

    delta = series.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100/(1+rs))

    return rsi.iloc[-1]


# ==============================
# EXECUTION
# ==============================

def execution_layer(score):

    if score >= 90:
        return "BUY","HIGH"

    elif score <= 20:
        return "SELL","HIGH"

    elif 45 <= score <= 65:
        return "WAIT","NEUTRAL"

    else:
        return "WAIT","LOW"


# ==============================
# WRITE LOGIC
# ==============================

def update_logic(action,confidence,score):

    logic = {

        "action":action,
        "confidence":confidence,
        "signal_score":round(score,2),

        "max_layer":2,
        "lot":0.02,
        "trailing_ratio":0.65,
        "ghost_sl":True,

        "timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    }

    with open(LOGIC_PATH,"w") as f:
        json.dump(logic,f,indent=4)

    print("🧠 AI Decision:",action,"Score:",score)


# ==============================
# MAIN BRAIN
# ==============================

if __name__ == "__main__":

    df = load_market_data()

    weights = load_json(WEIGHT_PATH)
    genome = load_json(GENOME_PATH)
    risk = load_json(RISK_PATH)
    boost = load_json(BOOST_PATH)

    if df is None:

        update_logic("WAIT","INITIALIZING",0)
        exit()

    sensory = sensory_layer(df,weights)

    indicator = indicator_layer(df,weights)

    genome_score = genome_layer(genome)

    learning = learning_layer(df)

    risk_score = risk_layer(risk)

    boost_score = boost_layer(boost)

    total_score = sensory + indicator + genome_score + learning + risk_score + boost_score

    action,confidence = execution_layer(total_score)

    update_logic(action,confidence,total_score)
