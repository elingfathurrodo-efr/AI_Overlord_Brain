import random

def test_experiment(strategy):

    winrate = random.randint(35,70)

    profit = random.randint(-100,300)

    drawdown = random.randint(5,30)

    return {

        "strategy":strategy,
        "winrate":winrate,
        "profit":profit,
        "drawdown":drawdown

    }
