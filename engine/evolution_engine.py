import json
import pandas as pd
import random
import os

GENOME_PATH = 'genomes/genomes_active.json'
HISTORY_PATH = 'data/trade_history.csv'

MIN_TRADES = 30
MUTATION_THRESHOLD = 0.55


def evolve_strategy():

    print("🧬 Memulai Proses Evolusi Genetik...")

    if not os.path.exists(HISTORY_PATH):
        print("⚠️ Belum ada riwayat trading.")
        return

    df = pd.read_csv(HISTORY_PATH)

    if len(df) < MIN_TRADES:
        print(f"⏳ Trade belum cukup ({len(df)}/{MIN_TRADES})")
        return

    # ========================
    # METRICS
    # ========================

    wins = df[df['profit'] > 0]
    losses = df[df['profit'] <= 0]

    win_rate = len(wins) / len(df)

    total_profit = df['profit'].sum()
    profit_factor = wins['profit'].sum() / abs(losses['profit'].sum()) if len(losses) > 0 else 999

    print(f"📊 Win Rate: {win_rate:.2%}")
    print(f"💰 Profit Factor: {profit_factor:.2f}")
    print(f"📈 Total Profit: {total_profit:.2f}")

    # ========================
    # DECISION
    # ========================

    if win_rate > 0.60 and profit_factor > 1.2:

        print("🌟 Strategi masih bagus. Tidak perlu mutasi.")
        return

    print("🛠️ Performa turun → melakukan mutasi DNA")

    # ========================
    # LOAD DNA
    # ========================

    with open(GENOME_PATH) as f:
        dna = json.load(f)

    # ========================
    # MUTATION
    # ========================

    dna['rsi_period'] = random.randint(7,21)
    dna['ema_fast'] = random.randint(5,25)

    # mutasi kecil saja
    dna['risk_per_trade'] = round(
        max(0.3, min(2.5, dna.get('risk_per_trade',1.0) + random.uniform(-0.3,0.3))),
        2
    )

    # ========================
    # SAVE DNA
    # ========================

    with open(GENOME_PATH,"w") as f:
        json.dump(dna,f,indent=4)

    print("✅ DNA berhasil berevolusi")


if __name__ == "__main__":
    evolve_strategy()
