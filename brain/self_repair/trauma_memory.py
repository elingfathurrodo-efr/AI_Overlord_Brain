import json

file="memory/trauma_memory.json"

def record_trauma(reason):

    try:

        with open(file,"r") as f:
            data=json.load(f)

    except:
        data=[]

    data.append(reason)

    with open(file,"w") as f:
        json.dump(data,f,indent=2)

    print("Trauma recorded:",reason)
