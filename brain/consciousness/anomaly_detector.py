def detect_anomaly(state):

    if state["stress"] > 80:
        return "HIGH_STRESS"

    if state["energy"] < 10:
        return "LOW_ENERGY"

    return "NORMAL"
