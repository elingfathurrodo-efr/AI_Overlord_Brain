import random

indicators = [

    "MA",
    "RSI",
    "MACD",
    "BOLLINGER",
    "ATR",
    "STOCHASTIC"

]

def random_indicators():

    return random.sample(indicators,2)
