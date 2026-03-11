import random

def create_genome():

    genome = {

        "ma_fast": random.randint(5,50),

        "ma_slow": random.randint(50,200),

        "rsi_period": random.randint(7,21),

        "rsi_overbought": random.randint(65,80),

        "rsi_oversold": random.randint(20,35)

    }

    return genome
