def analyze_trade(profit):

    if profit > 0:
        return "SUCCESS"

    if profit < 0:
        return "LOSS"

    return "BREAKEVEN"
