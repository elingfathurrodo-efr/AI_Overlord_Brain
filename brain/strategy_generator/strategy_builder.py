import random
from strategy_generator.indicator_library import random_indicators


def build_strategy():

    indicators=random_indicators()

    strategy={

        "name":"_".join(indicators),

        "indicators":indicators,

        "risk":round(random.uniform(0.5,2.0),2)

    }

    return strategy
