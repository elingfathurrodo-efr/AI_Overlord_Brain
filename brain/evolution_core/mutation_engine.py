import random

def mutate_strategy(strategy):

    mutation=random.choice([

        "increase_rsi",
        "decrease_rsi",
        "change_ema",
        "add_filter"

    ])

    strategy["mutation"]=mutation

    return strategy
