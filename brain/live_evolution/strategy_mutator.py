import random

def mutate_strategy(strategy):

    mutation=random.choice([

        "increase_speed",
        "reduce_risk",
        "add_filter",
        "change_indicator"

    ])

    return {

        "base":strategy,
        "mutation":mutation

    }
