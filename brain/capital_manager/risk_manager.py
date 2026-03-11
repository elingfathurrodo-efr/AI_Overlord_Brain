def calculate_risk(equity):

    if equity < 1000:
        return 0.01

    if equity < 5000:
        return 0.02

    if equity < 10000:
        return 0.03

    return 0.01
