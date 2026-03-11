def check_drawdown(balance,equity):

    dd = (balance-equity)/balance*100

    if dd > 20:
        return "CRITICAL"

    if dd > 10:
        return "WARNING"

    return "SAFE"
