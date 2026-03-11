import random

def test_strategy(strategy):

    profit=random.uniform(-5,10)

    drawdown=random.uniform(0,5)

    score=profit-drawdown

    return{

        "profit":profit,
        "drawdown":drawdown,
        "score":score

    }
