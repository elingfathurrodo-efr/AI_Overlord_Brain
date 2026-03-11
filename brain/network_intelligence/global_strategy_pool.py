import json

file="global_strategy_pool.json"

def store_strategy(data):

    try:

        with open(file,"r") as f:

            db=json.load(f)

    except:

        db=[]

    db.append(data)

    with open(file,"w") as f:

        json.dump(db,f,indent=2)
