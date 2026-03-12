import json

file="purpose_state.json"

def load_purpose():

    try:
        with open(file,"r") as f:
            return json.load(f)

    except:

        return {

            "main_goal":"STABLE_GROWTH",

            "risk_priority":"CAP
