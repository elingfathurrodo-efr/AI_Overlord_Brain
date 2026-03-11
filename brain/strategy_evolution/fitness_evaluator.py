def evaluate_strategy(winrate,profit,drawdown):

    score = (winrate*2)+(profit*0.5)-(drawdown*1.5)

    return score
