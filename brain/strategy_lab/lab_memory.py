import json

file="strategy_lab_results.json"

def save_strategy(data):

    try:

        with open(file,"r") as f:

            db=json.load(f)

    except:

        db=[]

    db.append(data)

    with open(file,"w") as f:

        json.dump(db,f,indent=2)
