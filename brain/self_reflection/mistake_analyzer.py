def analyze_mistake(trade):

    if trade["profit"] < 0:

        if trade["market_regime"] == "RANGE":

            return "TREND_STRATEGY_IN_RANGE"

        if trade["market_regime"] == "VOLATILE":

            return "VOLATILITY_MISREAD"

        return "STRATEGY_ERROR"

    return "GOOD_DECISION"
