import random

def mutate_strategy(strategy):

    new_strategy = strategy.copy()

    mutation = random.choice(["risk","tp","sl"])

    if mutation == "risk":
        new_strategy["risk"] *= random.uniform(0.8,1.2)

    if mutation == "tp":
        new_strategy["tp"] *= random.uniform(0.9,1.3)

    if mutation == "sl":
        new_strategy["sl"] *= random.uniform(0.8,1.1)

    return new_strategy
