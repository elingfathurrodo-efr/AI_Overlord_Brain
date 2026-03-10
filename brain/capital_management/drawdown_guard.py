def check_drawdown(balance,equity):

    dd = ((balance-equity)/balance)*100

    if dd > 20:

        return "danger"

    elif dd > 10:

        return "warning"

    else:

        return "safe"
