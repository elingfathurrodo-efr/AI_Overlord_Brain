def select_strategy(strategies,market_regime):

    for s in strategies:

        if s["type"] == market_regime:

            return s

    return strategies[0]
