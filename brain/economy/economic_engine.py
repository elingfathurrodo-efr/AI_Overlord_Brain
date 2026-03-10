import json
import random

STATE_FILE="economy/economic_state.json"


def load_state():

    with open(STATE_FILE,"r") as f:
        return json.load(f)


def save_state(data):

    with open(STATE_FILE,"w") as f:
        json.dump(data,f,indent=2)


def analyze_market_conditions():

    state = load_state()

    # simulasi analisa volatilitas
    volatility = random.randint(1,5)

    if volatility >= 4:

        state["market_mode"] = "VOLATILE"

    elif volatility == 3:

        state["market_mode"] = "AGGRESSIVE"

    elif volatility == 2:

        state["market_mode"] = "NORMAL"

    else:

        state["market_mode"] = "SAFE"

    state["volatility_level"] = volatility

    save_state(state)

    return state
