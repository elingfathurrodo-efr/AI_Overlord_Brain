import json

file="memory/regret_memory.json"

def load_mistakes():

    try:
        with open(file,"r") as f:
            return json.load(f)
    except:
        return []
