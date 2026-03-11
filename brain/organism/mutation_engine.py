import random

def mutate_dna(dna):

    dna["risk"] += random.uniform(-0.2,0.2)

    dna["speed"] += random.randint(-1,1)

    return dna
