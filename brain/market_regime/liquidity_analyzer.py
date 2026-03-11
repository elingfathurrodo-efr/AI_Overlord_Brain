def check_liquidity(spread):

    if spread > 30:
        return "LOW_LIQUIDITY"

    if spread < 10:
        return "HIGH_LIQUIDITY"

    return "NORMAL_LIQUIDITY"
