import json

TRAUMA_FILE = "memory/trauma_memory.json"

def load_trauma():

    with open(TRAUMA_FILE,"r") as f:
        data=json.load(f)

    return data

def record_trauma(event):

    data=load_trauma()

    data["traumas"].append(event)

    with open(TRAUMA_FILE,"w") as f:
        json.dump(data,f,indent=2)
