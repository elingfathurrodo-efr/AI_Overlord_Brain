def choose_mode(danger_level):

    if danger_level == "CRITICAL":
        return "STOP_TRADING"

    if danger_level == "LOSS_SPIRAL":
        return "PAUSE_AND_ANALYZE"

    if danger_level == "HIGH_VOLATILITY":
        return "LOW_RISK_MODE"

    if danger_level == "WARNING":
        return "DEFENSIVE_TRADING"

    return "NORMAL_TRADING"
