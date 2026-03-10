import json
import random

STATE_FILE="market_sensor/market_state.json"


def load_state():

    with open(STATE_FILE,"r") as f:
        return json.load(f)


def save_state(data):

    with open(STATE_FILE,"w") as f:
        json.dump(data,f,indent=2)


def analyze_market():

    state=load_state()

    spread=random.uniform(0.5,3.0)
    volatility=random.randint(1,5)
    trend=random.randint(1,5)

    state["spread"]=spread
    state["volatility"]=volatility
    state["trend_strength"]=trend

    if spread>2.5:

        state["market_mode"]="SAFE"

    elif volatility>=4:

        state["market_mode"]="BREAKOUT"

    elif trend>=4:

        state["market_mode"]="TREND"

    else:

        state["market_mode"]="SCALPING"

    save_state(state)

    return state
