def detect_volatility(atr):

    if atr > 2:

        return "high"

    if atr < 0.8:

        return "low"

    return "normal"
