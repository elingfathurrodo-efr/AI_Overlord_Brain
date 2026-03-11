def predict_impact(score):

    if score>=3:

        return "HIGH"

    if score==2:

        return "MEDIUM"

    return "LOW"
