def check_trend(ma_fast, ma_slow):

    if ma_fast > ma_slow:
        return "UP_TREND"

    if ma_fast < ma_slow:
        return "DOWN_TREND"

    return "NO_TREND"
