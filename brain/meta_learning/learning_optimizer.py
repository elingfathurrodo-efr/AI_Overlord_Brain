def optimize_learning(score):

    if score < 50:

        return "INCREASE_EXPERIMENTS"

    if score < 100:

        return "ADJUST_PARAMETERS"

    return "LEARNING_OPTIMAL"
