import json

file="experiments.json"

def save_experiment(exp):

    try:

        with open(file,"r") as f:
            data=json.load(f)

    except:

        data=[]

    data.append(exp)

    with open(file,"w") as f:
        json.dump(data,f,indent=2)
