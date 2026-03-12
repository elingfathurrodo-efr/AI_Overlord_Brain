import json

file = "learning_history.json"

def load_history():

    try:
        with open(file,"r") as f:
            return json.load(f)

    except:
        return []

def save_history(data):

    with open(file,"w") as f:
        json.dump(data,f,indent=2)
