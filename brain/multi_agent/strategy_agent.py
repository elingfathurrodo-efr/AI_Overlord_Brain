def choose_strategy(market_regime):

    if market_regime == "TREND":

        return "MACD_TREND"

    if market_regime == "RANGE":

        return "RSI_RANGE"

    return "BOLLINGER_BREAKOUT"
