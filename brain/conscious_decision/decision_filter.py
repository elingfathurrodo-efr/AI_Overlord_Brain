def filter_decision(risk_level):

    if risk_level == "HIGH":

        return "WAIT"

    if risk_level == "MEDIUM":

        return "SMALL_TRADE"

    return "TRADE"
