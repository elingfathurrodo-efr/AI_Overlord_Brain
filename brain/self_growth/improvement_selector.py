def select_improvement(score):

    if score < 0:

        return "MAJOR_STRATEGY_CHANGE"

    if score < 50:

        return "PARAMETER_OPTIMIZATION"

    return "STABLE_CONTINUE"
