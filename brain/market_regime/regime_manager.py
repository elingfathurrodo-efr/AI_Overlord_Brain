from market_regime.regime_detector import detect_regime


def get_market_mode(atr,ma_fast,ma_slow,spread):

    regime = detect_regime(atr,ma_fast,ma_slow,spread)

    if regime["volatility"] == "HIGH_VOLATILITY":
        return "VOLATILE_MARKET"

    if regime["trend"] == "UP_TREND":
        return "TREND_BUY"

    if regime["trend"] == "DOWN_TREND":
        return "TREND_SELL"

    if regime["liquidity"] == "LOW_LIQUIDITY":
        return "WAIT"

    return "RANGE_MARKET"
