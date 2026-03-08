import json
import os
import random

# --- PATH KONFIGURASI ---
FORMULA_DIR = 'formulas/'
GENOME_PATH = 'genomes/genomes_active.json'

def generate_new_strategy():
    print("🧪 Generative Engine: Menciptakan Kombinasi Strategi Baru...")

    # 1. List semua rumus yang tersedia di folder formulas/
    available_formulas = [f for f in os.listdir(FORMULA_DIR) if f.endswith('.json')]
    
    if len(available_formulas) < 2:
        print("⚠️ Rumus tidak cukup untuk kombinasi. Tambahkan lebih banyak file .json di folder formulas/.")
        return

    # 2. Pilih 2-3 rumus secara acak untuk dikombinasikan (Prinsip 4)
    selected_formulas = random.sample(available_formulas, k=min(3, len(available_formulas)))
    print(f"🧬 Menggabungkan: {', '.join(selected_formulas)}")

    new_dna = {
        "strategy_id": f"GEN-{random.randint(1000, 9999)}",
        "active_components": selected_formulas,
        "parameters": {},
        "risk_management": {
            "max_lot": 0.5,
            "use_ghost_mode": True
        }
    }

    # 3. Ekstrak parameter dari tiap rumus dan gabungkan (Modular)
    for formula_file in selected_formulas:
        with open(os.path.join(FORMULA_DIR, formula_file), 'r') as f:
            formula_data = json.load(f)
            # Ambil parameter default dari rumus
            for key, value in formula_data.items():
                new_dna["parameters"][f"{formula_file.replace('.json','')}_{key}"] = value

    # 4. Simpan sebagai DNA Aktif untuk dicoba oleh MT5
    with open(GENOME_PATH, 'w') as f:
        json.dump(new_dna, f, indent=4)
    
    print(f"✅ Strategi Generatif Berhasil Dibuat: {new_dna['strategy_id']}")

if __name__ == "__main__":
    generate_new_strategy()

