import json
import os
import pandas as pd
import numpy as np
from datetime import datetime

# ==========================================
# ENGINE IMPORTS
# ==========================================
try:
    from engine.market_regime import detect_market_regime
except ImportError:
    def detect_market_regime(df): return "TRENDING"

# ==========================================
# PATH CONFIG
# ==========================================
DATA_PATH = "data/trade_history.csv"
WEIGHT_PATH = "intelligence/neural_weights.json"
GENOME_PATH = "genomes/genomes_active.json"
RISK_PATH = "config/risk_protector.json"
BOOST_PATH = "config/boost_config.json"
LOGIC_PATH = "logic.json"

# ==========================================
# HELPER FUNCTIONS
# ==========================================
def load_json(path, default={}):
    if os.path.exists(path):
        try:
            with open(path) as f:
                return json.load(f)
        except:
            return default
    return default

def load_market_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    return None

def compute_rsi(series, period=14):
    if len(series) < period: return 50
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100/(1+rs))
    return rsi.iloc[-1]

# ==========================================
# DYNAMIC RISK & LOT
# ==========================================
def compute_dynamic_lot(equity, balance, max_lot, profit_ratio=0.5):
    """
    Lot scale based on equity vs balance and profit_ratio (0.5 = 50%)
    """
    ratio = min(max(equity / balance, profit_ratio), 2.0)  # scale 0.5-2x
    return round(max_lot * ratio, 4)

def dynamic_trailing_ratio(base_ratio, profit, equity):
    """
    Trailing ratio naik seiring profit
    """
    bonus = min(profit / equity, 0.5)  # maksimal tambah 50%
    return min(base_ratio + bonus, 0.95) # cap 95%

def partial_close_needed(equity, equity_guard, positions):
    """
    Hitung apakah perlu partial close jika equity mendekati limit
    """
    if equity / equity_guard < 1.05:
        return True
    return False

# ==========================================
# 6-LAYER NEURAL ARCHITECTURE
# ==========================================
def sensory_layer(df, weights):
    score = 0
    close = df['close']
    last = close.iloc[-1]
    sma200 = close.rolling(200).mean().iloc[-1]
    sma50 = close.rolling(50).mean().iloc[-1]

    if last > sma200: score += 20 * weights.get("structure", 0.7)
    if sma50 > sma200: score += 10 * weights.get("trend", 0.7)
    volatility = close.std()
    if volatility > 0.001: score += 10 * weights.get("volatility", 0.6)
    return score

def indicator_layer(df, weights, genome_params):
    score = 0
    price = df['close'].iloc[-1]
    ema_f_p = int(genome_params.get("ema_fast", 20))
    ema_s_p = int(genome_params.get("ema_slow", 50))
    rsi_p = int(genome_params.get("rsi_period", 14))

    ema_f = df['close'].ewm(span=ema_f_p).mean().iloc[-1]
    ema_s = df['close'].ewm(span=ema_s_p).mean().iloc[-1]
    if price > ema_f: score += 10 * weights.get("ema_fast", 0.7)
    if price > ema_s: score += 10 * weights.get("ema_slow", 0.7)
    rsi = compute_rsi(df['close'], period=rsi_p)
    if rsi < 35: score += 15 * weights.get("rsi_buy", 0.6)
    if rsi > 70: score -= 15 * weights.get("rsi_sell", 0.6)
    return score

def genome_layer(genome):
    score = 0
    params = genome.get("parameters", {})
    if any("elite" in key for key in params.keys()): score += 15
    if "GEN" in genome.get("strategy_id", ""): score += 10
    return score

def learning_layer(df):
    score = 0
    if 'profit' in df.columns and not df.empty:
        wins = df[df['profit'] > 0].shape[0]
        total = df.shape[0]
        if total > 0:
            winrate = wins / total
            score += winrate * 25
    return score

def risk_layer(risk):
    protection = risk.get("protection", 0.9)
    equity_guard = risk.get("equity_guard", 0.8)
    return (protection * 10) + (equity_guard * 10)

def boost_layer(boost):
    return boost.get("boost_power", 1.0) * 5

# ==========================================
# EXECUTION LAYER
# ==========================================
def execution_layer(score):
    if score >= 85: return "BUY", "HIGH"
    elif score <= 25: return "SELL", "HIGH"
    elif score >= 65: return "BUY", "MEDIUM"
    elif score <= 45: return "SELL", "MEDIUM"
    else: return "IDLE", "LOW"

def update_logic(action, confidence, score, genome, equity, balance, profit):
    risk_mgmt = genome.get("risk_management", {})
    max_lot = risk_mgmt.get("max_lot", 0.01)
    base_trailing = risk_mgmt.get("trailing_ratio", 0.65)
    ghost = risk_mgmt.get("use_ghost_mode", True)
    lot = compute_dynamic_lot(equity, balance, max_lot)
    trailing_ratio = dynamic_trailing_ratio(base_trailing, profit, equity)

    logic = {
        "command": action,
        "kill": False,
        "confidence": confidence,
        "signal_score": round(score, 2),
        "strategy_id": genome.get("strategy_id", "UNKNOWN"),
        "lot_override": lot,
        "trailing_ratio": trailing_ratio,
        "ghost_sl": ghost,
        "apply_to_new_trades_only": True,
        "trade_direction_mode": "BOTH",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": "AI_BRAIN_V3"
    }

    with open(LOGIC_PATH, "w") as f:
        json.dump(logic, f, indent=4)
    print(f"🧠 [DECISION] {action} | Score: {round(score,2)} | DNA: {logic['strategy_id']} | Lot: {lot} | Trailing: {round(trailing_ratio,2)}")

# ==========================================
# MAIN LOOP
# ==========================================
if __name__ == "__main__":
    df = load_market_data()
    weights = load_json(WEIGHT_PATH)
    genome = load_json(GENOME_PATH)
    risk = load_json(RISK_PATH)
    boost = load_json(BOOST_PATH)

    equity = 10000  # bisa diganti dengan real balance dari MT5
    balance = 10000
    profit = df['profit'].sum() if df is not None and 'profit' in df.columns else 0

    if df is None or df.empty:
        update_logic("IDLE", "INITIALIZING", 0, genome, equity, balance, profit)
        exit()

    regime = detect_market_regime(df)
    if regime == "CHAOS":
        update_logic("IDLE", "LOW", 0, genome, equity, balance, profit)
        exit()

    genome_params = genome.get("parameters", {})

    l1 = sensory_layer(df, weights)
    l2 = indicator_layer(df, weights, genome_params)
    l3 = genome_layer(genome)
    l4 = learning_layer(df)
    l5 = risk_layer(risk)
    l6 = boost_layer(boost)

    total_score = l1 + l2 + l3 + l4 + l5 + l6
    action, confidence = execution_layer(total_score)
    update_logic(action, confidence, total_score, genome, equity, balance, profit)
