import random
from strategy_lab.indicator_builder import build_indicator

def combine_strategy():

    indicators=[]

    count=random.randint(2,4)

    for i in range(count):

        indicators.append(build_indicator())

    strategy={

        "indicators":indicators,
        "entry_rule":"combined_signal",
        "exit_rule":"reverse_signal"

    }

    return strategy
