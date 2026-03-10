import json
import time

STATE_FILE="mt5_bridge/bridge_state.json"
LOGIC_FILE="../shared/logic.json"


def load_state():

    with open(STATE_FILE,"r") as f:
        return json.load(f)


def save_state(data):

    with open(STATE_FILE,"w") as f:
        json.dump(data,f,indent=2)


def update_logic(strategy):

    try:

        with open(LOGIC_FILE,"r") as f:
            logic=json.load(f)

    except:

        logic={}

    logic["strategy"]=strategy
    logic["last_update"]=time.time()

    with open(LOGIC_FILE,"w") as f:
        json.dump(logic,f,indent=2)

    print("MT5 logic updated")


def sync_mt5():

    state=load_state()

    state["last_sync"]=time.time()
    state["status"]="synced"

    save_state(state)

    print("MT5 bridge synchronized")
