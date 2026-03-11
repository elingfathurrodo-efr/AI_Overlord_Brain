def select_strategy(regime):

    if regime=="TREND":

        return "EMA_STRATEGY"

    if regime=="TREND_VOLATILE":

        return "BREAKOUT_STRATEGY"

    if regime=="VOLATILE":

        return "SCALPING_STRATEGY"

    return "MEAN_REVERSION"
