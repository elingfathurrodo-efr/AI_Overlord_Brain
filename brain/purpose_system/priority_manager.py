def priority_decision(drawdown):

    if drawdown > 20:

        return "SURVIVE"

    if drawdown > 10:

        return "PROTECT"

    return "EXPAND"
