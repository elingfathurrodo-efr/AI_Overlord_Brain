import random

def crossover(genome1,genome2):

    child={}

    for key in genome1:

        child[key]=random.choice([genome1[key],genome2[key]])

    return child
