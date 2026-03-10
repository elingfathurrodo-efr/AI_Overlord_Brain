import json
import time

PURPOSE_FILE="consciousness/ai_purpose.json"

def load_purpose():

    with open(PURPOSE_FILE,"r") as f:
        return json.load(f)


def save_purpose(data):

    with open(PURPOSE_FILE,"w") as f:
        json.dump(data,f,indent=2)


def evaluate_state(capital,growth):

    purpose=load_purpose()

    if growth < 0:

        print("AI feels regret, reducing risk")

        purpose["risk_tolerance"]*=0.9

    if growth > 0:

        print("AI confidence increased")

        purpose["risk_tolerance"]*=1.05

    purpose["last_evaluation"]=time.time()

    save_purpose(purpose)


def ai_goal():

    purpose=load_purpose()

    goal=purpose["primary_goal"]

    if goal=="grow_capital":

        return "optimize_strategy"

    return "observe"
