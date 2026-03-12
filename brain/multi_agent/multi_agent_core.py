from multi_agent.market_agent import analyze_market
from multi_agent.strategy_agent import choose_strategy
from multi_agent.risk_agent import check_risk
from multi_agent.execution_agent import execute_trade
from multi_agent.evolution_agent import evolve_strategy


def run_multi_agent():

    market = analyze_market()

    strategy = choose_strategy(market)

    risk = check_risk(strategy)

    decision = execute_trade(strategy,risk)

    evolution = evolve_strategy(strategy)

    return {

        "market":market,
        "strategy":strategy,
        "risk":risk,
        "decision":decision,
        "evolution":evolution

    }
