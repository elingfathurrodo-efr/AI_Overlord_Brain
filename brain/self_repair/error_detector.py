def detect_error(drawdown,system_state):

    if drawdown > 30:

        return "critical"

    if system_state == "crash":

        return "critical"

    if drawdown > 15:

        return "warning"

    return "normal"
