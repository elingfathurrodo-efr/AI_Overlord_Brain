import random

def build_indicator():

    indicators = [
        "EMA",
        "SMA",
        "RSI",
        "MACD",
        "ATR",
        "BOLLINGER"
    ]

    periods = [5,10,14,20,50,100]

    indicator = random.choice(indicators)
    period = random.choice(periods)

    return {
        "indicator": indicator,
        "period": period
    }
