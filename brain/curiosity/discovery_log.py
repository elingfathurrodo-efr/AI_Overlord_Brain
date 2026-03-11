import json

file="results/discoveries.json"

def save_discovery(exp):

    try:

        with open(file,"r") as f:

            data=json.load(f)

    except:

        data=[]

    data.append(exp)

    with open(file,"w") as f:

        json.dump(data,f,indent=2)
