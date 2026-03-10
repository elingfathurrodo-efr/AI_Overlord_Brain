import json
import random
import time

STATE_FILE="global_intelligence/market_state.json"


def load_state():

    with open(STATE_FILE,"r") as f:
        return json.load(f)


def save_state(data):

    with open(STATE_FILE,"w") as f:
        json.dump(data,f,indent=2)


def analyze_market():

    state=load_state()

    volatility=random.choice(["low","normal","high"])
    regime=random.choice(["trend","sideways","chaos"])

    state["volatility"]=volatility
    state["market_regime"]=regime
    state["last_update"]=time.time()

    if volatility=="high":
        state["risk_level"]=0.5
    else:
        state["risk_level"]=1.0

    save_state(state)

    print("Market regime:",regime)
    print("Volatility:",volatility)
