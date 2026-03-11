def detect_trend(ema_fast,ema_slow):

    if ema_fast > ema_slow:

        return "trend"

    if ema_fast < ema_slow:

        return "downtrend"

    return "sideways"
