import random

indicators=[

"RSI",
"EMA",
"MACD",
"ATR",
"BREAKOUT",
"SMC",
"VWAP"

]

def random_indicators():

    return random.sample(indicators,3)
