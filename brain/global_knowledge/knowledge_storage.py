import json

file = "knowledge_db.json"

def load_knowledge():

    try:

        with open(file,"r") as f:
            return json.load(f)

    except:

        return []


def save_knowledge(data):

    with open(file,"w") as f:
        json.dump(data,f,indent=2)
