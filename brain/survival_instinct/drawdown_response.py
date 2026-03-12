def drawdown_action(drawdown):

    if drawdown > 20:
        return "STOP_TRADING"

    if drawdown > 10:
        return "REDUCE_RISK"

    return "NORMAL"
