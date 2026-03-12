import time

from brain.autonomous_loop.market_scanner import scan_market
from brain.autonomous_loop.learning_cycle import learning_step
from brain.autonomous_loop.evolution_cycle import evolution_step
from brain.central_brain.central_core import central_brain


def start_ai():

    print("=================================")
    print("AI OVERLORD SYSTEM STARTED")
    print("=================================")

    while True:

        try:

            # 1 scan market
            market_regime = scan_market()

            # 2 risk mode
            risk_mode = "NORMAL"

            # 3 AI decision
            decision = central_brain(market_regime, risk_mode)

            print("Market :", market_regime)
            print("Decision :", decision)

            # learning
            learning_step()

            # evolution
            evolution_step()

            time.sleep(10)

        except Exception as e:

            print("ERROR :", e)

            time.sleep(5)


if __name__ == "__main__":
    start_ai()
