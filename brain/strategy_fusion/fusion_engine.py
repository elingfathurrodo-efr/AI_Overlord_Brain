import random

def fuse_strategies(strategy_list):

    s1 = random.choice(strategy_list)

    s2 = random.choice(strategy_list)

    hybrid = {

        "strategy_A":s1["name"],
        "strategy_B":s2["name"],
        "mode":"HYBRID"

    }

    return hybrid
