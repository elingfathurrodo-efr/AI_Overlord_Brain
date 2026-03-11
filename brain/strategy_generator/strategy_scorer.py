import random

def score_strategy(strategy):

    score=random.uniform(0,1)

    strategy["score"]=round(score,2)

    return strategy
