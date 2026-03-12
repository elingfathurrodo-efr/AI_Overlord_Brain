from strategy_creator.strategy_builder import build_strategy
from strategy_creator.strategy_tester import test_strategy


def create_strategy():

    strategy = build_strategy()

    result = test_strategy(strategy)

    return result
