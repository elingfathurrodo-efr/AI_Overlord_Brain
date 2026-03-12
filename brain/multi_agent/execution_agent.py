def execute_trade(strategy,risk):

    if risk == "HIGH":

        return "NO_TRADE"

    return f"EXECUTE_{strategy}"
