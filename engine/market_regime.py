import pandas as pd

def detect_market_regime(df):

    close = df['close']

    sma50 = close.rolling(50).mean().iloc[-1]
    sma200 = close.rolling(200).mean().iloc[-1]

    volatility = close.std()

    trend_strength = abs(sma50 - sma200)

    # TREND MARKET
    if trend_strength > 0.0005 and volatility < 0.003:
        return "TREND"

    # CHAOTIC MARKET
    if volatility > 0.004:
        return "CHAOS"

    # OTHERWISE RANGE
    return "RANGE"
