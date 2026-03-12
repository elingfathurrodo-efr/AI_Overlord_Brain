import json

file = "ai_growth.json"

def load_growth():

    try:
        with open(file,"r") as f:
            return json.load(f)

    except:
        return []

def save_growth(data):

    with open(file,"w") as f:
        json.dump(data,f,indent=2)
