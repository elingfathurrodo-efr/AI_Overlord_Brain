import json

file="memory/knowledge.json"

def read_knowledge():

    try:
        with open(file,"r") as f:
            data=json.load(f)
    except:
        data={"known":50,"unknown":50}

    return data
