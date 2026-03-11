def check_volatility(atr):

    if atr > 0.0020:
        return "HIGH_VOLATILITY"

    if atr < 0.0005:
        return "LOW_VOLATILITY"

    return "NORMAL_VOLATILITY"
