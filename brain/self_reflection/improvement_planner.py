def plan_improvement(mistake):

    if mistake == "TREND_STRATEGY_IN_RANGE":

        return "USE_RANGE_STRATEGY"

    if mistake == "VOLATILITY_MISREAD":

        return "INCREASE_VOLATILITY_FILTER"

    if mistake == "STRATEGY_ERROR":

        return "ADJUST_STRATEGY_PARAMETERS"

    return "NO_CHANGE"
