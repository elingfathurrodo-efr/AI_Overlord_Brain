import json

file="results/evolution_generation.json"

def update_generation():

    try:
        with open(file,"r") as f:
            data=json.load(f)
    except:
        data={"generation":0}

    data["generation"]+=1

    with open(file,"w") as f:
        json.dump(data,f,indent=2)

    return data["generation"]
