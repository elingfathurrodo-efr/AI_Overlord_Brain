import json

file="logs/entropy_log.json"

def save_entropy(entropy):

    try:
        with open(file,"r") as f:
            data=json.load(f)
    except:
        data=[]

    data.append(entropy)

    with open(file,"w") as f:
        json.dump(data,f,indent=2)
