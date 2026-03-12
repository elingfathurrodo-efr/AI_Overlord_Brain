def trading_decision(strategy,risk_mode):

    if risk_mode == "STOP":

        return "NO_TRADE"

    if strategy == "NONE":

        return "WAIT"

    return "TRADE"
