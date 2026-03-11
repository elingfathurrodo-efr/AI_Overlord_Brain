from market_regime.volatility_analyzer import check_volatility
from market_regime.trend_analyzer import check_trend
from market_regime.liquidity_analyzer import check_liquidity


def detect_regime(atr,ma_fast,ma_slow,spread):

    vol = check_volatility(atr)

    trend = check_trend(ma_fast,ma_slow)

    liquidity = check_liquidity(spread)

    return {

        "volatility":vol,
        "trend":trend,
        "liquidity":liquidity

    }
