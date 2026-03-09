import json
import os
import random

# ----------------------------
# PATH KONFIGURASI
# ----------------------------
FORMULA_DIR = 'formulas/'              # Folder berisi file .json indikator dan rumus trading
GENOME_PATH = 'genomes/genomes_active.json'  # File DNA aktif

# ----------------------------
# GENERATIVE STRATEGY ENGINE
# ----------------------------
def generate_new_strategy():

    print("🧪 Generative Engine: Menciptakan Kombinasi Strategi Baru...")

    # 1️⃣ List semua rumus yang tersedia
    available_formulas = [f for f in os.listdir(FORMULA_DIR) if f.endswith('.json')]
    
    if len(available_formulas) < 2:
        print("⚠️ Tidak cukup rumus. Tambahkan file .json di folder formulas/")
        return

    # 2️⃣ Pilih 2-3 rumus acak (bisa dari internet strategy + elite + indikator)
    selected_formulas = random.sample(available_formulas, k=min(3, len(available_formulas)))
    print(f"🧬 Menggabungkan: {', '.join(selected_formulas)}")

    # 3️⃣ Buat DNA baru
    new_dna = {
        "strategy_id": f"GEN-{random.randint(10000,99999)}",
        "active_components": selected_formulas,
        "parameters": {},
        "risk_management": {
            "max_lot": 0.5,
            "use_ghost_mode": True,
            "trailing_ratio": 0.65
        }
    }

    # 4️⃣ Ambil parameter default dari setiap formula
    for formula_file in selected_formulas:
        with open(os.path.join(FORMULA_DIR, formula_file), 'r') as f:
            formula_data = json.load(f)
            for key, value in formula_data.items():
                new_dna["parameters"][f"{formula_file.replace('.json','')}_{key}"] = value

    # 5️⃣ Simpan sebagai DNA aktif
    with open(GENOME_PATH, 'w') as f:
        json.dump(new_dna, f, indent=4)

    print(f"✅ Strategi Generatif Berhasil Dibuat: {new_dna['strategy_id']}")


# ----------------------------
# EKSEKUSI LANGSUNG
# ----------------------------
if __name__ == "__main__":
    generate_new_strategy()
