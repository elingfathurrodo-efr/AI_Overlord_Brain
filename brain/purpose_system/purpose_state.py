import json

file = "purpose_state.json"


def load_purpose():

    try:
        with open(file,"r") as f:
            return json.load(f)

    except:

        return {

            "main_goal":"STABLE_GROWTH",
            "risk_priority":"CAPITAL_PROTECTION",
            "evolution_mode":"ADAPTIVE"

        }


def save_purpose(data):

    with open(file,"w") as f:
        json.dump(data,f,indent=2)
