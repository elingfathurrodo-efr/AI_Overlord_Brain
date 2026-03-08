import json
import pandas as pd
import random
import os

# --- KONFIGURASI EVOLUSI ---
GENOME_PATH = 'genomes/genomes_active.json'
HISTORY_PATH = 'data/trade_history.csv'

def evolve_strategy():
    print("🧬 Memulai Proses Evolusi Genetik...")

    # 1. Cek Riwayat Trading (Feedback Loop)
    if not os.path.exists(HISTORY_PATH):
        print("⚠️ Belum ada riwayat trading. Menggunakan DNA Standar.")
        return

    df = pd.read_csv(HISTORY_PATH)
    if len(df) < 5: # Minimal 5 trade untuk mulai belajar
        print("⏳ Data belum cukup untuk evolusi.")
        return

    # 2. Hitung Win Rate (Seleksi)
    win_rate = (df['profit'] > 0).sum() / len(df)
    print(f"📊 Win Rate Saat Ini: {win_rate:.2%}")

    # 3. Proses Mutasi (Jika Win Rate < 60%)
    if win_rate < 0.60:
        print("🛠️ Performa rendah. Melakukan MUTASI DNA...")
        
        # Load DNA lama
        with open(GENOME_PATH, 'r') as f:
            dna = json.load(f)

        # MUTASI: Mengacak parameter sedikit (Saraf 36)
        dna['rsi_period'] = random.randint(7, 21)
        dna['ema_fast'] = random.randint(5, 25)
        dna['risk_per_trade'] = round(random.uniform(0.5, 2.0), 2)
        
        # Simpan DNA baru (Evolusi Berhasil)
        with open(GENOME_PATH, 'w') as f:
            json.dump(dna, f, indent=4)
        
        print(f"✅ DNA Berhasil Dimutasi: RSI {dna['rsi_period']}, Risk {dna['risk_per_trade']}%")
    else:
        print("🌟 Strategi masih Gacor. Tidak perlu mutasi.")

if __name__ == "__main__":
    evolve_strategy()

