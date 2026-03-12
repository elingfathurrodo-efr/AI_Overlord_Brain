import time

# AI LOOP
from autonomous_loop.ai_loop import run_ai_loop

# CENTRAL BRAIN
from central_brain.central_core import central_brain

# MARKET SCANNER
from autonomous_loop.market_scanner import scan_market

# LEARNING & EVOLUTION
from autonomous_loop.learning_cycle import learning_step
from autonomous_loop.evolution_cycle import evolution_step


def start_ai():

    print("===================================")
    print("   AI TRADING SYSTEM STARTED")
    print("===================================")

    while True:

        try:

            # 1 scan market
            market_regime = scan_market()

            # 2 risk mode default
            risk_mode = "NORMAL"

            # 3 central brain decision
            decision = central_brain(market_regime, risk_mode)

            print("Market Regime :", market_regime)
            print("AI Decision   :", decision)

            # 4 learning cycle
            learning_step()

            # 5 evolution cycle
            evolution_step()

            # delay siklus
            time.sleep(10)

        except Exception as e:

            print("AI ERROR:", e)

            time.sleep(5)


if __name__ == "__main__":

    start_ai()
