def override_decision(signal,anomaly):

    if anomaly=="HIGH_STRESS":
        return "NO_TRADE"

    if anomaly=="LOW_ENERGY":
        return "WAIT"

    return signal
