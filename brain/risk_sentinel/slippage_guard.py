def check_slippage(slippage):

    if slippage > 10:
        return "DANGER"

    if slippage > 5:
        return "WARNING"

    return "SAFE"
