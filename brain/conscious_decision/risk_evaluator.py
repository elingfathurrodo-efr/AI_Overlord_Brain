def evaluate_risk(prediction):

    if prediction == "TREND_REVERSAL":

        return "HIGH"

    if prediction == "VOLATILITY_EXPANSION":

        return "MEDIUM"

    return "LOW"
