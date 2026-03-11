import random

def mutate(genome):

    key = random.choice(list(genome.keys()))

    genome[key] += random.randint(-5,5)

    return genome
