import random

def generate_experiment():

    indicators = ["MA","RSI","MACD","BOLLINGER","ATR"]

    strategy = {

        "indicator_1": random.choice(indicators),
        "indicator_2": random.choice(indicators),
        "entry":"signal_cross",
        "exit":"reverse_signal"

    }

    return strategy
