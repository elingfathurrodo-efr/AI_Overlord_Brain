import time

from autonomous_loop.market_scanner import scan_market
from autonomous_loop.learning_cycle import learning_step
from autonomous_loop.evolution_cycle import evolution_step
from central_brain.central_core import central_brain


def run_ai_loop():

    while True:

        # scan kondisi market
        market_regime = scan_market()

        # mode risiko (sementara default)
        risk_mode = "NORMAL"

        # keputusan AI
        decision = central_brain(market_regime, risk_mode)

        print("Market:", market_regime)
        print("Decision:", decision)

        # AI belajar
        learning_step()

        # AI berevolusi
        evolution_step()

        # jeda siklus
        time.sleep(10)
