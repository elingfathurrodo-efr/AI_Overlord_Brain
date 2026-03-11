def detect_regime(trend,volatility):

    if trend=="trend" and volatility=="high":

        return "TREND_VOLATILE"

    if trend=="trend":

        return "TREND"

    if volatility=="high":

        return "VOLATILE"

    return "SIDEWAYS"
