import json

file="trauma_memory.json"

def save_trauma(event):

    try:
        with open(file,"r") as f:
            data=json.load(f)

    except:
        data=[]

    data.append(event)

    with open(file,"w") as f:
        json.dump(data,f,indent=2)
