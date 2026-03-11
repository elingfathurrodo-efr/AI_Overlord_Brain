import json

file="genomes/genomes_active.json"

def save_strategy(strategy):

    try:

        with open(file,"r") as f:

            data=json.load(f)

    except:

        data=[]

    data.append(strategy)

    with open(file,"w") as f:

        json.dump(data,f,indent=2)
