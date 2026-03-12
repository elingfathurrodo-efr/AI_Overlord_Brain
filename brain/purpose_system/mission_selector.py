def select_mission(market_state):

    if market_state == "TREND":
        return "GROW_CAPITAL"

    if market_state == "VOLATILE":
        return "OPPORTUNITY_HUNT"

    if market_state == "RANGE":
        return "SAFE_TRADING"

    return "OBSERVE"
