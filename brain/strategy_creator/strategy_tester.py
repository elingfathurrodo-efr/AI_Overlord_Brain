import random


def test_strategy(strategy):

    winrate = random.randint(40,70)

    profit = random.randint(-50,200)

    drawdown = random.randint(5,25)

    return {

        "strategy":strategy,
        "winrate":winrate,
        "profit":profit,
        "drawdown":drawdown

    }
