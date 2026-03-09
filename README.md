AI_Overlord_Brain/
├── index.html       ← Dashboard (GitHub Pages)
├── logic.json       ← Perintah dari Dashboard → MT5
├── status.json      ← Status MT5 → Dashboard (ditulis EA)
├── AI_Overlord_V20.mq5  ← Expert Advisor MT5
└── README.md


AI_Overlord_Brain/
│
├── .github/workflows/          # Jantung Otomatisasi
│   └── ai_heartbeat.yml        # Script yang menjalankan brain.py setiap 10 menit
│
├── engine/                     # Mesin Utama (7 Prinsip AI)
│   ├── brain.py                # Sang Pencipta (Menghitung 50 Saraf & Update logic.json)
│   ├── evolution_engine.py     # Mutasi strategi & Crossover parameter
│   ├── strategy_generator.py   # Menggabungkan indikator internet menjadi strategi baru
│   └── market_regime.py
├── formulas/                   # Modul Rumus (Modular Indicator)
│   ├── rsi.json                # Parameter dinamis RSI (Saraf 11)
│   ├── ema.json                # Parameter trend-following (Saraf 16)
│   ├── macd.json               # Konfirmasi momentum (Saraf 12)
│   └── smc_logic.json          # Rumus OrderBlock & BOS (Saraf 1-10)
│
├── genomes/                    # DNA Strategi yang Sedang Aktif
│   └── genomes_active.json     # Berisi kombinasi rumus yang sedang dipakai MT5
│
├── config/                     # Remote Control (Protection & Speed)
│   ├── boost_config.json       # Kecepatan eksekusi (Scalping/Swing) (Saraf 41)
│   └── risk_protector.json     # Batas Loss & Profit (Saraf 21-30)
│
├── data/                       # Memori & Feedback Loop
│   └── trade_history.csv       # Laporan dari MT5 untuk dipelajari AI (Saraf 31)
│
├── results/                    # Validasi Sebelum Live
│   └── backtest_results.json   # Hasil simulasi strategi baru (Saraf 37)
│
├── communication/              # Notifikasi & Web UI
│   ├── index.html              # Dashboard Monitoring (Link yang kamu punya)
│   └── style.css               # Tampilan Dashboard
│
├── logs/                       # Catatan Kesehatan Sistem
│   └── system_log.txt          # Log aktivitas Brain & MT5
│
├── logic.json                  # JEMBATAN UTAMA (Satu-satunya file yang dibaca MT5)
├── intelligence/
|      └── neural_weights.json
├── ai_runner.py
