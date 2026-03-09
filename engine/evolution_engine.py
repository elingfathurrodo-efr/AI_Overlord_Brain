import json
import pandas as pd
import random
import os

GENOME_PATH = "genomes/genomes_active.json"
HISTORY_PATH = "data/trade_history.csv"
MEMORY_PATH = "memory/bad_genomes.json"

MIN_TRADES = 30


def load_memory():

    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH) as f:
            return json.load(f)

    return []


def save_memory(memory):

    with open(MEMORY_PATH,"w") as f:
        json.dump(memory,f,indent=4)


def evolve_strategy():

    print("🧬 Evolution Engine Running")

    if not os.path.exists(HISTORY_PATH):
        return

    df = pd.read_csv(HISTORY_PATH)

    if len(df) < MIN_TRADES:
        print("⏳ Not enough trades for evolution")
        return

    wins = df[df['profit'] > 0]
    losses = df[df['profit'] <= 0]

    winrate = len(wins) / len(df)

    profit_factor = wins['profit'].sum() / abs(losses['profit'].sum()) if len(losses)>0 else 999

    print("Winrate:",winrate)
    print("Profit Factor:",profit_factor)

    if winrate > 0.6 and profit_factor > 1.2:
        print("🌟 Strategy healthy")
        return

    print("⚠ Strategy weak → mutation triggered")

    # LOAD DNA
    with open(GENOME_PATH) as f:
        dna = json.load(f)

    # LOAD MEMORY
    bad_memory = load_memory()

    # SAVE BAD DNA
    bad_memory.append(dna)

    save_memory(bad_memory)

    # CREATE NEW DNA
    new_dna = dna.copy()

    new_dna["rsi_period"] = random.randint(7,21)
    new_dna["ema_fast"] = random.randint(5,25)

    new_dna["risk_per_trade"] = round(
        max(0.3, min(2.5, new_dna.get("risk_per_trade",1.0) + random.uniform(-0.3,0.3))),
        2
    )

    # CHECK AGAINST MEMORY
    if new_dna in bad_memory:
        print("⚠ DNA pernah gagal, mutasi ulang")
        return

    with open(GENOME_PATH,"w") as f:
        json.dump(new_dna,f,indent=4)

    print("✅ New DNA evolved")
