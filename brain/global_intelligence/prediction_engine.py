import random

def predict_market():

    predictions = [

        "TREND_CONTINUE",
        "TREND_REVERSAL",
        "RANGE_FORMING",
        "VOLATILITY_EXPANSION"

    ]

    return random.choice(predictions)
