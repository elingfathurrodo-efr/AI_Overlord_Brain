from strategy_creator.indicator_library import random_indicators


def build_strategy():

    indicators = random_indicators()

    strategy = {

        "indicator_1":indicators[0],
        "indicator_2":indicators[1],
        "entry_rule":"signal_cross",
        "exit_rule":"opposite_signal"

    }

    return strategy
