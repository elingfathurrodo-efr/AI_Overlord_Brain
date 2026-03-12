def select_best(result):

    score = result["winrate"]*2 + result["profit"] - result["drawdown"]*3

    if score > 150:

        return "PROMOTE_STRATEGY"

    if score > 50:

        return "KEEP_TESTING"

    return "REJECT"
