def select_strategy(regime,volatility):

    if regime=="uptrend":

        return "trend_following"

    if regime=="downtrend":

        return "trend_sell"

    if regime=="sideways" and volatility=="low":

        return "mean_reversion"

    if volatility=="high":

        return "breakout"

    return "safe_mode"
