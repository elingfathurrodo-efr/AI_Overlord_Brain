from governor.survival_rules import rules

def check_risk(drawdown,risk):

    if drawdown > rules["max_drawdown"]:

        return "STOP_TRADING"

    if risk > rules["max_risk_per_trade"]:

        return "REDUCE_RISK"

    return "OK"
