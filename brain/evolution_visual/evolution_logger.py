import json
import time

log_file="../../dashboard/api/evolution.json"

def log_evolution(genome,score):

    node={

        "genome":genome,
        "score":score,
        "time":time.time()

    }

    try:

        with open(log_file,"r") as f:
            data=json.load(f)

    except:

        data=[]

    data.append(node)

    with open(log_file,"w") as f:
        json.dump(data,f,indent=2)

    print("Evolution logged")
