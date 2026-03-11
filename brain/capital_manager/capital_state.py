import json

file="capital_state.json"

def load_state():

    try:

        with open(file,"r") as f:
            return json.load(f)

    except:

        return {

            "initial_capital":1000,
            "secured_profit":0

        }


def save_state(state):

    with open(file,"w") as f:
        json.dump(state,f,indent=2)
