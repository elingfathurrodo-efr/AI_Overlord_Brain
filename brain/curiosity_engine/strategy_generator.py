import random

def generate_strategy():

    strategies = [

        {"type":"MA_CROSS","fast":20,"slow":50},
        {"type":"RSI","period":14,"overbought":70,"oversold":30},
        {"type":"BOLLINGER","period":20,"dev":2},
        {"type":"BREAKOUT","range":30}

    ]

    return random.choice(strategies)
