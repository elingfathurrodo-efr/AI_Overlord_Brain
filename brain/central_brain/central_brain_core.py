from central_brain.market_reader import read_market
from central_brain.strategy_manager import choose_strategy
from central_brain.risk_manager import risk_control
from central_brain.decision_engine import make_decision


def central_brain(balance):

    market = read_market()

    strategy = choose_strategy(market["regime"])

    risk = risk_control(balance)

    decision = make_decision()

    return {

        "market":market,
        "strategy":strategy,
        "risk":risk,
        "decision":decision

    }
