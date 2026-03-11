def check_volatility(atr):

    if atr > 0.0030:
        return "EXTREME"

    if atr > 0.0020:
        return "HIGH"

    return "NORMAL"
