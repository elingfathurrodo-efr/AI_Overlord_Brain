import random

def crossover(parent1,parent2):

    child={}

    for key in parent1:

        child[key]=random.choice([parent1[key],parent2.get(key)])

    return child
