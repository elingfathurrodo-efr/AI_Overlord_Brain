import json

file = "optimization_log.json"


def load_log():

    try:
        with open(file,"r") as f:
            return json.load(f)

    except:
        return []


def save_log(data):

    with open(file,"w") as f:
        json.dump(data,f,indent=2)
