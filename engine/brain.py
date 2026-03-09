import json
import os
import pandas as pd
import numpy as np
from datetime import datetime

# Mengimpor deteksi regime dari modul market_regime
try:
    from engine.market_regime import detect_market_regime
except ImportError:
    # Fallback jika struktur folder berbeda saat pengetesan
    def detect_market_regime(df): return "TRENDING"

# =========================
# PATH KONFIGURASI
# =========================
DATA_PATH = "data/trade_history.csv"
WEIGHT_PATH = "intelligence/neural_weights.json"
GENOME_PATH = "genomes/genomes_active.json"
RISK_PATH = "config/risk_protector.json"
BOOST_PATH = "config/boost_config.json"
LOGIC_PATH = "logic.json"

# =========================
# FUNGSI HELPER
# =========================
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
        # Membaca data harga (MT5 harus selalu update file ini)
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
# 🧠 6-LAYER NEURAL ARCHITECTURE
# ==========================================

# LAYER 1: MARKET STRUCTURE (Saraf 01-10)
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

# LAYER 2: INDICATOR (Saraf 11-20)
def indicator_layer(df, weights, genome_params):
    score = 0
    price = df['close'].iloc[-1]
    
    # Mengambil periode dari Genome (Hasil Mutation) atau Default
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

# LAYER 3: GENOME STRATEGY (Saraf 31-40) - DYNAMIC SYNC
def genome_layer(genome):
    # Membaca skor adaptasi dari DNA yang sedang aktif
    score = 0
    params = genome.get("parameters", {})
    
    # Jika DNA mengandung parameter 'elite', berikan bonus skor
    if any("elite" in key for key in params.keys()):
        score += 15
    
    # Bonus skor jika ID strategi valid
    if "GEN" in genome.get("strategy_id", ""):
        score += 10
        
    return score

# LAYER 4: LEARNING MEMORY (Saraf 41-50)
def learning_layer(df):
    score = 0
    if 'profit' in df.columns and not df.empty:
        wins = df[df['profit'] > 0].shape[0]
        total = df.shape[0]
        if total > 0:
            winrate = wins / total
            score += winrate * 25 # Semakin tinggi winrate, semakin percaya diri
    return score

# LAYER 5: RISK BRAIN
def risk_layer(risk):
    protection = risk.get("protection", 0.9)
    equity_guard = risk.get("equity_guard", 0.8)
    return (protection * 10) + (equity_guard * 10)

# LAYER 6: BOOST MODE
def boost_layer(boost):
    # Mengaktifkan power tambahan jika market sangat mendukung
    return boost.get("boost_power", 1.0) * 5

# =========================
# EXECUTION & OUTPUT
# =========================
def execution_layer(score):
    if score >= 85: return "BUY", "HIGH"
    elif score <= 25: return "SELL", "HIGH"
    elif score >= 65: return "BUY", "MEDIUM"
    elif score <= 45: return "SELL", "MEDIUM"
    else: return "IDLE", "LOW"

def update_logic(action, confidence, score, genome):
    # Mengambil risk management dari DNA aktif
    risk_mgmt = genome.get("risk_management", {})
    
    logic = {
        "command": action,
        "kill": False,
        "confidence": confidence,
        "signal_score": round(score, 2),
        "strategy_id": genome.get("strategy_id", "UNKNOWN"),
        "lot_override": risk_mgmt.get("max_lot", 0.02),
        "trailing_ratio": risk_mgmt.get("trailing_ratio", 0.65),
        "ghost_sl": risk_mgmt.get("use_ghost_mode", True),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": "AI_BRAIN_V2"
    }

    with open(LOGIC_PATH, "w") as f:
        json.dump(logic, f, indent=4)
    
    print(f"🧠 [DECISION] {action} | Score: {round(score,2)} | DNA: {logic['strategy_id']}")

# =========================
# MAIN LOOP
# =========================
if __name__ == "__main__":
    # 1. Load All Components
    df = load_market_data()
    weights = load_json(WEIGHT_PATH)
    genome = load_json(GENOME_PATH)
    risk = load_json(RISK_PATH)
    boost = load_json(BOOST_PATH)

    if df is None or df.empty:
        update_logic("IDLE", "INITIALIZING", 0, genome)
        print("❌ Waiting for Market Data (CSV)...")
        exit()

    # 2. Market Regime Check (The Guardian)
    regime = detect_market_regime(df)
    print(f"🌐 Market Regime: {regime}")

    if regime == "CHAOS":
        update_logic("IDLE", "LOW", 0, genome)
        print("⚠ BlackSwan Protection Active: Trading Paused")
        exit()

    # 3. Processing Layers
    genome_params = genome.get("parameters", {})
    
    l1 = sensory_layer(df, weights)
    l2 = indicator_layer(df, weights, genome_params)
    l3 = genome_layer(genome)
    l4 = learning_layer(df)
    l5 = risk_layer(risk)
    l6 = boost_layer(boost)

    total_score = l1 + l2 + l3 + l4 + l5 + l6

    # 4. Final Decision
    action, confidence = execution_layer(total_score)
    update_logic(action, confidence, total_score, genome)
