def evaluate_performance(winrate,profit,drawdown):

    score = (winrate*2) + profit - (drawdown*3)

    return score
