import random

def combine_indicators():

    indicators = ["MA","RSI","MACD","BOLLINGER","ATR"]

    combo = random.sample(indicators,2)

    return combo
