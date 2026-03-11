def analyze_market(trend,volatility,retrace):

    if trend > 70 and volatility > 60:
        return "STRONG_TREND"

    if retrace > 50:
        return "RETRACEMENT"

    if volatility > 80:
        return "BREAKOUT"

    return "UNCLEAR"
