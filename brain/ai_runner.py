import time

# ==========================================
# CURIOSITY ENGINE
# ==========================================

try:
    from curiosity.strategy_hunter import search_github_strategies
except:
    def search_github_strategies():
        print("[AI] Curiosity module not ready")


# ==========================================
# MEMORY ENGINE
# ==========================================

try:
    from engine.memory_engine import load_trauma
except:
    def load_trauma():
        return {"traumas":[]}


# ==========================================
# GENOME EVOLUTION ENGINE
# ==========================================

try:
    from genome.genome_engine import evolve_population
except:
    def evolve_population():
        print("[AI] Genome engine not ready")


# ==========================================
# CAPITAL MANAGER
# ==========================================

try:
    from capital.capital_manager import evaluate_capital
except:
    def evaluate_capital(balance):
        return {"risk_level":1.0}


# ==========================================
# CURIOSITY RUNNER
# ==========================================

def run_curiosity():

    print("\n[AI] Curiosity Engine Start")

    try:

        search_github_strategies()

        print("[AI] Curiosity scan completed")

    except Exception as e:

        print("[AI] Curiosity error:", e)


# ==========================================
# MEMORY RUNNER
# ==========================================

def run_memory():

    print("\n[AI] Loading trauma memory")

    try:

        trauma = load_trauma()

        print("[AI] Trauma records:", len(trauma["traumas"]))

    except Exception as e:

        print("[AI] Memory error:", e)


# ==========================================
# EVOLUTION RUNNER
# ==========================================

def run_evolution():

    print("\n[AI] Genome Evolution Start")

    try:

        evolve_population()

        print("[AI] Evolution completed")

    except Exception as e:

        print("[AI] Evolution error:", e)


# ==========================================
# CAPITAL MANAGER RUNNER
# ==========================================

def run_capital_management():

    print("\n[AI] Capital Management")

    try:

        # nanti ini akan diganti data real dari MT5
        balance = 100

        state = evaluate_capital(balance)

        print("[AI] Risk Level:", state["risk_level"])

    except Exception as e:

        print("[AI] Capital manager error:", e)


# ==========================================
# MAIN AI LOOP
# ==========================================

def main_loop():

    print("\n==============================")
    print("AI OVERLORD BRAIN STARTED")
    print("==============================")

    while True:

        print("\n---------------------------------")
        print("AI BRAIN CYCLE START")
        print("---------------------------------")

        run_curiosity()

        run_memory()

        run_evolution()

        run_capital_management()

        print("\n[AI] Cycle Completed")

        print("[AI] Sleeping 10 minutes...\n")

        time.sleep(600)


# ==========================================
# START AI
# ==========================================

if __name__ == "__main__":
    main_loop()
