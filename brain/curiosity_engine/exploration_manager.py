import random

strategies=[

"rsi_strategy",
"ema_strategy",
"macd_strategy",
"breakout_strategy",
"mean_reversion"

]

def explore_strategy():

    new_strategy=random.choice(strategies)

    print("AI exploring:",new_strategy)

    return new_strategy
