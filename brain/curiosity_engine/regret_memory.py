import json

file="memory/regret_memory.json"

def record_regret(strategy):

    try:

        with open(file,"r") as f:
            data=json.load(f)

    except:

        data=[]

    data.append(strategy)

    with open(file,"w") as f:
        json.dump(data,f,indent=2)

    print("AI learned regret:",strategy)
