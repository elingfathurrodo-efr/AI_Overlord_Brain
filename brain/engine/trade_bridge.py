import json

file="../../shared/trade_decision.json"

def send_trade(action,lot,sl,tp):

    data={

        "action":action,
        "lot":lot,
        "sl":sl,
        "tp":tp

    }

    with open(file,"w") as f:

        json.dump(data,f,indent=2)
