# ============================================
# AI OVERLORD - MAXIMAL RUNNER
# ============================================

import os
import sys
import json
import time
import random
import traceback
from datetime import datetime

# ============================================
# PATH SETUP
# ============================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# ============================================
# IMPORT CORE MODULES (REQUIRED)
# ============================================

from brain.market_sensor import market_reader
from brain.strategy_generator import generator
from brain.strategy_evolution import evolution
from brain.risk_sentinel import risk_manager
from mt5_bridge import trade_executor

# ============================================
# OPTIONAL MODULES (AUTO FALLBACK)
# ============================================

def optional_import(module_path):
    try:
        module = __import__(module_path, fromlist=['*'])
        return module
    except:
        return None

memory_store = optional_import("brain.memory.memory_store")
meta_learning = optional_import("brain.meta_learning.meta_learning")
curiosity_engine = optional_import("brain.curiosity.curiosity_engine")
performance_tracker = optional_import("brain.analytics.performance_tracker")
repair_engine = optional_import("brain.self_repair.repair_engine")

# ============================================
# CONFIGURATION
# ============================================

CONFIG = {
    "loop_delay": 10,
    "population_size": 12,
    "mutation_rate": 0.25,
    "max_trades": 3,
    "signal_file": os.path.join(BASE_DIR, "shared", "trade_decision.json")
}

# ============================================
# POPULATION STORAGE
# ============================================

strategy_population = []

# ============================================
# UTILITIES
# ============================================

def log(msg):
    print(f"[{datetime.now()}] {msg}")

def save_signal(signal):

    try:
        with open(CONFIG["signal_file"], "w") as f:
            json.dump(signal, f, indent=4)
    except Exception as e:
        log(f"Signal save error: {e}")

# ============================================
# INITIAL POPULATION
# ============================================

def initialize_population(market):

    global strategy_population

    if strategy_population:
        return

    log("Generating initial strategy population...")

    for _ in range(CONFIG["population_size"]):
        strategy = generator.generate_strategy(market)
        if strategy:
            strategy_population.append(strategy)

# ============================================
# EVOLUTION STEP
# ============================================

def evolve_population():

    global strategy_population

    if not strategy_population:
        return

    log("Evolving strategy population...")

    new_population = []

    for strat in strategy_population:

        if random.random() < CONFIG["mutation_rate"]:
            strat = evolution.mutate(strat)

        new_population.append(strat)

    strategy_population = new_population

# ============================================
# SELECT BEST STRATEGY
# ============================================

def select_strategy(market):

    global strategy_population

    best = None
    best_score = -999999

    for strat in strategy_population:

        try:
            score = evolution.evaluate(strat, market)

            if score > best_score:
                best_score = score
                best = strat

        except:
            continue

    return best

# ============================================
# AI CYCLE
# ============================================

def ai_cycle():

    log("===== AI CYCLE START =====")

    try:

        # ---------------------------
        # MARKET DATA
        # ---------------------------

        market_data = market_reader.get_market_data()

        if not market_data:
            log("No market data received")
            return

        # ---------------------------
        # MEMORY STORAGE
        # ---------------------------

        if memory_store:
            try:
                memory_store.store_market(market_data)
            except:
                pass

        # ---------------------------
        # POPULATION INIT
        # ---------------------------

        initialize_population(market_data)

        # ---------------------------
        # EVOLUTION
        # ---------------------------

        evolve_population()

        # ---------------------------
        # STRATEGY SELECTION
        # ---------------------------

        strategy = select_strategy(market_data)

        if not strategy:
            log("No valid strategy found")
            return

        # ---------------------------
        # META LEARNING
        # ---------------------------

        if meta_learning:
            try:
                strategy = meta_learning.adjust(strategy)
            except:
                pass

        # ---------------------------
        # EXPLORATION
        # ---------------------------

        if curiosity_engine:
            try:
                strategy = curiosity_engine.explore(strategy)
            except:
                pass

        # ---------------------------
        # RISK VALIDATION
        # ---------------------------

        decision = risk_manager.validate(strategy)

        if not decision:
            log("Risk filter blocked trade")
            return

        # ---------------------------
        # SAVE SIGNAL
        # ---------------------------

        save_signal(decision)

        # ---------------------------
        # EXECUTE TRADE
        # ---------------------------

        trade_executor.execute(decision)

        log("Trade executed")

        # ---------------------------
        # PERFORMANCE TRACK
        # ---------------------------

        if performance_tracker:
            try:
                performance_tracker.record(decision)
            except:
                pass

    except Exception as e:

        log(f"AI cycle error: {e}")
        traceback.print_exc()

        if repair_engine:
            try:
                repair_engine.self_repair()
            except:
                pass

# ============================================
# MAIN LOOP
# ============================================

def main():

    log("====================================")
    log("AI OVERLORD MAX RUNNER STARTED")
    log("====================================")

    while True:

        ai_cycle()

        log(f"Sleeping {CONFIG['loop_delay']} seconds")

        time.sleep(CONFIG["loop_delay"])

# ============================================
# START
# ============================================

if __name__ == "__main__":
    main()
