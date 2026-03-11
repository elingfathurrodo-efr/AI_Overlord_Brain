def capital_protection(balance,equity):

    ratio = equity / balance

    if ratio < 0.5:

        return "CAPITAL_PROTECTION"

    return "NORMAL"
