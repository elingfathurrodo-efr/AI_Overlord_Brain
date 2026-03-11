def detect_error(result):

    if result["drawdown"] > 20:
        return True

    if result["profit"] < -10:
        return True

    return False
