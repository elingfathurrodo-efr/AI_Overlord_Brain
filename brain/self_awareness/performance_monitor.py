def evaluate_performance(profit,drawdown):

    score = profit - (drawdown * 2)

    return score
