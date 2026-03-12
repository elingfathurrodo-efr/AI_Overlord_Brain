import json

file = "awareness_state.json"


def load_state():

    try:
        with open(file,"r") as f:
            return json.load(f)

    except:

        return {

            "profit_growth":0,
            "drawdown":0,
            "evolution_count":0,
            "strategy_score":0

        }


def save_state(data):

    with open(file,"w") as f:
        json.dump(data,f,indent=2)
