import json

file = "brain_state.json"


def load_state():

    try:
        with open(file,"r") as f:
            return json.load(f)

    except:

        return {

            "market_regime":"UNKNOWN",
            "active_strategy":"NONE",
            "risk_mode":"NORMAL",
            "ai_mode":"LEARNING"

        }


def save_state(data):

    with open(file,"w") as f:
        json.dump(data,f,indent=2)
