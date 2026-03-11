from organism.dna_generator import generate_dna
from organism.mutation_engine import mutate_dna
from organism.selection_engine import select_best
from organism.reproduction_engine import reproduce
import random

def evolve():

    population=[]

    for i in range(10):

        dna=generate_dna()

        dna["score"]=random.uniform(-1,1)

        population.append(dna)

    best=select_best(population)

    child=reproduce(best[0],best[1])

    child=mutate_dna(child)

    return child
