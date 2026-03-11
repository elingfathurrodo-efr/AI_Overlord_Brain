import json

genome_file="genomes/genomes_active.json"

def load_genomes():

    try:

        with open(genome_file,"r") as f:

            data=json.load(f)

    except:

        data=[]

    return data


def save_genomes(data):

    with open(genome_file,"w") as f:

        json.dump(data,f,indent=2)
