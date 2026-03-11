import random

def should_evolve():

    chance=random.random()

    if chance>0.6:

        return True

    return False
