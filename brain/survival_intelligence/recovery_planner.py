def recovery_plan(drawdown):

    if drawdown > 25:

        return "FULL_RECOVERY_MODE"

    if drawdown > 15:

        return "SLOW_RECOVERY"

    if drawdown > 5:

        return "CAUTIOUS_GROWTH"

    return "NORMAL_GROWTH"
