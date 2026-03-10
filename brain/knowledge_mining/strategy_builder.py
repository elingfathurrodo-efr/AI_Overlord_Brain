import json

strategy_file="../genomes/genomes_archive.json"

def save_new_strategy(name,formula):

    strategy={

        "name":name,
        "formula":formula

    }

    try:

        with open(strategy_file,"r") as f:
            data=json.load(f)

    except:

        data=[]

    data.append(strategy)

    with open(strategy_file,"w") as f:
        json.dump(data,f,indent=2)

    print("New strategy discovered:",name)
