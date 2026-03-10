import json
import random

GENOME_FILE="genome/genome_pool.json"

def load_genomes():

    with open(GENOME_FILE,"r") as f:
        data=json.load(f)

    return data


def save_genomes(data):

    with open(GENOME_FILE,"w") as f:
        json.dump(data,f,indent=2)


def mutate_genome(genome):

    genome["rsi_period"] += random.randint(-2,2)
    genome["ema_fast"] += random.randint(-5,5)
    genome["ema_slow"] += random.randint(-10,10)

    return genome


def evolve_population():

    data=load_genomes()

    for g in data["genomes"]:

        if random.random() < 0.3:
            mutate_genome(g)

    save_genomes(data)
