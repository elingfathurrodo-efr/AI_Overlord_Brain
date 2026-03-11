import json

file="results/strategy_scores.json"

def record_performance(strategy,profit):

    try:
        with open(file,"r") as f:
            data=json.load(f)
    except:
        data=[]

    data.append({

        "strategy":strategy,
        "profit":profit

    })

    with open(file,"w") as f:
        json.dump(data,f,indent=2)
