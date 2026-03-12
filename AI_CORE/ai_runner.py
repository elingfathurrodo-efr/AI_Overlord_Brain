import time

from mt5_bridge.mt5_connector import connect
from mt5_bridge.market_reader import get_market_data
from mt5_bridge.trade_executor import buy

from brain.autonomous_loop.market_scanner import scan_market
from brain.autonomous_loop.learning_cycle import learning_step
from brain.autonomous_loop.evolution_cycle import evolution_step
from brain.central_brain.central_core import central_brain


def start_ai():

    print("=================================")
    print("AI OVERLORD SYSTEM STARTED")
    print("=================================")

    # connect MT5
    connect()

    while True:

        try:

            # read market
            market_data = get_market_data("EURUSD")

            if market_data:

                print("Market Data:", market_data)

            # scan market regime
            market_regime = scan_market()

            # risk mode
            risk_mode = "NORMAL"

            # AI decision
            decision = central_brain(market_regime, risk_mode)

            print("AI Decision:", decision)

            # simple example execution
            if decision == "BUY":

                result = buy("EURUSD", 0.01)

                print("Trade Result:", result)

            # learning
            learning_step()

            # evolution
            evolution_step()

            time.sleep(10)

        except Exception as e:

            print("ERROR:", e)

            time.sleep(5)


if __name__ == "__main__":

    start_ai()
