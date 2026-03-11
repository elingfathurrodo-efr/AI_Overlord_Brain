import random

strategies = [
"RSI_EMA",
"MACD_BREAKOUT",
"EMA_TREND",
"SMC_STRATEGY",
"VOLATILITY_SCALP"
]

def generate_dna():

    dna = {
        "strategy": random.choice(strategies),
        "risk": round(random.uniform(0.5,2.0),2),
        "speed": random.randint(1,10)
    }

    return dna
