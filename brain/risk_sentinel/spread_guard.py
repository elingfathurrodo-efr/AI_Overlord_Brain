def check_spread(spread):

    if spread > 30:
        return "DANGER"

    if spread > 20:
        return "WARNING"

    return "SAFE"
