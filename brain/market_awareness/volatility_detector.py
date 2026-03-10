def detect_volatility(atr):

    if atr > 2.0:

        return "high"

    elif atr > 1.0:

        return "medium"

    else:

        return "low"
