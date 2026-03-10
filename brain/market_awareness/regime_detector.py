def detect_regime(ema_fast, ema_slow):

    if ema_fast > ema_slow:

        return "uptrend"

    elif ema_fast < ema_slow:

        return "downtrend"

    else:

        return "sideways"
