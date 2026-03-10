import json

STATE_FILE="capital/capital_state.json"

def load_state():

    with open(STATE_FILE,"r") as f:
        return json.load(f)


def save_state(data):

    with open(STATE_FILE,"w") as f:
        json.dump(data,f,indent=2)


def evaluate_capital(balance):

    state=load_state()

    checkpoint=state["last_checkpoint"]

    # jika balance sudah 2x
    if balance >= checkpoint * 2:

        profit=balance - checkpoint

        saved=profit * 0.5

        state["saved_profit"] += saved

        state["last_checkpoint"]=balance

        state["risk_level"]=1.2

        print("Capital milestone reached")

        print("Saved profit:",saved)

    # jika drawdown besar
    if balance < checkpoint * 0.7:

        state["risk_level"]=0.5

        print("Drawdown detected - reducing risk")

    save_state(state)

    return state
