import json
import random
import time

POOL="strategy_lab/strategy_pool.json"
SCORES="strategy_lab/strategy_scores.json"

indicators=[
"RSI",
"EMA",
"MACD",
"Bollinger",
"ATR",
"Stochastic"
]


def load(path):

    with open(path,"r") as f:
        return json.load(f)


def save(path,data):

    with open(path,"w") as f:
        json.dump(data,f,indent=2)


def create_strategy():

    ind1=random.choice(indicators)
    ind2=random.choice(indicators)

    strategy={
        "time":time.time(),
        "logic":f"{ind1} + {ind2}"
    }

    pool=load(POOL)

    pool["strategies"].append(strategy)

    save(POOL,pool)

    print("New strategy created:",strategy["logic"])

    return strategy


def score_strategy(strategy):

    score=random.uniform(-1,1)

    data=load(SCORES)

    entry={
        "time":time.time(),
        "strategy":strategy["logic"],
        "score":score
    }

    data["scores"].append(entry)

    save(SCORES,data)

    print("Strategy score:",score)
