import json

file="memory/regret_memory.json"

def record_regret(data):

    try:
        with open(file,"r") as f:
            regrets=json.load(f)
    except:
        regrets=[]

    regrets.append(data)

    with open(file,"w") as f:
        json.dump(regrets,f,indent=2)
