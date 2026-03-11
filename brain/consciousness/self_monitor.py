import json

state_file="organism_state.json"

def read_state():

    try:
        with open(state_file,"r") as f:
            data=json.load(f)
    except:
        data={
            "energy":100,
            "stress":10,
            "growth":1
        }

    return data
